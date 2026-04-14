# Paper Analysis: Toward Improving Digital Attribution Model Accuracy

**Source:** https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45766.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Toward Improving Digital Attribution Model Accuracy  
**Authors:** Stephanie Sapp, Jon Vaver (Google Inc.)  
**Abstract:** Argues matched-pairs data-driven attribution (DDA) implicitly assumes ads only shift immediate conversion propensity and do not change post-exposure browsing; matching on downstream events therefore bakes in post-treatment paths. Introduces **Upstream DDA (UDDA)**, aligned with Rubin’s framework, that matches only the pre-exposure prefix and compares conversion rates of exposed vs unexposed users sharing the same upstream history at the exposure index. Evaluates on DASS simulations with virtual-experiment ground truth.

**Key contributions:**
- Clear causal critique of downstream-conditioned DDA / discrete-choice formulations.
- UDDA algorithm aggregating incremental rate differences per unique upstream path.
- Discussion of residual biases: censored never-observed users, browsing dissimilarity, targeting.

**Methodology:** DASS = non-stationary Markov browsing + ad serving + ad impact modules; compare DDA vs UDDA vs “UDDA all users” oracle for censored visibility.

**Main results:** When ads change browsing (not only p(conversion)), matched-pairs DDA flatlines attributed conversions vs true incremental curve; UDDA tracks shape but has fixed bias without censored-user visibility; with full visibility UDDA recovers truth in the two primary scenarios.

---

## 2. Experiment Critique

**Design:** Simulation-only (no public real path benchmark with known causal graph).

**Statistical validity:** Virtual A/B (ads off) gives credible incremental ground truth inside simulator; stresses MNAR censoring and comparability failures.

**Online experiments (if any):** Not specified in source.

**Reproducibility:** DASS described in companion pub; this PDF is self-contained on UDDA steps.

**Overall:** Foundational measurement paper for *path-consistent* incremental credit at event indices; not a neural MTA trainer.

---

## 3. Industry Contribution

**Deployability:** High conceptual value for any DDA vendor; depends on having comparable unexposed controls per upstream prefix.

**Problems solved:** Separates incremental ad effect from post-exposure path distortion.

**Engineering cost:** Requires careful cohort construction and handling invisible users.

---

## 4. Novelty vs. Prior Work

Builds on DASS (Sapp et al. 2016), Reiley et al. field experiments vs PBA, Shapley-based DDA exposition, Gelman & Hill on conditioning, Rubin causal model.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| DASS simulations | Referenced companion | Partial | Parameters in appendix |

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

**Authors:** Stephanie Sapp, Jon Vaver  
**Affiliations:** Google Inc.  
**Venue:** Google technical report / marketing science stream (PDF dated work ~2016)  
**Year:** 2016  
**PDF:** https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45766.pdf  
**Relevance:** Core  
**Priority:** 1

---

## Project Relevance

**(a) Per-touchpoint fractional credit:** Yes at the level of **event indices** on paths—UDDA assigns credit from upstream-matched exposed vs unexposed conversion-rate differences; aggregation to channel totals is explicit. Using those credits as *supervised labels* for a second-stage model is not specified in source.

**(b) Continuous outcomes:** Not specified in source.

**(c) Selection / heterogeneity:** Detailed discussion of MNAR censoring, browsing dissimilarity, and targeting bias for exposed vs unexposed pools.

**(d) Incrementality:** Central—evaluation is against virtual-experiment incremental conversions, not correlational fit alone.
