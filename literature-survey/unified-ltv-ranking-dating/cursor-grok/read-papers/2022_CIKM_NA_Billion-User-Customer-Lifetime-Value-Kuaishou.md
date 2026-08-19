# Paper Analysis: Billion-user Customer Lifetime Value Prediction: An Industrial-scale Solution from Kuaishou

**Source:** https://arxiv.org/pdf/2208.13358.pdf
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Billion-user Customer Lifetime Value Prediction: An Industrial-scale Solution from Kuaishou
- **authors or company:** Kunpeng Li, Guangcui Shao, Naijun Yang, Xiao Fang, Yang Song (Kuaishou)
- **venue:** CIKM
- **year:** 2022
- **URL:** https://arxiv.org/pdf/2208.13358.pdf
- **source type:** industry paper
- **direction:** D4
- **problem setting:** Multi-horizon new-user LTV prediction at billion-user scale for user-growth/ad ROI; not feed ranking.
- **objective and label definition:** Active return days (offline) or platform value after 30 days (online A/B) at horizons 30/90/180/365; ordered \(ltv_{30}\le ltv_{90}\le ltv_{180}\le ltv_{365}\).
- **prediction or incrementality:** Predicts absolute multi-horizon LTV; ROI uplift measured only in online A/B.
- **model architecture:** ODMN multi-task framework with MDME divide-and-conquer (distribution segmentation + bucket classification/ordinal + bias regression) and Mono Units enforcing cross-horizon monotonicity.
- **credit assignment:** Not specified in source (user-level acquisition prediction).
- **training data and counterfactual handling:** 180M new-user industrial logs (7-day post-register features); no item-level counterfactuals.
- **offline and online evaluation:** Offline NRMSE, NMAE, AMBE, Mutual Gini, Gini; online A/B on ad delivery ROI-7/14/30 vs ZILN.
- **reported gains:** ODMN vs ZILN on \(ltv_{30}\): AMBE 0.0423 vs 0.1336; Mutual Gini 0.0125 vs 0.0226; online ROI +11.9%/+12.8%/+14.7%.
- **applicability note for a two-sided dating recommender:** MDME’s bucketed loss design directly addresses whale-sparse LTV tails; ODMN’s horizon monotonicity fits dating where D7/D30/D90 retention/value must stay ordered.
  Mono Units + calibration loss are a concrete pattern for fusing short-horizon retention signals into longer subscriber-value heads without violating business constraints.
- **unverified claims:** none

## 1. Summary

Kuaishou presents ODMN (Order Dependency Monotonic Network) for simultaneous prediction of multi-span LTV (\(ltv_{30}\)–\(ltv_{365}\)) on 180M new users. Each horizon uses an MDME module that segments the imbalanced distribution, classifies buckets with ordinal distillation, and regresses within-bucket bias. Mono Units transfer short-horizon bucket distributions to longer horizons with gradient truncation and a calibration penalty when short-term predictions exceed long-term ones. The paper introduces Mutual Gini (Lorenz-curve area gap) and reports large offline gains over two-stage XGBoost and ZILN, plus +11.9–14.7% ROI in online user-growth A/B tests.

## 2. Experiment Critique

Strengths: massive real industrial data, strong baselines (ZILN, two-stage), multi-horizon metrics including distribution-fit Mutual Gini, ablation on Mono Unit, and production A/B. Weaknesses: online label for A/B differs from offline active-days label; Gini alone can miss crossing Lorenz curves (motivating Mutual Gini); ZILN lognormal assumption noted as restrictive; standard shared-bottom MTL without ODMN gives limited gains.

## 3. Industry Contribution

End-to-end deployed pipeline: day-level batch training, cached LTV for real-time acquisition bidding. MDME reframes heavy-tailed regression as balanced classification + localized MSE—practical stabilization vs raw MSE on whales. ODMN is the reference industrial extension of ZILN to multi-horizon ordered LTV.

## 4. Novelty vs. Prior Work

Extends ZILN (Wang et al. 2019), two-stage LTV (Drachen et al. 2018), BTYD/RFM (Fader et al.), TSUR sequence LTV (Xing et al. KDD 2021), ordinal regression (Fu et al. 2018), sequential MTL dependencies (Xi et al. 2021), MMoE/PLE backbones. Novel: MDME divide-and-conquer + cross-horizon Mono Unit + Mutual Gini metric.

## 5. Dataset Availability

Proprietary Kuaishou user-growth dataset (180M new users); not publicly released.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

### (1) Ranking objective: retention / LTV / revenue vs CTR
LTV/revenue prediction for acquisition ROI and CRM; not feed ranking. CTR mentioned only as unrelated representation technique (DeepFM/DCN).

### (2) Credit assignment: user-level delayed outcome → item-level decision
Not specified in source.

### (3) Label and horizon definitions; delay, sparsity, censoring
Offline label: active return days at 30/90/180/365 days from 7-day post-register features. Online A/B: value user brings in 30 days. Extreme sparsity of high-value users; raised long tail. Censoring and explicit label delay: not specified in source.

### (4) Short vs long-term head fusion
Mono Units add transformed upstream bucket distributions to downstream DCT/BCT logits; `stop_gradient` on upstream; calibration loss penalizes \(y_t > y_{t+1}\). Learned cross-horizon transfer, not fixed weighted sum.

### (5) Prediction vs incrementality
Absolute multi-horizon prediction; incrementality assessed only via platform-level online ROI A/B.

### (6) Offline and online evaluation
Offline: 180M-user dataset, NRMSE/NMAE/AMBE/Mutual Gini. Online: 10% control (ZILN) vs 10% treatment, ROI-7/14/30 uplifts +11.9%/+12.8%/+14.7%.

### (7) Reciprocity, congestion, fairness, revenue vs match quality
Not specified in source.

### (8) Migration path from CTR-like model toward unified long-term model
Deployed in user-growth with day-level batch training and cached scores. Phased migration steps: not specified in source.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Kunpeng Li, Guangcui Shao, Naijun Yang, Xiao Fang, Yang Song
**Affiliations:** Kuaishou
**Venue:** CIKM
**Year:** 2022
**PDF:** https://arxiv.org/pdf/2208.13358.pdf
**Relevance:** Core
**Priority:** 1
