# Paper Analysis: Modeling Delayed Feedback in Display Advertising

**Source:** https://arxiv.org/abs/1406.6035
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Modeling Delayed Feedback in Display Advertising
- **authors or company:** Olivier Chapelle (Criteo Labs)
- **venue:** KDD
- **year:** 2014
- **URL:** https://arxiv.org/abs/1406.6035
- **source type:** industry paper
- **direction:** D7
- **problem setting:** CPA display advertising; clicks arrive immediately but conversions delay days/weeks; fixed attribution window creates false negatives if training window is too short, or stale data if too long.
- **objective and label definition:** Post-click conversion probability \(p(x)\) and conversion delay \(\lambda(x)\); 30-day attribution window; last-click attribution; first conversion per click only.
- **prediction or incrementality:** Predicts absolute conversion probability; not causal uplift of ad exposure.
- **model architecture:** Joint probabilistic model: logistic regression for eventual conversion \(p(x)\) plus exponential hazard \(\lambda(x)=\exp(w_d\cdot x)\) for delay; trained via EM or joint L-BFGS on negative log-likelihood.
- **credit assignment:** Post-click attribution: conversion within 30 days mapped to clicked impression via shared user/advertiser ID; last-click wins; multiple conversions per click discarded (first kept).
- **training data and counterfactual handling:** Survival-analysis treatment of unobserved conversions as right-censored; EM E-step computes posterior \(w_i=\exp(-\lambda(x_i)e_i)p(x_i)\) for unlabeled clicks; no IPS/counterfactual correction.
- **offline and online evaluation:** Criteo retargeting logs (~6M examples per 3-week training window, 7 test days); NLL (not AUC—absolute probabilities matter for bidding). No online A/B reported.
- **reported gains:** Overall NLL 0.3960 vs Naive 0.4076 (~3% improvement); recent campaigns NLL 0.4006 vs Shifted 0.4176; Naive underpredicts conversions by 21%; DFM converges to true CVR after 2 days in toy simulation (mean delay 4 days).
- **applicability note for a two-sided dating recommender:** Foundational template for training on fresh clicks/matches while censoring not-yet-observed long-horizon outcomes (reply, retention, subscription).
  Maps to impression-level CPA bidding, not reciprocal matching or slate credit assignment—pair with ESMM/entire-space or two-stage OPE for dating rankers.
- **unverified claims:** none

## 1. Summary

Chapelle proposes the Delayed Feedback Model (DFM): jointly model whether a click will eventually convert (\(p(x)\)) and how long conversion takes (exponential delay \(\lambda(x)\)), treating unobserved conversions as censored survival data. This eliminates the need for a fixed matching window—fresh clicks enter training immediately while EM/L-BFGS adjusts for incomplete labels. Evaluated on Criteo CPA logs against Naive, Oracle, Shifted, Rescale, and STC baselines.

## 2. Experiment Critique

Strengths: large industrial dataset (publicly downloadable), NLL metric aligned with bidding use case, separate evaluation on recent/fast-changing campaigns. Weaknesses: exponential delay misfits diurnal patterns and short/long delay tails; non-convex objective with rate/delay ambiguity at low sample sizes; single-conversion attribution only; no online validation; one-sided ad setting.

## 3. Industry Contribution

Canonical production pattern for delayed CVR: ingest real-time clicks, censor pending conversions, retrain daily. Widely cited ancestor of ES-DFM, DEFUSE, ESDF streaming pipelines. Public Criteo dataset enabled a decade of follow-on work.

## 4. Novelty vs. Prior Work

Unifies conversion probability and delay in one likelihood; adapts survival analysis (Kalbfleisch & Prentice 2002) to display ads. Baselines: PU learning (Elkan & Noto 2008, Rescale), STC two-model heuristic, shifted training. Builds on Rosales et al. (2012), Lee et al. (2012) CVR estimation.

## 5. Dataset Availability

- **Criteo display advertising logs:** http://labs.criteo.com/tag/dataset

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

### (1) Ranking objective: retention / LTV / revenue vs CTR
CPA eCPM = CPA × Pr(click) × Pr(conversion|click). Retention/LTV: Not specified in source.

### (2) Credit assignment: user-level delayed outcome → item-level decision
Post-click 30-day last-click attribution to clicked impression; first conversion only.

### (3) Label and horizon definitions; delay, sparsity, censoring
30-day horizon; \(Y\)=observed conversion, \(C\)=eventual conversion (latent), \(D\)=delay, \(E\)=elapsed time. Censoring via survival analysis and EM posterior weights. Sparsity: Not specified in source.

### (4) Short vs long-term head fusion
Fixed multiplicative fusion: Pr(conversion,click)=Pr(click)×Pr(conversion|click). Within DFM, fixed joint \(p(x)\) and \(\lambda(x)\).

### (5) Prediction vs incrementality
Absolute outcome prediction; not incrementality.

### (6) Offline and online evaluation
Offline NLL on Criteo (rolling 3-week train, 7-day test). Online: Not specified in source.

### (7) Reciprocity, congestion, fairness, revenue vs match quality
Not specified in source.

### (8) Migration path from CTR-like model toward unified long-term model
Progression: Naive → Shifted (30-day lag) → Rescale (PU) → STC (1-day + ratio model) → DFM (joint survival model on fresh logs).

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Olivier Chapelle
**Affiliations:** Criteo Labs
**Venue:** KDD 2014
**Year:** 2014
**PDF:** https://arxiv.org/abs/1406.6035
**Relevance:** Core
**Priority:** 1
