# Relevance index 4/4 — Project Relevance sections of all cards (generated)

### Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?
`2026_arXiv_LLMTouchpointSelection_Can-LLMs-Identify-Meaningful-Touchpoints-in-Conversion-Attribution.md`
**Source:** https://arxiv.org/html/2608.28649v1 | **NLM source id:** 32c86ead-a887-40ef-84ee-da9eaa3cff38 | **Year / venue:** 2026, CIKM '26 (arXiv:2608.28649) | **Authors / affiliation:** Jinqi Wu, Sishuo Chen, Zhangming Chan, Yong Bai, Chao Yi, Han Zhu, Shuodian Yu, Lei Zhang, Sheng Chen, Chenghuan Hou, Jian Xu, Chaoyou Fu — Nanjing University; Taobao & Tmall Group of Alibaba | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q1
- **Attributes retention to individual interactions?** No — attributes discrete e-commerce purchase conversion to prior touchpoints, not recurring retention/days-active.
- **Transferable components:** Two-stage selection-then-allocation framing; LLM-based pairwise semantic scoring to surface implicitly-relevant interactions beyond rule-matching; using LLM-attributed labels as auxiliary training targets for a production ranking/prediction model.
- **Required changes:** Re-anchor the target from single purchase conversion to recurring N7 retention; adapt prompts/features from product metadata to heterogeneous dating actions (swipe, match, message) with temporal gaps; run LLM scoring offline to distill into a lightweight online ranker (real-time LLM calls per swipe are infeasible at scale).
- **On last-touch:** Does not name last-touch explicitly but shows in-shop/single-item heuristic baselines are "blind" to the 14.91% of touchpoints that are implicitly relevant, understating the value of full-path attribution.
- **Transfer rating:** adaptable — the LLM semantic-selection and auxiliary-label mechanism transfers, but the outcome must move from a one-time purchase to a recurring multi-touch retention label.

### MODE: Mutual Optimality in Direct Effects of Reciprocal Recommendations in Matching Markets
`2026_arXiv_MODE_Mutual-Optimality-Direct-Effects-Reciprocal-Recommendations.md`
**Source:** https://arxiv.org/pdf/2608.01731.pdf | **NLM source id:** c951f48e-7cc6-4e8c-a92c-dccc076edab6 | **Year / venue:** RecSys 2026 (arXiv 2608.01731) | **Authors / affiliation:** Yoji Tomita (CyberAgent, Inc., Tokyo) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries; Query A required one retry due to an empty first response)

- **Answers:** Q2
- **Attributes retention to individual interactions?** no — MODE optimizes reciprocal-recommendation list ranking to maximize expected mutual matches under a game-theoretic mutual-optimality criterion; it does not attribute retention, engagement, or active-day outcomes to individual interaction logs at all.
- **Transferable components:** two-sided preference and position-based examination modeling (proactive swipe preference p_i,j and reactive match preference q_j,i); recursive ranking-probability computation for estimating true match likelihood under competition/congestion; the mutual-optimality guarantee that no individual user's experience is sacrificed for aggregate platform gains.
- **Required changes:** shift entirely from static list-ranking/match-maximization to sequence-level fractional retention-credit attribution; extend the binary like/nope, thank/sorry action set to a full heterogeneous funnel (swipe, like, match, message); replace the single-period expected-matches objective with a daily-recurring rolling N7 active-retention target.
- **On last-touch:** does not discuss last-touch/last-click by name, but shows naive one-sided preference ranking (analogous to any non-causal heuristic) creates severe congestion and yields substantially fewer matches than mutually-optimal two-sided ranking.
- **Transfer rating:** background — a game-theoretic two-sided matching/congestion algorithm for match-list optimization, not an attribution or retention-credit model; useful context on dating-market dynamics (congestion, reciprocal preference) but not a building block for the per-swipe credit pipeline itself.

