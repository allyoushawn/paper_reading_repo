# Paper Analysis: A/B Testing for Recommender Systems in a Two-sided Marketplace

**Source:** https://arxiv.org/pdf/2106.00762
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** A/B Testing for Recommender Systems in a Two-sided Marketplace
- **authors or company:** Preetam Nandy, Divya Venugopalan, Chun Lo, Shaunak Chatterjee (LinkedIn Corporation)
- **venue:** NeurIPS 2021
- **year:** 2021
- **URL:** https://arxiv.org/pdf/2106.00762
- **source type:** industry paper
- **direction:** D8
- **problem setting:** Producer-side (seller/creator/candidate) measurement of ranking-model treatment effects in a two-sided marketplace where SUTVA is violated — a producer's experience depends on treatment assignment of every connected consumer.
- **objective and label definition:** Not an ML training objective — UniCoRn is a post-hoc experiment-design layer on trained control/treatment scoring models T0/T1; estimation target is producer-level response Y_i aggregated over the experiment window.
- **prediction or incrementality:** Incrementality — measures average treatment effect (ATE) of ranking changes on producers, not outcome prediction.
- **model architecture:** Experiment-design algorithm (UniCoRn) blending counterfactual rankings for a sampled mixing pool per session; tunable α∈[0,1] trades design inaccuracy vs. computational cost (α=0 rescores only treatment items with zero added latency).
- **credit assignment:** Pointwise item-level: outcomes assigned to rank position R_D(i,I_s) in a consumer session; producer response Y_i aggregates position-based attention across items and sessions.
- **training data and counterfactual handling:** No training data — randomized unit is the producer/candidate/viewee split into control P0 and treatment P1; blends control and treatment counterfactual rankings to approximate unrealizable ideal rank; proved optimal for design-inaccuracy metric at α=1.
- **offline and online evaluation:** Offline synthetic simulation (bivariate-Gaussian and Beta-quality producer models) comparing MAE/RMSE and ATE-estimation error against OASIS and HaThucEtAl baselines; online production A/B tests on LinkedIn edge recommender at 40% viewer traffic (UniCoRn(0), zero added serving latency).
- **reported gains:** Candidate-generation experiment: +0.51% Weekly Active Unique users, +0.57% Sessions (p<0.001); ranking-model experiment: +0.13% WAU, +0.11% Sessions (p<0.001); offline UniCoRn variants outperform OASIS and HaThucEtAl on ATE-estimation error in synthetic simulation.
- **applicability note for a two-sided dating recommender:** Most directly transferable candidate-side A/B method — production-proven way to measure ranking changes on shown profiles without clustering or knowing the viewer-candidate graph, with explicit latency/accuracy knob α.
- **applicability note for a two-sided dating recommender:** Cannot capture treatment effects on viewer total session time or attention — candidate-side UniCoRn alone would not measure whether the viewer retained longer, only whether candidates' exposure changed; needs companion viewer-side arm for retention objective.
- **unverified claims:** Production lift numbers reported p<0.001 but without confidence intervals; authors state 40%-viewer-traffic constraint underestimates full-ramp effect.

## 1. Summary

LinkedIn addresses producer-side measurement in two-sided marketplace recommenders where standard consumer-side A/B testing violates SUTVA. Contributions: (1) "design inaccuracy" metric measuring squared error between realized and ideal counterfactual rank; (2) UniCoRn algorithm blending control/treatment counterfactual rankings per session; (3) proof of optimality at α=1 with bias/variance bounds; (4) tunable α cost/accuracy trade-off; (5) network-structure-agnostic operation; (6) production deployment in LinkedIn's edge recommender serving tens of millions of members and billions of recommendations daily.

## Project Relevance

Direct answer to **Q6** for candidate/viewee-side evaluation: concrete production-proven algorithm measuring shown-side effects without graph clustering. Speaks to **Q7** via "no cannibalization" guarantee — control and treatment items receive same rank distribution. Limitation matters for **Q1/Q3**: cannot detect viewer session-time effects; dating deployment needs companion viewer-side A/B arm. Does not address Q1–Q5 or Q8 as ML-training questions.

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | Not an ML training paper — evaluates ranking-model ATE on producers. |
| **(2) Credit assignment** | Position-based item-level assignment to producer aggregates. |
| **(3) Label / horizon; delay / sparsity / censoring** | Producer response over experiment window; no delay model beyond window. |
| **(4) Short-term vs long-term head fusion** | Not applicable. |
| **(5) Prediction vs incrementality** | Incrementality — ATE estimation. |
| **(6) Offline / online eval** | Synthetic simulation plus live LinkedIn production A/B (p<0.001). |
| **(7) Reciprocity / congestion / fairness / revenue vs match** | No-cannibalization exposure balance across candidate-side split. |
| **(8) CTR → unified long-term migration** | Not applicable — experiment design, not model training. |

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Preetam Nandy, Divya Venugopalan, Chun Lo, Shaunak Chatterjee  
**Affiliations:** LinkedIn Corporation  
**Venue:** NeurIPS 2021 (arXiv:2106.00762)  
**Year:** 2021  
**Relevance:** Core  
**Priority:** 1
