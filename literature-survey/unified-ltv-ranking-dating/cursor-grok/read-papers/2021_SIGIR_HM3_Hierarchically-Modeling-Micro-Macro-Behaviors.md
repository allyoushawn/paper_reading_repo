# Survey Card

| Field | Value |
|-------|-------|
| **Title** | HM³: Hierarchically Modeling Micro and Macro Behaviors for Conversion Rate Prediction |
| **Authors / Company** | Zulong Chen, et al. / Alibaba |
| **Venue / Year** | SIGIR 2021 |
| **URL** | https://doi.org/10.1145/3404835.3462973 |
| **Source type** | Industry paper |
| **Direction** | D5 |
| **Problem setting** | Alibaba Shopping Recommendation CVR: extend ESM² behavior graph by hierarchically inserting micro behaviors (D-Mi/O-Mi) before macro behaviors (D-Ma/O-Ma) between click and purchase; purchases <0.1% of impressions |
| **Objective + label + horizon + delay** | Four entire-space auxiliary targets (CTR, D-Mi, D-Ma, CTCVR) plus derived pCVR from six conditional sub-path probabilities; per-impression binary labels on graph nodes; SR logs 2020-09-16 to 09-30 |
| **Prediction or incrementality** | Prediction (supervised multi-task probability decomposition on behavior graph) |
| **Architecture** | Shared Feature Embedding Module + six parallel DNN sub-networks (y₁…y₆) + formula-free composition of four auxiliary targets and CVR via conditional probability on hierarchical graph |
| **Credit assignment** | Not specified in source for user-level delayed outcomes; per-impression labels on micro/macro/purchase nodes |
| **Training / counterfactual** | Joint four cross-entropy losses over entire impression space; shared FEM receives gradients from all tasks; no explicit debiasing |
| **Offline / online eval** | Offline: CVR and CTCVR AUC on SR-S/M/L datasets; online A/B (2020-10-08–10-21) on CVR and GMV vs BASE |
| **Reported gains** | SR-L CVR AUC: HM³ 0.84891 vs BASE 0.84703 (+0.00188); vs ESMM +0.00166. Online: +8.27% CVR, +8.32% GMV vs BASE (vs ESMM +2.76% CVR, ESM² +4.84%) |
| **Dating applicability** | Hierarchical micro→macro funnel (profile component clicks → super-like/message → match) densifies supervision for sparse terminal outcomes—extends ESM² decomposition to finer-grained dating engagement signals before match/subscribe. |
| **Unverified claims** | None beyond NLM source extraction. |

**Community Reaction:** No significant community discussion found.

---

## 1. Summary

HM³ constructs a complete sequential behavior graph with D-Mi (picture clicks, Q&A, chat, comments, cart button) and D-Ma (cart/wishlist) nodes hierarchically between click and purchase, plus O-Mi/O-Ma catch-alls. Six parallel heads predict sub-path probabilities composed into CTR, D-Mi, D-Ma, and CTCVR targets over entire impression space. Shared embedding module keeps model lightweight. Evaluated on Alibaba SR datasets (up to 31.7B impressions, 32M purchases) and online A/B with largest CVR/GMV gains among baselines.

## 2. Experiment Critique

No public benchmark with micro+macro labels (authors note gap). Micro-behavior taxonomy is Alibaba-specific. HM³-R ablation shows hierarchy order matters but gains are incremental offline (0.001–0.002 AUC). Future work: finer-grained post-click modeling.

## 3. Industry Contribution

Two-week online A/B on production SR module with 8%+ CVR/GMV lift. Low-latency deployment (shared FEM, formula-free target combination). Completes ESMM→ESM²→HM³ Alibaba funnel-modeling lineage.

## 4. Novelty vs. Prior Work

Unifies ESM² macro decomposition and GMCM micro-behavior modeling in one hierarchical graph vs. parallel ESM²+Mi baseline. Extends ESMM/ESM² entire-space MTL with six-head architecture.

## 5. Dataset Availability

Alibaba SR internal logs only (SR-S/M/L); no public release. Authors state no large-scale public micro+macro behavior dataset available.

---

## Project Relevance (Q3)

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | CVR, CTCVR, and auxiliary CTR/D-Mi/D-Ma targets for shopping recommendation ranking; retention, LTV, and revenue not specified (GMV reported in online A/B). |
| **(2) Credit assignment** | Not specified in source for mapping user-level delayed outcomes to item-level decisions. |
| **(3) Label / horizon; delay / sparsity / censoring** | Per-impression binary labels on micro, macro, click, purchase nodes; purchase <0.1% of impressions; delay and censoring not specified. |
| **(4) Short-term vs long-term head fusion** | **Fixed** (conditional-probability composition of six sub-path heads into CVR/CTCVR; no learned fusion or separate long-term head). |
| **(5) Prediction vs incrementality** | **Prediction** (estimates conversion probabilities along hierarchical behavior graph). |
| **(6) Offline / online eval; delayed retention; two-sided interference** | Offline CVR/CTCVR AUC; online A/B on CVR and GMV. Delayed retention and two-sided interference not specified. |
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
| **NLM source ID** | ad032348-2b1f-4018-8ed5-15768681767b |
| **Notebook ID** | 67046a44-7490-4fe5-b54a-3f39ef37fdd3 |
