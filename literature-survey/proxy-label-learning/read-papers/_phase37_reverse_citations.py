#!/usr/bin/env python3
"""
Phase 3.7: build reverse citation maps across read-papers/*.md
Run from read-papers/: python3 _phase37_reverse_citations.py
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path


SECTION_HEADER = "## Papers That Mention This Paper (Reverse Citation Map)"
TABLE_HEADER = "| Mentioning Paper | Mention Context | Summary of Original Wording |"
TABLE_SEP = "| --- | --- | --- |"
EMPTY_NOTE = "*(no cross-links to other read-papers notes detected)*"


def norm_ws(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = s.lower()
    s = re.sub(r"\s+", " ", s).strip()
    return s


# Titles so short/common that a substring hit needs corroboration (author / venue / year cue).
AMBIGUOUS_TITLE_SUBSTRINGS: set[str] = {
    norm_ws("Learning with Noisy Labels"),
}


def strip_md(s: str) -> str:
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
    s = re.sub(r"`([^`]+)`", r"\1", s)
    return s


def slice_between(text: str, start_pat: str, end_pat: str) -> str:
    i = text.find(start_pat)
    if i < 0:
        return ""
    i += len(start_pat)
    j = text.find(end_pat, i)
    if j < 0:
        return text[i:]
    return text[i:j]


def citation_scan_segments(text: str) -> tuple[list[tuple[str, str]], str]:
    """
    Return (segments, joined) where each segment is (context_label, text).
    joined is concatenation with '\\n\\n' for searching.
    """
    if "## 1. Summary" in text:
        s1 = slice_between(text, "## 1. Summary", "## 2.")
        s4 = slice_between(text, "## 4. Novelty vs. Prior Work", "## 5.")
        segs: list[tuple[str, str]] = []
        if s1.strip():
            segs.append(("Summary", s1))
        if s4.strip():
            segs.append(("Novelty vs. Prior Work", s4))
        if not segs:
            return [("Main body", text[:2000])], text[:2000]
        joined = "\n\n".join(s for _, s in segs)
        return segs, joined
    end_markers = [
        "## Papers That Mention This Paper",
        "## Meta Information",
        "## Relevance to Proxy Label Learning",
        "## Method Tracker Update",
    ]
    end = len(text)
    for m in end_markers:
        k = text.find(m)
        if k != -1:
            end = min(end, k)
    body = text[:end]
    return [("Main note body", body)], body


def context_for_position(segments: list[tuple[str, str]], pos: int) -> str:
    """Map index inside joined segments back to segment label."""
    if not segments:
        return "Main note body"
    if len(segments) == 1:
        return segments[0][0]
    off = 0
    sep_len = 2  # \n\n between segments
    for i, (label, seg) in enumerate(segments):
        chunk_len = len(seg)
        if pos < off + chunk_len:
            return label
        off += chunk_len
        if i < len(segments) - 1:
            off += sep_len
    return segments[-1][0]


def parse_paper_title(text: str, stem: str) -> str:
    m = re.search(r"^\*\*Title:\*\*\s*(.+)$", text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    m = re.search(r"^#\s+Paper Analysis:\s*(.+)$", text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    # Filename slug fallback
    parts = stem.split("_")
    if len(parts) >= 4:
        return parts[3].replace("-", " ")
    return stem


def parse_year(stem: str) -> str | None:
    m = re.match(r"^(\d{4})_", stem)
    return m.group(1) if m else None


def parse_first_author_last(text: str) -> str | None:
    m = re.search(r"^\*\*Authors:\*\*\s*(.+)$", text, re.MULTILINE)
    if not m:
        return None
    authors = m.group(1).strip()
    if authors.lower().startswith("not specified"):
        return None
    first = authors.split(",")[0].strip()
    # "Foo Bar" -> Bar; "Bar" -> Bar
    tok = first.split()
    if not tok:
        return None
    return tok[-1]


def method_token_from_stem(stem: str) -> str | None:
    """Third underscore field in YYYY_Venue_METHOD_..."""
    parts = stem.split("_")
    if len(parts) < 4:
        return None
    tok = parts[2]
    if tok.upper() in {"NA", "ICML", "ICLR", "BLOG"}:
        return None
    if len(tok) < 3:
        return None
    return tok


def excerpt_around(hay: str, idx: int, win: int = 170) -> str:
    lo = max(0, idx - win)
    hi = min(len(hay), idx + win)
    # If we landed mid-word, advance to the next whitespace boundary
    while lo < len(hay) and lo > 0 and hay[lo].isalnum() and hay[lo - 1].isalnum():
        lo += 1
    while lo < len(hay) and hay[lo].isspace():
        lo += 1
    snippet = re.sub(r"\s+", " ", hay[lo:hi]).strip()
    if len(snippet) > 300:
        snippet = snippet[:297] + "..."
    return snippet


def find_sentence_window(hay: str, idx: int, radius: int = 220) -> str:
    start = max(0, hay.rfind(".", 0, idx))
    if start == -1:
        start = max(0, idx - radius)
    else:
        start = min(start + 1, idx)
    end = hay.find(".", idx)
    if end == -1:
        end = min(len(hay), idx + radius)
    else:
        end = min(len(hay), end + 1)
    snippet = hay[start:end].strip()
    snippet = re.sub(r"\s+", " ", snippet)
    if len(snippet) > 280:
        snippet = snippet[:277] + "..."
    return snippet


def flexible_title_find(hay: str, title: str, min_norm_len: int = 8) -> int:
    """Find start index of title in hay allowing arbitrary whitespace between tokens."""
    t = norm_ws(strip_md(title))
    if len(t) < min_norm_len:
        return -1
    parts = [p for p in t.split() if p]
    if not parts:
        return -1
    ws_pat = r"\s*".join(re.escape(p) for p in parts)
    m = re.search(ws_pat, hay, flags=re.IGNORECASE | re.DOTALL)
    return m.start() if m else -1


def title_subsumed_by_own_title(mentioner_title_norm: str, target_norm: str) -> bool:
    """True if target title is a contiguous substring of the mentioner's own title (header pollution)."""
    if not mentioner_title_norm or not target_norm:
        return False
    return target_norm in mentioner_title_norm


