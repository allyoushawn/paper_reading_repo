# Literature Review — Two-Sided Market Balancing for a Dating Recommender

**Run:** `claude_opus` · 2026-08-18 · synthesised by Codex over the complete extraction corpus.

## Coverage

- **86 extraction files**, each source read and extracted individually.
- **82 distinct works** — four files duplicate another (a blog summarising its own paper, a
  preprint alongside its published form). See ARTIFACT 0. Per the survey brief, both members of
  such a pair are cited, but they are never counted as independent evidence.
- Fit distribution across the 86 files: 40 high, 29 medium, 12 low.

> **Method note.** Extraction ran in two passes. The first used NotebookLM until that account hit
> an account-level block on programmatic access (`nlm doctor` passes every check, so it is a
> restriction, not an auth failure). The remainder — and the majority of the corpus — was extracted
> by **reading the source PDFs directly**, which proved more reliable: agents read real results
> sections and caught eight citation errors that metadata alone would have propagated. Corrections
> are listed in `log.md`; residual gaps in `RESUME-HERE.md`.

---

## PROOF OF READING

- `q1.md` (~line 7): “Highly-messaged users reply less often, since their inboxes are flooded.”
- `q2.md` (~line 7): “The LP objective Σf(s,r)g(r,s)x_sr subject to receiver capacity C_R(r) and sender capacity C_S(s) is a direct, real-data-validated instance of Layer 1 (reciprocal scoring) combined with Layer 2 (capacity-aware exposure allocation) — one of the closest matches to the project's own framing found in this corpus.”
- `q3.md` (~line 7): “LiJAR is the strongest direct methodological match found so far for the project's "capacity-aware exposure allocation" layer.”
- `q4.md` (~line 7): “This is very likely the single most directly relevant source found in this batch, and among the most relevant in the survey to date.”
- `q5.md` (~line 7): “One of the **highest-relevance sources in the survey**.”
- `q6.md` (~line 7): “Directly addresses **Layer 3 (market-design levers)**: this is a formal welfare analysis of a "like/application limit" as a platform intervention, providing a theoretical mechanism and proof that capping outbound applications protects the capacity-constrained side (employers, analogous to highly-desirable dating-app recipients) from being overwhelmed, at limited or no cost to the sending side.”
- `q7.md` (~line 7): “This source is one of the most directly on-target items in the survey.”
- `q8.md` (~line 7): “This is one of the strongest direct theoretical matches found in the survey for the project's Layer 2 (capacity-aware exposure allocation).”
- `q9.md` (~line 7): “High relevance to **layer 2 (capacity-aware exposure allocation)** — this is the closest mechanism in this batch to "cap likes/exposure to desirable users, guarantee a floor for under-shown users," expressed as a clean, model-agnostic quota re-ranking optimization with a demonstrated large effect size on a real dataset.”
- `q10.md` (~line 7): “The TU matching mechanism functions as a genuine capacity-aware exposure redistribution scheme, though it models capacity only implicitly.”
- `q11.md` (~line 7): “Strong fit for **Layer 2 (capacity-aware exposure allocation)**: the UAC module is essentially a deployed per-user capacity constraint and exposure-fairness re-ranking mechanism (cap matches per user at Q, remove saturated users from the eligible pool, predict who will actually be available to consume more) — directly transferable to gating who receives more likes/impressions based on remaining reply bandwidth.”
- `q12.md` (~line 7): “One of the most directly transferable papers in this batch.”
- `q13.md` (~line 7): “Directly relevant to layer 3 (market-design levers) and, more loosely, layer 2 (capacity-aware exposure allocation).”
- `q14.md` (~line 7): “Directly addresses **Layer 2 (capacity-aware exposure allocation)**: MRet is essentially a redistribution mechanism — reranking by joint retention gain instead of raw match probability, functionally similar in spirit to LiJAR-style redistribution but keyed on a learned retention curve rather than exposure counts.”
- `q15.md` (~line 7): “Direct structural analogue of capacity-aware exposure allocation: per-listing scores from posted/unfilled capacity, capped and converted to eligibility thresholds that throttle over-subscribed listings and redistribute exposure to under-served ones — parallelizable, unlike LiJAR-style sequential RSD.”

