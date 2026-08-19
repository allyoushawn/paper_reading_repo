# Paper Analysis: The Proximal Surrogate Index: Long-Term Treatment Effects under Unobserved Confounding

**Source:** https://arxiv.org/abs/2601.17712
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** The Proximal Surrogate Index: Long-Term Treatment Effects under Unobserved Confounding
- **authors or company:** Ting-Chih Hung, Yu-Chang Chen (National Taiwan University)
- **venue:** arXiv
- **year:** 2026
- **URL:** https://arxiv.org/abs/2601.17712
- **source type:** academic paper
- **direction:** D3
- **problem setting:** Estimate long-term treatment effect \(\tau_0 = E[Y(1)-Y(0) \mid G=E]\) when experimental sample has treatment \(A\) and short-term surrogates \(S\) but not long-term outcome \(Y\), while observational sample has \(Y\) and \(S\) but not \(A\) — unobserved confounders \(U\) may violate standard surrogate-index assumptions.
- **objective and label definition:** Primary outcome \(Y\) (e.g. year-4 weekly earnings, weeks employed); surrogates \(S\) (years 2–3 earnings/employment); proxies \(W\) (outcome-aligned, both samples) and \(Z\) (surrogate-aligned, observational only); experimental ATE on \(Y\) is estimand — not a ranking model training loss.
- **prediction or incrementality:** Identifies and estimates causal ATE on long-term \(Y\) via proximal surrogate index \(h_0(W,S,X)\) and multiply robust DML estimators — causal effect estimation, not predictive ranking of retention conditional on exposure.
- **model architecture:** Two bridge strategies: outcome bridge \(h_0\) imputes \(Y\) in experimental sample; surrogate bridge \(q_{a,0}\) reweights observational sample; multiply robust influence function \(\phi(D;\eta)\) combining experimental IPW/AIPW and observational reweighting; cross-fitted \(\hat\tau_{MR}\) with semiparametric efficiency bound.
- **credit assignment:** Unit-level causal estimand — no item-level or slate-level credit assignment; surrogates \(S\) mediate \(A \to Y\) under no-direct-effect assumption; proxies adjust for \(U\) confounding \(S\)–\(Y\) and \(A\)–\(Y\) relationships.
- **training data and counterfactual handling:** Two-sample design: RCT stratum (\(A,S,X,W\)) + observational stratum (\(Y,S,X,Z,W\)); Job Corps application masks \(Y\) in half of RCT and \(A\) in observational split to benchmark estimators; assumes transportability of \(Y,W\) given \((S,X,U)\).
- **offline and online evaluation:** Simulation-free empirical benchmark on Job Corps vs RCT ground truth; standard surrogate index underestimates effects (earnings ATE 7.05 vs RCT 15.30); proximal method 16.43; diagnostic regressions test surrogacy violation (significant \(A\) coef in OLS, insignificant after IV adjustment with proxies).
- **reported gains:** Proximal estimator closer to RCT benchmark than naive surrogate index for 4-year earnings (16.43 vs 7.05–7.30) and weeks employed (3.50 vs 0.80–0.84); larger standard errors than naive methods.
- **applicability note for a two-sided dating recommender:** Framework for validating short-term ranking proxies (match, conversation) against delayed retention when logged experiments lack long horizons and observational retention logs lack clean treatment labels — directly relevant to surrogate-metric design under hidden user quality confounders.
- **applicability note for a two-sided dating recommender:** Labor-economics setting with no recommender, reciprocity, or congestion; requires explicit proxy variables \(W,Z\) for unobserved confounders and no direct \(A \to Y\) path — assumptions must be mapped carefully to dating experiments before adopting estimators.
- **unverified claims:** none

## 1. Summary

This paper extends the surrogate index (Athey et al. 2025b) to allow unobserved confounding by combining experimental and observational samples with proximal outcome-aligned and surrogate-aligned proxies. Outcome and surrogate bridge functions yield a multiply robust ATE estimator with DML inference. On Job Corps, the proximal surrogate index recovers experimental long-term treatment effects that standard surrogate-index regression substantially underestimates when surrogacy is violated.
