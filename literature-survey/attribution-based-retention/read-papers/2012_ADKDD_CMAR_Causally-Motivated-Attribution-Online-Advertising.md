# Paper Analysis: Causally Motivated Attribution for Online Advertising

**Source:** https://fosterprovost.com/wp-content/uploads/2019/07/CAUSALLY-MOTIVATED-ATTRIBUTION.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Causally Motivated Attribution for Online Advertising  
**Authors:** Brian Dalessandro; Chris Perlich; Ori Stitelman; Foster Provost (Media6Degrees / NYU)  
**Abstract:** Defines **channel importance** as **Shapley value** over a space \(\Omega\) of feasible joint distributions of channels (including uniform over subsets as a default); decomposes predicted conversion probability into additive channel credits; studies confounding where retargeting absorbs credit from prospecting.

**Key contributions:**
- Shapley attribution on predictive model \(P(Y=1\mid \mathbf{X})\) with explicit \(\Omega\) for counterfactual channel presence/absence.
- Empirical case: retargeting vs prospecting with **38–73%** of retargeting conversions reallocated under causal-motivated \(\Omega\) vs last-touch.

**Methodology:** Logistic (and ensemble) models on display campaign data; compares last-touch, proportional hazard-style, and Shapley under different \(\Omega\).

**Main results:** Large credit shifts when \(\Omega\) encodes realistic joint channel variation; discussion of incentive alignment for budget allocation.

---

## 2. Experiment Critique

**Design:** Observational campaign studies; Shapley on fitted model—not RCT incrementality.

**Statistical validity:** Choice of \(\Omega\) drives results (sensitivity central to paper).

**Online experiments (if any):** Not specified in source.

**Reproducibility:** Historical Yahoo/campaign examples; full public replication bundle not specified in source.

**Overall:** Seminal **causal-motivated Shapley** framing for display MTA predating deep neural MTA wave.

---

## 3. Industry Contribution

**Deployability:** High conceptually — wraps existing conversion model.

**Problems solved:** Retargeting inflation under last-touch; transparent counterfactual credit via \(\Omega\).

**Engineering cost:** Moderate–high — exponential subsets unless approximations.

---

## 4. Novelty vs. Prior Work

Predates many neural MTA papers; influences later game-theoretic and causal MTA lines (cited in Molina et al. 2020 and surveys).

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Internal display logs | N/A | No | Case studies |

**Offline experiment reproducibility:** Not specified in source.

---

## 6. Community Reaction

Not specified in source.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** Brian Dalessandro; Chris Perlich; Ori Stitelman; Foster Provost  
**Affiliations:** Media6Degrees; NYU Stern  
**Venue:** ADKDD / KDD Applied Data Science Track 2012  
**Year:** 2012  
**PDF:** https://fosterprovost.com/wp-content/uploads/2019/07/CAUSALLY-MOTIVATED-ATTRIBUTION.pdf  
**Relevance:** Core  
**Priority:** 1

---

## Project Relevance

**(A)** Channel-level Shapley credits from \(P(\text{conv}\mid \mathbf{X})\); **path-ordered touch labels are not specified in source** as outputs for a ranker.

**(B)** Binary conversion; **continuous engagement is not specified in source.**

**(C)** Explicitly targets **confounding** between retargeting and prospecting via \(\Omega\); **user-activity-driven touch frequency** discussed qualitatively but **full IV/RDD treatment is not specified in source.**
