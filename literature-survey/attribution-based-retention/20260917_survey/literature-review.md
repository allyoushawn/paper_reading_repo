Date: 2026-09-17  
Topic: Attribution-based retention  
Paper count: 50 cards

# Attribution-based Retention Literature Review

## Executive Summary

The strongest evidence supports replacing last-touch with per-interaction sequence credit calibrated to randomized outcomes. *Interpretable User Retention Modeling in Recommendation* supplies direct per-item retention scores; *Modeling User Retention through Generative Flow Networks* propagates terminal retention through earlier steps; *ALM-MTA* adds counterfactual deletion and front-door deconfounding; and *Downstream Rewards* supplies a practical user-prevalence correction. No named dating company published a production per-swipe retention-attribution system, although *MRet* and *Not All Matches Are Equally Valuable* provide two-sided retention-shaping evidence.

### Most Promising Approaches

1. Causal removal effects: explicit per-touch credit with experimental or front-door identification.
2. Retention-flow and attention credit: distribute delayed outcomes across non-last interactions.
3. Debiased downstream rewards: create practical dense labels while controlling user activity prevalence.

### Practical Recommendations

Short term (1–3 months):

- Build a removal-effect sequence attributor with event-type embeddings, rolling N7 labels, user-prevalence normalization, and randomized validation.

Mid term (3–6 months):

- Add propensity/outcome heads, a return-time survival head, and experiment-based aggregate calibration; reserve front-door/flow matching for v3.

---

## 1. Retention credited to individual interactions — reciprocal / two-sided platforms (3 papers)

These papers show that match value is concave and bilateral, but the cards correct NotebookLM’s characterization: MRet and Wantedly optimize future allocation; they do not perform retrospective per-match attribution.

### Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method (KDD 2024)

- Source: KDD 2024
- Detailed analysis: [read-papers/2024_KDD_CRRS_Revisiting-Reciprocal-Recommender-Systems-Metrics-Formulation-Method.md](read-papers/2024_KDD_CRRS_Revisiting-Reciprocal-Recommender-Systems-Metrics-Formulation-Method.md)

*Revisiting Reciprocal Recommender Systems* models bilateral recommendation treatments and vacant-slot opportunity cost, but its outcome is a match rather than retention.

### Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching (ICLR 2026)

- Source: ICLR 2026
- Detailed analysis: [read-papers/2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md](read-papers/2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md)

*MRet* learns concave retention-versus-match-count curves and reaches about 66.5% retention in an offline evaluation on imputed real dating-platform logs, not a live test. Contrary to the NotebookLM synthesis, the card identifies it as forward ranking, not retrospective per-match credit.

### Not All Matches Are Equally Valuable (RecSys in HR 2026)

- Source: RecSys in HR Workshop 2026
- Detailed analysis: [read-papers/2026_RecSysHR_WantedlyChurnBoost_Not-All-Matches-Are-Equally-Valuable.md](read-papers/2026_RecSysHR_WantedlyChurnBoost_Not-All-Matches-Are-Equally-Valuable.md)

*Not All Matches Are Equally Valuable* boosts low-match users and reports churn odds ratios of 0.957 and 0.948. The card says both results were directionally favorable but statistically insignificant, and the method does not attribute churn to individual matches.

---

## 2. Retention credited to individual interactions — feed recommenders (11 papers)

This category contains the closest direct mechanisms: per-item retention scores, step-wise retention flow, delayed-reward critics, downstream proxies, and learned item-level LTV weights.

### Interpretable User Retention Modeling in Recommendation (RecSys 2023)

- Source: RecSys 2023
- Detailed analysis: [read-papers/2023_RecSys_IURO_Interpretable-User-Retention-Modeling.md](read-papers/2023_RecSys_IURO_Interpretable-User-Retention-Modeling.md)

*IURO* computes a retention score for each historical item and uses attention and contrastive “aha item” learning. It improved WeChat next-day retention by 0.76% and next-three-day retention by 0.65%.

### Modeling User Retention through Generative Flow Networks (KDD 2024)

- Source: KDD 2024
- Detailed analysis: [read-papers/2024_KDD_GFN4Retention_Modeling-User-Retention-Generative-Flow-Networks.md](read-papers/2024_KDD_GFN4Retention_Modeling-User-Retention-Generative-Flow-Networks.md)

