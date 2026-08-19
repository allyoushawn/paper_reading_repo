# Paper Analysis: Asymptotically Unbiased Estimation for Delayed Feedback Modeling via Label Correction

**Source:** /Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/Delayed-Feedback-Problem/2022 (Alibaba) (WWW) [DEFUSE] Asymptotically Unbiased Estimation for Delayed Feedback Modeling via Label Correction.pdf
**Date analyzed:** 2026-08-16

## 1. Summary

Yu Chen, Jiaqi Jin, Hui Zhao, Pengjie Wang, Guojun Liu, Jian Xu, and Bo Zheng, of Alibaba Group, refine the importance-sampling line of delayed-feedback work (FNW/FNC, ES-DFM, DEFER) by arguing those methods conflate two different kinds of "observed negative": a **fake negative** (FN, will convert later, before the full attribution window w_a) and a **real negative** (RN, never converts). DEFUSE (DElayed Feedback modeling with UnbiaSed Estimation) instead partitions every observed sample into four finer-grained types — immediate positive (IP, converts within the short observation window w_o), fake negative (FN), real negative (RN), and delay positive (DP, already-known late converters re-ingested with a positive label) — and derives separate, provably asymptotically-unbiased importance weights for each type (Section 4.1, proof in the appendix), using a two-step optimization that first infers a latent probability z(x) that an observed negative is actually a fake negative, then applies the derived weights. A **Bi-Distribution** multi-task architecture (shared bottom, separate in-window/out-window expert-gate branches) further splits training into an unbiased "immediate positive" sub-task (trained directly on non-duplicated, correctly-labeled data) and a corrected "delay positive" sub-task (trained with the importance weights), summing the two probabilities for the overall CVR prediction. Experiments on the public Criteo dataset (in 30-day and 1-day attribution-window variants) and a large industrial Taobao dataset (5.2 billion samples, 21 days) show DEFUSE/Bi-DEFUSE outperforming FNW, ES-DFM, and DEFER, and DEFUSE's importance-weight correction is shown to generalize as a drop-in replacement across all three prior duplicating mechanisms. A production online A/B test reports a CVR gain.

## 2. Experiment Critique

One-paragraph summary (priority 3, per depth rule): the offline evaluation is a streaming simulation (models trained and evaluated hour-by-hour) on Criteo-30d, Criteo-1d, and the industrial Taobao dataset, reported via AUC, PR-AUC, NLL, and a relative-improvement metric (RI-AUC, normalized against a Pretrained-vs-Oracle bound) rather than raw significance tests. The paper is candid that a strong prior competitor, DFM (Chapelle 2014), was excluded from comparison entirely because it "is difficult to converge on our sizeable industrial dataset due to the difficulty of estimating the delay time based on a strong distribution assumption" — a direct empirical data point against the exponential-hazard assumption at industrial scale. The ablations (Section 5.5) are unusually thorough for this batch: they separately test the effect of how the latent fake-negative variable z(x) is estimated (Table 7), the effect of removing the shared-network gating (Figure 4), and — most relevant to this project — the effect of the attribution window length w_a itself, swept across {1, 3, 7, 14, 30} days (Figure 5), which is direct evidence that the method's advantage *shrinks as the window lengthens toward a month*, even though the underlying feature domain remains ordinary advertising conversion. A production A/B test with a 30-minute observation window and 1-day attribution window reports CVR +2.28%, but no confidence interval or test duration is given for this single online number.

## 3. Industry Contribution

One-paragraph summary (priority 3, per depth rule): the paper targets a concrete streaming-training engineering trade-off directly familiar to ad-serving teams — a short observation window w_o keeps training data fresh but mislabels many true positives as negative, and DEFUSE's four-way sample partition plus learned fake-negative probability is explicitly designed as a drop-in loss reweighting that "can be applied to different duplicating mechanisms" (demonstrated by inserting DEFUSE's weights into FNW, ES-DFM, and DEFER's existing pipelines, Table 6), rather than a full architecture replacement. Code is released (https://github.com/ychen216/DEFUSE.git). The stated engineering cost is the Bi-Distribution model's extra shared-gate multi-task architecture (Figure 3), which the paper's own ablation shows outperforms a naive "two fully independent models" design (`ind`) while using roughly half the compute/storage of that alternative — a genuine deployability argument, though only demonstrated at industrial-advertising latency/serving requirements, not discussed explicitly.

## 4. Novelty vs. Prior Work

