#!/usr/bin/env python3
"""Compact review surface: truncated card excerpts + related-notebook answers."""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CARDS = os.path.join(ROOT, "read-papers")
OUT = os.path.join(HERE, "context")
os.makedirs(OUT, exist_ok=True)

MAX_SUMM = 1400
MAX_EV = 900
MAX_REL = 1600
CHUNK = 26000


def section(text, title_re):
    m = re.search(r"^## [^\n]*(" + title_re + r")[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(2).strip() if m else "(section missing)"


def trunc(s, n):
    s = re.sub(r"\n{3,}", "\n\n", s).strip()
    if len(s) <= n:
        return s
    return s[: n - 20].rsplit(" ", 1)[0] + "\n… [truncated]"


def write_chunks(prefix, header, blocks):
    chunks, cur, size = [], [], 0
    for block in blocks:
        if size + len(block) > CHUNK and cur:
            chunks.append(cur)
            cur, size = [], 0
        cur.append(block)
        size += len(block)
    if cur:
        chunks.append(cur)
    paths = []
    for i, ch in enumerate(chunks, 1):
        fn = f"{prefix}-{i}.md"
        path = os.path.join(OUT, fn)
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"{header} ({i}/{len(chunks)})\n\n")
            f.writelines(ch)
        paths.append((fn, os.path.getsize(path)))
    return paths


entries = []
for fn in sorted(os.listdir(CARDS)):
    if not fn.endswith(".md"):
        continue
    t = open(os.path.join(CARDS, fn), encoding="utf-8", errors="ignore").read()
    title = t.splitlines()[0].lstrip("# ").strip() if t else fn
    header = next((ln for ln in t.splitlines() if ln.startswith("**Source:**")), "")
    q2 = next((ln for ln in t.splitlines() if ln.startswith("**Q2 class:**")), "")
    gid = next((ln for ln in t.splitlines() if ln.startswith("**Queue id:**")), "")
    entries.append((fn, title, header, q2, gid, t))

# compact q2 table
with open(os.path.join(OUT, "q2-class-index.md"), "w", encoding="utf-8") as f:
    f.write("# Q2 class index — NLM card labels (re-classify with D3 rubric if they conflict)\n\n")
    f.write("| Queue | Q2 class (card) | Filename |\n|---|---|---|\n")
    for fn, title, header, q2, gid, t in entries:
        cls = q2.replace("**Q2 class:**", "").strip()
        qid = gid.replace("**Queue id:**", "").strip()
        f.write(f"| {qid} | {cls} | `{fn}` |\n")

rel_blocks = []
sum_blocks = []
for fn, title, header, q2, gid, t in entries:
    rel = trunc(section(t, r"Project Relevance"), MAX_REL)
    summ = trunc(section(t, r"Summary"), MAX_SUMM)
    ev = trunc(section(t, r"Evidence"), MAX_EV)
    rel_blocks.append(f"### {title}\n`{fn}`\n{header}\n{q2}\n\n{rel}\n\n")
    sum_blocks.append(f"### {title}\n`{fn}`\n{header}\n{q2}\n\n**Summary.** {summ}\n\n**Evidence.** {ev}\n\n")

# Write compact-* files; leave the untruncated relevance-index-* / cards-summaries-* in place.
rpaths = write_chunks(
    "compact-relevance",
    "# Compact relevance index — truncated Project Relevance from this-run cards",
    rel_blocks,
)
spaths = write_chunks(
    "compact-summaries",
    "# Compact card summaries — truncated Summary + Evidence from this-run cards",
    sum_blocks,
)

# related notebooks: extract answer only, keep under 28 KB
def extract_answer(path):
    raw = open(path, encoding="utf-8", errors="ignore").read()
    try:
        obj = json.loads(raw)
        v = obj.get("value") or obj
        return v.get("answer") or raw
    except json.JSONDecodeError:
        return raw


unified = extract_answer(os.path.join(OUT, "nlm-unified-ltv-q2.txt"))
twosided = extract_answer(os.path.join(OUT, "nlm-twosided-q2.txt"))
banner = """# Related-notebook Q2 queries (NOT ground truth)

NotebookLM answers from related surveys. These notebooks over-classify RL/LTR
retention optimizers as TRUE attribution. **Ground truth for this run:** D3
rubric in `discovery/D3_retention_attribution.md` plus this folder's cards.
RL-for-retention (RLUR, GFN4Retention, AURO, SEC, OCARM, MRet) is not
automatically attribution; say whether the method produces per-interaction
credit for a delayed retention label.

Do not cite papers that are only in these related notebooks unless a card
exists under this run's `read-papers/`.

"""
compact = banner + "## unified-ltv-ranking-dating (`67046a44-7490-4fe5-b54a-3f39ef37fdd3`)\n\n" + trunc(unified, 12000)
compact += "\n\n## two-sided-market-balancing-dating (`d3071ac8-16ef-4460-8991-7701679974c8`)\n\n" + trunc(twosided, 8000)
open(os.path.join(OUT, "related-notebooks-q2.md"), "w").write(compact)

print("relevance", rpaths)
print("summaries", spaths)
print("q2-class-index", os.path.getsize(os.path.join(OUT, "q2-class-index.md")))
print("related-notebooks-q2", os.path.getsize(os.path.join(OUT, "related-notebooks-q2.md")))
