Date: 2026-08-16 (last updated)
Topic: two-sided market balancing in dating-app recommendation

# two-sided market balancing in dating-app recommendation - Methodology Fundamentality Tracking

This file is accumulated automatically while reading PDFs during Phase 3 batch processing.
Update after each batch. Final sorting happens in Phase 3.5.

## Methodology Table

| Method Name | Proposal Paper (Year) | Baseline Mention Count | Derived Variant Count | Independent Measured Performance (Dataset: metric \| source) | Component Count | Simplicity Score (1-5) | Performance Consistency Score (1-5) | Fundamentality Composite Score |
|---|---|---|---|---|---|---|---|---|
| Gale-Shapley (stable matching) algorithm | Gale & Shapley (1962); applied by Hinge as "Most Compatible" (2018) | | | | | | | |
| TinVec (embedding-based recommendation) | Steve Liu / Tinder (MLconf SF 2017) | | | | | | | |
| Elo-style desirability score (retired) | Tinder (pre-2019; noted as retired in "Powering Tinder" 2019) | | | | | | | |
| PageRank-based desirability score | Bruch & Newman, Science Advances 2018 | | | | | | | |
| Dating Heuristic (integral / non-sequential variants) | Rios, Saban, Zheng (2023, per citation in "Platform Design in Curated Dating Markets"); assortment applied in Rios/Saban/Zheng M&SOM 2022 | | | | | | | |
| LiJAR (job application redistribution) | Borisyuk, Zhang, Kenthapadi; LinkedIn, KDD 2017 | | | | | | | |
| Impression Discounting | Lee, Lakshmanan, Tiwari, Shah; LinkedIn, KDD 2014 | | | | | | | |
| Examination-agnostic reciprocal recommendation | CyberAgent, RecSys 2023 | | | | | | | |
| BOSS (Bilateral Occupational-Suitability-Aware recommender) | BOSS Zhipin + USTC, KDD 2023 | | | | | | | |
| Two-Way Selection Preference model | BOSS Zhipin + Renmin U, RecSys 2022 | | | | | | | |
| Reciprocal Sequential Recommendation model | Zheng et al., RecSys 2023 | | | | | | | |
| MODE (Mutual Optimality in Direct Effects) | (arXiv, exact venue TBD) | | | | | | | |
| Nash Social Welfare fairness-balancing approach | (arXiv, exact venue TBD) | | | | | | | |
| Lorenz Dominance (two-sided fairness in rankings) | Do, Corbett-Davies, Atif, Usunier; Meta, NeurIPS 2021 | | | | | | | |
| Fairness of Exposure (exposure-proportional-to-relevance ranking) | Singh & Joachims, KDD 2018 | | | | | | | |
| Assortment Optimization for two-sided sequential matching | Ashlagi, Krishnaswamy, Makhijani, Saban, Shiragur, OR 2022 | | | | | | | |
| Cluster Randomization (experimental design under interference) | Holtz, F. Lobel, R. Lobel, Liskovich, Aral; Management Science 2025 (Airbnb) | | | | | | | |
| Multiple Randomization Designs | Bajari et al., arXiv 2021 | | | | | | | |
| Capacity-Constrained Recommendation | Christakopoulou, Kawale, Banerjee, CIKM 2017 | | | | | | | |

## How to Compute the Fundamentality Composite Score

Composite score = (baseline mention count × 3) + (derived variant count × 2) + (simplicity score × 1) + (performance consistency score × 2)

- baseline mention count: in how many other papers this method was used as a comparison baseline
- derived variant count: number of papers that directly modified/extended this method
  (mentions such as "based on X", "variant of X" in Related Work)
- simplicity score: 5 = 1-2 components, 4 = 3 components, 3 = 4 components, 2 = 5 components, 1 = 6+ components
- performance consistency score: higher when reported numbers across independent papers have lower variance
  (5 = stddev < 0.5%, 1 = > 3%)

## Top Method Analysis (Written in Phase 3.5)

Not yet started — populate after Phase 3 batch processing completes.
