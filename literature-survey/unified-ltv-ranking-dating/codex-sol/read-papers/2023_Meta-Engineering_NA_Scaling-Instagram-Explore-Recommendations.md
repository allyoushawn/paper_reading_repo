# Paper Analysis: Scaling the Instagram Explore recommendations system

**Source:** https://engineering.fb.com/2023/08/09/ml-applications/scaling-instagram-explore-recommendations-system/  
**Date analyzed:** 2026-08-18  
**Source ID:** f11ef30f-1525-43fc-a365-f8318ea62e93  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** Q1/Q2/Q3 not started after generative-query plateau; source fallback completed

---

## Required Survey Card Fields

- **Title:** Scaling the Instagram Explore recommendations system
- **Authors or company:** Meta
- **Venue:** Meta-Engineering
- **Year:** 2023
- **URL:** https://engineering.fb.com/2023/08/09/ml-applications/scaling-instagram-explore-recommendations-system/
- **Source type:** company blog
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

- We leverage machine learning to make sure people are always seeing content that is the most interesting and relevant to them.
- Using more advanced machine learning models, like Two Towers neural networks, we've been able to make the Explore recommendation system even more scalable and…
- AI plays an important role in what people see on Meta's platforms .

### Objective — indexed-source evidence

- Additionally, retrieval sources can be real-time (capturing most recent interactions) and pre-generated (capturing long-term interests).
- As the system has continued to evolve, we've expanded our multi-stage ranking approach with several well-defined stages, each focusing on different objectives and algorithms.

### Label definition, horizon, delay, sparsity, and censoring — indexed-source evidence

- Every day, hundreds of millions of people visit Explore on Instagram to discover something new, making it one of the largest recommendation surfaces on…
- Even though the model architecture could be similar to retrieval, the learning objective differs quite a bit: We train the first stage ranker to…

### Architecture — indexed-source evidence

- Even though the model architecture could be similar to retrieval, the learning objective differs quite a bit: We train the first stage ranker to…
- The Two Towers model extends the Word2Vec algorithm, allowing us to use arbitrary user or media/author features and learn from multiple tasks at the…
- Learn more, including about available controls: Cookie Policy Accept
- Retrieval First-stage ranking Second-stage ranking Final reranking By leveraging caching and pre-computation with highly-customizable modeling techniques, like a Two Towers neural network (NN) ,…

### Credit assignment — indexed-source evidence

Not specified in source.

### Training data and baselines — indexed-source evidence

- Every day, hundreds of millions of people visit Explore on Instagram to discover something new, making it one of the largest recommendation surfaces on…
- But, given real-world requirements and constraints, most large-scale recommender systems employ a multi-stage funnel approach – starting with thousands of candidates and narrowing down…

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- Candidates from pre-generated sources could be generated offline during off-peak hours (e.g., locally popular media), which further contributes to system scalability.
- In Explore, because it's infeasible to rank all candidates using heavy models, we use two stages: A first-stage ranker (i.e., lightweight model), which is…

### Reported gains — indexed-source evidence

- Ranking in a high load system is usually divided into multiple stages that gradually reduce the number of candidates from a few thousand to…

### Limitations and negative results — indexed-source evidence

- However, it requires a strong correlation between offline and online metrics.

**Statistical validity:** Not specified in source beyond the evidence snippets above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - In a world with infinite computational power and no latency requirements we could rank all possible content.
- To build a large-scale system capable of recommending the most relevant content to people in real time out of billions of available options, we've…  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - In a world with infinite computational power and no latency requirements we could rank all possible content.

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

**Authors:** Meta (individual authors not taken from selected-source metadata)  
**Affiliations:** Meta  
**Venue:** Meta-Engineering  
**Year:** 2023  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 1
