# Paper Analysis: Multitask Mixture of Sequential Experts for User Activity Streams

**Source:** https://doi.org/10.1145/3394486.3403359  
**Date analyzed:** 2026-08-18  
**Source ID:** 3aa95e7d-b724-4750-8924-22fee68db14a  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** Q1/Q2/Q3 not started after generative-query plateau; source fallback completed

---

## Required Survey Card Fields

- **Title:** Multitask Mixture of Sequential Experts for User Activity Streams
- **Authors or company:** Not specified in selected-source metadata
- **Venue:** KDD
- **Year:** 2020
- **URL:** https://doi.org/10.1145/3394486.3403359
- **Source type:** industry paper
- **Direction:** D1-D5
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

- Multitask Mixture of Sequential Experts for User Activity Streams Zhen Qin∗, Yicheng Cheng∗, Zhe Zhao, Zhe Chen, Donald Metzler, Jingzheng Qin Google LLC, Mountain…
- Multi-task learning has become the standard approach for such applications recently.
- While most of the multi-task recommendation model architectures proposed to date are focusing on using non-sequential input features (e.g., query and context), input data…

### Objective — indexed-source evidence

- Turning Clicks into Purchases: Revenue Optimization for Product Search in E-Commerce.
- Multitask Mixture of Sequential Experts for User Activity Streams Zhen Qin∗, Yicheng Cheng∗, Zhe Zhao, Zhe Chen, Donald Metzler, Jingzheng Qin Google LLC, Mountain…

### Label definition, horizon, delay, sparsity, and censoring — indexed-source evidence

- The horizontal axis is time, vertical axis is the feature or target value.
- The recent work [5] shows it can be beneficial to stochastically aggregate the labels.
- They typically possess very different properties such as data sparsity and thus need careful treatment when being modeled jointly.

### Architecture — indexed-source evidence

- While most of the multi-task recommendation model architectures proposed to date are focusing on using non-sequential input features (e.g., query and context), input data…
- The model is a novel combination of the state-of-art multi-gate mixture of experts (MMoE) multi-task learning model [24] and Long Short-Term Memory (LSTM) [15].
- Multi-task learning has become the standard approach for such applications recently.
- Exploring techniques such as model distillation [14] is a future direction.

### Credit assignment — indexed-source evidence

- Learning shared Applied Data Science Track Paper KDD '20, August 23–27, 2020, Virtual Event, USA This work is licensed under a Creative Commons Attribution…
- [17] proposes a self-attention based sequential model for next item recommendation [13] shows that RNN can learn multiple user dynamics patterns in individual recommendation…

### Training data and baselines — indexed-source evidence

- For example, user behavior streams, such as user search logs in search systems, are naturally a temporal sequence.
- We also demonstrate the effectiveness and flexibility of the MoSE architecture in a real-world decision making engine in GMail that involves millions of users,…
- It alleviates the need of task training weight tuning for achieving accurate predictions on all tasks.

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- Our application only requires an offline inference of the UI decision for users daily.
- Due to the accurate modeling of MoSE, it outperforms baselines consistently on serving with different business needs after a single MoSE model is trained.
- In order to evaluate how the models performed at different tradeoff points, we measure the overall performance by the AUC (Area Under the Curve)…

### Reported gains — indexed-source evidence

- For a given time step 𝑡 with input x(𝑡 ) , we can formulate the output for task 𝑘 at time 𝑡 + 1…
- This potentially improves performance of all tasks involved, especially those with sparse signals when tackled alone (e.g.

### Limitations and negative results — indexed-source evidence

- While multi-task learning can potentially help to learn better joint representations for different user behavior objectives, we face the following challenges: Data Sparsity —…

**Statistical validity:** Not specified in source beyond the evidence snippets above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - Recently, neural multi-task learning, which jointlymodels multiple objectives, has been actively researched for such kind of problems and has been deployed in several real-world…
- Due to the accurate modeling of MoSE, it outperforms baselines consistently on serving with different business needs after a single MoSE model is trained.
- For example, a large scale multi-objective ranking system was introduced for recommending the next video to watch on an industrial video sharing platform, and…  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - We also demonstrate the effectiveness and flexibility of the MoSE architecture in a real-world decision making engine in GMail that involves millions of users,…

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

**Survey inference:** The paper may inform long-horizon retention optimization or request-level credit assignment. This transfer is unverified. A dating deployment needs 7–30 day retention and weeks-long revenue labels while preserving like, match, and conversation auxiliaries during migration.

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
**Venue:** KDD  
**Year:** 2020  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 1