def ambiguous_title_ok(target_norm: str, hay: str, pos: int) -> bool:
    if target_norm not in AMBIGUOUS_TITLE_SUBSTRINGS:
        return True
    lo = max(0, pos - 140)
    hi = min(len(hay), pos + 140)
    win = hay[lo:hi]
    return bool(
        re.search(
            r"\bNatarajan\b|\bNIPS\b|\bNeurIPS\b|\(2013\)|,\s*2013\b|NeurIPS\s*2013",
            win,
            re.I,
        )
    )


def title_match(
    title: str, hay_raw: str, mentioner_title_norm: str
) -> tuple[int, str] | bool:
    """Return (index_in_hay_raw, sentence) or False."""
    t = norm_ws(strip_md(title))
    if len(t) < 18:
        return False
    if title_subsumed_by_own_title(mentioner_title_norm, t):
        return False
    pos = flexible_title_find(hay_raw, title, min_norm_len=18)
    if pos != -1:
        if not ambiguous_title_ok(t, hay_raw, pos):
            return False
        plain = strip_md(hay_raw)
        return pos, excerpt_around(plain, pos)
    return False


def author_year_patterns(last: str, year: str) -> list[re.Pattern]:
    if not last or not year:
        return []
    last_re = re.escape(last)
    y = re.escape(year)
    pats = [
        re.compile(rf"\b{last_re}\s+et\s+al\.?,?\s*\(?{y}\)?", re.I),
        re.compile(rf"\b{last_re}\s+et\s+al\.?\s+[\[\(]?\s*{y}", re.I),
        re.compile(rf"\b{last_re},?\s+{y}\b", re.I),
    ]
    return pats


def detect_mention(a_stem: str, a_text: str, b_stem: str, b_text: str, titles: dict[str, str]) -> tuple[str, str] | None:
    if a_stem == b_stem:
        return None
    segments, scan_raw = citation_scan_segments(a_text)
    scan_plain = strip_md(scan_raw)
    scan_norm = norm_ws(scan_plain)
    mentioner_own = norm_ws(strip_md(parse_paper_title(a_text, a_stem)))

    title_b = titles[b_stem]
    # Explicit relative link to B
    link_pat = "./" + b_stem + ".md"
    li = scan_raw.find(link_pat)
    if li != -1:
        return context_for_position(segments, li), f"Contains link `{link_pat}`."

    tm = title_match(title_b, scan_raw, mentioner_own)
    if tm:
        pos, sent = tm
        return context_for_position(segments, pos), sent

    # Shorter titles: only if normalized title is unique across the corpus
    t = norm_ws(strip_md(title_b))
    if 12 <= len(t) < 18:
        owners = [s for s, tt in titles.items() if norm_ws(strip_md(tt)) == t]
        if len(owners) == 1 and not title_subsumed_by_own_title(mentioner_own, t):
            pos = flexible_title_find(scan_raw, title_b, min_norm_len=12)
            if pos != -1 and ambiguous_title_ok(t, scan_raw, pos):
                return context_for_position(segments, pos), excerpt_around(scan_plain, pos)

    year_b = parse_year(b_stem)
    last_b = parse_first_author_last(b_text)
    for pat in author_year_patterns(last_b or "", year_b or ""):
        m = pat.search(scan_raw)
        if m:
            return context_for_position(segments, m.start()), excerpt_around(scan_plain, m.start())

    # Method token (filename) as whole word — conservative
    mt = method_token_from_stem(b_stem)
    if mt and len(mt) >= 4 and not mt.isdigit():
        # avoid generic words
        blocklist = {"FROM", "WITH", "THAT", "THIS", "DUAL", "SOFT", "BASE", "DATA", "CROSS"}
        if mt.upper() in blocklist:
            return None
        word_pat = re.compile(rf"\b{re.escape(mt)}\b", re.I)
        m = word_pat.search(scan_raw)
        if m:
            # Require that another paper does not share same method token
            peers = [s for s in titles if s != b_stem and method_token_from_stem(s) == mt]
            if peers:
                return None
            return context_for_position(segments, m.start()), excerpt_around(scan_plain, m.start())

    return None