Read: **86 sources across the 15 files**.
## ARTIFACT 0 — Distinct-works reconciliation

Duplicate/related groups:

1. `2018_CIKM_NA_Towards-Fair-Marketplace-Counterfactual-Evaluation.md` + `2018_Spotify-Research-Blog_NA_Towards-Fair-Marketplace-Trade-off.md` — same Spotify fairness work.
2. `2023_QuotaFair_Fairness-Job-Recommendation-Quantity-Constraints.md` + `Unknown_PIKE-Group_NA_Fairness-Job-Recommendation-Quantity-Constraints.md` — same quantity-constraints work.
3. `2026_arXiv_ECDA_Integrating-Predictive-Models-Into-Two-Sided-Recommendations-Matching-Theoretic-Approach.md` + `Unknown_arXiv_NA_Integrating-Predictive-Models-Two-Sided-Recommendations.md` — same ECDA work.
4. `2022_CyberAgent-Blog_ChooSiow_Matching-Theory-Reciprocal-Recommender.md` + `2022_arXiv_MTRS_Matching-Theory-Based-RecSys-Online-Dating.md` — blog summary and underlying MTRS work.

Result: 86 files − 4 redundant files = **82 distinct works**.

## ARTIFACT 1 — Reverse citation map

Cited at least twice within the corpus:

- **Gale & Shapley (1962)** — `2010_AER_HitschHortacsuAriely_Matching-And-Sorting-In-Online-Dating.md`; `2013_UMUAI_RECON_Recommending-People-To-People.md`; `2014_SocialRecSys_TwoSidedLDA_Online-Dating-Recommendations-Matching-Markets-And-Learning-Preferences.md`; `2018_RecSys_RWS_Optimally-Balancing-Receiver-And-Recommended-Users-Importance-Reciprocal-Recommender-Systems.md`; `2018_SciAdv_AspirationalPursuit_Aspirational-Pursuit-Of-Mates-In-Online-Dating-Markets.md`; `2018_WorkingPaper_NA_Search-Selectivity-Market-Thickness.md`; `2021_NeurIPS_Welf_Two-sided-Fairness-Rankings-Lorenz-Dominance.md`; `2021_MSOM_NA_Managing-Congestion-Matching-Markets.md`; `2022_AAAI_MatchingConstraints_Matching-Market-Design-With-Constraints.md`; `2022_CSUR_NA_Challenge-based-Survey-E-recruitment-Recommendation-Systems.md`; `2022_CyberAgent-Blog_ChooSiow_Matching-Theory-Reciprocal-Recommender.md`; `2022_arXiv_MTRS_Matching-Theory-Based-RecSys-Online-Dating.md`; `2023_NeurIPS_AdversarialInteraction_Strategic-Behavior-In-Two-Sided-Matching-Markets-With-Recommendation-Enhanced-Preference-Formation.md`; `2025_WorkingPaper_NA_Congestion-and-Information-Design-in-Matching-Markets.md`; `2026_arXiv_NSW_Balancing-Fairness-And-High-Match-Rates-In-Reciprocal-Recommender-Systems.md`; `2026_arXiv_TwoSidedRegret_Two-Sided-Time-Independent-Regret-For-Matching-Markets-With-Limited-Interviews.md`. **Foundational.**

