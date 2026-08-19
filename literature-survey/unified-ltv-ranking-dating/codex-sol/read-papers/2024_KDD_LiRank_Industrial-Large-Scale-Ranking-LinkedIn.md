# Paper Analysis: LiRank: Industrial Large Scale Ranking Models at LinkedIn

**Source:** https://arxiv.org/pdf/2402.06859  
**Date analyzed:** 2026-08-18  
**Source ID:** 53250d02-7287-46f6-9fc7-c7afe931b690  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** Q1/Q2/Q3 not started after generative-query plateau; source fallback completed

---

## Required Survey Card Fields

- **Title:** LiRank: Industrial Large Scale Ranking Models at LinkedIn
- **Authors or company:** LinkedIn
- **Venue:** KDD
- **Year:** 2024
- **URL:** https://arxiv.org/pdf/2402.06859
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

- We unveil several modeling improvements, including Residual DCN, which adds attention and residual connections to the famous DCNv2 architecture.
- We share insights into combining and tuning SOTA architectures to create a unified model, including Dense Gating, Transformers and Residual DCN.
- We also propose novel techniques for calibration and describe how we productionalized deep learning based explore/exploit methods.

### Objective — indexed-source evidence

- A simple utilization of member’s historical feedback data ("exploitation") to maximize immediate performance might hurt long term gain; while boosting new items (“exploration”) could…
- distribution can change when using different models or objectives.

### Label definition, horizon, delay, sparsity, and censoring — indexed-source evidence

- Experiments Feed Ranking Ads CTR Cold Start Data Range 21 days 14 days Incremental Data Range 1 day 0.5 day Incremental Iterations 6 4…
- Usually only positive customized chargeable clicks are treated as positive labels.
- However, as Feed scaled up from using 13% of sessions for training to using 100% of sessions, this join caused long delay.
- Sparse ID embedding features (§A.1) are transformed into dense embeddings [21] through lookup in embedding tables of Member/Actor 95d120fe-5834-4b3f-84b6-36a4be58e268 ad2fc165-b5eb-4b22-ac15-8e6cb03de01a LiRank: Industrial Large Scale…

### Architecture — indexed-source evidence

- We unveil several modeling improvements, including Residual DCN, which adds attention and residual connections to the famous DCNv2 architecture.
- We also explored common approaches, including MMoE [19] and PLE [29].
- In §3, we discuss our approach to developing high-performing production ranking models, combining Residual DCN (§3.3), isotonic calibration layer (§3.4), dense gating with larger…

### Credit assignment — indexed-source evidence

- In Ads CTR prediction, we observed a +0.9% CTR relative improvement in online testing, which we attribute to quantization smoothing decision boundaries, improving generalization…
- A simple utilization of member’s historical feedback data ("exploitation") to maximize immediate performance might hurt long term gain; while boosting new items (“exploration”) could…
- These ideas have contributed to relative metrics improvements across the board at LinkedIn: +0.5% member sessions in the Feed, +1.76% qualified job applications for…

### Training data and baselines — indexed-source evidence

- Denote the current dataset at timestamp 𝑡 as D𝑡 , the last estimated weight vector as w𝑡−1, the Hessian matrix with regard to w𝑡−1…
- 1 Introduction LinkedIn is the world’s largest professionals network with more than 1 billion members in more than 200 countries and territories worldwide.
- To enable effective, production-grade serving of large ranking models, we detail how to train and compress models using quantization and vocabulary compression.

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- We summarize our learnings from various A/B tests by elucidating the most effective technical approaches.
- In §5, we detail our experiences in deploying large-ranking models in production for Feed Ranking, Jobs Recommendations, and Ads CTR prediction, summarizing key learnings…
- Our exploration of MTL in SPR has involved various model architectures designed to improve task-specific learning, each with unique features and benefits: (1) Hard…
- These ideas have contributed to relative metrics improvements across the board at LinkedIn: +0.5% member sessions in the Feed, +1.76% qualified job applications for…

### Reported gains — indexed-source evidence

- We unveil several modeling improvements, including Residual DCN, which adds attention and residual connections to the famous DCNv2 architecture.

### Limitations and negative results — indexed-source evidence

- Integrating various architectures into a large-scale unified ranking model presented challenges such as diminishing returns (first attempt lead to no gain), overfitting, divergence, and…

**Statistical validity:** Not specified in source beyond the evidence snippets above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - We also propose novel techniques for calibration and describe how we productionalized deep learning based explore/exploit methods.
- To enable effective, production-grade serving of large ranking models, we detail how to train and compress models using quantization and vocabulary compression.
- We provide details about the deployment setup for large-scale use cases of Feed ranking, Jobs Recommendations, and Ads click-through rate (CTR) prediction.  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - Proposed modeling advancements within this paper enabled our models to efficiently handle a larger number of parameters, leading to higher-quality content delivery.

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

**Authors:** LinkedIn (individual authors not taken from selected-source metadata)  
**Affiliations:** LinkedIn  
**Venue:** KDD  
**Year:** 2024  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 1
