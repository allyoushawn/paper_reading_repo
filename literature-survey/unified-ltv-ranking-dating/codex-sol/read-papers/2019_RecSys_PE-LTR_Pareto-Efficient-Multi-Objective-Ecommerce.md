# Paper Analysis: A Pareto-Eficient Algorithm for Multiple Objective Optimization in E-Commerce Recommendation

**Source:** https://doi.org/10.1145/3298689.3346998  
**Date analyzed:** 2026-08-18  
**Source ID:** 670273a1-bfae-4b62-94a7-dac93de83f9d  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** Q1/Q2/Q3 not started after generative-query plateau; source fallback completed

---

## Required Survey Card Fields

- **Title:** A Pareto-Eficient Algorithm for Multiple Objective Optimization in E-Commerce Recommendation
- **Authors or company:** Not specified in selected-source metadata
- **Venue:** RecSys
- **Year:** 2019
- **URL:** https://doi.org/10.1145/3298689.3346998
- **Source type:** industry paper
- **Direction:** D1
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1.
- **Prediction or incrementality:** Not specified in source. The indexed evidence supports outcome/utility prediction or optimization, not exposure-effect identification.
- **Model architecture:** See §1, “Architecture.”
- **Credit assignment:** See §1, “Credit assignment.”
- **Training data and counterfactual handling:** See §1 and the prediction/incrementality field above.
- **Offline and online evaluation:** See §2.
- **Reported gains:** See §2; no metrics are added beyond indexed-source evidence.
- **Applicability to a two-sided dating recommender:** See § Project Relevance.
- **Unverified claims:** All dating transfer statements below are survey inference, not claims made by the source.

---

## 1. Summary

### Core problem and contribution — indexed-source evidence

- A Pareto-Eficient Algorithm for Multiple Objective Optimization in E-Commerce Recommendation Xiao Lin∗ Hongjie Chen, Changhua Pei, Yongfeng Zhang, Wenwu Ou, Alibaba Group Fei Sun,…
- ABSTRACT Recommendation with multiple objectives is an important but diffcult problem, where the coherent difculty lies in the possible conficts between objectives.
- In this case, multi-objective optimiza- tion is expected to be Pareto efcient, where no single objective can be further improved without hurting the others.

### Objective — indexed-source evidence

- For E-Commerce platforms, the primary objective is to improve the GMV, but too much sacrifce of CTR may cause a severe decrease of daily…
- We specifcally apply the proposed framework on E-Commerce recommendation to optimize GMV and CTR simulta- neously.
- A Pareto-Eficient Algorithm for Multiple Objective Optimization in E-Commerce Recommendation Xiao Lin∗ Hongjie Chen, Changhua Pei, Yongfeng Zhang, Wenwu Ou, Alibaba Group Fei Sun,…

### Label definition, horizon, delay, sparsity, and censoring — indexed-source evidence

- To validate this inconsistency, we collect one-week online data from a real-world E-Commerce platform and plot the trends of GMV when CTR .
- To the best of our knowledge, no public dataset includes all three labels and enough features, this dataset can be used for further studies.

### Architecture — indexed-source evidence

- In this case, multi-objective optimiza- tion is expected to be Pareto efcient, where no single objective can be further improved without hurting the others.
- CXR-RL uses reinforcement learning techniques to optimize CXR, thus achieving a trade-of between CTR and CVR.

### Credit assignment — indexed-source evidence

Not specified in source.

### Training data and baselines — indexed-source evidence

- We open-source a large-scale E-Commerce recommendation dataset EC-REC, which contains the real records of impressions, clicks and purchases.
- Due to the huge amount of online data, we collect one-week data and sample over seven million impressions for ofine experiments, and the dataset…
- The condition is equivalent to a constrained optimization problem, and we propose an algorithm that solves the problem in two steps.

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- 2 is negligible and the online experiments have verifed this 4 PARETO FRONTIER GENERATION AND SOLUTION SELECTION Multiple objective optimization can either be used…
- The online and ofine experimental results both indicate that our solution outperforms other baselines signifcantly and the solutions are nearly Pareto efcient.
- A MART model is used to optimize a diferentiable loss for NDCG.

### Reported gains — indexed-source evidence

- In this case, multi-objective optimiza- tion is expected to be Pareto efcient, where no single objective can be further improved without hurting the others.

### Limitations and negative results — indexed-source evidence

- However existing approaches to Pareto efcient multi-objective recommendation still lack good theoretical guarantees.

**Statistical validity:** Not specified in source beyond the evidence snippets above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - We open-source a large-scale E-Commerce recommendation dataset EC-REC, which contains the real records of impressions, clicks and purchases.  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - Assuming that there are K objectives in a given recommender system, a model F (θ ) needs to optimize these objectives simultaneously, where θ…

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** See the source-grounded contribution and architecture evidence in §1.  
**Prior work comparison:** Not specified in source. Raw indexed content does not establish a defensible top-5–7 citation-frequency ranking.  
**Verification:** No independent novelty verification was performed in this fallback batch.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Dataset or production logs described by the source | Not specified in source. | Not specified in source. | Evidence appears in §1 when available. |

**Offline experiment reproducibility:** Not specified in source.

---

## 6. Community Reaction

Not specified in source.

---

## Project Relevance

**Source-grounded facts:** The indexed-source evidence above identifies the paper's objective, architecture, labels, attribution mechanism, and evaluation where available.

**Survey inference:** The paper may inform learned multi-objective fusion, delayed-value auxiliary heads, or staged replacement of the current hand-tuned blend. This transfer is unverified. A dating deployment needs 7–30 day retention and weeks-long revenue labels while preserving like, match, and conversation auxiliaries during migration.

**Prediction vs. incrementality:** Not specified in source. The indexed evidence supports outcome/utility prediction or optimization, not exposure-effect identification.

**Reciprocity and congestion:** Not specified in source unless explicitly present above. Candidate-side capacity and bilateral acceptance require an added reciprocal or marketplace layer.

**Cascade and low base rates:** Mapping the method onto impression → like → match → conversation → retention/revenue is survey inference and requires sparse-label calibration.

**Success paradox:** Not specified in source. A dating system must protect match quality and successful outcomes so retention/revenue optimization does not punish successful matching.

**Evaluation implication:** Where source evidence exists, reproduce its offline/online protocol; add bilateral metrics, candidate exposure concentration, and incrementality validation.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** Not specified in selected-source metadata (individual authors not taken from selected-source metadata)  
**Affiliations:** Not specified in selected-source metadata  
**Venue:** RecSys  
**Year:** 2019  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 1
