# Paper Analysis: Addressing Delayed Feedback for Continuous Training with Neural Networks

**Source:** https://doi.org/10.1145/3298689.3347002  
**Source ID:** ee57717b-2970-4b54-ac93-ab024d7e503a  
**Date analyzed:** 2026-08-18  
**Model identifier:** codex-sol  
**Evidence mode:** NotebookLM indexed-content fallback after source-scoped query plateau.

---

## 1. Summary

**Authors:** Sofia Ira Ktena; Alykhan Tejani; Lucas Theis; Pranay Kumar Myana; Deepak Dilipkumar; Ferenc Huszár; Steven Yoo; Wenzhe Shi  
**Abstract:** The paper compares five delayed-label losses with logistic and wide-and-deep models for continuous Twitter ad training. Fake-negative weighting and calibration correct the duplicated-positive stream without waiting for labels.

**Main results:** On 668M internal examples the proposed losses improved relative cross-entropy about 3% over prior state of the art. Online, the top method delivered a 55% RPMq gain versus naive log loss. Positive-unlabeled loss diverged online.

---

## 2. Experiment Critique

**Design:** Public and proprietary offline data, shallow/deep architectures, five losses, engineering-cost comparison, and production validation.

**Statistical validity:** Headline relative improvements are reported; exact uncertainty, traffic split, duration, and metric guardrails are not in extracted content.

**Online experiments:** Yes; online instability of PU learning is an important negative result.

**Reproducibility:** Equations and architectures are described; internal data/pipeline are proprietary.

**Overall:** Strong practical evidence, though the unusually large online lift needs missing experiment detail for full interpretation.

---

## 3. Industry Contribution

**Deployability:** Designed explicitly for continuous large-scale training and discusses infrastructure tradeoffs.

**Project relevance:** Core baseline for training retention/revenue heads before labels mature; fake-negative weighting/calibration can prevent systematic underprediction.

**Most important mismatch:** Ad engagement delays are shorter and simpler than reciprocal dating outcomes, subscription revenue, or successful-exit censoring; the method is predictive, not causal.

---

## 4. Novelty vs. Prior Work

**Claimed novelty:** Broad principled comparison plus new fake-negative losses validated online with neural continuous training.

**Verification:** Source-grounded only.

---

## 5. Dataset Availability

| Dataset | Accessible | Notes |
|---------|------------|-------|
| Public delayed-feedback dataset | Partial | Name not in extracted snippets. |
| Twitter in-house | No | 668M examples. |

---

## 6. Community Reaction

No significant discussion assessed.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Affiliations:** Twitter  
**Venue:** RecSys  
**Year:** 2019  
**Relevance:** Core  
**Priority:** 1  
**Direction:** D7 — delayed feedback / censored labels
