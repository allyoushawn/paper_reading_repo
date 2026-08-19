# Paper Analysis: xMTF: A Formula-Free Model for Reinforcement-Learning-Based Multi-Task Fusion in Recommender Systems

**Source:** https://arxiv.org/html/2504.05669v1  
**Date analyzed:** 2026-08-18  
**Source ID:** da625059-d4d2-4065-9d44-6a9fe8a1cfba  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** Q1/Q2/Q3 not started after generative-query plateau; source fallback completed

---

## Required Survey Card Fields

- **Title:** xMTF: A Formula-Free Model for Reinforcement-Learning-Based Multi-Task Fusion in Recommender Systems
- **Authors or company:** Kuaishou
- **Venue:** WWW
- **Year:** 2025
- **URL:** https://arxiv.org/html/2504.05669v1
- **Source type:** industry paper
- **Direction:** D1
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1, “Objective and labels.”
- **Prediction or incrementality:** - Enhancing Interpretability and Effectiveness in Recommendation with Numerical Features via Learning to Contrast the Counterfactual samples.
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

- xMTF: A Formula-Free Model for Reinforcement-Learning-Based Multi-Task Fusion in Recommender Systems Report GitHub Issue × Title: Content selection saved.
- Describe the issue below: Description: Submit without GitHub Submit in GitHub arXiv is now an independent nonprofit!
- Learn more × arXiv logo Back to arXiv Why HTML?

### Objective — indexed-source evidence

- Recently, reinforcement learning (RL) has been applied to MTF tasks to improve long-term user satisfaction.
- Instead, overall satisfaction is indicated by long-term feedback such as session length, daily watch time, and retention, which cannot be directly linked to individual…
- Overall Framework Recall that our objective is to maximize the long-term user experience R t R_{t} in Eq.

### Label definition, horizon, delay, sparsity, and censoring — indexed-source evidence

- In practice, the xMTF model converges within two days when trained from scratch, and it is then continuously trained and updated online, serving users…
- However, the supervised learning of the inner stage is still challenging since the labels needed for learning are not directly provided by users (note…
- Feedback Sparse Ratio click 37.93% long view 26.35% like 1.51% follow 0.12% comment 0.25% share 0.09% Table 7.

### Architecture — indexed-source evidence

- To ensure fairness, we keep the same network architecture for the actors and critics across all compared methods, which consists of a five-layer MLP.
- Multi-gate Mixture-of-Experts (MMoE) ( Ma et al.
- xMTF: A Formula-Free Model for Reinforcement-Learning-Based Multi-Task Fusion in Recommender Systems Report GitHub Issue × Title: Content selection saved.
- Recently, reinforcement learning (RL) has been applied to MTF tasks to improve long-term user satisfaction.

### Credit assignment — indexed-source evidence

- Instead, overall satisfaction is indicated by long-term feedback such as session length, daily watch time, and retention, which cannot be directly linked to individual…

### Training data and baselines — indexed-source evidence

- 1: Input: training data (replay buffer) { 𝒔 1 : T , 𝒂 1 : T , r 1 : T , 𝒐 1…
- • Extensive offline and online experiments show the effectiveness of xMTF, and xMTF has been applied to our online system, serving over 100 million…
- Furthermore, we employ a two-stage hybrid (TSH) learning strategy to train xMTF effectively.
- 2022 construct the BatchRL-MTF framework for MTF recommendation tasks to address issues like the deadly triad problem and extrapolation error problem of traditional off-policy…

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- By expanding the MTF search space, xMTF outperforms existing methods in extensive offline and online experiments.
- • Extensive offline and online experiments show the effectiveness of xMTF, and xMTF has been applied to our online system, serving over 100 million…
- Baselines • Cross Entropy Method (CEM) ( Rubinstein and Kroese 2004 ) : a black-box optimization method commonly used for hyper-parameter optimization.
- Recall that existing approaches focus on personalizing only a few coefficients under pre-defined (non-personalized) fusion formulas.

### Reported gains — indexed-source evidence

- Recently, reinforcement learning (RL) has been applied to MTF tasks to improve long-term user satisfaction.

### Limitations and negative results — indexed-source evidence

- However, existing RL-based MTF methods are formula-based methods, which only adjust limited coefficients within pre-defined formulas.

**Statistical validity:** Not specified in source beyond the evidence snippets above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - Specifically, when a user exits a session, the session's data is immediately sent to the xMTF model for training, and the updated model is…
- • Extensive offline and online experiments show the effectiveness of xMTF, and xMTF has been applied to our online system, serving over 100 million…
- Reinforcing user retention in a billion scale short video recommender system.  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - The outer stage contains fewer parameters as RL actions, learning long-term rewards, while the inner stage, with more parameters, learns the knowledge of the…

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

**Prediction vs. incrementality:** - Enhancing Interpretability and Effectiveness in Recommendation with Numerical Features via Learning to Contrast the Counterfactual samples.

**Reciprocity and congestion:** Not specified in source unless explicitly present in the evidence above. Candidate-side capacity and bilateral acceptance therefore require an added reciprocal or marketplace layer.

**Cascade and low base rates:** The method may be mapped to impression → like → match → conversation → retention/revenue, but that mapping is survey inference and requires sparse-label calibration.

**Success paradox:** Not specified in source. A dating system must separately guard match quality and successful off-platform outcomes so retention/revenue optimization does not punish successful matching.

**Evaluation implication:** Reproduce the source's offline/online pattern where stated, then add dating-specific bilateral metrics, candidate exposure concentration, and incrementality validation.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** Kuaishou (individual authors not taken from selected-source metadata)  
**Affiliations:** Kuaishou  
**Venue:** WWW  
**Year:** 2025  
**PDF:** NotebookLM indexed source available  
**Relevance:** Core  
**Priority:** 1
