# Paper Analysis: Understanding dwell time to improve LinkedIn feed ranking

**Source:** https://www.linkedin.com/blog/engineering/feed/understanding-feed-dwell-time  
**Date analyzed:** 2026-08-18  
**Source ID:** f461ed13-1164-4d28-90f9-51e7132d2acb  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** Q1/Q2/Q3 not started after generative-query plateau; source fallback completed

---

## Required Survey Card Fields

- **Title:** Understanding dwell time to improve LinkedIn feed ranking
- **Authors or company:** LinkedIn
- **Venue:** LinkedIn-Engineering
- **Year:** 2020
- **URL:** https://www.linkedin.com/blog/engineering/feed/understanding-feed-dwell-time
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

- Staff Software Engineer at LinkedIn May 12, 2020 Co-authors: Siddharth Dangi , Johnson Jia , Manas Somaiya , and Ying Xuan The LinkedIn feed…
- It’s where our members post ideas, career news, questions, and jobs in an array of formats, including short text, long-form articles, images, and videos.
- The Feed AI Team’s mission is to help LinkedIn’s members discover the most relevant conversations and content in their feed to help them be…

### Objective — indexed-source evidence

- Aside from a few notable exceptions, we assume that members value their time, and will spend it appropriately on feed content that they’re interested…
- A single choice of the threshold T skip works well for all of the heterogenous update types Incorporating a new P(skip) model into feed…

### Label definition, horizon, delay, sparsity, and censoring — indexed-source evidence

- We can use a member’s dwell time on an update to modify the weight and/or label of our training data points, which can improve…
- With this assumption in mind, dwell time has the following advantages over solely looking at click and viral actions: table Click/Viral Actions Dwell Time…

### Architecture — indexed-source evidence

Not specified in source.

### Credit assignment — indexed-source evidence

Not specified in source.

### Training data and baselines — indexed-source evidence

- We can use a member’s dwell time on an update to modify the weight and/or label of our training data points, which can improve…
- To accomplish this, we train our machine learning models to predict several quantities for each possible click and viral action (click, react, comment, share):…

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- To measure the impact of our new P(skip) model and features, we conducted several online A/B experiments on a small percentage of LinkedIn members.
- Through numerous experiments, we found that a combination of member-update features (which estimate a member’s interest in content of a certain type based on…

### Reported gains — indexed-source evidence

- Through numerous experiments, we found that a combination of member-update features (which estimate a member’s interest in content of a certain type based on…
- In this post, we explore how understanding our members’ time distribution spent on the feed has helped us improve the algorithms that rank content.

### Limitations and negative results — indexed-source evidence

- However, the work described in this post is only one component of a larger strategy to incorporate dwell time into our AI modeling.

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

**Authors:** LinkedIn (individual authors not taken from selected-source metadata)  
**Affiliations:** LinkedIn  
**Venue:** LinkedIn-Engineering  
**Year:** 2020  
**PDF:** NotebookLM indexed source available  
**Relevance:** Core  
**Priority:** 1
