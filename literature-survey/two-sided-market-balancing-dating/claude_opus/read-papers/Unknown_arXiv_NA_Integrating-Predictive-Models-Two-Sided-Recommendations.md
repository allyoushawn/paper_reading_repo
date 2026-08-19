# Paper Analysis: Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach

**Source:** arXiv (per batch manifest label; source_id `dc9b9201-8782-4615-8aaa-61a69421d536`)
**Date analyzed:** 2026-08-16

**Note on source type:** Total extraction failure — see Summary below. Per the batch's validity gate, no content in this file is fabricated, inferred from the title, or filled in from outside knowledge.

---

## 1. Summary

All three NotebookLM queries for this source (core problem/method/datasets; quantitative results/limitations/cited works; project-relevance probe) returned `RESOURCE_EXHAUSTED` errors from Google on every attempt — the initial call plus four retries with escalating cooldowns (immediate, 45s, 90s, 180s; ~5 minutes total). No query ever returned grounded content or a valid `sources_used`. The same failure occurred simultaneously for all four sources in this batch, which points to a shared account-level NotebookLM quota being exhausted by concurrent batch agents querying the same notebook (`d3071ac8-16ef-4460-8991-7701679974c8`) in parallel, rather than a per-source content gap (e.g. an empty-shell source). Recommend re-querying this source once the shared quota resets.

---

## 2–6. (Omitted — extraction failed)

Not applicable. No grounded content was obtained for any section.

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Unknown — extraction failed
**Affiliations:** Unknown — extraction failed
**Venue:** arXiv (per manifest label only, unverified)
**Year:** Unknown — extraction failed
**PDF:** Not available — extraction failed via NotebookLM source
**Relevance:** Unknown — extraction failed
**Priority:** 3 (tier per manifest)

---

## Bibliography Fields

- **title:** Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach (per batch manifest label)
- **authors or organization:** Unknown — extraction failed
- **year:** Unknown — extraction failed
- **venue or type:** arXiv (per manifest label only, unverified)
- **link:** Unknown — extraction failed
- **tier tag:** Tier 3

**what they did (≤80 words):** Not specified in source. All three NotebookLM queries for this source failed with `RESOURCE_EXHAUSTED` across five attempts (~5 minutes of retries); no grounded content was ever returned.

**mechanism relevant to two-sided balancing (≤50 words):** Not specified in source.

**metrics used, and the reported effect:** Not specified in source.

**fit for a dating app:** Unknown — extraction failed. Cannot be assessed without grounded content; per the validity gate this must not be inferred from the title alone.

**confidence that the item is real and described correctly:** low — no grounded NotebookLM content was ever returned for this source, so even its basic existence/description cannot be independently verified beyond the manifest's title string.

---

## Project Relevance

**Low project relevance — extraction failed, not a content judgment.** Query 3 (the project-relevance probe) returned `RESOURCE_EXHAUSTED` on every attempt across five retries. No assessment of this source's fit to the reciprocal-scoring / capacity-allocation / market-design / ecosystem-metrics framing could be made. This is a note about extraction status, not a substantive relevance judgment — recommend re-running Phase 3 for this source once the shared NotebookLM quota clears.
