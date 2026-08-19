# Paper Analysis: Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems

**Source:** https://arxiv.org/pdf/2511.18013.pdf
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems
- **authors or company:** Weijie Jiang, Armando Ordorica, Jaewon Yang, Olafur Gudmundsson, Yucheng Tu, Huizhong Duan (Pinterest)
- **venue:** arXiv (industry paper)
- **year:** 2025
- **URL:** https://arxiv.org/pdf/2511.18013.pdf
- **source type:** industry paper
- **direction:** D1
- **problem setting:** Pinterest Related Pins search-like surface (~50% of platform traffic) ranks candidate Pins after a query Pin click; retention depends on users returning to saved content, but revisitation is delayed, cross-session, and cross-surface (save on Related Pins, revisit on own profile).
- **objective and label definition:** Adds merged revisitation head RP&RV predicting save-then-revisit: same-day revisitation impression (1dRevImpre), same-day revisitation grid-click (1dRevGrid), and 7-day revisitation grid-click (7dRevGrid) within 0–6 days after repin; fused into existing MMoE MTL ranker with grid-click, repin, click, long-click heads via utility-weighted score (u_RP&RV tuned to 1.27× u_Repin offline).
- **prediction or incrementality:** Predicts probability of joint repin-and-revisit outcomes from exposure logs—surrogate attribution links save on Related Pins to later profile revisit by user ID + Pin ID, not causal incrementality of ranking exposure on retention.
- **model architecture:** Existing Related Pins ranker: transformer user sequence + DCNv2 + MMoE over binary action heads; new revisitation head and revisitation Pin-perf features (7/30/90-day counts of revisit impressions and grid-clicks, Related-Pins-triggered and overall variants); cross-surface 7-day join pipeline from Feedview logs to profile revisitation events.
- **credit assignment:** Surrogate attribution: revisitation credited only to the saved Pin when user revisits that Pin on own profile within 7 days (same-day or cross-day rules); cross-surface join on user ID and Pin ID with time_save < time_revisit < time_save+7 days; item-level label on the originally saved candidate Pin.
- **training data and counterfactual handling:** ~6.6B training / ~700M eval examples (27-day train, 3-day eval); production impression logs with cross-surface label construction; no off-policy correction—supervised BCE on constructed revisitation labels.
- **offline and online evaluation:** Offline NDCG/MAP/Recall/Hits@3 per head; online A/B Apr 29–Jun 26, 2025 on Related Pins (~12M users per arm, 2 months); site-wide active users, sessions ≥5 min, time spent on Related Pins and own profile.
- **reported gains:** Offline: revisitation head NDCG@3 +40.15%, Hits@3(repin) +0.59%, Hits@3(revisit) +0.65%; online: 7dRevGrid +1.18% volume / +1.42% propensity, repin +0.94% / +0.64%, active users +0.10% volume / +0.08% propensity, sessions ≥5 min +0.41%, total time spent +0.39%.
- **applicability note for a two-sided dating recommender:** Concrete template for a delayed retention surrogate—save/bookmark → return visit within 7 days—as an auxiliary MTL head with cross-session joins, when full 7–30 day retention labels are too sparse for primary training.
- **applicability note for a two-sided dating recommender:** Pinterest content-save revisitation is one-sided; dating needs reciprocity (match requires both likes), congestion on attractive profiles, and distinction between prediction and incremental retention from showing a specific candidate.
- **unverified claims:** none
