# Paper Analysis: Returning is Believing: Optimizing Long-term User Engagement in Recommender Systems

**Source:** https://doi.org/10.1145/3132847.3133025
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Returning is Believing: Optimizing Long-term User Engagement in Recommender Systems
- **authors or company:** Qingyun Wu, Hongning Wang (University of Virginia); Liangjie Hong (Etsy, ex-Yahoo Research); Yue Shi (Yahoo Research)
- **venue:** CIKM 2017
- **year:** 2017
- **URL:** https://doi.org/10.1145/3132847.3133025
- **source type:** industry paper
- **direction:** D2
- **problem setting:** Online news/content recommendation maximizing cumulative clicks over a fixed time horizon by modeling both immediate clicks and user return intervals; contextual bandit with article pool and user context.
- **objective and label definition:** Immediate reward = click; return time between sessions determines interaction rounds available; optimize total clicks in period T; r²Bandit balances exploration, short-term click exploitation, and long-term return exploitation via expected future clicks ε from return model.
- **prediction or incrementality:** Contextual bandit scores articles by immediate click probability plus expected future clicks from return-time model (GLM with logit/inverse link); UCB-style exploration on combined score—not uplift estimation.
- **model architecture:** r²Bandit: generalized linear models for click (logit) and return time (inverse link); closed-form confidence bounds enable efficient UCB exploration; naive-r²Bandit variant uses fixed dataset-average CTR for ε.
- **credit assignment:** Per recommendation round: chosen article affects immediate click and subsequent return interval, which scales future interaction opportunities; finite-horizon expected future reward approximation avoids full MDP transition estimation.
- **training data and counterfactual handling:** Yahoo front-page news logs (large-scale real-world); offline replay with reweighted metrics to reduce article-distribution bias; simulation experiments; users handled independently (no cross-user pooling in base algorithm).
- **offline and online evaluation:** Simulation + offline replay on Yahoo logs (~28 days); metrics: cumulative clicks, CTR, average return time, return rate, improved-user ratio, no-return count; theoretical sublinear regret bound when modeling return vs. linear regret if ignored.
- **reported gains:** r²Bandit ~2× CTR of GLM-UCB/rGLM-UCB on Yahoo replay; return rate ~1.8× GLM-UCB; naive-r²Bandit reduces average return time 18–25% vs. logged baseline; ~63% users with shorter return than historical average; significantly lower no-return user count vs. baselines.
- **applicability note for a two-sided dating recommender:** r²Bandit formalizes return-interval optimization alongside clicks—the core credit-assignment problem when dating LTV depends on bringing users back for more swipes/matches, not just immediate engagement.
- **applicability note for a two-sided dating recommender:** Single-sided article recommendation with stationary candidate distribution assumption; no reciprocity, match-market congestion, or bilateral outcome modeling.
- **unverified claims:** none

## 1. Summary

**Title:** Returning is Believing: Optimizing Long-term User Engagement in Recommender Systems
**Authors:** Qingyun Wu, Hongning Wang, Liangjie Hong, Yue Shi
**Abstract:** Formulates long-term engagement as sequential decision making where return time determines future click opportunities; r²Bandit contextual bandit balances exploration, immediate clicks, and expected future clicks with provable regret bounds.

**Key contributions:**
- Sequential optimization objective: maximize cumulative clicks over time horizon via return-aware recommendations.
- r²Bandit with GLM click/return models and UCB exploration.
- Sublinear regret proof; linear regret if return behavior ignored.

**Methodology:** Click = immediate reward; inter-session return interval governs future rounds; stationary click preference assumption; finite-horizon ε for expected future clicks.

**Main results:** Large gains on Yahoo news replay for cumulative clicks, CTR, return rate, and retention proxies vs. GLM-UCB and return-aware UCB variants.

## 2. Experiment Critique

**Design:** Simulation plus large-scale offline replay on real Yahoo logs; theoretical regret analysis complements empirical work.

**Statistical validity:** Replay metrics reweighted for article distribution bias; figures show trends over 28 days; no formal online A/B reported.

**Online experiments:** Not specified in source as live deployment; evaluation is offline replay on production logs.

**Reproducibility:** Yahoo-scale logs referenced but not released in paper; algorithm and GLM details specified.

**Overall:** Foundational return-aware bandit paper; offline-only empirical validation but strong theory and later citations in retention RL work.

## 3. Industry Contribution

**Deployability:** Bandit with GLM + closed-form UCB—lightweight vs. deep RL; suitable for news-style candidate pools.

**Problems solved:** Myopic CTR optimization ignoring that bad recommendations shorten user lifetime interaction count.

**Engineering cost:** Online GLM updates with return-time modeling; per-user independence simplifies deployment but limits data sharing.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First bandit directly optimizing long-term engagement when users may leave after bad recommendations; integrates return time with click exploitation.

**Prior work comparison:** Kapoor et al. survival return prediction (offline only); standard contextual bandits (Li et al.); dwell-time/post-click work (Barbieri, Lalmas); multi-armed bandit recommendation assuming always-return users.

**Verification:** Regret bound and offline replay gains support core claim; foundational for DRN, RLUR, and retention literature.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Yahoo front-page news log | Not public in paper | No | Large-scale summer 2016 collection |

**Offline experiment reproducibility:** Not reproducible without Yahoo data.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** Maximizes cumulative clicks over a time period by optimizing return frequency—not explicit LTV/revenue; CTR is component metric.

**(2) Credit assignment:** Each recommendation affects immediate click and distribution of next return time, which determines future recommendation opportunities; per-article decision per round.

**(3) Label and horizon definitions:** Click labels; return time between sessions; finite-horizon expected future clicks; offline replay over ~28 days; reweighting for label distribution bias.

**(4) Short-term + long-term heads:** Single scoring function combining immediate click estimate and expected future clicks ε from return model—analytic fusion, not neural multi-head.

**(5) Prediction vs incrementality:** Predicts click probability and return time; optimizes combined score for policy, not causal effect of exposure on retention.

**(6) Offline and online evaluation:** Simulation + offline replay on Yahoo logs; reweighted cumulative clicks/return metrics; no live A/B in paper; two-sided interference not specified in source.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Not specified in source.

**(8) Migration path from CTR-like model:** Extends GLM-UCB click bandit with return-time GLM and expected-future-click term; drop-in for any system with return timestamps in logs.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Qingyun Wu, Hongning Wang, Liangjie Hong, Yue Shi
**Affiliations:** University of Virginia; Etsy; Yahoo Research
**Venue:** CIKM 2017
**Year:** 2017
**PDF:** https://doi.org/10.1145/3132847.3133025
**Relevance:** Core
**Priority:** 1
