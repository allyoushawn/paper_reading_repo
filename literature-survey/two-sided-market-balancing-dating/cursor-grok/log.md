# cursor-grok run log — two-sided-market-balancing-dating

## [2026-08-17] nlm CLI follow-up (MCP still Not connected; CLI works)

- Auth: `nlm login --check` valid (`allyoushawn@gmail.com`). Notebook `d3071ac8` now **165 sources** (was 157).
- Added: Hinge 2025 pages (`b2ee80ca`, `76a4eccc`); UniCoRn arXiv PDF (`93144d1a`); Kanzhun CMBI/IR (`94e5fef2`, `503e6bd0`); GFRR text extract (`2383281d`). Junk walls: IEEE `d9e1502a`, OpenReview `bc2811a7` — left in place (ask before delete).
- Queries: RecSys 2025 list (Hayashi present; Kaya hiring fairness); Kanzhun trio (responsive-traffic + 1.5B mutual achievements 2023; no ranker architecture); Hinge (NLM confirms double-digit matches); UniCoRn (α=0; +0.51%/+0.57% cand-gen WAU/sessions).
- Deep research started: task `ChBjM2UxZDliYmYxN2JiODI4EAgaBDAxZDIqA3Vzdw`. `nlm research status`/`import` fail with HTTP 400 on poll RPC `e3bVqc`. Hits **not** imported via CLI.

## [2026-08-17] literature-survey-nlm gap-fill (cursor-grok workplace)

- Filled remaining gaps after the 66-item continuation. Did **not** recreate shared README/requirements; **appended** `queue.md` only.
- NotebookLM MCP **not connected** (`notebook_get` / `research_start` / `source_add` all failed). Did not pad T3. Paper-keyword 61-hit re-import still blocked.
- Live-page additions (6 annotated): Hinge 2025 How We Connect + product evolution (mutual-compat DL; double-digit matches); GFRR IEEE Access 2023; UniCoRn NeurIPS 2021; Kanzhun IR/CMBI fairer traffic; Xia ASONAM 2015 Baihe; Kaya RecSys 2025 Jobindex fairness interviews.
- RecSys 2025 accepted list mined: Hayashi OPE is the matching paper; LCM4Rec not added.
- Bumble ranking re-confirmed null (`site:tech.bumble.com ranking` empty). Dating-log OPE still none.
- Bibliography **72** annotated, **86%** T1+2 (62/72). New notes in `read-papers/`; corpus citation map in `reverse-citation-map.md`.

Skill name: literature-survey-nlm (brief path, workplace `cursor-grok`).

## [2026-08-17] literature-survey-nlm continuation (cursor-grok workplace)

- Resumed from 2026-08-16 53-item bib. Did **not** recreate shared README/requirements; appended to shared `queue.md` only.
- Notebook `d3071ac8-16ef-4460-8991-7701679974c8` had **141 sources** at start of this continuation.
- Imported leftover industry task `7ddbec32` (indices 1, 8): Airbnb two-sided ranking PDF; CyberAgent Speaker Deck. Did not import Scribd/Techugo duplicates.
- New industry `research_start` `275cee32` (fast, 10 hits). Imported 0, 5, 6, 7: Tinder Elastic YouTube talk, LinkSAGE, Kanzhun HKEX, Columbia congestion PDF. **Skipped** Hinge/Bumble SEO pages.
- Added URLs: Tapple AAAI 2021 PDF; Dating Heuristic arXiv 2308.02584; Mashayekhi HTML; LinkedIn fairness arXiv 1905.01989. Failed: student.cs LinkedIn PDF, several bulk URLs.
- NLM extracts: Tinder ES8, CUPID, GraphMatch succeeded. Eureka / OkCupid JAX / Maimai queried with timeout or NO CONTENT — cited from live pages.
- Paper-keyword 61-hit import from 2026-08-16 still unrecoverable.
- Bibliography now **66** annotated (85% T1+2). New read-papers: Tinder ES8, Ramanathan AAAI 2021, CUPID, OkCupid JAX.
- Blind-spot update: dating ranking blogs **do** exist (Tinder ES8, OkCupid JAX). Dedicated RRS survey after Palomares 2021 still missing; Neve 2025 book + Mashayekhi 2024 CSUR are substitutes.

Skill name: literature-survey-nlm (brief path, workplace `cursor-grok`).

## [2026-08-16] literature-survey-nlm (cursor-grok workplace)

- Shared root already had README.md + requirements.md (claude_opus Phase 1). Did not recreate. No shared queue.md yet — created additively this run.
- Notebook `d3071ac8-16ef-4460-8991-7701679974c8` existed with **119 sources** at start (ingest was already done). Added missing free URLs: Kleinerman RecSys 2018 author PDF; Hayashi et al. RecSys 2025 OPE; MODE RecSys 2026 PDF; Tomita RecSys 2022 talk PDF; Jiayuan/Tencent Cloud 2018; Wantedly RecSys 2025 post; CFRR/KDD-TSMO PDF; mini-batch stable matching PDF. Mistaken add: arXiv 2201.11331 (unrelated ID guess). RecSys 2026 CFP page added (low value).
- Paper-keyword `research_start` (deep) completed: **61 hits**. `research_import` and industry `research_start` (fast, task `7ddbec32-...`) were interrupted by NotebookLM MCP disconnect (`Not connected`). Did not pad the notebook further.
- NLM per-source extracts written under `working-notes/nlm-extract-*.md`. Several requested source_ids returned “NO CONTENT” (Quartz Gini, Eureka ethics, OkCupid JAX, Lyft MMV, DoorDash, Airbnb host, Thumbtack, Upwork) — those items are cited from publisher pages / the brief’s verified URLs, not from NLM body text.
- Awesome recsys repo Step 0: 0 filename matches for reciprocal / LiJAR / matching-market. Null.
- Outputs: `executive-summary.md`, `literature-review.md`, `method-tracker.md`, `read-papers/` (read-first 10), this log.
- NLM notebook source count: ~130 after adds (119 + ~11; exact count unverified after MCP drop). Added this run: ~11 URLs.

Skill name: literature-survey-nlm (brief path, workplace `cursor-grok`, not the 200-paper default).
