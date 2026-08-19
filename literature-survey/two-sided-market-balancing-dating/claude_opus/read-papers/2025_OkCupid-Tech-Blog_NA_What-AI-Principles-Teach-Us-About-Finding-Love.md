# Paper Analysis: What AI Principles Teach Us About Finding Love

**Source:** OkCupid Tech Blog, 2025
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** What AI Principles Teach Us About Finding Love
**Authors:** OkCupid (recommendations research team)
**Abstract:**
Consumer-facing tech blog post using the "Curse of Dimensionality" (an AI/ML concept) to explain why daters should limit simultaneous strict filters ("Dealbreakers"). Describes OkCupid's use of collaborative filtering for holistic, pattern-based matching (as opposed to rigid checklist search) and presents a simulation showing how a 1,000-user dating pool collapses as sequential filters are applied.

**Key contributions:**
- Frames excessive simultaneous filtering ("dealbreakers") as an instance of the Curse of Dimensionality, applied to dating-app search UX.
- Reports a simulation: starting from a 1,000-user pool, each additional Dealbreaker "more than halves" the remaining pool, so three Dealbreakers can eliminate >90% of options before matching even starts.
- States OkCupid uses collaborative filtering (referencing a 2021 OkCupid blog post) to find users similar to profiles previously liked, rather than exact-attribute checklist matching.
- Recommends users set only "one or two" Dealbreakers at a time.

**Methodology:**
Not a formal methodology — a narrative case study/simulation illustrating pool-size decay under progressive filter stacking, plus a general (non-technical) description of collaborative filtering as OkCupid's recommendation approach.

**Main results:**
99.8% of the OkCupid pool fails a 3-attribute conjunctive filter (6'2" AND Leo AND "jacked"), even though ~5% of users independently meet the height criterion alone. Progressive Dealbreaker stacking on a simulated 1,000-user pool leaves "only a couple" of users after several filters are applied.

---

## 2. Experiment Critique

**Design:**
No controlled experiment; a single illustrative simulation (1,000 simulated users, sequential filters) with no described methodology for how filter selectivity was chosen or how representative the simulation is of real OkCupid users.

**Statistical validity:**
Not applicable — no significance testing, confidence intervals, or real production A/B data; the headline percentages (99.8%, ~5%) are simple population statistics, not causal or comparative results.

**Online experiments (if any):**
None described.

**Reproducibility:**
Not reproducible — no dataset, code, or precise decay-curve numbers released; the simulation is illustrative only.

**Overall:**
This is consumer education content dressed in AI framing, not a rigorous evaluation. The Curse-of-Dimensionality argument is intuitively correct and a known phenomenon in recsys, but no quantitative evidence beyond the anecdotal simulation is given.

---

## 3. Industry Contribution

**Deployability:**
Describes an already-deployed practice (collaborative filtering as OkCupid's core recommendation approach, per their 2021 post) and a design/UX recommendation (limit simultaneous Dealbreakers) rather than a new deployable system.

**Problems solved:**
Addresses a real recsys UX problem — conjunctive hard-filter overuse causing catastrophic candidate-pool collapse — that is directly relevant to any filter/dealbreaker feature design in a two-sided marketplace app.

**Engineering cost:**
Low — the actionable recommendation (nudge users toward fewer simultaneous hard filters) is a UX/product change, not a new algorithm; the underlying collaborative filtering system is referenced, not newly proposed here.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** None claimed — the Curse of Dimensionality is a well-established ML concept; the post applies it to a dating-app UX problem for a lay audience.

**Prior work comparison:** The post's only cited prior work is OkCupid's own 2021 tech blog post on collaborative filtering.

**Verification:** Not specified in source — no external literature is referenced or checked against.

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Simulated 1,000-user pool | N/A | No | Illustrative simulation, not a real dataset |
| OkCupid production user statistics (e.g., ~5% users 6'2"+) | N/A | No | Internal aggregate stats cited, not released |

**Offline experiment reproducibility:**
Not reproducible — no dataset or code released.

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

**Authors:** OkCupid (recommendations research team; individual bylines not given in source)
**Affiliations:** OkCupid
**Venue:** OkCupid Tech Blog (consumer-facing blog post)
**Year:** 2025
**PDF:** Not available — web article, accessed via NotebookLM source
**Relevance:** Related
**Priority:** 2

---

## Bibliography Fields

- **title:** What AI Principles Teach Us About Finding Love
- **authors or organization:** OkCupid (recommendations research team)
- **year:** 2025
- **venue or type:** OkCupid Tech Blog (consumer-facing blog post)
- **link:** Not available in source metadata (OkCupid blog)
- **tier tag:** Tier 1 — Dating-platform primary source

**what they did (≤80 words):** OkCupid explains the "Curse of Dimensionality" for a general audience: stacking too many simultaneous hard filters ("Dealbreakers") collapses the candidate pool catastrophically, illustrated by a simulation where a 1,000-user pool shrinks to "only a couple" after a few filters, and by the fact 99.8% of users fail a 3-attribute conjunctive filter. Recommends users set only one or two Dealbreakers at a time; states OkCupid uses collaborative filtering for holistic (non-checklist) matching.

**mechanism relevant to two-sided balancing (≤50 words):** None. Per NotebookLM, the entire piece addresses unilateral search/filter optimization for a single dater; it contains no reciprocal-interest scoring, no reply-capacity concept, no exposure redistribution away from popular profiles, and no ecosystem-health metric.

**metrics used, and the reported effect:** Population statistics only: 99.8% of users fail a 3-attribute conjunctive filter (6'2" + Leo + "jacked"); ~5% of users meet the height criterion alone; simulated pool of 1,000 users shrinks by "more than half" per added Dealbreaker, with 3 Dealbreakers eliminating >90% of options. No match-outcome or fairness metric reported.

**fit for a dating app:** medium — reason: directly from a real dating platform and addresses a genuine filter-design UX problem relevant to any two-sided dating product, but it is single-user search optimization, not marketplace balancing.

**confidence that the item is real and described correctly:** high — all three NotebookLM queries returned `sources_used` matching this source_id with detailed, internally consistent, specific content (author framing, statistics, blog reference).

---

## Project Relevance

**Low project relevance.** Per NotebookLM's direct answer, this source addresses a purely unilateral, one-sided search-optimization problem (helping a single dater avoid over-filtering) and contains no reciprocal-interest scoring, no capacity/reply-limit concept, no exposure-redistribution mechanism, and no ecosystem-health metric — none of the four modeling layers in the project's framing are touched. The Curse-of-Dimensionality argument is a useful *adjacent* idea worth noting for the market-design-levers layer: it explains why letting users stack many hard dealbreaker filters can pathologically shrink the effective candidate pool on the sender's side, which is a distinct failure mode from (but could compound) the capacity/reply-side skew the project cares about — an oversupply of hard filters could suppress exposure for otherwise-compatible, non-"superstar" candidates independent of any capacity constraint. Otherwise this is background UX rationale, not a transferable mechanism, metric, or method for capacity-aware exposure allocation.
