# Paper Analysis: Deep Reinforcement Learning for Search, Recommendation, and Online Advertising: A Survey

**Source:** `/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/09_Reinforcement_Learning/2019 (Sigweb) Deep Reinforcement Learning for Search, Recommendation, and Online Advertising - A Survey.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

This is a short (12-page) 2019 ACM SIGWEB Newsletter survey by Xiangyu Zhao, Long Xia, Jiliang Tang (Michigan State University), and Dawei Yin (JD.com) that gives a taxonomy snapshot of deep reinforcement learning applied to three "information seeking" mechanisms — search, recommendation, and online advertising — as of early 2019. It introduces RL foundations (multi-armed bandits, Markov Decision Processes, Partially Observable MDPs, multi-agent stochastic games; model-based vs. model-free methods; value-function methods such as Q-learning/SARSA/DQN vs. policy-search methods such as REINFORCE, Actor-Critic, and DDPG), then surveys representative algorithms per domain: for search, query reformulation, relevance ranking (MDPRank, cascading bandits), whole-page optimization, and session search; for recommendation, the exploitation/exploration dilemma (contextual bandits, LinUCB), temporal dynamics of user preference, long-term user engagement (a bandit method trading off immediate clicks against expected future clicks, and a multi-agent framework, DeepChain, coordinating strategies across scenarios), and page-wise/whole-page recommendation (DDPG for large action spaces); for online advertising, guaranteed delivery and real-time bidding under MDP and multi-agent formulations. It closes with five future directions: cross-scenario collaborative RL, richer reward-function design, incorporating more user-agent interaction signals, cheaper/safer offline simulation for pre-deployment testing, and open RL environments for the field. As a pure survey it reports no original experiments; every quantitative claim in it belongs to one of the roughly 40 primary studies it cites.

## 2. Experiment Critique

Not expanded — Priority 4, reduced depth per the survey's depth rule.

## 3. Industry Contribution

Not expanded — Priority 4, reduced depth per the survey's depth rule.

## 4. Novelty vs. Prior Work

Not expanded — Priority 4, reduced depth per the survey's depth rule.

## 5. Dataset Availability

Not expanded — Priority 4, reduced depth per the survey's depth rule.

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | Deep Reinforcement Learning for Search, Recommendation, and Online Advertising: A Survey; Xiangyu Zhao, Long Xia, Jiliang Tang, Dawei Yin; ACM SIGWEB Newsletter, Spring 2019; DOI 10.1145/3320496.3320500, http://doi.acm.org/10.1145/3320496.3320500 |
| 2 | Source type | Academic (survey) |
| 3 | Direction | D2 |
| 4 | Problem setting | Taxonomizing deep-RL-based techniques across three "information seeking" mechanisms — search, recommendation, and online advertising — organized around two RL problem formulations: multi-armed bandits (no state transition) and Markov Decision Processes / POMDPs / multi-agent stochastic games (with state transition). |
| 5 | Objective and label definition | No single model — the survey states generically that RL's advantage is maximizing "expected cumulative long-term reward," where reward is domain-specific (CTR, revenue, dwell time, user engagement/return frequency). The subsection closest to this project (§4.3, "Long Term User Engagement") describes a bandit method balancing immediate clicks against expected future clicks on a user's next visit, and a Deep-Q-Learning framework (Zheng et al., 2018) that adds "how frequently a user returns" as a supplement to immediate-click labels — but the survey gives no explicit horizon, delay-handling, or censoring treatment for any of these; it only names the cited papers' mechanisms at a high level. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. The survey frames every RL policy as maximizing predicted/observed reward from an action, never as estimating a counterfactual exposure effect. |
| 7 | Model architecture | Not a single architecture — a taxonomy of RL problem formulations (K-armed bandits, contextual bandits, MDP, POMDP, multi-agent stochastic games) and solution families (model-based vs. model-free; value-function methods — Q-learning, SARSA, DQN — vs. policy-search methods — REINFORCE, Actor-Critic, DDPG), instantiated per domain by roughly 30 cited primary works (e.g., MDPRank, MDP-DIV, DeepChain, MA-RDPG). |
| 8 | Credit assignment | Not addressed as a unified mechanism. Per-domain sketches vary: LTR-style work (MDPRank) assigns reward at each ranking-position decision within a session; the long-term-engagement subsection (§4.3) is the only place a delayed, user-level outcome (return frequency) is described, but the survey does not explain how that delayed signal is credited back to a specific earlier recommendation. |
| 9 | Training data and counterfactual handling | Not addressed in general terms — as a survey it does not describe a unified training/data pipeline; cited works are described only as "user interacts with the system as the environment," with no discussion of off-policy correction, propensity weighting, or counterfactual estimators across the field. |
| 10 | Offline and online evaluation | Not addressed systematically — the survey names cited works' evaluation settings only in passing (e.g., offline historical logs, a live news-feed deployment for the DQN return-frequency method) without a consolidated offline/online evaluation methodology. |
| 11 | Reported gains | None — this is a survey with no original experiments; no aggregate quantitative results are given anywhere in the source. |
| 12 | Applicability to a two-sided dating recommender | Useful only as a coarse map of where "long-term user engagement" work sat in the RL-for-recsys literature circa 2019 (§4.3); it predates and is superseded in this survey's own corpus by the retention-specific RL papers already carded here (RLUR, GFN4Retention, Two-Stage Constrained Actor-Critic), which give concrete architectures and results this 2019 survey only gestures at. |
| 13 | Unverified claims | None applicable — the survey makes no primary empirical claims of its own; every number belongs to a cited source, and this analysis did not independently check any of them. |

## Project Relevance

**Low project relevance, and explicitly historical.** This 2019 survey **predates** the retention-focused RL-for-recommendation line already carded in this survey — RLUR (2023, WWW, `2023_WWW_RLUR_Reinforcing-User-Retention-Billion-Scale-Video.md`), GFN4Retention (2024, KDD, `2024_KDD_GFN4Retention_Modeling-User-Retention-Generative-Flow-Networks.md`), and the Two-Stage Constrained Actor-Critic paper (2023, WWW, `2023_WWW_TSCAC_Two-Stage-Constrained-Actor-Critic-Short-Video.md`) — all of which post-date it by 4–5 years and supply the concrete, evaluated retention-objective architectures this survey only sketches in one short subsection (§4.3, Long Term User Engagement). It should **not be cited for current practice** on Q1 (retention/LTV as training objective) or Q3 (label and horizon definitions); its only value here is as a taxonomy snapshot of RL-for-recommendation's pre-2020 state, useful for framing how far the field has moved — from generic "user engagement" bandits and DQN toward the explicit multi-day retention objectives, GFlowNet-based methods, and constrained actor-critic formulations now already in this corpus. It touches Q7 not at all (no two-sided, reciprocal, or congestion treatment anywhere in the source), and Q2/Q5/Q6 only at the level of naming that such problems exist in cited work, without adding method-level detail beyond what the later, already-carded papers provide directly.

## Papers That Mention This Paper (Reverse Citation Map)

_This paper proposes no distinctively-named method, so no automated reverse-citation match was possible._

## Meta Information

- **Authors:** Xiangyu Zhao, Long Xia, Jiliang Tang, Dawei Yin
- **Affiliations:** Michigan State University (Zhao, Tang); JD.com (Xia, Yin)
- **Venue:** ACM SIGWEB Newsletter, Spring 2019
- **Year:** 2019
- **Relevance:** Related
- **Priority:** 4
- **nlm:259cc507**
