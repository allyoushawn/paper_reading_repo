# Paper Analysis: Recommending What Video to Watch Next: A Multitask Ranking System

**Source:** https://doi.org/10.1145/3298689.3346997  
**Date analyzed:** 2026-08-18  
**Source ID:** a130cd67-9f8e-488b-b844-aa91ba854ef2  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** Q1/Q2/Q3 not started after generative-query plateau; source fallback completed

---

## Required Survey Card Fields

- **Title:** Recommending What Video to Watch Next: A Multitask Ranking System
- **Authors or company:** Google / YouTube
- **Venue:** RecSys
- **Year:** 2019
- **URL:** https://doi.org/10.1145/3298689.3346997
- **Source type:** industry paper
- **Direction:** D1-D5
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1.
- **Prediction or incrementality:** - Batch learning from logged bandit feedback through counterfactual risk minimization.
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

- Recommending What Video to Watch Next: A Multitask Ranking System Zhe Zhao, Lichan Hong, Li Wei, Jilin Chen, Aniruddh Nath, Shawn Andrews, Aditee Kumthekar,…
- {zhezhao,lichan,liwei,jilinc,aniruddhnath,shawnandrews,aditeek,nlogn,xinyang,edchi}@google.com ABSTRACT In this paper, we introduce a large scale multi-objective ranking system for recommending what video to watch next on an industrial video…
- The system faces many real-world challenges, including the presence of multiple competing ranking objectives, as well as implicit selection biases in user feedback.

### Objective — indexed-source evidence

- {zhezhao,lichan,liwei,jilinc,aniruddhnath,shawnandrews,aditeek,nlogn,xinyang,edchi}@google.com ABSTRACT In this paper, we introduce a large scale multi-objective ranking system for recommending what video to watch next on an industrial video…

### Label definition, horizon, delay, sparsity, and censoring — indexed-source evidence

- architecture factorizes the label in training data into two parts: the unbiased user utility learned from the main model, and the estimated propensity score…
- It cuts across two difcult issues: 1) bridging the semantic gap from low-level content features for content fltering; 2) learning from sparse distribution of…

### Architecture — indexed-source evidence

- To address these challenges, we propose an efcient multitask neural network architecture for the ranking system, as shown in Figure 1.
- To tackle these challenges, we explored a variety of soft-parameter sharing techniques such as Multi-gate Mixture-of-Experts so as to efciently optimize for multiple ranking…
- {zhezhao,lichan,liwei,jilinc,aniruddhnath,shawnandrews,aditeek,nlogn,xinyang,edchi}@google.com ABSTRACT In this paper, we introduce a large scale multi-objective ranking system for recommending what video to watch next on an industrial video…
- Ranking distillation: Learning compact ranking models with high performance for recommender system.

### Credit assignment — indexed-source evidence

- 5.4 Discussion In this section, we discuss a few insights and limitations which we have learned from the journey of developing and experimenting our…

### Training data and baselines — indexed-source evidence

- To model and reduce the selection bias (e.g., position bias) from biased training data, we propose to add a shallow tower to the main…
- Scalability is extremely important since we are building a recommendation system for billions of users and videos.
- Therefore, models trained using data generated from the current system will be biased, causing a feedback loop efect [33].
- Batch learning from logged bandit feedback through counterfactual risk minimization.

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- For live experiments, we conduct A/B testing comparing with production system.
- Comparing with state-of-the-art baseline methods, we show signifcant improvements of our proposed framework.
- Recall that the goal of our recommendation system is to provide a ranked list of videos, given currently watching video and context.

### Reported gains — indexed-source evidence

- In training, the positions of all impressions are used, with a 10% feature drop-out rate to prevent our model from over-relying on the position…
- We demonstrated that our proposed techniques can lead to substantial improvements on recommendation quality on one of the world’s largest video sharing platforms.

### Limitations and negative results — indexed-source evidence

- The system faces many real-world challenges, including the presence of multiple competing ranking objectives, as well as implicit selection biases in user feedback.

**Statistical validity:** Not specified in source beyond the evidence snippets above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - 2.3 Understanding and Modeling Biases in Training Data User logs, which are used as our training data, capture user behaviors and responses to recommendations…
- decided by the current system, and outputs a scalar serving as aACM ISBN 978-1-4503-6243-6/19/09.
- {zhezhao,lichan,liwei,jilinc,aniruddhnath,shawnandrews,aditeek,nlogn,xinyang,edchi}@google.com ABSTRACT In this paper, we introduce a large scale multi-objective ranking system for recommending what video to watch next on an industrial video…  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - To tackle these challenges, we explored a variety of soft-parameter sharing techniques such as Multi-gate Mixture-of-Experts so as to efciently optimize for multiple ranking…

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

**Prediction vs. incrementality:** - Batch learning from logged bandit feedback through counterfactual risk minimization.

**Reciprocity and congestion:** Not specified in source unless explicitly present above. Candidate-side capacity and bilateral acceptance require an added reciprocal or marketplace layer.

**Cascade and low base rates:** Mapping the method onto impression → like → match → conversation → retention/revenue is survey inference and requires sparse-label calibration.

**Success paradox:** Not specified in source. A dating system must protect match quality and successful outcomes so retention/revenue optimization does not punish successful matching.

**Evaluation implication:** Where source evidence exists, reproduce its offline/online protocol; add bilateral metrics, candidate exposure concentration, and incrementality validation.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** Google / YouTube (individual authors not taken from selected-source metadata)  
**Affiliations:** Google / YouTube  
**Venue:** RecSys  
**Year:** 2019  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 1