### Balancing Fairness and High Match Rates in Reciprocal Recommender Systems: A Nash Social Welfare Approach
`2026_arXiv_NashSocialWelfare_Balancing-Fairness-High-Match-Rates-Reciprocal-Recommender-Systems.md`
**Source:** https://arxiv.org/pdf/2601.13609.pdf | **NLM source id:** e25aceef-c31c-4d9f-8b20-cf96dc9c7c92 | **Year / venue:** 2026, arXiv 2601.13609 | **Authors / affiliation:** Yoji Tomita (CyberAgent, Inc., Japan), Tomohiko Yokoyama (School of Information Science and Technology, The University of Tokyo, Japan) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2 background — a dating-platform-specific recommender-system paper, but on fairness/exposure allocation, not retention attribution.
- **Attributes retention to individual interactions?** No — optimizes static recommendation-list allocation to maximize expected matches subject to both-side envy-freeness; no retention, engagement, active-days, or LTV outcome at all.
- **Transferable components:** The position-based examination model (e(k) weighting by rank position) is a standard, reusable building block for any exposure/attribution model involving ranked candidate lists; the general insight that naive match/exposure maximization concentrates value unfairly on a subset of users is a relevant fairness consideration if a retention-credit ranking model is later used to actually decide who gets shown — but this is a downstream deployment concern, not part of the credit-assignment mechanism itself.
- **Required changes:** Would need essentially a different problem formulation entirely — this paper's objective and outcome (static match/exposure allocation and envy-freeness) have no retention or attribution dimension; only the position-examination modeling primitive is reusable.
- **On last-touch:** Not discussed — no attribution-heuristic critique of any kind; the paper's only "unfairness" critique is about popularity-driven exposure concentration under match-maximizing ranking, unrelated to last-touch credit assignment.
- **Transfer rating:** background — a well-evidenced dating-platform recommender-system paper on a genuinely different problem (fair match allocation), with only the position-examination-model primitive plausibly reusable for this project.

### From Prediction to Incrementality: Causal Optimization for Large-Scale Targeting and Recommendation
`2026_arXiv_PredictionToIncrementality_Causal-Optimization-Large-Scale-Targeting-Recommendation.md`
**Source:** https://arxiv.org/pdf/2608.10182.pdf | **NLM source id:** 471fd316-4d94-413c-ba4e-ed61b92956ac | **Year / venue:** 2026, arXiv 2608.10182 | **Authors / affiliation:** Changshuai Wei, John Bencina, Phuc Nguyen, Andre Assuncao Silva T Ribeiro, Benjamin Zelditch — all LinkedIn (Seattle/Sunnyvale, USA) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q1 (latest industry attribution/causal-targeting approach, 2026, LinkedIn production).
- **Attributes retention to individual interactions?** No — estimates user-level CATE for marketing-campaign allocation under LP constraints; does not do multi-touch sequence attribution or fractional per-interaction retention credit.
- **Transferable components:** Transformer sequence encoder over touchpoints (with days-since/day-of-week/positional embeddings); DragonNet joint outcome+propensity architecture for de-biasing "would have engaged anyway" users; randomized snapshot-date training-log construction to avoid last-touch leakage; explicit counterfactual/no-action baseline; neural-bandit exploration to expand overlap.
- **Required changes:** Move from user-level campaign allocation to per-touch (swipe/like/match/message) fractional credit; extend the touchpoint vocabulary to dating-funnel event types; re-anchor the outcome from LTV/conversion to a recurring daily N7-active binary label evaluated per rolling reference date.
- **On last-touch:** Explicitly states randomizing the training snapshot date "avoids a last-touch label, captures long-term action effects, and preserves variable-length histories" — a direct, named critique of last-touch labeling.
- **Transfer rating:** adaptable — the causal de-biasing and sequence-modeling machinery transfers, but the unit of credit and outcome must be redesigned for per-swipe daily retention.

