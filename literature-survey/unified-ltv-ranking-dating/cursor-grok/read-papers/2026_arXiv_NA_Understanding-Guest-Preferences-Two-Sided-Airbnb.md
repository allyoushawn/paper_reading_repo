# Paper Analysis: Understanding Guest Preferences and Optimizing Two-sided Marketplaces: Airbnb as an Example

**Source:** https://arxiv.org/pdf/2607.00280.pdf
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** Understanding Guest Preferences and Optimizing Two-sided Marketplaces: Airbnb as an Example
- **authors or company:** Yufei Wu, Daniel Schmierer (Airbnb)
- **venue:** arXiv
- **year:** 2026
- **URL:** https://arxiv.org/pdf/2607.00280.pdf
- **source type:** industry paper
- **direction:** D8
- **problem setting:** Airbnb two-sided marketplace where hosts set prices (Airbnb does not); platform needs ongoing measurement of guest price sensitivity and preference heterogeneity to optimize host pricing tools and personalize guest search/ranking — experiments on pricing face interference and low power.
- **objective and label definition:** Guest demand modeled via logit choice; price elasticity of demand estimated from host-set prices; segment-level heterogeneity in price sensitivity derived from how guest mix shifts with price; labels are booking/conversion shares by guest segment and geo-time panel — not a ranker training objective.
- **prediction or incrementality:** Causal price elasticity via supply-based instrumental variables isolating supply-driven price variation conditional on demand; observational estimates calibrated ("haircut") against pricing experiments — not incrementality of a ranked impression on retention.
- **model architecture:** Economics stack: logit demand model + supply-based IV for price; panel regression linking segment conversion shares to price (Equation 6) to recover heterogeneous elasticities; validated/calibrated against designed pricing experiments.
- **credit assignment:** Geo-time panel attribution of guest-mix changes to price movements; not impression-level delayed retention credit assignment.
- **training data and counterfactual handling:** Observational marketplace data with supply-driven IVs; initial calibration to low-interference pricing experiments; ongoing updates as new experiments arrive; acknowledges exclusion-restriction limitations.
- **offline and online evaluation:** No new online A/B test of a ranker; method validated by comparing observational elasticity estimates to experimental ground truth and subsequent confirmatory experiments.
- **reported gains:** Enables ongoing guest price-sensitivity measurement where experiments are impractical; segment heterogeneity insights inform host pricing tools and guest personalization (e.g., affordable-listing marketing for price-sensitive segments).
- **applicability note for a two-sided dating recommender:** Analogous two-sided marketplace where the platform does not set "prices" (hosts set listing prices; dating apps may set boost pricing) — IV + experiment-calibration pattern for measuring heterogeneous guest/user sensitivity when randomized tests are constrained.
- **applicability note for a two-sided dating recommender:** Does not describe ranking model architecture, match outcomes, reciprocity, or retention/LTV objectives; demand/elasticity focus not swipe/match funnel optimization.
- **unverified claims:** none

## 1. Summary

**Title:** Understanding Guest Preferences and Optimizing Two-sided Marketplaces: Airbnb as an Example
**Authors:** Yufei Wu, Daniel Schmierer (Airbnb Pricing Modeling)
**Abstract:** Combines economic modeling and causal inference to measure guest price elasticity and preference heterogeneity from observational data, complementing low-power pricing experiments.

**Key contributions:**
- Supply-based instrumental variables to estimate guest price elasticity when Airbnb cannot directly vary host prices.
- Experiment-calibrated observational pipeline for ongoing measurement and segment heterogeneity.
- Framework for personalizing guest experience and host pricing tools from elasticity insights.

**Methodology:** Logit demand model; IV isolating supply-driven price variation across geographies; panel regression for segment-level elasticity; validation against designed pricing experiments with bias haircut.

**Main results:** Observational estimates align with experimental ground truth after calibration; method supports continuous measurement and heterogeneity analysis where experiments are costly or infeasible.

## 2. Experiment Critique

**Design:** Honest treatment of observational limitations (exclusion restriction unprovable); dual use of experiments for calibration not just ground truth.

**Statistical validity:** IV and panel methods standard in economics; calibration procedure described qualitatively; no new quantitative A/B results in this paper.

**Online experiments (if any):** References prior Airbnb pricing experiments for calibration; no new ranker A/B reported.

**Reproducibility:** Airbnb proprietary data; method description at economics-survey level, not full estimation code.

**Overall:** Useful marketplace measurement playbook; thin on ranking-system specifics despite citing prior Airbnb search-ranking personalization work.

## 3. Industry Contribution

**Deployability:** Ongoing observational measurement pipeline for host pricing products and guest personalization segments.

**Problems solved:** Low statistical power and interference in marketplace pricing experiments; need for continuous elasticity monitoring as guest preferences shift.

**Engineering cost:** Economics/ML hybrid team capability; IV construction and experiment calibration infrastructure.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Integrated observational + experimental calibration workflow for two-sided marketplaces with host-set prices.

**Prior work comparison:** Prior Airbnb KDD pricing model (Ye et al.); search personalization (Grbovic); marketplace experiment interference (Holtz, Johari, Le & Deng); logit heterogeneity methods (Gandhi & Nevo, Dubé et al.).

**Verification:** Calibration narrative supported by comparison to historical experiments; this paper is primarily methodological exposition, not a new benchmark result.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Airbnb guest/host marketplace logs | Proprietary | No | Geo-panel observational + experiment calibration |

**Offline experiment reproducibility:** Not reproducible without Airbnb data.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**Low–moderate relevance for unified LTV ranking; moderate for D8 marketplace measurement infrastructure.**

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | Not a ranking paper; informs personalization and pricing tools that feed into search ranking indirectly. |
| **(2) Credit assignment** | Not applicable to impression-level ranking. |
| **(3) Label / horizon; delay / sparsity / censoring** | Booking/conversion shares; no delayed retention labels. |
| **(4) Short-term vs long-term head fusion** | Not applicable. |
| **(5) Prediction vs incrementality** | Causal elasticity estimation, not exposure incrementality on retention. |
| **(6) Offline / online eval** | Experiment validation of observational method; no ranker A/B. |
| **(7) Reciprocity / congestion / fairness / revenue vs match** | Two-sided guest/host marketplace; host pricing and guest affordability — analog to supply/demand balance, not bilateral matching. |
| **(8) CTR → unified long-term migration** | Not applicable. |

Relevant as marketplace **measurement** context for when dating platforms cannot experiment freely on economically salient levers.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Yufei Wu, Daniel Schmierer
**Affiliations:** Airbnb, Inc.
**Venue:** arXiv (cs.LG)
**Year:** 2026
**PDF:** https://arxiv.org/pdf/2607.00280.pdf
**Relevance:** Peripheral
**Priority:** 3
**Card date:** 2026-08-17
**Workplace:** cursor-grok
**Reader:** PDF only
