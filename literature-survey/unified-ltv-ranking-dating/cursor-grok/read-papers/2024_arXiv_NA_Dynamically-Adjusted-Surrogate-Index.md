# Survey Card

| Field | Value |
|-------|-------|
| **Title** | Estimating the Long-Term Effects of Novel Treatments: The Dynamically Adjusted Surrogate Index |
| **Authors** | Keith Battocchi, Eleanor Dillon, Maggie Hei, Greg Lewis, Miruna Oprescu, Vasilis Syrgkanis (Microsoft Research) |
| **Venue** | NeurIPS 2021 |
| **Year** | 2021 |
| **Type** | Academic |
| **Survey Phase** | D3 — Surrogates / Evaluation |
| **NLM Source ID** | 2a94d6c3-3337-4a8c-af75-1733f35e8e77 |
| **PDF** | https://arxiv.org/pdf/2103.08390.pdf |
| **One-line summary** | Extends Athey et al. surrogate index by dynamically adjusting long-term outcomes to remove bias from auto-correlated future treatments, then combines with double ML for novel multi-treatment causal estimation. |
| **Core mechanism** | (1) Lewis & Syrgkanis recursive adjustment removes future-treatment contamination from historical outcomes; (2) ML surrogate model maps short-term proxies → adjusted long-term index; (3) DML on experimental short-run data estimates novel treatment effects with valid CIs. |

**Dating applicability:** When ranking experiments assign repeated treatments over weeks (boosts, notification pushes), standard short-term surrogate indices can overstate retention lift — DASI adjusts for dynamic policy bias before gating ranking launches.
**Dating applicability:** Customer-investment econometric setting with no ranking model, item credit assignment, or two-sided reciprocity — methodology transfers to experiment analysis, not ranker training.

---

# Paper Reader

## 1. Problem & Motivation

Firms need long-term causal effects of novel treatments but only have short-term experimental data. Standard surrogate indices (Athey et al. 2020) break under dynamic treatment policies: auto-correlated future treatments inflate surrogate predictions, biasing estimated effects upward.

## 2. Method

**Setting:** Customers receive treatment vectors \(T_{i,t}\) each period; observe features \(X_{i,t}\), short-term surrogates \(S_{i,t}\), and M-period cumulative outcome \(\bar{Y}_{i,t}\).

**Standard surrogate index (biased under dynamics):**
\[
\hat{g}(S_{i,t}, X_{i,t}) \approx E[\bar{Y}_{i,t} \mid S_{i,t}, X_{i,t}]
\]

**Dynamic adjustment (Lewis & Syrgkanis 2020):** Estimate \(\bar{Y}^{adj}_{i,t}\) = expected cumulative outcome assuming no further treatments over next M periods. Train adjusted surrogate model \(g^{adj}_0(S_{i,t}, X_{i,t}) := E[\bar{Y}^{adj}_{i,t} \mid S_{i,t}, X_{i,t}]\).

**Pipeline combines:**
1. Surrogate index (Athey et al. 2020)
2. Double/debiased machine learning (Chernozhukov et al. 2018)
3. Dynamic treatment effect estimation (Lewis & Syrgkanis 2020)

Supports multiple continuous treatments (not just binary) with root-n asymptotically normal estimates under Markovian assumptions.

## 3. Evaluation

- **Data:** Semi-synthetic panel from major corporate customer-investment dataset (3-year real moments preserved).
- **Simulation:** 100 simulated datasets; compare direct DML on raw outcomes vs unadjusted surrogate vs adjusted surrogate vs adjusted raw outcomes.
- **Horizons:** 4-period and 8-period cumulative outcomes; varying sample sizes.

## 4. Key Results

| Method | Bias under auto-correlated treatments |
|--------|--------------------------------------|
| Direct DML on raw \(\bar{Y}\) ("total") | **Substantial overestimate** of true effects |
| Unadjusted surrogate index | **Still biased** (slightly less than direct) |
| Adjusted raw outcomes (Lewis & Syrgkanis) | **Significantly less bias** at larger samples |
| **Adjusted surrogate index** | **Comparable accuracy to raw long-term outcomes**; works for novel treatments absent from adjustment training |

Qualitative finding: adjusted surrogate approach recommended when treatments are serially correlated and no single dataset contains both long-term outcomes and all treatments of interest.

## 5. Limitations

- Markovian assumption on data and observational policy.
- Surrogacy assumption: causal path from treatment to outcome must pass through observed short-term proxies.
- Comparability assumption: surrogate–outcome mapping stable across historical and projection periods.
- Semi-synthetic evaluation only; no live production A/B deployment reported.
- No ranking, reciprocity, or item-level attribution.

## 6. Prior Work Cited

Athey et al. (2020) surrogate index; Chernozhukov et al. (2018) double ML; Lewis & Syrgkanis (2020) dynamic treatment effects; Prentice (1989) surrogacy; Robins structural nested models.

---

# Project Relevance

**High relevance for D3 (surrogates/evaluation) and Q6.** Addresses a failure mode of surrogate-index gating when treatment policies are dynamic — relevant if dating platforms run overlapping experiments or auto-correlated engagement campaigns. Does not inform Q1–Q2 (ranking objective / item credit) or Q7 (two-sided markets).

| # | Field | Answer |
|---|-------|--------|
| 1 | Ranking objective | Not specified in source (causal inference for treatment effects on customer outcomes). |
| 2 | Credit assignment | Not specified in source (customer-period level, not item impressions). |
| 3 | Labels / horizon | M-period cumulative outcome \(\bar{Y}_{i,t}\); short-term surrogates \(S_{i,t}\); few months of proxies vs M-period outcomes. |
| 4 | Short/long fusion | Statistical surrogate index (ML mapping proxies → adjusted long-term projection), not neural multi-head fusion. |
| 5 | Prediction vs incrementality | Estimates average treatment effects on long-term outcomes via causal inference; not per-user outcome ranking. |
| 6 | Offline / online eval | Semi-synthetic simulation (100 replicates); no production online experiment. |
| 7 | Reciprocity / fairness | Not specified in source. |
| 8 | CTR → long-term migration | Evaluation methodology for shortening experiment read windows under dynamic policies; not a ranker migration path. |

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
| **Reader** | PDF/URL fallback — arxiv:2103.08390 (NLM RESOURCE_EXHAUSTED) |
| **Community Reaction** | No significant community discussion found. |
