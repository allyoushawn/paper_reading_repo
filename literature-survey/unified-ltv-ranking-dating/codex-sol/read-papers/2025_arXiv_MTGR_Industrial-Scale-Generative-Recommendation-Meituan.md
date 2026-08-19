# Paper Analysis: MTGR: Industrial-Scale Generative Recommendation Framework in Meituan

**Source:** https://arxiv.org/pdf/2505.18654  
**Date analyzed:** 2026-08-18  
**Source ID:** 3e635d25-da77-4583-ab24-87e2f143d0e5  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** notebook_query intentionally not called; source_get_content success

---

## Required Survey Card Fields

- **Title:** MTGR: Industrial-Scale Generative Recommendation Framework in Meituan
- **Authors or company:** Meituan
- **Venue:** arXiv
- **Year:** 2025
- **URL:** https://arxiv.org/pdf/2505.18654
- **Source type:** industry paper
- **Direction:** D9
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1, “Objective” and “Labels.”
- **Prediction or incrementality:** Not specified in source. Indexed evidence does not establish exposure-effect identification; treat the method as prediction or optimization unless validated experimentally.
- **Model architecture:** See §1, “Architecture.”
- **Credit assignment:** See §1, “Credit assignment.”
- **Training data and counterfactual handling:** See §1, “Training evidence,” and prediction/incrementality above.
- **Offline and online evaluation:** See §2.
- **Reported gains:** See §2; no metric is added beyond indexed-source evidence.
- **Applicability to a two-sided dating recommender:** See § Project Relevance.
- **Unverified claims:** Dating transfer statements are explicitly labeled as survey inference.

---

## 1. Summary

### Core problem and contribution — indexed-source evidence

- Scaling law has been extensively validated in many domains such as natural language processing and computer vision.
- In the recommendation system, recent work has adopted generative recommendations to achieve scalability, but their generative approaches require abandoning the carefully constructed cross features of traditional recommendation…
- We found that this approach significantly degrades model performance, and scaling up cannot compensate for it at all.
- In this paper, we propose MTGR (Meituan Generative Recommendation) to address this issue.

### Objective — indexed-source evidence

- In the future, we will explore how to extend MTGR to multi-scenario modeling, similar to large language models, to establish a recommendation foundation model with extensive knowledge.
- Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are…
- This two-part system achieves two primary objectives: (1) facilitating dynamic expansion of capacity by replicating only the key storage instead of the extensive embeddings, and (2) improving…
- The large version, compared to the DLRM baseline optimized over years, demonstrates 65x FLOPs per sample for forward computation and increases the conversion volumes by 1.22% and…

### Labels, horizon, delay, sparsity, and censoring — indexed-source evidence

- In MTGR, candidates are aggregated by user in a specific window for training and by request for inference.
- However, GRM heavily relies on next token prediction to model a complete user behavior sequence, which requires removing cross features between candidates and the 1Cross features measure…
- For example, while the compute stream performs forward and backward passes for batch T, the copy stream simultaneously loads batch T+1, thereby minimizing I/O delay.
- Specifically, to handle the real-time insert/delete of sparse embedding entries, we employ dynamic hash tables to replace static tables.

### Architecture — indexed-source evidence

- MTGR is modeling based on the HSTU [23] architecture and can retain the original deep learning recommendation model (DLRM) features, including cross features.
- Modeling task relationships in multi-task learning with multi-gate mixture-of-experts.
- In the recommendation system, recent work has adopted generative recommendations to achieve scalability, but their generative approaches require abandoning the carefully constructed cross features of traditional recommendation…

### Credit assignment — indexed-source evidence

- Public datasets widely use independent ID and attribute features, where cross features are seldom introduced.

### Training data, baselines, and counterfactual evidence

- We validate the scalability of MTGR on a small-scale dataset.
- MTGR-large has been deployed in the Meituan take-away recommendation system, serving hundreds of millions of users.

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- Both offline and online experimentswere conducted to demonstrate the power-law relationship between the performance of MTGR and computational complexity, and its superiority compared to DLRM.
- MTGR achieved 65x FLOPs for single-sample forward inference compared to the DLRM model, resulting in the largest gain in nearly two years both offline and online.
- The large version, compared to the DLRM baseline optimized over years, demonstrates 65x FLOPs per sample for forward computation and increases the conversion volumes by 1.22% and…
- In offline, we focus on learning of two tasks: CTR and CTCVR (Click-Through Conversion Rate) and use AUC[5] and GAUC (Group AUC) for evaluation.

### Reported gains — indexed-source evidence

- The large version, compared to the DLRM baseline optimized over years, demonstrates 65x FLOPs per sample for forward computation and increases the conversion volumes by 1.22% and…
- However, such a implementation does not bring in significant improvement in MTGR.
- MTGR achieved 65x FLOPs for single-sample forward inference compared to the DLRM model, resulting in the largest gain in nearly two years both offline and online.

### Limitations, failure modes, and negative results — indexed-source evidence

- However, DLRM has two significant drawbacks when it comes to scaling: 1) with exponential growth of user behavior, traditional DLRM cannot efficiently process entire user behaviors, often…

**Statistical validity:** Not specified in source beyond the indexed evidence above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - This breakthrough was successfully deployed on Meituan, the world’s largest food delivery platform, where it has been handling the main traffic.
- Under the requirements of high QPS (Queries Per Second) and low latency in industrial recommendation systems, the scaling of the model is usually limited by both the…
- MTGR: Industrial-Scale Generative Recommendation Framework in Meituan Ruidong Han, Bin Yin, Shangyu Chen, He Jiang, Fei Jiang, Xiang Li, Chi Ma, Mincong Huang, Xiaoguang Li, Chunzhen Jing,…  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - We further optimize the training frameworks, enabling support for our models with 10 to 100 times computational complexity compared to the DLRM, without significant cost increases.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** See §1 source evidence.  
**Prior work comparison:** Not specified in source. Indexed content does not provide a defensible top-5–7 ranking by citation frequency.  
**Verification:** No independent novelty verification was performed in this fallback batch.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Dataset or production logs described by the source | Not specified in source. | Not specified in source. | Indexed evidence is summarized in §1 where available. |

**Offline experiment reproducibility:** Not specified in source.

---

## 6. Community Reaction

Not specified in source.

---

## Project Relevance

**Source-grounded facts:** The evidence snippets above summarize only material present in the indexed source.

**Survey inference:** This source can inform generative candidate/slate optimization, but long-term retention and revenue relevance must be demonstrated rather than assumed. For dating, any transfer must be tested with 7–30 day retention and weeks-long subscription/à-la-carte revenue labels while keeping like, match, and conversation heads as migration auxiliaries.

**Prediction vs. incrementality:** Not specified in source. Indexed evidence does not establish exposure-effect identification; treat the method as prediction or optimization unless validated experimentally.

**Reciprocity and congestion:** Not specified in source unless explicitly shown above. Add candidate-capacity and bilateral-acceptance constraints.

**Cascade and low base rates:** Map the method to impression → like → match → conversation → retention/revenue only as a survey hypothesis; validate calibration and rare-event behavior.

**Success paradox:** Not specified in source. Protect match quality and successful off-platform outcomes so retention/revenue optimization does not penalize successful matching.

**Evaluation implication:** Add bilateral outcome metrics, candidate exposure concentration, delayed-label backtests, and randomized incrementality checks to any source protocol.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** Meituan (individual authors not taken from selected-source metadata)  
**Affiliations:** Meituan  
**Venue:** arXiv  
**Year:** 2025  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 2
