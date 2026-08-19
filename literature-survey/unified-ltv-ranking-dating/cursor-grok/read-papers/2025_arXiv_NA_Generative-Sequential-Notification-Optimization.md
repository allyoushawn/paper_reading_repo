# Paper Analysis: Generative Sequential Notification Optimization via Multi-Objective Decision Transformers

**Source:** https://arxiv.org/pdf/2509.02458.pdf
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** Generative Sequential Notification Optimization via Multi-Objective Decision Transformers
- **authors or company:** Borja Ocejo, Ruofan Wang, Ke Liu, Rohit Patra, Haotian Shen, David Liu, Yiwen Yuan, Gokulraj Mohanasundaram, Fedor Borisyuk, Prakruthi Prabhakar (LinkedIn)
- **venue:** arXiv (cs.LG)
- **year:** 2025
- **URL:** https://arxiv.org/pdf/2509.02458.pdf
- **source type:** industry paper
- **direction:** D4
- **problem setting:** Nearline notification send/drop for millions of LinkedIn users: after a multitask ranker selects the top notification candidate, a decision agent chooses send-as-badge, send-as-push, or don't-send under fatigue and relevance constraints.
- **objective and label definition:** Multi-objective discounted return-to-go over finite-horizon episodes (length T+H) sampled from continuous interaction streams; reward vector includes predicted click/open value, actual inter-state visits, and adaptive volume-penalty fatigue signals; γ discounts future steps; RTG computed with H-step look-ahead.
- **prediction or incrementality:** Return-conditioned policy learning (offline RL as supervised sequence modeling); not explicit CATE/uplift—uses predicted engagement models as reward components plus realized visit rewards.
- **model architecture:** Decision Transformer with multi-dimensional RTG conditioning; quantile regression over RTG distribution (pinball loss at 0.25/0.5/0.75 quantiles); eligible-action-set embedding fused into action head; circular-buffer sequence persistence (length up to 16) in Venice for near-real-time inference.
- **credit assignment:** User-level sequential notification decisions; rewards mix candidate-level predicted CTR/open with user visit events between states—not item-level attribution of long-horizon retention to a single feed impression.
- **training data and counterfactual handling:** ε-greedy randomized logging from deployed CQL policy (2% users, one week); 70/30 train/validation split; offline RL on logged trajectories without explicit IPS/DR correction described.
- **offline and online evaluation:** Offline: action accuracy 96.7%, pinball loss 0.358; online A/B (2% users, one week each) vs CQL baseline on Sessions, Notification Volume, Notification CTR; best DT: +0.72% Sessions, −1.68% Volume, CTR not statistically significant.
- **reported gains:** +0.72% user sessions vs multi-objective CQL while reducing notification volume; learned RTG prompts and context length 4 ablations contribute incrementally; production at 100–150K QPS.
- **applicability note for a two-sided dating recommender:** Analogous send/drop or pacing layer above a ranked candidate pool (e.g., push vs in-app vs silence) with fatigue and session-level north stars.
- **applicability note for a two-sided dating recommender:** Not reciprocal matching or profile ranking; session/notification credit differs from attributing 30-day retention to one swipe; no two-sided congestion modeling.
- **unverified claims:** none

## 1. Summary

LinkedIn replaces a deployed Conservative Q-Learning notification agent with a multi-objective Decision Transformer that reframes offline RL as return-conditioned supervised learning. Key innovations: quantile-regression RTG prompts (avoiding manual RTG updates when some rewards are unrealized), vector-valued rewards without fixed fusion weights, and production circular-buffer sequence infrastructure. Online, DT beats CQL on sessions at lower volume with unchanged CTR guardrail.

## 2. Experiment Critique

Strong production deployment evidence (scale, ablations on context length and prompt tuning). Offline metrics are imitation accuracy, not counterfactual policy value. Single-week A/B slices at 2% traffic; no long-horizon retention labels. CQL baseline comparison is fair within the same logging pipeline but TD-learning instability on rich features is a known DT advantage the authors emphasize.

## 3. Industry Contribution

Fully deployed nearline system (Air Traffic Controller / Samza, Venice stores, model cloud). Demonstrates DT stability vs CQL when feature dimensionality grows 10×. Prompt tuning via RTG quantiles gives interpretable trade-offs between CTR and volume objectives.

## 4. Novelty vs. Prior Work

Builds on Decision Transformer (Chen et al. 2021), LinkedIn CQL notification work (Prabhakar et al. 2022), and quantile RTG ideas from multi-game DT (Lee et al. 2022). Novelty is production-scale multi-reward RTG quantile modeling and circular-buffer serving for infinite-horizon notification streams.

## 5. Dataset Availability

Proprietary LinkedIn notification interaction logs; no public dataset.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

Speaks to **Q1** (sessions as long-horizon objective beyond CTR), **Q4** (multi-reward vector without fixed fusion—DT learns implicit combination; inference-time per-reward quantile tuning), and **Q8** (migration from short-term supervised/CQL to return-conditioned sequence policy). Weak on **Q2** (no item-level credit for delayed retention), **Q5** (not incrementality/CATE), **Q7** (no reciprocity). Useful template for a notification/push pacing layer above a dating ranker, not for reciprocal feed ranking itself.

| # | Field | Answer |
|---|-------|--------|
| 1 | Ranking objective | Sessions plus notification relevance (CTR) and fatigue penalties in multi-objective RTG; not pure LTV. |
| 2 | Credit assignment | Sequential user notification states; predicted click rewards + realized visits between steps. |
| 3 | Labels / horizon | Finite episodes T+H from continuous stream; RTG with discount γ; fatigue via adaptive volume penalties. |
| 4 | Short/long fusion | Multi-dimensional reward vector; DT learns implicit fusion; quantile prompts tune per objective at inference. |
| 5 | Prediction vs incrementality | Return-conditioned policy over logged actions; not causal effect of showing a specific item. |
| 6 | Offline / online eval | Offline accuracy/pinball; online A/B on Sessions, Volume, CTR vs CQL. |
| 7 | Reciprocity / fairness | Not specified in source. |
| 8 | CTR → long-term migration | Replace unstable value-based RL with DT on same logged data; add richer state/reward heads incrementally. |

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Borja Ocejo, Ruofan Wang, Ke Liu, Rohit Patra, Haotian Shen, David Liu, Yiwen Yuan, Gokulraj Mohanasundaram, Fedor Borisyuk, Prakruthi Prabhakar
**Affiliations:** LinkedIn (Mountain View, USA)
**Venue:** arXiv:2509.02458
**Year:** 2025
**PDF:** https://arxiv.org/pdf/2509.02458.pdf
**Relevance:** Related
**Priority:** 3