- **Pizzato et al., RECON (2010)** — `2013_UMUAI_RECON_Recommending-People-To-People.md`; `2015_ASONAM_ReciprocalRec_Reciprocal-Recommendation-System-For-Online-Dating.md`; `2018_RecSys_RWS_Optimally-Balancing-Receiver-And-Recommended-Users-Importance-Reciprocal-Recommender-Systems.md`; `2021_InfoFusion_RRSSurvey_Reciprocal-Recommender-Systems-Analysis-State-of-Art-Literature.md`; `2022_arXiv_MTRS_Matching-Theory-Based-RecSys-Online-Dating.md`; `2024_RecSys_NSW_Fair-Reciprocal-Recommendation-Matching-Markets.md`. **Foundational for reciprocal scoring.**

- **Choo & Siow (2006)** — `2019_WorkingPaper_CongestionMatchmakers_Prediction-Congestion-Two-Sided-Markets-Economist-vs-Machine-Matchmakers.md`; `2022_CyberAgent-Blog_ChooSiow_Matching-Theory-Reciprocal-Recommender.md`; `2022_arXiv_MTRS_Matching-Theory-Based-RecSys-Online-Dating.md`; `2023_RecSys_TU_Fast-Examination-agnostic-Reciprocal-Recommendation-in-Matching-Markets.md`; `2024_RecSysHR_ParallelIPFP_Parallel-And-Mini-Batch-Stable-Matching-For-Large-Scale-Reciprocal-Recommender-Systems.md`; `2026_arXiv_ECDA_Integrating-Predictive-Models-Into-Two-Sided-Recommendations-Matching-Theoretic-Approach.md`; `2026_arXiv_NSW_Balancing-Fairness-And-High-Match-Rates-In-Reciprocal-Recommender-Systems.md`; `2026_RecSys_MODE_Mutual-Optimality-Direct-Effects-Reciprocal-Recommendations-Matching-Markets.md`. **Foundational for TU matching.**

- **Singh & Joachims (2018), Fairness of Exposure** — `2018_FAT_NA_Balanced-Neighborhoods-Multi-sided-Fairness-Recommendation.md`; `2018_Spotify-Research-Blog_NA_Towards-Fair-Marketplace-Trade-off.md`; `2021_ICTIR_TSFD_User-Fairness-Item-Fairness-And-Diversity-For-Rankings-In-Two-Sided-Markets.md`; `2021_NeurIPS_Welf_Two-sided-Fairness-Rankings-Lorenz-Dominance.md`; `2022_SIGIR_JME-Fairness_Joint-Multisided-Exposure-Fairness-Recommendation.md`; `2025_ICML_PopEffects_Policy-Design-Two-sided-Platforms-Participation-Dynamics.md`; `2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md`; `2026_arXiv_NSW_Balancing-Fairness-And-High-Match-Rates-In-Reciprocal-Recommender-Systems.md`. **Foundational for exposure fairness.**

- **LiJAR (2017)** — `2020_KDD_Job2Skills_Salience-and-Market-aware-Skill-Extraction-for-Job-Targeting.md`; `2022_CSUR_NA_Challenge-based-Survey-E-recruitment-Recommendation-Systems.md`; `2022_CyberAgent-Blog_ChooSiow_Matching-Theory-Reciprocal-Recommender.md`; `2024_RecSysHR_ParallelIPFP_Parallel-And-Mini-Batch-Stable-Matching-For-Large-Scale-Reciprocal-Recommender-Systems.md`; `2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md`; `2026_arXiv_TEC_Designing-Recommendation-Exposure-Favorite-Lists.md`.

- **Roth & Sotomayor / matching-market theory** — `2010_AER_HitschHortacsuAriely_Matching-And-Sorting-In-Online-Dating.md`; `2014_SocialRecSys_TwoSidedLDA_Online-Dating-Recommendations-Matching-Markets-And-Learning-Preferences.md`; `2018_WorkingPaper_NA_Search-Selectivity-Market-Thickness.md`; `2021_NeurIPS_Welf_Two-sided-Fairness-Rankings-Lorenz-Dominance.md`; `2023_NeurIPS_AdversarialInteraction_Strategic-Behavior-In-Two-Sided-Matching-Markets-With-Recommendation-Enhanced-Preference-Formation.md`.

