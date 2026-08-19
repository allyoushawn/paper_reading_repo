# Paper Analysis: Entire Space Multi-Task Model

**Source:** https://doi.org/10.1145/3209978.3210104  
**Source ID:** f9d15f60-f3ba-4949-bab1-c1ce17615a03  
**Date analyzed:** 2026-08-18  
**Model identifier:** codex-sol  
**Evidence mode:** NotebookLM indexed-content fallback after source-scoped query plateau.

---

## 1. Summary

**Authors:** Xiao Ma; Liqin Zhao; Guan Huang; Zhi Wang; Zelin Hu; Xiaoqiang Zhu; Kun Gai  
**Abstract:** ESMM trains CTR and click-through-and-conversion (CTCVR) tasks on all impressions and derives post-click CVR through the probability identity CTCVR=CTR×CVR. Shared embeddings transfer dense click supervision to the sparse conversion task.

**Main results:** On the public Taobao sample, ten-run CVR/CTCVR AUC was 68.56±0.37/65.32±0.49, versus 66.00±0.37/62.07±0.45 for base and 68.25±0.44/64.44±0.62 without shared embeddings. The full source covers 8.9B samples.

---

## 2. Experiment Critique

**Design:** Time-ordered half-train/half-test split, public and product data, several sampling/debiasing baselines, and a no-sharing ablation.

**Statistical validity:** Ten repeated public runs with mean±SD are a strength. Product results and online business effects are not detailed in extracted content.

**Online experiments:** Not specified.

**Reproducibility:** A 1% 38GB public sample with sequential labels was released and model hyperparameters are reported.

**Overall:** Foundational and practical for sparse funnel modeling, but later work shows ESMM is not theoretically unbiased for MNAR conversion labels.

---

## 3. Industry Contribution

**Deployability:** Simple probability heads and shared embeddings fit standard rankers.

**Problems solved:** Click-space versus impression-space mismatch and sparse conversions.

**Engineering cost:** Low-to-moderate; requires consistent sequential labels and numerical care around probability products.

**Project relevance:** Core architecture for like→match→conversation→subscription auxiliary tasks and an impression-space final outcome.

**Most important mismatch:** The probability-product chain does not model reciprocal outcomes, causal incrementality, congestion, delayed censoring, success exits, or heterogeneous revenue. It is a predictive funnel, not a direct unified LTV optimizer.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Entire-space CVR modeling via jointly trained CTR/CTCVR tasks and representation transfer.

**Prior work comparison:** Replaces clicked-only CVR, oversampling, and all-missing-negative heuristics with a sequential probability identity.

**Verification:** Source-grounded only.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Ali-CCP / public Taobao sample | Paper dataset link | Yes | 1% sample, about 38GB. |
| Full product dataset | Not specified | No | 8.9B samples. |

**Offline experiment reproducibility:** Public-data reproduction is feasible; exact product results are not.

---

## 6. Community Reaction

No significant community discussion was assessed in this fallback batch.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|---|---|---|
| [2020_SIGIR_ESM2_Post-Click-Behavior-Decomposition.md](./2020_SIGIR_ESM2_Post-Click-Behavior-Decomposition.md) | Introduction / Summary | Explicitly mentions ESMM in baseline or comparison context. |
| [2020_WWW_MultiDR_Causal-Debiasing-Post-Click-CVR.md](./2020_WWW_MultiDR_Causal-Debiasing-Post-Click-CVR.md) | Introduction / Summary | Explicitly mentions ESMM in baseline or comparison context. |
| [2021_AAAI_ESDF_Delayed-Feedback-Entire-Space-CVR.md](./2021_AAAI_ESDF_Delayed-Feedback-Entire-Space-CVR.md) | Introduction / Summary | Explicitly mentions ESMM in baseline or comparison context. |
| [2021_KDD_AITM_Sequential-Multi-Step-Conversions.md](./2021_KDD_AITM_Sequential-Multi-Step-Conversions.md) | Experiments | Explicitly mentions ESMM in baseline or comparison context. |
| [2021_SIGIR_HM3_Hierarchical-Micro-Macro-Behaviors.md](./2021_SIGIR_HM3_Hierarchical-Micro-Macro-Behaviors.md) | Introduction / Summary | Explicitly mentions ESMM in baseline or comparison context. |
| [2022_SIGIR_ESCM2_Entire-Space-Counterfactual-Multi-Task-Model.md](./2022_SIGIR_ESCM2_Entire-Space-Counterfactual-Multi-Task-Model.md) | Introduction / Summary | Explicitly mentions ESMM in baseline or comparison context. |
| [2026_arXiv_PDQ_Long-Term-Value-Prediction-Video-Ranking.md](./2026_arXiv_PDQ_Long-Term-Value-Prediction-Video-Ranking.md) | Related Work | Explicitly mentions full title in baseline or comparison context. |

---

## Meta Information

**Venue:** SIGIR  
**Year:** 2018  
**PDF:** Indexed via DOI  
**Relevance:** Core  
**Priority:** 1  
**Direction:** D5 — multi-stage / multi-task conversion chains
