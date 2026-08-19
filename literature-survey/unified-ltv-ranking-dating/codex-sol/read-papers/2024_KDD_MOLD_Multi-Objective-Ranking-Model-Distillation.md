# Paper Analysis: Multi-objective Learning to Rank by Model Distillation

**Source:** https://doi.org/10.1145/3637528.3671597  
**Date analyzed:** 2026-08-18  
**Source ID:** e69a0fca-4086-4f0f-9da9-97887d0d6c59  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** Q1/Q2/Q3 not started after generative-query plateau; source fallback completed

---

## Required Survey Card Fields

- **Title:** Multi-objective Learning to Rank by Model Distillation
- **Authors or company:** Not specified in selected-source metadata
- **Venue:** KDD
- **Year:** 2024
- **URL:** https://doi.org/10.1145/3637528.3671597
- **Source type:** industry paper
- **Direction:** D1
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1, “Objective and labels.”
- **Prediction or incrementality:** Not specified in source. The indexed evidence supports outcome/utility prediction or optimization, not exposure-effect identification.
- **Model architecture:** See §1, “Architecture.”
- **Credit assignment:** See §1, “Credit assignment.”
- **Training data and counterfactual handling:** See §1, “Training evidence,” and the prediction/incrementality field above.
- **Offline and online evaluation:** See §2.
- **Reported gains:** See §2; no metrics are added beyond indexed-source evidence.
- **Applicability to a two-sided dating recommender:** See § Project Relevance.
- **Unverified claims:** All dating transfer statements below are survey inference, not claims made by the source.

---

## 1. Summary

### Core problem and contribution — indexed-source evidence

- bf63ca8b-4559-4c94-8e0b-27967ef41ca6 Multi-objective Learning to Rank by Model Distillation Jie Tang Airbnb San Francisco, USA jie.tang@airbnb.com Huiji Gao Airbnb San Francisco, USA huiji.gao@airbnb.com Liwei He…
- order cancellation(or return), review rating, customer service inquiries, platform long term growth.
- Multi-objective learning to rank has been widely studied to balance primary and secondary objectives.

### Objective — indexed-source evidence

- order cancellation(or return), review rating, customer service inquiries, platform long term growth.
- Although a higher conversion rate can increase marketplace revenues, the associated costs of cancellations, returns, and customer service can significantly eat into profits.
- bf63ca8b-4559-4c94-8e0b-27967ef41ca6 Multi-objective Learning to Rank by Model Distillation Jie Tang Airbnb San Francisco, USA jie.tang@airbnb.com Huiji Gao Airbnb San Francisco, USA huiji.gao@airbnb.com Liwei He…

### Label definition, horizon, delay, sparsity, and censoring — indexed-source evidence

- Besides the the challenges mentioned above, we also found another issue ignored by previous studies: nowadays most of ranking systems are deep learning models,…
- Besides optimizing aggregated objective cost functions, some study aggregated multiple labels into one label thus it could also construct a single objective cost function…
- But traditional approaches in industry face some challenges including expensive parameter tuning leads to sub-optimal solution, suffering from imbalanced data sparsity issue, and being…

### Architecture — indexed-source evidence

- bf63ca8b-4559-4c94-8e0b-27967ef41ca6 Multi-objective Learning to Rank by Model Distillation Jie Tang Airbnb San Francisco, USA jie.tang@airbnb.com Huiji Gao Airbnb San Francisco, USA huiji.gao@airbnb.com Liwei He…
- In this paper, we propose a distillation-based ranking solution for multi-objective ranking, which optimizes the end-to-end ranking system at Airbnb across multiple ranking models…

### Credit assignment — indexed-source evidence

- in Airbnb search, each search result page shows a finite site of listings, in most of time booking label is attributed to only one…
- 6 LEARNING AND FUTUREWORK Our experiments demonstrated the proposed MO-LTR-MD system doesn’t only help us find better optimization solution and improve model irrproducibility, but…
- Unlike web search, online marketplace is a two-sided market, both user journey and merchant journey is much longer than web search user: a typical…

### Training data and baselines — indexed-source evidence

- In industrial practice, scalarization is much more popular thanMOEAs given it’s simple and also easy to be scaled to large training data efficiently.
- The proposed model (MO-LTR-MD) is trained with around 360 millions training examples collected from last a few months which only contains booking label.
- In this paper, we propose a distillation-based ranking solution for multi-objective ranking, which optimizes the end-to-end ranking system at Airbnb across multiple ranking models…

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- Such update could be done daily, weekly, or monthly as offline batch training from scratch(cold start), or even in real-time as online continuous training.
- 5 EXPERIMENTAL RESULTS 5.1 Experiment Setup In this Airbnb experiment, the search ranking system is a multiobjective learning to rank system, the primary objective…
- [5] In early days, these studies only considered optimizing single objective: NDCG, since the major LTR application that time was web search.

### Reported gains — indexed-source evidence

- We found it performs much better than traditional approaches, it doesn’t only significantly increases primary objective by a large margin but also meet secondary…

### Limitations and negative results — indexed-source evidence

- But traditional approaches in industry face some challenges including expensive parameter tuning leads to sub-optimal solution, suffering from imbalanced data sparsity issue, and being…

**Statistical validity:** Not specified in source beyond the evidence snippets above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - In this case, such objective can’t be included into optimization directly, it has to be some manual tuning after the model is trained and…
- In this paper, we propose a distillation-based ranking solution for multi-objective ranking, which optimizes the end-to-end ranking system at Airbnb across multiple ranking models…
- In industrial practice, scalarization is much more popular thanMOEAs given it’s simple and also easy to be scaled to large training data efficiently.  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - But traditional approaches in industry face some challenges including expensive parameter tuning leads to sub-optimal solution, suffering from imbalanced data sparsity issue, and being…

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

**Survey inference:** The paper can inform replacing a hand-tuned score blend with learned multi-objective fusion, a delayed-value head, or a staged auxiliary-head design. A dating deployment would need labels at 7–30 day retention and weeks-long revenue horizons and must retain like, match, and conversation heads as stabilizing auxiliaries during migration.

**Prediction vs. incrementality:** Not specified in source. The indexed evidence supports outcome/utility prediction or optimization, not exposure-effect identification.

**Reciprocity and congestion:** Not specified in source unless explicitly present in the evidence above. Candidate-side capacity and bilateral acceptance therefore require an added reciprocal or marketplace layer.

**Cascade and low base rates:** The method may be mapped to impression → like → match → conversation → retention/revenue, but that mapping is survey inference and requires sparse-label calibration.

**Success paradox:** Not specified in source. A dating system must separately guard match quality and successful off-platform outcomes so retention/revenue optimization does not punish successful matching.

**Evaluation implication:** Reproduce the source's offline/online pattern where stated, then add dating-specific bilateral metrics, candidate exposure concentration, and incrementality validation.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** Not specified in selected-source metadata (individual authors not taken from selected-source metadata)  
**Affiliations:** Not specified in selected-source metadata  
**Venue:** KDD  
**Year:** 2024  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 1
