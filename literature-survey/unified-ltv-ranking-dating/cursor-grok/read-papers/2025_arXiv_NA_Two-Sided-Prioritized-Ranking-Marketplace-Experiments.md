# Paper Analysis: Two-Sided Prioritized Ranking: A Coherency-Preserving Design for Marketplace Experiments

**Source:** https://arxiv.org/pdf/2502.09806.pdf
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** Two-Sided Prioritized Ranking: A Coherency-Preserving Design for Marketplace Experiments
- **authors or company:** Mahyar Habibi (Lyft), Zahra Khanalizadeh (University of Washington), Negar Ziaeian (University of Warwick)
- **venue:** arXiv
- **year:** 2025 (v2 March 2026)
- **URL:** https://arxiv.org/pdf/2502.09806.pdf
- **source type:** academic paper (industry-affiliated)
- **direction:** D8
- **problem setting:** Item-side interventions (e.g., pricing) in ranked-list marketplaces where items interfere within a query, user-level A/B tests violate price/catalog coherency, and item-level A/B tests are biased by spillovers.
- **objective and label definition:** Estimand is global lift Φ — proportional change in query-level outcomes when all items are treated vs. all untreated; outcomes y_{q,i} are clicks, bookings, or revenue aggregated per query; not a recommender ranking objective.
- **prediction or incrementality:** Causal experimental-design framework; uses recommender relevance scores only to break ties within priority tiers, not to optimize ranking quality.
- **model architecture:** Two-Sided Prioritized Ranking (TSPR): randomize items into Treated/Untreated/Placebo (probabilities p, p, 1−2p); randomize each query to group QA or QB; reorder lists so QA prioritizes Untreated→Placebo→Treated and QB prioritizes Treated→Placebo→Untreated, secondary sort by relevance score.
- **credit assignment:** Not applicable — paper designs experiments to estimate global treatment effects under within-list interference (limited attention + unit-demand substitution), not per-impression delayed outcome attribution.
- **training data and counterfactual handling:** Semi-synthetic Monte Carlo simulations calibrated to open-source Expedia hotel search data with estimated click/booking behavioral models; compares TSPR to item-level Bernoulli randomization and cluster-randomized baselines.
- **offline and online evaluation:** Simulation-only; no live platform A/B test. Authors report TSPR substantially reduces bias and variance vs. item-level A/B and strongly outperforms cluster randomization on estimate variance.
- **reported gains:** Monte Carlo evidence that TSPR identifies global treatment effect under coherency constraints where user-level and naive item-level designs fail; semi-synthetic Expedia calibration.
- **applicability note for a two-sided dating recommender:** Directly relevant to **how** to run marketplace experiments when profile boosts/pricing-like interventions create interference and coherency constraints — uses ranking position bias as identification lever rather than changing the ranker objective.
- **applicability note for a two-sided dating recommender:** Does not address retention/LTV ranking, reciprocal matching integrators, or credit assignment; assumes slack supply and negligible user-side interference across queries.
- **unverified claims:** none

## 1. Summary

**Title:** Two-Sided Prioritized Ranking: A Coherency-Preserving Design for Marketplace Experiments
**Authors:** Habibi, Khanalizadeh, Ziaeian
**Abstract:** Proposes TSPR, an experimental design for item-side interventions in ranked marketplaces that preserves price parity and full catalog access while exploiting position bias to vary treatment exposure across user groups.

**Key contributions:**
- Formalizes coherency constraints (same item treatment for all users; full catalog access) that rule out standard user-level and two-sided-randomization designs.
- TSPR design randomizing users and items with group-specific list reordering to identify global lift under interference.
- Semi-synthetic Expedia-based simulations showing reduced bias and improved power vs. baselines.

**Methodology:** Ranked-list marketplace model with position bias; identification conditions for proportional global treatment effect; Monte Carlo evaluation against Bernoulli item-level and cluster-randomized designs.

**Main results:** TSPR substantially reduces bias and variance relative to item-level A/B tests and outperforms cluster randomization on variance of global lift estimates in calibrated simulations.

## 2. Experiment Critique

**Design:** Well-motivated by real marketplace constraints (price parity, catalog coherency, Instacart/Amazon backlash examples); clear contrast with switchbacks, cluster randomization, exposure-based designs, and interleaving.

**Statistical validity:** Identification theorem under stated assumptions (position bias, sufficient relevant items per query, slack supply); Monte Carlo evidence on bias/variance tradeoffs.

**Online experiments (if any):** None — simulation only on Expedia hotel search data.

**Reproducibility:** Expedia dataset is open; simulation code availability not stated in source.

**Overall:** Strong methodological contribution for marketplace experiment design; external validity to dating feed ranking experiments requires validating position-bias and slack-supply assumptions.

## 3. Industry Contribution

**Deployability:** Conceptually deployable wherever platforms control list ordering and can randomize item treatment without varying per-user prices; legal/reputational coherency constraints are central motivation.

**Problems solved:** Biased item-level A/B tests under within-list interference; infeasibility of user-level price experiments in coherency-constrained marketplaces.

**Engineering cost:** Requires coordinated item randomization plus query-group-specific reordering atop existing ranker; simpler than cluster designs in some settings but needs sufficient list depth per query.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First coherency-preserving design using prioritized ranking to shift treatment exposure via position bias; differs from ranking-algorithm experiments and interleaving methods.

**Prior work comparison:** Builds on interference literature (Hudgens & Halloran, Manski, Munro); two-sided randomization (Johari, Bajari, Li); ranking position bias (Craswell, Joachims); marketplace experiment constraints (Blake & Coey, Fradkin).

**Verification:** Simulation evidence supports bias/variance claims; no field validation in source.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Expedia hotel search (open source) | Public | Yes | Used for semi-synthetic behavioral calibration |

**Offline experiment reproducibility:** Partially reproducible with Expedia data; proprietary marketplace deployment details not applicable.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**Moderate relevance for D8 (two-sided marketplace experiment infrastructure), low for unified LTV ranking.**

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | Not a ranking objective paper; estimand is global treatment lift on query outcomes. |
| **(2) Credit assignment** | Not applicable. |
| **(3) Label / horizon; delay / sparsity / censoring** | Not applicable to model training. |
| **(4) Short-term vs long-term head fusion** | Not applicable. |
| **(5) Prediction vs incrementality** | Causal experiment design for item-side interventions under interference. |
| **(6) Offline / online eval** | Semi-synthetic Monte Carlo only. |
| **(7) Reciprocity / congestion / fairness / revenue vs match** | Within-list item competition and substitution; two-sided market framing but not reciprocal user matching. |
| **(8) CTR → unified long-term migration** | Not applicable. |

Useful when dating platforms need coherency-preserving experiments on boosts, pricing-like features, or item-side treatments in ranked profile lists where standard A/B designs are biased.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Mahyar Habibi, Zahra Khanalizadeh, Negar Ziaeian
**Affiliations:** Lyft; University of Washington; University of Warwick
**Venue:** arXiv (econ.EM)
**Year:** 2025
**PDF:** https://arxiv.org/pdf/2502.09806.pdf
**Relevance:** Related
**Priority:** 2
**Card date:** 2026-08-17
**Workplace:** cursor-grok
**Reader:** PDF only