*GFN4Retention* uses detailed-balance flow matching to propagate terminal return reward to non-last recommendation steps. Its Kuaishou test improved first-stage next-day retention by 0.015% overall and 0.069% for low-activity users; a second-stage deployment showed +0.002% (not significant).

### Reinforcing User Retention in a Billion Scale Short Video Recommender System (WWW 2023)

- Source: WWW 2023
- Detailed analysis: [read-papers/2023_WWW_RLUR_Reinforcing-User-Retention-Billion-Scale-Short-Video-Recommender.md](read-papers/2023_WWW_RLUR_Reinforcing-User-Retention-Billion-Scale-Short-Video-Recommender.md)

*RLUR* assigns implicit value at each request through a retention critic, activity cohorts, and return-time normalization. It improved Kuaishou DAU by 0.20% and seventh-day retention by 0.063%, but it does not emit per-item fractional labels.

### User Retention-oriented Recommendation with Decision Transformer (WWW 2023)

- Source: WWW 2023
- Detailed analysis: [read-papers/2023_WWW_DT4Rec_User-Retention-Oriented-Recommendation-Decision-Transformer.md](read-papers/2023_WWW_DT4Rec_User-Retention-Oriented-Recommendation-Decision-Transformer.md)

*DT4Rec* conditions sequence generation on future active days. It is retention-aware policy learning, not credit decomposition; removal masking or a separate attribution layer would be required.

### Coarse-to-fine Dynamic Uplift Modeling for Real-time Video Recommendation (RecSys 2025)

- Source: RecSys 2025
- Detailed analysis: [read-papers/2025_RecSys_CDUM_Coarse-to-fine-Dynamic-Uplift-Modeling.md](read-papers/2025_RecSys_CDUM_Coarse-to-fine-Dynamic-Uplift-Modeling.md)

*CDUM* estimates request-level treatment effects with offline long-term preferences and real-time correction. Its live test reported Enter LT7 +0.048%, but the treatment is a recommendation strategy rather than one item.

### AURO: Reinforcement Learning for Adaptive User Retention Optimization (WWW 2025)

- Source: WWW 2025
- Detailed analysis: [read-papers/2025_WWW_AURO_Adaptive-User-Retention-Optimization-RL.md](read-papers/2025_WWW_AURO_Adaptive-User-Retention-Optimization-RL.md)

*AURO* uses value-based state abstraction and guarded exploration under non-stationarity. Its per-action Q-values are useful precursors, but the method does not generate retrospective fractional credit.

### Stratified Expert Cloning for Retention-Aware Recommendation at Scale (CIKM 2025)

- Source: CIKM 2025
- Detailed analysis: [read-papers/2025_CIKM_SEC_Stratified-Expert-Cloning-Retention-Aware-Recommendation.md](read-papers/2025_CIKM_SEC_Stratified-Expert-Cloning-Retention-Aware-Recommendation.md)

*SEC* stratifies retention experts and prevents policy collapse. It improved cumulative active days by 0.098% and 0.122% on two Kuaishou products, but it clones policies rather than assigning interaction credit.

### Save, Revisit, Retain (AAAI 2026)

- Source: AAAI 2026
- Detailed analysis: [read-papers/2025_arXiv_PinterestSRR_Save-Revisit-Retain-Scalable-Retention-Framework.md](read-papers/2025_arXiv_PinterestSRR_Save-Revisit-Retain-Scalable-Retention-Framework.md)

*Save, Revisit, Retain* assigns a same-item revisit surrogate to each saved Pin. It offers scalable single-touch attribution and raised active-user propensity by 0.08%, but it does not split app-level retention across multiple items.

### Retentive Relevance: Capturing Long-Term User Value in Recommendation Systems (arXiv 2025)

- Source: arXiv 2025
- Detailed analysis: [read-papers/2025_arXiv_RetentiveRelevance_Capturing-Long-Term-User-Value.md](read-papers/2025_arXiv_RetentiveRelevance_Capturing-Long-Term-User-Value.md)

*Retentive Relevance* predicts per-item return intent, corrects survey non-response with CBPS, and increased sessions per user by 0.030%. It ranks items by a retention proxy rather than decomposing realized retention.

### Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning (RecSys 2026)

- Source: RecSys 2026
- Detailed analysis: [read-papers/2026_RecSys_DownstreamRewards_Long-Term-User-Engagement-Optimization-Model-Agnostic-Downstream-Rewards.md](read-papers/2026_RecSys_DownstreamRewards_Long-Term-User-Engagement-Optimization-Model-Agnostic-Downstream-Rewards.md)

