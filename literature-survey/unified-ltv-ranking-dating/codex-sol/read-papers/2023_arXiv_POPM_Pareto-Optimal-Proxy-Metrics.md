# Paper Analysis: Pareto Optimal Proxy Metrics

**Source:** https://arxiv.org/pdf/2307.01000  
**Date analyzed:** 2026-08-18  
**Source ID:** 0c4393ea-b677-42e2-8fa0-410244bffdcf  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** notebook_query intentionally not called; source_get_content success

---

## Required Survey Card Fields

- **Title:** Pareto Optimal Proxy Metrics
- **Authors or company:** Google Inc.
- **Venue:** arXiv
- **Year:** 2023
- **URL:** https://arxiv.org/pdf/2307.01000
- **Source type:** industry-lab arXiv
- **Direction:** D3
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1, “Objective” and “Labels.”
- **Prediction or incrementality:** - We can write this as P (Reject H0) = ∫ P (Reject H0|δ)dP (δ), (1) where δ is the true treatment effect, P (Reject H0|δ) is the…
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

- North star metrics and online experimentation play a central role in how technology companies improve their products.
- In many practical settings, however, evaluating experiments based on the north star metric directly can be difficult.
- The two most significant issues are 1) low sensitivity of the north star metric and 2) differences between the shortterm and long-term impact on it.
- A common solution is to rely on proxy metrics rather than the north star in experiment evaluation and launch decisions.

### Objective — indexed-source evidence

- The two most significant issues are 1) low sensitivity of the north star metric and 2) differences between the shortterm and long-term impact on it.
- We also give a multiobjective optimization algorithm to solve our specific problem.
- A common solution is to rely on proxy metrics rather than the north star in experiment evaluation and launch decisions.

### Labels, horizon, delay, sparsity, and censoring — indexed-source evidence

- A standard flow is the following: a team of engineers, data scientists and product managers have an idea to improve the product; the idea is implemented, and…
- This is a crucial aspect of insensitive target: empirically, we show that there is an inverse between how sensitive a proxy is in the short term, and…
- The two most significant issues are 1) low sensitivity of the north star metric and 2) differences between the shortterm and long-term impact on it.
- A first future direction involves the introduction of sparsity when finding the Pareto front.

### Architecture — indexed-source evidence

- The advantage of our approach lies within its high modularity with respect to the choices of sensitivity and correlation measures, yielding an easily adaptable framework to the…
- A common solution is to rely on proxy metrics rather than the north star in experiment evaluation and launch decisions.
- In particular, we propose the Pareto optimal proxy metrics method, which simultaneously optimizes prediction accuracy and sensitivity.

### Credit assignment — indexed-source evidence

- A solution to deal with this problem is to use a proxy metric, also referred to as a surrogate metric, in place of the north star (Duan…

### Training data, baselines, and counterfactual evidence

- Indeed, experiments can also be viewed as training data for proxy metrics, which in turn leads to more precise proxies.
- Each gray dot represents evaluations of the objective in a randomized search.

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- Chan School of Public Health, Boston, MA, USA 2Google Inc., San Bruno, CA, USA February 20, 2025 Abstract North star metrics and online experimentation play a central…
- For example, in our applied simulation below, we pick T = 7 as an additional guard against day of week effects, but values for T = 5…
- We learned baseline sensitivities, how the baseline sensitives vary across different product areas, and the correlations between metrics.
- A solution to deal with this problem is to use a proxy metric, also referred to as a surrogate metric, in place of the north star (Duan…

### Reported gains — indexed-source evidence

- , J denote the shortterm recorded values for metric m in experiment j in the treatment and in the control group, respectively, and let Xi,j,m = 100%…
- Finally, we illustrate the improvements obtained by Pareto-optimal proxies in a set of experiments from a large recommendation system.

### Limitations, failure modes, and negative results — indexed-source evidence

- In many practical settings, however, evaluating experiments based on the north star metric directly can be difficult.

**Statistical validity:** Not specified in source beyond the indexed evidence above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - 5.1 Considerations beyond Pareto optimality Below are other important considerations we learned from deploying proxy metrics in practice: Make sure you need proxies before developing them.
- We apply our methodology to experiments from a large industrial recommendation system, and found proxy metrics that are eight times more sensitive than the north star and…  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - , N , where θj,m and σ2 j,m are unknown mean and variance parameters.

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

**Prediction vs. incrementality:** - We can write this as P (Reject H0) = ∫ P (Reject H0|δ)dP (δ), (1) where δ is the true treatment effect, P (Reject H0|δ) is the…

**Reciprocity and congestion:** Not specified in source unless explicitly shown above. Add candidate-capacity and bilateral-acceptance constraints.

**Cascade and low base rates:** Map the method to impression → like → match → conversation → retention/revenue only as a survey hypothesis; validate calibration and rare-event behavior.

**Success paradox:** Not specified in source. Protect match quality and successful off-platform outcomes so retention/revenue optimization does not penalize successful matching.

**Evaluation implication:** Add bilateral outcome metrics, candidate exposure concentration, delayed-label backtests, and randomized incrementality checks to any source protocol.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** Google Inc. (individual authors not taken from selected-source metadata)  
**Affiliations:** Google Inc.  
**Venue:** arXiv  
**Year:** 2023  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 2
