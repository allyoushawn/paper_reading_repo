# Paper Analysis: Automated Decision Making at Grindr

**Source:** Grindr Blog — https://www.grindr.com/blog/automated-decision-making-at-grindr (Company Updates), NotebookLM source_id `c60a97fd-d38e-4c59-a1f3-3cf84e8abaf1`
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** Automated Decision Making at Grindr
**Authors:** Shane Wiley (Chief Privacy Officer), with input from Tom Quisel (CTO)
**Abstract:**
A corporate privacy blog post (published April 14, 2023) clarifying how much of Grindr's platform actually uses Automated Decision Making (ADM) or AI, in the context of GDPR Article 22, proposed EU AI rules, and emerging US state privacy laws. The piece exists to manage regulatory and user expectations, not to describe a recommendation system.

**Key contributions:**
- Explicitly states Grindr's core app has **no recommendation/matchmaking algorithm**.
- Describes the actual grid as **distance-sorted, filter-applied, with minor randomness** for freshness.
- Confines ADM/AI use to background safety systems: spam detection and non-compliant-image filtering.

**Methodology:**
Not applicable — this is a policy/product-transparency statement, not a technical paper. No architecture, model, or algorithm for matching or ranking is proposed.

**Main results:**
No experimental results. The only figures given are qualitative product description and an App Store rating (4.6 / 259.4k ratings, incidental to the post).

---

## 2. Experiment Critique

**Design:** N/A — no experiment was run or reported.

**Statistical validity:** N/A.

**Online experiments (if any):** None described for matching/ranking. Some general mention that spam/image-moderation ADM systems are "tuned" for false-positive/false-negative tradeoffs, but no methodology or metrics given.

**Reproducibility:** N/A.

**Overall:** This is a negative-contrast source: valuable to the survey precisely because it documents the *absence* of an active matching algorithm at a major dating platform, not because it proposes one.

---

## 3. Industry Contribution

**Deployability:** N/A (descriptive, not prescriptive).

**Problems solved:** Regulatory transparency / user trust communication regarding ADM under GDPR Art. 22 and emerging AI regulation.

**Engineering cost:** N/A.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** None claimed; this is a disclosure, not a research contribution.

**Prior work comparison:** N/A.

**Verification:** N/A.

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| None | — | — | No datasets used or referenced |

**Offline experiment reproducibility:** N/A.

---

## 6. Community Reaction

Not assessed for this source (out of scope for Phase 3 batch processing; would require separate web search).

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Shane Wiley (CPO); Tom Quisel (CTO) quoted
**Affiliations:** Grindr, LLC
**Venue:** Grindr corporate blog (Company Updates)
**Year:** 2023
**PDF:** Not applicable — web article, fetched via NotebookLM source
**Relevance:** Related (negative contrast / market-design baseline)
**Priority:** 1 (per queue tier)

---

## Bibliography Fields

- **title:** Automated Decision Making at Grindr
- **authors or organization:** Shane Wiley (Chief Privacy Officer), Grindr, LLC
- **year:** 2023
- **venue or type:** Company blog post (Grindr, Company Updates)
- **link:** https://www.grindr.com/blog/automated-decision-making-at-grindr
- **tier tag:** Tier 1 — Dating-platform primary source
- **what they did (≤80 words):** Grindr's CPO publicly clarifies, in response to GDPR/AI-regulation scrutiny, that the app uses no recommendation or matchmaking algorithm. The core grid is sorted strictly by distance plus user-selected filters (age, tribe, relationship status), with minor randomness for freshness. The only ADM/AI in production is confined to background spam detection and non-compliant-image filtering, tuned for a false-positive/false-negative tradeoff, with human override via Customer Experience.
- **mechanism relevant to two-sided balancing (≤50 words):** None. Explicitly no reciprocal scoring, no capacity awareness, no exposure redistribution — the platform deliberately avoids algorithmic curation, relying on distance-sort plus manual user filtering to allocate exposure.
- **metrics used, and the reported effect:** None reported (no matching/ranking metrics; only incidental App Store rating 4.6/259.4k, unrelated to matching).
- **fit for a dating app:** low — it *is* a dating app, but the source describes the absence of any balancing mechanism, so it offers no transferable technique, only a documented counter-example.
- **confidence that the item is real and described correctly:** high (NotebookLM grounded answer with direct quotes from the source; source_id validated in all three queries).

---

## Project Relevance

**Low project relevance.** This source is useful only as a documented negative example: a major dating platform (Grindr) explicitly states it runs no recommendation, reciprocal-scoring, capacity-aware, or exposure-redistribution system — matching is left entirely to user-driven, distance-sorted browsing. It confirms that at least one large dating marketplace has chosen not to engage the over-subscription/wasted-likes problem algorithmically at all, which is worth citing as contrast when motivating why capacity-aware allocation matters, but it contains no mechanism, metric, or lever the project can adopt or adapt.
