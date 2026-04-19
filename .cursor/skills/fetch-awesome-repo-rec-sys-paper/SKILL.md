---
name: fetch-awesome-repo-rec-sys-paper
description: >-
  Resolves paper titles and repository-relative PDF paths from the curated
  Awesome Deep Learning papers list (search / recommendation / ads) by
  keyword. Project skill for paper_reading_repo; use when the user names a
  paper, acronym, author, or venue and needs the canonical path or GitHub blob
  URL from that index, or when they mention
  Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising.
---

# Fetch paper path from Awesome rec-sys list

## Source of truth

Papers are **not** stored as PDFs in the Awesome repo. That clone only holds `README.md` (and a few extras). Each bullet is a markdown link whose URL points at **`guyulongcs/Deep-Learning-for-Search-Recommendation-Advertisements`** on GitHub. The **repo-relative path** is the segment after `blob/<branch>/` in that URL (URL-decoded).

## Default README resolution

1. Env **`AWESOME_REC_SYS_README`** if set  
2. Else **`../Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/README.md`** relative to this repository root (sibling folder under the same parent as `paper_reading_repo`)  
3. Else a machine-specific fallback path (override with env or `--readme` if missing)

## What to run

From the **paper_reading_repo** root:

```bash
python3 .cursor/skills/fetch-awesome-repo-rec-sys-paper/scripts/find_paper.py "DIEN"
python3 .cursor/skills/fetch-awesome-repo-rec-sys-paper/scripts/find_paper.py wide deep
```

- **Query**: one or more tokens; **every** token must appear somewhere in the link title, relative path, or URL (case-insensitive). Split concepts into separate words for stricter matching.  
- **Output**: section heading, human title, decoded **`path:`** (PDF path inside the PDF repo), and **`url:`** (GitHub blob link).

If no README is found, clone [Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising](https://github.com/guyulongcs/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising) as a sibling of this repo, or set `AWESOME_REC_SYS_README` / pass `--readme`.

## Fallback without the script

1. Open the README at the resolved path above (or user-provided).  
2. Search for the keyword (case-insensitive).  
3. For each `* [Title](URL)` line with a `.pdf` URL, decode the path after `blob/master/` (or other branch) using URL decoding (e.g. `%20` → space).  
4. Return **section** (nearest preceding `##` heading), **title**, **relative path**, and **full URL**.

## Notes

- Link titles use nested brackets (e.g. `[DIN]` inside the outer `[...](url)`); the script parses those correctly. Manual search should not use a naive `[^]]+` regex on the whole line.  
- Duplicate titles can appear under different sections (e.g. same paper under `03_Ranking` and `Sequence-Modeling`); report all matches or the path the user needs.  
- Some link texts use markdown emphasis (`**`); the script strips `*` / `_` / `` ` `` for display.  
- Local PDF files only exist if the user has separately cloned **`Deep-Learning-for-Search-Recommendation-Advertisements`**; the Awesome README still gives the correct **relative path** inside that repo.  
- Query tokens that are letters, digits, or hyphens are matched as **whole words** (so `DIEN` does not match inside `Gradient`).
