# Paper Analysis: Evaluating for the Long Term: Learnings from Industry

**Source:** https://arxiv.org/pdf/2608.08043  
**Date analyzed:** 2026-08-18  
**Source ID:** 4e0cbb02-d402-485e-8cb7-c37581a20095  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** notebook_query intentionally not called; source_get_content success

---

## Required Survey Card Fields

- **Title:** Evaluating for the Long Term: Learnings from Industry
- **Authors or company:** Multi-company workshop report
- **Venue:** arXiv
- **Year:** 2026
- **URL:** https://arxiv.org/pdf/2608.08043
- **Source type:** industry report
- **Direction:** D3
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1, “Objective” and “Labels.”
- **Prediction or incrementality:** - Participants largely agreed that reversals of sign from short-run to long-run treatment effects are rare, with reversals concentrating in specific cases such as treatments involving content quality…
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

- Evaluating for the Long Term: Learnings from Industry Leif Sigerson (Pinterest), Tom Cunningham (METR), Winston Chou (Netflix), Sana Pandey (MIT CSAIL), Jonathan Stray (UC Berkeley CHAI), Lo-Hua…
- Demetri Pananos (Datadog), Lee Richardson (Google), Brennan Schaffner (Knight-Georgetown Institute), Rose Tan, Martin Tingley, Nadia Tomova (Booking.com), Panagiotis Toulis (University of Chicago Booth School of Business), Wenjing…
- Our goal in this paper is to collect and share industry knowledge on how to make decisions from short-term experiments that are better aligned with long-term outcomes.
- Based on a daylong workshop with 26 experts from 15 online platforms and 4 universities, we formulate a series of propositions that reflect current industry knowledge.

### Objective — indexed-source evidence

- Evaluating for the Long Term: Learnings from Industry Leif Sigerson (Pinterest), Tom Cunningham (METR), Winston Chou (Netflix), Sana Pandey (MIT CSAIL), Jonathan Stray (UC Berkeley CHAI), Lo-Hua…
- “Hyper monetization” in gaming platforms that increases revenue in the short run but hurts it in the long run because of lost user retention.
- The goal of the methods we describe is not necessarily unbiased estimation of long-term treatment effects, although this can be an important input into decisions, but enabling…
- Although the magnitude of treatment effects can shift over time, a “univariate autosurrogate”, corresponding to the short-run treatment effect on the long-run metric of interest, is often…

### Labels, horizon, delay, sparsity, and censoring — indexed-source evidence

- The canonical problem we consider is predicting the effect of a change to a ranking algorithm on 6-month daily active users (DAU), based on 7-day cumulative measured…
- Demetri Pananos (Datadog), Lee Richardson (Google), Brennan Schaffner (Knight-Georgetown Institute), Rose Tan, Martin Tingley, Nadia Tomova (Booking.com), Panagiotis Toulis (University of Chicago Booth School of Business), Wenjing…
- Evaluating for the Long Term: Learnings from Industry Leif Sigerson (Pinterest), Tom Cunningham (METR), Winston Chou (Netflix), Sana Pandey (MIT CSAIL), Jonathan Stray (UC Berkeley CHAI), Lo-Hua…
- Furthermore, due to this cost, long-term experiments tend to be limited to the most significant changes, introducing selection bias.

### Architecture — indexed-source evidence

- In Proceedings of the 22nd IEEE International Conference on Software Architecture Companion (ICSA-C).
- (2024) find that policy learning based on a surrogate index led to similar results to policy learning based on the ground truth long-term outcomes; however, the test…
- Proxy metric An individual short-run metric that may be informative about long-run effects.

### Credit assignment — indexed-source evidence

- Here, we present propositions that gained consensus among workshop participants regarding the typical trajectory of treatment effects in instances where both short-run and long-run observations are available.
- Although the magnitude of treatment effects can shift over time, a “univariate autosurrogate”, corresponding to the short-run treatment effect on the long-run metric of interest, is often…
- Tackling interference induced by data training loops in A/B tests: A weighted training approach.

### Training data, baselines, and counterfactual evidence

- Even ignoring active iteration on features, algorithms can evolve according to the training data they collect.
- 3 1.1 Platforms with over 10 million monthly active users (MAU) run 10,000– 100,000+ experiments per year.
- Definitions Experiment A randomized A/B test in which users (unless otherwise specified) are randomly assigned to two or more conditions.

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- The canonical problem we consider is predicting the effect of a change to a ranking algorithm on 6-month daily active users (DAU), based on 7-day cumulative measured…
- Although the magnitude of treatment effects can shift over time, a “univariate autosurrogate”, corresponding to the short-run treatment effect on the long-run metric of interest, is often…

### Reported gains — indexed-source evidence

- In a meta-analysis of 200 A/B tests at Netflix, researchers report that the launch decision at two weeks would agree with the launch decision at two months…
- Here, we present propositions that gained consensus among workshop participants regarding the typical trajectory of treatment effects in instances where both short-run and long-run observations are available.

### Limitations, failure modes, and negative results — indexed-source evidence

- However, the drawback is that learning good surrogates from experiments typically requires a large, representative portfolio of long-run experiments that few platforms possess.

**Statistical validity:** Not specified in source beyond the indexed evidence above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - For example, a contextual bandit model that trains on both production and randomized data will evolve even without active development.
- Extensible experimentation platform: Effective A/B test analysis at scale.  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - Long-term metric effects are not the only input into launch decisions, which will often also depend on judgments of costs and benefits not captured in these aggregate…

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

**Prediction vs. incrementality:** - Participants largely agreed that reversals of sign from short-run to long-run treatment effects are rare, with reversals concentrating in specific cases such as treatments involving content quality…

**Reciprocity and congestion:** Not specified in source unless explicitly shown above. Add candidate-capacity and bilateral-acceptance constraints.

**Cascade and low base rates:** Map the method to impression → like → match → conversation → retention/revenue only as a survey hypothesis; validate calibration and rare-event behavior.

**Success paradox:** Not specified in source. Protect match quality and successful off-platform outcomes so retention/revenue optimization does not penalize successful matching.

**Evaluation implication:** Add bilateral outcome metrics, candidate exposure concentration, delayed-label backtests, and randomized incrementality checks to any source protocol.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** Multi-company workshop report (individual authors not taken from selected-source metadata)  
**Affiliations:** Multi-company workshop report  
**Venue:** arXiv  
**Year:** 2026  
**PDF:** NotebookLM indexed source available  
**Relevance:** Core  
**Priority:** 2
