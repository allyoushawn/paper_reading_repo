# Paper Analysis: Inferring Causal Impact Using Bayesian Structural Time-Series Models

**Source:** https://arxiv.org/pdf/1506.00356.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Inferring Causal Impact Using Bayesian Structural Time-Series Models  
**Authors:** Kay H. Brodersen, Fabian Gallusser, Jim Koehler, Nicolas Remy, Steven L. Scott (Google)  
**Abstract:**  
Introduces **Bayesian structural time-series** counterfactual forecasting for market interventions: local linear trend + seasonality + regression on **donor/control** series with **spike-and-slab** covariate selection and **Zellner g-prior**; MCMC via Gibbs sampling with **Durbin–Koopman** simulation smoother. Posterior predictive draws yield pointwise and cumulative incremental effects. Released as **`CausalImpact`** R package.

**Key contributions:**
- Extends DiD thinking to full Bayesian dynamic trajectory with flexible components.
- Model averaging over controls and coefficients to reduce arbitrary control picking/overfitting.
- Empirical validation on Google advertiser geo experiment (95 treated vs 95 control DMAs) plus simulations.

**Methodology:**  
State-space observation + transition equations; counterfactual = forecast absent treatment; causal increments = observed minus counterfactual draws; cumulative effects for flow outcomes.

**Main results:**  
Geo ad campaign: cumulative lift ~88,400 clicks (+22% posterior mean) vs randomization-based linear model ~84,700 (<5% deviation); observational-controls variant using Google Trends covariates ~85,900 (~1% deviation). Simulations: power for large lifts; misses ≤1% lifts ~90% of time; structural break stress test degrades fits.

---

## 2. Experiment Critique

**Design:**  
Strong external anchor via randomized geo experiment; placebo on untreated regions shows ~2% non-significant lift.

**Statistical validity:**  
Bayesian predictive intervals (wider than classical CIs as expected). Coverage simulation ~nominal for campaign length per paper.

**Online experiments (if any):**  
Uses real randomized geo A/B as gold standard comparison.

**Reproducibility:**  
Public R package; empirical data not fully public per source.

**Overall:**  
Landmark applied methodology paper with careful stress tests; limitations on spillover, structural breaks, long post-period accuracy documented.

---

## 3. Industry Contribution

**Deployability:**  
Very high—standard tool for geo/campaign post-analysis when RCT imperfect or absent.

**Problems solved:**  
Quick counterfactual trajectories for launches, campaigns, feature flags on aggregate KPIs.

**Engineering cost:**  
Low for analysts comfortable with R; danger of misuse if parallel trends/spillover violated.

---

## 4. Novelty vs Prior Work

**Paper's claimed novelty:**  
Bayesian dynamic synthetic control with integrated uncertainty vs static DiD / convex synthetic control / pure regression.

**Prior work comparison:**  
Positions vs Abadie synthetic control, classical DD limitations (i.i.d. assumption, two-point DD), Belloni et al. lasso selection.

**Verification:**  
Widely adopted; empirical section matches randomized benchmark closely per source.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Simulated series | Generated in paper | Partial | Specs in paper |
| Google advertiser DMA experiment | Not public | No | Aggregated clicks |

**Offline experiment reproducible:**  
Simulations reproducible from spec; empirical panel not shared.

---

## 6. Community Reaction

No significant community discussion found.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** Kay H. Brodersen; Fabian Gallusser; Jim Koehler; Nicolas Remy; Steven L. Scott  
**Affiliations:** Google, Inc.  
**Venue:** The Annals of Applied Statistics (2015)  
**Year:** 2015  
**PDF:** downloaded (arXiv / IMS reprint)  
**Relevance:** Related  
**Priority:** 2

---

## Project Relevance

**Low project relevance.** Method targets **aggregate/market-level** time series (e.g., DMA-level clicks) for **discrete interventions**, explicitly in settings that **preclude individual exposure** measurement; it does **not** assign per-touchpoint credit across heterogeneous in-app interactions or produce user-level continuous days-active labels.

---

*[If datasets are accessible: To run experiments on these datasets, use the experiment-runner skill with the dataset URL or info above.]*
