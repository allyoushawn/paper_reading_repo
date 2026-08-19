# Survey Card

| Field | Value |
|-------|-------|
| **Title** | ESCM²: Entire Space Counterfactual Multi-Task Model for Post-Click Conversion Rate Estimation |
| **Authors / Company** | Hao Wang, Tai-Wei Chang, Tianqiao Liu, Jianmin Huang, Zhichao Chen, Chao Yu, Ruopeng Li, et al. / Ant Group |
| **Venue / Year** | SIGIR 2022 |
| **URL** | https://doi.org/10.1145/3534678.3539382 |
| **Source type** | Industry paper |
| **Direction** | D5 |
| **Problem setting** | Post-click CVR at Ant Group: ESMM addresses SSB/DS via entire-space MTL but suffers Inherent Estimation Bias (IEB, systematic CVR overestimation) and Potential Independence Priority (PIP, CTR⊥CVR in CTCVR) |
| **Objective + label + horizon + delay** | CTR, CVR (counterfactual-regularized), CTCVR over exposure space; binary click/conversion labels; 90-day industrial logs + Ali-CCP; chronological train/val/test split |
| **Prediction or incrementality** | Prediction with counterfactual risk minimization (IPS/DR regularizers debias CVR estimation toward causal estimand) |
| **Architecture** | MMoE shared backbone + CTR/CVR/imputation towers; ESCM²-IPS or ESCM²-DR counterfactual CVR loss weighted by propensity (CTR tower output, clipped at 0.1); L = L_CTR + λ_c L_CVR + λ_g L_CTCVR |
| **Credit assignment** | Not specified in source for user-level delayed outcomes; per (user,item) exposure labels with IPS/DR reweighting from click propensity |
| **Training / counterfactual** | IPS inversely weights CVR error by propensity; DR adds imputation tower for error deviation; gradient from L_CVR to CTR truncated; λ_c tuned small (0.1–1), λ_g=1 |
| **Offline / online eval** | Offline: AUC, KS, Recall, F1; online A/B in Ant Insurance/Wufu campaigns (order quantity, premium, UV-CVR, UV-CTCVR) |
| **Reported gains** | CVR AUC industrial: ESCM²-IPS 0.7730 vs ESMM 0.7547; CTCVR AUC: ESCM²-DR 0.8265 vs ESMM 0.8153. Online: +2.84% orders, +10.85% premium, +5.64% UV-CVR vs ESMM (scenario 1) |
| **Dating applicability** | When ESMM-style funnel models overestimate sparse downstream rates (match/subscribe), IPS/DR counterfactual regularization offers a principled debiasing layer atop shared-embedding MTL—relevant if dating stacks inherit ESMM bias on reciprocal conversion heads. |
| **Unverified claims** | None beyond NLM source extraction. |

**Community Reaction:** No significant community discussion found.

---

## 1. Summary

ESCM² theoretically proves ESMM's CVR estimates are biased high (IEB) and that CTCVR can treat CTR and CVR as conditionally independent (PIP). It adds IPS or DR counterfactual regularizers to ESMM's multi-task objective, directly debiasing CVR over click space while retaining entire-space CTR/CTCVR training. MMoE backbone; propensity from CTR tower with clipping and gradient truncation. Validated on Ant industrial data (61.58M train) and Ali-CCP with offline AUC gains and online business lifts in insurance marketing.

## 2. Experiment Critique

IPS variance and propensity accuracy remain fragile—authors clip scores and limit λ_c. Large λ_c hurts CTCVR. Biased estimators (Naïve, MTL-IMP) competitive with ESMM on CVR AUC in MTL setting. Online daily metrics volatile (e.g., premium −12.49% day 4). Future work notes propensity fragility and need for adversarial/representation alternatives.

## 3. Industry Contribution

Production deployment at Ant Group across insurance campaigns (5.6M+ UV). First rigorous proof of ESMM CVR bias with causal regularization fix. Demonstrates counterfactual debiasing compatible with industrial MTL stacks.

## 4. Novelty vs. Prior Work

Extends ESMM/ESM² probability-decomposition line with causal IPS/DR regularizers vs. MTL-EIB, MTL-IPS, MTL-DR baselines. Builds on Schnabel et al. IPS, doubly robust estimators, and Zhang et al. MTL debiasing.

## 5. Dataset Availability

Industrial 90-day Ant logs (downsampled 100:10:1 exposure:click:conversion on train). Public Ali-CCP benchmark used for reproducibility.

---

## Project Relevance (Q3)

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | CTR, CVR, CTCVR for recommender ranking; retention, LTV, and revenue not specified as ranking objectives. |
| **(2) Credit assignment** | Not specified in source for mapping user-level delayed outcomes to item-level decisions. |
| **(3) Label / horizon; delay / sparsity / censoring** | Binary click/conversion labels per exposure; CTR ~3.8–4% on datasets; negative downsampling on industrial train; delay/censoring not specified. |
| **(4) Short-term vs long-term head fusion** | **Fixed** (ESMM-style multiplicative decomposition with added counterfactual CVR regularizer; no separate long-term head). |
| **(5) Prediction vs incrementality** | **Prediction** with counterfactual debiasing (IPS/DR align click-space CVR error to exposure-space distribution). |
| **(6) Offline / online eval; delayed retention; two-sided interference** | Offline AUC/KS/F1; online A/B on orders, premium, UV-CVR, UV-CTCVR. Delayed retention and two-sided interference not specified. |
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
| **NLM source ID** | 43084729-4a01-433c-b6bc-c5316c19ea31 |
| **Notebook ID** | 67046a44-7490-4fe5-b54a-3f39ef37fdd3 |
