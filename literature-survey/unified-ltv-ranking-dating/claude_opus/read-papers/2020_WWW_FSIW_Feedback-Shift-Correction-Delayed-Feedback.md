# Paper Analysis: A Feedback Shift Correction in Predicting Conversion Rates under Delayed Feedback

**Source:** /Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/Delayed-Feedback-Problem/2020 (WWW) [FSIW] A Feedback Shift Correction in Predicting Conversion Rates under Delayed Feedback.pdf
**Date analyzed:** 2026-08-16

## 1. Summary

Shota Yasui, Gota Morishita, Komei Fujita, and Masashi Shibata, of CyberAgent, Inc., reframe the delayed-feedback CVR problem as a **feedback shift**: the feature distribution P(X) is unchanged between training and deployment, but the conditional label distribution differs, because a still-unconverted click's training label Y=0 is a mixture of true negatives and not-yet-observed conversions, whereas the target distribution's C=1|X is the eventual, fully-attributed conversion probability. Their fix is a feedback-shift importance weight (FSIW), w(x,y)=P(C=y|X=x)/P(Y=y|X=x), applied to the standard empirical-risk loss; Theorem 5.1 proves this reweighted loss is consistent (asymptotically unbiased) for the feedback shift, given the feature distribution stays fixed. Because P(C|X) is exactly the quantity the CVR model is trying to predict, FSIW cannot be estimated directly; instead the authors manufacture an "artificial dataset" using a counterfactual deadline τ on already-fully-observed historical data (relabeling clicks as correctly- or incorrectly-labeled had they been observed only up to τ), train an auxiliary classifier on this artificial dataset to estimate the two component probabilities in equations (8)-(9), and use its output as the importance weight at real training time. The method is model-, loss-, and learner-agnostic (demonstrated on plain logistic regression as LR-FSIW and on Field-aware Factorization Machines as FFMIW) and requires no assumption on the shape of the delay distribution at all — a deliberate departure from DFM's exponential-hazard assumption. The paper validates offline on the public Criteo dataset and an in-house CyberAgent/Dynalyst advertising dataset (three campaigns with 1-, 3-, and 7-day observation windows), and — unusually for this sub-literature — with a 14-day live online A/B test on production traffic.

## 2. Experiment Critique

One-paragraph summary (priority 3, per depth rule): the offline evaluation on Criteo (Table 1) uses log loss (LL), PR-AUC, and a normalized log-loss (NLL) metric, and reports LR-FSIW beating DFM by a statistically-significant margin on LL and NLL but not on PR-AUC; the in-house evaluation (Table 2) reports FFMIW beating FFM on all three metrics across three campaigns, but the authors are explicit that only Campaign L's NLL improvement is statistically significant — Campaigns M and S are directionally consistent but not significant, a limitation stated plainly rather than hidden. Training-time cost is also reported directly: FSIW estimation takes ~2.1 hours versus ~140 hours to train the DFM baseline on the same data, a substantial practical advantage. The live 14-day online A/B test (one production campaign, ~1 million impressions, models retrained daily) is a genuine strength relative to the rest of this batch — it reports a statistically significant +31% conversions and +28% cost, with a non-significant −2% CPA, and the authors interpret this honestly as "FFMIW incurred more costs, and performed similarly to the FFM in obtaining a conversion" rather than overstating the CPA result.

## 3. Industry Contribution

One-paragraph summary (priority 3, per depth rule): this is a production-deployed method from an ad-tech company (CyberAgent/Dynalyst), demonstrated end-to-end from offline validation through a live A/B test, and its explicit selling point for an engineering audience is that FSIW is a drop-in loss-reweighting step that requires no change to the underlying CVR model architecture (shown working with both plain LR and an existing production FFM) and no assumption about the delay distribution's shape — in contrast to DFM, which the authors note took ~140 hours to train on their data and struggled to converge, versus ~2.1 hours for FSIW estimation. The cost is an extra offline pipeline stage: constructing the artificial counterfactual-deadline dataset and training an auxiliary "correctly-labeled" classifier before the real CVR model can be trained or weighted.

## 4. Novelty vs. Prior Work

