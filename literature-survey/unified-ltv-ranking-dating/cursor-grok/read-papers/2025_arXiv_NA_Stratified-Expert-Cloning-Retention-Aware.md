# Paper Analysis: Stratified Expert Cloning for Retention-Aware Recommendation at Scale

**Source:** https://arxiv.org/abs/2504.05628
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** Stratified Expert Cloning for Retention-Aware Recommendation at Scale
- **authors or company:** Chengzhi Lin, Annan Xie, Shuchang Liu, Wuhong Wang, Chuyuan Wang, Yongqi Liu, Han Li (Kuaishou Technology; Peking University)
- **venue:** CIKM
- **year:** 2025
- **URL:** https://arxiv.org/abs/2504.05628
- **source type:** industry paper
- **direction:** D2
- **problem setting:** Large-scale short-video recommendation (Kuaishou, Kuaishou Lite) where long-term user retention (active days) is the goal but RL faces delayed credit assignment, large action spaces, and sample inefficiency.
- **objective and label definition:** Maximize expected long-term retention \(E_u[R_u \mid \pi]\) measured by active days in a window (online: 7-day Active Days) or return time / engagement in offline KuaiSim; expert users stratified by retention score (active days/month or LTV) into K=3 levels; offline experts defined as return time ≤3 days.
- **prediction or incrementality:** Behavior cloning from high-retention expert trajectories — learns policies that mimic expert actions given user state, indirectly optimizing retention without explicit reward-modeling or uplift estimation of exposure effects.
- **model architecture:** SEC: shared state encoder \(f_\phi\) + per-level action predictors \(g_{\theta_k}\) (K expert policies); multi-level expert stratification; adaptive expert selection via K-means centroids on encoded states with historical retention floor constraint; action entropy regularization (nuclear norm on continuous action embeddings or categorical entropy).
- **credit assignment:** Trajectory-level imitation — retention outcome attributed implicitly through expert demonstration labels rather than per-action delayed reward backprop; adaptive selection maps current user state to nearest expert-level policy cluster.
- **training data and counterfactual handling:** Expert interaction trajectories from high-retention users; offline KuaiRand-Pure (27,285 users, 1.4M interactions) with KuaiSim retention simulator; online integrates cluster-level action probabilities with existing two-stage rankers (video clusters from multimodal features); 10% A/B traffic over two weeks.
- **offline and online evaluation:** Offline vs TD3, SAC, DIN, CEM, RLUR, GFN on Return Time, Click Rate, Long View Rate, Like Rate; online Active Days (7-day window) and valid interest clusters on Kuaishou platforms (>200M DAU each).
- **reported gains:** Offline Return Time 1.411 vs GFN 1.496 (−5.7%); online cumulative Active Days +0.098% (Kuaishou) and +0.122% (Kuaishou Lite), each >200k additional DAU; valid interest clusters +1.31% / +1.14%.
- **applicability note for a two-sided dating recommender:** Imitation from stratified high-retention user cohorts is an RL alternative when delayed match/retention rewards are too sparse — clone policies from users who stay active without online exploration risk.
- **applicability note for a two-sided dating recommender:** Expert definition and state encoder assume one-sided feed ranking (video clusters), not reciprocal matching or B-side congestion; offline eval uses KuaiSim simulator, not production retention A/B for the full policy replacement.
- **unverified claims:** none

## 1. Summary

SEC replaces direct RL on retention with stratified behavior cloning from multi-level expert users, adaptive policy selection by user state, and action-entropy regularization for diversity. Offline KuaiSim experiments beat RLUR/GFN on return time; large-scale online A/B on Kuaishou platforms shows statistically significant Active Days lifts staged through behavior cloning, multi-level experts, and entropy loss.
