# Paper Analysis: Billion-user Customer Lifetime Value Prediction: An Industrial-scale Solution from Kuaishou

**Source:** https://arxiv.org/pdf/2208.13358  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** Billion-user Customer Lifetime Value Prediction: An Industrial-scale Solution from Kuaishou  
**Authors:** Kunpeng Li; Guangcui Shao; Naijun Yang; Xiao Fang; Yang Song  
**Abstract:** Kuaishou's ODMN jointly predicts 30-, 90-, 180-, and 365-day user revenue with soft monotonic order dependencies. MDME divides the severely imbalanced LTV distribution into easier sub-distributions, with ordinal distillation and bucket-bias regression.  
**Methodology:** Multi-horizon monotonic network, bucket-distribution transitions, calibration loss, divide-and-conquer mixture of experts, and Mutual Gini evaluation.  
**Main results:** On 365-day labels ODMN reduces NRMSE from 1.2163 to 1.1538 and NMAE from 0.6086 to 0.5833 versus the single-horizon baseline; MDME reduces AMBE from 8.3200 to 0.5606 in its ablation. Deployed with daily full-population scoring; exact A/B lift Not specified.

## 2. Experiment Critique

**Design:** Large industrial datasets, ZILN/Two-Stage XGBoost and component baselines, multi-horizon ablations, online use.  
**Statistical validity:** Multiple distribution/ranking/error metrics; exact live test details Not specified.  
**Online experiments:** Effectiveness claimed; numerical A/B result absent.  
**Reproducibility:** Proprietary data/system.  
**Overall:** Excellent label-horizon and imbalance design for revenue prediction, but no item-level ranker or causal impact evidence.

## 3. Industry Contribution

**Deployability:** Fully deployed in Kuaishou user growth with day-level training/cached LTV.  
**Problems solved:** Atypical long tail, sparse high-value users, inconsistent multi-horizon predictions.  
**Engineering cost:** Multi-horizon full-population training, expert buckets, daily cache serving.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Ordered multi-horizon LTV architecture, MDME distribution decomposition, and Mutual Gini.  
**Prior work comparison:** ZILN, Two-Stage XGBoost, ordinal regression, deep LTV.  
**Verification:** Indexed source only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| Kuaishou user-growth LTV | Not specified in source. | No | E-commerce, ads, and other revenue channels. |

**Offline experiment reproducibility:** Not specified.

## 6. Community Reaction

Not specified.

## Survey Card Fields

**Source type:** Industry paper  
**Direction:** D4  
**Problem setting:** Billion-user, multi-channel, multi-horizon revenue prediction.  
**Objective and label definition:** Total user revenue over 30/90/180/365 days; monotonicity across horizons; severe long tail and sparse high-value users. Censoring/maturity sampling Not specified.  
**Prediction or incrementality:** Prediction, not incremental effect.  
**Model architecture:** ODMN multi-horizon monotonic network + MDME bucket experts/distillation.  
**Credit assignment:** User-level LTV; no item/exposure assignment.  
**Training data and counterfactual handling:** Observational user revenue; no counterfactual correction.  
**Offline and online evaluation:** Offline metrics and production deployment; exact A/B lift absent.  
**Reported gains:** ODMN/MDME metric improvements above.  
**Unverified claims:** Live economic lift Not specified.

## Project Relevance

**Source-stated facts:** Supplies concrete 30/90/180/365-day revenue labels, cross-horizon consistency, and production scaling for multiple revenue channels.

**Survey inference:** The dating team can adapt 30-day and longer subscription/a-la-carte heads, perhaps adding 7-day retention. It still needs exposure-level attribution, incremental learning, reciprocal actions, candidate congestion, interference-aware evaluation, and a match-quality/positive-churn objective.

**Applicability note:** Strong production template for multi-horizon revenue labels and skew handling.  
It is a user-value model, not yet the unified candidate-profile ranking objective.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## Meta Information

**Authors:** Kunpeng Li; Guangcui Shao; Naijun Yang; Xiao Fang; Yang Song  
**Affiliations:** Kuaishou Technology  
**Venue:** CIKM  
**Year:** 2022  
**PDF:** Available  
**Relevance:** Core  
**Priority:** 1
