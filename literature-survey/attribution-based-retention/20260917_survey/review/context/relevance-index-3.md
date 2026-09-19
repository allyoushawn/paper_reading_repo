# Relevance index 3/4 — Project Relevance sections of all cards (generated)

### Impact of Organic Ranking on Ad Click Incrementality
`2026_GoogleBlog_OrganicRankIncrementality_Impact-Of-Organic-Ranking-On-Ad-Click-Incrementality.md`
**Source:** https://research.google/blog/impact-of-organic-ranking-on-ad-click-incrementality/ | **NLM source id:** 077dc10e-9f00-4a5b-a018-f35d94d5691d | **Year / venue:** 2026-06, Google Research blog (post itself is dated 2012-03-27 per the retrieved page text; treated per batch metadata) | **Authors / affiliation:** David Chan (Statistician), Lizzy Van Alstine (Research Evangelist) — Google Research | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q1
- **Attributes retention to individual interactions?** No — measures aggregate ad-click incrementality relative to organic search rank; no retention, engagement, or per-interaction credit.
- **Transferable components:** The core "organic baseline" idea — disentangling causal incremental value from activity a user would have generated anyway — is directly analogous to the dating platform's selection-bias problem (engaged users swipe/return regardless). Pause/holdout experiments as the causal-anchor mechanism also transfers conceptually.
- **Required changes:** Everything about granularity: this is aggregate search-campaign click incrementality, not micro-level per-swipe sequence attribution for a recurring N7 outcome; would need a full redesign to heterogeneous, multi-touch, daily-recurring in-app events.
- **On last-touch:** Not discussed — the post does not address multi-touch or last-touch attribution models at all, only ad-vs-organic click substitution.
- **Transfer rating:** background — useful only as a conceptual illustration of the organic-baseline/cannibalization idea, not as an attribution methodology.

### Meridian GeoX: An Open-Source Framework for Precision and Efficiency in Geo Experiments
`2026_GoogleResearch_MeridianGeoX_Open-Source-Framework-Precision-Efficiency-Geo-Experiments.md`
**Source:** https://research.google/pubs/meridian-geox-an-open-source-framework-for-precision-and-efficiency-in-geo-experiments/ | **Retrieved via:** NotebookLM source 535371ff-3748-464a-b495-57e0c4b8ce23 | **Year / venue:** 2026 (techreport), Google Research | **Authors / team:** Steven Ye, Fabian Sinn, Yunxiao Li, Yang Jiao (Google) | **Analyzed:** 2026-09-17

- **Answers:** Q1 (adjacent) — 2026 state-of-the-art causal geo-experiment tooling, not user-level attribution.
- **Attributes retention to individual interactions?** no — unit of analysis is geographic region/market, not user or interaction.
- **Transferable components:** the general synthetic-control / placebo counterfactual-inference logic could inform macro geo-holdout validation of a ranking-model rollout, but not the per-swipe credit mechanism itself.
- **Required changes:** would need to move entirely from macro geo time-series to user-/event-level sequence modeling — different unit, different data structure.
- **On last-touch:** not discussed.
- **Transfer rating:** background — a state-of-the-art causal geo-experiment framework for ad measurement, useful only as macro validation context, not a transferable attribution method.