*Downstream Rewards* predicts per-impression downstream trajectories and uses User-Prevalence normalization to remove heavy-user exposure bias. Successful sessions improved by up to 0.36%; the card says the method remains proxy reward learning, not complete multi-touch attribution.

### A Long-term Value Prediction Framework in Video Ranking (WWW 2026)

- Source: WWW 2026
- Detailed analysis: [read-papers/2026_arXiv_TaobaoLTV_Long-term-Value-Prediction-Framework-Video-Ranking.md](read-papers/2026_arXiv_TaobaoLTV_Long-term-Value-Prediction-Framework-Video-Ranking.md)

*Taobao LTV* learns per-video downstream attribution weights, applies position-aware quantile debiasing, and co-trains delayed seven-day author value. Its Author Time variant improved LT3 by 0.21%.

---

## 3. Notification incrementality (3 papers)

Notification work gives the cleanest randomized single-action uplift precedent, although it does not solve multi-touch splitting.

### User State-based Notification Volume Optimization (Pinterest Engineering 2020)

- Source: Pinterest Engineering 2020
- Detailed analysis: [read-papers/2020_PinterestEngBlog_NotificationVolumeOptimization_User-State-Based-Notification-Volume-Optimization.md](read-papers/2020_PinterestEngBlog_NotificationVolumeOptimization_User-State-Based-Notification-Volume-Optimization.md)

*User State-based Notification Volume Optimization* allocates cohort-level notification budgets and improved WAU by 1%. It has no per-notification causal credit.

### Improving Instagram Notification Management with Machine Learning and Causal Inference (Meta Engineering 2022)

- Source: Meta Engineering 2022
- Detailed analysis: [read-papers/2022_MetaBlog_IGNotif_Instagram-Notification-Causal-Management.md](read-papers/2022_MetaBlog_IGNotif_Instagram-Notification-Causal-Management.md)

*Instagram Notification Management* estimates `P(active|send) − P(active|drop)` from 50/50 randomized logs. It is a direct template for incremental candidate value, but only for one binary action.

### HGenPush (KDD 2026)

- Source: KDD 2026
- Detailed analysis: [read-papers/2026_KDD_HGenPush_Heterogeneous-Generative-Recommendation-Push-Notifications.md](read-papers/2026_KDD_HGenPush_Heterogeneous-Generative-Recommendation-Push-Notifications.md)

*HGenPush* optimizes post-click session quality with group-relative rewards and increased DAU by 0.181%. It is a notification generator and ranker, not a retention-attribution system.

---

## 4. Industry attribution systems 2025–2026 (14 papers)

The current industry frontier combines experiments with observational models, models incrementality rather than response, and uses sequence, semantic, or aggregate priors where raw touch logs are incomplete.

### Smarter Promotions with Causal Machine Learning (DoorDash Engineering 2025)

- Source: DoorDash Engineering 2025
- Detailed analysis: [read-papers/2025_DoorDashBlog_CausalPromotions_Smarter-Promotions-With-Causal-Machine-Learning.md](read-papers/2025_DoorDashBlog_CausalPromotions_Smarter-Promotions-With-Causal-Machine-Learning.md)

*Smarter Promotions* uses Double ML to separate persuadables from always-buyers and achieved near-equal incremental orders at roughly half the cost.

### Optimizing DoorDash’s Marketing Spend with Machine Learning (DoorDash Engineering; date disputed)

- Source: DoorDash Engineering, page byline 2020 versus supplied 2025 metadata
- Detailed analysis: [read-papers/2025_DoorDashBlog_MarketingSpendML_Optimizing-Marketing-Spend-With-Machine-Learning.md](read-papers/2025_DoorDashBlog_MarketingSpendML_Optimizing-Marketing-Spend-With-Machine-Learning.md)

*Optimizing DoorDash’s Marketing Spend* retains modified last-touch at channel level. Because the card reports an unresolved date discrepancy and no per-touch debiasing, it is negative rather than state-of-the-art evidence.

### A Large Scale Heterogeneous Treatment Effect Estimation Framework at Snap (arXiv 2025)

- Source: Snap, arXiv 2025
- Detailed analysis: [read-papers/2025_arXiv_SnapHTE_Large-Scale-Heterogeneous-Treatment-Effect-Users-Journey-Snap.md](read-papers/2025_arXiv_SnapHTE_Large-Scale-Heterogeneous-Treatment-Effect-Users-Journey-Snap.md)

