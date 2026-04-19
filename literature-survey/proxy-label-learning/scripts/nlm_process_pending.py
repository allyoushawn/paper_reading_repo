#!/usr/bin/env python3
"""Process nlm:pending papers for proxy-label-learning survey (NotebookLM + markdown)."""

from __future__ import annotations

import argparse
import re
import time
from datetime import date
from pathlib import Path

from notebooklm_tools.mcp.tools._utils import get_client
from notebooklm_tools.services import chat as chat_service
from notebooklm_tools.services import notebooks as notebooks_service
from notebooklm_tools.services import sources as sources_service
from notebooklm_tools.services.errors import ServiceError

MAIN_NB = "6fbcf9e6-3833-4660-8b56-67b0b98bf394"
TOPIC_SLUG = "proxy-label-learning"
SURVEY_DIR = Path(__file__).resolve().parents[1]
QUEUE_PATH = SURVEY_DIR / "queue.md"
STATE_PATH = SURVEY_DIR / "notebooklm-state.md"
READ_PAPERS = SURVEY_DIR / "read-papers"
AWESOME = Path(
    "/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising"
)
KD_PDF = AWESOME / "03_Ranking/Transfer_Learning/2014 (Google) (NIPS) [Knoledge Distillation] Distilling the Knowledge in a Neural Network.pdf"
MAL_PDF = AWESOME / (
    "03_Ranking/Multi-task/2025 （Alibaba) (CIKM) [MAL] See Beyond a Single View - "
    "Multi-Attribution Learning Leads to Better Conversion Rate Prediction.pdf"
)

Q1 = """For the paper in this source, provide all of the following clearly labeled:
(1) Core problem and key contribution
(2) Proposed method or architecture in detail
(3) Datasets used for evaluation and comparison baselines"""

Q2 = """For the paper in this source, provide all of the following clearly labeled:
(1) Key quantitative results and improvements over baselines
(2) Limitations, failure modes, or negative results noted by the authors
(3) Top 5–7 most heavily cited prior works named in the related work or introduction"""


def refuse_cleanup(text: str) -> str:
    if not text:
        return "Not specified in source."
    low = text.lower()
    if any(
        x in low
        for x in (
            "i cannot",
            "cannot answer",
            "not mentioned in the source",
            "don't have enough information",
            "do not have enough information",
            "unable to find",
        )
    ):
        return "Not specified in source."
    return text


def parse_tail_meta(line: str) -> tuple[str, str, int]:
    """Return (source_field, relevance, priority_int)."""
    rel = "Core"
    pr = 2
    if "Relevance: Related" in line:
        rel = "Related"
    elif "Relevance: Peripheral" in line:
        rel = "Peripheral"
    dem = re.search(r"→\s*Priority\s*(\d+)", line)
    if dem:
        pr = int(dem.group(1))
    elif "Priority 3" in line:
        pr = 3
    elif "Priority 1" in line:
        pr = 1
    elif "Priority 4" in line:
        pr = 4
    m = re.search(r"Source:\s*([^|]+)", line)
    src = m.group(1).strip() if m else "web-search"
    return src, rel, pr


def infer_venue_year(title: str) -> tuple[str, str]:
    m = re.search(r"\(([A-Za-z]+)[\s,]*(\d{4})\)\s*$", title)
    if m:
        return m.group(1), m.group(2)
    m2 = re.search(r"\((\d{4})\)\s*$", title)
    if m2:
        return "arXiv", m2.group(1)
    m3 = re.search(r"(\d{4})\)", title)
    if m3:
        return "arXiv", m3.group(1)
    return "arXiv", "NA"


def method_slug(title: str) -> str:
    if ":" in title:
        return re.sub(r"[^A-Za-z0-9]+", "", title.split(":")[0])[:24] or "NA"
    if "(" in title:
        inner = title.split("(")[-1].split(")")[0]
        tok = inner.replace(",", " ").split()
        for t in tok:
            if t.isupper() and len(t) >= 2:
                return t
    return "NA"


