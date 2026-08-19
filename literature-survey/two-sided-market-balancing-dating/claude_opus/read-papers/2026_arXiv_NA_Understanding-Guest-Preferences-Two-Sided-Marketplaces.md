# Paper Analysis: Understanding Guest Preferences and Optimizing Two-sided Marketplaces: Airbnb as an Example

**Source:** Yufei Wu, Daniel Schmierer (Airbnb, Inc.), arXiv:2607.00280v1 [cs.LG], 2026. NotebookLM source_id `254165eb-d1bc-4762-bde2-c94b7ae4a468`
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** Understanding Guest Preferences and Optimizing Two-sided Marketplaces: Airbnb as an Example
**Authors:** Yufei Wu, Daniel Schmierer
**Abstract:**
Airbnb combines economic demand modeling and observational causal inference (validated/calibrated against randomized pricing experiments) to measure guest price sensitivity on an ongoing basis, since running pricing experiments directly is low-power and interference-prone, and raw observational price/quantity data conflates guest demand response with host supply response. Also proposes a simple method to estimate price-elasticity heterogeneity across guest segments without the standard logit model's zero-market-share bias. Used to inform host pricing-guidance tools and guest-experience personalization.

**Key contributions:**
- Hybrid framework combining a BLP-style discrete-choice demand model, observational data, and an instrumental-variables identification strategy (differential geographic supply growth, controlling for realized demand) to estimate guest price elasticity without running a live pricing experiment.
- Calibration procedure: compare observational estimates to ground-truth pricing-experiment results and apply an empirical "haircut" correction for observed upward bias.
- A tractable estimator for guest-segment-level price-elasticity heterogeneity that avoids dropping/mis-imputing zero-share segments (a known logit-model pathology).

**Methodology:**
Multinomial logit discrete-choice demand model (guest utility linear in price and product attributes, Type-I extreme-value error) linearized via the Berry-Levinsohn-Pakes (BLP, 1995) approach into a regression; price identified via an instrumental-variables strategy using geographic differences in supply growth (driven by regulation/cost heterogeneity) as a plausibly exogenous shifter, conditional on realized demand (listing views); segment-level elasticity heterogeneity estimated via a derived log-share panel regression.

**Main results:**
Observational IV-based elasticity estimates, once calibrated against randomized pricing experiments via a "haircut" adjustment, closely matched subsequent independent experimental results. Demonstrated a real geographic example: Geo B (faster relative supply growth, ~60% more than Geo A conditional on demand) saw prices fall ~13% vs. Geo A's +4%, consistent with the identified supply-driven price mechanism.

---

## 2. Experiment Critique

**Design:** Combines quasi-experimental (IV) identification from observational data with genuine randomized pricing experiments used purely as a calibration/validation benchmark — a reasonable design given the authors' own acknowledgment that direct pricing experiments are low-power and suffer interference bias in a marketplace.

**Statistical validity:** Explicit and honest treatment of identification assumptions: authors state plainly that the IV exclusion restriction "is not possible" to prove, and rely on experimental calibration instead of asserting unconditional validity — an unusually rigorous and self-critical stance for an industry paper.

**Online experiments (if any):** Randomized pricing experiments are used as ground truth/calibration only, not as the primary estimation method (motivated by their stated low statistical power and interference concerns in a two-sided marketplace).

**Reproducibility:** Model equations and IV strategy fully specified; underlying Airbnb global production data (5M+ hosts, 1.5B guest arrivals) is proprietary and not released.

**Overall:** A methodologically careful causal-inference paper; the explicit combination of observational IV + experimental calibration, and the stated unprovability of the exclusion restriction, reflect strong intellectual honesty about the method's limits.

---

## 3. Industry Contribution

**Deployability:** Already used in production to power host pricing-guidance tools and guest-experience/marketing personalization at Airbnb.

**Problems solved:** Ongoing, granular measurement of guest price sensitivity without needing continuous live pricing experiments; used explicitly as "a lever to balance supply and demand" in a two-sided marketplace.

**Engineering cost:** Moderate — requires an observational causal-inference pipeline (IV construction from geographic supply-growth data, BLP-style estimation, periodic recalibration against experiments) rather than new online infrastructure.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** A practical solution to the standard logit zero-market-share bias for estimating preference heterogeneity across small guest segments, plus the applied combination of a supply-growth-based IV with experimental calibration in a live two-sided marketplace setting.

