# Paper Analysis: Estimating the Long-Term Effects of Novel Treatments: The Dynamically Adjusted Surrogate Index

**Source:** https://arxiv.org/pdf/2103.08390  
**Date analyzed:** 2026-08-18  
**Source ID:** 2a94d6c3-3337-4a8c-af75-1733f35e8e77  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** notebook_query intentionally not called; source_get_content success

---

## Required Survey Card Fields

- **Title:** Estimating the Long-Term Effects of Novel Treatments: The Dynamically Adjusted Surrogate Index
- **Authors or company:** Microsoft Research
- **Venue:** arXiv
- **Year:** 2021
- **URL:** https://arxiv.org/pdf/2103.08390
- **Source type:** industry-lab arXiv
- **Direction:** D3
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1, “Objective” and “Labels.”
- **Prediction or incrementality:** - Our work combines three major recent techniques in the causal machine learning literature: surrogate indices, dynamic treatment effect estimation and double machine learning, in a unified pipeline.
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

- Policy makers typically face the problem of wanting to estimate the long-term effects of novel treatments, while only having historical data of older treatment options.
- We assume access to a long-term dataset where only past treatments were administered and a short-term dataset where novel treatments have been administered.
- We propose a surrogate based approach where we assume that the long-term effect is channeled through a multitude of available short-term proxies.
- Our work combines three major recent techniques in the causal machine learning literature: surrogate indices, dynamic treatment effect estimation and double machine learning, in a unified pipeline.

### Objective — indexed-source evidence

- Policy makers typically face the problem of wanting to estimate the long-term effects of novel treatments, while only having historical data of older treatment options.
- In practice, this can for instance include the next few months of revenue and other measures that are indicative of a customer’s trajectory.
- This allows one to use the historical long-term data set to learn a mapping from short-term signals to a projected long-term reward — referred to as the…
- We propose a surrogate based approach where we assume that the long-term effect is channeled through a multitude of available short-term proxies.

### Labels, horizon, delay, sparsity, and censoring — indexed-source evidence

- A sample from each population consists of a finite horizon time-series (S0, T1, S1, Y1, T2, S2, Y2, .
- The fundamental assumption of the surrogate index is that there exist short-term proxies that are observed in the short-term dataset and that causal effects on long-term outcomes…
- Estimating the Long-Term Effects of Novel Treatments: The Dynamically Adjusted Surrogate Index Keith Battocchi 1 Eleanor Dillon 1 Maggie Hei 1 Greg Lewis 1 Miruna Oprescu 1…

### Architecture — indexed-source evidence

- Policy makers typically face the problem of wanting to estimate the long-term effects of novel treatments, while only having historical data of older treatment options.
- Estimating the Long-Term Effects of Novel Treatments: The Dynamically Adjusted Surrogate Index Keith Battocchi 1 Eleanor Dillon 1 Maggie Hei 1 Greg Lewis 1 Miruna Oprescu 1…
- , τM ), let Y (τ) t denote the counterfactual outcome at period t under such a sequence of interventions, equivalently in do-calculus notation Yt | do(T̄M…

### Credit assignment — indexed-source evidence

- These future investments can substantially increase the long-term outcome of interest, and this increase will be attributed to the short-term proxies.
- In practice, this can for instance include the next few months of revenue and other measures that are indicative of a customer’s trajectory.
- Estimating the Long-Term Effects of Novel Treatments: The Dynamically Adjusted Surrogate Index Keith Battocchi 1 Eleanor Dillon 1 Maggie Hei 1 Greg Lewis 1 Miruna Oprescu 1…

### Training data, baselines, and counterfactual evidence

- We assume access to a long-term dataset where only past treatments were administered and a short-term dataset where novel treatments have been administered.
- , τM ), let Y (τ) t denote the counterfactual outcome at period t under such a sequence of interventions, equivalently in do-calculus notation Yt | do(T̄M…

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- The top row plots the estimation error when estimating the effect on four periods of outcomes, increasing the sample size of each simulation from left to right,…
- Our goal is to estimate the causal effect of treatment vector T1 on the long term outcome: Ȳ := M∑ t=1 Yt (long-term outcome) in the experimental/short-term…
- Estimating the Long-Term Effects of Novel Treatments: The Dynamically Adjusted Surrogate Index Keith Battocchi 1 Eleanor Dillon 1 Maggie Hei 1 Greg Lewis 1 Miruna Oprescu 1…

### Reported gains — indexed-source evidence

- Begin with a long-term observational data set that, for each period and customer, consists of customer characteristics Xi,t, customer surrogates for growth Si,t+1 and realized M -period…
- This is again satisfied if the data generating process adheres to the causal graph presented in Figure 3a, as can be easily verified from the single-world-intervention graph…

### Limitations, failure modes, and negative results — indexed-source evidence

- We show that our method is consistent and provides root-n asymptotically normal estimates under a Markovian assumption on the data and the observational policy.

**Statistical validity:** Not specified in source beyond the indexed evidence above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - We evaluate the performance of our method and discuss practical challenges of deploying our formal methodology and how to address them.
- Based on these insights, we then draw new coefficients for each model, with decaying trend on lagged variables in different scale, and randomly draw coefficients for demographics.  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - These two parameters govern how surrogates today relate to future outcomes in the absence of any treatment.

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

**Survey inference:** This source can inform validation and selection of short-term surrogate metrics for slow retention and revenue outcomes; it is evaluation infrastructure, not by itself a ranking architecture. For dating, any transfer must be tested with 7–30 day retention and weeks-long subscription/à-la-carte revenue labels while keeping like, match, and conversation heads as migration auxiliaries.

**Prediction vs. incrementality:** - Our work combines three major recent techniques in the causal machine learning literature: surrogate indices, dynamic treatment effect estimation and double machine learning, in a unified pipeline.

**Reciprocity and congestion:** Not specified in source unless explicitly shown above. Add candidate-capacity and bilateral-acceptance constraints.

**Cascade and low base rates:** Map the method to impression → like → match → conversation → retention/revenue only as a survey hypothesis; validate calibration and rare-event behavior.

**Success paradox:** Not specified in source. Protect match quality and successful off-platform outcomes so retention/revenue optimization does not penalize successful matching.

**Evaluation implication:** Add bilateral outcome metrics, candidate exposure concentration, delayed-label backtests, and randomized incrementality checks to any source protocol.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** Microsoft Research (individual authors not taken from selected-source metadata)  
**Affiliations:** Microsoft Research  
**Venue:** arXiv  
**Year:** 2021  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 2