### Privacy-Robust Incrementality Measurement for Advertising Systems under Signal Loss
`2026_arXiv_PrivacyRobustIncrementality_Privacy-Robust-Incrementality-Measurement-Advertising-Signal-Loss.md`
**Source:** https://arxiv.org/pdf/2606.03878.pdf | **NLM source id:** 2e9a3300-7b3b-43da-87d8-2b068a86c466 | **Year / venue:** 2026, arXiv:2606.03878 | **Authors / affiliation:** Prashant Shekhar (corresponding), Caroline Howard — Department of Mathematics, Embry-Riddle Aeronautical University | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q1
- **Attributes retention to individual interactions?** No — explicitly defines its target as a decision-certification layer downstream of attribution, not credit distribution across touchpoints, and operates at segment/campaign granularity.
- **Transferable components:** The three-state Certify/Reject/Unresolved discipline (refusing an overconfident point estimate when signal is too degraded/sparse) and the reporting-granularity-vs-noise tradeoff diagnostic are useful design patterns for any per-swipe credit system built on incomplete/censored interaction logs.
- **Required changes:** Aggregate segment-level bounds would need to become per-swipe/per-sequence micro attribution; the scalar retention multiplier would need to become heterogeneous, temporally-decaying event-type features (swipe/match/message); the one-time lift target Δ_s would need to become a recurring daily N7 outcome.
- **On last-touch:** Contrasts itself with MTA generally (not last-touch specifically) and proves that under degraded/incomplete signal, any forced binary decision rule has worst-case error ≥1/2 — a formal argument for why heuristic point-attribution (including last-touch) can be overconfident when the underlying signal is weak.
- **Transfer rating:** background — a decision-theoretic layer for macro-level ad measurement under privacy constraints, not an in-app sequence-attribution algorithm.

### The Proximal Surrogate Index: Long-Term Treatment Effects under Unobserved Confounding
`2026_arXiv_ProximalSurrogateIndex_Long-Term-Treatment-Effects-Unobserved-Confounding.md`
**Source:** https://arxiv.org/pdf/2601.17712.pdf | **NLM source id:** 0b33a3db-d741-43f2-802c-7f3558a3838d | **Year / venue:** 2026, arXiv 2601.17712 (January 27, 2026) | **Authors / affiliation:** Ting-Chih Hung, Yu-Chang Chen — National Taiwan University | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2 background (methodological extension of surrogate-index literature to handle unobserved confounding — directly relevant to the "engaged users swipe more" selection-bias problem, framed as unobserved user-level confounding).
- **Attributes retention to individual interactions?** No — estimates a population-level ATE of a single binary macro treatment; not a per-touch/multi-touch attribution method.
- **Transferable components:** The core insight — that standard causal-adjustment methods (including plain surrogate indices or ordinary propensity-score methods) can still be badly biased if there's an *unobserved* confounder like "latent swiper motivation/attractiveness" driving both engagement and retention — is directly relevant motivation for the dating platform's stated selection-bias problem; the dual-proxy bridge-function framework offers a concrete technique (using pre-existing behavioral proxies as stand-ins for unobserved user quality/motivation) that could debias a per-swipe credit model beyond what observed covariates alone allow.
- **Required changes:** Reframe from single binary-treatment ATE to per-touch fractional credit across a heterogeneous swipe/match/message sequence; would need identification of suitable proxy variables (W, Z) for unobserved "swiper engagement propensity" in the dating context; outcome must shift to a recurring daily N7-active binary.
- **On last-touch:** Not discussed directly — no explicit critique of last-touch/last-click attribution; the paper's empirical contribution is showing standard surrogate methods underestimate long-term effects by >50% under unobserved confounding, which is a cautionary parallel to any single-proxy or single-touch credit scheme trusting confounded engagement signals.
- **Transfer rating:** adaptable — its diagnosis (unobserved user-level confounding badly biases naive short-term-proxy or observed-covariate adjustment) is highly relevant to the platform's exact selection-bias concern, and its proxy/bridge-function machinery is a reusable de-biasing technique, though the paper itself operates on single binary treatments, not multi-touch sequences.

