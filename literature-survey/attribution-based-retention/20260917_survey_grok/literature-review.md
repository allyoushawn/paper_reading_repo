
Date: 2026-09-18  
Topic: Attribution-based retention  
Paper count: 27

# Attribution-based Retention Literature Review

## Executive Summary

No card demonstrates identified causal attribution of binary N-day retention to individual in-app interactions. The closest systems are per-item predictive retention scores, save-to-revisit surrogates, and policy-internal item decompositions. The strongest transferable design combines ALM-MTA-style removal scores, LinkedIn-style experiment calibration, and Spotify-style organic holdbacks.

### Most Promising Approaches

1. Causal removal MTA: explicit touch-level labels with a serious confounding model.
2. Experiment-calibrated deep attribution: scalable fractional allocation tied to randomized anchors.
3. Item-retention scoring: directly bridges user-level delayed labels to item-level ranking.

### Practical Recommendations

Short term: build N7 deletion scores, propensity diagnostics, and randomized validation cells.  
Mid term: add discrete-time survival modeling and calibration against persistent exposure holdbacks.

---

## 1. Retention-targeted methods — reciprocal / two-sided platforms (1 paper)

### Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching (ICLR 2026)

- Detailed analysis: [read-papers/2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md](read-papers/2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md)

Kishimoto et al., *Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching*, ICLR 2026 is directly about dating-like reciprocal matching. MRet scores candidates through personalized retention curves but does not allocate observed N7 to past swipes, matches, or conversations; under the D3 rubric it is NOT attribution.

## 2. Retention-targeted methods — feed recommenders (RL/flow, per-item scores, ranking) (10 papers)

### Save, Revisit, Retain (AAAI 2026)

- Detailed analysis: [read-papers/2026_AAAI_RevisitMTL_Save-Revisit-Retain.md](read-papers/2026_AAAI_RevisitMTL_Save-Revisit-Retain.md)

Jiang et al., *Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems*, AAAI 2026 links a saved Pin to 0–6-day revisitation and production retention metrics. It produces an item surrogate but acknowledges intent, notification, and UI confounding; classification: PARTIAL.

### Interpretable User Retention Modeling in Recommendation (RecSys 2023)

- Detailed analysis: [read-papers/2023_RecSys_IURO_Interpretable-User-Retention-Modeling.md](read-papers/2023_RecSys_IURO_Interpretable-User-Retention-Modeling.md)

Ding et al., *Interpretable User Retention Modeling in Recommendation*, RecSys 2023 assigns each historical interaction a retention score and aggregates scores through multi-instance attention for next-3-day retention. It is a useful but noncausal PARTIAL attribution method.

### Rethinking User Retention Modeling in Recommendation (TOIS 2026)

- Detailed analysis: [read-papers/2026_TOIS_IURO+_Rethinking-User-Retention-Modeling.md](read-papers/2026_TOIS_IURO+_Rethinking-User-Retention-Modeling.md)

Ding et al., *Rethinking User Retention Modeling in Recommendation*, TOIS 2026 extends IURO’s item scorer and BCMIL training. The paper explicitly recognizes weak causality and the absence of item-level ground truth; classification: PARTIAL.

### Future Impact Decomposition in Request-level Recommendations (KDD 2024)

- Detailed analysis: [read-papers/2024_KDD_FID_Future-Impact-Decomposition.md](read-papers/2024_KDD_FID_Future-Impact-Decomposition.md)

Wang et al., *Future Impact Decomposition in Request-level Recommendations*, KDD 2024 decomposes a slate-level actor-critic target into item-level delayed-value advantages and reports next-week retention and DAU lifts in production. Under the D3 rubric this is PARTIAL (item-level delayed scores without identified causal MTA), not TRUE: the scores update an RL policy and are not a reusable causal retention-credit table.

### Modeling User Retention through Generative Flow Networks (KDD 2024)

- Detailed analysis: [read-papers/2024_KDD_GFN4Retention_Modeling-User-Retention.md](read-papers/2024_KDD_GFN4Retention_Modeling-User-Retention.md)

Liu et al., *Modeling User Retention through Generative Flow Networks*, KDD 2024 propagates terminal return rewards through trajectory flows. Contrary to the related-notebook answer, it learns a recommendation policy and does not publish per-item retention labels; classification: NOT.

### Reinforcing User Retention in a Billion Scale Short Video Recommender System (WWW 2023)

- Detailed analysis: [read-papers/2023_WWW_RLUR_Reinforcing-User-Retention.md](read-papers/2023_WWW_RLUR_Reinforcing-User-Retention.md)

Cai et al., *Reinforcing User Retention in a Billion Scale Short Video Recommender System*, WWW 2023 explicitly says item-level retention decomposition is difficult. Its DDPG critic optimizes request-level ranking weights; classification: NOT.

### AURO (WWW 2025)

