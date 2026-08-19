# Paper Analysis: Multi-task Learning and Calibration for Utility-based Home Feed Ranking

**Source:** https://medium.com/pinterest-engineering/multi-task-learning-and-calibration-for-utility-based-home-feed-ranking-64087a7bcbad  
**Date analyzed:** 2026-08-18  
**Source ID:** ea19556b-36f9-42a7-ab79-6549c3d77729  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM source description fallback after indexed content failure  
**Query status:** Q1/Q2/Q3 not started after generative-query plateau; source fallback failed (indexed content and source description unavailable)

---

## Required Survey Card Fields

- **Title:** Multi-task Learning and Calibration for Utility-based Home Feed Ranking
- **Authors or company:** Pinterest
- **Venue:** Pinterest-Engineering
- **Year:** 2020
- **URL:** https://medium.com/pinterest-engineering/multi-task-learning-and-calibration-for-utility-based-home-feed-ranking-64087a7bcbad
- **Source type:** company blog
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

Not specified in source.

### Objective — indexed-source evidence

Not specified in source.

### Label definition, horizon, delay, sparsity, and censoring — indexed-source evidence

Not specified in source.

### Architecture — indexed-source evidence

Not specified in source.

### Credit assignment — indexed-source evidence

Not specified in source.

### Training data and baselines — indexed-source evidence

Not specified in source.

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

Not specified in source.

### Reported gains — indexed-source evidence

Not specified in source.

### Limitations and negative results — indexed-source evidence

Not specified in source.

**Statistical validity:** Not specified in source beyond the evidence snippets above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** Not specified in source.  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** Not specified in source.

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

**Source-grounded facts:** Not specified in source because both indexed-content and source-description fallbacks failed.

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

**Authors:** Pinterest (individual authors not taken from selected-source metadata)  
**Affiliations:** Pinterest  
**Venue:** Pinterest-Engineering  
**Year:** 2020  
**PDF:** NotebookLM indexed source unavailable  
**Relevance:** Core  
**Priority:** 1
