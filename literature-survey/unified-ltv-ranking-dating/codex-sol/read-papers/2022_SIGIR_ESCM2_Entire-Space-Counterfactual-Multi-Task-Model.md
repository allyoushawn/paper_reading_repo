# Paper Analysis: ESCM2: Entire Space Counterfactual Multi-Task Model for Post-Click Conversion Rate Estimation

**Source:** https://arxiv.org/pdf/2204.05125  
**Date analyzed:** 2026-08-18  
**Source ID:** 43084729-4a01-433c-b6bc-c5316c19ea31  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** notebook_query intentionally not called; source_get_content success

---

## Required Survey Card Fields

- **Title:** ESCM2: Entire Space Counterfactual Multi-Task Model for Post-Click Conversion Rate Estimation
- **Authors or company:** Ant Group
- **Venue:** SIGIR
- **Year:** 2022
- **URL:** https://arxiv.org/pdf/2204.05125
- **Source type:** industry paper
- **Direction:** D5
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1, “Objective” and “Labels.”
- **Prediction or incrementality:** - Leveraging causality methodology, we propose the Entire Space Counterfactual Multi-task Model (ESCM 2 ), a model that incorpo- rates counterfactual risk minimizer (CRM), i.e.
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

- Accurate estimation of post-click conversion rate is critical for building recommender systems, which has long been confronted with sample selection bias and data sparsity issues.
- Methods in the Entire Space Multi-task Model (ESMM) family leverage the sequen- tial pattern of user actions, i.e.
- 𝑖𝑚𝑝𝑟𝑒𝑠𝑠𝑖𝑜𝑛 → 𝑐𝑙𝑖𝑐𝑘 → 𝑐𝑜𝑛𝑣𝑒𝑟𝑠𝑖𝑜𝑛 to address data sparsity issue.
- However, they still fail to ensure the unbiasedness of CVR estimates.

### Objective — indexed-source evidence

- 3b236c81-3bf6-4bb8-9374-65b64e0a6661 ecfc3c8f-1b3d-4a28-940e-b4467a2b1427 7 CONCLUSION AND FUTUREWORK Due to the effectiveness of modeling associations between tasks, ESMM dominates many large-scale business scenarios.
- Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are…
- As such, we intro- duce the counterfactual risk minimizers in section 4.1 and derive the final learning objective of ESCM 2 : ℒ ESCM 2 ∶= ℒCTR…
- Accurate estimation of post-click conversion rate is critical for building recommender systems, which has long been confronted with sample selection bias and data sparsity issues.

### Labels, horizon, delay, sparsity, and censoring — indexed-source evidence

- Scenario 1: This experiment was deployed in one of Ant insur- ance’s scenarios for 6 days, covering around 2.2 million unique visitors (UVs) and 3.1 million page…
- Denote 𝒪 as the click matrix where each entry 𝑜𝑢,𝑖 ∈ {0, 1} indicates whether clicking took place between user 𝑢 and item 𝑖 , R ∈…
- 𝑖𝑚𝑝𝑟𝑒𝑠𝑠𝑖𝑜𝑛 → 𝑐𝑙𝑖𝑐𝑘 → 𝑐𝑜𝑛𝑣𝑒𝑟𝑠𝑖𝑜𝑛 to address data sparsity issue.

### Architecture — indexed-source evidence

- 4.2 Architecture of ESCM2 As shown in Figure 4, we employ the multi-task learning tech- nique to train ESCM 2 , which is effective in alleviating data…
- Methods in the Entire Space Multi-task Model (ESMM) family leverage the sequen- tial pattern of user actions, i.e.
- Leveraging causality methodology, we propose the Entire Space Counterfactual Multi-task Model (ESCM 2 ), a model that incorpo- rates counterfactual risk minimizer (CRM), i.e.

### Credit assignment — indexed-source evidence

- Therefore, ESMM’s better performance in our case might be attributed to its multi-task learning paradigm.

### Training data, baselines, and counterfactual evidence

- Extensive experiments on offline datasets and online environments demonstrate that our proposed ESCM 2 can largely mitigate the inherent IEB and PIP issues and achieve better performance…
- Scenario 1: This experiment was deployed in one of Ant insur- ance’s scenarios for 6 days, covering around 2.2 million unique visitors (UVs) and 3.1 million page…
- Afterwards, we downsample the negative samples of the training set to keep the ratio of exposure:click:conversion to be 100:10:1, approximately.
- Leveraging causality methodology, we propose the Entire Space Counterfactual Multi-task Model (ESCM 2 ), a model that incorpo- rates counterfactual risk minimizer (CRM), i.e.

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- We conducted online experiments to further showcase the superi- ority of ESCM 2 over ESMM.
- Extensive experiments on offline datasets and online environments demonstrate that our proposed ESCM 2 can largely mitigate the inherent IEB and PIP issues and achieve better performance…
- Unbiased baseline estimators at large generally outperform the biased ones across these two datasets.
- For the offline experiments, following existing works, AUC (Area Under ROC) is primarily used as the main ranking metric to gauge performance.

### Reported gains — indexed-source evidence

- Another problem stems from the data sparsity of clicked samples, where we have a CTR around 3.8% on our production dataset and a 4% on the Ali-CCP…
- 5 EXPERIMENTS We conduct experiments to evaluate the performance of ESCM 2 and answer the following research questions: RQ1: Does ESCM2 outperform SOTA CVR and CTCVR estimators?
- The proposed ESCM 2 achieves significant improvement com- pared with various state-of-the-art baselines.

### Limitations, failure modes, and negative results — indexed-source evidence

- However, they still fail to ensure the unbiasedness of CVR estimates.

**Statistical validity:** Not specified in source beyond the indexed evidence above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - Another problem stems from the data sparsity of clicked samples, where we have a CTR around 3.8% on our production dataset and a 4% on the Ali-CCP…
- Figure 1 exhibits a two-stage pipeline to building recommender system in an industrial setting.  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - Admittedly, it has mitigated data sparsity effectively via parameter sharing [14, 16, 24]; however, unbiasedness of its CVR estimate is still not guaranteed.

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

**Survey inference:** This source can inform a staged multi-task cascade with impression-space auxiliary heads before adding delayed retention and revenue heads. For dating, any transfer must be tested with 7–30 day retention and weeks-long subscription/à-la-carte revenue labels while keeping like, match, and conversation heads as migration auxiliaries.

**Prediction vs. incrementality:** - Leveraging causality methodology, we propose the Entire Space Counterfactual Multi-task Model (ESCM 2 ), a model that incorpo- rates counterfactual risk minimizer (CRM), i.e.

**Reciprocity and congestion:** Not specified in source unless explicitly shown above. Add candidate-capacity and bilateral-acceptance constraints.

**Cascade and low base rates:** Map the method to impression → like → match → conversation → retention/revenue only as a survey hypothesis; validate calibration and rare-event behavior.

**Success paradox:** Not specified in source. Protect match quality and successful off-platform outcomes so retention/revenue optimization does not penalize successful matching.

**Evaluation implication:** Add bilateral outcome metrics, candidate exposure concentration, delayed-label backtests, and randomized incrementality checks to any source protocol.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|---|---|---|
| [2023_KDD_MTL_Optimizing-Airbnb-Search-Journey.md](./2023_KDD_MTL_Optimizing-Airbnb-Search-Journey.md) | Introduction / Summary | Explicitly names full title in the card evidence. |

---

## Meta Information

**Authors:** Ant Group (individual authors not taken from selected-source metadata)  
**Affiliations:** Ant Group  
**Venue:** SIGIR  
**Year:** 2022  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 2