- Detailed analysis: [read-papers/2025_WWW_AURO_Adaptive-User-Retention-Optimization.md](read-papers/2025_WWW_AURO_Adaptive-User-Retention-Optimization.md)

Xue et al., *AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems*, WWW 2025 adapts a continuous-action policy to nonstationary return-time dynamics. It yields no historical touch-credit table; classification: NOT.

### Stratified Expert Cloning (CIKM 2025)

- Detailed analysis: [read-papers/2025_CIKM_SEC_Stratified-Expert-Cloning.md](read-papers/2025_CIKM_SEC_Stratified-Expert-Cloning.md)

Lin et al., *Stratified Expert Cloning for Retention-Aware Recommendation at Scale*, CIKM 2025 bypasses delayed credit assignment by cloning high-retention trajectories. It is policy optimization, not attribution; classification: NOT.

### Learned Ranking Function (RecSys 2024)

- Detailed analysis: [read-papers/2024_RecSys_LRF_Learned-Ranking-Function-YouTube.md](read-papers/2024_RecSys_LRF_Learned-Ranking-Function-YouTube.md)

Wu et al., *Learned Ranking Function: From Short-term Behavior Predictions to Long-term User Satisfaction*, RecSys 2024 produces a candidate ranking score from click, abandonment, and long-term reward predictions. It does not explain an observed retention outcome across prior touches; classification: NOT.

### Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning (arXiv 2026)

- Detailed analysis: [read-papers/2026_arXiv_DownstreamRewards_Long-Term-Engagement-Optimization.md](read-papers/2026_arXiv_DownstreamRewards_Long-Term-Engagement-Optimization.md)

Wang et al., *Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning*, arXiv 2026 predicts candidate-level downstream-session surrogates for Pinterest rankers. Those predicted rewards are policy inputs, not retention attribution; classification: NOT.

## 3. Notification incrementality (2 papers)

### Incrementality-Focused Messaging Measurement (industry blog 2023)

- Detailed analysis: [read-papers/2023_NetflixBlog_NA_Incrementality-Focused-Messaging-Measurement.md](read-papers/2023_NetflixBlog_NA_Incrementality-Focused-Messaging-Measurement.md)

Netflix, *Incrementality-Focused Messaging Measurement*, industry blog 2023 reportedly uses message withholding to estimate downstream viewing. The card is an `nlm:failed` stub, so no discovery one-liner is treated as a measured result. It remains PARTIAL because the touch is a notification and the outcome is viewing, not per-swipe N7.

### A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications (KDD 2020)

- Detailed analysis: [read-papers/2020_KDD_RDSA_Sleeping-Recovering-Bandit-Notifications.md](read-papers/2020_KDD_RDSA_Sleeping-Recovering-Bandit-Notifications.md)

Yancey and Settles, *A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications*, KDD 2020 corrects eligibility bias with IPW and models fatigue with recency decay. It produces notification-arm policy scores, not multi-touch retention credit; classification: NOT.

## 4. Industry attribution systems 2025–2026 (experiment-calibrated, causal, LLM, multi-attribution) (4 papers)

### ALM-MTA (arXiv 2026)

- Detailed analysis: [read-papers/2026_ICLR_ALM-MTA_Front-Door-Causal-Multi-Touch-Attribution.md](read-papers/2026_ICLR_ALM-MTA_Front-Door-Causal-Multi-Touch-Attribution.md)

Liu et al., *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization*, arXiv 2026 combines front-door identification, proxy mediation, contrastive overlap control, IPW, and per-touch deletion scores. It is the strongest causal MTA mechanism but attributes upload rather than retention; Q2 classification: NOT.

### Buyer Journey Insights with Data-Driven Attribution (LinkedIn Engineering 2025)

- Detailed analysis: [read-papers/2025_LinkedIn_LiDDA_Buyer-Journey-Data-Driven-Attribution.md](read-papers/2025_LinkedIn_LiDDA_Buyer-Journey-Data-Driven-Attribution.md)

Bencina et al., *Buyer Journey Insights with Data-Driven Attribution*, LinkedIn Engineering 2025 uses normalized Transformer attention, paid-impression imputation, and experiment/MMM post-calibration. It is production conversion MTA, not retention attribution; Q2 classification: NOT.

### Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution? (CIKM 2026)

- Detailed analysis: [read-papers/2026_CIKM_LOTUS_Meaningful-Touchpoints-Conversion-Attribution.md](read-papers/2026_CIKM_LOTUS_Meaningful-Touchpoints-Conversion-Attribution.md)

Wu et al., *Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?*, CIKM 2026 uses pairwise/listwise LLM reasoning to select explicit and implicit purchase touchpoints and generate normalized conversion weights. It has no causal calibration and does not target retention; Q2 classification: NOT.

### Integrated Marketing Attribution (arXiv 2026)

- Detailed analysis: [read-papers/2026_arXiv_IMA_Integrated-Marketing-Attribution.md](read-papers/2026_arXiv_IMA_Integrated-Marketing-Attribution.md)