## ARTIFACT 2 — Taxonomy

### 1. Reciprocal scoring and bilateral preference

Scope: Estimate whether both parties will like, reply to, accept, or mutually benefit from a recommendation.

`2013_UMUAI_RECON_Recommending-People-To-People.md`; `2014_SocialRecSys_TwoSidedLDA_Online-Dating-Recommendations-Matching-Markets-And-Learning-Preferences.md`; `2015_ASONAM_ReciprocalRec_Reciprocal-Recommendation-System-For-Online-Dating.md`; `2017_MLconf_TinVec_Personalized-Recommendations-At-Tinder.md`; `2018_RecSys_RWS_Optimally-Balancing-Receiver-And-Recommended-Users-Importance-Reciprocal-Recommender-Systems.md`; `2021_InfoFusion_RRSSurvey_Reciprocal-Recommender-Systems-Analysis-State-of-Art-Literature.md`; `2022_RecSys_DPGNN_Modeling-Two-Way-Selection-Preference-Person-Job-Fit.md`; `2022_arXiv_MTRS_Matching-Theory-Based-RecSys-Online-Dating.md`; `2023_KDD_BOSS_Bilateral-Occupational-Suitability-Aware-Recommender.md`; `2023_RecSys_ReSeq_Reciprocal-Sequential-Recommendation.md`; `2024_arXiv_BoB_Best-of-Both-Match-Predictions-Reciprocal-Recommendations-Job-Search.md`; `2024_KDD_CRRS_Revisiting-Reciprocal-Recommender-Systems.md`; `2025_RecSys_OPEMatching_Off-Policy-Evaluation-And-Learning-For-Matching-Markets.md`; `2025_TSMO-KDD-Workshop_CFRR_Counterfactual-Reciprocal-Recommender-Systems-User-to-User-Matching.md`; `2026_RecSys_MODE_Mutual-Optimality-Direct-Effects-Reciprocal-Recommendations-Matching-Markets.md`; `2026_arXiv_TwoSidedRegret_Two-Sided-Time-Independent-Regret-For-Matching-Markets-With-Limited-Interviews.md`; `Unknown_MDPI_NA_Explainable-Reciprocal-Recommender-Affiliate-Seller-Matching.md`.

### 2. Capacity-aware exposure allocation and congestion pricing

Scope: Cap, forecast, price, or redistribute receiver exposure according to demand, backlog, capacity, or congestion.

`2014_SocialRecSys_TwoSidedLDA_Online-Dating-Recommendations-Matching-Markets-And-Learning-Preferences.md`; `2017_CIKM_CapMF_Recommendation-with-Capacity-Constraints.md`; `2017_KDD_LiJAR_Job-Application-Redistribution-Career-Marketplace.md`; `2018_FAT_NA_Balanced-Neighborhoods-Multi-sided-Fairness-Recommendation.md`; `2018_CIKM_NA_Towards-Fair-Marketplace-Counterfactual-Evaluation.md`; `2018_KDD_ListingEmbeddings_Real-time-Personalization-Embeddings-Search-Ranking-Airbnb.md`; `2019_WorkingPaper_CongestionMatchmakers_Prediction-Congestion-Two-Sided-Markets-Economist-vs-Machine-Matchmakers.md`; `2021_NeurIPS_Welf_Two-sided-Fairness-Rankings-Lorenz-Dominance.md`; `2021_ICTIR_TSFD_User-Fairness-Item-Fairness-And-Diversity-For-Rankings-In-Two-Sided-Markets.md`; `2022_SIGIR_JME-Fairness_Joint-Multisided-Exposure-Fairness-Recommendation.md`; `2022_OperationsResearch_NA_Assortment-Planning-Two-Sided-Sequential-Matching.md`; `2022_CyberAgent-Blog_ChooSiow_Matching-Theory-Reciprocal-Recommender.md`; `2023_QuotaFair_Fairness-Job-Recommendation-Quantity-Constraints.md`; `2023_RecSys_TU_Fast-Examination-agnostic-Reciprocal-Recommendation-in-Matching-Markets.md`; `2024_RecSysHR_ParallelIPFP_Parallel-And-Mini-Batch-Stable-Matching-For-Large-Scale-Reciprocal-Recommender-Systems.md`; `2024_LinkedIn-Eng-Blog_PYMK_People-You-May-Know-Recommendation-System.md`; `2025_WWW_DualRec_Creator-Side-Recommender-System-Challenges-Designs-Applications.md`; `2025_ICML_PopEffects_Policy-Design-Two-sided-Platforms-Participation-Dynamics.md`; `2026_RecSys_MODE_Mutual-Optimality-Direct-Effects-Reciprocal-Recommendations-Matching-Markets.md`; `2026_arXiv_NSW_Balancing-Fairness-And-High-Match-Rates-In-Reciprocal-Recommender-Systems.md`; `2026_arXiv_TEC_Designing-Recommendation-Exposure-Favorite-Lists.md`; `2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md`; `Unknown_PIKE-Group_NA_Fairness-Job-Recommendation-Quantity-Constraints.md`.

