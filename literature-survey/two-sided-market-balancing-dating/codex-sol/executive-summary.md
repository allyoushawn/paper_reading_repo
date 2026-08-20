Date: 2026-08-19

# Two-Sided Market Balancing in Dating-App Recommendation — Executive Summary

The 45-source review supports a market layer above single-viewer ranking: estimate mutual interest, account for scarce recipient attention, allocate exposure across the market, and evaluate market health under interference. Industry and applied evidence comprise 39/45 sources (86.7%), but no study validates this entire chain in one dating system.

## Design Patterns

1. **Score both directions:** harmonic bilateral scoring nearly doubled offline success-at-10 in Pizzato et al., *Recommending People to People: The Nature of Reciprocal Recommenders with a Case Study in Online Dating*, UMUAI 2013.
2. **Budget recipient attention:** receiver-level caps improved congestion-adjusted dating outcomes, though messaging did not rise, in Sekiya et al., *Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach*, arXiv 2026.
3. **Redistribute overdelivery with relevance guardrails:** LinkedIn shifted applications 6.5% toward underserved jobs and 8.7% away from overserved jobs in Borisyuk et al., *LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace*, KDD 2017.
4. **Apply market-wide scarcity adjustments:** equilibrium outside-option factors improved expected matches and reduced concentration in Tomita et al., *Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets*, RecSys 2023.
5. **Use product rules as market-design instruments:** a scarce virtual rose raised acceptance by 3.3 percentage points in Lee and Niederle, *Propose with a Rose? Signaling in Internet Dating Markets*, Experimental Economics 2015.
6. **Count distinct reciprocal outcomes:** vacant-slot reranking improved whole-set reciprocal coverage in Yang et al., *Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method*, KDD 2024.
7. **Randomize interacting substitutes together:** cluster randomization removed 19.76% of an individual-level estimate in Holtz et al., *Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization: Evidence from a Pricing Meta-Experiment on Airbnb*, Management Science 2025.

## Most Fundamental Methods

These tracker leaders measure lineage and reuse, not product priority; incompatible outcomes prevent cross-paper performance comparison.

1. **Dual-Perspective Graph Neural Network — 8:** separates outgoing taste from incoming appeal; Yang et al., *Modeling Two-Way Selection Preference for Person-Job Fit*, RecSys 2022.
2. **Transferable-Utility reciprocal ranking — 8:** combines bilateral preference with market-clearing pressure; Tomita et al., *Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets*, RecSys 2023.
3. **RECON harmonic scoring — 6:** provides a simple dating-tested bilateral rule; Pizzato et al., *Recommending People to People: The Nature of Reciprocal Recommenders with a Case Study in Online Dating*, UMUAI 2013.
4. **Exposure-fair probabilistic ranking — 6:** supplies the canonical constrained-exposure primitive; Singh and Joachims, *Fairness of Exposure in Rankings*, KDD 2018.
5. **Personalized weighted-harmonic aggregation — 6:** tunes sender-versus-recipient importance; Kleinerman et al., *Optimally Balancing Receiver and Recommended Users’ Importance in Reciprocal Recommender Systems*, RecSys 2018.

## Recommendations

- Calibrate view→like→like-back→conversation separately by side and report reciprocal coverage, following Yang et al., *Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method*, KDD 2024.
- Define capacity as reply bandwidth, concurrent conversations, or productive interactions; monitor demand-to-capacity before intervention, informed by Borisyuk et al., *LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace*, KDD 2017.
- Test exposure budgets, like limits, curated batches, signaling, and initiation rules separately because welfare effects depend on imbalance and screening costs, as shown by Arnosti et al., *Managing Congestion in Matching Markets*, M&SOM 2021.
- Track matches, conversations, share with at least one match, Gini/Lorenz spread, wasted likes, and two-sided retention; OkCupid, *Your Looks and Your Inbox*, 2009, supports concentration diagnosis but not causal redistribution.
- Match experiment design to spillovers using two-sided randomization, competitive-neighborhood clusters, or regional/time switchbacks, guided by Johari et al., *Experimental Design in Two-Sided Platforms: An Analysis of Bias*, Management Science 2022.

## Evidence Limits

Most effects come from adjacent markets, offline replay, theory, or small regional tests. Capacity definitions and outcomes vary, so pooled effects are not defensible; direct dating validation remains the main gap.
