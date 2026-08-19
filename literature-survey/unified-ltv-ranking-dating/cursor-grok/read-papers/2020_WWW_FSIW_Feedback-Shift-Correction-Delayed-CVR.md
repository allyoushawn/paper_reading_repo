# Paper Analysis: A Feedback Shift Correction in Predicting Conversion Rates under Delayed Feedback

**Source:** https://arxiv.org/pdf/2002.02068.pdf
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** A Feedback Shift Correction in Predicting Conversion Rates under Delayed Feedback
- **authors or company:** Shota Yasui, Gota Morishita, Komei Fujita, Masashi Shibata (Cyberagent, Inc.)
- **venue:** WWW
- **year:** 2020
- **URL:** https://arxiv.org/abs/2002.02068
- **source type:** industry paper
- **direction:** D7
- **problem setting:** Display-ad CPA bidding requires accurate CVR, but training labels \(Y\) are gathered before conversions complete, causing feedback shift: \(P(Y|X) \neq P(C|X)\) while \(P(X)\) is unchanged.
- **objective and label definition:** Latent eventual conversion \(C \in \{0,1\}\); observed training label \(Y\); elapsed time \(E\) since click; delay \(D\); correct-label indicator \(S\); 30-day Criteo observation period; campaign-specific observational windows on Dynalyst (1–7 days).
- **prediction or incrementality:** Predicts absolute \(P(C=1|X)\) via consistent importance-weighted ERM—not incrementality.
- **model architecture:** Model-agnostic FSIW sample weights applied to any CVR model; FSIW estimated by LightGBM on counterfactual-deadline artificial data (Algorithm 1); FFMIW = FFM + FSIW weights.
- **credit assignment:** Post-click impression features \(X\) at click time; elapsed time \(e_i\) included as FSIW feature.
- **training data and counterfactual handling:** FSIW \(= P(C=y|X)/P(Y=y|X)\) decomposed into \(1/P(S=1|C=1,X)\) and \(1 - P(S=0,C=1|X)/P(Y=0|X)\); estimated via counterfactual deadline \(\tau\) (7 days on Criteo; campaign observational period on Dynalyst); weights applied as sample weights in LR/FFM training.
- **offline and online evaluation:** Criteo public logs (7 rolling 3-week train + 1-day test splits, 30-day test tracking); Dynalyst in-house (3 campaigns, 16 splits, 13-day train / 1-day val / 1-day test); metrics LL, PR-AUC, NLL. Online 14-day A/B on Campaign L (~1M impressions).
- **reported gains:** Criteo LR-FSIW: LL 0.3928 vs DFM 0.3989 (1.5% improvement, significant), NLL 28.02 vs 27.33 (2.5%, significant); training ~2.1h vs DFM ~140h. Dynalyst Campaign L FFMIW: NLL 2.304 vs FFM 1.7197 (significant). Online Campaign L: +31% conversions, +28% cost, −2% CPA (CPA not significant).
- **applicability note for a two-sided dating recommender:** Consistent-loss importance weighting for any ranker when fresh training data mislabels eventual matches as negatives—plug-in weights without changing base architecture.
  Ad CVR setting; no reciprocal match labels, multi-event-per-impression counts, or LTV horizons.
- **unverified claims:** none

## 1. Summary

FSIW frames delayed feedback as feedback shift (label distribution mismatch, not covariate shift) and proves importance-weighted ERM consistency. FSIW is estimated indirectly via counterfactual-deadline synthetic data and LightGBM models predicting correct-label probability from elapsed time and features. Demonstrated on logistic regression (Criteo) and FFM (Dynalyst) with large training-time savings vs DFM and statistically significant online gains on long-observation campaign.

## 2. Experiment Critique

Strengths: theoretical consistency proof; model-agnostic weights; 67× faster training than DFM on Criteo; online A/B validation. Weaknesses: PR-AUC not significantly better than DFM on Criteo; FFMIW gains significant only on Campaign L (longest observational window); counterfactual deadline choice somewhat ad hoc.

## 3. Industry Contribution

Production-tested at Dynalyst/Cyberagent; FSIW drops into existing FFM/LR pipelines as sample weights. Open Cython DFM comparison repo referenced.

## 4. Novelty vs. Prior Work

First feedback-shift framing with IW consistency proof. Compared to DFM (Chapelle 2014), non-parametric delay (Yoshikawa & Imai 2018), continuous-training FNW (Ktena et al. 2019). Does not allow positive label correction after deadline (unlike Defer).

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Criteo conversion logs | labs.criteo.com | Yes | 30-day observation |
| Dynalyst in-house | dynalyst.io | No | 3 campaigns |

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

### (1) Ranking objective: retention / LTV / revenue vs CTR
CVR point prediction for bidding.

### (2) Credit assignment: user-level delayed outcome → item-level decision
Click-time features with elapsed-time-aware FSIW.

### (3) Label and horizon definitions; delay, sparsity, censoring
Feedback shift with \(E < D\) mislabeling; counterfactual deadline simulates censoring.

### (4) Short vs long-term head fusion
Single CVR head with sample weights only.

### (5) Prediction vs incrementality
Absolute conversion probability.

### (6) Offline and online evaluation
LL/NLL on Criteo and Dynalyst; 14-day online A/B on Campaign L.

### (7) Reciprocity, congestion, fairness, revenue vs match quality
Not specified in source.

### (8) Migration path from CTR-like model toward unified long-term model
Add FSIW weights to any existing CVR ranker trained on fresh incomplete labels.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Shota Yasui, Gota Morishita, Komei Fujita, Masashi Shibata
**Affiliations:** Cyberagent, Inc.
**Venue:** WWW 2020
**Year:** 2020
**PDF:** https://arxiv.org/pdf/2002.02068.pdf
**Relevance:** Core
**Priority:** 2
