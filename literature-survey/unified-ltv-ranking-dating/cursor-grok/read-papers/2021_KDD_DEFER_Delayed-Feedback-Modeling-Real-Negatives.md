# Paper Analysis: Real Negatives Matter: Continuous Training with Real Negatives for Delayed Feedback Modeling

**Source:** https://arxiv.org/pdf/2104.14121.pdf
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** Real Negatives Matter: Continuous Training with Real Negatives for Delayed Feedback Modeling
- **authors or company:** Siyu Gu, Xiang-Rong Sheng, Ying Fan, Guorui Zhou, Xiaoqiang Zhu (Alibaba Group)
- **venue:** KDD
- **year:** 2021
- **URL:** https://arxiv.org/abs/2104.14121
- **source type:** industry paper
- **direction:** D7
- **problem setting:** Online display-ad CVR with continuous training on fresh click streams; short waiting window \(w_1\) vs attribution window \(w_2\) creates fake negatives (conversion after ingest labeled negative) and duplicated positives that bias feature distribution \(q(x) \neq p(x)\).
- **objective and label definition:** Post-click binary conversion \(y \in \{0,1\}\); sample types: real negative (\(z > w_2\)), fake negative (\(w_1 < z < w_2\)), positive (\(z < w_1\)); duplicated real negatives and positives re-ingested after attribution window closes.
- **prediction or incrementality:** Predicts absolute CVR \(p(y=1|x)\); importance-sampled loss corrects distribution shift—not incrementality.
- **model architecture:** Redesigned streaming data pipeline duplicating both positives and real negatives; Defer IS loss with CVR head \(f_\theta\) and fake-negative classifier \(f_{dp}\); variants for FNW/FNC with real negatives; offline multi-task heads for \(p(y=1|x)\) and \(p(z < w_n, y=1|x)\) across time windows.
- **credit assignment:** Post-click attribution to clicked impression features \(x\) at click time; last-click 7-day attribution on Taobao-30days.
- **training data and counterfactual handling:** Hourly streaming simulation on second data partition; waiting window \(w_1 = 0.25\) hour; importance weights derived under \(q(x)=p(x)\) after real-negative duplication; fake-negative probability \(p_{dp}(x)\) estimated by auxiliary classifier.
- **offline and online evaluation:** Criteo conversion logs (1.59M samples, 60 days) and Taobao-30days (~120M samples, 30 days, 7-day last-click attribution); AUC, PR-AUC, NLL, relative improvement vs pre-trained and Oracle. Online A/B on Alibaba display ads (Adding To Cart, 1-day window; Purchase, 7-day offline training).
- **reported gains:** Offline DEFER: Criteo AUC 0.8394 (RI-AUC 90.11% vs Oracle), Taobao AUC 0.6483 (RI-AUC 88.00%); beats FNW-RN, ES-DFM, Oracle-close NLL. Online: >6.0% CVR improvement in several scenarios; 8.5% CVR (continuous, Add-to-Cart); 6% CVR and offline AUC 0.8385 vs 0.8347 baseline (Purchase, 7-day).
- **applicability note for a two-sided dating recommender:** Direct pattern for continuous retraining when match/reply labels mature after a short ingest window—duplicating confirmed non-converters restores \(q(x)=p(x)\) and adds certainty beyond scarce positive labels.
  One-sided CPA ads; no reciprocity, retention horizon, or subscription LTV objective.
- **unverified claims:** none

## 1. Summary

DEFER addresses biased continuous CVR training where prior methods duplicate only delayed positives, shifting \(q(x)\) away from \(p(x)\) and relying on scarce positives for label certainty. Ingesting duplicated real negatives (samples that never convert within the attribution window) restores feature-distribution equivalence and supplies additional certain negative signal. Importance sampling with a fake-negative auxiliary model corrects the remaining label shift. Also provides production recipes for short vs long attribution windows and an offline multi-task delay-head alternative.

## 2. Experiment Critique

Strengths: industrial-scale streaming evaluation on Criteo and Taobao; ablations show real negatives consistently help FNW, FNC, ES-DFM; online A/B on production traffic. Weaknesses: attribution windows (1–7 days) shorter than dating retention; waiting window 0.25h is ad-specific; Oracle gap remains on Taobao NLL.

## 3. Industry Contribution

Deployed in Alibaba display advertising; code and data open-sourced (github.com/gusuperstar/defer). Practical guidance for three deployment modes (short window continuous, long window approximated real negatives via \(w_3\), offline multi-task).

## 4. Novelty vs. Prior Work

Extends FNW/FNC (Ktena et al. 2019), FSIW (Yasui et al. 2020), ES-DFM (Yang et al. 2020) by emphasizing real-negative duplication to fix \(q(x) \approx p(x)\) violation. Builds on DFM (Chapelle 2014) delayed-feedback framing.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Criteo conversion logs | labs.criteo.com | Yes | 60 days, timestamps |
| Taobao-30days | Alibaba internal sample | Partial | Authors released via Defer repo |
| Alibaba production | Internal | No | Online A/B |

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

### (1) Ranking objective: retention / LTV / revenue vs CTR
Post-click CVR only; no retention or revenue head.

### (2) Credit assignment: user-level delayed outcome → item-level decision
Click-time features \(x\) receive conversion label after waiting/attribution windows elapse.

### (3) Label and horizon definitions; delay, sparsity, censoring
\(w_1\) waiting vs \(w_2\) attribution; fake/real negative taxonomy; IS correction for censored positives.

### (4) Short vs long-term head fusion
Separate offline multi-task heads per delay window; online single CVR head with IS.

### (5) Prediction vs incrementality
Absolute CVR prediction.

### (6) Offline and online evaluation
Streaming hourly eval plus production A/B CVR lifts reported.

### (7) Reciprocity, congestion, fairness, revenue vs match quality
Not specified in source.

### (8) Migration path from CTR-like model toward unified long-term model
Continuous-training delayed-feedback stack: Vanilla-NoWin → FNW/FNC → +real negatives → Defer IS loss.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Siyu Gu, Xiang-Rong Sheng, Ying Fan, Guorui Zhou, Xiaoqiang Zhu
**Affiliations:** Alibaba Group
**Venue:** KDD 2021
**Year:** 2021
**PDF:** https://arxiv.org/pdf/2104.14121.pdf
**Relevance:** Core
**Priority:** 2
