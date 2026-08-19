# Paper Analysis: Delayed Feedback Model with Negative Binomial Regression for Multiple Conversions

**Source:** /Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/Delayed-Feedback-Problem/2020 (AdKDD) Delayed Feedback Model with Negative Binomial Regression for Multiple Conversions.pdf
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** Delayed Feedback Model with Negative Binomial Regression for Multiple Conversions
**Authors:** Youngmin Choi, Mugeun Kwon, Younjin Park, Jinsoo Oh, Suyoung Kim (LINE Plus)
**Venue/Year:** AdKDD '20 (ACM workshop co-located with KDD, San Diego, California), 2020

LINE Plus's display-ad platform pays advertisers on a cost-per-conversion (CPA) basis, computed via eCPM = CPA × pCVR × pCTR × 1000, so pCVR accuracy directly drives revenue and advertiser trust. The paper identifies two compounding real-data problems beyond simple delayed feedback: (1) conversions can recur multiple times per click for some product types (e.g., repeat purchases) — the paper's "Non-binary ratio" statistic shows over 25% of clicks in two of their four conversion types have 2+ conversions — and existing delayed-feedback models (DFM) only model the first conversion as a binary event, discarding this count information. The paper proposes a jointly trained **Negative Binomial regression + Order Statistics** delayed feedback model (NBDFM): the eventual number of conversions C given features x follows Pr(C=k|x) = p(x)^k(1−p(x)), a negative-binomial-form regression, while the arrival times of the k conversions D_1<...<D_k are modeled as the Order Statistics of k i.i.d. Exponential(λ(x)) draws, letting the joint likelihood (Eq. 9–13) be derived in closed form via a negative-binomial-series simplification for tractable L-BFGS optimization. Evaluated on real LINE Ads Platform traffic (conversion "Type A," selected for having sufficient volume and many multi-conversion clicks) against DFM, Logistic, Poisson, Negative-Binomial-alone, a DFM+Poisson heuristic (their prior production model), and Oracle upper-bound variants, across 7 held-out test days using MSE and Calibration (predicted/actual conversion-count ratio). NBDFM achieves the lowest MSE (0.08454 vs. DFM's 0.09219) and calibration closest to 100% (101.12% vs. DFM's 141.77%), i.e., DFM and Logistic (binary-only models) substantially under-predict total conversion volume. The model has been deployed to LINE's production ranking system, with an end-to-end serving latency on the order of 10ms.

## 2. Experiment Critique / 3. Industry Contribution / 4. Novelty vs. Prior Work / 5. Dataset Availability