### Pseudo-Incrementality Testing: Measuring Advertising Lift from Naturally Occurring Interventions
`2026_arXiv_PseudoIncrementality_Measuring-Advertising-Lift-Naturally-Occurring-Interventions.md`
**Source:** https://arxiv.org/pdf/2609.18257.pdf | **NLM source id:** c6d16a82-6dff-4801-aedc-e93009b24441 | **Year / venue:** 2026, arXiv 2609.18257 | **Authors / affiliation:** Georgios Filippou, Boi Mai Quach (Trinity College Dublin, School of Computer Science and Statistics), Ashish Kumar Jha (Trinity College Dublin, Trinity Business School), Dublin, Ireland | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q1 (2026 industry-adjacent quasi-experimental lift-measurement method), though it targets advertising spend, not in-app interaction attribution.
- **Attributes retention to individual interactions?** No — operates entirely on aggregate macro time-series (channel-level spend/outcome), not individual user interactions.
- **Transferable components:** Bayesian online change-point detection could date undocumented feature rollouts/algorithm changes in platform logs; the variance-constrained counterfactual identification principle (forcing structural-break effect estimation through co-observed regressors, not a free-floating trend) is a useful de-biasing pattern; the five-screen qualification framework (adequacy, materiality, isolation, directional significance, economic plausibility) is a reusable checklist for validating any observational incrementality estimate.
- **Required changes:** Would need a complete redesign from macro channel-level time series to individual user-level, per-swipe interaction sequences; requires a micro-level multi-touch attribution or counterfactual-path model instead of aggregate time-series forecasting; outcome must shift from cumulative revenue lift to a recurring daily N7-active binary per user.
- **On last-touch:** Not discussed — the paper does not analyze last-touch/last-click attribution; it instead critiques observational/unconstrained time-series methods generally for selection and endogeneity bias.
- **Transfer rating:** background — sound quasi-experimental identification machinery for aggregate campaign-level lift, but not designed for individual-level multi-touch attribution and requires substantial adaptation to be relevant.

### Multi-channel Uplift Policy Learning
`2026_arXiv_ReAlloc_Multi-channel-Uplift-Policy-Learning.md`
**Source:** https://arxiv.org/pdf/2607.28182.pdf | **NLM source id:** cb8ad114-6778-438e-a0ab-dfd458147b4a | **Year / venue:** 2026, arXiv 2607.28182 | **Authors / affiliation:** Changjian Liu (Peking University), Tianyu Wang, Xiaoxuan Deng, Junqi Jin, Chuan Yu, Jian Xu, Bo Zheng (Alibaba Group/Taobao), Wentao Zhu (Beihang University), Yuwei Xu (CUHK-Shenzhen) — work done during internship at Taobao, Alibaba Group | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q1 (2026 industrial uplift/causal allocation system, Alibaba/Taobao production).
- **Attributes retention to individual interactions?** No — allocates marketing budget across channels per item to optimize e-commerce business metrics (orders, GMV, ROI); it explicitly distinguishes itself from multi-touch attribution, noting in related work that "multi-touch attribution assigns conversion credit across sequences but lacks explicit simplex-constrained optimization" — i.e., the authors are aware of MTA as a different, adjacent problem.
- **Transferable components:** The DML/orthogonalization pattern for removing legacy-policy confounding is directly analogous to removing "engaged users swipe more" selection bias; the support-aware conservative-decision mechanism (penalize/reject actions/attributions unsupported by historical data) is a reusable safety pattern for any counterfactual credit-assignment model operating near the edge of its training distribution; the scalar-potential-function trick for guaranteeing path-consistent (non-cyclic) marginal credit could inform how per-swipe fractional credit is made internally consistent across a session.
- **Required changes:** Complete redesign from a continuous per-item budget-simplex allocation problem to a discrete, sequential, per-user multi-touch attribution problem; would need a sequence model over heterogeneous event types rather than a K-dimensional channel simplex; outcome must shift from e-commerce revenue metrics to a recurring daily N7-retention binary.
- **On last-touch:** Not directly addressed — the paper only briefly distinguishes multi-touch attribution from its own compositional-allocation setting, without a substantive critique of last-touch attribution specifically.
- **Transfer rating:** background — a sophisticated causal budget-allocation framework for a structurally different (continuous multi-channel spend) problem; the confounding-removal and support-aware conservatism ideas are useful analogies but the method itself is not a per-touch attribution mechanism.