### 
`2026_ICLR_ALM-MTA_Front-Door-Causal-Multi-Touch-Attribution-Creator-Ecosystem.md`
**Source:** https://arxiv.org/pdf/2605.08881.pdf | **NLM source id:** 916117a6-16d6-4277-ad48-fd92b7e60f51 | **Year / venue:** ICLR 2026 (arXiv 2605.08881) | **Authors / affiliation:** Yuguang Liu, Luyao Xia, Hu Liu, Zhangxi Yan, Jian Liang, Han Li, Kun Gai — Kuaishou Technology, Beijing; The University of Auckland | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** both Q1 and Q2 (front-door causal MTA is a 2026 industrial approach; also attributes an in-app behavioral outcome — uploads — to individual interactions, though not retention).
- **Attributes retention to individual interactions?** No — attributes content-upload probability, not N7 retention/engagement, to individual consumed touchpoints.
- **Transferable components:** front-door identification via adversarial proxy mediator (bypasses unobserved confounding without requiring backdoor ignorability); counterfactual touchpoint-deletion credit Δ(τⱼ); InfoNCE contrastive overlap control for positivity in huge treatment spaces; IPW reweighting.
- **Required changes:** swap binary upload outcome Y for daily-recurring N7 retention label; extend the homogeneous video-touchpoint sequence to heterogeneous swipe/like/match/message events with type + temporal-gap embeddings; redefine proxy Y′ from content-similarity to a dating-funnel synergy signal (e.g., match/high-dwell-conversation likelihood).
- **On last-touch:** explicitly cites last-touch as an early rule-based heuristic that data-driven MTA (logistic regression, Markov-chain removal effects, RNN, Shapley) moved beyond; critiques rule/similarity-based industrial methods for lacking causal identifiability and ignoring heterogeneous treatment effects.
- **Transfer rating:** adaptable — the front-door deconfounding and counterfactual-deletion machinery transfers directly, but the outcome, touchpoint typology, and proxy definition all need redesign for daily-recurring, heterogeneous-touch retention.

### Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching
`2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md`
**Source:** https://arxiv.org/pdf/2602.15752.pdf | **NLM source id:** 54b047fc-b81a-40d6-84fd-d935a35cf0b2 | **Year / venue:** 2026, ICLR (arXiv 2602.15752) | **Affiliation:** Hanjuku-kaso, Co., Ltd. (Yuta Saito et al.) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2 (partly — see below); not Q1
- **Attributes retention to individual interactions?** no — MRet is a forward-looking allocation/ranking policy driven by a learned retention-vs-match-count curve, not a backward-looking credit-assignment method over realized swipes/matches.
- **Transferable components:** the concave personalized retention curve f(x, m) as a reward shape for a credit/reward function; the two-sided retention-gain framing (crediting the value to both the swiper and the candidate); cluster/feature-based retention regression as a lightweight way to estimate the shape of f.
- **Required changes:** replace the ranking-time argsort with a true post-hoc sequence attribution architecture (e.g., sequence models, Shapley-style credit) over heterogeneous event types; move from a scalar cumulative-match count and monthly login label to a daily-recurring N7 target with time-aware/temporal modeling of swipe→match→message sequences.
- **On last-touch:** not discussed — comparison baselines are Max Match, Uniform, and FairCo; no mention of last-touch/last-click attribution.
- **Transfer rating:** adaptable — the retention-curve concept and two-sided gain framing are directly reusable as reward-shape priors, but the method itself is a ranking policy, not an attribution/credit-assignment technique.

### CanniUplift: A Holistic Framework for Mitigating Seller and Incentive Cannibalization in E-commerce Uplift Modeling
`2026_KDD_CanniUplift_Mitigating-Seller-Incentive-Cannibalization-Ecommerce-Uplift-Modeling.md`
**Source:** https://arxiv.org/pdf/2607.05242.pdf | **NLM source id:** acc8a491-158c-4f24-b43a-833a622ec5d5 | **Year / venue:** KDD '26 (32nd ACM SIGKDD), arXiv 2607.05242, Jeju Island, Korea, Aug 2026 | **Authors / affiliation:** Zuwang He, Shihao Shu, Yuli Qu (co-first authors), Hanyu Gao, Ziliang Zhang, Diwei Chen, Xiangda Yan, Buyu Gao, Tanchao Zhu, Yumeng Li (corresponding), Junxiong Zhu — all Taobao & Tmall Group of Alibaba | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q1 (2026 industrial uplift-modeling system, Alibaba/Taobao production, directly targets the "would have converted anyway" selection-bias problem).
- **Attributes retention to individual interactions?** No — estimates incremental GMV from personalized incentive allocation to sellers/coupons; not a retention or multi-touch attribution method, though its debiasing logic is highly analogous.
- **Transferable components:** RDD is the most directly relevant idea in this batch to "credits swipes that would have happened anyway" — it explicitly separates a post-treatment observable signal (redemption vs. non-redemption) to strip out organic/pseudo-incrementality, which maps onto separating "swipe led to a genuine match/conversation" from "swipe/match that would have retained the user regardless"; PGA's platform-wide aggregation-consistency constraint maps onto ensuring per-swipe fractional credits sum consistently to the true observed N7 outcome per user rather than each candidate profile independently over-claiming credit (an internal-consistency check analogous to fractional-credit normalization); the Treat-Attention mechanism (candidate as query over a user's behavior/treatment sequence) is a directly reusable architecture pattern for scoring each candidate swipe's incremental contribution against a user's history.
- **Required changes:** Retarget outcome from platform GMV to daily N7-active retention; redefine "redemption" analogously as a genuine downstream signal (e.g., match converts to a real conversation) vs. a swipe/match with no downstream engagement; extend to a full heterogeneous event-type sequence rather than seller/coupon candidates.
- **On last-touch:** Not discussed directly by name, but the paper's core critique — that naive local (per-unit) uplift models over-attribute credit to organic conversions and ignore cross-unit interference, overestimating true incrementality by ~35% — is structurally the same failure mode as last-touch attribution over-crediting swipes that would have happened anyway.
- **Transfer rating:** adaptable — RDD's redemption-based denoising and PGA's aggregation-consistency constraint are concrete, directly portable mechanisms for exactly the selection-bias and double-crediting problems the dating platform's retention-attribution project is trying to solve.