One-paragraph summary (priority 3, per depth rule): the explicit novelty is (1) recognizing that prior importance-sampling delayed-feedback methods implicitly conflate fake negatives with real negatives, degrading their importance weights, and (2) deriving finer-grained, asymptotically-unbiased weights for four sample types instead of two, plus (3) the Bi-Distribution architecture that trains the always-correctly-labeled immediate-positive sub-task without any importance-sampling bias at all. The most heavily cited/discussed prior works are Chapelle (2014), the delayed-feedback founding paper (this batch's paper 1, excluded from experimental comparison as noted above); Ktena et al. (2019), FNW/FNC, the fake-negative weighting/calibration duplicating mechanism DEFUSE's weights are shown to plug into; Ma et al. (2021, AAAI), ES-DFM, the elapsed-time-sampling observation-window method, a second duplicating mechanism DEFUSE is shown to improve; Gu et al. (2021, KDD), DEFER, the "real negatives matter" duplicating mechanism, a third baseline/host pipeline; and Yoshikawa & Imai (2018), a non-parametric delayed-feedback model, cited as an alternative to Chapelle's exponential assumption.

## 5. Dataset Availability

| Dataset | Size | Description | Public? |
|---|---|---|---|
| Criteo (30-day and 1-day attribution variants) | 5,443 items, 17 features, 3,619,801 conversions, 15,898,883 samples, 60-day duration, avg. CVR 0.2269 | Public display-advertising click/conversion logs (same underlying dataset as Chapelle 2014 and FSIW) | Yes — https://labs.criteo.com/2013/12/conversion-logs-dataset/ |
| Taobao industrial dataset | ~382 million users, 10.6 million items, 23 features, ~208 million conversions, ~5.2 billion samples, 21-day duration, avg. CVR 0.04005 | Industrial e-commerce click/conversion streaming logs | No — proprietary Alibaba data |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

1. **Title, authors, venue, year, URL:** "Asymptotically Unbiased Estimation for Delayed Feedback Modeling via Label Correction," Yu Chen, Jiaqi Jin, Hui Zhao, Pengjie Wang, Guojun Liu, Jian Xu, Bo Zheng, Alibaba Group, WWW 2022. https://doi.org/10.1145/3485447.3511965 (code: https://github.com/ychen216/DEFUSE.git)
2. **Source type:** Industry paper (Alibaba Group; peer-reviewed at WWW).
3. **Direction:** D7.
4. **Problem setting:** Streaming CVR prediction for online advertising, where a short observation window w_o (needed to keep streaming training data fresh) causes many true positives to be mislabeled negative before eventually converting within the longer attribution window w_a.
5. **Objective and label definition:** Predicts overall P(conversion=1|x), decomposed as P(immediate positive, converts ≤ w_o) + P(delay positive, converts > w_o but ≤ w_a), trained jointly by the Bi-Distribution multi-task architecture. Horizon: attribution window w_a = 30 days (Criteo-30d) or 1 day (Criteo-1d, Taobao); explicit ablation over w_a ∈ {1, 3, 7, 14, 30} days. Delay/censoring handled via a four-way sample-type partition (immediate positive / fake negative / real negative / delay positive) plus a learned latent fake-negative probability z(x), rather than a parametric delay distribution.
6. **Prediction or incrementality:** Prediction only — the paper does not address incrementality.
7. **Model architecture:** Multi-task "Bi-Distribution" network (shared bottom layers; separate in-window and out-window expert/gate branches) jointly optimizing an in-window loss and an importance-weighted out-window loss; the latent fake-negative probability z(x) is modeled either by a direct binary classifier or indirectly via the CVR model combined with an auxiliary delay-positive-probability model.
8. **Credit assignment:** Not specified in source. As with the rest of this batch, the prediction unit is a single click/impression and its own (possibly delayed) conversion; there is no user-level-to-item-level aggregation problem addressed.
9. **Training data and counterfactual handling:** Public Criteo dataset (two attribution-window variants) and the industrial Taobao streaming dataset. Counterfactual handling: importance sampling with weights derived to asymptotically match the ground-truth distribution across the four sample types (Section 4.1.1), explicitly contrasted with — and shown to plug into — the sample-duplication mechanisms of FNW, ES-DFM, and DEFER.
10. **Offline and online evaluation:** Offline — AUC, RI-AUC, PR-AUC, NLL in a simulated hourly streaming setting on Criteo and Taobao. Online — a production A/B test (30-minute observation window, 1-day attribution window) reporting CVR +2.28%.
11. **Reported gains:** DEFUSE/Bi-DEFUSE improve RI-AUC over the strongest prior baseline (ES-DFM/DEFER) by 6.22% on Criteo-30d, 2.13% on Criteo-1d, and 15.31% on the Taobao dataset (Table 5); absolute AUC on Taobao reaches 0.8069 (DEFUSE) / 0.8080 (Bi-DEFUSE) versus 0.8066 for the best baseline (ES-DFM). Production online A/B test: CVR +2.28%.
12. **Applicability to a two-sided dating recommender:** The finer-grained sample-type partition and learned fake-negative estimator are a real methodological refinement over this batch's other label-correction papers, but the method's own ablation (Figure 5) shows its advantage *degrading as the attribution window lengthens toward 30 days* — already the paper's own upper bound, and still well short of the weeks-long revenue horizon this project needs, so the correction's reliability at that scale is directly unverified rather than merely untested.
13. **Unverified claims:** The "asymptotically unbiased" claim is proven in the appendix under a stated feature-distribution-invariance assumption (p(x)≈q(x)), not merely asserted — but the paper's own derivation (Equation 33) explicitly notes the practical weight estimator becomes exact only "with sufficient data, which is usually abundant in digital advertising," i.e., the guarantee is asymptotic and conditional on data volumes this project's much sparser retention/subscription events may not match. The interpretation that Bi-DEFUSE's advantage shrinks with longer w_a "because smaller w_a … makes the unbiased prediction of IPs more decisive" (Section 5.5.3) is offered as a post-hoc reading of Figure 5, not isolated by a controlled ablation.

## Project Relevance

This paper speaks most directly to **Q3** (label/horizon/delay handling), contributing both a finer-grained mechanism than DFM or FSIW and — unusually for this batch — direct empirical evidence (its own w_a ablation) of a scale mismatch: even within advertising, the correction's advantage degrades as the attribution window approaches a month, which is a load-bearing data point for the survey's caution that this batch's toolkit was built for hours-to-days delays, not weeks. It touches **Q6** only lightly (a single unreplicated online A/B number). It does not address **Q1** (no retention/LTV objective), **Q2** (no user-level-to-item-level credit assignment), **Q4–Q5** (no head fusion, no incrementality), or **Q7** (no two-sided/reciprocal market treatment).

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2014_KDD_DFM_Modeling-Delayed-Feedback-Display-Advertising.md](./2014_KDD_DFM_Modeling-Delayed-Feedback-Display-Advertising.md) | Related Work / Experiments | Names this paper's method (`DEFUSE`) |
| [2019_RecSys_FNW-FNC_Addressing-Delayed-Feedback-Continuous-Training.md](./2019_RecSys_FNW-FNC_Addressing-Delayed-Feedback-Continuous-Training.md) | Related Work / Experiments | Names this paper's method (`DEFUSE`) |
| [2020_WWW_FSIW_Feedback-Shift-Correction-Delayed-Feedback.md](./2020_WWW_FSIW_Feedback-Shift-Correction-Delayed-Feedback.md) | Related Work / Experiments | Names this paper's method (`DEFUSE`) |
| [2021_AAAI_ESDF_Delayed-Feedback-Modeling-Entire-Space.md](./2021_AAAI_ESDF_Delayed-Feedback-Modeling-Entire-Space.md) | Related Work / Experiments | Names this paper's method (`DEFUSE`) |
| [2024_AAAI_MISS_Online-Conversion-Rate-Prediction-Multi-Interval-Screening.md](./2024_AAAI_MISS_Online-Conversion-Rate-Prediction-Multi-Interval-Screening.md) | Related Work / Experiments | Names this paper's method (`DEFUSE`) |
| [2026_SIGIR_CM-DCM_Counterfactual-Multi-task-Learning-Delayed-Conversion.md](./2026_SIGIR_CM-DCM_Counterfactual-Multi-task-Learning-Delayed-Conversion.md) | Related Work / Experiments | Names this paper's method (`DEFUSE`) |

_6 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `DEFUSE` across all 133 cards._

## Meta Information

- **Authors:** Yu Chen, Jiaqi Jin, Hui Zhao, Pengjie Wang, Guojun Liu, Jian Xu, Bo Zheng
- **Affiliations:** Alibaba Group
- **Venue:** The Web Conference (WWW) 2022
- **Year:** 2022
- **Relevance:** Core
- **Priority:** 3
- **NotebookLM source:** nlm:d16aaef1