Bhat et al., *Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM*, arXiv 2026 disaggregates weekly MMM contributions into daily campaign effects. It is privacy-safe aggregate attribution, not user-touch or retention attribution; Q2 classification: NOT.

## 5. Incrementality measurement and evaluation devices (2 papers)

### Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking (KDD 2025)

- Detailed analysis: [read-papers/2025_KDD_NA_Interleaving-Counterfactual-Airbnb-Search.md](read-papers/2025_KDD_NA_Interleaving-Counterfactual-Airbnb-Search.md)

Zhang et al., *Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking*, KDD 2025 combines team-draft interleaving and position-aware counterfactual estimators. It is a strong validation device but does not produce persistent retention credit; classification: NOT.

### Incremental Recommendation via Causal Models (arXiv 2026)

- Detailed analysis: [read-papers/2026_arXiv_NA_Incremental-Recommendation-Causal-Models.md](read-papers/2026_arXiv_NA_Incremental-Recommendation-Causal-Models.md)

Vlontzos et al., *Incremental Recommendation via Causal Models*, arXiv 2026 uses holdbacks and treated/organic models to suppress recommendations to always-takers. Because its windows differ, it does not claim a valid pointwise \(p_1-p_0\) CATE and does not assign retention credit to histories; classification: NOT.

## 6. Long-term outcome estimation (surrogate index and variants) (5 papers)

### Impatient Bandits (JMLR 2026)

- Detailed analysis: [read-papers/2025_JMLR_ImpatientBandits_Optimizing-Recommendations-Long-Term.md](read-papers/2025_JMLR_ImpatientBandits_Optimizing-Recommendations-Long-Term.md)

Zhang et al., *Impatient Bandits: Optimizing for the Long-Term Without Delay*, JMLR 2026 updates 60-day active-day beliefs as daily feedback arrives. It optimizes content selection and does not retrospectively decompose retention; classification: NOT.

### Surrogate for Long-Term User Experience in Recommender Systems (KDD 2022)

- Detailed analysis: [read-papers/2022_KDD_NA_Surrogate-Long-Term-User-Experience.md](read-papers/2022_KDD_NA_Surrogate-Long-Term-User-Experience.md)

Wang et al., *Surrogate for Long-Term User Experience in Recommender Systems*, KDD 2022 connects medium-term behavior patterns with five-month visiting frequency and uses them as RL reward multipliers. It is surrogate policy optimization, not attribution; classification: NOT.

### Long-run User Value Optimization through Content Creation Modeling (arXiv 2022)

- Detailed analysis: [read-papers/2022_arXiv_NA_Long-run-User-Value-Optimization-Meta.md](read-papers/2022_arXiv_NA_Long-run-User-Value-Optimization-Meta.md)

Lada et al., *Long-run User Value Optimization in Recommender Systems through Content Creation Modeling*, arXiv 2022 estimates producer-level heterogeneous treatment effects from a distribution-boost experiment. It is causal at the producer treatment level, not per-consumer interaction; classification: NOT.

### Break the Inaccessible Boundary (arXiv 2026)

- Detailed analysis: [read-papers/2026_arXiv_OCARM_Post-Conversion-Content-Retention.md](read-papers/2026_arXiv_OCARM_Post-Conversion-Content-Retention.md)

Ma et al., *Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling*, arXiv 2026 distills future onboarding-content representations into a bidding-time retention predictor. It outputs user/ad-context predictions, not interaction credit; classification: NOT.

### DCEO (arXiv 2026)

- Detailed analysis: [read-papers/2026_arXiv_DCEO_Direct-Causal-Effect-Optimization.md](read-papers/2026_arXiv_DCEO_Direct-Causal-Effect-Optimization.md)

Zhang et al., *DCEO: Direct Causal Effect Optimization for Long-Term User Value Modeling in E-commerce Search*, arXiv 2026 optimizes the relative causal effect of an aggregate proxy on four-day value. It neither targets retention nor decomposes a historical journey; classification: NOT.

## References (Low Relevance)

- Zhao et al., *User Retention-oriented Recommendation with Decision Transformer*, WWW 2023 — [card](read-papers/2023_WWW_DT4Rec_User-Retention-Oriented-Decision-Transformer.md). Offline policy generation; NOT attribution.
- Authors not reported in the card, *Sequential Recommendation for Optimizing Both Immediate Feedback and Long-term Retention*, arXiv 2024 — [card](read-papers/2024_arXiv_NA_Sequential-Rec-Immediate-Feedback-Long-term-Retention.md). Offline Decision Transformer; NOT attribution.
- Netflix, *A Human-Augmenting Agentic Workflow for Causal Inference*, Netflix Technology Blog 2026 — [card](read-papers/2026_NetflixBlog_oci-agent_Causal-Inference-Workflow.md). Stub card for treatment-level causal tooling; NOT per-touch attribution.
