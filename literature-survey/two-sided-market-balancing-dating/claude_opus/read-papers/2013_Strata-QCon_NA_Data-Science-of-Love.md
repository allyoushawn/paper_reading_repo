# Paper Analysis: Data Science of Love

**Source:** eHarmony — Vaclav Petricek, Strata + QCon 2013 (conference slide deck)
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** Data Science of Love
**Authors:** Vaclav Petricek (eHarmony)
**Abstract:**
Industry slide deck describing eHarmony's Compatibility Matching System, a three-layer pipeline (Compatibility Matching, Affinity Matching, Match Distribution) for matching romantic partners at scale. Combines a psychological questionnaire, large-scale behavioral modeling, and network-wide graph optimization.

**Key contributions:**
- Describes a 3-layer production matching pipeline: (1) Compatibility Matching via a Relationship Questionnaire across 29 Dimensions® (personality, values, attitudes, beliefs), (2) Affinity Matching using ~3,000 behavioral attributes (distance, height difference, attractiveness, food preference) scored with Vowpal Wabbit and GBDTs, (3) Match Distribution using graph optimization to spread matches across the whole network.
- Frames match delivery as a network-level optimization ("delivering the right matches at the right time to as many people as possible across the entire network") rather than isolated pairwise scoring.
- Reports operating scale: ~40M registered users, ~1,000 attributes/profile, ~10^8 matches/day.

**Methodology:**
Pipeline of questionnaire-based compatibility scoring → ML-based affinity probability scoring (Prob(match | data) via GBDT/Vowpal Wabbit over sparse, high-dimensional behavioral data) → graph optimization for match distribution across the user network.

**Main results:**
Only business-level outcome metrics reported (Harris Interactive survey on marriages attributable to eHarmony): 90/day (2005) → 236/day (2007) → 542/day (2009). No model-level accuracy or matching-quality metrics given.

---

## 2. Experiment Critique

**Design:**
None — this is a conference slide deck with no experimental design, no controls, no ablations, no baseline comparisons.

**Statistical validity:**
Not applicable. No significance tests, effect sizes, or sample-size reporting for any modeling claim; the only "statistic" cited (daily marriage counts) traces to a third-party survey with no methodology detail.

**Online experiments (if any):**
None described.

**Reproducibility:**
Not reproducible — no code, hyperparameters, data splits, or dataset access. Internal production data only.

**Overall:**
Business-outcome numbers are not tied to specific model versions or controlled comparisons, so they cannot support causal claims about the matching algorithm's effectiveness. Treat as a system-design description, not an evaluated method.

---

## 3. Industry Contribution

**Deployability:**
This is itself a description of a deployed, production-scale system (eHarmony's live matching pipeline), so deployability is not in question — it already runs at ~40M users / ~10^8 matches per day.

**Problems solved:**
Combines stated-preference data (questionnaire) with learned behavioral affinity and a network-level distribution step meant to spread matches broadly rather than let pairwise scoring concentrate matches on a few profiles.

**Engineering cost:**
High: a 3-stage pipeline requiring a proprietary psychometric instrument (29 Dimensions®), a large-scale sparse feature ML system (~3,000 attributes, GBDT/Vowpal Wabbit at ~10^8 matches/day), and a graph optimization layer over the full user network — substantial infra and maintenance burden.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Not applicable — no novelty claims are made; the deck does not reference academic literature or position itself against prior methods.

**Prior work comparison:** Not specified in source.

**Verification:** Not specified in source.

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| eHarmony internal production data | N/A | No | Internal only; ~40M users, ~1,000 attributes/user, not public |

**Offline experiment reproducibility:**
Not reproducible — no public dataset or benchmark is used or released.

---

## 6. Community Reaction

No significant community discussion found (not investigated as part of this NotebookLM-based extraction).

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Vaclav Petricek
**Affiliations:** eHarmony
**Venue:** Strata + QCon 2013 (conference talk / slide deck)
**Year:** 2013
**PDF:** Not available — NotebookLM-hosted source (slide deck)
**Relevance:** Core
**Priority:** 1

---

## Bibliography Fields

- **title:** Data Science of Love
- **authors or organization:** Vaclav Petricek; eHarmony
- **year:** 2013
- **venue or type:** Conference talk / slide deck (Strata + QCon)
- **link:** Not available in source metadata (SlideShare deck, "Uploaded by Vaclav Petricek")
- **tier tag:** Tier 1 — Dating-platform primary source

**what they did (≤80 words):** eHarmony describes its production Compatibility Matching System: a Relationship Questionnaire scoring users on 29 psychological Dimensions®, an Affinity Matching layer using GBDT/Vowpal Wabbit over ~3,000 behavioral attributes to estimate match probability, and a Match Distribution layer applying graph optimization to spread matches across the ~40M-user network rather than scoring pairs in isolation, aimed at maximizing successful long-term relationships.

**mechanism relevant to two-sided balancing (≤50 words):** The Match Distribution graph-optimization layer explicitly aims to deliver matches "to as many people as possible across the entire network," implying some redistribution away from naive greedy pairwise matching — but no capacity limits, reciprocal-reply modeling, or fairness metric are named.

**metrics used, and the reported effect:** Only business-outcome metric: eHarmony-attributed daily marriages per Harris Interactive survey, rising from 90/day (2005) to 236/day (2007) to 542/day (2009). No model accuracy, precision/recall, or match-distribution-fairness metric reported.

**fit for a dating app:** high — reason: it is a real dating platform's own production matching architecture, directly analogous to the project's domain, though light on quantitative rigor.

**confidence that the item is real and described correctly:** high — content is grounded (all three NotebookLM queries returned `sources_used` matching this source_id), and details (29 Dimensions®, Vowpal Wabbit, graph optimization) are internally consistent and specific.

---

## Project Relevance

The Match Distribution layer is the one part of this deck that speaks to the project's core exposure-allocation concern: eHarmony explicitly reframes matching as a network-wide graph optimization problem — "delivering the right matches at the right time to as many people as possible across the entire network" — rather than treating each pair's compatibility score in isolation, which the source itself notes is meant to avoid a few popular users monopolizing matches. This is directionally aligned with the project's capacity-aware exposure allocation layer (layer 2 of the four modeling layers). However, per NotebookLM's direct answer to the reciprocal/capacity query, the source names **no per-user reply-capacity limit, no reciprocal-interest/like-back probability model, and no fairness metric** (no Gini, no share-of-users-with-≥1-match) — the graph optimization's objective function and constraints are not disclosed. It is useful as evidence that a real large-scale dating platform already treats match delivery as a global allocation problem (validating the project's framing), but it provides no transferable mechanism, formula, or metric to borrow.
