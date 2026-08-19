# Paper Analysis: Online Conversion Rate Prediction via Multi-Interval Screening and Synthesizing under Delayed Feedback

**Source:** /Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/29402.pdf
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** Online Conversion Rate Prediction via Multi-Interval Screening and Synthesizing under Delayed Feedback
**Authors:** Qiming Liu, Xiang Ao, Yuyao Guo, Qing He (Key Lab of Intelligent Information Processing, Institute of Computing Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences)
**Venue/Year:** AAAI-24 (Thirty-Eighth AAAI Conference on Artificial Intelligence), 2024

MISS addresses the freshness/label-accuracy trade-off in choosing a single waiting window for online CVR prediction under delayed feedback by training an ensemble of heads instead of one model. A shared-bottom "multi-interval screening" model trains N independent output heads, each on a differently-windowed, duplication-corrected training pipeline (waiting windows d_1 > d_2 > ... > d_N, e.g., [1,7,14,21,30] days on Criteo or [1,6,24,48,120] hours on Tencent) — shorter windows are fresher but noisier (more fake negatives), longer windows are more label-accurate but staler. A lightweight "assembled pipeline synthesizing" model then takes the concatenated head predictions (plus a normalized variant) as input and produces softmax-weighted dynamic aggregation weights, trained on an "assembled data pipeline" that substitutes the latest confirmed positive samples for older, staler ones — shown via accumulated KL-divergence analysis to sit closer to the ideal ground-truth distribution than the standard maximum-attribution-window dataset. Finally, a low-cost "global positive weighting" step (an importance-sampling-style correction using a single hyperparameter α rather than an auxiliary model) globally amplifies the weight of positive samples to counter residual fake-negative bias. On Criteo and the Tencent Advertising Algorithm Competition 2017 dataset, under a streaming online-simulation protocol, MISS significantly outperforms FNW, FNC, ES-DFM, DEFUSE, MTDFM, and FTP baselines, achieving relative-AUC improvements of 16.8% (Criteo) and 6.1% (Tencent) over the strongest baseline, normalized against the Pretrain-to-Oracle gap.

## 2. Experiment Critique / 3. Industry Contribution / 4. Novelty vs. Prior Work / 5. Dataset Availability

