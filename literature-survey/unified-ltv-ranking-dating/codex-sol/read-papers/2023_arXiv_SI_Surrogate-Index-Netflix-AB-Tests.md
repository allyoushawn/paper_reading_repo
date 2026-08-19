# Paper Analysis: Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix

**Source:** https://arxiv.org/pdf/2311.11922  
**Date analyzed:** 2026-08-18  
**Source ID:** ad7e1e30-9bb9-47cb-ad2b-c14326f53adb  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** notebook_query intentionally not called; source_get_content success

---

## Required Survey Card Fields

- **Title:** Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix
- **Authors or company:** Netflix
- **Venue:** arXiv
- **Year:** 2023
- **URL:** https://arxiv.org/pdf/2311.11922
- **Source type:** industry-lab arXiv
- **Direction:** D3
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1, “Objective” and “Labels.”
- **Prediction or incrementality:** - In this paper, we leverage 1098 test arms from 200 A/B tests at Netflix to empirically investigate to what degree would decisions made using a surrogate index…
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

- Surrogate index approaches have recently become a popular method of estimating longer-term impact from shorter-term outcomes.
- In this paper, we leverage 1098 test arms from 200 A/B tests at Netflix to empirically investigate to what degree would decisions made using a surrogate index…
- Focusing specifically on linear “auto-surrogate” models that utilize the shorter-term observations of the long-term outcome of interest, we find that the statistical inferences that we would draw…
- Moreover, when we restrict ourselves to the set of tests that would be “launched” (i.e.

### Objective — indexed-source evidence

- Focusing specifically on linear “auto-surrogate” models that utilize the shorter-term observations of the long-term outcome of interest, we find that the statistical inferences that we would draw…
- Surrogate index approaches have recently become a popular method of estimating longer-term impact from shorter-term outcomes.

### Labels, horizon, delay, sparsity, and censoring — indexed-source evidence

- In this paper, we leverage 1098 test arms from 200 A/B tests at Netflix to empirically investigate to what degree would decisions made using a surrogate index…
- Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix Vickie Zhang Michael Zhao Anh Le Maria Dimakopoulou Nathan Kallus Abstract Surrogate index…
- Focusing specifically on linear “auto-surrogate” models that utilize the shorter-term observations of the long-term outcome of interest, we find that the statistical inferences that we would draw…

### Architecture — indexed-source evidence

- Surrogate index approaches have recently become a popular method of estimating longer-term impact from shorter-term outcomes.

### Credit assignment — indexed-source evidence

- Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix Vickie Zhang Michael Zhao Anh Le Maria Dimakopoulou Nathan Kallus Abstract Surrogate index…

### Training data, baselines, and counterfactual evidence

- Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix Vickie Zhang Michael Zhao Anh Le Maria Dimakopoulou Nathan Kallus Abstract Surrogate index…
- Learning causal effects from many randomized experiments using regularized instrumental variables.

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix Vickie Zhang Michael Zhao Anh Le Maria Dimakopoulou Nathan Kallus Abstract Surrogate index…
- In this paper, we leverage 1098 test arms from 200 A/B tests at Netflix to empirically investigate to what degree would decisions made using a surrogate index…

### Reported gains — indexed-source evidence

- Focusing specifically on linear “auto-surrogate” models that utilize the shorter-term observations of the long-term outcome of interest, we find that the statistical inferences that we would draw…
- We compare these against estimates produced via a surrogate index.

### Limitations, failure modes, and negative results — indexed-source evidence

- If this set of short-term outcomes taken together satisfies the “surrogacy assumption” [Prentice, 1989], namely that they fully mediate all of the treatment’s long-term effects and that…

**Statistical validity:** Not specified in source beyond the indexed evidence above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** - In this paper, we explore the efficacy of applying surrogate index methods at scale.  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - Further assuming that there are no or very low marginal costs for additional experiments, this implies that the benefits from increased throughput from a shorter, faster testing…

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

**Prediction vs. incrementality:** - In this paper, we leverage 1098 test arms from 200 A/B tests at Netflix to empirically investigate to what degree would decisions made using a surrogate index…

**Reciprocity and congestion:** Not specified in source unless explicitly shown above. Add candidate-capacity and bilateral-acceptance constraints.

**Cascade and low base rates:** Map the method to impression → like → match → conversation → retention/revenue only as a survey hypothesis; validate calibration and rare-event behavior.

**Success paradox:** Not specified in source. Protect match quality and successful off-platform outcomes so retention/revenue optimization does not penalize successful matching.

**Evaluation implication:** Add bilateral outcome metrics, candidate exposure concentration, delayed-label backtests, and randomized incrementality checks to any source protocol.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|---|---|---|
| [2024_KDD_NA_Choosing-Proxy-Metric-Past-Experiments.md](./2024_KDD_NA_Choosing-Proxy-Metric-Past-Experiments.md) | Introduction / Summary | Explicitly mentions full title in baseline or comparison context. |

---

## Meta Information

**Authors:** Netflix (individual authors not taken from selected-source metadata)  
**Affiliations:** Netflix  
**Venue:** arXiv  
**Year:** 2023  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 2