def build_reverse_edges(files: dict[str, str]) -> dict[str, list[tuple[str, str, str]]]:
    titles = {stem: parse_paper_title(text, stem) for stem, text in files.items()}
    edges: dict[str, list[tuple[str, str, str]]] = {s: [] for s in files}
    seen: dict[str, set[str]] = {s: set() for s in files}
    stems = list(files)
    for a in stems:
        for b in stems:
            if a == b:
                continue
            hit = detect_mention(a, files[a], b, files[b], titles)
            if hit:
                ctx, summ = hit
                if a in seen[b]:
                    continue
                seen[b].add(a)
                edges[b].append((a, ctx, summ))
    return edges


def format_table_rows(rows: list[tuple[str, str, str]]) -> str:
    lines = [TABLE_HEADER, TABLE_SEP]
    for stem, ctx, summ in sorted(rows, key=lambda x: x[0]):
        summ_esc = summ.replace("|", "\\|")
        lines.append(
            f"| [{stem}.md](./{stem}.md) | {ctx} | {summ_esc} |"
        )
    return "\n".join(lines) + "\n"


def replace_or_insert_section(text: str, new_section_body: str) -> str:
    """new_section_body is content AFTER the ## header line (table + optional note)."""
    if SECTION_HEADER in text:
        pre, rest = text.split(SECTION_HEADER, 1)
        # drop through next --- line that follows section (keep trailing consistent)
        if "\n---\n" in rest:
            _, post = rest.split("\n---\n", 1)
            rebuilt = (
                pre.rstrip()
                + "\n\n"
                + SECTION_HEADER
                + "\n\n"
                + new_section_body.strip()
                + "\n\n---\n"
                + post.lstrip()
            )
            return rebuilt
        # no --- after section: append --- before next ## if any
        m = re.search(r"\n##\s", rest)
        if m:
            post = rest[m.start() :]
            rebuilt = (
                pre.rstrip()
                + "\n\n"
                + SECTION_HEADER
                + "\n\n"
                + new_section_body.strip()
                + "\n"
                + post
            )
            return rebuilt
        return pre + SECTION_HEADER + "\n\n" + new_section_body.strip() + "\n" + rest
    # Insert before Meta Information or Method Tracker or end
    insert_markers = ["## Meta Information", "## Method Tracker Update", "## Relevance to Proxy Label Learning"]
    insert_at = len(text)
    chosen = None
    for mk in insert_markers:
        k = text.find(mk)
        if k != -1 and k < insert_at:
            insert_at = k
            chosen = mk
    block = "\n\n" + SECTION_HEADER + "\n\n" + new_section_body.strip() + "\n\n---\n\n"
    if chosen:
        return text[:insert_at].rstrip() + block + text[insert_at:]
    return text.rstrip() + block


def main() -> None:
    root = Path(__file__).resolve().parent
    md_paths = sorted(root.glob("*.md"))
    md_paths = [p for p in md_paths if p.name.startswith("_") is False]
    files = {p.stem: p.read_text(encoding="utf-8") for p in md_paths}
    edges = build_reverse_edges(files)

    updated = 0
    total_rows = 0
    for stem, text in files.items():
        rows = edges.get(stem, [])
        if rows:
            body = format_table_rows(rows)
            total_rows += len(rows)
        else:
            body = EMPTY_NOTE + "\n\n" + TABLE_HEADER + "\n" + TABLE_SEP + "\n"
        new_text = replace_or_insert_section(text, body)
        if new_text != text:
            updated += 1
        (root / f"{stem}.md").write_text(new_text, encoding="utf-8")

    print(f"files_changed={updated}")
    print(f"files_written={len(files)}")
    print(f"reverse_edge_rows={total_rows}")


if __name__ == "__main__":
    main()
