# Paper Analysis: Customer Lifetime Value Prediction Using Embeddings

**Source:** https://arxiv.org/pdf/1703.02596.pdf
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** Customer Lifetime Value Prediction Using Embeddings
- **authors or company:** Benjamin Paul Chamberlain, Ângelo Cardoso, C.H. Bryan Liu, Roberto Pagliari (ASOS); Marc Peter Deisenroth (Imperial College London)
- **venue:** KDD 2017
- **year:** 2017
- **URL:** https://arxiv.org/pdf/1703.02596.pdf
- **source type:** industry paper
- **direction:** D4
- **problem setting:** Production CLTV and churn system at ASOS e-commerce: daily per-customer forecasts of net spend and churn risk for marketing allocation and retention.
- **objective and label definition:** CLTV = net sales minus returns over next 12 months; churn = no order in past year; training labels from disjoint prior-year window (Figure 1); model predicts CLTV percentiles then maps to monetary values via calibration trees.
- **prediction or incrementality:** Outcome prediction only; no treatment/uplift framing.
- **model architecture:** Deployed: Spark ML pipeline with 132 handcrafted features → calibrated Random Forest (churn classifier + CLTV percentile regressor); experimental: SkipGram-with-negative-sampling customer embeddings from product-view sequences (window 11) concatenated to RF; hybrid logistic+DNN explored for churn.
- **credit assignment:** Customer-level annual net spend; features from demographics, purchases, returns, and session logs over prior 12 months—no per-impression attribution.
- **training data and counterfactual handling:** Daily retrain on ~10M+ customers; strict train/label period disjointness to prevent leakage; observational supervised learning only.
- **offline and online evaluation:** Offline: churn AUC 0.798 (calibrated); CLTV Spearman 0.56 all customers, 0.46 excluding zeros; embedding AUC uplift on 20K-customer test sets (Figure 8). Live system serves business stakeholders; no randomized experiment numbers reported.
- **reported gains:** Session-log embeddings significantly improve churn AUC over handcrafted-only RF (Figure 8; best hidden dim 32–128); hybrid DNN beats logistic regression on churn but did not exceed RF within affordable compute (Figures 9–11).
- **applicability note for a two-sided dating recommender:** Foundational D4 reference for label horizon design (12-month net value), calibration, and leakage-safe train/label windows.
- **applicability note for a two-sided dating recommender:** Customer-level e-commerce CLTV—not reciprocal match ranking; embedding warm-start trick is session-specific.
- **unverified claims:** none

## 1. Summary

ASOS describes a large-scale production CLTV system using calibrated random forests on 132 handcrafted features, then shows unsupervised customer embeddings from browsing sequences (SGNS over co-viewing customers per product) improve churn prediction when added to the RF. Discusses deployment architecture (Azure blob, Spark, TensorFlow embeddings) and the permutation problem when embedding dimensions are unlabeled across train/live periods (solved via warm-start initialization).

## 2. Experiment Critique

Rich production detail and calibration methodology often omitted in academic LTV papers. Embedding experiments on subsamples (20K–50K customers); DNN cost analysis honest about commercial non-viability vs RF. No rigorous online uplift of embedding-augmented model reported at publication time ("working to incorporate").

## 3. Industry Contribution

Cornerstone personalized marketing system at ASOS (12.5M active customers at writing). Emphasizes calibration (logistic on RF churn probs; decision tree percentile→value mapping) so aggregated predictions match realized distributions.

## 4. Novelty vs. Prior Work

Extends Vanderveld et al. (KDD 2016) engagement-based CLTV with learned session embeddings (item2vec/prod2vec lineage). Customer-level (not product-level) embeddings for long-horizon forecasting with fast catalogue turnover.

## 5. Dataset Availability

Proprietary ASOS customer data; not public.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

High value as **D4 foundational** for **Q3**: 12-month net-spend label, churn coupling, percentile regression + calibration, and strict temporal label/feature separation—directly relevant when defining dating retention/LTV horizons and offline training protocols. Embeddings from behavioral sequences inform **Q8** (richer features before end-to-end LTV). No ranking, incrementality, or two-sided market content (**Q2, Q5, Q7** weak).

| # | Field | Answer |
|---|-------|--------|
| 1 | Ranking objective | Not specified in source—customer value regression, not feed ranking. |
| 2 | Credit assignment | Customer-level 12-month net spend from aggregated features. |
| 3 | Labels / horizon | 12-month net spend; churn if no order in past year; disjoint label/feature windows; percentile then calibrated mapping. |
| 4 | Short/long fusion | Separate churn classifier and CLTV percentile regressor with calibration stage. |
| 5 | Prediction vs incrementality | Predicts future spend/churn probability; not causal effect of interventions. |
| 6 | Offline / online eval | Offline AUC/Spearman; daily production scoring; no A/B metrics in source. |
| 7 | Reciprocity / fairness | Not specified in source. |
| 8 | CTR → long-term migration | Add learned session embeddings to existing RF pipeline before full neural replacement. |

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Benjamin Paul Chamberlain, Ângelo Cardoso, C.H. Bryan Liu, Roberto Pagliari, Marc Peter Deisenroth
**Affiliations:** ASOS.com; Imperial College London
**Venue:** KDD 2017 (Halifax)
**Year:** 2017
**PDF:** https://arxiv.org/pdf/1703.02596.pdf
**Relevance:** Related
**Priority:** 3
