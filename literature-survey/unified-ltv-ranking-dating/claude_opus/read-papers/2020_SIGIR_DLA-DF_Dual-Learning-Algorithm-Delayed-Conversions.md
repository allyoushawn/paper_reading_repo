# Paper Analysis: Dual Learning Algorithm for Delayed Conversions

**Source:** `/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/Delayed-Feedback-Problem/2020 (SIGIR) [DLA-DF] Dual Learning Algorithm for Delayed Conversions.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

Yuta Saito, Gota Morishita, and Shota Yasui (Tokyo Institute of Technology / independent researcher / CyberAgent, Inc.), "Dual Learning Algorithm for Delayed Conversions," SIGIR '20 (short research paper). The paper addresses two compounding sources of bias in CVR prediction under delayed feedback: the positive-unlabeled (PU) problem (unconverted-so-far examples are not confirmed negatives) and the missing-not-at-random (MNAR) problem (the probability that a conversion has been observed by training time is not uniform across users — decisive users convert and get observed faster than indecisive ones). Prior work (Chapelle 2014's DFM, Yoshikawa & Imai 2018's non-parametric model) addresses delay via a parametric or non-parametric delay-distribution assumption but does not address MNAR; a separate line (Ktena et al. 2019, paper #1 in this batch) uses importance weighting for MNAR but does not simultaneously solve the PU problem. This paper proposes DLA-DF: two unbiased estimators — an inverse-propensity-scored (IPS) CVR loss and an "inverse conversion rate" (ICVR) propensity-score loss — trained jointly in alternating fashion (a "dual learning" scheme, Algorithm 1), each supervising the other, without requiring true propensity scores or a parametric delay-distribution assumption. A non-negative variant (nnDLA-DF) is also proposed to reduce the high variance of the underlying inverse-propensity-weighted estimators, at the cost of some bias. Evaluated only on a synthetic dataset (N=100,000 simulated units, exponential and normal delay distributions, training-period lengths L = 0.5, 1, 2, 4 days) against Oracle, Naive, and DFM baselines; DLA-DF is competitive with or outperforms DFM particularly when the delay distribution is not exponential (i.e., when DFM's own parametric assumption is violated) and when the training period L is short (more severe delay/censoring), though its relative advantage narrows at L=4 days, and DFM (unsurprisingly) wins when the true delay distribution is exponential, matching DFM's own assumption exactly.

## 2. Experiment Critique

Not padded — priority 3 depth. Evaluation is entirely synthetic (no real-world or public benchmark dataset), a limitation the authors implicitly acknowledge by calling it a "synthetic experiment"; only relative log-loss vs. an unobservable Oracle is reported (mean ± std dev over 10 iterations), and no online experiment is included.

## 3. Industry Contribution

Not padded — priority 3 depth. As a synthetic-data-only short paper, the industry contribution is theoretical/algorithmic rather than demonstrated in production; no serving-latency, feature-engineering, or deployment discussion is given, despite one author's industry (CyberAgent) affiliation.

## 4. Novelty vs. Prior Work

Not padded — priority 3 depth. Positioned explicitly against Chapelle 2014 (DFM, parametric exponential delay, doesn't address MNAR), Yoshikawa & Imai 2018 (non-parametric delay, doesn't address MNAR), and Ktena et al. 2019 (importance weighting for MNAR, doesn't address PU) as the first method to jointly solve both the PU and MNAR problems without a parametric delay-distribution assumption.

## 5. Dataset Availability

| Dataset | Type | Size | Availability |
|---|---|---|---|
| Synthetic delayed-conversion data (Algorithm 2 generator) | Synthetic | N=100,000 simulated units, p=30 features | Generation procedure described in the paper; no dataset file released — Not specified in source. |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Dual Learning Algorithm for Delayed Conversions," Yuta Saito, Gota Morishita, Shota Yasui; Tokyo Institute of Technology / independent / CyberAgent Inc.; SIGIR '20; 2020; https://doi.org/10.1145/3397271.3401282 |
| 2 | Source type | Academic (short research paper), with industry co-authorship (CyberAgent) |
| 3 | Direction | D7 |
| 4 | Problem setting | CVR prediction under delayed feedback where conversion labels are both positive-unlabeled (an unconverted-so-far example may convert later) and missing-not-at-random (the probability of having observed a true conversion label by training time depends on user behavior — decisive users are observed sooner). |
| 5 | Objective and label definition | Objective: predict the true CVR γ(X) = Pr(Y=1\|X). Label definition/censoring handling: an observed label Y^obs = O·Y, where Y is the (partially unobservable) true conversion indicator and O is a binary "has the outcome been correctly observed by now" indicator dependent on elapsed time E since click; the model does not treat Y^obs=0 as confirmed negative but instead reweights each observed conversion by the inverse of its estimated propensity score θ(X,E) = Pr(O=1\|Y=1,X,E) to recover an unbiased estimate of the true CVR loss. No parametric delay-distribution assumption is required — propensity is estimated jointly and unbiasedly via the ICVR estimator rather than assumed exponential (as in DFM) or otherwise. Horizon: evaluated only via synthetic training-period lengths L ∈ {0.5, 1, 2, 4} days; no real-world delay horizon is reported. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. IPS/ICVR reweighting here corrects a label-observation bias (MNAR + PU) in CVR prediction; it is not an estimate of the causal effect of any treatment or exposure. This is a label-bias correction, explicitly distinct from incremental-effect estimation — the inverse-propensity weighting used here corrects for informative censoring in the training labels, not for confounding in a treatment-effect sense. |
| 7 | Model architecture | Logistic regression used for both the CVR predictor f and the propensity-score estimator g in the synthetic experiments, trained in alternating fashion via Algorithm 1 (dual learning): fix the propensity estimator, update the CVR predictor via the IPS loss; fix the CVR predictor, update the propensity estimator via the ICVR loss; repeat until convergence. A non-negative loss variant (Eq. 5) clips the per-sample IPS loss at zero to reduce variance at the cost of some bias. |
| 8 | Credit assignment | Not addressed — the paper operates at the single click-to-conversion label level, with no multi-item, slate, or multi-event structure. |
| 9 | Training data and counterfactual handling | Synthetic data only, generated via Algorithm 2 (sigmoid-linear true CVR model, exponential or normal delay distribution, uniformly distributed click timestamps). "Counterfactual handling" here means the dual IPS/ICVR estimators correct for the fact that observed conversions are a biased (MNAR) subsample of true conversions, not causal-inference counterfactual adjustment. |
| 10 | Offline and online evaluation | Offline only, on synthetic data: relative log-loss on held-out synthetic test sets vs. an unobservable Oracle model, averaged with standard deviation over 10 iterations, across two delay-distribution families (exponential, normal) and four training-period lengths. No online or real-world evaluation. |
| 11 | Reported gains | On synthetic data with a normal delay distribution (Figure 1, right panel), DLA-DF has consistently lower relative log-loss than DFM and Naive across all tested training-period lengths L (0.5-4 days), with the largest relative advantage at L=0.5-2 days; under an exponential delay distribution — which exactly matches DFM's own parametric assumption — DFM outperforms DLA-DF, a result the authors describe as expected given DFM's assumption is satisfied in that setting. No numeric log-loss values are stated in the extracted text; only the relative-ranking pattern across the figures is described by the authors. |
| 12 | Applicability to a two-sided dating recommender | Low direct applicability: the MNAR insight (users who are "decisive" are observed sooner, biasing naive delayed-feedback correction) is conceptually relevant to a dating app, where active/engaged users may show retention or conversion signals faster than passive ones, but the method is validated only on synthetic single-event ad-conversion data with no two-sided, reciprocal, or multi-event structure. |
| 13 | Unverified claims | All reported results are on a synthetic dataset generated by the authors' own procedure (Algorithm 2); no real-world validation is presented. The claim that DLA-DF provides "stable prediction performance" across "a wide range of situations" is an inference from four synthetic training-period settings and two delay-distribution families, not a broad empirical demonstration. |

## Project Relevance

Speaks to **Q3** (censoring/delay handling — the joint PU+MNAR correction is a more complete treatment of censoring bias than single-mechanism approaches) but is **low project relevance** for most other questions: the paper is evaluated only on synthetic data with no real system, no real delay horizon, no multi-event or two-sided structure, and does not address incrementality (Q5), credit assignment across a cascade (Q2), or fusion of short/long-term heads (Q4). Its main transferable insight is conceptual: correcting for delayed-label bias requires addressing both "not yet converted" (PU) and "who gets observed sooner" (MNAR) as distinct, compounding biases — a useful framing check for the project's own retention-label design, even though the concrete estimators here are not directly portable given the lack of real-world validation.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2021_arXiv_NA_Many-Conversions-Per-Click-Delayed-Feedback.md](./2021_arXiv_NA_Many-Conversions-Per-Click-Delayed-Feedback.md) | Related Work / Experiments | Names this paper's method (`DLA-DF`) |

_1 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `DLA-DF` across all 133 cards._

## Meta Information

- **Authors:** Yuta Saito, Gota Morishita, Shota Yasui
- **Affiliations:** Tokyo Institute of Technology; independent researcher; CyberAgent, Inc.
- **Venue:** SIGIR '20 (43rd International ACM SIGIR Conference), Short Research Papers
- **Year:** 2020
- **Relevance:** Related
- **Priority:** 3
- **nlm:987cb2e2**
