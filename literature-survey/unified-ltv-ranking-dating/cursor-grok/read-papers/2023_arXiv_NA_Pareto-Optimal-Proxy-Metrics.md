# Survey Card

| Field | Value |
|-------|-------|
| **Title** | Pareto Optimal Proxy Metrics |
| **Authors** | Alessandro Zito, Dylan Greaves, Jacopo Soriano, Lee Richardson |
| **Venue** | arXiv (Google Inc.) |
| **Year** | 2025 |
| **Type** | Industry |
| **Survey Phase** | D3 — Surrogates / Evaluation |
| **NLM Source ID** | 0c4393ea-b677-42e2-8fa0-410244bffdcf |
| **PDF** | https://arxiv.org/pdf/2307.01000 |
| **One-line summary** | Multi-objective framework that learns linear composite proxy metrics balancing short-term sensitivity and long-term directional alignment with the north-star metric. |
| **Core mechanism** | Pareto front over auxiliary-metric weights; proxy score selects launch metric from non-dominated set. |

**Dating applicability:** Directly applicable for choosing which short-horizon experiment metrics (match rate, reply rate, 7-day return) best track delayed retention when gating ranking A/B launches. Gives a principled sensitivity–directionality trade-off instead of defaulting to the short-term north star alone.

---

# Paper Reader

## 1. Problem & Motivation

North-star metrics (here DAU) are central to launch decisions but are often insensitive in short experiments and can diverge from long-term impact due to novelty, user learning, and fatigue. Prior proxy-metric work optimizes prediction of long-term treatment effects but ignores the inverse relationship between short-term sensitivity and long-term directionality.

## 2. Method

**Proxy representation:** Linear combination of \(M\) auxiliary metrics:
\[Z_{i,j}(\omega) = \sum_{m=1}^M \omega_m X_{i,j,m}\]
where \(X_{i,j,m}\) is the percentage treatment–control difference for auxiliary metric \(m\) in experiment \(j\) across cookie buckets \(i\).

**Objectives (Pareto front):**
- **Sensitivity:** Binary Sensitivity (proportion of experiments with significant proxy effect) or Average Sensitivity (mean \(|t_j|\)).
- **Directionality:** MSE or correlation between proxy treatment effect \(\bar{Z}_j(\omega)\) and long-term north-star effect \(\bar{Y}_j\).

**Algorithms:** Randomized search (Algorithm 1) and constrained optimization via binning with DIRECT-L (Algorithm 2).

**Selection:** Proxy Score = (Detections − Mistakes) / (experiments where north star is significant), rewarding aligned significant reads and penalizing opposite-direction mistakes.

## 3. Evaluation

- **Training:** 300 historical experiments; north star = DAU; 30-day runs; long-term label = average DAU in last 7 days; 70 auxiliary metrics (subsets of \(M \in \{5,10,15\}\)).
- **Hold-out:** 500+ experiments over subsequent six months.
- **Baselines:** Short-term north star; Kriging (GPareto); randomized search.

## 4. Key Results

| Metric | Proxy | Short-term North Star |
|--------|-------|----------------------|
| Relative sensitivity | **8.5×** | 1× |
| Recall (when long-term NS significant) | **72%** | 40% |
| Precision | **1.0** | 1.0 |
| Proxy score | **0.72** | 0.41 |

Constrained binning outperforms Kriging at \(M=10,15\) on AUPF with faster runtime (<500s vs >1000s).

## 5. Limitations

- Does not estimate exact long-term effect size; anticipates direction/existence only.
- Assumes stable treatment-effect distribution; requires re-fit every 5–6 months.
- Directionality measured against noisy long-term north-star reads.
- Linear composites only; no nonlinear combinations.
- Proxy score fragile when north star is rarely significant.
- Randomized search inefficient at high \(M\).

## 6. Prior Work Cited

Deng & Shi (2016); Duan et al. (2021); Athey et al. (2019); Hohnhold et al. (2015); Dmitriev & Wu (2016); Chamandy et al. (2012); Drutsa et al. (2017).

---

# Project Relevance

**High relevance for D3 (surrogates/evaluation).** Operates at the experiment-decision layer above any ranking model: constructs composite proxies from historical A/B portfolios that balance detectability and long-term alignment. For dating: (1) weight multiple short-horizon metrics (matches, messages, returns) for launch gates; (2) avoid over-relying on insensitive retention reads in short tests; (3) monitor via cumulative long-term holdbacks. Incrementality (treatment effects), not outcome prediction. No credit assignment, ranking architecture, or two-sided market dynamics.

| # | Field | Answer |
|---|-------|--------|
| 1 | Ranking objective | Not a ranking model; experiment metric framework. North star = DAU; auxiliary metrics include engagement quality signals. |
| 2 | Credit assignment | Not specified in source. |
| 3 | Labels / horizon | 30-day experiments; long-term label = avg DAU last 7 days. Sparsity handled via sensitive auxiliary metrics. |
| 4 | Short/long fusion | Linear combination of auxiliary metrics via learned weights on Pareto front. |
| 5 | Prediction vs incrementality | Treatment effects (incrementality); not designed to estimate exact effect magnitude. |
| 6 | Offline / online eval | 300 train + 500+ hold-out experiments; cumulative long-term holdbacks for online monitoring. |
| 7 | Reciprocity / fairness | Not specified in source. |
| 8 | CTR → long-term migration | Not specified in source. |

---

# Reverse Citation Map

| This paper cites → | Notes |
|--------------------|-------|
| | |

| ← Cited by this survey | Notes |
|------------------------|-------|
| | |

---

# Meta Information

| Field | Value |
|-------|-------|
| **Card date** | 2026-08-16 |
| **Workplace** | cursor-grok |
| **Reader** | NotebookLM Q1–Q3 (source 0c4393ea-b677-42e2-8fa0-410244bffdcf) |
| **Community Reaction** | No significant community discussion found. |
