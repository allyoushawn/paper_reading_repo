# Survey Card

| Field | Value |
|-------|-------|
| **Title** | AITM: Modeling the Sequential Dependence for Audience Multi-step Conversion with Multi-task Learning in the Meituan App |
| **Authors / Company** | Dongbo Xi, Zhen Chen, Peng Yan, Yinger Zhang, Yongchun Zhu, Fuzhen Zhuang, Yu Chen / Meituan |
| **Venue / Year** | KDD 2021 |
| **URL** | https://doi.org/10.1145/3477495.3532030 |
| **Source type** | Industry paper |
| **Direction** | D5 |
| **Problem setting** | Meituan co-branded credit card banner ranking: 4-step sequential funnel (click→application→approval→activation) with extreme class imbalance and T+14 delayed activation feedback |
| **Objective + label + horizon + delay** | Per-step binary conversion labels; end-to-end probability y_t = p(y₁=1,…,y_t=1\|x); activation negatives downsampled to 1% positive ratio in train; activation has delayed feedback (T+14 noted for online deploy constraints) |
| **Prediction or incrementality** | Prediction (multi-task supervised conversion probability per funnel step) |
| **Architecture** | Shared embeddings + per-task towers + Adaptive Information Transfer (AIT) attention module transferring vector representations between adjacent tasks + Behavioral Expectation Calibrator (penalizes ŷ_t > ŷ_{t-1}); L = L_ce + α L_lc |
| **Credit assignment** | Not specified in source for user-level delayed outcomes; per-banner impression labels with sequential funnel constraints |
| **Training / counterfactual** | Standard cross-entropy over all tasks on entire sample space; calibrator enforces monotonic funnel probabilities; no IPS/DR |
| **Offline / online eval** | Offline: AUC (5 runs mean±std) on approval/activation; online A/B on impression→approval and impression→activation conversion rates (2-week tests, tens of millions daily traffic) |
| **Reported gains** | Offline approval AUC 0.8534 vs PLE 0.8518 (+0.0142 vs LightGBM); activation AUC 0.8770 vs PLE 0.8731 (+0.0234). Online vs MLP: +25.0% approval CR, +42.11% activation CR |
| **Dating applicability** | AITM's vector-space transfer between adjacent funnel stages (swipe→like→match→message) beats scalar ESMM multiplication when downstream labels are extremely sparse and sequentially dependent—direct pattern for multi-step dating conversion ranking. |
| **Unverified claims** | None beyond NLM source extraction. |

**Community Reaction:** No significant community discussion found.

---

## 1. Summary

AITM targets multi-step audience conversion (credit card: click, application, approval, activation) where expert-bottom MTL (MMoE/PLE) shares only shallow representations and probability-transfer models (ESMM) lose rich vector information. An Adaptive Information Transfer module uses attention to weight upstream vs. native tower representations between adjacent tasks. A Behavioral Expectation Calibrator enforces ŷ_{t-1} ≥ ŷ_t. Deployed in Meituan app banner ranking with strong offline AUC and online conversion lifts over LightGBM, MLP, ESMM, OMoE, MMoE, and PLE.

## 2. Experiment Critique

Calibrator strength α causes seesaw tradeoffs across tasks. Activation downsampling sensitivity: performance drops sharply if positive ratio too high. Online A/B constrained by business competition and T+14 activation delay—not all baselines deployed. AIT can mislead downstream tasks when upstream predictions are poor (case study). Public Ali-CCP eval (2 tasks only) shows smaller MTL gains on click.

## 3. Industry Contribution

Full-traffic production deployment via TF Serving (<20ms TP999). Bank-specific selector routes different conversion objectives. Demonstrates vector-transfer MTL for 4-step financial funnel at Meituan scale.

## 4. Novelty vs. Prior Work

Bridges expert-bottom MTL (MMoE, PLE, MoSE) and probability-transfer (ESMM, ESM², NMTR) by transferring representations—not just scalars—between sequentially dependent tasks, with funnel monotonicity constraint.

## 5. Dataset Availability

Industrial Meituan credit-card logs (20M train, 3M val, 26M test) not public. Ali-CCP public benchmark used (38M train, click+purchase tasks).

---

## Project Relevance (Q3)

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | Multi-step conversion rates (click, application, approval, activation) for banner ranking; retention, LTV, and revenue not specified as objectives. |
| **(2) Credit assignment** | Not specified in source for mapping user-level delayed outcomes to item-level decisions. |
| **(3) Label / horizon; delay / sparsity / censoring** | Per-step binary labels; activation positives 1% in train (downsampled); activation delayed feedback T+14 noted for online deployment; class imbalance 23.29/1.84/1.30/1.00% positive rates. |
| **(4) Short-term vs long-term head fusion** | **Learned fusion** (AIT attention weights between adjacent task representations); separate per-step heads, not one unified LTV head. |
| **(5) Prediction vs incrementality** | **Prediction** (estimates end-to-end conversion probability per funnel step). |
| **(6) Offline / online eval; delayed retention; two-sided interference** | Offline AUC; online A/B on end-to-end conversion rates. Activation delay (T+14) acknowledged; delayed retention metrics and two-sided interference not specified. |
| **(7) Reciprocity, congestion, fairness, revenue vs match quality** | Not specified in source. |
| **(8) Migration path from CTR-like model to unified long-term model** | Not specified in source. |

---

## Reverse Citation Map

*(blank)*

---

## Meta Information

| Field | Value |
|-------|-------|
| **Date analyzed** | 2026-08-16 |
| **Workplace** | cursor-grok |
| **NLM source ID** | 876bc6f2-0112-448e-8fac-ae78057dc1f0 |
| **Notebook ID** | 67046a44-7490-4fe5-b54a-3f39ef37fdd3 |
