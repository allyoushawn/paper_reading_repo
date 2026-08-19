# Paper Analysis: Delayed Feedback Modeling with Influence Functions

**Source:** /Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/42445.pdf
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** Delayed Feedback Modeling with Influence Functions
**Authors:** Chenlu Ding, Jiancan Wu, Yancheng Yuan, Cunchun Li, Xiang Wang, Dingxian Wang, Frank Yang, Andrew Rabinovich (University of Science and Technology of China; Shanghai Key Laboratory for Data Science; The Hong Kong Polytechnic University; Upwork)
**Venue/Year:** AAAI-26 (Fortieth AAAI Conference on Artificial Intelligence), 2026

IF-DFM addresses the standard delayed-feedback CVR problem (a clicked sample not yet converted at model-training time T is labeled a fake negative, and the true label may reverse to positive after T) with a different mechanism than the rest of this batch: instead of duplicating samples, training auxiliary label-correction models, or waiting/retraining, it uses influence functions — a robust-statistics tool for estimating how a model's parameters would change under a small perturbation to the training data — to directly estimate the parameter update caused by (a) label reversals (fake negatives that later convert) and (b) newly arrived post-deployment behavioral data, without retraining. The core technical contribution is reformulating the expensive inverse-Hessian-vector product (normally required by influence functions) as an equivalent finite-sum convex quadratic optimization problem solvable with a standard stochastic optimizer (Adam), making the approach scalable. On Criteo and Taobao benchmarks, across four CVR backbones (MLP, DeepFM, AutoInt, DCNV2) and against 13 baselines including DFM, FSIW, ES-DFM, and DDFM, IF-DFM achieves average improvements of 0.55% AUC, 1.29% PR-AUC, and 4.99% LL over the best baseline, closing 85.16%/82.07%/85.89% of the Vanilla-to-Retrain performance gap while updating parameters in 14.8 seconds versus 1351.4 seconds for full retraining (1.1% of the cost) — and it degrades more gracefully than baselines as the temporal gap between training and test data grows, indicating better adaptation to evolving user interest without needing auxiliary models.

## 2. Experiment Critique / 3. Industry Contribution / 4. Novelty vs. Prior Work / 5. Dataset Availability