Condensed per the Priority-4 depth rule — see the Reference Card (Section 7) and Project Relevance below. Datasets: Criteo Conversion Logs (public, labs.criteo.com/2013/12/conversion-logs-dataset, 30-day attribution window, ~16M samples, avg CVR 0.2277) and Tencent Advertising Algorithm Competition 2017 (public, algo.qq.com, 5-day attribution window, ~22.6M samples, avg CVR 0.0276). Source code linked at github.com/NealWalker/MISS. Ablation study (MISS_O/L/A/R/H variants on Criteo) confirms the duplication mechanism and the dynamic-weight synthesizing model both matter, with naive last-head or averaged-head aggregation performing measurably worse. Novelty is framing multiple waiting windows explicitly as a bagging/stacking-style ensemble with a learned, dynamic aggregation weight (rather than a single fixed window, a single auxiliary re-weighting model, or an ad hoc multi-head imitation target as in the cited FTP baseline), plus the assembled-pipeline freshness trick and the auxiliary-model-free global positive-weighting correction.

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Online Conversion Rate Prediction via Multi-Interval Screening and Synthesizing under Delayed Feedback," Qiming Liu, Xiang Ao, Yuyao Guo, Qing He; Institute of Computing Technology, Chinese Academy of Sciences / University of Chinese Academy of Sciences; AAAI-24, 2024; code at https://github.com/NealWalker/MISS |
| 2 | Source type | Academic |
| 3 | Direction | D7 |
| 4 | Problem setting | Online CVR prediction under delayed feedback in cost-per-action (CPA) display advertising, specifically the trade-off between data freshness and label accuracy inherent in choosing a single waiting window before treating a sample's label as final. |
| 5 | Objective and label definition | Binary label ŷ_i = 1 if conversion timestamp v_i ≤ click timestamp c_i + maximum attribution time d_max, else 0 (Eq. 2) — a hard threshold at a fixed maximum attribution window (30 days on Criteo, 5 days on Tencent). MISS additionally defines per-head training datasets D+_{τ,d_i} at N shorter waiting windows d_1>...>d_N < d_max (with duplication: a sample later confirmed positive within its head's window replaces its earlier fake-negative copy), so censoring is handled as an ensemble of several simultaneous hard-threshold windows rather than one. Horizon: explicit and dataset-native — 30 days (Criteo) and 5 days (Tencent), with per-head windows swept as [1D,7D,14D,21D,30D] on Criteo and [1H,6H,24H,48H,120H] on Tencent. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. MISS is a bias-correction/ensemble-aggregation technique for a CVR probability prediction; it does not estimate the causal effect of an exposure. |
| 7 | Model architecture | Shared bottom/embedding layers + N independent output heads h_1...h_N, each trained on its own duplication-corrected data pipeline D+_{τ,d_i} at waiting window d_i (Eq. 10). Head predictions are concatenated (x_pred) alongside a normalized variant (x_norm) and fed to a lightweight "synthesizing" model (small dense layers + softmax) that outputs dynamic per-head weights w_i, producing the final CVR y_s = Σ w_i·y_hi (Eq. 14). The synthesizing model is trained on an "assembled data pipeline" M_τ that substitutes the latest confirmed positives for the oldest ones used by the max-window dataset. A separate, model-free "global positive weighting" step (Eqs. 15–17, hyperparameter α) amplifies positive-sample weights across all heads to correct residual fake-negative bias. |
| 8 | Credit assignment | Not specified in source. Operates at single click → single conversion-label granularity; no multi-item slate or ranked-list credit assignment is addressed. |
| 9 | Training data and counterfactual handling | Criteo (60 days, 30-day attribution window, ~15.9M samples, 3.6M conversions) and Tencent Advertising Algorithm Competition 2017 (9 days, 5-day attribution window, ~22.6M samples, 624K conversions). No counterfactual/causal treatment-effect handling — importance-sampling-derived reweighting (Eq. 9, following Bottou et al. 2013) is used only to correct sampling bias from the delayed-feedback data pipeline toward the ideal (fully-labeled) distribution, not to estimate a treatment effect. |
| 10 | Offline and online evaluation | Offline only, via a streaming online-simulation protocol (pretraining split + hour-by-hour streaming evaluation and update), reporting AUC, NLL, and PR-AUC, with 5 random runs and significance testing (p<0.05) against Pretrain (0%) and Oracle (100%) anchors. No online A/B test is reported. |
| 11 | Reported gains | On the Pretrain(0%)→Oracle(100%) relative-improvement scale (Table 2): Criteo — MISS RI-AUC 83.7%*, RI-NLL 83.9%*, RI-PRAUC 78.1%*, a 16.8-percentage-point RI-AUC gain over the strongest Criteo AUC baseline (DEFUSE at 66.9%). Tencent — MISS RI-AUC 86.0%*, RI-NLL 82.8%*, RI-PRAUC 88.2%*, a 6.1-percentage-point RI-AUC gain over the strongest Tencent AUC baseline (FTP at 79.9%). (* = p<0.05 vs. best baseline.) |
| 12 | Applicability to a two-sided dating recommender | The multi-window-ensemble idea (train several heads at different label-accuracy/freshness trade-off points and learn a dynamic aggregation weight) is a reasonable pattern if the project ultimately needs several intermediate retention checkpoints (e.g., 7-day, 14-day, 30-day heads) rather than a single 30-day label. But MISS's own tested windows (up to 30 days, mostly hours-to-days) sit at the short end of the project's 7–30-day retention / weeks-long revenue range, and the method has no two-sided or reciprocal-market treatment. |
| 13 | Unverified claims | None beyond standard motivating citations; the paper's quantitative claims are all tied to reported experimental tables in the read sections. |

## Project Relevance

Speaks most directly to **Q3** (label/horizon/censoring handling: an explicit multi-window ensemble as an alternative to a single hard threshold or a continuous survival function, plus a model-free global positive-reweighting correction). Marginally informs **Q4** (combining several differently-windowed prediction heads via a learned dynamic-weight synthesizing model — a fixed-architecture, learned-fusion pattern, though fusing heads of the *same* target at different windows rather than fusing short-term and long-term *different* objectives). Does not address Q1, Q2, Q5, Q6 (online), Q7, or Q8.

**Low-to-moderate project relevance.** The dataset-native horizons (30 days Criteo, 5 days Tencent) sit at the short end of the project's retention window and well short of its weeks-long revenue horizon, and the setting is single-sided display advertising with no reciprocity or congestion. The most transferable idea is structural — an ensemble of windowed heads reconciled by a learned aggregator, and a low-cost (auxiliary-model-free) global positive-reweighting correction — rather than any of its reported numbers.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `MISS`._

## Meta Information

- **Authors:** Qiming Liu, Xiang Ao, Yuyao Guo, Qing He
- **Affiliations:** Key Lab of Intelligent Information Processing, Institute of Computing Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences
- **Venue:** AAAI
- **Year:** 2024
- **Relevance:** Related
- **Priority:** 4
- nlm:8b7867b6