### 3. Matching, assortment, quotas, and stable allocation

Scope: Allocate finite slots or menus with matching-theoretic, quota, assortment, or deferred-acceptance constraints.

`2010_AER_HitschHortacsuAriely_Matching-And-Sorting-In-Online-Dating.md`; `2013_Strata-QCon_NA_Data-Science-of-Love.md`; `2018_TechCrunch_GaleShapley_Hinge-Most-Compatible-Match-Algorithm.md`; `2022_AAAI_MatchingConstraints_Matching-Market-Design-With-Constraints.md`; `2025_MSOM_DatingHeuristic_Platform-Design-Curated-Dating-Markets.md`; `2026_arXiv_ECDA_Integrating-Predictive-Models-Into-Two-Sided-Recommendations-Matching-Theoretic-Approach.md`; `Unknown_arXiv_NA_Integrating-Predictive-Models-Two-Sided-Recommendations.md`.

### 4. Market-design levers: limits, signaling, information, and directionality

Scope: Change who may initiate, how many proposals are sent, what information is revealed, or how scarce signals are used.

`2015_ExpEcon_NA_Propose-With-A-Rose-Signaling-Dating.md`; `2018_MgmtSci_NA_Competing-By-Restricting-Choice.md`; `2018_WorkingPaper_NA_Search-Selectivity-Market-Thickness.md`; `2021_MSOM_NA_Managing-Congestion-Matching-Markets.md`; `2021_ManagementScience_NA_Facilitating-Search-Partners-Matching-Platforms.md`; `2022_CyberAgent-Blog_ReciprocalCF_Analyzing-Encounters-Matching-App.md`; `2025_WorkingPaper_NA_Congestion-and-Information-Design-in-Matching-Markets.md`; `2026_2024_ISR_NA_Mr-Right-or-Mr-Best-Preference-Mismatch.md`; `2026_arXiv_TwoSidedRegret_Two-Sided-Time-Independent-Regret-For-Matching-Markets-With-Limited-Interviews.md`.

### 5. Ecosystem metrics, retention, and feedback dynamics

Scope: Measure spread, coverage, welfare, retention, liquidity, churn, and long-run population effects.

