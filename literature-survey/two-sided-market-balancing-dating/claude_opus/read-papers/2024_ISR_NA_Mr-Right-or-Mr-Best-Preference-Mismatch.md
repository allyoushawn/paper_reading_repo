# Paper Analysis: Mr. Right or Mr. Best: The Role of Information Under Preference Mismatch in Online Dating

**Source:** NotebookLM source `c5479a0f-7b8c-40be-a830-212326305de6` (Information Systems Research, 2024)
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Note:** The NotebookLM source for this paper contains only its publication metadata and abstract — the full text was not retrievable. All three queries returned `sources_used` matching the scoped source_id (technically grounded), but content is limited to what the abstract states; sections below reflect that limit.

**Title:** Mr. Right or Mr. Best: The Role of Information Under Preference Mismatch in Online Dating
**Authors:** Hongchuan Shen (University of Macau); Chu (Ivy) Dang (University of Hong Kong); Xiaoquan (Michael) Zhang (Chinese University of Hong Kong; Tsinghua University)
**Abstract:**
Uses a large field dataset from an online dating website to document real preference mismatch between the two sides of the market, then shows a "less information is more" effect: the side making a proposal has a *higher* chance of achieving a mutual match when the decision is based on the target's short/partial profile rather than their long/complete profile — because more information can sharpen an unrealistic aspiration rather than help the proposer target reciprocally reachable candidates.

**Key contributions:**
- Field evidence that preference mismatch between proposer and target is real and measurable.
- The "less information is more" finding: partial information about a candidate raises match probability versus complete information.
- Empirical isolation showing the effect is caused by preference mismatch, not some other confound.
- Managerial implication that platforms should treat **amount of information disclosed** as an active design lever, not default to maximal disclosure.

**Methodology:**
Not specified in source — empirical models comparing outcomes when proposers act on "short profile" (partial information) vs. "long profile" (complete information); exact econometric specification not available from the abstract-only extraction.

**Main results:**
Not specified in source beyond the qualitative direction: proposal decisions based on partial information convert to mutual matches at a higher rate than decisions based on complete information. No effect sizes, coefficients, or significance levels were retrievable.

---

## 2. Experiment Critique

**Design:** Not specified in source.

**Statistical validity:** Not specified in source.

**Online experiments (if any):** Not specified in source — appears to be an observational field-data study on a real dating platform's logs, not a randomized intervention, based on the abstract's framing ("we use a large data set... to provide empirical evidence").

**Reproducibility:** Not specified in source.

**Overall:** Cannot be assessed beyond the abstract's own claims; full text was not available through NotebookLM.

---

## 3. Industry Contribution

**Deployability:** The core actionable idea — deliberately limiting/curating profile information shown to a proposer before they act — is simple to implement as a UI/ranking-surface change (e.g., a condensed "first look" card vs. a full profile).

**Problems solved:** Reduces proposals sent under an inflated, information-driven aspiration that a target cannot reciprocate, which is adjacent to the project's "wasted likes" problem, though addressed via information design rather than exposure allocation.

**Engineering cost:** Low, if adopted narrowly (control what profile fields are shown at the point of decision); the paper gives no guidance on *which* fields to hide or how to determine the "optimal amount" of information for a given user pair.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First (per the abstract) to empirically demonstrate a "less information is more" effect in real two-sided-matching field data, and to attribute it causally to preference mismatch between the two sides.

**Prior work comparison:** Not specified in source — related-work section/citations not retrievable from the abstract-only extraction.

**Verification:** Not specified in source.

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Large field dataset, unnamed online dating website | N/A | No | Name/scale/platform not given in the abstract |

**Offline experiment reproducibility:** Not specified in source — dataset is proprietary to an unnamed dating platform and not described in enough detail to assess accessibility.

---

## 6. Community Reaction

Not checked — out of scope for this NotebookLM-sourced batch pass (no web search performed).

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Hongchuan Shen; Chu (Ivy) Dang; Xiaoquan (Michael) Zhang
**Affiliations:** University of Macau; University of Hong Kong; Chinese University of Hong Kong / Tsinghua University
**Venue:** Information Systems Research 35(4), pp. 2013–2029
**Year:** 2024 (published online 13 Mar 2024)
**PDF:** Not fetched directly — NotebookLM source contains abstract/metadata only, full text unavailable
**Relevance:** Related
**Priority:** 3

---

## Bibliography Fields

- **title:** Mr. Right or Mr. Best: The Role of Information Under Preference Mismatch in Online Dating
- **authors or organization:** Hongchuan Shen (University of Macau); Chu (Ivy) Dang (University of Hong Kong); Xiaoquan (Michael) Zhang (Chinese University of Hong Kong / Tsinghua University)
- **year:** 2024
- **venue or type:** Information Systems Research, 35(4):2013–2029
- **link:** https://doi.org/10.1287/isre.2022.0233
- **tier tag:** Tier 2 — Applied research / field experiments on real matching or dating platforms

**What they did (80 words max):** Used a large field dataset from an online dating website to document real preference mismatch between the two sides of the market, and showed a "less information is more" effect: proposers have a higher chance of a mutual match when acting on a candidate's short/partial profile rather than complete/long profile, because fuller information can sharpen an unrealistic aspiration instead of guiding the proposer toward reciprocally reachable candidates.

**Mechanism relevant to two-sided balancing (50 words max):** Indirect market-design lever — profile information depth/order calibrates a sender's aspiration toward realistically reciprocal targets, reducing proposals wasted on unreachable matches. No exposure-allocation, capacity, or scoring mechanism is proposed; it is purely an information-disclosure design finding.

**Metrics used, and the reported effect:** Primary outcome is match probability conditional on proposer information level (partial vs. complete profile). Direction: partial information yields a higher match rate than complete information. Exact effect sizes, sample size, and significance are Not specified in source (abstract-only extraction).

**Fit for a dating app:** medium — the underlying insight (curating disclosed information to calibrate aspiration toward reciprocally realistic targets) is a plausible, cheap market-design lever for reducing wasted proposals, but the paper contributes no capacity-aware exposure allocation, reciprocal scoring, or ecosystem-health metric, and only the abstract was accessible for verification.

**Confidence that the item is real and described correctly:** medium — `sources_used` matched the scoped source_id on all three queries (the paper is real and correctly identified: verified DOI, authors, venue, and volume/issue in the citation metadata), but NotebookLM could only surface the publication's abstract/metadata, not its body, so the described mechanism and results are trustworthy only at the level of what the published abstract itself states.

---

## Project Relevance

Modest but real relevance to modeling layer (3) market-design levers, specifically as an information-design tool for calibrating sender aspiration rather than an exposure-allocation or scoring mechanism.

What transfers: the core finding — showing a proposer *less* profile detail about a candidate can raise match probability — suggests a dating app could deliberately curate what's shown on a first-look card for over-subscribed/highly-desirable profiles, tempering unrealistic aspiration and potentially reducing the volume of likes sent that a desirable user structurally cannot reciprocate. This is a genuinely different lever from redistribution/quota mechanisms (Layer 2) — it works on the demand side (shaping what senders want) rather than the supply side (reallocating exposure).

What does not transfer: no reciprocal-scoring, capacity-awareness, or ecosystem-metric content is present even in principle — the abstract gives no indication the paper measures match spread, Gini, or two-sided retention. Because only the abstract was retrievable via NotebookLM, the actual empirical strategy, dataset, and effect sizes could not be verified; this entry should be treated as a lower-confidence, information-design-adjacent finding rather than a load-bearing citation until the full text is obtained separately.
