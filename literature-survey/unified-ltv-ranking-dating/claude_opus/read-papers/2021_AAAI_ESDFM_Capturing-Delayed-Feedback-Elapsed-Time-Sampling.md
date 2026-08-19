# Paper Analysis: Capturing Delayed Feedback in Conversion Rate Prediction via Elapsed-Time Sampling

**Source:** /Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/Delayed-Feedback-Problem/2021 (Alibaba) (AAAI) [ES-DFM] Capturing Delayed Feedback in Conversion Rate Prediction via Elapsed-Time Sampling.pdf
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** Capturing Delayed Feedback in Conversion Rate Prediction via Elapsed-Time Sampling
**Authors:** Jia-Qi Yang, Xiang Li, Shuguang Han, Tao Zhuang, De-Chuan Zhan, Xiaoyi Zeng, Bin Tong (Nanjing University; Alibaba Group)

**Abstract (paraphrase):** Streaming conversion-rate (CVR) prediction must trade off waiting long enough for accurate conversion labels against updating the model with fresh data. The paper proposes the Elapsed-Time Sampling Delayed Feedback Model (ES-DFM), which models the relationship between the *observed conversion* distribution and the *true conversion* distribution as a function of elapsed time, then optimizes the expectation of the true conversion distribution via importance sampling under an elapsed-time sampling distribution. An importance weight is estimated per instance and used as the training-loss weight.

**Key contribution:** The paper is presented as the first to explicitly study the trade-off between label accuracy and data freshness in streaming CVR prediction, by introducing an elapsed-time distribution p(e|x) as a design knob and deriving an unbiased importance-sampling correction around it, robust to changes in the underlying data distribution.

**Methodology:** The observed-label distribution q(y|x) is decomposed relative to the true distribution p(y|x) using the delay-time distribution p(h|x, y=1) and the elapsed-time distribution p(e|x) (Eq. 2–7). The importance weight w(x,y) = p(y|x)/q(y|x) is decomposed into two bounded probabilities: p_dp(x), the probability a sample is a "delayed positive" (will convert after elapsed time e), and p_rn(x), the probability an observed negative is a genuine "real negative." Two auxiliary binary classifiers f_dp and f_rn (same MLP architecture as the CVR model) are trained jointly with the CVR model in streaming fashion to estimate these probabilities, which weight the cross-entropy loss (Eq. 17). As soon as a conversion is observed, the sample is duplicated with a positive label (as in prior delayed-feedback methods), but now under an importance-weighted loss rather than an unweighted one.

**Main results:** ES-DFM outperforms all baselines (Pre-trained, Vanilla finetune, DFM, FNW, FNC, FSIW) on AUC, PR-AUC and NLL on both the public Criteo dataset and a private Taobao dataset, and narrows the largest share of the "delayed feedback gap" to an Oracle model (trained on ground-truth labels) among compared methods. An online A/B test reports AUC +0.3% within a 7-day window, CVR +0.7%, and GMV +1.8% versus the best baseline.

## 2. Experiment Critique

- **Design:** A streaming-training/streaming-evaluation protocol is constructed to mirror industrial online-learning cadence (train on hour *t*, test on hour *t+1*), on both a public (Criteo, 60-day) and a private industrial (Taobao, 14-day) dataset — a stronger design than a single static offline split.
- **Statistical validity:** Main AUC/PR-AUC/NLL improvements are marked with a t-test at p<0.05 (asterisked in Table 2).
- **Online experiment:** A single reported A/B test over a 7-day window; the paper does not state traffic scale, confidence intervals, or which specific product surface was tested.
- **Reproducibility:** Code for the Criteo experiments is released (GitHub link in the paper); the private Taobao dataset and its results are not reproducible externally.
- **Ablations:** RQ2 (elapsed-time hyperparameter c) and RQ3 (robustness to randomly flipped/mislabeled positives) are both run, showing performance degrades sharply once the waiting window exceeds roughly 1 hour.

