# Paper Analysis: Optimizing Airbnb Search Journey with Multi-task Learning

**Source:** https://doi.org/10.1145/3580305.3599881  
**Date analyzed:** 2026-08-18  
**Source ID:** a32f27cc-d656-437c-8c7a-5090569572ce  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** Q1/Q2/Q3 not started after generative-query plateau; source fallback completed

---

## Required Survey Card Fields

- **Title:** Optimizing Airbnb Search Journey with Multi-task Learning
- **Authors or company:** Airbnb
- **Venue:** KDD
- **Year:** 2023
- **URL:** https://doi.org/10.1145/3580305.3599881
- **Source type:** industry paper
- **Direction:** D1
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1, “Objective and labels.”
- **Prediction or incrementality:** - ESCM2: Entire Space Counterfactual Multi-Task Model for Post-Click Conversion Rate Estimation.
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

- 1ad34ddb-2435-403c-90bb-4830d8a175c2 Optimizing Airbnb Search Journey with Multi-task Learning Chun How Tan Airbnb Inc.
- USA chunhow.tan@airbnb.com Austin Chan Airbnb Inc.
- USA austin.chan@airbnb.com Malay Haldar Airbnb Inc.

### Objective — indexed-source evidence

- USA sanjeev.katariya@airbnb.com ABSTRACT At Airbnb, an online marketplace for stays and experiences, guests often spend weeks exploring and comparing multiple items before making a…
- 2 RELATEDWORK The majority of previous works in Search and Recommendation involves training deep learning models to optimize for a single business objective such…
- They are also delayed outcomes where the final label could arrive after a long time has elapsed.

### Label definition, horizon, delay, sparsity, and censoring — indexed-source evidence

- USA sanjeev.katariya@airbnb.com ABSTRACT At Airbnb, an online marketplace for stays and experiences, guests often spend weeks exploring and comparing multiple items before making a…
- 034ca8e1-b362-4757-a32b-b540122182ee b4cc11c9-51c1-4332-a851-1eb9a2f76802 Optimizing Airbnb Search Journey with Multi-task Learning KDD ’23, August 6–10, 2023, Long Beach, CA, USA (a) Example search journey (b) Example…
- They are also delayed outcomes where the final label could arrive after a long time has elapsed.
- Instead, we need to capture sparse guests and hosts preferences at multiple stages (i.e.

### Architecture — indexed-source evidence

- In this paper, we present Jour-ney Ranker, a new multi-task deep learning model architecture that addresses these challenges.
- 1ad34ddb-2435-403c-90bb-4830d8a175c2 Optimizing Airbnb Search Journey with Multi-task Learning Chun How Tan Airbnb Inc.

### Credit assignment — indexed-source evidence

- 034ca8e1-b362-4757-a32b-b540122182ee b4cc11c9-51c1-4332-a851-1eb9a2f76802 Optimizing Airbnb Search Journey with Multi-task Learning KDD ’23, August 6–10, 2023, Long Beach, CA, USA (a) Example search journey (b) Example…
- Finally, we discuss possible future directions in Section 6.
- 1ad34ddb-2435-403c-90bb-4830d8a175c2 Optimizing Airbnb Search Journey with Multi-task Learning Chun How Tan Airbnb Inc.

### Training data and baselines — indexed-source evidence

- In that case, 𝑤𝑙𝑐 will be the empirical fraction of long clicks that will convert into an uncancelled booking in our training data.
- For model training, we use around 500 millions searches for training, and all the models are trained using Tensorflow.
- 2 RELATEDWORK The majority of previous works in Search and Recommendation involves training deep learning models to optimize for a single business objective such…
- ESCM2: Entire Space Counterfactual Multi-Task Model for Post-Click Conversion Rate Estimation.

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- 4 and the offline and online experiment results in Section 5.
- We conducted offline and online testing of the Journey Ranker and successfully deployed it in production to four different Airbnb products with significant business…
- In Section 3, we present the Airbnb Stays Ranking problem formulation and the baseline.
- These negative search milestones are rarer (<1% to 10% depending on the action), leading to class imbalance.

### Reported gains — indexed-source evidence

- We conducted offline and online testing of the Journey Ranker and successfully deployed it in production to four different Airbnb products with significant business…

### Limitations and negative results — indexed-source evidence

- The long and exploratory nature of the search journey, as well as the need to balance both guest and host preferences, present unique challenges…

**Statistical validity:** Not specified in source beyond the evidence snippets above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - We conducted offline and online testing of the Journey Ranker and successfully deployed it in production to four different Airbnb products with significant business…
- Leveraging a multi-task approach allows sharing of feature representation, resulting in better performance for each task through transfer learning, while achieving lower overall serving…  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - Specifically, given query parameters from the guest (e.g.

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

**Prediction vs. incrementality:** - ESCM2: Entire Space Counterfactual Multi-Task Model for Post-Click Conversion Rate Estimation.

**Reciprocity and congestion:** Not specified in source unless explicitly present in the evidence above. Candidate-side capacity and bilateral acceptance therefore require an added reciprocal or marketplace layer.

**Cascade and low base rates:** The method may be mapped to impression → like → match → conversation → retention/revenue, but that mapping is survey inference and requires sparse-label calibration.

**Success paradox:** Not specified in source. A dating system must separately guard match quality and successful off-platform outcomes so retention/revenue optimization does not punish successful matching.

**Evaluation implication:** Reproduce the source's offline/online pattern where stated, then add dating-specific bilateral metrics, candidate exposure concentration, and incrementality validation.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** Airbnb (individual authors not taken from selected-source metadata)  
**Affiliations:** Airbnb  
**Venue:** KDD  
**Year:** 2023  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 1
