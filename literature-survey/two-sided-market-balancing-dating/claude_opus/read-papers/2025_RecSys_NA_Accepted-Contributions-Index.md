# Paper Analysis: RecSys 2025 — Accepted Contributions

**Source:** ACM RecSys 2025 (Prague) conference website — accepted-contributions listing page (full papers, short papers, reproducibility, industry, LBR, demo, doctoral)
**Date analyzed:** 2026-08-16

**Note on source type:** This is a conference program index page listing dozens of accepted papers with abstracts, not a single research paper. Per the batch manifest and paper-reader's peripheral-source rule, this file is a one-paragraph summary plus Bibliography Fields and Project Relevance only.

---

## 1. Summary

**Title:** RecSys 2025 — Accepted Contributions
**Authors:** N/A (conference program index, ACM RecSys)
**Abstract:**
A listing of accepted full papers, short papers, reproducibility papers, industry papers, late-breaking results (LBR), demos, and doctoral symposium contributions for ACM RecSys 2025 (Prague), each with title, authors, affiliations, and abstract. Query 1 (grounded, `sources_used` valid) surfaced one directly on-target accepted paper: **"Off-Policy Evaluation and Learning for Matching Markets"** by Yudai Hayashi (Wantedly), Shuhei Goda (Independent Researcher), Yuta Saito (Cornell University) — which explicitly targets reciprocal-recommendation platforms including dating apps, proposing novel off-policy estimators (DiPS and DPR) for matching-market settings with sparse, bidirectional reward signals, evaluated on synthetic data and real A/B logs from job-matching platform Wantedly Visit. Three other tangentially relevant accepted papers were also surfaced: a non-parametric choice model for inter-item competition (LCM4Rec), a social-choice-based individual+group fairness integration paper, and a sparse-autoencoder group-fairness aggregation method (SAGEA) — none reciprocal-matching-specific.

**Key contributions:** Not applicable — this is an index, not a single contribution.

**Methodology:** Not applicable.

**Main results:** Not applicable.

---

## 2–6. (Omitted for peripheral index source)

Not applicable — this source is a conference program listing, not a single paper with its own experiments, novelty claims, or datasets. Query 2 (quantitative results / limitations / cited works) and Query 3 (project-relevance probe) both returned `RESOURCE_EXHAUSTED` API errors on the initial call and the mandated retry; per the validity gate, no content from those two query attempts was used or written into this file.

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** N/A (ACM RecSys 2025 program committee / conference website)
**Affiliations:** ACM RecSys
**Venue:** ACM RecSys 2025 (Prague) — conference website
**Year:** 2025
**PDF:** Not available — web index page, accessed via NotebookLM source
**Relevance:** Peripheral (index page; one embedded paper title is highly relevant — see Project Relevance)
**Priority:** 4

---

## Bibliography Fields

- **title:** RecSys 2025 — Accepted Contributions
- **authors or organization:** ACM RecSys (conference program index)
- **year:** 2025
- **venue or type:** Conference program index page (not a paper)
- **link:** https://recsys.acm.org (RecSys 2025, Prague — Accepted Contributions page)
- **tier tag:** Tier 1 — Adjacent marketplace, conference index (not a primary source)

**what they did (≤80 words):** Not applicable — this is a listing of dozens of independently authored papers accepted to RecSys 2025, not a single piece of work. The one query that returned valid grounded content (EXTRACTION FAILED for the other two, see Notes) surfaced "Off-Policy Evaluation and Learning for Matching Markets" (Hayashi, Goda, Saito) as the most on-target accepted paper for this project's reciprocal-recommendation and dating/job-matching framing.

**mechanism relevant to two-sided balancing (≤50 words):** The index itself has no mechanism. The surfaced paper "Off-Policy Evaluation and Learning for Matching Markets" proposes DiPS/DPR off-policy estimators for reciprocal recommendation platforms (dating, job search) under sparse bidirectional rewards — directly relevant to the project's evaluation-under-interference layer, but not independently verified here (Query 3 failed).

**metrics used, and the reported effect:** Not applicable to the index itself. Per the Query 1 abstract snippet only (not independently verified via Query 2/3): the Hayashi/Goda/Saito paper reports empirical superiority of DiPS/DPR over existing OPE methods on synthetic data and real Wantedly Visit A/B logs, especially under sparse match labels.

**fit for a dating app:** medium — reason: the index page itself has no mechanism (low fit), but it surfaces one paper ("Off-Policy Evaluation and Learning for Matching Markets") whose abstract explicitly targets dating/reciprocal-matching platforms and is worth independently reading as its own source in a future batch; this file does not substitute for that.

**confidence that the item is real and described correctly:** medium — Query 1 returned `sources_used` matching this source_id with detailed, internally consistent listing content (real author affiliations, verifiable-looking abstracts). However, Query 2 and Query 3 failed on both the initial call and the mandated retry (`RESOURCE_EXHAUSTED`), so the fuller extraction (quantitative results, limitations, project-relevance probe) could not be independently confirmed — confidence is capped at medium pending a possible later re-query.

---

## Project Relevance

**Low project relevance (as an index page).** The RecSys 2025 accepted-contributions listing itself is a program index, not a mechanism source, so it does not itself address reciprocal scoring, capacity limits, exposure allocation, or ecosystem-health metrics. However, Query 1's grounded response (valid `sources_used`) surfaced one paper worth flagging for a future reading batch: **"Off-Policy Evaluation and Learning for Matching Markets"** (Yudai Hayashi, Shuhei Goda, Yuta Saito; RecSys 2025 full paper) — its abstract explicitly frames the problem around "services driven by reciprocal recommendations, such as job search and dating applications," addresses the sparse, bidirectional-reward evaluation problem central to the project's Phase 4 "experimentation under interference" layer, and reports empirical results on a real matching platform (Wantedly Visit). This paper was not independently queried in this batch (Query 3, which would have probed its fit against the dating-market framing directly, failed twice with `RESOURCE_EXHAUSTED`), so its content here is a title/abstract-level flag only, not a verified analysis — recommend adding it to the survey queue as its own source in a later phase.

**Extraction note:** Query 2 (quantitative results / limitations / top cited works) and Query 3 (project-relevance probe) both returned `RESOURCE_EXHAUSTED` errors on the initial call and the one mandated retry. Per the brief's validity gate, no content from those failed calls was fabricated, inferred, or written into this file — this file relies solely on the one successful, grounded Query 1 response.