`2009_Blog_NA_Your-Looks-And-Your-Inbox.md`; `2018_SciAdv_AspirationalPursuit_Aspirational-Pursuit-Of-Mates-In-Online-Dating-Markets.md`; `2021_NeurIPS_Welf_Two-sided-Fairness-Rankings-Lorenz-Dominance.md`; `2022_CyberAgent-Blog_ReciprocalCF_Analyzing-Encounters-Matching-App.md`; `2025_ICML_PopEffects_Policy-Design-Two-sided-Platforms-Participation-Dynamics.md`; `2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md`; `2026_KISSmetrics-Blog_NA_Marketplace-Analytics-Supply-Demand-Liquidity.md`; `2026_arXiv_NSW_Balancing-Fairness-And-High-Match-Rates-In-Reciprocal-Recommender-Systems.md`; `2026_RecSys_MODE_Mutual-Optimality-Direct-Effects-Reciprocal-Recommendations-Matching-Markets.md`.

### 6. Experimentation, causal evaluation, and interference

Scope: Evaluate marketplace interventions when treatment changes shared demand, supply, or reply capacity.

`2018_CIKM_NA_Towards-Fair-Marketplace-Counterfactual-Evaluation.md`; `2022_KDD_NA_Decision-Intelligence-Analytics-Online-Marketplaces.md`; `2022_ManagementScience_TSR_Experimental-Design-Two-Sided-Platforms-Bias.md`; `2025_ManagementScience_ClusterRandomization_Reducing-Interference-Bias-Airbnb-Pricing.md`; `2025_arXiv_SMRD_Multiple-Randomization-Designs-Estimation-Inference-Interference.md`; `2026_Blog_NA_Beyond-AB-Testing-Surrogacy-Region-Splits-Marketplaces.md`; `2026_arXiv_ECDA_Integrating-Predictive-Models-Into-Two-Sided-Recommendations-Matching-Theoretic-Approach.md`; `2025_TSMO-KDD-Workshop_CFRR_Counterfactual-Reciprocal-Recommender-Systems-User-to-User-Matching.md`.

### 7. Background / References: unilateral ranking, infrastructure, surveys, and low-relevance items

Scope: Useful context or engineering patterns, but no complete reciprocal capacity-balancing mechanism.

`2014_KDD_ImpressionDiscounting_Modeling-Impression-Discounting-Recommender-Systems.md`; `2016_Blog_SmartPhotos_Introducing-Smart-Photos.md`; `2017_Podcast_InstantMatch_Thumbtack-Marketplace-Evolution.md`; `2018_KDD_NA_Fairness-Exposure-Rankings.md`; `2018_Spotify-Research-Blog_NA_Towards-Fair-Marketplace-Trade-off.md`; `2019_AWS-Blog_NA_Powering-Recommendation-Models-ElastiCache-Redis.md`; `2019_Blog_NA_Powering-Tinder-Method-Behind-Matching.md`; `2019_RecSys_NA_Recommendations-in-a-Marketplace.md`; `2020_KDD_Job2Skills_Salience-and-Market-aware-Skill-Extraction-for-Job-Targeting.md`; `2022_CSUR_NA_Challenge-based-Survey-E-recruitment-Recommendation-Systems.md`; `2022_KDD_NA_Decision-Intelligence-Analytics-Online-Marketplaces.md`; `2023_Blog_NA_3-Powerful-Features-Ziprecruiter-Search.md`; `2023_Blog_NA_Automated-Decision-Making-At-Grindr.md`; `2025_Blog_AIPhotoSelector_How-On-Device-AI-Finds-Best-Tinder-Photos.md`; `2025_KDD_NA_Two-Sided-Marketplace-Optimization-Workshop.md`; `2025_Thumbtack-Eng-Blog_NA_Engineering-Right-Opportunities-Thumbtack-Pros.md`; `2025_Tinder-Tech-Blog_TwoTower_Tinders-Migration-Elasticsearch-8.md`; `2026_Blog_JourneyFormer_Personalizing-Airbnb-Search-Guest-Journey.md`; `2026_Thumbtack-Eng-Blog_AdaptiveMixedSampling_Transformer-Based-Category-Recommender-Thumbtack.md`; `2026_arXiv_NA_Understanding-Guest-Preferences-Two-Sided-Marketplaces.md`; `Unknown_MDPI_NA_Explainable-Reciprocal-Recommender-Affiliate-Seller-Matching.md`; `Unknown_NA_NA_Designing-Labor-Market-Recommender-Systems.md`.