### HGenPush: A Heterogeneous Generative Recommendation Architecture for Industrial Push Notification Systems
`2026_KDD_HGenPush_Heterogeneous-Generative-Recommendation-Push-Notifications.md`
**Source:** https://arxiv.org/pdf/2607.03362.pdf | **NLM source id:** 0fea3f6f-1070-40ed-8ecc-0d28bd996c7e | **Year / venue:** KDD 2026 (v.2) | **Authors / affiliation:** Xiao Liang, Jiali Feng, Xin Feng, Yiqing Wang, Baolin Ye, Siyao Feng, Zhihui Deng, Cunyi Zhang, Huajin Sun, Xuanping Li, Kaiqiao Zhan, Yanan Niu, Kun Gai (Kuaishou Technology, Beijing) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2 (background)
- **Attributes retention to individual interactions?** no — generates and ranks push-notification candidates using post-click session reward signals; does not attribute retention/engagement/active-days to individual historical interactions (swipes/likes/matches) via fractional credit.
- **Transferable components:** post-exposure session reward shaping (rewarding deep post-swipe/post-match engagement like conversation continuation, penalizing quick bounces/unmatches) as an RLVR-style signal; group-relative advantage normalization to strip out user-level baseline activity variance when comparing candidate profiles; hybrid long/short-term + channel-specific behavior fusion for building a user-interest representation.
- **Required changes:** shift from generating/ranking candidate lists to per-touch sequence attribution; replace video/author semantic IDs with heterogeneous dating-funnel event types (swipe, like, match, message) with event and time-gap embeddings; re-anchor the reward from within-session consumption quality to a daily-recurring rolling N7 active-retention indicator.
- **On last-touch:** does not name last-touch/last-click explicitly, but shows relying on immediate clicks alone (a myopic/proximate signal, structurally similar to last-touch) produces clickbait-like recommendations, while incorporating post-click/post-exposure session behavior via RL improves long-term engagement and drives the observed DAU gain.
- **Transfer rating:** background — an industrial generative-retrieval and post-click preference-alignment architecture for push notifications, not an attribution or retention-credit model; its reward-shaping and group-normalization ideas are conceptually adjacent but not a direct building block for per-swipe fractional credit.

