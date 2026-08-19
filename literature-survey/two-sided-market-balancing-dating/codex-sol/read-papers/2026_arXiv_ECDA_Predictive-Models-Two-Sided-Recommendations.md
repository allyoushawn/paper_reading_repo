# Paper Analysis: Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach

**Source:** https://arxiv.org/abs/2602.19689  
**Date analyzed:** 2026-08-19

---

## 1. Summary

**Title:** Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach  
**Authors:** Kazuki Sekiya, Suguru Otani, Yuki Komatsu, Sachio Ohkawa, Shunya Noda  
**Abstract:** Ranking by predicted bilateral dating probability can still overload responsive receivers, producing many formal matches that do not progress. The paper introduces effective dates, which discount congested matches, and Exposure-Constrained Deferred Acceptance (ECDA), which caps expected incoming likes or dates. Offline simulations and a regional CoupLink field experiment evaluate efficiency, distribution, and downstream messaging.

**Key contributions:**

- Defines effective dates as a congestion-adjusted match-quality metric.
- Replaces headcount recommendation limits with fractional expected-exposure budgets.
- Proves dating-rate-sorted deferred acceptance and ECDA reduce to scalable greedy scans.
- Validates ECDA in production with a regional difference-in-differences experiment.

**Methodology:** Gradient-boosted trees predict proposer login, like, receiver login, and relike probabilities; their product is a pair's dating rate. ECDA allocates a recommendation-probability matrix subject to sender profile-review capacity and receiver expected-like or expected-date budgets. Synthetic and empirical simulations compare one-sided ranking, standard deferred acceptance, and ECDA. Kanto receives ECDA while Kansai-Tokai remains control.

**Main results:** In empirical simulation, date-exposure ECDA raises average effective dates 7.6% and receiver dating probability 8.7% versus one-sided dating-rate ranking, while reducing raw dates. In the field experiment, excluding the most congested 0.1% yields +0.003 realized effective dates, +0.002 proposer dating probability, and +0.005 receiver dating probability; messaging is unchanged.

## 2. Experiment Critique

**Design:** Evaluation includes ten-run synthetic simulations, a production-log empirical market, and a geographically separated treatment/control rollout. Baselines include like-sort, date-sort, the current production heuristic, and standard deferred acceptance.

**Statistical validity:** Difference-in-differences estimates report p-value thresholds. Only two macro-regions are observed, so standard clustered event-study errors are unreliable. Trimming the top 0.1% is substantively motivated but makes the strongest realized effects conditional on excluding the worst congestion tail.

**Online experiments:** January 13–26, 2026; Kanto treatment and Kansai-Tokai control. Full-sample receiver messages fall 0.004 and proposer message probability falls 0.001; after tail trimming, message effects are zero.

**Reproducibility:** Algorithms, capacities, prediction metrics, and market sizes are specified. Production data and code are not specified in source.

**Overall:** This is unusually direct evidence for capacity-aware dating allocation. The effective-date model assumes an overloaded receiver uniformly chooses one match, and the regional design cannot fully resolve inference or spillover concerns.

## 3. Industry Contribution

**Deployability:** When sorted by predicted dating rate, ECDA is a greedy scan suitable for large-scale serving.

**Problems solved:** Superstar receiver congestion, wasted likes, unequal match distribution, and inflated raw-match objectives.

**Engineering cost:** Moderate to high: four calibrated predictors, daily exposure budgets, fractional allocation, regional experimentation, and distribution monitoring.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Integrates production predictive models with exposure-budgeted matching and introduces effective dates as an outcome metric for receiver congestion.

**Prior work comparison:** Hitsch, Hortaçsu, and Ariely (2010) model online dating; Horton (2017) evaluates two-sided recommendations; Halaburda et al. (2018) restrict choice; Choo and Siow (2006) motivate matching-theoretic balancing; Tomita, Togashi, and Moriwaki (2022) deploy capacity-aware matching scores; Kanoria and Saban (2021) restrict decentralized actions; Pizzato et al. (2010) introduce reciprocal dating recommendation.

**Verification:** All results here are source-scoped. The direct comparison to Tomita et al. is conceptual rather than a reported implementation baseline.

## 5. Dataset Availability

**Datasets mentioned:**

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| CoupLink synthetic market | Not public | No | 1,000 proposers and 1,000 receivers; ten runs. |
| CoupLink empirical candidate market | Not public | No | About 8,000 proposers and 5,000 receivers. |
| CoupLink regional field experiment | Not public | No | Kanto treatment versus Kansai-Tokai control. |

**Offline experiment reproducibility:** Inputs and equations are detailed, but production logs, trained models, and code are unavailable.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Exact mechanism:** Sort pairs by predicted date probability, then greedily allocate exposure subject to sender review capacity and receiver budgets expressed as expected likes or expected dates. The effective-date objective discounts matches to receivers already predicted to have multiple dates.

**Metrics and reported effect:** Simulation: effective dates +7.6% and receiver dating probability +8.7%, with raw dates reduced 24.6%. Field, excluding top 0.1% congestion: effective dates +0.003 (`p<0.05`), proposer probability +0.002 and receiver probability +0.005 (`p<0.10`); messaging effect 0.000.

**Capacity/congestion relevance:** Senders have a daily profile capacity; receivers have expected-exposure budgets and are assumed to pursue one concurrent date. The method directly reallocates exposure away from overloaded recipients.

**Practical mapping:** Replace a pure mutual-likelihood ranker with ECDA over predicted login, like, and like-back stages. Tune exposure budgets against effective matches and side-specific probability, with message and retention guardrails.

**Dating fit: High.** The method is implemented and field-tested on CoupLink under reciprocal, sequential dating-app mechanics.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| No verified inbound mentions within the 45-source corpus. | — | — |

## Meta Information

**Authors:** Kazuki Sekiya, Suguru Otani, Yuki Komatsu, Sachio Ohkawa, Shunya Noda  
**Affiliations:** Not specified in source.  
**Venue:** arXiv preprint  
**Year:** 2026  
**PDF:** available  
**Relevance:** Core  
**Priority:** 2

## Annotated Bibliography Fields

- **Title:** Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach
- **Authors/organization:** Kazuki Sekiya, Suguru Otani, Yuki Komatsu, Sachio Ohkawa, Shunya Noda
- **Year:** 2026
- **Venue/type:** arXiv technical preprint; production simulation and regional field experiment
- **Link:** https://arxiv.org/abs/2602.19689
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Predicted the full login-like-login-relike funnel, defined congestion-adjusted effective dates, and allocated recommendation probabilities with receiver budgets for expected likes or dates. They prove ECDA becomes a greedy scan under date-rate sorting, compare it with one-sided and deferred-acceptance baselines, and run a regional CoupLink difference-in-differences rollout.
- **Mechanism relevant to two-sided balancing (≤50 words):** Cap expected inbound likes or dates, not just recommendation counts, and optimize effective dates so already overloaded receivers are discounted. This spreads exposure toward users who can still convert a match into interaction.
- **Metrics and reported effect:** Simulation: effective dates +7.6%, receiver probability +8.7%, raw dates -24.6%. Field excluding top 0.1%: effective dates +0.003, proposer probability +0.002, receiver probability +0.005; messaging unchanged.
- **Dating-app fit:** High — direct production implementation and field evidence on a reciprocal dating platform.
- **Confidence:** High on source-scoped methods and reported effects; medium-high on causal precision because only two rollout regions support the difference-in-differences design.
