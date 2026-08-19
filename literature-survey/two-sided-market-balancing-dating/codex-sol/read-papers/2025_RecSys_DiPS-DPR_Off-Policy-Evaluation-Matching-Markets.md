# Paper Analysis: Off-Policy Evaluation and Learning for Matching Markets

**Source:** https://arxiv.org/abs/2507.13608  
**Date analyzed:** 2026-08-19

---

## 1. Summary

**Title:** Off-Policy Evaluation and Learning for Matching Markets  
**Authors:** Yudai Hayashi, Shuhei Goda, Yuta Saito  
**Abstract:** Reciprocal matching produces extremely sparse final rewards because both sides must act positively. DiPS and DPR use the denser first-stage action together with a modeled conditional response to reduce off-policy estimator variance and support offline policy learning.

**Key contributions:**

- Formalizes off-policy evaluation and learning for two-stage reciprocal matches.
- Introduces DiPS and DPR estimators that combine propensity weighting with intermediate and modeled rewards.
- Extends both estimators to policy-gradient learning and validates them on synthetic and industrial job-matching logs.

**Methodology:** A sender action s and conditional receiver response r yield match m=s·r. DiPS propensity-weights s and multiplies it by a regression estimate of response probability. DPR adds a direct match-probability baseline and correction term. Policy-gradient variants optimize target policies offline.

**Main results:** On Wantedly Visit logs with 21,736 companies, 17,460 job seekers, and 1.2% match sparsity, DPR has the lowest mean squared error across almost all sample sizes. DiPS and IPS nevertheless have lower policy-selection error than DPR and DR. Synthetic studies show DiPS/DPR remain more stable as sample size, action space, sparsity, and policy divergence change.

## 2. Experiment Critique

**Design:** Synthetic experiments vary sample size, action count, sparsity, and target-policy divergence; real A/B logs are repeatedly subsampled at 2,000, 5,000, and 8,000 companies. Standard direct, IPS, and doubly robust estimators are appropriate baselines.

**Statistical validity:** Real-data evaluation repeats sampling 20 times. Curves show variability bands, but exact confidence levels and experiment duration are not specified in source. The observed MSE-versus-selection-error reversal is an important negative result.

**Online experiments:** The source uses historical A/B logs for offline validation; it does not report a new online launch experiment.

**Reproducibility:** Synthetic setup and estimators are described. Public code and proprietary data access are not specified in source.

**Overall:** Evidence supports variance reduction and better synthetic learning performance. Regression error introduces bias, error correlations matter, and lower MSE does not guarantee better policy selection.

## 3. Industry Contribution

**Deployability:** Requires logged action propensities plus first-stage and receiver-response labels; compatible with daily batch or offline evaluation pipelines.

**Problems solved:** High-variance offline evaluation when final reciprocal matches are rare.

**Engineering cost:** Moderate: propensity logging, two reward models, overlap diagnostics, and policy-selection calibration.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** The first OPE/OPL formulation that explicitly exploits intermediate actions in reciprocal matching markets.

**Prior work comparison:** Dudík et al. (2014) supplies doubly robust evaluation; Gilotte et al. (2018) studies offline recommender A/B testing; Saito and Joachims (2021) reviews counterfactual recommendation; Bembom and van der Laan (2008), Kiyohara et al. (2024), and Su et al. (2020) study OPE risk and estimator choice; Pizzato et al. (2010) provides reciprocal-recommendation context.

**Verification:** Based on the source-scoped related work only.

## 5. Dataset Availability

**Datasets mentioned:**

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Wantedly Visit A/B logs | https://www.wantedly.com | No | 21,736 companies, 17,460 job seekers, 1.2% final reward. |
| Synthetic reciprocal-matching data | Not specified in source | No packaged data specified | 10-dimensional contexts with tunable sparsity. |

**Offline experiment reproducibility:** Formulas and synthetic design are available, but code and proprietary logs are not specified in source.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Exact mechanism:** Decompose a dating outcome into outbound like, conditional like-back, and final match. Apply propensity weights to the denser outbound action and model the receiver response rather than weighting only the sparse final match.

**Metrics and reported effect:** On logs with a 1.2% final match rate, DPR has significantly lower mean squared error than standard estimators across almost all sample sizes. DiPS and IPS have lower policy-selection error than DPR and DR.

**Capacity/congestion relevance:** Reciprocal match formation is explicit. Marketplace interference, receiver capacity, inbox congestion, match distribution, wasted likes, and retention are not specified in source.

**Practical mapping:** Use DiPS/DPR for offline comparison of reciprocal scoring policies, but add capacity features and do not treat OPE as a substitute for interference-aware market experiments.

**Dating fit: High.** The like-to-like-back-to-match funnel maps directly to dating, and the method targets sparse reciprocal rewards.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| No verified inbound mentions within the 45-source corpus. | — | — |

## Meta Information

**Authors:** Yudai Hayashi, Shuhei Goda, Yuta Saito  
**Affiliations:** Wantedly; independent researcher; Cornell University  
**Venue:** RecSys  
**Year:** 2025  
**PDF:** available  
**Relevance:** Core  
**Priority:** 1

## Annotated Bibliography Fields

- **Title:** Off-Policy Evaluation and Learning for Matching Markets
- **Authors/organization:** Yudai Hayashi, Shuhei Goda, Yuta Saito; Wantedly, independent, Cornell
- **Year:** 2025
- **Venue/type:** RecSys; reciprocal-matching OPE/OPL research
- **Link:** https://arxiv.org/abs/2507.13608
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Modeled a reciprocal match as an outbound request followed by a conditional response, then proposed DiPS and DPR estimators that combine logged propensities with the denser first-stage label and modeled reply probability. Policy-gradient versions optimize recommendations offline. Synthetic tests and Wantedly job-matching logs compare direct, IPS, and doubly robust baselines.
- **Mechanism relevant to two-sided balancing (≤50 words):** Evaluate reciprocal policies through separate like and like-back stages, using propensity weighting only on the denser first action and regression for receiver response. This stabilizes sparse match evaluation but does not model capacity or interference.
- **Metrics and reported effect:** On 21,736 companies and 17,460 job seekers with 1.2% matches, DPR has the lowest MSE; DiPS and IPS have lower policy-selection error than DPR and DR.
- **Dating-app fit:** High — the two-stage reward exactly matches like and like-back, though market-health effects require live interference-aware tests.
- **Confidence:** High — primary RecSys paper with industrial logs; proprietary data and no public code limit replication.