## ARTIFACT 3 — Design-pattern matrix

| Pattern | Sources and concrete mechanism |
|---|---|
| Reciprocal scoring | `2014_SocialRecSys_TwoSidedLDA_Online-Dating-Recommendations-Matching-Markets-And-Learning-Preferences.md` — LP uses `f(s,r)g(r,s)`; `2018_RecSys_RWS_Optimally-Balancing-Receiver-And-Recommended-Users-Importance-Reciprocal-Recommender-Systems.md` — AdaBoost reply-probability `PR(y,x)`; `2026_arXiv_ECDA_Integrating-Predictive-Models-Into-Two-Sided-Recommendations-Matching-Theoretic-Approach.md` — `δij = λi αij λj βij`; `2024_arXiv_BoB_Best-of-Both-Match-Predictions-Reciprocal-Recommendations-Job-Search.md` — personalized blend of directional predictions and true matches. |
| Capacity-aware scoring | `2017_KDD_LiJAR_Job-Application-Redistribution-Career-Marketplace.md` — forecast-volume confidence bands with multiplicative boost/penalty; `2022_CyberAgent-Blog_ChooSiow_Matching-Theory-Reciprocal-Recommender.md` — TU transfer prices suppress congested users; `2025_WWW_DualRec_Creator-Side-Recommender-System-Challenges-Designs-Applications.md` — eligibility cap `|D_u| < Q`; `2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md` — rank by joint retention gain. |
| Constrained re-ranking | `2017_CIKM_CapMF_Recommendation-with-Capacity-Constraints.md` — differentiable expected-usage capacity loss; `2023_QuotaFair_Fairness-Job-Recommendation-Quantity-Constraints.md` — model-agnostic upper/lower quantity quotas; `2022_SIGIR_JME-Fairness_Joint-Multisided-Exposure-Fairness-Recommendation.md` — target exposure matrix plus Gumbel-Softmax optimization; `2026_arXiv_TEC_Designing-Recommendation-Exposure-Favorite-Lists.md` — capped eligibility thresholds. |
| Market-design lever | `2015_ExpEcon_NA_Propose-With-A-Rose-Signaling-Dating.md` — limited roses raise acceptance by 3.3 percentage points; `2018_TechCrunch_GaleShapley_Hinge-Most-Compatible-Match-Algorithm.md` — exactly one curated reciprocal match/day; `2021_ManagementScience_NA_Facilitating-Search-Partners-Matching-Platforms.md` — directional search and hidden desirability; `2025_WorkingPaper_NA_Congestion-and-Information-Design-in-Matching-Markets.md` — caps and personalized best-fit disclosure reduce over-search. |
| Ecosystem metrics | `2018_SciAdv_AspirationalPursuit_Aspirational-Pursuit-Of-Mates-In-Online-Dating-Markets.md` — 1,504 messages/month to the most popular user and upward-message reply rates below 21%; `2023_RecSys_TU_Fast-Examination-agnostic-Reciprocal-Recommendation-in-Matching-Markets.md` — match Gini 0.387→0.102; `2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md` — retention at ~70% of Max Match volume; `2026_arXiv_NSW_Balancing-Fairness-And-High-Match-Rates-In-Reciprocal-Recommender-Systems.md` — envy and utility Gini. |
| Evaluation method | `2018_CIKM_NA_Towards-Fair-Marketplace-Counterfactual-Evaluation.md` — IPS counterfactual evaluation; `2022_ManagementScience_TSR_Experimental-Design-Two-Sided-Platforms-Bias.md` — TSR/TSRI; `2025_ManagementScience_ClusterRandomization_Reducing-Interference-Bias-Airbnb-Pricing.md` — cluster randomization, correcting 19.76% bias; `2025_arXiv_SMRD_Multiple-Randomization-Designs-Estimation-Inference-Interference.md` — independently randomize both sides; `2026_Blog_NA_Beyond-AB-Testing-Surrogacy-Region-Splits-Marketplaces.md` — region splits plus AIPW/surrogacy. |

