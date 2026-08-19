# Survey Card

| Field | Value |
|-------|-------|
| **Title** | Entire Space Multi-Task Model: An Effective Approach for Estimating Post-Click Conversion Rate |
| **Authors / Company** | Xiao Ma, Liqin Zhao, Guan Huang, Zhi Wang, Zelin Hu, Xiaoqiang Zhu, Kun Gai / Alibaba |
| **Venue / Year** | SIGIR 2018 |
| **URL** | https://doi.org/10.1145/3209978.3210024 |
| **Source type** | Industry paper |
| **Direction** | D5 |
| **Problem setting** | Post-click CVR estimation for Taobao recommender ranking: train on sequential impression→click→conversion logs but deploy pCVR over all impressions |
| **Objective + label + horizon + delay** | pCTR (click label y on all impressions), pCTCVR (joint y∧z label on all impressions), pCVR derived as intermediate; per-impression binary labels from traffic logs; temporal split (first half train, second half test); delay not specified |
| **Prediction or incrementality** | Prediction (supervised probability estimation of conversion conditional on click) |
| **Architecture** | Two shared-embedding Embedding&MLP towers (CTR, CVR) with element-wise multiplication for pCTCVR = pCTR × pCVR; joint loss on CTR + CTCVR over entire impression space |
| **Credit assignment** | Not specified in source for mapping user-level delayed outcomes to item-level decisions; per-impression pointwise labels only |
| **Training / counterfactual** | Entire-space multi-task training on all impressions; shared embedding transfer from CTR to CVR; no explicit IPS/DR debiasing |
| **Offline / online eval** | Offline: AUC on CVR task (clicked impressions) and CTCVR task (all impressions), 10-run mean±std; no online A/B reported in source |
| **Reported gains** | Public dataset: CVR AUC 68.56% vs BASE 66.00% (+2.56 abs); CTCVR AUC 65.32% vs 62.07% (+3.25 abs). Product dataset (100%): +2.18% CVR AUC, +2.32% CTCVR AUC vs production baseline |
| **Dating applicability** | Canonical template for modeling sparse downstream outcomes (match/subscribe) as a sequential funnel atop CTR-like engagement, training over the full impression space to avoid selection bias. Shared embeddings let abundant swipe/like signals supervise sparse conversion heads—directly relevant to dating CVR/LTV ranking stacks. |
| **Unverified claims** | None beyond NLM source extraction. |

**Community Reaction:** No significant community discussion found.

---

## 1. Summary

ESMM reframes post-click CVR as a multi-task problem over the sequential pattern impression→click→conversion. Instead of training CVR only on clicked impressions (causing sample selection bias and data sparsity), it co-trains CTR and CTCVR over all impressions and derives pCVR via the identity pCTCVR = pCTR × pCVR. Shared embeddings let the sparse CVR tower learn from unclicked impressions. Evaluated on Taobao public (84M impressions) and product (8.95B impressions) datasets with strong AUC gains over BASE, AMAN, OVERSAMPLING, UNBIAS, DIVISION, and ESMM-NS.

## 2. Experiment Critique

Evaluation is offline AUC only—no production A/B in the paper. CVR AUC is still measured on clicked impressions, which partially sidesteps the deployment mismatch the paper motivates. Authors omit backbone architecture search due to space. Baseline heuristics (AMAN, OVERSAMPLING) are sensitive to sampling rates; ESMM itself has no reported failure modes.

## 3. Industry Contribution

First public dataset with sequential click+conversion labels (Taobao 1% sample). Deployed pattern at Alibaba scale; authors note 0.1% AUC gain is highly significant in industrial RS. Released dataset enables reproducible CVR research.

## 4. Novelty vs. Prior Work

Extends conventional click-space CVR (BASE) and debiasing heuristics (AMAN, UNBIAS, DIVISION) by jointly modeling CTR+CTCVR over entire space with multiplication-form probability decomposition, avoiding division instability. Builds on Wide&Deep/DIN-style Embedding&MLP and multi-task learning (Ruder).

## 5. Dataset Availability

Public: Alibaba Taobao 1% sample (38GB uncompressed, 84M impressions, 3.4M clicks, 18k conversions) at https://tianchi.aliyun.com/datalab/dataSet.html?dataId=408. Full product dataset not released.

---

## Project Relevance (Q3)

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | CTR (pCTR) and CVR/CTCVR proxies for ranking and OCPC bidding; retention, LTV, and revenue not specified as ranking objectives. |
| **(2) Credit assignment** | Not specified in source for mapping user-level delayed outcomes to item-level decisions. |
| **(3) Label / horizon; delay / sparsity / censoring** | Per-impression binary click (y) and conversion (z) labels with sequential dependence y→z; CVR training data ~4% of CTR volume; delay, censoring, and horizon not specified. |
| **(4) Short-term vs long-term head fusion** | **Fixed** (deterministic multiplication pCTCVR = pCTR × pCVR; no separate long-term head). |
| **(5) Prediction vs incrementality** | **Prediction** (estimates p(conversion\|click, impression)). |
| **(6) Offline / online eval; delayed retention; two-sided interference** | Offline AUC on CVR and CTCVR tasks; online A/B and delayed retention not specified. Two-sided interference not specified. |
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
| **NLM source ID** | f9d15f60-f3ba-4949-bab1-c1ce17615a03 |
| **Notebook ID** | 67046a44-7490-4fe5-b54a-3f39ef37fdd3 |
