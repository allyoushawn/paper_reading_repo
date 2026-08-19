# Paper Analysis: Stratified Expert Cloning for Retention-Aware Recommendation at Scale

**Source:** `/Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/2504.05628.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

Chengzhi Lin, Annan Xie, Shuchang Liu, Wuhong Wang, Chuyuan Wang, Yongqi Liu, Han Li (Kuaishou Technology / Peking University). CIKM '25. Stratified Expert Cloning (SEC) is an imitation-learning framework for retention-aware recommendation. Instead of using RL to optimize retention directly (which the authors argue suffers from delayed credit assignment, large action spaces, and sample inefficiency), SEC treats interaction sequences from high-retention "expert" users as demonstrations and learns policies via behavior cloning (BC). Three components: (1) **multi-level expert stratification** — expert users are split into K levels (K=3 in experiments) by a retention score (e.g., average active days/month or LTV), rather than a single binary expert/non-expert split, motivated by a t-SNE finding that non-expert users cluster closer to lower-level experts than to the highest-retention experts, i.e., retention behavior is continuous, not binary; (2) **adaptive expert selection** — at inference, a user's state embedding is matched via K-means cluster distance to the nearest expert level, constrained to be no lower than the user's own historical retention level; (3) **action entropy regularization (AER)** — a nuclear-norm (continuous actions) or class-entropy (discrete actions) penalty on the policy's action distribution to counter the mode collapse observed in vanilla BC (Figure 4). Offline evaluation on KuaiRand-Pure with the KuaiSim/GFN retention simulator (leave module + return module) shows SEC outperforming TD3, SAC, DIN, CEM, RLUR, and GFN on Return Time, Click Rate, and Long View Rate. Online A/B tests on Kuaishou and Kuaishou Lite (200M+ DAU, video platforms, not dating) show cumulative lifts of +0.098% and +0.122% in 7-day Active Days, translating to 200,000+ additional daily active users per platform.

## 2. Experiment Critique

Offline experiments use a single dataset (KuaiRand-Pure) and a retention *simulator* (GFN's leave/return modules) rather than real return-time observations, so the offline "Return Time" metric is itself a model prediction, not ground truth. The online A/B test (Table 3) allocated only 10% traffic to baseline vs. SEC over two weeks and reports statistically significant (p<5%) but very small absolute lifts (+0.028% to +0.043% per stage); no confidence intervals or effect-size context are given beyond the p-value threshold. The ablation study (Table 2) is informative — removing multi-level stratification and removing action entropy regularization each degrade Return Time and Click/Long-View Rate — but is run on the same single offline dataset. The authors report a trade-off: SEC's Like Rate is 8.9% lower than GFN's, attributed to "optimizing user retention rather than maximizing immediate satisfaction" — a plausible but not causally verified explanation.

## 3. Industry Contribution

Deployed at scale on two production video platforms with hundreds of millions of DAU, with a described two-stage ranking integration (cluster action prediction blended with other ranking scores). Architecture is comparatively lightweight (shared state encoder + per-level MLP action predictors, K-means clustering for expert assignment), a genuine advantage over RL alternatives requiring reward-model design and online exploration. Cold-start and small/niche platforms are explicitly named as a limitation (Section 6) since the method depends on having "a sufficiently large and diverse set of high-retention 'expert' users."

## 4. Novelty vs. Prior Work

Extends behavior cloning (well established in LLM alignment, robotics, autonomous driving) to the retention-optimization setting, contrasting with prior recommendation-specific approaches cited in Related Work: DT4Rec / IURO (interpretable retention factors) and Generative Flow Networks for retention (GFN, the strongest offline baseline here). The paper's stated novelty is the *stratification* of experts into continuous levels (motivated empirically by t-SNE clustering, Figure 3) rather than a binary expert/non-expert split, plus the entropy regularizer for diversity.

## 5. Dataset Availability

| Dataset | Type | Public | Notes |
|---|---|---|---|
| KuaiRand-Pure | Offline, video | Yes (public benchmark) | 27,285 users, 7,551 items, 1,436,609 interactions, 0.70% density |
| Kuaishou / Kuaishou Lite (online A/B) | Online, video | No (proprietary production traffic) | 200M+ DAU each |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | Stratified Expert Cloning for Retention-Aware Recommendation at Scale; Lin, Xie, Liu, Wang, Wang, Liu, Li (Kuaishou Technology, Peking University); CIKM 2025; https://arxiv.org/abs/2504.05628 |
| 2 | Source type | Academic (industry-affiliated, with production A/B test results) |
| 3 | Direction | D2 |
| 4 | Problem setting | Large-scale video recommendation; goal is a recommendation policy π: S → A maximizing expected long-term user retention, learned by imitating high-retention "expert" user trajectories rather than by direct RL reward optimization. |
| 5 | Objective and label definition | Retention is measured offline as **Return Time** — average days until the user returns to the platform (lower is better), estimated via a simulator (KuaiSim/GFN leave-and-return modules), not observed ground truth. For online A/B tests the metric is **Active Days within a 7-day window**. Expert selection threshold: offline, users with simulated return time ≤3 days are labeled experts; online, users are stratified into 3 levels by activity days. No delay/censoring-handling mechanism beyond the simulator's own leave/return modeling is described. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. The policy is trained purely to imitate the actions of users who already exhibited high retention; it does not estimate the counterfactual/causal effect of any recommendation on retention. **This also means expert selection is confounded**: experts are chosen by realized retention outcome (return time ≤3 days, or historical active-days level), and the paper never checks whether these users would have retained regardless of what was recommended to them. The paper does not address this selection-bias risk anywhere in the text, including the Limitations section, which discusses only expert-population scarcity and cold-start, not confounding. |
| 7 | Model architecture | Shared state encoder f_φ (MLP; user context + state) feeding K expert-level action predictors g_θk (Gaussian output head for continuous actions, categorical for discrete). K-means clustering of state embeddings per expert level for adaptive inference-time expert assignment, with a floor constraint k* = min(k*, r_h) tying the assigned expert level to the user's own historical retention level. Trained with combined BC loss (Eq. 2–4) and action-entropy regularization loss (nuclear norm of the action matrix, or class-entropy for discrete actions), Eq. 5. |
| 8 | Credit assignment | Not addressed directly — the paper does not perform per-action credit assignment for the delayed retention outcome. Imitation learning is explicitly used to *bypass* the credit-assignment problem rather than solve it: the policy imitates the full observed action sequence of a user who was later found to retain, without attributing the retention outcome to any specific action within that sequence. |
| 9 | Training data and counterfactual handling | State-action pairs (s_t, a_t) drawn from interaction trajectories of stratified expert users (KuaiRand-Pure offline; production logs online). No counterfactual or off-policy correction is applied; this is standard behavior cloning on observational trajectories from a subpopulation selected by outcome. |
| 10 | Offline and online evaluation | Offline: KuaiRand-Pure + GFN/KuaiSim retention simulator; metrics Return Time, Click Rate, Long View Rate, Like Rate; baselines TD3, SAC, DIN, CEM, RLUR, GFN. Online: A/B test on Kuaishou and Kuaishou Lite, 10% traffic each arm, two weeks, metric = 7-day Active Days, with a separate online AUC check across expert-activity levels (Figure 7) and a "Valid Clusters" interest-expansion metric (Table 4). |
| 11 | Reported gains | Offline: 5.7% reduction in Return Time vs. GFN on the KuaiRand-Pure simulator (Table 1); Click Rate and Long View Rate improved 3.5% and 3.9% over GFN, Like Rate 8.9% lower. Online: cumulative Active Days lift of +0.098% (Kuaishou) and +0.122% (Kuaishou Lite) over two weeks (Table 3), described as translating to 200,000+ additional DAU per platform. |
| 12 | Applicability to a two-sided dating recommender | Video-platform behavior cloning does not transfer directly: it has no notion of reciprocity, congestion, or a shared limited resource on the recommended side, and its expert-selection confound is a serious risk if reused for a revenue/retention objective in dating. The multi-level stratification and entropy-regularization ideas are architecturally reusable, but only after adding an incrementality check on expert selection. |
| 13 | Unverified claims | The claim that experts genuinely demonstrate "retention-causing" behavior (rather than being merely correlated with retention through unobserved user traits) is asserted, not tested. The 200,000+ additional DAU figure is derived from a small percentage lift without reported confidence intervals. Offline Return Time is a simulator output, not a directly observed metric, though this is disclosed. |

## Project Relevance

Speaks most directly to **Q1** (retention as training objective) and **Q8** (a documented migration path — imitation learning as an alternative to RL for retention optimization). Also touches **Q3** (label/horizon: return-time and 7-day active-days) and **Q2** only negatively — the paper is a clear example of a paper that optimizes for retention without addressing incrementality, illustrating the survey's central prediction-vs-incrementality distinction. **Caution for reuse**: the expert-selection-by-outcome confound flagged above is a first-order risk if this pattern (clone the behavior of retained/high-LTV users) were applied to the dating-app setting, since active/repeat users likely retain regardless of exposure.

## Papers That Mention This Paper (Reverse Citation Map)

_This paper proposes no distinctively-named method, so no automated reverse-citation match was possible._

## Meta Information

- **Authors:** Chengzhi Lin, Annan Xie, Shuchang Liu, Wuhong Wang, Chuyuan Wang, Yongqi Liu, Han Li
- **Affiliations:** Kuaishou Technology, Beijing; Peking University, Beijing
- **Venue:** CIKM 2025 (34th ACM International Conference on Information and Knowledge Management)
- **Year:** 2025
- **Relevance:** Core
- **Priority:** 3
- **nlm:a6817bf6**
