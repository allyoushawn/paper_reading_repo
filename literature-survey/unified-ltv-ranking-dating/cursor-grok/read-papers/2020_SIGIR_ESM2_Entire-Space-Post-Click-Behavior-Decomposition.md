# Survey Card

| Field | Value |
|-------|-------|
| **Title** | Entire Space Multi-Task Modeling via Post-Click Behavior Decomposition for Conversion Rate Prediction |
| **Authors / Company** | Quan Lin, Keping Yang, et al. / Alibaba |
| **Venue / Year** | SIGIR 2020 |
| **URL** | https://doi.org/10.1145/3397271.3401064 |
| **Source type** | Industry paper |
| **Direction** | D5 |
| **Problem setting** | E-commerce CVR ranking: extend impression→click→purchase path by decomposing post-click behaviors (DAction/OAction) to address SSB and extreme purchase sparsity (<0.1% impressions) |
| **Objective + label + horizon + delay** | Auxiliary targets CTR, CTAVR (impression→DAction), CTCVR over entire impression space; CVR derived from decomposed sub-paths; per-impression binary labels from user logs; delay not specified |
| **Prediction or incrementality** | Prediction (supervised multi-task probability estimation) |
| **Architecture** | Shared Embedding Module + four parallel MLP heads (y₁…y₄) + parameter-free Sequential Composition Module composing pCTR, pCTAVR, pCVR, pCTCVR via conditional probability on behavior graph |
| **Credit assignment** | Not specified in source for user-level delayed outcomes; per-impression labels on decomposed funnel steps |
| **Training / counterfactual** | Joint logloss over entire impression space (w_ctr=w_ctavr=w_ctcvr=1.0); shared embeddings; no explicit counterfactual correction |
| **Offline / online eval** | Offline: AUC, GAUC, F1 at top-k thresholds; online A/B vs GBDT on industrial RS (millions of users, <20ms latency) |
| **Reported gains** | Offline: CVR AUC 0.8486 vs ESMM 0.8398 (+0.0088); CTCVR AUC 0.8371 vs 0.8270 (+0.0101); CTCVR GAUC 0.8051 vs 0.7906 (+0.0145). Online: +3% CVR vs ESMM |
| **Dating applicability** | Decomposing the sparse terminal outcome (purchase/match) into denser intermediate engagement signals (cart/wish → profile view/message) is directly transferable to dating funnels where match/subscribe labels are rare but mid-funnel actions are abundant. |
| **Unverified claims** | None beyond NLM source extraction. |

**Community Reaction:** No significant community discussion found.

---

## 1. Summary

ESM² inserts parallel Deterministic Action (cart/wish) and Other Action nodes between click and purchase, forming graph impression→click→D(O)Action→purchase. Four hidden probabilities are predicted in parallel over all impressions, then composed via conditional probability rules into CTR, CTAVR, CVR, and CTCVR. Abundant post-click supervision mitigates data sparsity while entire-space training addresses selection bias. Tested on 326M-impression Alibaba logs with offline and online A/B gains over GBDT, DNN, DNN-OS, and ESMM.

## 2. Experiment Critique

DAction definition (SCart+Wish) is platform-specific; generalization to other behavior taxonomies unclear. Online eval compares to GBDT baseline only in figure; ESMM is intermediate. Authors note 0.01 AUC ≈ significant revenue but do not report confidence intervals on online lift. No delayed-label or attribution analysis.

## 3. Industry Contribution

Deployed on Alibaba e-commerce RS at 100M+ users/sec peak with <20ms inference. Promises source code and dataset release. Demonstrates post-click decomposition as production-viable extension of ESMM.

## 4. Novelty vs. Prior Work

Extends ESMM (entire-space probability transfer) by decomposing post-click macro behaviors into intermediate supervised nodes, vs. ESMM's direct impression→click→purchase path. Contrasts with GBDT/DNN click-space training and oversampling (DNN-OS).

## 5. Dataset Availability

Industrial offline dataset (326M impressions, 226k purchases, 2.5M DActions) described; authors state no public entire-space dataset existed and intend release. Public availability at time of writing not confirmed in source.

---

## Project Relevance (Q3)

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | CTR, CVR, CTAVR, CTCVR proxies for e-commerce ranking; retention, LTV, and revenue not specified as objectives. |
| **(2) Credit assignment** | Not specified in source for mapping user-level delayed outcomes to item-level decisions. |
| **(3) Label / horizon; delay / sparsity / censoring** | Per-impression binary labels on funnel steps; purchase <0.1% of impressions; oversampling for DNN-OS baseline; delay and censoring not specified. |
| **(4) Short-term vs long-term head fusion** | **Fixed** (conditional-probability composition of parallel sub-target heads into CVR/CTCVR; no learned fusion across short/long horizons). |
| **(5) Prediction vs incrementality** | **Prediction** (estimates conversion probabilities along decomposed paths). |
| **(6) Offline / online eval; delayed retention; two-sided interference** | Offline AUC/GAUC/F1; online A/B on CVR. Delayed retention and two-sided interference not specified. |
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
| **NLM source ID** | e253a958-bfba-4cf7-aaf8-fb74b5fc6a14 |
| **Notebook ID** | 67046a44-7490-4fe5-b54a-3f39ef37fdd3 |
