#!/usr/bin/env python3
"""Build compact review-surface files from read-papers/ cards for the CLI reviewers.

Writes review/context/relevance-index-{1,2}.md (header line + Project Relevance section per card,
split so each file stays under ~28 KB) and review/context/cards-summaries.md (header + Summary section).
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
CARDS = os.path.join(HERE, "..", "read-papers")
OUT = os.path.join(HERE, "context")
os.makedirs(OUT, exist_ok=True)


def section(text, title_re):
    m = re.search(r"^## [^\n]*(" + title_re + r")[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(2).strip() if m else "(section missing)"


entries = []
for fn in sorted(os.listdir(CARDS)):
    if not fn.endswith(".md"):
        continue
    t = open(os.path.join(CARDS, fn), encoding="utf-8", errors="ignore").read()
    title = t.splitlines()[0].lstrip("# ").strip() if t else fn
    header = next((ln for ln in t.splitlines() if ln.startswith("**Source:**")), "")
    rel = section(t, r"Project Relevance")
    summ = section(t, r"Summary")
    ev = section(t, r"Evidence")
    entries.append((fn, title, header, rel, summ, ev))

# relevance index, split in two
chunks, cur, size = [], [], 0
for fn, title, header, rel, _, _ in entries:
    block = f"### {title}\n`{fn}`\n{header}\n\n{rel}\n\n"
    if size + len(block) > 28000 and cur:
        chunks.append(cur)
        cur, size = [], 0
    cur.append(block)
    size += len(block)
if cur:
    chunks.append(cur)
for i, ch in enumerate(chunks, 1):
    with open(os.path.join(OUT, f"relevance-index-{i}.md"), "w", encoding="utf-8") as f:
        f.write(f"# Relevance index {i}/{len(chunks)} — Project Relevance sections of all cards (generated)\n\n")
        f.writelines(ch)

# summaries + evidence, split by size
chunks, cur, size = [], [], 0
for fn, title, header, _, summ, ev in entries:
    block = f"### {title}\n`{fn}`\n{header}\n\n**Summary.** {summ}\n\n**Evidence.** {ev}\n\n"
    if size + len(block) > 28000 and cur:
        chunks.append(cur)
        cur, size = [], 0
    cur.append(block)
    size += len(block)
if cur:
    chunks.append(cur)
for i, ch in enumerate(chunks, 1):
    with open(os.path.join(OUT, f"cards-summaries-{i}.md"), "w", encoding="utf-8") as f:
        f.write(f"# Card summaries {i}/{len(chunks)} — Summary and Evidence sections of all cards (generated)\n\n")
        f.writelines(ch)

print(f"{len(entries)} cards -> relevance-index x{len([c for c in os.listdir(OUT) if c.startswith('relevance-index')])}, cards-summaries x{len([c for c in os.listdir(OUT) if c.startswith('cards-summaries')])}")
for c in sorted(os.listdir(OUT)):
    print(c, os.path.getsize(os.path.join(OUT, c)))