Condensed per the Priority-4 depth rule — see the Reference Card (Section 7) and Project Relevance below. Datasets: Criteo (public, labs.criteo.com/2013/12/conversion-logs-dataset, 3M-sample subset used for training) and Taobao (public, tianchi.aliyun.com/dataset, dataId=649). Code released at github.com/oceanoceanna/IF-DFM. Backbones: MLP, DeepFM, AutoInt, DCNV2, following the same experimental convention as Wang et al. 2023 (ULC) for fair comparison. Novelty is the direct application of influence functions — reformulated as a scalable finite-sum optimization rather than a literal Hessian inversion — to update a deployed CVR model's parameters for both delayed-label correction and new-data integration, eliminating the auxiliary-model and full-retrain costs that dominate the FSIW/ES-DFM/DDFM lineage.

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Delayed Feedback Modeling with Influence Functions," Chenlu Ding, Jiancan Wu, Yancheng Yuan, Cunchun Li, Xiang Wang, Dingxian Wang, Frank Yang, Andrew Rabinovich; USTC / Shanghai Key Laboratory for Data Science / Hong Kong Polytechnic University / Upwork; AAAI-26, 2026; code at https://github.com/oceanoceanna/IF-DFM |
| 2 | Source type | Academic (with an industry-affiliated co-author group, Upwork) |
| 3 | Direction | D7 |
| 4 | Problem setting | CVR prediction under delayed feedback in cost-per-conversion (CPA) online advertising: a click sample not yet converted by a model-training-start timestamp T is labeled a fake negative (observed label y^O=0), which may later reverse to a true positive once conversion occurs. |
| 5 | Objective and label definition | Binary CVR label; observed label y^O_i = 0 if conversion has not occurred by the training-start timestamp T (default −1/negative if unobserved), true label y^T_i =1 if the sample eventually converts. Delay/censoring is handled not by a survival function but by treating a later-observed conversion (a "label reversal") as a data perturbation, and using the influence function's first-order approximation to estimate the resulting model parameter change (Δθ_delay, Eq. 9) without retraining — an efficient approximation to what a full retrain with corrected labels would produce. Horizon: not restated explicitly for this paper's own experiments beyond adopting the standard Criteo (30-day, per Chapelle 2014 convention) and Taobao settings; training uses a 3M-sample, 14-day Criteo subset, with a temporal-gap robustness experiment (Table 3) evaluated at gaps of "c=5" and "c=14" (days, by convention with the same "c" notation used elsewhere in this lineage). |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. IF-DFM uses influence functions purely to correct label bias/staleness in a CVR probability prediction model's parameters (approximating what retraining on corrected labels would yield); it does not estimate the causal effect of an exposure. |
| 7 | Model architecture | Backbone-agnostic (tested on MLP, DeepFM, AutoInt, DCNV2). The method itself is not a network architecture but a parameter-update procedure: given a trained "Vanilla" model θ̂, IF-DFM computes Δθ_total = Δθ_delay + Δθ_add by solving a convex quadratic optimization problem (Eq. 18, an equivalent finite-sum reformulation of the inverse-Hessian-vector product) via Adam, then directly applies θ_new = θ̂ + Δθ_total without retraining. |
| 8 | Credit assignment | Not specified in source. Operates at single click sample → single conversion-label granularity; no multi-item slate or ranked-list credit assignment is addressed. |
| 9 | Training data and counterfactual handling | Criteo (3M samples, 14 days) and Taobao (public interaction logs with timestamps). No counterfactual/causal treatment-effect handling — this is a label-noise/label-reversal bias-correction technique via influence functions, not treatment-effect estimation. |
| 10 | Offline and online evaluation | Offline only, via a temporally-partitioned pretrain/streaming protocol (train/validation/test split by elapsed days c after the training cutoff), reporting AUC, PR-AUC (PRAUC), and Log Loss (LL), plus a Relative Improvement metric normalized against the Vanilla-to-Retrain performance gap, and separately reported wall-clock update time. No online A/B test is reported; the paper's own Limitations section states real-world A/B deployment is left to future work. |
| 11 | Reported gains | Criteo, averaged across four backbones: IF-DFM achieves average improvements of 0.55% AUC, 1.29% PRAUC, and 4.99% LL over the best baseline, and closes 85.16% (AUC) / 82.07% (PRAUC) / 85.89% (LL) of the Vanilla→Retrain relative-improvement gap. Taobao: 0.28% AUC and 0.94% PRAUC gains over the best baseline. Efficiency: parameter update takes 14.8 seconds vs. 1351.4 seconds for full Vanilla retraining (MLP backbone, Criteo, c=10) — roughly 1.1% of retrain cost. |
| 12 | Applicability to a two-sided dating recommender | The efficiency argument (near-retrain accuracy without the cost of retraining or maintaining auxiliary label-correction models) is attractive for a production retention/revenue model that must continuously incorporate newly resolved 7–30-day labels. But the method is validated only at Criteo/Taobao's hours-to-~14-day temporal gaps and single-click-to-single-label granularity; its scalability to week-long horizons, high-cardinality two-sided features, and the volume/parameter-count of a production dating-recommender model is untested. |
| 13 | Unverified claims | None beyond standard forward-looking future-work statements (the paper explicitly flags online A/B validation as future work rather than an untested claim presented as fact) — no other assertions in the read sections lack accompanying experimental support. |

## Project Relevance

Speaks most directly to **Q3** (delay/censoring handling: an influence-function-based label-reversal correction as an alternative to duplication/importance-sampling or survival-analysis approaches used elsewhere in this lineage) and secondarily to operational aspects of **Q6** (evaluation under evolving/non-stationary conditions — the temporal-gap robustness experiment is directly relevant to how a model should be assessed as retention/revenue label distributions drift). Does not address Q1, Q2, Q4, Q5, Q7, or Q8.

**Low-to-moderate project relevance regarding horizon; higher relevance as an operational technique.** The paper's tested delay/temporal-gap regime (days, not weeks) is short relative to the project's 7–30-day retention window, and the single-sided ad-click setting has no two-sided or reciprocal structure. Its most transferable idea is operational rather than architectural: efficiently updating a production model's parameters as delayed labels resolve, without full retraining or auxiliary models — a genuinely different technique from the reweighting/duplication/survival-analysis approaches seen elsewhere in D7.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `IF-DFM`._

## Meta Information

- **Authors:** Chenlu Ding, Jiancan Wu, Yancheng Yuan, Cunchun Li, Xiang Wang, Dingxian Wang, Frank Yang, Andrew Rabinovich
- **Affiliations:** University of Science and Technology of China; Shanghai Key Laboratory for Data Science; The Hong Kong Polytechnic University; Upwork
- **Venue:** AAAI
- **Year:** 2026
- **Relevance:** Related
- **Priority:** 4
- nlm:bffc8cb9
