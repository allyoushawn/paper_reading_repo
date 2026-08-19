Date: 2026-08-19

# Two-Sided Market Balancing in Dating-App Recommendation — Executive Summary

The 45-source review supports a market layer above single-viewer ranking: estimate mutual interest, account for scarce recipient attention, allocate exposure across the market, and evaluate matches, conversations, distribution, and retention under interference; 39/45 sources (86.7%) are industry or applied field evidence, but no study yet validates this entire chain in one dating system.

## Design Patterns

1. **Score both directions before spending exposure:** harmonic bilateral scoring nearly doubled offline success-at-10 over unilateral recommendation in Pizzato et al., *Recommending People to People: The Nature of Reciprocal Recommenders with a Case Study in Online Dating* (2013).
2. **Budget recipient attention explicitly:** receiver-level caps on expected inbound likes or dates improved congestion-adjusted dating outcomes in a two-region field study, although messaging did not rise, in Sekiya et al., *Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach* (2026).
3. **Redistribute predicted overdelivery with relevance guardrails:** a LinkedIn experiment shifted applications 6.5% toward underserved jobs and 8.7% away from overserved jobs while total applications changed nonsignificantly in Borisyuk et al., *LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace* (2017).
4. **Use market-wide scarcity adjustments when pair scores create superstar congestion:** equilibrium outside-option factors improved expected matches and reduced concentration on dating data in Tomita et al., *Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets* (2023).
5. **Treat product rules as market-design instruments:** a scarce virtual rose raised acceptance by 3.3 percentage points in Lee and Niederle, *Propose with a Rose? Signaling in Internet Dating Markets* (2015).
6. **Count distinct reciprocal outcomes rather than independent top-k hits:** vacant-slot reranking improved whole-set reciprocal coverage on dating and recruitment data in Yang et al., *Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method* (2024).
7. **Randomize interacting substitutes together:** cluster randomization removed 19.76% of an individual-level estimate in one Airbnb pricing meta-experiment, demonstrating treatment-specific—not universal—interference risk in Holtz et al., *Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization: Evidence from a Pricing Meta-Experiment on Airbnb* (2025).

## Most Fundamental Methods

These are the finalized tracker’s top five lineage/reuse methods, not a product-priority ranking; incompatible datasets and outcomes leave every cross-paper performance-consistency score unestablished.

1. **Dual-Perspective Graph Neural Network — 8:** separates outgoing taste from incoming appeal and is a recurring direct baseline; Yang et al., *Modeling Two-Way Selection Preference for Person-Job Fit* (2022).
2. **Transferable-Utility reciprocal ranking — 8:** joins bilateral preference with market-clearing demand pressure; Tomita et al., *Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets* (2023).
3. **RECON harmonic reciprocal scoring — 6:** supplies a simple dating-tested bilateral aggregation rule; Pizzato et al., *Recommending People to People: The Nature of Reciprocal Recommenders with a Case Study in Online Dating* (2013).
4. **Exposure-fair probabilistic ranking — 6:** provides the canonical constrained-exposure primitive; Singh and Joachims, *Fairness of Exposure in Rankings* (2018).
5. **Personalized reciprocal weighted-harmonic aggregation — 6:** tunes sender-versus-recipient importance and has one independent industry reproduction; Kleinerman et al., *Optimally Balancing Receiver and Recommended Users’ Importance in Reciprocal Recommender Systems* (2018).

## Recommendations for the Dating Recommender

- Calibrate the full view→like→like-back→conversation funnel separately by side, and report reciprocal coverage rather than only swipe accuracy, following Yang et al., *Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method* (2024).
- Define operational capacity as reply bandwidth, concurrent conversations, or expected productive interactions, then monitor demand-to-capacity by recipient and segment before selecting an allocation lever, informed by Borisyuk et al., *LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace* (2017).
- Evaluate exposure budgets or pacing with relevance guardrails, and test scarce signals, like limits, curated batches, and initiation rules separately because their welfare effects depend on imbalance and screening costs, as shown by Arnosti et al., *Managing Congestion in Matching Markets* (2021).
- Use a market-health scorecard containing total matches and conversations, share of users with at least one, Gini/Lorenz spread, unrequited or wasted likes, effective interactions, and retention on both sides; OkCupid, *Your Looks and Your Inbox* (2009), supports concentration diagnosis but not causal redistribution claims.
- Match the experiment design to spillover structure—two-sided randomization, competitive-neighborhood clustering, or regional/time switchbacks—and use reciprocal off-policy evaluation only for screening, guided by Johari et al., *Experimental Design in Two-Sided Platforms: An Analysis of Bias* (2022).

## Evidence Limits

Most effects come from jobs, lodging, spot work, offline replay, theory, or small regional tests; heterogeneous capacity definitions and outcomes preclude pooled effect sizes, and the selected 45-source bibliography is within the authoritative 30–50 target while evidence remains uneven across directions and domains.