### A Long-term Value Prediction Framework In Video Ranking
`2026_arXiv_TaobaoLTV_Long-term-Value-Prediction-Framework-Video-Ranking.md`
**Source:** https://arxiv.org/pdf/2602.17058.pdf | **NLM source id:** fcca450b-5415-4dee-b49a-2a2c79a2d751 | **Year / venue:** WWW 2026 | **Authors / affiliation:** Huabin Chen, Xinao Wang, Huiping Chu, Keqin Xu, Chenyi Wang, Kai Meng, Yuning Jiang (Alibaba Group, Hangzhou); Chenhao Zhai (Tsinghua University, Shenzhen) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2
- **Attributes retention to individual interactions?** partly — attributes subsequent intra-session engagement to individual recommended items via learned attribution weights, and aggregates multi-day creator watch time into an author-level LTV target that improves LT1/LT3; does not perform micro-level multi-touch sequence attribution (e.g., Shapley/counterfactual masking) across a full swipe/like/match/message history for a single retention outcome.
- **Transferable components:** PDQ position-debiasing (directly analogous to correcting for power-swipers reaching more profiles); multi-dimensional attribution weights to filter unrelated subsequent activity noise; Tweedie+MSE loss for zero-inflated, heavy-tailed retention/engagement targets; dual-stream co-training with stop-gradient for handling N7-delayed retention labels alongside real-time signals.
- **Required changes:** shift from video-exposure attribution to heterogeneous dating-funnel touch types (swipe, like, match, message) with event-type and time-gap features; replace author-centric aggregation with profile-cluster or funnel-stage aggregation; re-anchor the day-level target from a 3-day return-visit rate to a daily-recurring rolling N7 active-retention indicator.
- **On last-touch:** does not name last-touch/last-click explicitly, but explicitly critiques naive unattributed aggregation of subsequent interactions as failing to establish causal relationships and introducing noise — directly analogous to the critique of assigning all credit to only the last touch.
- **Transfer rating:** adaptable — a session/day-level LTV attribution framework for video ranking, not a multi-touch swipe-credit model, but its position-debiasing, learned attribution weights, and delayed-label co-training are directly adaptable building blocks for per-swipe retention credit.

### Neural ODE for Multi-Channel Attribution
`OpenReview_NeuralODE_Neural-ODE-for-Multi-Channel-Attribution.md`
**Source:** https://openreview.net/pdf?id=2hEx8jzRBo | **NLM source id:** 25cc68ad-d29d-494f-b765-36a55fb25d7f | **Year / venue:** Not specified in source (OpenReview) | **Authors / affiliation:** Not specified in source | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q1 (per batch tag; cannot be confirmed from source content)
- **Attributes retention to individual interactions?** Not specified in source — no paper content was available to answer.
- **Transferable components:** Not specified in source.
- **Required changes:** Not specified in source.
- **On last-touch:** Not specified in source.
- **Transfer rating:** background — no usable content; source ingestion failed (CAPTCHA-blocked page only). Re-ingesting this source into NotebookLM (or supplying the PDF directly) is required before this paper can be evaluated.

