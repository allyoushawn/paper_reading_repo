# Paper Analysis: A/B Testing for Recommender Systems in a Two-sided Marketplace

**Source:** https://arxiv.org/pdf/2106.00762  
**Date analyzed:** 2026-08-18  
**Source ID:** 607b5523-bda9-4e62-933f-7c3e67199154  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** notebook_query intentionally not called; source_get_content success

---

## Required Survey Card Fields

- **Title:** A/B Testing for Recommender Systems in a Two-sided Marketplace
- **Authors or company:** LinkedIn Corporation
- **Venue:** arXiv
- **Year:** 2021
- **URL:** https://arxiv.org/pdf/2106.00762
- **Source type:** industry paper
- **Direction:** D8
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1, “Objective” and “Labels.”
- **Prediction or incrementality:** - Our approach, called UniCoRn (Unifying Counterfactual Rankings), provides explicit control over the quality of the experiment and its computation cost.
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

- Two-sided marketplaces are standard business models of many online platforms (e.g., Amazon, Facebook, LinkedIn), wherein the platforms have consumers, buyers or content viewers on one side and…
- Consumer side measurement of the impact of a treatment variant can be done via simple online A/B testing.
- Producer side measurement is more challenging because the producer experience depends on the treatment assignment of the consumers.
- Existing approaches for producer side measurement are either based on graph cluster-based randomization or on certain treatment propagation assumptions.

### Objective — indexed-source evidence

- In one such experiment, the treatment model T1 optimized for viewee side retention, i.e., we boosted viewees likely to visit if they received an edge formation request.
- For example, a treatment may have an impact on a viewer’s attention (e.g., the amount of time a viewer is spending on each session or the total…

### Labels, horizon, delay, sparsity, and censoring — indexed-source evidence

- An online experiment typically spans over a time window, in which each consumer can have zero to more than one sessions and each producer can produce zero…
- One can get an unbiased estimate of the consumer-side impact (with respect to a metric, outcome or response of interest) by randomly exposing two disjoint groups of…
- This works well in sparse graphs where many such clusters can be found without ignoring too many edges.

### Architecture — indexed-source evidence

- Limitations and Future work: Our experiment design framework focuses on capturing the difference in exposure distribution of the producers in the treatment group and the producers in…
- Our approach, called UniCoRn (Unifying Counterfactual Rankings), provides explicit control over the quality of the experiment and its computation cost.

### Credit assignment — indexed-source evidence

- The design accuracy measurement framework based on Definition 1 does not directly translate to the accuracy in the producer side treatment effect estimation without additional assumptions on…
- A/B Testing for Recommender Systems in a Two-sided Marketplace Preetam Nandy, Divya Venugopalan, Chun Lo, Shaunak Chatterjee LinkedIn Corporation Mountain View, CA 94083 {pnandy, dvenugopalan, chunlo, shchatterjee}@linkedin.com…

### Training data, baselines, and counterfactual evidence

- We also deployed UniCoRn in an edge recommendation application that serves tens of millions of members and billions of edge recommendations daily.
- Our approach, called UniCoRn (Unifying Counterfactual Rankings), provides explicit control over the quality of the experiment and its computation cost.

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- A/B Testing for Recommender Systems in a Two-sided Marketplace Preetam Nandy, Divya Venugopalan, Chun Lo, Shaunak Chatterjee LinkedIn Corporation Mountain View, CA 94083 {pnandy, dvenugopalan, chunlo, shchatterjee}@linkedin.com…
- We use simulations to validate our approach and compare it against existing methods.
- Recall that {Rk(i, I ′)} denotes a ranking of the items in I ′ according to Tk in descending order (i.e.

### Reported gains — indexed-source evidence

- The equality holds in both cases when r 6= |Is|+1 2 and the treatment ranking {R1(i, Is)} is the reverse of the control ranking {R0(i, Is)} with…
- Figure 3a shows that the performance of UniCoRn(0) and UniCoRn(1) are roughly similar (or slightly better for UniCoRn(0)) with respect to MAE, but UniCoRn(1) outperforms UniCoRn(0) with…
- We use simulations to validate our approach and compare it against existing methods.

### Limitations, failure modes, and negative results — indexed-source evidence

- Existing approaches for producer side measurement are either based on graph cluster-based randomization or on certain treatment propagation assumptions.

**Statistical validity:** Not specified in source beyond the indexed evidence above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - We also deployed UniCoRn in an edge recommendation application that serves tens of millions of members and billions of edge recommendations daily.
- Hence, it is suitable for offline scoring applications and online applications without strict scoring latency constraints.
- Moreover, unlike the existing approaches, we do not need to know the underlying network in advance, making this widely applicable to the industrial setting where the underlying…  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - Our approach, called UniCoRn (Unifying Counterfactual Rankings), provides explicit control over the quality of the experiment and its computation cost.

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

**Survey inference:** This source is relevant to reciprocal or two-sided ranking, marketplace interference, congestion, or bilateral experimentation. For dating, any transfer must be tested with 7–30 day retention and weeks-long subscription/à-la-carte revenue labels while keeping like, match, and conversation heads as migration auxiliaries.

**Prediction vs. incrementality:** - Our approach, called UniCoRn (Unifying Counterfactual Rankings), provides explicit control over the quality of the experiment and its computation cost.

**Reciprocity and congestion:** This direction directly targets two-sided or reciprocal concerns where the evidence above supports them; dating still needs candidate-capacity and bilateral-acceptance checks.

**Cascade and low base rates:** Map the method to impression → like → match → conversation → retention/revenue only as a survey hypothesis; validate calibration and rare-event behavior.

**Success paradox:** Not specified in source. Protect match quality and successful off-platform outcomes so retention/revenue optimization does not penalize successful matching.

**Evaluation implication:** Add bilateral outcome metrics, candidate exposure concentration, delayed-label backtests, and randomized incrementality checks to any source protocol.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** LinkedIn Corporation (individual authors not taken from selected-source metadata)  
**Affiliations:** LinkedIn Corporation  
**Venue:** arXiv  
**Year:** 2021  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 2
