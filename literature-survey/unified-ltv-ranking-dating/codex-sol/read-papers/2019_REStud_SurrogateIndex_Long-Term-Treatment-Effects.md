# Paper Analysis: The Surrogate Index

**Source:** https://www.nber.org/system/files/working_papers/w26463/w26463.pdf  
**Source index:** 101  
**Source ID:** f19c6829-6721-46d7-b6b5-9fc1301a9b16  
**Date analyzed:** 2026-08-18  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

---

## 1. Summary

**Authors:** Susan Athey; Raj Chetty; Guido W. Imbens; Hyunseung Kang  
**Abstract:** The surrogate-index method learns the conditional expectation of a long-term outcome from multiple short-term outcomes in an observational sample, then estimates an experimental treatment effect on that index. It formalizes unconfoundedness, surrogacy, comparability, and overlap assumptions; derives efficient estimators and bias bounds; and validates with California GAIN job-training data.

**Key contributions:** Data fusion for experimental short-term and observational long-term samples; precision gains for rare/noisy endpoints; diagnostics and bounds for assumption violations.

**Main results:** Short-term employment/earnings proxies detected long-term GAIN effects several years earlier and substantially improved precision; exact headline coefficients are not specified in the extracted passages.

---

## 2. Experiment Critique

**Design:** Formal identification/efficiency analysis plus cross-site empirical validation and held-out proxy checks.

**Statistical validity:** Explicit assumptions and bias bounds are strengths. Surrogacy and cross-sample comparability are fundamentally untestable in full; external validity depends on the observational bridge remaining stable.

**Online experiments:** None.

**Reproducibility:** Public program data/methods are described, but exact replication assets are not specified in source excerpts.

**Overall:** Strong causal framework for long-term proxy construction, with validity dominated by surrogate completeness and transportability.

---

## 3. Industry Contribution

**Deployability:** Requires an RCT with short-term signals plus historical cohorts with matured long-term labels.

**Project relevance:** Core. Likes, matches, conversations, and early sessions can form a learned surrogate index for 30-day retention or revenue, enabling faster experiments without hand-blended metrics.

**Most important mismatch:** Dating interventions may affect retention/revenue through paths not captured by proxies; reciprocity, congestion, and successful exit can violate surrogacy/comparability.

---

## 4. Novelty vs. Prior Work

**Claimed novelty:** Formal two-sample surrogate-index identification, efficient estimation, and bias analysis.

**Prior work comparison:** Extends clinical surrogacy, mediation, missing-data, and data-fusion literatures.

**Verification:** Source-grounded only.

---

## 5. Dataset Availability

| Dataset | Accessible | Notes |
|---------|------------|-------|
| California GAIN job-training data | Partial/public research data | Access details not specified in extracted source. |

---

## 6. Community Reaction

No significant discussion assessed.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## 8. Meta Information

**Venue:** NBER / Review of Economic Studies  
**Year:** 2019 (revised 2024)  
**Relevance:** Core  
**Priority:** 3  
**Direction:** D3 — proxy/surrogate objectives
