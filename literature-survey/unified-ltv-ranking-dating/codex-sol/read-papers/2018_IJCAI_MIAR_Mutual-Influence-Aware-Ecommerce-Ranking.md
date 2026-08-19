# Paper Analysis: Globally Optimized Mutual Influence Aware Ranking in E-Commerce Search

**Source:** https://doi.org/10.24963/ijcai.2018/518  
**Date analyzed:** 2026-08-18  
**Source ID:** e0f5a865-314a-4adb-9c25-7a3c4bbbfb4f  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** notebook_query intentionally not called; source_get_content success

---

## Required Survey Card Fields

- **Title:** Globally Optimized Mutual Influence Aware Ranking in E-Commerce Search
- **Authors or company:** Not specified in selected-source metadata
- **Venue:** IJCAI
- **Year:** 2018
- **URL:** https://doi.org/10.24963/ijcai.2018/518
- **Source type:** industry paper
- **Direction:** D1
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1, “Objective” and “Labels.”
- **Prediction or incrementality:** Not specified in source. Indexed evidence does not establish exposure-effect identification; treat the method as prediction or optimization unless validated experimentally.
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

- In web search, mutual influences between documents have been studied from the perspective of search result diversification.
- But the methods in web search is not directly applicable to e-commerce search because of their differences.
- And little research has been done on the mutual influences between items in e-commerce search.
- We propose a global optimization framework for mutual influence aware ranking in e-commerce search.

### Objective — indexed-source evidence

- Future research will be focused on more efficient attention mechanisms that increase GMV with less computations.
- Our framework directly optimizes the Gross Merchan-dise Volume (GMV) for ranking, and decomposes ranking into two tasks.
- We formulate ranking as a global optimization problem with the objective to maximize the mathematical expectation of GMV.
- The local features of an item include the price, the relevance to query, the Click Through Rate (CTR), the Click-purchase Conversion Rate (CVR), and various user preference…

### Labels, horizon, delay, sparsity, and censoring — indexed-source evidence

Not specified in source.

### Architecture — indexed-source evidence

- We propose a global optimization framework for mutual influence aware ranking in e-commerce search.
- [2017] model the sequential selection process as a Markov Decision Process and make a greedy selection at each step.

### Credit assignment — indexed-source evidence

- Neural machine translation by jointly learning to align and translate.

### Training data, baselines, and counterfactual evidence

- All the parameters and position embeddings are learned on training data.
- 4 Experiments 4.1 Experimental Setup Our experiments are carried out on the Taobao Search platform, which is one of the largest e-commerce search services in the world,…

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- We performed online A/B test on a large e-commerce search engine.
- The results show that our method brings a 5% increase in GMV for the search engine over a strong baseline.
- So the most widely used metric for e-commerce search in industry is the GMV of the search engine, rather than the Normalized Discounted Cumulative Gain (NDCG) for…

### Reported gains — indexed-source evidence

- The results show that our method brings a 5% increase in GMV for the search engine over a strong baseline.
- So the most widely used metric for e-commerce search in industry is the GMV of the search engine, rather than the Normalized Discounted Cumulative Gain (NDCG) for…

### Limitations, failure modes, and negative results — indexed-source evidence

- However, mutual influences between items in e-commerce search are quite different.

**Statistical validity:** Not specified in source beyond the indexed evidence above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - Each experimental algorithm of ours is deployed in 1 bucket.
- To study the additional computational Proceedings of the Twenty-Seventh International Joint Conference on Artificial Intelligence (IJCAI-18) 714571c4-e273-412c-89f1-c0644f99a6a7 5d9ce5cc-9b1c-4334-81bd-cc312c5359d3 0 10 20 30 40 50 60 70 rerank…  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - We compared the GMV and computational cost of our methods with a strong baseline.

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

**Survey inference:** This source can inform learned multi-objective fusion or list-level optimization that replaces a hand-tuned score blend. For dating, any transfer must be tested with 7–30 day retention and weeks-long subscription/à-la-carte revenue labels while keeping like, match, and conversation heads as migration auxiliaries.

**Prediction vs. incrementality:** Not specified in source. Indexed evidence does not establish exposure-effect identification; treat the method as prediction or optimization unless validated experimentally.

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
**Venue:** IJCAI  
**Year:** 2018  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 2
