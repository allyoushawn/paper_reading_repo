# Paper Analysis: Choosing a Proxy Metric from Past Experiments

**Source:** https://arxiv.org/pdf/2309.07893  
**Date analyzed:** 2026-08-18  
**Source ID:** e33e4636-ba5b-4b65-a4b4-abeb9df03476  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** notebook_query intentionally not called; source_get_content success

---

## Required Survey Card Fields

- **Title:** Choosing a Proxy Metric from Past Experiments
- **Authors or company:** Google DeepMind and Google
- **Venue:** KDD
- **Year:** 2024
- **URL:** https://arxiv.org/pdf/2309.07893
- **Source type:** industry-lab arXiv
- **Direction:** D3
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1, “Objective” and “Labels.”
- **Prediction or incrementality:** - Choosing a Proxy Metric from Past Experiments Nilesh Tripuraneni Google DeepMind nileshtrip@google.com Lee Richardson Google leerich@google.com Alexander D’Amour Google DeepMind alexdamour@google.com Jacopo Soriano Google jacoposoriano@google.com Steve Yadlowsky…
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

- In many randomized experiments, the treatment effect of the long-term metric (i.e.
- the primary outcome of interest) is often difficult or infeasible to measure.
- Such long-term metrics are often slow to react to changes and sufficiently noisy they are challenging to faithfully estimate in short-horizon experiments.
- A common alternative is to measure several short-term proxy metrics in the hope they closely track the long-term metric – so they can be used to effectively…

### Objective — indexed-source evidence

- In many randomized experiments, the treatment effect of the long-term metric (i.e.
- Rather it should depend on the sample size (or effective noise level) of the randomized experiment for which it is deployed in order to profitably trade-off bias…
- Conveniently, our definition also packages two important considerations for a proxy metric – short-term sensitivity of the proxy metric and directional alignment with the long-term outcome –…
- A common alternative is to measure several short-term proxy metrics in the hope they closely track the long-term metric – so they can be used to effectively…

### Labels, horizon, delay, sparsity, and censoring — indexed-source evidence

- Such long-term metrics are often slow to react to changes and sufficiently noisy they are challenging to faithfully estimate in short-horizon experiments.
- the primary outcome of interest) is often difficult or infeasible to measure.
- Choosing a Proxy Metric from Past Experiments Nilesh Tripuraneni Google DeepMind nileshtrip@google.com Lee Richardson Google leerich@google.com Alexander D’Amour Google DeepMind alexdamour@google.com Jacopo Soriano Google jacoposoriano@google.com Steve Yadlowsky…
- Variance reduction using in-experiment data: Efficient and targeted online measurement for sparse and delayed outcomes.

### Architecture — indexed-source evidence

- We introduce a new statistical framework to both define and construct an optimal proxy metric for use in a homogeneous population of randomized experiments.
- Such metrics are critical components in the decision-making pipelines of many large-scale technology companies [Chen and Fu, 2017, Rachitsky] as well as used to guide policy decisions…
- A common alternative is to measure several short-term proxy metrics in the hope they closely track the long-term metric – so they can be used to effectively…
- While only this assumption was needed for our previous discussion, we now introduce additional parametric structure in the form of an explicit generative model to allow for…

### Credit assignment — indexed-source evidence

- (4) Essentially all considerations noted in the previous section translate to the vector-valued setting mutatis mutandis.
- On the other hand, proxy metrics (or surrogates) that are easier to measure or faster to react are often available to use in lieu of the long-term…

### Training data, baselines, and counterfactual evidence

- Figure 2 provides an example where the inference procedure is used to extract the latent population variation in a synthetically generated dataset.
- Evaluating the surrogate index as a decision-making tool using 200 a/b tests at netflix.
- Hence, we use held-out/cross-validated 8 evaluations of certain criterion which depend on the noisy metrics aggregated over an evaluation set, to gauge the performance of proxy metrics…
- Choosing a Proxy Metric from Past Experiments Nilesh Tripuraneni Google DeepMind nileshtrip@google.com Lee Richardson Google leerich@google.com Alexander D’Amour Google DeepMind alexdamour@google.com Jacopo Soriano Google jacoposoriano@google.com Steve Yadlowsky…

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- Choosing a Proxy Metric from Past Experiments Nilesh Tripuraneni Google DeepMind nileshtrip@google.com Lee Richardson Google leerich@google.com Alexander D’Amour Google DeepMind alexdamour@google.com Jacopo Soriano Google jacoposoriano@google.com Steve Yadlowsky…
- To instantiate and evaluate our framework, we employ our methodology in a large corpus of randomized experiments from an industrial recommendation system and construct proxy metrics that…
- On the other hand, proxy metrics (or surrogates) that are easier to measure or faster to react are often available to use in lieu of the long-term…

### Reported gains — indexed-source evidence

- 6 Algorithm 1 Composite Proxy Algorithm Input: {(∆̂N i , ∆̂P i , Ξ̂i)}Ki=1 (TE and Noise Estimates from Historical Tests), Ξ̂PP K+1 (Noise Estimate for New…
- (3) Again, the estimated TEs are unbiased estimators of their underlying latent population quantities, so we can parameterize ∆̂P = ∆P + ( ΞPP )1/2 · ϵ,…

### Limitations, failure modes, and negative results — indexed-source evidence

- 1 Introduction Randomized controlled trials (RCTs) are the gold standard approach for measuring the causal effect of an intervention [Hernán and Robins, 2010]; however, designing and analyzing…

**Statistical validity:** Not specified in source beyond the indexed evidence above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - One key insight derived from our approach is that the optimal proxy metric for a given experiment is not apriori fixed; rather it should depend on the…
- The results of these A/B tests on long-term outcomes and proxy metrics are logged, serving as a history of past candidate launches that we may use to…
- To instantiate and evaluate our framework, we employ our methodology in a large corpus of randomized experiments from an industrial recommendation system and construct proxy metrics that…  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - Subsequently, we show how the relevant latent parameters contained in the definition of proxy quality can be efficiently estimated via a hierarchical model.

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

**Prediction vs. incrementality:** - Choosing a Proxy Metric from Past Experiments Nilesh Tripuraneni Google DeepMind nileshtrip@google.com Lee Richardson Google leerich@google.com Alexander D’Amour Google DeepMind alexdamour@google.com Jacopo Soriano Google jacoposoriano@google.com Steve Yadlowsky…

**Reciprocity and congestion:** Not specified in source unless explicitly shown above. Add candidate-capacity and bilateral-acceptance constraints.

**Cascade and low base rates:** Map the method to impression → like → match → conversation → retention/revenue only as a survey hypothesis; validate calibration and rare-event behavior.

**Success paradox:** Not specified in source. Protect match quality and successful off-platform outcomes so retention/revenue optimization does not penalize successful matching.

**Evaluation implication:** Add bilateral outcome metrics, candidate exposure concentration, delayed-label backtests, and randomized incrementality checks to any source protocol.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** Google DeepMind and Google (individual authors not taken from selected-source metadata)  
**Affiliations:** Google DeepMind and Google  
**Venue:** KDD  
**Year:** 2024  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 2