Disanalogy flags: Spotify/music, Airbnb, jobs, movies, POIs, categories, listings, and creator-content sources generally have unlimited or renewable supply-side capacity; their exposure-fairness mechanisms transfer only after replacing “item availability” with human reply bandwidth. Dating-native sources—`2014_SocialRecSys_TwoSidedLDA_Online-Dating-Recommendations-Matching-Markets-And-Learning-Preferences.md`, `2018_RecSys_RWS_Optimally-Balancing-Receiver-And-Recommended-Users-Importance-Reciprocal-Recommender-Systems.md`, `2023_RecSys_TU_Fast-Examination-agnostic-Reciprocal-Recommendation-in-Matching-Markets.md`, `2025_MSOM_DatingHeuristic_Platform-Design-Curated-Dating-Markets.md`, `2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md`, and `2026_arXiv_ECDA_Integrating-Predictive-Models-Into-Two-Sided-Recommendations-Matching-Theoretic-Approach.md`—are more directly analogous.

## ARTIFACT 4 — Read-first top 12

1. `2026_arXiv_ECDA_Integrating-Predictive-Models-Into-Two-Sided-Recommendations-Matching-Theoretic-Approach.md` — field-tested expected-like/date caps; effective dates 0.0623 vs. 0.0584 for the current recommender.
2. `2023_RecSys_TU_Fast-Examination-agnostic-Reciprocal-Recommendation-in-Matching-Markets.md` — TU/IPFP reduced match Gini from 0.387 to 0.102.
3. `2026_RecSys_MODE_Mutual-Optimality-Direct-Effects-Reciprocal-Recommendations-Matching-Markets.md` — at 1,000×1,000 users, MODE beat TU expected matches by more than 10%.
4. `2018_RecSys_RWS_Optimally-Balancing-Receiver-And-Recommended-Users-Importance-Reciprocal-Recommender-Systems.md` — live dating experiment raised successful interactions from 1 to 8 and reduced recommended-user popularity from 59.49 to 32.72.
5. `2014_SocialRecSys_TwoSidedLDA_Online-Dating-Recommendations-Matching-Markets-And-Learning-Preferences.md` — explicit sender/receiver capacity LP; reciprocal recommendation improved success rate by 46.84% for male suitors.
6. `2017_KDD_LiJAR_Job-Application-Redistribution-Career-Marketplace.md` — production A/B shifted applications +6.5% to underserved jobs, −8.7% to overserved jobs, with entropy +12%.
7. `2025_WWW_DualRec_Creator-Side-Recommender-System-Challenges-Designs-Applications.md` — deployed capacity gate raised new-item coverage from 13.6% to 82.3%.
8. `2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md` — higher retention with only about 70% of Max Match’s volume; directly optimizes the project’s north star.
9. `2024_RecSys_NSW_Fair-Reciprocal-Recommendation-Matching-Markets.md` — cut envy 92–98% while retaining roughly 79–81% of social-welfare match volume.
10. `2015_ExpEcon_NA_Propose-With-A-Rose-Signaling-Dating.md` — limited roses increased acceptance by 3.3 percentage points, or 20% relatively.
11. `2025_arXiv_SMRD_Multiple-Randomization-Designs-Estimation-Inference-Interference.md` — two-sided randomization recovered the correct treatment sign when standard single-sided testing failed.
12. `2025_MSOM_DatingHeuristic_Platform-Design-Curated-Dating-Markets.md` — real dating backlog/swipe data; one-directional design captured at least 50% of two-directional matches, with a `1−1/e ≈ 63.2%` approximation guarantee.
