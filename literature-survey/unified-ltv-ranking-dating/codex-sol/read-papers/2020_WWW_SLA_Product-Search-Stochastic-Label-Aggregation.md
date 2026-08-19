# Paper Analysis: Multi-Objective Ranking Optimization for Product Search Using Stochastic Label Aggregation

**Source:** https://doi.org/10.1145/3366423.3380122  
**Date analyzed:** 2026-08-18  
**Source ID:** f3865b86-af82-4689-bede-d274881b5f83  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** Q1/Q2/Q3 not started after generative-query plateau; source fallback completed

---

## Required Survey Card Fields

- **Title:** Multi-Objective Ranking Optimization for Product Search Using Stochastic Label Aggregation
- **Authors or company:** Not specified in selected-source metadata
- **Venue:** WWW
- **Year:** 2020
- **URL:** https://doi.org/10.1145/3366423.3380122
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

- Multi-Objective Ranking Optimization for Product Search Using Stochastic Label Aggregation David Carmel Amazon Haifa, Israel dacarmel@amazon.com Elad Haramaty Amazon Haifa, Israel eladh@amazon.com Arnon Lazerson…
- Multi-Objective Rank- ing Optimization (MORO) is the task of learning a ranking model from training examples while optimizing multiple objectives si- multaneously.
- Label aggregation is a popular solution approach for multi-objective optimization, which reduces the problem into a single objective optimization problem, by aggregating the multiple…

### Objective — indexed-source evidence

- [14] focused on user feedback signals (such as click rate, order rate, revenue and add-to-cart) as objective criteria for training and evaluation.
- Multi-Objective Ranking Optimization for Product Search Using Stochastic Label Aggregation David Carmel Amazon Haifa, Israel dacarmel@amazon.com Elad Haramaty Amazon Haifa, Israel eladh@amazon.com Arnon Lazerson…

### Label definition, horizon, delay, sparsity, and censoring — indexed-source evidence

- The purchase label P is derived by the number of purchases of p given q, relative to the number of times it was offered…
- Multi-Objective Ranking Optimization for Product Search Using Stochastic Label Aggregation David Carmel Amazon Haifa, Israel dacarmel@amazon.com Elad Haramaty Amazon Haifa, Israel eladh@amazon.com Arnon Lazerson…

### Architecture — indexed-source evidence

- Our experimental results (see Section 5.3) reveal that the two- phase approach provides a very strong optimization mechanism, which can be partially explained due…
- Multi-Objective Ranking Optimization for Product Search Using Stochastic Label Aggregation David Carmel Amazon Haifa, Israel dacarmel@amazon.com Elad Haramaty Amazon Haifa, Israel eladh@amazon.com Arnon Lazerson…

### Credit assignment — indexed-source evidence

- In Proceedings of TheWeb Conference 2020 (WWW This paper is published under the Creative Commons Attribution 4.0 International (CC-BY 4.0) license.
- 1 INTRODUCTION Product search provided by eCommerce sites is an important service allowing customers to search for products which they can purchase, or upon…
- They considered both clicks and purchases for modeling the two stages of the purchase journey and propose a nested framework to model the interdependence…

### Training data and baselines — indexed-source evidence

- We experiment on three different datasets: two from the voice product search domain, and one publicly available dataset from the Web product search domain.
- Multi-Objective Rank- ing Optimization (MORO) is the task of learning a ranking model from training examples while optimizing multiple objectives si- multaneously.

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- Multi-Objective Ranking Optimization for Product Search Using Stochastic Label Aggregation David Carmel Amazon Haifa, Israel dacarmel@amazon.com Elad Haramaty Amazon Haifa, Israel eladh@amazon.com Arnon Lazerson…

### Reported gains — indexed-source evidence

- Label aggregation is a popular solution approach for multi-objective optimization, which reduces the problem into a single objective optimization problem, by aggregating the multiple…

### Limitations and negative results — indexed-source evidence

- Moreover, we prove that this does not hold in the case of deterministic aggregation, by describing a spe- cific MORO problem, with an existing…

**Statistical validity:** Not specified in source beyond the evidence snippets above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** Not specified in source.  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - We provide a theoretical proof showing that stochastic label aggregation is superior to alternative aggregation approaches, in the sense that any optimal solution of…

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

**Authors:** Not specified in selected-source metadata (individual authors not taken from selected-source metadata)  
**Affiliations:** Not specified in selected-source metadata  
**Venue:** WWW  
**Year:** 2020  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 1