One-paragraph summary (priority 3, per depth rule): the explicit novelty is recasting delayed feedback as a feedback-shift problem (a labeled special case of the more general label-shift/covariate-shift literature) and proving the importance-weighted loss is consistent under it (Theorem 5.1) without any parametric assumption on the delay. The most heavily cited/discussed prior works are Chapelle (2014), the delayed-feedback and exponential-hazard founding paper (also this batch's paper 1, referred to throughout as "[2]" and as the DFM baseline); Yoshikawa & Imai (2018), a non-parametric delayed-feedback model; Ktena et al. (2019), the Facebook/industry paper introducing continuous-training neural-network delayed-feedback correction (cited as related recent work, [12]); Sugiyama et al. (2007) and Shimodaira (2000), the covariate-shift-correction and importance-weighted cross-validation literature this paper's core technique is adapted from; and Lipton, Wang & Smola (2018), label-shift detection and correction, the closest prior formalization to this paper's own "feedback shift" concept.

## 5. Dataset Availability

| Dataset | Size | Description | Public? |
|---|---|---|---|
| Criteo delayed-feedback dataset | Same as used in Chapelle (2014) | Public display-advertising click/conversion logs, 30-day attribution | Yes — https://labs.criteo.com/2013/12/conversion-logs-dataset/ |
| Dynalyst in-house dataset (3 campaigns L/M/S) | 3 campaigns; 16 rolling 13-day-train/1-day-validation/1-day-test sets each; ~1M impressions in the online A/B period | Real-time in-house advertising conversion logs with per-advertiser attribution windows (Campaign L: 7 days; Campaign M: 3 days; Campaign S: 1 day) | No — proprietary CyberAgent/Dynalyst data |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

1. **Title, authors, venue, year, URL:** "A Feedback Shift Correction in Predicting Conversion Rates under Delayed Feedback," Shota Yasui, Gota Morishita, Komei Fujita, Masashi Shibata, CyberAgent, Inc., WWW 2020. https://doi.org/10.1145/3366423.3380032
2. **Source type:** Industry paper (CyberAgent, Inc.; peer-reviewed at WWW).
3. **Direction:** D7.
4. **Problem setting:** CVR prediction for CPA display-advertising bidding, where the label distribution used at training time (click-labeled-so-far) differs from the label distribution needed at inference time (eventual, fully-attributed conversion) — framed generally as a "feedback shift," a labeled instance of covariate/label shift.
5. **Objective and label definition:** Predicts P(C=1|X=x), the probability a click will *eventually* convert, versus the biased training signal P(Y=1|X=x) (converted so far). Horizon: Criteo dataset retains its original 30-day attribution window; the in-house Dynalyst campaigns use 1-, 3-, or 7-day observation windows per advertiser. Delay/censoring handled by an importance weight (FSIW) estimated from an artificially constructed "counterfactual deadline" dataset, with no assumption on the shape of the underlying delay distribution.
6. **Prediction or incrementality:** Prediction only — the paper does not address incrementality.
7. **Model architecture:** Model-agnostic reweighting scheme; demonstrated with plain logistic regression (LR-FSIW) and Field-aware Factorization Machines (FFMIW); the FSIW weight itself is estimated via LightGBM binary classifiers predicting whether an observed negative is correctly labeled.
8. **Credit assignment:** Not specified in source. As with the rest of this batch, the outcome unit already equals the decision unit (one click, one eventual conversion); no user-level-to-item-level aggregation is addressed.
9. **Training data and counterfactual handling:** Public Criteo dataset plus in-house Dynalyst conversion logs (3 campaigns). Counterfactual handling: a counterfactual deadline τ is applied to already-fully-observed historical data to simulate the delayed-labeling process, producing an "artificial dataset" used to train the auxiliary correctly-labeled classifier that in turn estimates FSIW for the real training data.
10. **Offline and online evaluation:** Offline — Criteo public benchmark and Dynalyst historical logs, metrics LL/PR-AUC/NLL with bootstrapped 95% confidence intervals. Online — a 14-day live A/B test on one Dynalyst production campaign (Campaign L), FFM vs. FFMIW, ~1M impressions, daily retraining.
11. **Reported gains:** On the Criteo dataset, LR-FSIW improves log loss (LL) by 1.5% and NLL by 2.5% versus DFM, both statistically significant (Table 1: LL 0.3928 vs. 0.3989; NLL 28.02 vs. 27.33); PR-AUC shows no significant difference. On the production online A/B test (Table 3), FFMIW vs. FFM on Dynalyst Campaign L: conversions +31% and cost +28% (both statistically significant), CPA −2% (not statistically significant).
12. **Applicability to a two-sided dating recommender:** The model-agnostic, distribution-assumption-free importance-weighting approach is architecturally easy to bolt onto an existing prediction head, and its rare live-A/B validation is a real strength — but the online evidence and offline campaign windows only span 1–7 days, far short of a 30-day retention or multi-week revenue horizon, so the counterfactual-deadline construction's stability at that longer scale is untested.
13. **Unverified claims:** The consistency result (Theorem 5.1) is a proven mathematical claim within the paper's own framework, not merely asserted. However, the practical FSIW estimation procedure via the artificial-dataset auxiliary classifier is heuristic and not itself proven unbiased — its stability is only checked empirically (Figure 5, varying the counterfactual deadline from 1–7 days on Criteo). The Campaign M and S improvements in Table 2 are explicitly *not* flagged as statistically significant, so the FFMIW-over-FFM claim is only formally supported for Campaign L, a point the authors state rather than obscure.

## Project Relevance

This paper speaks to **Q3** (label and horizon definitions, delay/censoring handling) by offering a genuinely different mechanism from DFM's parametric hazard model — a distribution-free importance-weighting correction with a consistency proof — and it is one of only two papers in this batch (with DEFUSE) with any offline unbiasedness argument at all, and the only one with a live online validation, which is relevant to **Q6** (offline/online evaluation under delayed, noisy outcomes) as a rare existence proof that a delayed-feedback correction can be validated online. It does not address **Q1** (no retention/LTV reframing — the objective remains conversion prediction), **Q2** (no user-level-to-item-level credit assignment), **Q4–Q5** (no long/short-term head fusion, no incrementality), or **Q7** (no two-sided/reciprocal market treatment). Its transferable idea for the dating-app project is the general recipe of estimating an importance weight from an artificially manufactured "what would this label have looked like with less elapsed time" dataset — but validated only at a 1–7-day horizon, not the 7–30-day retention or weeks-long revenue scale the project needs.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2014_KDD_DFM_Modeling-Delayed-Feedback-Display-Advertising.md](./2014_KDD_DFM_Modeling-Delayed-Feedback-Display-Advertising.md) | Related Work / Experiments | Names this paper's method (`FSIW`) |
| [2021_AAAI_ESDFM_Capturing-Delayed-Feedback-Elapsed-Time-Sampling.md](./2021_AAAI_ESDFM_Capturing-Delayed-Feedback-Elapsed-Time-Sampling.md) | Related Work / Experiments | Names this paper's method (`FSIW`) |
| [2021_AAAI_ESDF_Delayed-Feedback-Modeling-Entire-Space.md](./2021_AAAI_ESDF_Delayed-Feedback-Modeling-Entire-Space.md) | Related Work / Experiments | Names this paper's method (`FSIW`) |
| [2022_WWW_DEFUSE_Asymptotically-Unbiased-Estimation-Label-Correction.md](./2022_WWW_DEFUSE_Asymptotically-Unbiased-Estimation-Label-Correction.md) | Related Work / Experiments | Names this paper's method (`FSIW`) |
| [2026_AAAI_IF-DFM_Delayed-Feedback-Modeling-Influence-Functions.md](./2026_AAAI_IF-DFM_Delayed-Feedback-Modeling-Influence-Functions.md) | Related Work / Experiments | Names this paper's method (`FSIW`) |

_5 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `FSIW` across all 133 cards._

## Meta Information

- **Authors:** Shota Yasui, Gota Morishita, Komei Fujita, Masashi Shibata
- **Affiliations:** CyberAgent, Inc., Shibuya, Tokyo
- **Venue:** The Web Conference (WWW) 2020
- **Year:** 2020
- **Relevance:** Core
- **Priority:** 3
- **NotebookLM source:** nlm:ab5a23dc
