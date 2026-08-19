# Two-Sided Prioritized Ranking: A Coherency-Preserving Design for Marketplace Experiments

- **Source index:** 104
- **Source ID:** `dda900fd-af47-45b1-866d-5dcb66bcfaa9`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Authors:** Mahyar Habibi, Zahra Khanalizadeh, Negar Ziaeian
- **Affiliations:** Lyft; University of Washington; University of Warwick
- **Year / venue:** March 2026 indexed revision / arXiv preprint
- **Direction / priority:** D6 marketplace experimentation and interference / Priority 3
- **URL:** https://arxiv.org/abs/2502.09806

## 1. Summary

The paper proposes Two-Sided Prioritized Ranking (TSPR) for estimating the total effect of an item-side intervention when items shown in the same ranked list interfere. It preserves “coherency”: every user has the same catalog and sees the same treatment status for each item. Users and items are randomized, but ranking is changed so one user arm sees treated items prioritized and the other sees untreated items prioritized. Position bias creates different treatment exposure without changing prices or availability across users.

Semi-synthetic Monte Carlo experiments calibrate click and booking models to the public Expedia hotel-search dataset. TSPR substantially reduces bias and variance relative to item-level Bernoulli tests. Clean cluster randomization can have low bias but, with roughly 200 clusters versus 20,000 query-level units, has about eight times the standard deviation of TSPR’s parametric estimator. The paper describes the gain as roughly an order-of-magnitude reduction in standard deviation.

## 2. Experiment Critique

The estimand is policy-relevant—the contrast between globally treated and globally untreated worlds—and the design respects real operational constraints. Calibration to observed position and cascade behavior makes the simulation more realistic than a purely synthetic test.

The evidence is nevertheless simulation-based. Identification depends on strong position bias, treatment–attention separability, symmetric reranking distortion, slack supply, and short horizons. The paper explicitly notes that TSPR is not unbiased for the global effect. Treatment can itself change attention, aggressive prioritization can damage experience, and dynamic feedback or capacity constraints can invalidate the setup. No live platform experiment is reported.

## 3. Industry Contribution / Project Relevance

TSPR is unusually relevant to dating because ranking creates exposure while candidates compete for limited attention. It suggests an experiment in which a candidate-side policy is fixed coherently but its prominence differs across randomized viewer arms, allowing measurement under substitution without hiding candidates.

Important adaptations are required: dating supply is not slack, each candidate has attention capacity, outcomes are reciprocal, and repeated sessions create carryover. Reordering may also directly change match quality. TSPR is best viewed as a design pattern for policy evaluation, not the unified ranking objective itself. Pre-tests should quantify position bias, candidate overload, and experience distortion, and the estimand should include both sides’ retention and revenue.

## 4. Novelty

The distinctive idea is to use the ranking mechanism—not merely tolerate it—as the source of causal exposure variation while preserving item treatment consistency and full catalog access.

## 5. Dataset Availability

The Expedia Personalized Sort dataset is public on Kaggle. Simulation code availability is **Not specified in source**.

## 6. Community Reaction

Not specified in source.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## 8. Meta Information

- **Data domain:** Hotel-search marketplace
- **Outcomes:** Clicks, bookings, aggregate query outcome
- **Estimand:** Global treatment lift under interference
- **Design:** Two-sided user/item randomization plus prioritized reranking
- **Primary limitations:** Semi-synthetic evidence, residual bias, slack-supply and short-horizon assumptions
- **Project role:** Marketplace experiment design