*Snap HTE* trains T-learners on randomized ITT logs and incrementally refreshes production models. It estimates user-level influenceability or sensitivity, not touch-level credit.

### Highlights of Booking.com’s Publication in 2025 (Booking.com 2026)

- Source: Booking.com 2026
- Detailed analysis: [read-papers/2026_BookingAIBlog_2025PublicationHighlights_Highlights-of-Booking-Com-Publication-in-2025.md](read-papers/2026_BookingAIBlog_2025PublicationHighlights_Highlights-of-Booking-Com-Publication-in-2025.md)

*Booking.com’s 2025 Highlights* describes causal promotion work and converted-only estimation. The summary supplies no quantitative result and converted-only filtering would be unsuitable for retention.

### Sequential Multimodal Evidence Optimization (CIKM 2026)

- Source: Amazon, CIKM 2026
- Detailed analysis: [read-papers/2026_CIKM_SMEO_Sequential-Multimodal-Evidence-Optimization-Product-Media-Ranking.md](read-papers/2026_CIKM_SMEO_Sequential-Multimodal-Evidence-Optimization-Product-Media-Ranking.md)

*SMEO* handles endogenous truncation and position bias, then derives per-asset credit by masking. It achieved +5.4% DR-CVR, an offline off-policy estimate, and 15.3% fewer swipes to conversion offline; serving uses precomputed values, not a live conversion lift.

### ALM-MTA (ICLR 2026)

- Source: Kuaishou, ICLR 2026
- Detailed analysis: [read-papers/2026_ICLR_ALM-MTA_Front-Door-Causal-Multi-Touch-Attribution-Creator-Ecosystem.md](read-papers/2026_ICLR_ALM-MTA_Front-Door-Causal-Multi-Touch-Attribution-Creator-Ecosystem.md)

*ALM-MTA* assigns touchpoint deletion credit under a learned front-door mediator. It improved DAU by 0.04% and daily active creators by 0.6% at 400M DAU.

### CanniUplift (KDD 2026)

- Source: Alibaba/Taobao, KDD 2026
- Detailed analysis: [read-papers/2026_KDD_CanniUplift_Mitigating-Seller-Incentive-Cannibalization-Ecommerce-Uplift-Modeling.md](read-papers/2026_KDD_CanniUplift_Mitigating-Seller-Incentive-Cannibalization-Ecommerce-Uplift-Modeling.md)

*CanniUplift* removes pseudo-incrementality through redemption decomposition and constrains local predictions to platform totals. Its online test improved incremental GMV by 4.08%.

### Attributed, But Not Incremental (ADKDD 2026)

- Source: TikTok, ADKDD 2026
- Detailed analysis: [read-papers/2026_arXiv_CannibalizationMTA_Attributed-But-Not-Incremental-TikTok.md](read-papers/2026_arXiv_CannibalizationMTA_Attributed-But-Not-Incremental-TikTok.md)

*Attributed, But Not Incremental* calibrates daily observational attribution to sparse randomized lift and reduces calibration error by 91.38%. Its unit is channel-day, so it supplies a calibration pattern rather than a swipe estimator.

### Heterogeneous Multi-treatment Uplift Modeling (arXiv 2026)

- Source: Kuaishou, arXiv 2026
- Detailed analysis: [read-papers/2026_arXiv_HMUM_Heterogeneous-Multi-treatment-Uplift-Modeling-Trade-off.md](read-papers/2026_arXiv_HMUM_Heterogeneous-Multi-treatment-Uplift-Modeling-Trade-off.md)

*HMUM* learns request-level treatment effects from RCT logs and aligns control representations across branches. Live usage-time lifts ranged from 0.044% to 0.073%.

### Integrated Marketing Attribution (arXiv 2026)

- Source: Lowe’s, arXiv 2026
- Detailed analysis: [read-papers/2026_arXiv_IMA-BayesianMMM_Integrated-Marketing-Attribution-Bayesian-Framework-Privacy-Safe-MMM.md](read-papers/2026_arXiv_IMA-BayesianMMM_Integrated-Marketing-Attribution-Bayesian-Framework-Privacy-Safe-MMM.md)

