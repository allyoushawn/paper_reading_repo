# Paper Analysis: Asymptotically Unbiased Estimation for Delayed Feedback Modeling via Label Correction

**Source:** https://doi.org/10.1145/3485447.3511965
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Asymptotically Unbiased Estimation for Delayed Feedback Modeling via Label Correction
- **authors or company:** Yu Chen, Jiaqi Jin, Hui Zhao, Pengjie Wang, Guojun Liu, Jian Xu, Bo Zheng (Alibaba Group)
- **venue:** WWW
- **year:** 2022
- **URL:** https://doi.org/10.1145/3485447.3511965
- **source type:** industry paper
- **direction:** D7
- **problem setting:** Streaming CVR prediction in online advertising; short observation window \(w_o\) creates fake negatives; prior importance-sampling methods falsely treat FNs as real negatives.
- **objective and label definition:** CVR \(p(y=1|x)\) decomposed into immediate positive IP (\(d\le w_o\)) plus delayed positive DP (\(d>w_o\)); attribution window \(w_a\) (1 day Taobao, 30 days Criteo); four sample types: IP, FN, RN, DP.
- **prediction or incrementality:** Predicts absolute conversion probability; not incrementality of ad exposure.
- **model architecture:** DEFUSE: label-corrected importance sampling with latent fake-negative probability \(z(x)\); Bi-DEFUSE: MMoE multi-task with in-window head \(F_{IP}(x)\) and out-window head \(F_{DP}(x)\), fused as \(p(y=1|x)=F_{IP}(x)+F_{DP}(x)\).
- **credit assignment:** Delayed conversion mapped back to original click features \(x\) at \(t_0\); DP duplicated with positive label injected at conversion time.
- **training data and counterfactual handling:** Asymptotically unbiased importance weights for four sample types; two-step optimization infers \(z(x)\) (via \(z_1=1-f_{rn}(x)\) or \(z_2=f_{dp}/(f_{dp}+1-f_\theta)\)) before weighted loss; bi-distribution splits unbiased IP task from DEFUSE-weighted DP task.
- **offline and online evaluation:** Streaming simulation on Criteo-30d, Criteo-1d, Taobao (5.2B interactions); hourly train/test; AUC, PR-AUC, NLL, RI-AUC. Online A/B: \(w_o=30\)min, \(w_a=1\)day, +2.28% CVR lift.
- **reported gains:** Criteo-30d: DEFUSE AUC 0.8408 (RI-AUC 52.33% vs ES-DFM 46.11%); Criteo-1d: Bi-DEFUSE AUC 0.8467 (RI-AUC 96.30%); Taobao: Bi-DEFUSE AUC 0.8080 (RI-AUC 66.33% vs ES-DFM 52.04%); online +2.28% CVR.
- **applicability note for a two-sided dating recommender:** Direct blueprint for streaming match/reply models with short observation windows and delayed mutual-match labels—four-way sample taxonomy plus bi-head fusion mirrors like→match funnels.
  Advertising CVR setting is one-sided; Bi-DEFUSE degrades at long \(w_a\) (14–30 days), relevant when dating retention horizons exceed ~7 days.
- **unverified claims:** none

## 1. Summary

DEFUSE corrects streaming CVR bias from fake negatives by classifying samples into IP/FN/RN/DP and applying asymptotically unbiased importance weights that distinguish fake from real negatives via inferred \(z(x)\). Bi-DEFUSE adds an MMoE architecture separating unbiased in-window immediate conversion from out-window delayed conversion. Outperforms FNW, FNC, ES-DFM, and DEFER on public and industrial datasets; deployed online with +2.28% CVR.

## 2. Experiment Critique

Strengths: billion-scale Taobao data, streaming hourly protocol, online A/B validation, ablations on \(z_1\) vs \(z_2\) and attribution-window length. Weaknesses: Bi-DEFUSE underperforms at long \(w_a\); \(z_2\) unstable; high variance in full DEFUSE; DFM baseline failed to converge on Taobao; independent two-network ablation doubles compute.

## 3. Industry Contribution

Production streaming CVR pipeline at Alibaba: 30-minute observation window, duplicate-on-conversion, four-type importance correction. Online A/B confirms offline gains. MMoE bi-distribution design balances accuracy and compute vs fully independent heads.

## 4. Novelty vs. Prior Work

First four-way sample taxonomy with label-corrected importance sampling for fake negatives. Builds on Chapelle DFM (2014), FNW/FNC (Ktena et al. 2019), ES-DFM (Yang et al. 2021), DEFER (Gu et al. 2021), MMoE (Ma et al. 2018).

## 5. Dataset Availability

- **Criteo:** Public conversion dataset (30-day and 1-day attribution variants).
- **Taobao:** Industrial dataset (5.2B interactions, 21 days).

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

### (1) Ranking objective: retention / LTV / revenue vs CTR
CVR prediction for CPA/CPC bidding; revenue via platform ROI. Retention/LTV: Not specified in source.

### (2) Credit assignment: user-level delayed outcome → item-level decision
Delayed conversion mapped to original click features; DP re-injected at conversion time with label 1.

### (3) Label and horizon definitions; delay, sparsity, censoring
\(w_o\) observation window (30min online); \(w_a\) attribution window (1–30 days). Four sample types IP/FN/RN/DP. Importance sampling + \(z(x)\) for FN inference. Bi-distribution reduces variance on sparse conversions.

### (4) Short vs long-term head fusion
Fixed additive fusion: \(p(y=1|x)=F_{IP}(x)+F_{DP}(x)\); MMoE shared experts with task-specific gates.

### (5) Prediction vs incrementality
Absolute CVR prediction; not incrementality.

### (6) Offline and online evaluation
Offline streaming AUC/PR-AUC/NLL on Criteo and Taobao. Online A/B: +2.28% CVR.

### (7) Reciprocity, congestion, fairness, revenue vs match quality
Not specified in source.

### (8) Migration path from CTR-like model toward unified long-term model
Vanilla → Vanilla-Win → FNW/FNC → DEFUSE (four-type weights + \(z(x)\)) → Bi-DEFUSE (decoupled IP/DP MMoE heads).

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Yu Chen, Jiaqi Jin, Hui Zhao, Pengjie Wang, Guojun Liu, Jian Xu, Bo Zheng
**Affiliations:** Alibaba Group
**Venue:** WWW 2022
**Year:** 2022
**PDF:** https://doi.org/10.1145/3485447.3511965
**Relevance:** Core
**Priority:** 1
