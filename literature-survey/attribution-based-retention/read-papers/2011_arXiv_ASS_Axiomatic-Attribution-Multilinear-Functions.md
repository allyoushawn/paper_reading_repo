# Paper Analysis: Axiomatic Attribution for Multilinear Functions

**Source:** https://arxiv.org/pdf/1102.0989.pdf  
**Date analyzed:** 2026-04-14 (NLM batch 2026-04-14; three `notebook_query` calls on source `a1aa3e37-f43b-4be5-9190-df6139a2d913` only)

---

## 1. Summary

**Title:** Axiomatic Attribution for Multilinear Functions  
**Authors:** Yi Sun, Mukund Sundararajan  
**Abstract:** Formalizes **attribution** as allocating the change \(f(s)-f(r)\) in a deterministic characteristic function \(f:\mathbb{R}^n\to\mathbb{R}\) across variables when inputs move from \(r\) to \(s\), requiring **completeness** \(\sum_i z_i = f(s)-f(r)\). For functions that are the **sum of a multilinear term and an additive term**, the authors prove there is a **unique** attribution rule satisfying Dummy, Additivity, Conditional Nonnegativity, Affine Scale Invariance, and Anonymity: the **Aumann–Shapley–Shubik (ASS)** path method. Outside this class, uniqueness fails. They give an efficient implementation for multilinear \(f\) and discuss PPC-style spend and portfolio analysis as applications.

**Key contributions:**
- Cost-sharing style axioms for “who caused how much of \(\Delta f\)?”
- Characterization theorem → unique ASS on multilinear + additive decomposable class; impossibility of the same axiom bundle pinning down a unique rule more broadly.
- Algorithmic recipe: dynamic program (**Algorithm 1**) computing ASS in **\(O(n^2 N)\)** time and **\(O(n)\)** memory for multilinear \(f\) with \(N\) nonzero monomials; unification of Aumann–Shapley and Shapley–Shubik on that class.

**Methodology:** Axiomatic derivation; relate to classical cost sharing; constructive path formulas for multilinear polynomials.

**Main results:** Uniqueness on stated class; explicit failure of naive partial-derivative attributions to satisfy completeness on large moves (worked example: attributions sum to 130.5 vs true \(\Delta f = 86\)); Theorem 4.4 — Aumann–Shapley and Shapley–Shubik agree **iff** \(f\) is multilinear + additively separable.

---

## 2. Experiment Critique

**Design:** Theory paper with illustrative analytic examples (e.g., multiplicative spend \(s=c\cdot p\)); not large-scale logged experiments.

**Statistical validity:** \(f\) assumed **known, deterministic**, and not learned from noisy data; \(r,s\) known exactly—appropriate for structural attribution of a **given** response surface, not raw sparse logs without a model.

**Online experiments (if any):** Not specified in source.

**Reproducibility:** Fully reproducible from closed-form definitions once \(f,r,s\) are specified.

**Overall:** Foundational credit algebra for **factorable nonlinear** surrogates—bridges calculus-style incremental shares to axiomatic fairness.

---

## 3. Industry Contribution

**Deployability:** High whenever conversion or a retention proxy is modeled as a **known** multilinear (+additive) function of levers (factored probabilities, multiplicative funnel models, DAG flow models with multilinear structure).

**Problems solved:** Prevents incomplete “local linearization” attributions that violate completeness on finite moves \(r\to s\).

**Engineering cost:** Requires explicit functional form \(f\); path integration / DP vs one-step gradients.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First systematic axiomatization linking multilinear attribution to unique ASS; clarifies limits outside that function class.

**Prior work comparison:** Builds on cooperative game / cost-sharing literature (Friedman & Moulin; Moulin; Aumann & Shapley; Shapley–Shubik; Billera–Heath; Mirman–Tauman; Owen multilinear extension, etc.); distinct from empirical Shapley sampling in black-box MTA papers.

**Verification:** Axiomatic claims are mathematical; PPC examples are conceptual.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Illustrative analytic examples | In paper | Yes | Toy multilinear functions |

**Offline experiment reproducibility:** N/A beyond worked algebra.

---

## 6. Community Reaction

No significant community discussion found (mature 2011 arXiv / Electronic Commerce reference work).

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|------------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Yi Sun, Mukund Sundararajan  
**Affiliations:** Not extracted in this pass (see PDF v2 front matter)  
**Venue:** arXiv (cs.GT); journal reference Electronic Commerce 2011  
**Year:** 2011 (arXiv v2 dated 2011)  
**PDF:** https://arxiv.org/pdf/1102.0989.pdf  
**Relevance:** Core  
**Priority:** 3  
**NLM:** `nlm:a1aa3e37-f43b-4be5-9190-df6139a2d913`

---

## Project Relevance

**Phase 1 label generation:** The paper does **not** learn from logs or correct **selection bias**; it requires a **deterministic** \(f\) and exact \(r,s\). It **does** provide a **unique, complete** split of any finite \(\Delta f\) across coordinates—so if Phase 1 first fits a **calibrated multilinear (+additive) surrogate** of expected **user-days-active** from binned touch counts or typed intensities, ASS yields **structured fractional increments** that can serve as **analytic pseudo-labels** or sanity checks against black-box MTA/Shapley outputs.

**Continuous outcomes:** Directly aligned with attributing changes in **real-valued** \(f\); maps naturally from “binary purchase” to “\(\Delta\) expected active days” once \(f\) is defined.

**Heterogeneous touches:** Credits are per **model coordinate** (e.g., channel or feature dimension), not necessarily per raw event row—aggregation vs sub-component attribution must follow the paper’s warnings (e.g., attributing on aggregates can mislead; attribute on components then aggregate).
