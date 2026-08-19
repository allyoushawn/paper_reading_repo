# Paper Analysis: The Proximal Surrogate Index: Long-Term Treatment Effects under Unobserved Confounding

**Source:** /Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/2601.17712.pdf
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** The Proximal Surrogate Index: Long-Term Treatment Effects under Unobserved Confounding
**Authors:** Ting-Chih Hung, Yu-Chang Chen (National Taiwan University)
**Venue:** arXiv (econ.EM), Jan 27, 2026

**Abstract (from source):** The paper studies the identification and estimation of long-term treatment effects under unobserved confounding by combining an experimental sample (long-term outcome missing) with an observational sample (treatment assignment unobserved). Standard surrogate index methods fail when unobserved confounders exist; the authors establish novel identification results by leveraging proxy variables for the unobserved confounders, and develop multiply robust estimation and inference procedures based on these results. Applied to the Job Corps program, the method recovers experimental benchmarks even when unobserved confounders bias standard surrogate index estimates.

**Key contributions:**
1. Extends the standard surrogate index (Athey et al., 2025b — the published/updated version of the 2019 NBER surrogate index paper) to a data-combination setting where the experimental sample lacks the long-term outcome AND the observational sample lacks the treatment indicator, while allowing unobserved confounders U to affect both the treatment/outcome relationship and the surrogate/outcome relationship (violating the standard method's surrogacy and comparability assumptions).
2. Introduces two classes of proxy variables for U — outcome-aligned proxies W (observed in both samples) and surrogate-aligned proxies Z (observed only in the observational sample) — drawing on the proximal causal inference literature (Miao et al., 2018).
3. Establishes nonparametric identification via two complementary "bridge functions": an outcome bridge function (imputes the missing long-term outcome in the experimental sample) and a surrogate bridge function (reweights the observational sample to the experimental target), then combines them into a multiply robust identification formula valid if any one of four alternative sets of nuisance functions is correctly specified.
4. Develops cross-fitted double/debiased machine learning (DML) estimators with proven consistency, asymptotic normality, and semiparametric local efficiency, and applies them to a real Job Corps dataset.

**Methodology.** Two samples: an experimental sample E with (A, S, X) observed but Y missing, and an observational sample O with (Y, S, X, Z, W) observed but A missing. Key assumptions: no direct effect of treatment A on long-term outcome Y except through the surrogate S (Assumption 2, mirroring the standard surrogacy assumption); unconfoundedness given observed covariates and the *unobserved* U within each sample (Assumptions 3-4); proxy availability with specific conditional-independence conditions defining W as "outcome-aligned" and Z as "surrogate-aligned" (Assumption 5); and transportability of the conditional distributions of Y and W (but notably not Z) across the two samples (Assumption 6). Theorem 1 identifies the ATE via an outcome bridge function h0 that must satisfy a completeness condition (Assumption 8); Theorem 2 gives an alternative identification via a surrogate bridge function q that reweights observational-sample outcomes; Theorem 3 combines both into a multiply robust estimator valid under any one of four correctly specified nuisance-function combinations. Section 5 develops cross-fitted DML estimators (outcome-regression, IPW, surrogate-bridge, and multiply-robust variants) with K-fold cross-fitting, proving consistency, asymptotic normality (under a "product rate" condition weaker than requiring both nuisance estimators individually to converge fast), and semiparametric efficiency under a surjectivity condition guaranteeing unique bridge functions.

**Main results.** Applied to the National Job Corps Study (a large RCT evaluating a U.S. job-training program for disadvantaged youth), with the single experimental dataset artificially split into a synthetic "experimental sample" (long-term outcome masked) and "observational sample" (treatment status masked) to create a benchmark with a known ground-truth ATE. Long-term outcome Y = weekly earnings / proportion of weeks employed in program year 4; surrogates S = the same outcomes in years 2-3; outcome-aligned proxy W = GED possession and English mother tongue (pre-treatment); surrogate-aligned proxy Z = a post-training survey on job-search self-efficacy. The standard surrogate index substantially underestimates the RCT benchmark ($7.05 vs. $15.30 weekly earnings), while the proposed proximal surrogate index recovers an estimate much closer to the benchmark ($16.43), albeit with a notably larger standard error.

## 2. Experiment Critique

**Design.** A theoretical identification-and-estimation paper with a single real-data application: the National Job Corps Study RCT, artificially split into synthetic experimental/observational halves of the *same* completed trial. This design guarantees, by construction, that there is no genuine cross-sample selection bias, isolating whether the standard surrogate index's known failure mode (unobserved confounding) alone explains the bias observed — a clean but artificial test.

**Statistical validity.** The paper proves consistency (Theorem 4), asymptotic normality (Theorem 5) under a "product rate" convergence condition for the DML nuisance estimators, and semiparametric local efficiency (Theorems 7-8) under a completeness/surjectivity condition on the bridge-function operators. The applied example uses linear bridge functions and reports standard errors via a plug-in sandwich estimator under a joint GMM framework.

**Online experiments.** None — this is an offline econometric identification/estimation paper. The Job Corps application is itself a retrospective RCT dataset, not a new experiment.

**Reproducibility.** Full proofs are given in an appendix; the Job Corps dataset is described as publicly available via the `causalweight` R package (Bodory, Huber, Kueck, 2025), so the applied example is, in principle, independently reproducible — unusually so among the papers in this batch.

**Overall.** Rigorous, formal econometric contribution. Its own diagnostic analysis (Table 4 in source) provides direct empirical evidence, within the Job Corps data, that the standard surrogacy assumption is in fact violated (the treatment coefficient remains significant even after conditioning on the surrogate), which substantiates the paper's motivating claim rather than merely asserting it.

## 3. Industry Contribution

**Deployability.** Low to moderate. The method requires identifying and collecting two distinct classes of proxy variables (outcome-aligned W, surrogate-aligned Z) for an unobserved confounder, satisfying nontrivial conditional-independence and completeness conditions that are themselves unverifiable in general — this is a substantially higher data-engineering and domain-knowledge bar than either other paper in this batch.

**Problems solved.** Directly targets bias from unobserved confounding in surrogate-index-style long-term-effect estimation, the exact failure mode this project faces (active users see more candidates and retain more for reasons the model does not observe).

**Engineering cost.** Not a ranking-model or serving-latency cost — this sits entirely in the offline causal-estimation/experiment-evaluation layer, requiring cross-fitted DML estimation (K-fold nuisance-function fitting) plus sourcing of valid proxy variables, a research and data-collection cost rather than an infrastructure one.

## 4. Novelty vs. Prior Work

**Claimed novelty.** The first extension of the surrogate index to a data-combination setting with confounding on *both* sides of the front-door-style decomposition (treatment→surrogate and surrogate→outcome), using proximal causal inference (proxy variables + bridge functions) rather than assuming no unobserved confounding as the standard surrogate index does; a new multiply robust identification result (Theorem 3) that is stated as novel to the literature even relative to prior proximal-inference work.

**Prior work named in the source (5-7 most relevant):**
- Athey, Chetty, Imbens, Kang, "The surrogate index: Combining short-term proxies to estimate long-term treatment effects more rapidly and precisely," Review of Economic Studies, 2025b — "the most related work"; the standard method this paper extends and empirically outperforms.
- Miao, Geng, Tchetgen Tchetgen, "Identifying causal effects with proxy variables of an unmeasured confounder," Biometrika, 2018 — foundational proximal causal inference paper underlying the proxy-variable approach.
- Prentice, "Surrogate endpoints in clinical trials: definition and operational criteria," Statistics in Medicine, 1989 — origin of the surrogacy assumption being relaxed.
- Tchetgen Tchetgen, Ying, Cui, Shi, Miao, "An introduction to proximal causal inference," Statistical Science, 2024.
- Chernozhukov, Chetverikov, Demirer, Duflo, Hansen, Newey, Robins, "Double/debiased machine learning for treatment and structural parameters," The Econometrics Journal, 2018 — source of the cross-fitting/DML estimation approach used.
- Imbens, Kallus, Mao, Wang, "Long-term causal inference under persistent confounding via data combination," Journal of the Royal Statistical Society Series B, 2025 — closely related data-combination-plus-confounding setting.
- Chen and Ritzwoller, "Semiparametric estimation of long-term treatment effects," Journal of Econometrics, 2023.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| National Job Corps Study (Schochet et al., 2001, 2008) | Government-sponsored RCT, US job-training program for disadvantaged youth | Yes | Publicly available via the `causalweight` R package (Bodory, Huber, Kueck, 2025); artificially split by the authors into synthetic experimental/observational halves for this paper's demonstration |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | The Proximal Surrogate Index: Long-Term Treatment Effects under Unobserved Confounding; Ting-Chih Hung, Yu-Chang Chen (National Taiwan University); arXiv (econ.EM), Jan 27, 2026; https://arxiv.org/abs/2601.17712 |
| 2 | Source type | Academic |
| 3 | Direction | D3 |
| 4 | Problem setting | Identifying and estimating the long-term average treatment effect (ATE) when it must be recovered from two separate, incomplete data sources — an experimental sample with randomized treatment but missing long-term outcome, and an observational sample with the long-term outcome but missing treatment status — in the presence of unobserved confounders U that bias the standard surrogate-index method. |
| 5 | Objective and label definition | Estimand τ0 = E[Y(1) − Y(0) \| G=E], the ATE on a scalar long-term outcome Y (applied example: weekly earnings and proportion of weeks employed in program year 4) in the experimental sample. Horizon in the applied example is 4 years post-random-assignment; short-term "surrogates" S are the same two outcome types measured in years 2-3. Delay/missingness is handled structurally rather than by a horizon cutoff: Y is never observed in the experimental sample and A is never observed in the observational sample, and the bridge functions statistically reconstruct the joint relationship rather than censoring or truncating any observation. |
| 6 | Prediction or incrementality | Incrementality, explicitly and formally. The entire paper is a causal-identification and semiparametric-efficient-estimation exercise for an average treatment effect (ATE) under a formal potential-outcomes framework, not a predictive model. This is the most rigorous incrementality treatment of the three papers in this batch. |
| 7 | Model architecture | Not a ranking or neural architecture. A pair of nonparametric "bridge functions" (outcome bridge h0 and surrogate bridge q_a) that use proxy variables (W: outcome-aligned; Z: surrogate-aligned) to correct for unobserved confounding, estimated via cross-fitted double/debiased machine learning (DML, Chernozhukov et al. 2018-style K-fold sample splitting). The applied example fits these bridge functions as linear models, but the identification theory is fully nonparametric and the estimator accommodates flexible ML nuisance estimators in general. |
| 8 | Credit assignment | **Not applicable at the item level — this paper operates entirely at the experiment/population level.** It estimates a single scalar population ATE for one treatment (program participation vs. not); there is no exposure-to-item or impression-level decision anywhere in the framework. |
| 9 | Training data and counterfactual handling | Two data sources combined: a randomized experimental sample (treatment randomized, long-term outcome missing) and an observational sample (long-term outcome observed, treatment status missing and confounded by unobserved U). Counterfactual identification relies on formal assumptions: no direct effect of treatment on the long-term outcome except through the surrogate (Assumption 2), unconfoundedness given observed covariates and the *unobserved* U within each sample (Assumptions 3-4), and — the paper's central contribution — proxy variables (W, Z) informative enough about U, satisfying stated conditional-independence and completeness conditions, to nonparametrically identify the confounding-corrected ATE despite U itself never being observed. |
| 10 | Offline and online evaluation | Offline only — a real-data application (not a live experiment) using the National Job Corps Study RCT, artificially split into synthetic "experimental" and "observational" halves of the same completed randomized trial to create a controlled benchmark with a known ground-truth ATE. No online/production evaluation. |
| 11 | Reported gains | On the Job Corps dataset (Table 3), the RCT benchmark weekly-earnings ATE is $15.30 (SE 5.49). The standard surrogate index estimates $7.05 (SE 3.70) — a roughly 54% underestimate. Adding the proxy variables merely as ordinary covariates to the standard method gives $7.30 (SE 3.69), essentially no improvement. The paper's proximal surrogate index gives $16.43 (SE 7.92) — within $1.13 of the RCT benchmark, but with roughly double the standard error of the naive alternatives. The same pattern holds for proportion of weeks employed (RCT 2.87 vs. standard surrogate 0.80 vs. proximal method 3.50, SE also roughly triple the naive alternatives). |
| 12 | Applicability to a two-sided dating recommender | **Directly on-point for this project's core confounding problem.** The paper's own diagnostic (Table 4) shows unobserved ability/motivation inflating a naive short-term-to-long-term surrogate exactly the way active dating-app users' unobserved propensity to both see more candidates and retain longer would bias a naive surrogate-index model. It requires identifying valid outcome-aligned and surrogate-aligned proxy variables in advance, which the project would need to source itself — no off-the-shelf proxy is proposed. |
| 13 | Unverified claims | The synthetic experimental/observational split from a single completed RCT (rather than two genuinely independent data collections) means the "no residual sample-selection bias" property is guaranteed by construction in this demonstration and may not hold in a genuine two-source deployment. The proposed method's precision cost (standard error roughly 2x the naive alternatives) is reported in the results table but not discussed as a limitation in the main text's Conclusion, which frames the result only as a bias-correction success. |

## Project Relevance

Speaks directly to **Q1** (making retention/revenue itself the training objective, addressed here as a fully causal ATE rather than a proxy) and, above all, **Q5**/**Q6** — this is the batch's clearest treatment of the project's own stated confounding problem ("active users both see more candidates and retain more, for reasons the model does not observe"), giving a formal identification strategy (proxy variables + bridge functions) for exactly that failure mode, plus a reusable evaluation template (synthetic experimental/observational split against a known RCT benchmark) for validating any surrogate the project builds. Also bears on **Q3** (label/horizon: demonstrates that naive short-to-long-term extrapolation can be badly biased — a caution the survey should carry alongside Paper 1's more optimistic empirical agreement rate). **Not relevant to Q2, Q4, or Q7** — no item-level credit assignment, no discussion of fusing model heads, and no two-sided-market or reciprocity treatment; the method is a general econometric identification result applied to a single-sided labor-market program evaluation, not a recommender system. Caveat the survey should carry: this method's confounding-robustness comes at a real statistical-power cost (roughly double the standard error of the naive/biased alternatives in the one applied example given) — a trade-off the executive summary's risk assessment should name alongside Paper 1's precision/recall figures.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `ProximalSurrogateIndex`._

## Meta Information

- **Authors:** Ting-Chih Hung, Yu-Chang Chen
- **Affiliations:** National Taiwan University
- **Venue:** arXiv (econ.EM)
- **Year:** 2026
- **Relevance:** Core
- **Priority:** 2
- **nlm:3933c4bd**