*Integrated Marketing Attribution* uses MMM estimates as priors for granular campaign attribution. Its macro-to-micro shrinkage pattern is useful, but it has no user-level interaction logs.

### Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution? (CIKM 2026)

- Source: Alibaba/Taobao, CIKM 2026
- Detailed analysis: [read-papers/2026_arXiv_LLMTouchpointSelection_Can-LLMs-Identify-Meaningful-Touchpoints-in-Conversion-Attribution.md](read-papers/2026_arXiv_LLMTouchpointSelection_Can-LLMs-Identify-Meaningful-Touchpoints-in-Conversion-Attribution.md)

*LOTUS/SILVA* separates touchpoint selection from allocation and finds 14.91% implicitly related touchpoints missed by rules. It improves production CVR GAUC by 0.35pp but does not establish causal retention credit.

### From Prediction to Incrementality (arXiv 2026)

- Source: LinkedIn, arXiv 2026
- Detailed analysis: [read-papers/2026_arXiv_PredictionToIncrementality_Causal-Optimization-Large-Scale-Targeting-Recommendation.md](read-papers/2026_arXiv_PredictionToIncrementality_Causal-Optimization-Large-Scale-Targeting-Recommendation.md)

*From Prediction to Incrementality* combines a sequence Transformer, DragonNet, exploration, and constrained allocation. It explicitly randomizes snapshot dates to avoid last-touch labels and reports +7.20% LTV.

### Multi-channel Uplift Policy Learning (arXiv 2026)

- Source: Alibaba/Taobao, arXiv 2026
- Detailed analysis: [read-papers/2026_arXiv_ReAlloc_Multi-channel-Uplift-Policy-Learning.md](read-papers/2026_arXiv_ReAlloc_Multi-channel-Uplift-Policy-Learning.md)

*ReAlloc* uses DML orthogonalization and support-aware conservative policy improvement. It improved pay orders by 3.53% (GMV −2.64%), but its object is a budget simplex, not a touch sequence.

### Fisher-Market Fractional Credit Assignment (arXiv 2026)

- Source: arXiv 2026
- Detailed analysis: [read-papers/2026_arXiv_AttributionMarkets_Fisher-Market-Fractional-Credit-Assignment.md](read-papers/2026_arXiv_AttributionMarkets_Fisher-Market-Fractional-Credit-Assignment.md)

*Fisher-Market Fractional Credit Assignment* guarantees conservation, hard caps, and exact zero credit for junk actions. It is theoretical and has no retention or production evidence.

---

## 5. Incrementality measurement and privacy-era attribution (6 papers)

These papers establish the validation principle: granular observational credit should be checked against randomized or quasi-experimental aggregate lift.

### Impact of Organic Ranking on Ad Click Incrementality (retrieved page dated 2012)

- Source: Google Research
- Detailed analysis: [read-papers/2026_GoogleBlog_OrganicRankIncrementality_Impact-Of-Organic-Ranking-On-Ad-Click-Incrementality.md](read-papers/2026_GoogleBlog_OrganicRankIncrementality_Impact-Of-Organic-Ranking-On-Ad-Click-Incrementality.md)

*Impact of Organic Ranking* uses 390 pause studies and shows incrementality depends on organic rank. The card contradicts the 2026 batch metadata: the retrieved page is dated 2012, so it is not current Q1 evidence.

### Meridian GeoX (Google Research 2026)

- Source: Google Research 2026
- Detailed analysis: [read-papers/2026_GoogleResearch_MeridianGeoX_Open-Source-Framework-Precision-Efficiency-Geo-Experiments.md](read-papers/2026_GoogleResearch_MeridianGeoX_Open-Source-Framework-Precision-Efficiency-Geo-Experiments.md)

*Meridian GeoX* combines stratification, synthetic controls, and design-aware placebo inference. It supports rollout validation, not per-interaction attribution.

### Media Measurement and the Assisted Own Goal (arXiv 2026)

- Source: GrowthLoop, arXiv 2026
- Detailed analysis: [read-papers/2026_arXiv_AssistedOwnGoal_Attribution-Marketing-Mix-Models-Individual-Level-Incrementality.md](read-papers/2026_arXiv_AssistedOwnGoal_Attribution-Marketing-Mix-Models-Individual-Level-Incrementality.md)

*Assisted Own Goal* shows that visible-touch reweighting cannot recover outcomes completed elsewhere. Its salted-hash ITT system recovered simulated true lift while last-touch undercounted it by 63.3%.

