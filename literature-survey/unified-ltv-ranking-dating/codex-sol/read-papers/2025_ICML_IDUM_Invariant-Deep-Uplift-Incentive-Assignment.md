# Paper Analysis: Invariant Deep Uplift Modeling for Incentive Assignment in Online Marketing via Probability of Necessity and Sufficiency

**Source:** https://icml.cc/virtual/2025/poster/44136  
**Date analyzed:** 2026-08-18  
**Source ID:** ca3a7f72-3089-435d-a0ba-7bea28e3ec04  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** notebook_query intentionally not called; source_get_content success

---

## Required Survey Card Fields

- **Title:** Invariant Deep Uplift Modeling for Incentive Assignment in Online Marketing via Probability of Necessity and Sufficiency
- **Authors or company:** Not specified in selected-source metadata
- **Venue:** ICML
- **Year:** 2025
- **URL:** https://icml.cc/virtual/2025/poster/44136
- **Source type:** industry paper
- **Direction:** D6
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1, “Objective” and “Labels.”
- **Prediction or incrementality:** - Uplift modeling methods are developed to estimate user responses from observational data, often incorporating distribution balancing to address selection bias.
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

- In online platforms, incentives (\textit{e.g}., discounts, coupons) are used to boost user engagement and revenue.
- Uplift modeling methods are developed to estimate user responses from observational data, often incorporating distribution balancing to address selection bias.
- However, these methods are limited by in-distribution testing data, which mirrors the training data distribution.
- In reality, user features change continuously due to time, geography, and other factors, especially on complex online marketing platforms.

### Objective — indexed-source evidence

- For instance, Booking implements promotional strategies to enhance user satisfaction ( Albert & Goldenberg , 2022 ), Meituan uses cash bonuses to stimulate user retention ( Wang…
- In online platforms, incentives (\textit{e.g}., discounts, coupons) are used to boost user engagement and revenue.
- The objective of uplift modeling is to evaluate the effect of treatment on the response for a given user with features , specifically calculating the difference between…
- Uplift modeling methods are developed to estimate user responses from observational data, often incorporating distribution balancing to address selection bias.

### Labels, horizon, delay, sparsity, and censoring — indexed-source evidence

- For instance, platforms may assign incentives based on user age, indicating a tendency to target younger users to enhance profit margins, which is called selection bias.
- Uplift modeling methods are developed to estimate user responses from observational data, often incorporating distribution balancing to address selection bias.

### Architecture — indexed-source evidence

- Regarding continuous outcomes, the Causal Forest ( Davis & Heller , 2017 ), a random forest-like algorithm, employs causal trees ( Daron- deau & Degano , 1989…
- Modeling task relationships in multi-task learning with multi-gate mixture-of-experts.
- Invariant policy learning: A causal perspective.
- Uplift modeling methods are developed to estimate user responses from observational data, often incorporating distribution balancing to address selection bias.

### Credit assignment — indexed-source evidence

- This can be attributed to their utilization of Integral Probability Metrics, such as Maximum Mean Discrepancy and Wasserstein distance, which facilitate the mitigation of selection bias between…
- Unite: A unified treatment effect esti- mation method for one-sided and two-sided marketing.

### Training data, baselines, and counterfactual evidence

- However, these methods are limited by in-distribution testing data, which mirrors the training data distribution.
- We also adopt an early stopping mechanism with a patience of 5 to avoid over-fitting to the training set.
- The objective of uplift modeling is to evaluate the effect of treatment on the response for a given user with features , specifically calculating the difference between…

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- Overall comparison between our IDUM and the baselines on ID Lazada and Production datasets.
- Show more Lay Summary Online platforms leverage incentives (e.g., discounts, coupons) to enhance user engagement and revenue, with uplift modeling methods estimating user responses from observational data…

### Reported gains — indexed-source evidence

- 3) Encouragingly, our IDUM consistently outperforms all baselines across both the Lazada dataset and the Production dataset, particularly on OOD testing data.

### Limitations, failure modes, and negative results — indexed-source evidence

- However, these methods are limited by in-distribution testing data, which mirrors the training data distribution.

**Statistical validity:** Not specified in source beyond the indexed evidence above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - Overall comparison between our IDUM and the baselines on ID Lazada and Production datasets.
- Secondly, the IPL part, serving as a crucial component for managing the distribution shift between training and testing data, significantly contributes to the accurate estimation of uplift,…
- We utilize a large-scale production dataset obtained from real voucher distribution operations at Lazada, a prominent e-commerce platform in Southeast Asia (SEA) operated by the Alibaba Group.  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - In reality, user features change continuously due to time, geography, and other factors, especially on complex online marketing platforms.

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

**Survey inference:** This source can inform moving incrementality inside ranking or policy optimization, directly addressing the gap between outcome prediction and exposure effect. For dating, any transfer must be tested with 7–30 day retention and weeks-long subscription/à-la-carte revenue labels while keeping like, match, and conversation heads as migration auxiliaries.

**Prediction vs. incrementality:** - Uplift modeling methods are developed to estimate user responses from observational data, often incorporating distribution balancing to address selection bias.

**Reciprocity and congestion:** Not specified in source unless explicitly shown above. Add candidate-capacity and bilateral-acceptance constraints.

**Cascade and low base rates:** Map the method to impression → like → match → conversation → retention/revenue only as a survey hypothesis; validate calibration and rare-event behavior.

**Success paradox:** Not specified in source. Protect match quality and successful off-platform outcomes so retention/revenue optimization does not penalize successful matching.

**Evaluation implication:** Add bilateral outcome metrics, candidate exposure concentration, delayed-label backtests, and randomized incrementality checks to any source protocol.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** Not specified in selected-source metadata (individual authors not taken from selected-source metadata)  
**Affiliations:** Not specified in selected-source metadata  
**Venue:** ICML  
**Year:** 2025  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 2