Condensed per the priority-3 depth rule — see the Reference Card (Section 7) and Project Relevance below. Dataset is proprietary real-traffic LINE Ads Platform data (conversion Type A), not publicly released. Novelty is the joint NB-regression + Order-Statistics-delay construction itself, contrasted against the authors' own prior heuristic (DFM+Poisson, an additive combination of DFM's binary "first conversion happened" probability and a separate Poisson count model that ignores delay for subsequent conversions) and against generic count-regression GLMs (Poisson, Negative Binomial alone) that ignore delayed feedback entirely.

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Delayed Feedback Model with Negative Binomial Regression for Multiple Conversions," Youngmin Choi, Mugeun Kwon, Younjin Park, Jinsoo Oh, Suyoung Kim; LINE Plus; AdKDD '20, August 23, 2020, San Diego, California; DOI 10.1145/xxxxxx (placeholder DOI printed in the PDF, not a resolvable URL) |
| 2 | Source type | Industry paper (LINE Plus), ACM workshop |
| 3 | Direction | D7 |
| 4 | Problem setting | CVR/conversion-count prediction for CPA display advertising where a single click can yield **multiple** conversions (not just one binary event), compounded by the standard delayed-feedback problem (conversions can arrive up to ~4 weeks after a click, per the paper's introduction). |
| 5 | Objective and label definition | Predicts the expected **number** of eventual conversions E(C\|x) per click (a count, not a binary CVR), via a Negative Binomial regression for the count C jointly with an Order-Statistics-of-k-i.i.d.-Exponential(λ(x)) model for the individual conversion delay times D_1..D_k. Horizon: experiment splits use 3 weeks of training data with the following day as test, across 7 consecutive test days; the paper's introduction qualitatively states conversions "may take up to 4 weeks" to complete, but no explicit attribution/censoring cutoff (in days) is stated for the experiments themselves — **not specified in source** beyond that qualitative "up to 4 weeks" framing. Un-converted/unresolved conversions are handled implicitly through the joint likelihood's marginalization over the hidden true-count variable C (Eq. 11–13), rather than a stated hard censoring rule. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. |
| 7 | Model architecture | Negative Binomial regression for conversion count (weight vector w_c) jointly combined with an Order-Statistics-of-Exponential(λ(x)) delay model (weight vector w_d); trained by maximizing a joint negative log-likelihood via L-BFGS (5 correction pairs, gradient tolerance 1e-5, function tolerance 1e-8, max 300 iterations). Deployed via a three-stage production system: Data Pipeline → Model Training → Model Serving, with reported ~10ms total serving latency including feature retrieval, ranking thousands of ad candidates by eCPM. |
| 8 | Credit assignment | Not specified in source. The model assigns a count outcome to a single click within a single, pre-selected conversion type ("Type A"); there is no multi-item, multi-slate, or cross-conversion-type credit-assignment mechanism. |
| 9 | Training data and counterfactual handling | Real LINE Ads Platform traffic logs for conversion Type A (chosen for sufficient volume and multi-conversion prevalence — Table 1 reports a 26.4% non-binary/multi-conversion ratio for this type). 7 experiment datasets, each with 3 weeks of training data and the following day as test. No counterfactual or causal handling — purely observational count-label correction for delayed/multiple conversions; an "Oracle" GLM variant (trained with full future-known conversions) is used only as an upper-bound reference, not a causal estimate. |
| 10 | Offline and online evaluation | Offline only: Mean Squared Error (MSE) and Calibration (ratio of predicted to actual total conversion counts) averaged across 7 test days, against Oracle upper-bound variants of Logistic/Poisson/Negative-Binomial. **No online A/B test is reported** — the production Model Serving architecture is described, but no online lift metric is given for NBDFM specifically. |
| 11 | Reported gains | MSE: NBDFM 0.08454 vs. DFM (baseline) 0.09219 (Diff −0.00764), vs. Logistic 0.09231, Poisson 0.08681, Negative Binomial 0.08682, DFM+Poisson 0.08723 — on real LINE Ads Platform Type-A conversion traffic, weighted average over 7 test days. Calibration: NBDFM 101.12% vs. DFM 141.77%, Logistic 146.60%, Poisson 108.85%, Negative Binomial 108.19%, DFM+Poisson 106.25% — i.e., DFM and Logistic (binary-only models) under-predict total conversion counts by roughly 40–47% on average, while NBDFM is within ~1% of actual. |
| 12 | Applicability to a two-sided dating recommender | Structurally the most relevant paper in this batch despite its low priority: the project's one-impression-to-{like, match, conversation, subscription} cascade is exactly the "multiple conversions from one event" shape this paper's NB + Order-Statistics machinery targets, rather than a single binary outcome. However, the model counts every conversion identically (E(C\|x) is a bare expected count) — differential valuation of a like vs. a subscription happens only outside the model, via the separate eCPM = CPA × pCVR × pCTR business formula, not inside the count distribution itself — so value-weighting would need to be added for the project's retention/revenue objective. |
| 13 | Unverified claims | The paper states its negative-binomial-series simplification "reduc[es] the complexity for training and prediction" giving "a powerful computational advantage," but the only latency figure given (~10ms) is a general production-serving number covering the whole ranking pipeline, not an isolated comparison of NBDFM's own inference cost against the GLM baselines it is compared to — flagged as an under-substantiated efficiency claim. |

## Project Relevance

**Structurally the most relevant paper in this batch, despite its stated low priority.** It speaks to **Q1** (moves the objective from a binary CVR label to a count of eventual conversions, a step toward a richer training signal than CTR-style proxies, though still not retention or revenue) and offers a directly transferable modeling primitive for the project's cascade of distinct outcome types per impression — but only as an event-**count** model, not a value-weighted one, so it does not by itself answer Q1's "retention/revenue as training objective" bar. Does not address Q2, Q4, Q5 (explicitly prediction-only), Q6 (no online evaluation is reported at all), Q7, or Q8.

The paper's own delay horizon is only loosely characterized ("up to 4 weeks" mentioned qualitatively, no explicit censoring cutoff stated for the reported experiments), so unlike DEFER's explicit 7-day attribution-window deployment, this paper cannot be used as horizon evidence for the project's 30-day retention definition — only as a candidate model *shape* (multiple, distinguishable conversion events per impression) that the project's eventual retention/revenue model should be able to represent, extended with per-event-type value weighting.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `NBDFM`._

## Meta Information

- **Authors:** Youngmin Choi, Mugeun Kwon, Younjin Park, Jinsoo Oh, Suyoung Kim
- **Affiliations:** LINE Plus
- **Venue:** AdKDD '20 (ACM workshop, San Diego, California)
- **Year:** 2020
- **Relevance:** Related
- **Priority:** 3
- nlm:71247ab8