### Privacy-Robust Incrementality Measurement under Signal Loss (arXiv 2026)

- Source: arXiv 2026
- Detailed analysis: [read-papers/2026_arXiv_PrivacyRobustIncrementality_Privacy-Robust-Incrementality-Measurement-Advertising-Signal-Loss.md](read-papers/2026_arXiv_PrivacyRobustIncrementality_Privacy-Robust-Incrementality-Measurement-Advertising-Signal-Loss.md)

*Privacy-Robust Incrementality* returns Certify, Reject, or Unresolved bounds rather than forced point estimates. It is a measurement-certification layer, not attribution.

### Pseudo-Incrementality Testing (arXiv 2026)

- Source: arXiv 2026
- Detailed analysis: [read-papers/2026_arXiv_PseudoIncrementality_Measuring-Advertising-Lift-Naturally-Occurring-Interventions.md](read-papers/2026_arXiv_PseudoIncrementality_Measuring-Advertising-Lift-Naturally-Occurring-Interventions.md)

*Pseudo-Incrementality Testing* turns operational changes into screened quasi-experiments and recovered GeoLift benchmarks within reported uncertainty. Its aggregate time-series unit does not transfer directly to swipes.

### Update on Plans for Privacy Sandbox Technologies (Google 2025)

- Source: Google 2025
- Detailed analysis: [read-papers/2025_GoogleBlog_PrivacySandboxUpdate_Attribution-Reporting-API-Retired.md](read-papers/2025_GoogleBlog_PrivacySandboxUpdate_Attribution-Reporting-API-Retired.md)

*Privacy Sandbox Update* retires several browser attribution APIs because of low adoption. It supplies industry context, not a model.

---

## 6. Long-term outcome estimation (surrogate index and variants) (7 papers)

These methods reduce delayed-label variance and latency. They should supplement, not replace, a touch-level causal estimator.

### From Clicks to Conversions: Recommendation for Long-term Reward (REVEAL 2020)

- Source: REVEAL 2020
- Detailed analysis: [read-papers/2020_arXiv_ClicksToConversions_Recommendation-For-Long-Term-Reward.md](read-papers/2020_arXiv_ClicksToConversions_Recommendation-For-Long-Term-Reward.md)

*From Clicks to Conversions* critiques last-click as correlated rather than causal reward shaping and proposes discounted credit in simulation. It has no production evidence.

### How Airbnb Measures Future Value to Standardize Tradeoffs (Airbnb Engineering 2021)

- Source: Airbnb Engineering 2021
- Detailed analysis: [read-papers/2021_AirbnbEngBlog_FutureIncrementalValue_How-Airbnb-Measures-Future-Value-To-Standardize-Tradeoffs.md](read-papers/2021_AirbnbEngBlog_FutureIncrementalValue_How-Airbnb-Measures-Future-Value-To-Standardize-Tradeoffs.md)

*Future Incremental Value* applies propensity-score matching to 150+ actions and long-run value. It addresses “would happen anyway” bias, but one action type at a time.

### Impatient Bandits: Optimizing Recommendations for the Long-Term Without Delay (KDD 2023)

- Source: KDD 2023
- Detailed analysis: [read-papers/2023_KDD_ImpatientBandits_Optimizing-Recommendations-Long-Term-Without-Delay.md](read-papers/2023_KDD_ImpatientBandits_Optimizing-Recommendations-Long-Term-Without-Delay.md)

*Impatient Bandits* uses progressive daily traces and Bayesian filtering to forecast 60-day engaged days. It is item-level delayed-reward learning, not user-touch attribution.

### Optimizing for the Long-Term Without Delay (Spotify Research 2023)

- Source: Spotify Research 2023
- Detailed analysis: [read-papers/2023_SpotifyBlog_ImpatientBandit_Optimizing-Long-Term-Without-Delay.md](read-papers/2023_SpotifyBlog_ImpatientBandit_Optimizing-Long-Term-Without-Delay.md)

The Spotify blog card describes the same *Impatient Bandits* method and emphasizes that short-term proxies plateau at non-zero regret.

### Estimating Long-term Outcome of Algorithms (Spotify Research/WWW 2024)

- Source: Spotify Research and WWW 2024
- Detailed analysis: [read-papers/2024_SpotifyBlog_LongTermOutcome_Estimating-Long-Term-Outcome-Of-Algorithms.md](read-papers/2024_SpotifyBlog_LongTermOutcome_Estimating-Long-Term-Outcome-Of-Algorithms.md)