## 3. Industry Contribution

- **Deployability:** Designed explicitly for hourly-cadence streaming retraining, matching common industrial online-learning pipelines. The two auxiliary classifiers reuse the main CVR model's MLP architecture and are trained jointly with a shared network, keeping the added serving/training cost modest.
- **Problems solved:** Reduces fake-negative label bias in delayed CVR prediction without requiring a long wait before ingesting a sample, via a tunable elapsed-time distribution that lets an operator dial the freshness/accuracy trade-off.
- **Engineering cost:** Requires a data pipeline that can correct/duplicate a sample's label once a delayed conversion arrives (the paper notes this is available "in a delayed data stream... delayed by 30 days to ensure label correctness" in practice), plus joint training of two additional classifiers under an importance-weighted loss.

## 4. Novelty vs. Prior Work

- **vs. DFM (Chapelle, "Modeling delayed feedback in display advertising," KDD 2014):** DFM assumes the conversion delay follows a specific parametric (exponential) distribution and jointly models CVR and delay time. ES-DFM avoids committing to a delay-density form altogether — it never fits p(h|x,y=1) explicitly, instead estimating bounded importance weights (p_dp, p_rn) directly.
- **vs. FNW / FNC (Ktena et al., "Addressing Delayed Feedback for Continuous Training with Neural Networks in CTR Prediction," RecSys 2019):** FNW labels every arriving sample negative initially and duplicates on conversion, correcting via importance sampling that stops gradient through an unbounded model estimate; ES-DFM's weights are two separately-estimated bounded probabilities, which the authors argue introduces less variance.
- **vs. FSIW (Yasui et al., "A Feedback Shift Correction in Predicting Conversion Rates under Delayed Feedback," WWW 2020):** FSIW waits a fixed interval and does not allow later correction if a conversion happens outside that interval; ES-DFM keeps correcting a sample's label whenever the true conversion event later arrives.

## 5. Dataset Availability

