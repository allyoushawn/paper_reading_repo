# Paper Analysis: Interference, Bias, and Variance in Two-Sided Marketplace Experimentation: Guidance for Platforms

**Source:** https://arxiv.org/pdf/2104.12222
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Interference, Bias, and Variance in Two-Sided Marketplace Experimentation: Guidance for Platforms
- **authors or company:** Hannah Li, Ramesh Johari, Geng Zhao, Gabriel Y. Weintraub (Stanford University)
- **venue:** WWW 2022
- **year:** 2022
- **URL:** https://arxiv.org/pdf/2104.12222
- **source type:** academic
- **direction:** D8
- **problem setting:** Bias and variance of standard A/B-test estimators (customer-side vs. listing-side randomization) under SUTVA-violating competition in two-sided booking marketplaces (ridesharing, lodging, online matching).
- **objective and label definition:** Not an ML paper — estimation target is Global Treatment Effect (GTE), expected change in fractional bookings if intervention launched platform-wide; static one-shot booking process with no delay/censoring.
- **prediction or incrementality:** Incrementality — causal GTE estimation, not predictive modeling.
- **model architecture:** Stylized static bipartite market model (N listings × M customers, consideration→application→acceptance) yielding closed-form asymptotic bias/variance for CR and LR difference-in-means estimators as function of relative demand λ = M/N.
- **credit assignment:** Group-level only — CR/LR estimators compare aggregate booking rates between treatment and control groups; no pointwise or slate-level decomposition.
- **training data and counterfactual handling:** No training data. CR randomizes customers/viewers; LR randomizes listings/candidates. CR bias → 0 as λ→0 (demand-constrained) while LR remains biased; LR bias → 0 as λ→∞ (supply-constrained) while CR remains biased. Prior cited work puts interference bias at roughly one-third to full size of true GTE.
- **offline and online evaluation:** Offline only — closed-form asymptotic limits plus calibrated numerical simulation (M≈4.1M customers, N swept 2^16–2^28, booking rates calibrated to 20%/22% control/treatment); no online evaluation reported.
- **reported gains:** Not model-comparison gains; deliverable is bias/variance characterization — 50-50 allocation achieves variance-approximation ratio ≤1.004 relative to variance-optimal allocation (CR design); CR relative bias ranges near 0 to ~80% depending on λ in authors' calibration.
- **applicability note for a two-sided dating recommender:** Actionable evaluation guidance — use relative supply/demand of active candidates vs. viewers (λ) to choose viewer-side (CR) vs. candidate-side (LR) randomization for ranking A/B tests, with expected bias directions and rough magnitudes.
- **applicability note for a two-sided dating recommender:** Assumes no reciprocal screening, static one-shot booking — does not capture mutual-consent matching or congestion under bilateral acceptance; formulas are approximate starting point, not exact fit for dating.
- **unverified claims:** Bias-optimal design "has little effect on variance" demonstrated only in authors' calibrated simulations; practical bias magnitudes drawn from cited prior empirical studies, not this paper's own live measurement.

## 1. Summary

Stanford researchers address SUTVA violations in two-sided marketplace A/B testing where treatment and control units compete for shared supply or demand. They develop a tractable static bipartite model yielding closed-form asymptotic bias and variance for customer-side (CR) and listing-side (LR) randomization as a function of market balance λ. Key results: bias-optimal experiment type depends on whether market is demand- or supply-constrained; 50-50 allocation is robust near-MSE-optimal default; treatment allocation proportion is a bias-variance lever; sequential ramp-up designs are self-correcting for risky interventions.

## Project Relevance

Answers core of **Q6** for single ranking-model A/B tests: market-balance rule (CR vs. LR keyed to λ), bias direction/magnitude quantification, and allocation recommendation (50-50 default, ramp-up for risky changes). Does not address Q1–Q5 or Q8. Static one-shot booking without reciprocal screening means formulas approximate but do not exactly fit dating's mutual-consent structure (**Q7**).

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | Not an ML training paper — GTE estimation for marketplace interventions. |
| **(2) Credit assignment** | Group-level aggregate booking rates only. |
| **(3) Label / horizon; delay / sparsity / censoring** | Static one-shot booking; no delay model. |
| **(4) Short-term vs long-term head fusion** | Not applicable. |
| **(5) Prediction vs incrementality** | Incrementality — GTE causal estimation. |
| **(6) Offline / online eval** | Closed-form theory plus calibrated simulation only; no online experiments. |
| **(7) Reciprocity / congestion / fairness / revenue vs match** | Competition/interference modeled; no bilateral consent or congestion capacity. |
| **(8) CTR → unified long-term migration** | Not applicable. |

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Hannah Li, Ramesh Johari, Geng Zhao, Gabriel Y. Weintraub  
**Affiliations:** Stanford University  
**Venue:** WWW 2022 (arXiv:2104.12222)  
**Year:** 2022  
**Relevance:** Core  
**Priority:** 1