### Not All Matches Are Equally Valuable: An Online Experiment of Retention-Focused Recommendation in a Job-Matching Platform
`2026_RecSysHR_WantedlyChurnBoost_Not-All-Matches-Are-Equally-Valuable.md`
**Source:** https://arxiv.org/pdf/2609.01652.pdf | **NLM source id:** 5779d9c7-d97d-4158-a00a-ef4c64268482 | **Year / venue:** 2026, RecSys in HR workshop (arXiv 2609.01652) | **Affiliation:** Wantedly, Inc. (Tokyo) and Hanjuku-kaso Co., Ltd. | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2 (partly — see below); not Q1 (not an industry-attribution-approach survey piece)
- **Attributes retention to individual interactions?** no — it reranks exposure toward churn-risk candidates via a heuristic boost; it does not attribute retention outcomes to specific past swipes/matches or produce fractional credit labels.
- **Transferable components:** the empirical non-linear retention-value curve (diminishing marginal value of matches beyond a threshold) as a shape prior for a reward/credit function; the exposure-decay term n(u) as a pattern for avoiding over-crediting/over-exposing already-satisfied users; the covariate-adjusted online A/B evaluation design for validating any resulting policy.
- **Required changes:** replace heuristic score-boosting with true sequence/credit attribution (e.g., sequence models or Shapley-style credit) over heterogeneous touch types (swipe, match, message); move from a static 4-week binary churn flag to a recurring daily N7 metric with time-aware modeling; adapt from one-sided candidate exposure credit to two-sided per-swipe credit for the initiating user.
- **On last-touch:** not discussed at all — the paper's baseline comparison is match-maximization ranking, not last-touch attribution.
- **Transfer rating:** adaptable — no attribution method to reuse, but the non-linear retention-value finding and exposure-decay mechanic are directly reusable design inputs for a per-swipe credit model.

### Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning
`2026_RecSys_DownstreamRewards_Long-Term-User-Engagement-Optimization-Model-Agnostic-Downstream-Rewards.md`
**Source:** https://arxiv.org/html/2607.14192v3 | **NLM source id:** d6f303ed-3a73-4c04-8313-a1af62a453d2 | **Year / venue:** arXiv 2607.14192, accepted RecSys 2026 | **Affiliation:** Pinterest | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q1 and Q2 (recent industry practice, 2026; partial per-interaction attribution)
- **Attributes retention to individual interactions?** Partly — proxy downstream rewards score the near-term engagement trajectory triggered by one impression/action, but the paper does not compute explicit offline multi-touch credit allocation (no Shapley values, no counterfactual path masking) across a user's full multi-day history.
- **Transferable components:** User-Prevalence normalization to remove exposure/selection bias (very close to the platform's own "engaged users swipe more" problem); negative rewards for shallow/low-intent actions; discounted downstream-trajectory proxy rewards (swipe→match→message chains); use-case/preference-expansion reward for diversity credit.
- **Required changes:** move from impression-level auxiliary prediction heads to an explicit sequence-attribution mechanism producing fractional credit labels per historical swipe; map the downstream event space onto the dating funnel (left/right swipe, match, message) with event-type weights; re-anchor the outcome to a rolling daily N7 active indicator instead of session continuation.
- **On last-touch:** The paper states directly that "even when downstream outcomes are observed, attributing them to specific earlier recommendations is challenging," and empirically shows that naive/shallow click-based signals flip to negative retention indicators once exposure bias is removed — a direct, recent (2026) argument against naive last-touch-style crediting.
- **Transfer rating:** adaptable — the UP-normalization debiasing technique is the most directly reusable selection-bias fix in this batch, even though the reward framework itself stops short of full sequence attribution.

### Media Measurement and the Assisted Own Goal: Attribution, Marketing-Mix Models, and Individual-Level Incrementality
`2026_arXiv_AssistedOwnGoal_Attribution-Marketing-Mix-Models-Individual-Level-Incrementality.md`
**Source:** https://arxiv.org/pdf/2607.09608.pdf | **NLM source id:** 83299ba5-8a24-4110-9d80-1d8f2b75b107 | **Year / venue:** 2026, arXiv 2607.09608 (06/21/2026) | **Authors / affiliation:** Tobias B. Konitzer, PhD — GrowthLoop | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q1 (2026 industry-adjacent incrementality measurement) and directly addresses last-touch critique relevant to Q2 framing.
- **Attributes retention to individual interactions?** No — attributes ad-driven purchase conversions across channels, not retention/engagement to in-app interactions.
- **Transferable components:** Ambient deterministic salted-hash holdouts (stateless, no assignment bookkeeping) is directly reusable for running always-on, per-user or per-feature-variant randomized experiments; the individual-level CATE extension of PIE is a template for a persuadability/incrementality model; the channel-complete/platform-complete outcome principle — aggregate outcomes across all downstream surfaces (matches, later conversations) rather than crediting only the observed touchpoint — maps closely onto "credit later matches and conversations, not just the last swipe."
- **Required changes:** Move from binary campaign/audience ITT assignment to micro-level fractional credit across a heterogeneous swipe/match/message sequence; re-anchor outcome from purchase conversion to a recurring daily N7-active binary; would need a sequence/path model since this paper's ITT machinery gives an aggregate treatment effect, not a per-touch decomposition within a single treated unit.
- **On last-touch:** Direct, sharp critique — proves last-touch (and even multi-touch/data-driven attribution) cannot fix the "assisted own goal" because the failure is *observability*, not the crediting heuristic: "no reweighting of visible touchpoints can restore credit for this invisible conversion." Directly analogous to the dating platform's problem of ignoring later matches/conversations.
- **Transfer rating:** background — its causal-identification principle (channel-complete/platform-complete measurement invariant to where the outcome is realized) is conceptually the strongest single argument against last-touch found in this batch, but the method itself (audience-level ITT for ad spend) does not directly give a per-swipe fractional-credit mechanism.

### 
`2026_arXiv_AttributionMarkets_Fisher-Market-Fractional-Credit-Assignment.md`
**Source:** https://arxiv.org/pdf/2607.20694.pdf | **NLM source id:** 98e96997-d361-431a-8573-119c026f8604 | **Year / venue:** arXiv 2607.20694 | **Authors / affiliation:** Salavat Ishbulatov — Independent researcher (doplan.ai) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q1 (a 2026 fractional-credit-assignment mechanism related to, and explicitly positioned against, MTA).
- **Attributes retention to individual interactions?** Partly — it is a general-purpose fractional credit-assignment framework (explicitly framed via MTA) applied to task/action effort logs, not to user retention/engagement.
- **Transferable components:** Fisher-market equilibrium with hard budget caps and a provable junk filter (exact zero credit for low-affinity swipes, rather than diffuse fractional noise across the whole swipe history); multi-signal log-odds affinity fusion (text + structural link + temporal decay) directly analogous to fusing profile-similarity, match, and recency signals per swipe; noise-adaptive entropy regularization for robustness.
- **Required changes:** re-frame task "hour budgets" as user attention capacity or retention-value budgets (candidate profiles have no natural hour budget); replace logged action duration with heterogeneous, non-duration interaction types (swipe/like/match/message); replace one-off task-completion progress with a daily-recurring N7 retention target.
- **On last-touch:** explicitly critiques the standard exclusive all-or-nothing linking rule (functionally last-touch/single-link attribution) for making genuinely related, unlinked effort invisible and reporting false stalls; separately notes MTA supplies fractional-credit framing but lacks a budget/price mechanism to prevent over-crediting.
- **Transfer rating:** adaptable — the budget-capped, junk-filtered market mechanism is a strong candidate for turning the current uncapped/last-touch credit rule into a bounded, sparse fractional-credit scheme, but the domain objects (budgets, goods, outcome) all need re-mapping from task-planning to retention.

### Attributed, But Not Incremental: Cannibalization-Corrected Attribution for Large-Scale Advertising
`2026_arXiv_CannibalizationMTA_Attributed-But-Not-Incremental-TikTok.md`
**Source:** https://arxiv.org/pdf/2606.26690.pdf | **NLM source id:** 65be2782-a8bc-41e2-a103-4e8c322830f8 | **Year / venue:** 2026, ADKDD '26 (August 10, 2026, Jeju, Korea) | **Authors / affiliation:** Donghui Li, Bowen Yuan, Zili Yang, Qinxin Chen, Lijing Song — TikTok / ByteDance | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q1
- **Attributes retention to individual interactions?** No — corrects channel/campaign-level acquisition (DNU) attribution, not per-user/per-interaction retention.
- **Transferable components:** Using sparse randomized holdouts as causal anchors to calibrate an observational attribution signal; explicit cannibalization/baseline-subtraction formulation (H_t = A_t − Lift_t); hierarchical, constraint-respecting credit propagation.
- **Required changes:** Move from channel-day scalar correction to micro sequence-level attribution over individual swipe/match/message histories; replace one-time DNU acquisition target with a recurring daily N7 retention outcome; model heterogeneous, multi-stage touchpoint types rather than a single upstream nominal-attribution input.
- **On last-touch:** Explicitly names last-touch attribution (LTA) as the common production baseline and shows it systematically overstates incremental value by crediting channels/touches that "harvest" existing demand rather than creating it.
- **Transfer rating:** background — the experiment-calibration and cannibalization-correction logic is conceptually relevant, but the framework operates at macro channel/campaign granularity, not on individual in-app interactions.

### Heterogeneous Multi-treatment Uplift Modeling for Trade-off Optimization in Short-Video Recommendation
`2026_arXiv_HMUM_Heterogeneous-Multi-treatment-Uplift-Modeling-Trade-off.md`
**Source:** https://arxiv.org/pdf/2511.18997.pdf | **NLM source id:** aafa7891-e78a-4b0d-9fdd-e5b869bfa23e | **Year / venue:** arXiv 2511.18997, 2026 (Kuaishou) | **Authors / affiliation:** Chenhao Zhai, Chang Meng, Xueliang Wang, Shuchang Liu, Xiaolong Hu, Shisong Tang, Xiaoqiang Feng (Kuaishou Technology); Chenhao Zhai, Xiu Li (Tsinghua Shenzhen International Graduate School) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** both
- **Attributes retention to individual interactions?** no — estimates request-level ITEs for macro strategy-enablement decisions, not fractional credit across a user's individual historical touchpoints (swipes/likes/matches/messages).
- **Transferable components:** KL-divergence non-treatment baseline alignment (removes cross-branch noise when comparing candidate-profile categories); online dynamic value-weighting (MMOE) for balancing competing outcomes (e.g., match conversion vs. N7 retention) using real-time context; relative uplift scaling to bridge heterogeneous metric scales; RCT-based causal incrementality isolation to de-bias engaged users who'd act anyway.
- **Required changes:** shift from request-level strategy-enablement to micro-level counterfactual credit assignment across individual touchpoint sequences; replace average-pooled interaction embeddings with event-type-aware (swipe/like/match/message) sequence modeling with funnel stage and time-gap features; re-anchor target from aggregate session metrics to a daily-recurring rolling N7 active-retention indicator.
- **On last-touch:** does not name last-touch/last-click explicitly, but shows static population-wide strategy rules create severe trade-off penalties versus personalized causal modeling — analogous critique of any non-causal heuristic, including last-touch.
- **Transfer rating:** adaptable — a request-level multi-treatment uplift framework, not a multi-touch attribution model, but its bias-correction (KL alignment) and dynamic value-weighting modules are directly adaptable building blocks for per-swipe retention credit.

### Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM
`2026_arXiv_IMA-BayesianMMM_Integrated-Marketing-Attribution-Bayesian-Framework-Privacy-Safe-MMM.md`
**Source:** https://arxiv.org/pdf/2606.16878.pdf | **NLM source id:** 5a8a299e-afe2-4909-ac42-4bfc9e71851f | **Year / venue:** 2026, arXiv:2606.16878 | **Authors / affiliation:** Meghana R. Bhat, Ankit Umare, Utsav Aggarwal, Richard Vecsler, Arunkumar Mani, Karthik Nair, Chandhu Nair — Lowe's Companies, Inc. | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q1
- **Attributes retention to individual interactions?** No — operates entirely on aggregate daily campaign/channel media series; there is no user-level tracking or in-app interaction data at all.
- **Transferable components:** The macro-to-micro Bayesian prior-anchoring pattern itself (use a reliable aggregate causal/experimental estimate as an informative prior to regularize a noisy, high-dimensional granular estimate) is a reusable idea for shrinking per-swipe credit estimates toward a more reliable aggregate N7 lift number. Adstock/carryover modeling is also conceptually relevant to delayed match/message effects.
- **Required changes:** Everything about the unit of analysis: aggregate daily campaign series would need to become individual user interaction sequences; the sales-revenue target would need to become a recurring daily N7 retention label; homogeneous media spend/impressions would need to become heterogeneous swipe/match/message event types.
- **On last-touch:** Does not address last-touch directly, but broadly critiques user-level MTA as increasingly unreliable and operationally fragile under privacy restrictions and incomplete customer journeys — motivating its own aggregate-data-only design.
- **Transfer rating:** background — a macro, aggregate-data attribution framework; useful only as a design pattern (prior-anchored shrinkage), not as a directly portable algorithm.

