# Paper Analysis: Entire Space Multi-Task Modeling via Post-Click Behavior Decomposition

**Source:** https://doi.org/10.1145/3397271.3401443  
**Source ID:** e253a958-bfba-4cf7-aaf8-fb74b5fc6a14  
**Date analyzed:** 2026-08-18  
**Model identifier:** codex-sol  
**Evidence mode:** NotebookLM indexed-content fallback after source-scoped query plateau.

---

## 1. Summary

**Abstract:** ESM2 decomposes click→purchase into parallel deterministic actions (cart/wishlist) and other actions, then composes hidden conditional probabilities into CVR. Entire-impression training reduces sample-selection bias, while abundant post-click labels reduce purchase sparsity.

**Methodology:** A shared multi-task DNN predicts CTR, action-path, and purchase subtargets dictated by the graph impression→click→D(O)Action→purchase.

**Main results:** On 326.3M impressions, ESM2 achieved CVR AUC 0.8486, CTCVR AUC 0.8371, and CTCVR GAUC 0.8051—gains of 0.0088/0.0101/0.0145 over ESMM. Production tests with millions of users reported about +3% CVR over ESMM and sub-20-ms response.

---

## 2. Experiment Critique

**Design:** Strong baselines (GBDT, DNN, oversampled DNN, ESMM), AUC/GAUC/F1 metrics, behavior-decomposition ablations, hyperparameter studies, and a production A/B test.

**Statistical validity:** Large data volume supports precision, but exact online intervals, p-values, test duration, randomization, and offline repeated-run variance are absent from extracted content.

**Online experiments:** Yes, same-sized user groups; only CVR lift is reported in text.

**Reproducibility:** Architecture and hyperparameters are given. The source says code/data would be released, but availability was not independently verified in this batch.

**Overall:** Strong predictive and online evidence for intermediate-action supervision; still optimizes purchase probability rather than long-term value.

---

## 3. Industry Contribution

**Deployability:** Demonstrated at hundreds-of-millions-user scale.

**Problems solved:** Entire-space selection bias and rare terminal conversion labels.

**Engineering cost:** Requires reliable post-click taxonomy and several coupled probability heads.

**Project relevance:** Core. Cart/wishlist analogues in dating are like, mutual match, message, and date-intent signals; ESM2 shows how abundant intermediate labels can support a sparse terminal subscription or retention target.

**Most important mismatch:** Its graph assumes one-sided conditional paths and a purchase endpoint. It lacks reciprocal eligibility, congestion/exposure effects, delayed label correction, causal incrementality, success-paradox censoring, and joint subscription/à-la-carte value.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Post-click behavior decomposition inside entire-space multi-task CVR modeling.

**Prior work comparison:** Extends ESMM by adding abundant deterministic intermediate actions instead of relying only on click and purchase.

**Verification:** Source-grounded only.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Industrial e-commerce sequence logs | Not specified | No/unclear | 13.38M users, 10.40M items, 326.3M impressions. |

**Offline experiment reproducibility:** Exact reproduction depends on the promised release; not independently verified here.

---

## 6. Community Reaction

No significant community discussion was assessed in this fallback batch.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|---|---|---|
| [2021_AAAI_ESDF_Delayed-Feedback-Entire-Space-CVR.md](./2021_AAAI_ESDF_Delayed-Feedback-Entire-Space-CVR.md) | Related Work | Explicitly mentions ESM2 in baseline or comparison context. |
| [2021_SIGIR_HM3_Hierarchical-Micro-Macro-Behaviors.md](./2021_SIGIR_HM3_Hierarchical-Micro-Macro-Behaviors.md) | Introduction / Summary | Explicitly mentions ESM2 in baseline or comparison context. |

---

## Meta Information

**Authors:** Hong Wen; Jing Zhang; Yuan Wang; Fuyu Lv; Wentian Bao; Quan Lin; Keping Yang  
**Venue:** SIGIR  
**Year:** 2020  
**PDF:** Indexed via DOI  
**Relevance:** Core  
**Priority:** 1  
**Direction:** D5 — multi-stage / multi-task conversion chains
