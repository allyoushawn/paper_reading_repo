# Paper Analysis: A Production-Ready RL Framework for Personalized Utility Tuning with Pareto Sweeping in Pinterest Recommender Systems

**Source:** https://arxiv.org/pdf/2605.16344.pdf
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** A Production-Ready RL Framework for Personalized Utility Tuning with Pareto Sweeping in Pinterest Recommender Systems (PRL-PUTS)
- **authors or company:** Yichu Zhou, Mehdi Ben Ayed, Lin Yang, Jiacong He, Andreanne Lemay, Jiaye Wang, Jaewon Yang, Josie Zeng, Dhruvil Deven Badani, Yijie Dylan Wang, Jiajing Xu, Charles Rosenberg (Pinterest)
- **venue:** arXiv (industry paper)
- **year:** 2026
- **URL:** https://arxiv.org/pdf/2605.16344.pdf
- **source type:** industry paper
- **direction:** D1
- **problem setting:** Pinterest Homefeed multi-task ranker outputs per-objective predictions aggregated by a linear utility layer with globally tuned weights; manual weight tuning is slow, non-personalized, and stale relative to ranker refreshes.
- **objective and label definition:** One-step contextual bandit (γ=0): agent selects discrete (Repin weight, P2P-impression weight) pairs applied to fixed ranker head scores; rewards are clipped binary request-level counts r^repin = min(n^repin,1), r^p2p = min(n^p2p,1) on top-k served items—not retention or revenue horizon labels.
- **prediction or incrementality:** Learns Q^repin(s,a) and Q^p2p(s,a) expected immediate request rewards under chosen utility weights—policy selects weights to maximize engagement, not causal incremental effect of exposure on long-term retention.
- **model architecture:** Ranker-independent control layer: state = user embedding + Transformer-encoded action history + context; action encoded via min-max normalized weight vector; shared 3-layer MLP backbone with two sigmoid value heads; inference sweeps scalarization α to pick argmax over discrete 7×7 weight grid (49 actions); runs parallel to ranker with zero added serving latency and fallback to static weights on failure.
- **credit assignment:** Request-level reward from engagement on the served top-k list; credit assigned to the chosen utility-weight action for that request, not to individual item exposures over a delayed retention window.
- **training data and counterfactual handling:** 1.25% Homefeed traffic uniform-random exploration over discrete weight actions with logged propensities; 14-day train / 7-day hold-out exploration logs; offline evaluation via Reward@HIT (action-match rejection estimator); no ranker retraining required when controlled heads unchanged.
- **offline and online evaluation:** Offline Pareto frontier over 25 α values with Reward@HIT lifts vs production static weights; online A/B 2 weeks, 1% traffic per arm, user-level split across global and cohort-conditioned (CORE/CASUAL/REST) operating policies; Successful Sessions (≥1 key positive action) as composite guardrail.
- **reported gains:** Global P2P-leaning policy (α=0.24): online Repin +0.66%, P2P +0.30%, Successful Sessions +0.13%; matched static average weights: Repin −0.24%, P2P +0.07%, SS +0.02% vs PRL-PUTS +0.12%/+0.21%/+0.11%; offline–online Pearson correlation up to 0.999 (Repin) and 0.986 (P2P) for global policies.
- **applicability note for a two-sided dating recommender:** Ranker-independent RL utility tuner is a migration stepping stone: keep existing CTR/CVR/match heads, learn context-dependent fusion weights toward session or retention proxies before replacing the blend with a unified LTV head.
- **applicability note for a two-sided dating recommender:** One-step bandit optimizes immediate request engagement only; authors note it does not model longer-horizon retention, handles only two objectives at a time, and uses a discrete weight grid—no reciprocity, congestion, or delayed 7–30 day labels.
- **unverified claims:** none