**Prior work comparison (top cited works per source):**
1. Berry, Levinsohn & Pakes 1995, "Automobile Prices in Market Equilibrium" — the "BLP" method the demand-estimation approach is built on.
2. Gandhi & Nevo 2021 — on bias from dropping/misassigning zero-share observations in logit models.
3. Dubé et al. 2021 and Gandhi et al. 2023 — alternative zero-share correction methods, noted as requiring restrictive assumptions or giving only partial identification (motivating this paper's simpler alternative).
4. Holtz et al. 2020, "Reducing Interference Bias in Online Marketplace Pricing Experiments."
5. Johari et al. 2022, "Experimental Design in Two-Sided Platforms: An Analysis of Bias."
6. Le & Deng 2023, "The Price is Right: Removing A/B Test Bias in a Marketplace of Expirable Goods."
7. Ye et al. 2018 (Airbnb Pricing team, KDD) and Grbovic 2017 / Grbovic & Cheng 2018 (Airbnb Relevance team, KDD) — sister Airbnb pricing/personalization systems this paper's estimates feed into.

**Verification:** Novelty claim (a simple, easy-to-implement zero-share correction, and combined IV+experimental-calibration pipeline in production) is plausible and well-situated relative to the cited zero-share-bias literature; not independently checked against the broader econometrics literature.

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Airbnb global production data: 5M+ hosts, 1.5B guest arrivals, 100,000+ cities | — | Not accessible (proprietary) | Internal only |
| Randomized pricing experiments (used for calibration) | — | Not accessible (proprietary) | Internal only |

**Offline experiment reproducibility:** Not reproducible outside Airbnb — proprietary data; the estimation methodology (equations, IV construction) is fully specified and could be reimplemented on comparable marketplace data.

---

## 6. Community Reaction

Not assessed for this source (out of scope for Phase 3 batch processing).

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Yufei Wu, Daniel Schmierer
**Affiliations:** Airbnb, Inc., San Francisco, California, USA
**Venue:** arXiv preprint (2607.00280v1, cs.LG), 2026
**Year:** 2026
**PDF:** Not fetched — analyzed via NotebookLM source; not accessed as local file
**Relevance:** Peripheral — rigorous single-sided (guest) demand-elasticity estimation method; explicitly confirmed to have no reciprocity, capacity, or exposure-redistribution content
**Priority:** 3 (per queue tier, downgraded from Tier 1 listing due to single-sidedness confirmed by Query 3)

---

## Bibliography Fields

- **title:** Understanding Guest Preferences and Optimizing Two-sided Marketplaces: Airbnb as an Example
- **authors or organization:** Yufei Wu, Daniel Schmierer — Airbnb, Inc.
- **year:** 2026
- **venue or type:** arXiv preprint (2607.00280v1, cs.LG)
- **link:** https://arxiv.org/abs/2607.00280
- **tier tag:** Tier 1 — Adjacent marketplace (home rental), pricing/demand-elasticity estimation
- **what they did (≤80 words):** Combined a BLP-style discrete-choice demand model with an instrumental-variables strategy (geographic supply-growth differences, controlling for realized demand) to estimate guest price elasticity from observational data without running a live pricing experiment, calibrated the estimates against ground-truth randomized pricing experiments via a "haircut" correction, and proposed a simple estimator for price-elasticity heterogeneity across guest segments that avoids standard logit zero-market-share bias.
- **mechanism relevant to two-sided balancing (≤50 words):** None on the reciprocity/capacity axis — the model is a unilateral guest-choice/demand-elasticity estimator; "two-sided" in the title refers only to using host-side price/supply variation as an instrument, not to modeling host acceptance capacity, reciprocal matching, or exposure redistribution.
- **metrics used, and the reported effect:** Guest price elasticity of demand (BLP-derived); observational-vs-experimental estimate agreement after "haircut" calibration (reported as closely matching); illustrative geo example: Geo B price −13% vs. Geo A +4%, explained by ~60% relative supply-growth differential.
- **fit for a dating app:** low — this is a rigorous causal-inference method for price/demand elasticity in a priced marketplace; the source's own Query-3 answer confirms no reciprocal-acceptance modeling, no capacity limits, no exposure redistribution, and no market-design levers beyond price guidance — dating apps generally have no price lever, and the paper explicitly optimizes single-sided guest conversion, not marketplace balance metrics.
- **confidence that the item is real and described correctly:** high (NotebookLM grounded answer with extensive direct quotes and equations across all three queries, source_id validated each time, matches a real identifiable arXiv preprint with named authors/affiliation).

---

## Project Relevance

**Low project relevance.** Despite the title's "optimizing two-sided marketplaces," the source's own Query-3 answer is explicit: the paper is "almost entirely single-sided." It models guest (unilateral) choice and price sensitivity via a standard multinomial logit with no host-acceptance-probability or reciprocal-matching term, imposes no capacity constraints on the host side, does not redistribute exposure away from over-booked listings, and its only "market-design lever" is price guidance to hosts — which has no analogue in a dating app (no price mechanism to clear the market). Its metrics (price elasticity, guest conversion share) are single-sided guest-conversion metrics, not ecosystem-health measures like match spread or wasted likes. The one transferable idea is methodological rather than mechanistic: the paper's discipline of validating/calibrating an observational causal estimate against a randomized experiment (the "haircut" correction) is a good general pattern for the project's own experimentation-under-interference layer, where full randomized tests of exposure-redistribution policies may also be low-power/interference-prone in a dating marketplace. Otherwise this source does not address the project's reciprocal-scoring, capacity-aware-allocation, or market-design-lever layers.
