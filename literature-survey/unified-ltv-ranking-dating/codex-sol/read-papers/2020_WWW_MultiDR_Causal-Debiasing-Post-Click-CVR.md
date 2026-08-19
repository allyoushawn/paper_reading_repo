# Paper Analysis: Large-scale Causal Approaches to Debiasing Post-click Conversion Rate Estimation

**Source:** https://doi.org/10.1145/3366423.3380037  
**Source ID:** 311e06b5-24ae-4a29-93fa-887ce0868211  
**Date analyzed:** 2026-08-18  
**Model identifier:** codex-sol  
**Evidence mode:** NotebookLM indexed-content fallback after source-scoped query plateau.

---

## 1. Summary

**Authors:** Wenhao Zhang; Wentian Bao; Xiao-Yang Liu; Keping Yang; Quan Lin; Hong Wen; Ramin Ramezani  
**Abstract:** Multi-IPW and Multi-DR treat click-conditioned CVR labels as missing-not-at-random. A shared CTR/CVR architecture estimates observation propensities; inverse-propensity or doubly robust losses correct selection while multi-task sharing reduces sparsity.

**Methodology:** The paper proves ESMM is not generally unbiased, derives IPW and doubly robust estimators, and shares representations with an abundant CTR task.

**Main results:** On the 11.5B-example production set, Multi-DR reached CTR AUC 82.72, CTCVR AUC 77.23, and CTCVR GAUC 62.28 versus ESMM 82.17/76.55/61.76. On Ali-CCP, ten-run mean CVR/CTCVR AUC was 69.29±0.31/65.43±0.34.

---

## 2. Experiment Critique

**Design:** Public Ali-CCP plus four nested production windows, noncausal and causal baselines, repeated public runs, and efficiency comparisons.

**Statistical validity:** Ten-run mean±SD is reported publicly. The production table lacks uncertainty; CTCVR is a proxy because an unbiased randomized click-to-conversion test cannot be generated.

**Online experiments:** None specified; evaluation is offline on logged traffic.

**Reproducibility:** Ali-CCP is linked and architecture/hyperparameters are reported. Production logs and exact propensities are proprietary; code availability is not specified.

**Overall:** Good evidence for MNAR correction, but unbiasedness depends on propensity/imputation assumptions and proxy evaluation rather than a causal online test.

---

## 3. Industry Contribution

**Deployability:** Designed for billion-scale distributed training with parameter sharing and comparable training cost.

**Problems solved:** Click-conditioned selection bias, label missingness, and rare conversion data.

**Engineering cost:** High-quality propensity logging/estimation and numerical stabilization are required.

**Project relevance:** Core for prediction-versus-incrementality and cascade selection. Dating outcomes are observed only after ranking, likes, and mutual actions; doubly robust entire-space learning is a strong candidate for correcting this observational gate.

**Most important mismatch:** Missingness correction is not treatment-effect estimation: it predicts counterfactual labels under selection assumptions but does not identify incremental retention/revenue from an impression. Reciprocal interference, congestion, delayed outcomes, and success exit violate simple user-item independence.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First combination of IPW/DR CVR estimation with industrial multi-task learning, plus a proof/counterexample that ESMM is biased.

**Prior work comparison:** Extends recommender IPW and doubly robust rating methods to the exposure→click→conversion funnel.

**Verification:** Source-grounded only.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Ali-CCP | https://tianchi.aliyun.com/dataset/dataDetail?dataId=408 | Yes | Public click/conversion benchmark. |
| Mobile Taobao production sets | Not specified | No | Up to 11.5B exposures, 109 features. |

**Offline experiment reproducibility:** Public benchmark is reproducible in principle; production results are not.

---

## 6. Community Reaction

No significant community discussion was assessed in this fallback batch.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Venue:** The Web Conference (WWW)  
**Year:** 2020  
**PDF:** Indexed via DOI  
**Relevance:** Core  
**Priority:** 1  
**Direction:** D5 — multi-stage / multi-task conversion chains