| Dataset | Type | Access | Size |
|---|---|---|---|
| Criteo conversion-log dataset (used in Chapelle 2014) | Public | https://labs.criteo.com/2013/12/conversion-logs-dataset/ | 60-day log period, 15,898,883 samples, avg. CVR 0.2269 |
| Taobao dataset | Private, industrial (Alibaba) | Not released | 14-day log period, ~9.8 billion samples, avg. CVR 0.03273 |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Capturing Delayed Feedback in Conversion Rate Prediction via Elapsed-Time Sampling," Jia-Qi Yang, Xiang Li, Shuguang Han, Tao Zhuang, De-Chuan Zhan, Xiaoyi Zeng, Bin Tong; Nanjing University / Alibaba Group; AAAI 2021 (preliminary version per the PDF header — "The AAAI Digital Library will contain the published version"); code at https://github.com/ThyrixYang/es_dfm |
| 2 | Source type | Academic (industry co-authored: Alibaba Group) |
| 3 | Direction | D7 |
| 4 | Problem setting | Streaming/online conversion-rate (CVR) prediction under delayed feedback, where the conversion may not be observed until well after the click, forcing a trade-off between waiting for label accuracy and retraining with fresh data. |
| 5 | Objective and label definition | Binary CVR prediction. A sample's elapsed time e is drawn from a per-sample distribution p(e\|x); the label is corrected/duplicated positive whenever a true conversion is later observed. Horizon: the model's own operating elapsed-time window is tuned to minutes-to-about-1-hour (best result at c ≈ 15 minutes on Criteo; performance "harmed significantly" once the window exceeds 1 hour). Delay/censoring is handled not by a hard cutoff but by importance-weighting every sample's loss using two estimated bounded probabilities, p_dp(x) (probability of being a delayed/fake positive) and p_rn(x) (probability of being a genuine real negative); the paper separately notes production pipelines may delay label finalization "by 30 days to ensure label correctness," but that 30-day figure describes the surrounding data pipeline, not the model's own elapsed-time window. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. |
| 7 | Model architecture | MLP with hidden units [256, 256, 128], Leaky ReLU activations, BatchNorm after each hidden layer, Adam optimizer (lr 1e-3, L2 reg 1e-6). Two auxiliary classifiers (f_dp, f_rn) share this same architecture and are trained jointly with the main CVR model in a streaming setting. |
| 8 | Credit assignment | Not specified in source. The model operates at single click → single conversion-label granularity; it does not address mapping a delayed outcome to a multi-item slate or ranked list. |
| 9 | Training data and counterfactual handling | Public Criteo conversion-log dataset (60-day period) and a private Taobao dataset (14-day period), both split into pre-training and streaming-simulation halves. No counterfactual or causal estimation is performed — this is purely observational label-bias correction for a prediction target. |
| 10 | Offline and online evaluation | Offline: AUC, PR-AUC, and NLL, plus relative metrics (R-AUC, R-PR-AUC, R-NLL) measuring the fraction of the Oracle-minus-Pretrained performance gap closed, on Criteo and Taobao streaming simulations. Online: a single A/B test in an unspecified Alibaba production recommender system over a 7-day window, reporting AUC, CVR and GMV deltas versus the best baseline. |
| 11 | Reported gains | "our method outperform[s] the best baseline by 0.26% and 0.44% AUC scores on the Criteo and Taobao Dataset respectively" (offline). Online A/B, 7-day window vs. best baseline: AUC +0.3%, CVR +0.7%, GMV (Gross Merchandise Volume) +1.8%. |
| 12 | Applicability to a two-sided dating recommender | Offers a label-bias-correction technique for a single binary delayed event at a minutes-to-hours horizon, with no incrementality or two-sided-market treatment. Its importance-sampling machinery could in principle sit underneath a longer-horizon head, but the paper never tests or extrapolates beyond ~1 hour, so applicability to a 7–30 day retention/revenue horizon is unverified by the paper itself. |
| 13 | Unverified claims | The claim that "even 0.1% of AUC improvement is substantial and achieves significant online promotion" is supported only by citing a different paper's (Zhou et al. 2018, DIN) CTR result as an analogy, not by an independent sensitivity analysis of ES-DFM's own online gain — flagged as an unverified extrapolation. The specific production system used for the reported online A/B test (platform, traffic scale, confidence interval) is not described. |

## Project Relevance

Speaks most directly to **Q3** (delay/censoring handling for a CVR-style label) via its elapsed-time importance-sampling alternative to hard censoring, and touches **Q1** (moves away from a naive same-session CVR label, though the objective remains a short-term prediction target, not retention/LTV) and **Q6** (offline+online evaluation design under label delay). It does **not** address Q2 (item/slate-level credit assignment), Q4 (fusion of short- and long-term heads), Q5 (uplift/incrementality — explicitly out of scope), Q7 (two-sided/reciprocal market, congestion, fairness), or Q8 (migration path from CTR+uplift to a unified model).

**Low relevance to the project's actual horizon.** The paper's whole design centers on a minutes-to-~1-hour elapsed-time window; it explicitly shows performance degrading fast once the window passes 1 hour, and offers no evidence about behavior at the project's 7–30 day retention scale. It is best read as a technique for the label-bias sub-problem at short horizons, not as a candidate architecture for the unified retention/revenue objective itself.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `ESDFM`._

## Meta Information

- **Authors:** Jia-Qi Yang, Xiang Li, Shuguang Han, Tao Zhuang, De-Chuan Zhan, Xiaoyi Zeng, Bin Tong
- **Affiliations:** State Key Laboratory for Novel Software Technology, Nanjing University; Alibaba Group
- **Venue:** AAAI 2021 (preliminary version, per PDF header)
- **Year:** 2021
- **Relevance:** Core
- **Priority:** 2
- nlm:adf6d4a9