def title_slug(title: str, max_words: int = 6) -> str:
    t = re.sub(r"\([^)]*\)", "", title)
    words = re.findall(r"[A-Za-z0-9]+", t)
    return "-".join(words[:max_words])


def build_filename(title: str, link: str) -> str:
    venue, year = infer_venue_year(title)
    if venue == "Google" and "2024" in title:
        venue, year = "arXiv", "2024"
    meth = method_slug(title)
    slug = title_slug(title)
    return f"{year}_{venue}_{meth}_{slug}.md"


def resolve_source(title: str, link: str) -> tuple[str, str | None]:
    """Returns (source_type, url_or_none). file_path passed separately."""
    if "See Beyond a Single View" in title:
        return "file", str(MAL_PDF)
    if "Distilling the Knowledge in a Neural Network" in title and KD_PDF.exists():
        return "file", str(KD_PDF)
    if link.startswith("http"):
        return "url", link
    if link.startswith("local-awesome-repo"):
        raise ValueError(f"No file mapping for {title!r} ({link})")
    raise ValueError(f"Unsupported link {link!r} for {title!r}")


def parse_pending_queue() -> list[dict]:
    rows: list[dict] = []
    text = QUEUE_PATH.read_text(encoding="utf-8")
    for line in text.splitlines():
        line = line.rstrip()
        if not line.startswith("- ") or "nlm:pending" not in line:
            continue
        rest = line[2:]
        parts = [p.strip() for p in rest.split(" | ")]
        title = parts[0]
        link = parts[1] if len(parts) > 1 else ""
        src, rel, pr = parse_tail_meta(line)
        rows.append(
            {
                "queue_line": line,
                "title": title,
                "link": link,
                "source": src,
                "relevance": rel,
                "priority": pr,
            }
        )
    return rows


def count_sources(client, notebook_id: str) -> int:
    data = notebooks_service.get_notebook(client, notebook_id)
    return int(data.get("source_count", 0))


def ensure_active_notebook(client, active: str, overflow_ids: list[str]) -> tuple[str, list[str]]:
    """Google AI Pro tier: overflow only near 300-source cap (see literature-survey-nlm SKILL)."""
    n = count_sources(client, active)
    if n < 290:
        return active, overflow_ids
    title = f"{TOPIC_SLUG}-overflow-{len(overflow_ids) + 1}"
    created = notebooks_service.create_notebook(client, title)
    new_id = created["notebook_id"]
    overflow_ids.append(new_id)
    append_state_overflow(title, new_id)
    return new_id, overflow_ids


def append_state_overflow(title: str, nb_id: str) -> None:
    lines = STATE_PATH.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    inserted = False
    for line in lines:
        out.append(line)
        if line.strip() == "overflow_notebooks:" and not inserted:
            out.append(f"  - {title}: {nb_id}")
            inserted = True
    if not inserted:
        out.append(f"  - {title}: {nb_id}")
    STATE_PATH.write_text("\n".join(out) + "\n", encoding="utf-8")


def move_queue_to_done(
    queue_line: str, md_name: str, source_id: str, *, link: str | None = None
) -> None:
    text = QUEUE_PATH.read_text(encoding="utf-8")
    lines = text.splitlines()
    new_lines: list[str] = []
    removed = False
    qn = queue_line.strip()
    for line in lines:
        sn = line.strip()
        match_exact = sn == qn
        match_fallback = (
            not match_exact
            and bool(link)
            and "nlm:pending" in sn
            and link in sn
        )
        if not removed and (match_exact or match_fallback):
            removed = True
            continue
        new_lines.append(line)
    if not removed:
        raise RuntimeError("queue line not found for removal")
    done_idx = None
    for i, line in enumerate(new_lines):
        if line.strip() == "## Done":
            done_idx = i
            break
    if done_idx is None:
        raise RuntimeError("## Done not found")
    short_title = queue_line.split(" | ")[0].removeprefix("- ").strip()
    entry = f"- {md_name} | {short_title} | {date.today().isoformat()} | nlm:{source_id}"
    insert_at = done_idx + 1
    while insert_at < len(new_lines) and new_lines[insert_at].startswith("- "):
        insert_at += 1
    new_lines.insert(insert_at, entry)
    QUEUE_PATH.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