*LOPE* combines short-term surrogate effects with residual action effects. It reduces MSE by 36% versus doubly robust OPE and 71% versus long-term causal inference in reported settings.

### The Surrogate Index (Review of Economic Studies 2025)

- Source: Review of Economic Studies 2025
- Detailed analysis: [read-papers/2025_REStud_SurrogateIndex_Combining-Short-Term-Proxies-Long-Term-Treatment-Effects.md](read-papers/2025_REStud_SurrogateIndex_Combining-Short-Term-Proxies-Long-Term-Treatment-Effects.md)

*The Surrogate Index* combines multiple short-term proxies and matches long-run RCT effects much earlier. It estimates a treatment-level effect, not fractional touch credit.

### The Proximal Surrogate Index (arXiv 2026)

- Source: arXiv 2026
- Detailed analysis: [read-papers/2026_arXiv_ProximalSurrogateIndex_Long-Term-Treatment-Effects-Unobserved-Confounding.md](read-papers/2026_arXiv_ProximalSurrogateIndex_Long-Term-Treatment-Effects-Unobserved-Confounding.md)

*The Proximal Surrogate Index* uses dual proxies and bridge functions to recover long-term effects under unobserved confounding. Its Job Corps estimate recovered the RCT benchmark where the ordinary surrogate index underestimated by more than 50%.

## References (Low Relevance)

### Round 2: A Survey of Causal Inference Applications at Netflix

- Source: Netflix TechBlog, unverified
- Detailed analysis: [read-papers/2023_NetflixTechBlog_CausalInferenceSurveyRound2_Round-2-A-Survey-of-Causal-Inference-Applications-At-Netflix.md](read-papers/2023_NetflixTechBlog_CausalInferenceSurveyRound2_Round-2-A-Survey-of-Causal-Inference-Applications-At-Netflix.md)
- Relevance: The card contains no verified content because both retrieval paths failed.

### Modeling Churn in Recommender Systems with Aggregated Preferences

- Source: arXiv 2025
- Detailed analysis: [read-papers/2025_arXiv_RecAPC_Modeling-Churn-Recommender-Systems-Aggregated-Preferences.md](read-papers/2025_arXiv_RecAPC_Modeling-Churn-Recommender-Systems-Aggregated-Preferences.md)
- Relevance: *Rec-APC* optimizes in-session likes before churn; it does not model multi-day retention attribution.

### Policy Design for Two-sided Platforms with Participation Dynamics

- Source: ICML 2025
- Detailed analysis: [read-papers/2025_arXiv_TwoSidedPolicy_Policy-Design-Two-sided-Platforms-Participation-Dynamics.md](read-papers/2025_arXiv_TwoSidedPolicy_Policy-Design-Two-sided-Platforms-Participation-Dynamics.md)
- Relevance: The paper studies subgroup population dynamics and welfare, not individual interaction credit.

### MODE: Mutual Optimality in Direct Effects of Reciprocal Recommendations

- Source: RecSys 2026
- Detailed analysis: [read-papers/2026_arXiv_MODE_Mutual-Optimality-Direct-Effects-Reciprocal-Recommendations.md](read-papers/2026_arXiv_MODE_Mutual-Optimality-Direct-Effects-Reciprocal-Recommendations.md)
- Relevance: *MODE* addresses match congestion and list optimality, not retention.

### Balancing Fairness and High Match Rates in Reciprocal Recommender Systems

- Source: arXiv 2026
- Detailed analysis: [read-papers/2026_arXiv_NashSocialWelfare_Balancing-Fairness-High-Match-Rates-Reciprocal-Recommender-Systems.md](read-papers/2026_arXiv_NashSocialWelfare_Balancing-Fairness-High-Match-Rates-Reciprocal-Recommender-Systems.md)
- Relevance: The paper optimizes exposure fairness and matches, with no retention outcome.

### Neural ODE for Multi-Channel Attribution

- Source: OpenReview, metadata unavailable
- Detailed analysis: [read-papers/OpenReview_NeuralODE_Neural-ODE-for-Multi-Channel-Attribution.md](read-papers/OpenReview_NeuralODE_Neural-ODE-for-Multi-Channel-Attribution.md)
- Relevance: The ingested source was only a browser-verification page; no method or evidence was available.
