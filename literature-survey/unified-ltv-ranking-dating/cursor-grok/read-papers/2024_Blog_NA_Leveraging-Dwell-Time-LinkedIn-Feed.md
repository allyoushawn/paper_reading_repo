# Paper Analysis: Leveraging Dwell Time to Improve Member Experiences on the LinkedIn Feed

**Source:** https://www.linkedin.com/blog/engineering/feed/leveraging-dwell-time-to-improve-member-experiences-on-the-linkedin-feed
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Leveraging Dwell Time to Improve Member Experiences on the LinkedIn Feed
- **authors or company:** LinkedIn Feed AI Team (acknowledges Siddharth Dangi, Jim Sorenson, Alison Liu, Hailing Chen, Yafang Yang)
- **venue:** LinkedIn Engineering Blog
- **year:** 2024
- **URL:** https://www.linkedin.com/blog/engineering/feed/leveraging-dwell-time-to-improve-member-experiences-on-the-linkedin-feed
- **source type:** blog
- **direction:** D1
- **problem setting:** LinkedIn Feed two-pass funnel (recall-oriented first pass, multi-objective second pass) ranks network and out-of-network posts; many weekly active users passively consume without explicit actions, so dwell is the primary engagement signal for that cohort.
- **objective and label definition:** Evolves from P(skip) negative signal to an Auto Normalized Long Dwell binary label: predict whether dwell exceeds the x-th percentile of dwell for the item's top-K attribute cluster (content type, creator type, distribution method, etc.), recomputed daily from data; fused in MOO utility with passive (click, dwell) and active (comment, reshare) heads plus downstream and creator-side terms.
- **prediction or incrementality:** Predicts skip probability and long-dwell exceedance probabilities fused into a weighted MOO score—predictive engagement modeling, not incremental retention effect of a specific exposure.
- **model architecture:** Second-pass deep neural networks per MOO objective group; P(skip) from prior work as negative passive signal; long-dwell binary classifier with cluster-level percentile normalization (not manual static thresholds); MOO combines alpha/beta/gamma-weighted passive, active, downstream, and creator objectives.
- **credit assignment:** Request/impression-level multi-head predictions combined via tuned MOO hyperparameters; long-dwell labels normalized within categorical clusters updated daily; no attribution of user-level retention to individual post exposures described.
- **training data and counterfactual handling:** Production feed logs with dwell distributions analyzed per content type and position; prior iterations (raw dwell regression, static thresholds) abandoned for noise and bias; online A/B validates final auto-normalized approach; no counterfactual training stated.
- **offline and online evaluation:** Iterative online A/B (iterations #1–#3 negative or weak; iteration #4 directionally then statistically significant positive on targeted dwell metrics); final model reports improved sessions, overall time spent, and time per post, especially for passive consumers.
- **reported gains:** Figure 8 shows iteration #4 achieved statistically significant positive improvements on targeted dwell metrics (exact lift percentages not stated in blog text); qualitative gains on sessions, overall time spent, and time spent per post for passive consumers.
- **applicability note for a two-sided dating recommender:** Adaptive percentile dwell labels (by card type, position, media) are a practical surrogate when match/conversation labels are delayed and sparse—extends short-horizon heads toward session-quality without waiting for 7–30 day retention.
- **applicability note for a two-sided dating recommender:** Still fuses multiple engagement heads via fixed MOO weights rather than a unified retention/revenue objective; no bilateral match credit, congestion on popular profiles, or incrementality framing.
- **unverified claims:** none
