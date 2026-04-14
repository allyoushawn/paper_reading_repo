# Paper Analysis: Trimmed Match Design for Randomized Paired Geo Experiments

**Source:** https://arxiv.org/pdf/2105.07060.pdf  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** Trimmed Match Design for Randomized Paired Geo Experiments  
**Authors:** Aiyou Chen, Marco Longfils, Nicolas Remy (Google)  
**Abstract:**
This paper proposes Trimmed Match Design (TMD), a robust nonparametric method for designing randomized paired geo experiments to measure incremental Return On Ad Spend (iROAS). It extends the Trimmed Match estimation framework (Chen & Au 2022) by integrating optimal subset pairing and sample splitting (cross-validation) for reliable power analysis. The method handles the three core challenges of geo experiments: small number of geos, heavy-tailed revenue distributions, and temporal non-stationarity.

**Key contributions:**
- Optimal subset pairing: non-bipartite matching algorithm minimizing L1-loss Σ|Zi1−Zi2| to find the n geo pairs with smallest "uninfluenced response" differences
- Cross-validation for power analysis: split pretest data into pairing period (Tp) and evaluation period (Te) to avoid overfitting
- RMSE-based power evaluation via holdback simulation: generate 1000+ random treatment assignments on Te data, compute Trimmed Match estimate for each, report RMSE
- Rerandomization for balance: reject and redo geo assignments that fail balance checks
- Companion to Chen & Au (2022) Trimmed Match — handles the design phase; Chen & Au handles the estimation phase

**Methodology:**
Design procedure: (1) Split pretest into Tp (pairing) and Te (evaluation). (2) For each candidate n, compute distance matrix D_gg' ≈ |R1g − R1g'|^2 on Tp, run non-bipartite matching to find optimal n pairs. (3) Simulate holdback experiments on Te: assign treatment/control within each pair, generate incremental spend/response data under assumed iROAS θ, estimate Trimmed Match θ̂, compute RMSE over K=1000 replications. (4) Choose n minimizing RMSE subject to marketing constraints. (5) Rerandomize to ensure balance checks pass.

**Main results:**
Simulation (N=100 geos, 6 weeks): reducing n from 50 to 45 pairs cuts RMSE by ~50%. Trimmed Match vs permutation test: 2× RMSE reduction at n=50 for log-normal data. Real case study (Nielsen 210 DMAs, 1+ year revenue data, Pareto-distributed — 80% revenue from 20% geos): optimal pairing reduces RMSE by factor 3 vs rank-based pairing. Real experiment post-analysis: 80% CI half-width matches 1.28×RMSE predicted at design time.

---

## 2. Experiment Critique

**Design:**
Two evaluations: (1) synthetic simulation with 5000 replicates of 100-geo lognormal data (fully reproducible), (2) real case study with Nielsen DMA data (proprietary). Comparison against permutation test baseline and rank-based pairing.

**Statistical validity:**
The cross-validation requirement (separate pairing and evaluation periods) is proven necessary by the overfitting comparison — RMSE is systematically lower when using the same period for pairing and evaluation. The real experiment post-analysis confirms theoretical predictions. SUTVA violation with fixed budget is honestly acknowledged.

**Online experiments (if any):**
The real case study is an actual deployed geo experiment (not online in the A/B sense, but field experiment).

**Reproducibility:**
Simulation fully reproducible from paper. Real data proprietary. The open-source `trimmed_match` Python package implements both the design and estimation.

**Overall:**
Strong companion paper to Chen & Au (2022). The cross-validation insight for experimental design is genuinely novel (cross-validation is standard in ML model fitting but not in experimental design). The paper is honest about limitations (SUTVA violation, rerandomization open problems).

---

## 3. Industry Contribution

**Deployability:**
Very high. The `trimmed_match` Python package is open source. Google authorship implies production deployment. The design procedure has three straightforward steps that any data scientist can implement.

**Problems solved:**
For dating platform retention experiments: the Trimmed Match Design framework is the right tool for designing geo-level or cohort-level experiments where the number of units is small (e.g., cities, demographic cohorts, device types). The optimal pairing algorithm reduces confounding between cohorts. The cross-validation insight prevents overpowered experiment designs that fail in practice.

**Engineering cost:**
Low. The non-bipartite matching is a standard operations research algorithm. The power simulation requires running the Trimmed Match estimator K=1000 times on historical data — fast on modern hardware. The `trimmed_match` package handles all of this.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**
First application of cross-validation to experimental design (not model fitting); first integration of optimal non-bipartite matching with Trimmed Match estimation for geo experiment design; first nonparametric iROAS design method.

**Prior work comparison:**
Chen & Au (2022) Trimmed Match: established robust estimation, but not the design procedure; Vaver & Koehler (2011) GBR: parametric, sensitive to regression weight choice; Kerman et al. (2017) TBR / Brodersen et al. (2015) Bayesian structural time series: synthetic control approaches requiring untestable assumptions.

**Verification:**
Claims verified. The RMSE improvement results are reproducible. Real experiment confirmation of the theoretical RMSE prediction is a strong validation.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Synthetic Simulation | Fully described | Yes | N=100 lognormal geos, 6 weeks |
| Nielsen DMA Data | Proprietary | No | 210 DMAs, 1+ year daily revenue |

**Offline experiment reproducibility:**
Fully reproducible for simulation. Real case study data proprietary.

---

## 6. Community Reaction

arXiv 2021, Google. ~50 citations. Directly companion to the highly-cited Trimmed Match paper (Chen & Au 2022). The open-source `trimmed_match` package has seen industry adoption. The cross-validation for experimental design insight is cited in subsequent geo experiment papers.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** Aiyou Chen, Marco Longfils, Nicolas Remy  
**Affiliations:** Google LLC  
**Venue:** arXiv 2021 (Google)  
**Year:** 2021  
**PDF:** https://arxiv.org/pdf/2105.07060.pdf  
**Relevance:** Core  
**Priority:** 3