def write_markdown(
    path: Path,
    *,
    title: str,
    link: str,
    source_id: str,
    relevance: str,
    priority: int,
    a1: str,
    a2: str,
    brief: bool,
) -> None:
    today = date.today().isoformat()
    venue, year = infer_venue_year(title)
    if brief:
        body = (
            f"## Summary\n\n{refuse_cleanup(a1)[:2200]}\n\n"
            f"{refuse_cleanup(a2)[:1800]}\n"
        )
    else:
        body = f"""## Contribution, method, and experimental setup (NLM Q1)

{refuse_cleanup(a1)}

## Results, limitations, and prior work (NLM Q2)

{refuse_cleanup(a2)}

## Relevance to Proxy Label Learning

This work informs supervised learning when training targets are **proxy or surrogate labels** (e.g., attribution-derived continuous scores rather than direct measurements of the deployment objective). Compare the paper's assumptions about label noise structure (systematic vs. random; instance-dependent vs. class-conditional) to Shapley-style credit assignments used as training signals.

## Method Tracker Update

- Add or increment counts for primary method and baselines named in this paper (see `method-tracker.md`).
"""
    content = f"""Date: {today}
Source: {link if link.startswith("http") else "local PDF"}
NLM Source ID: {source_id}
Venue: {venue} {year}
Relevance: {relevance}
Priority: {priority}

# {title}

**Authors:** Not specified in source.
**Affiliation:** Not specified in source.

{body}
"""
    path.write_text(content, encoding="utf-8")


def process_one(client, row: dict, notebook_id: str) -> tuple[str, str]:
    title = row["title"]
    link = row["link"]
    stype, loc = resolve_source(title, link)
    brief = row["priority"] >= 3
    if stype == "url":
        res = sources_service.add_source(
            client,
            notebook_id,
            "url",
            url=loc,
            wait=True,
            wait_timeout=180.0,
        )
    else:
        res = sources_service.add_source(
            client,
            notebook_id,
            "file",
            file_path=loc,
            wait=True,
            wait_timeout=240.0,
        )
    sid = res["source_id"]
    r1 = chat_service.query(client, notebook_id, Q1, source_ids=[sid], conversation_id=None)
    r2 = chat_service.query(client, notebook_id, Q2, source_ids=[sid], conversation_id=None)
    fname = build_filename(title, link or "")
    out_path = READ_PAPERS / fname
    write_markdown(
        out_path,
        title=title,
        link=link or loc,
        source_id=sid,
        relevance=row["relevance"],
        priority=row["priority"],
        a1=r1["answer"],
        a2=r2["answer"],
        brief=brief,
    )
    return fname, sid


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=3, help="Max papers to process this run")
    ap.add_argument("--start", type=int, default=0, help="Skip first N pending rows")
    args = ap.parse_args()
    client = get_client()
    pending = parse_pending_queue()
    sel = pending[args.start : args.start + args.limit]
    if not sel:
        print("No pending rows in range.")
        return
    active = MAIN_NB
    overflow: list[str] = []
    for row in sel:
        active, overflow = ensure_active_notebook(client, active, overflow)
        print("Processing:", row["title"][:70], "... notebook", active)
        try:
            md_name, sid = process_one(client, row, active)
        except Exception as e:
            print("FAILED:", row["title"], e)
            continue
        move_queue_to_done(row["queue_line"], md_name, sid, link=row.get("link") or "")
        print("  ->", md_name, sid)
        time.sleep(2)


if __name__ == "__main__":
    main()
