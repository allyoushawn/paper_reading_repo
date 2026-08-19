# Method Tracker — codex-sol

- model_identifier: codex-sol
- finalized: 2026-08-18
- cards scanned: 120
- named methods tracked: 99
- explicit relations mapped to tracked named methods: 38 (40 total paper-to-paper relations)

## Scoring rules

The required composite is `(baseline mention count × 3) + (derived variant count × 2) + (simplicity score × 1) + (performance consistency score × 2)`.

Only explicit card evidence is counted. “Baseline mention count” requires baseline/comparison wording in another card; “derived variant count” requires explicit extension/based-on/variant wording. Component counts and comparable independent performance series were generally not available in the cards, so they are marked `N/A` and contribute 0 rather than receiving invented 1–5 scores. Ties are sorted by method name after descending baseline count and composite score.

## Methodology Table

| Method Name | Direction | Proposal / Representative Paper (Year) | Industry Adopter | Baseline Mention Count | Derived Variant Count | Independent Measured Performance | Component Count | Simplicity Score | Performance Consistency Score | Fundamentality Composite Score |
|---|---|---|---|---:|---:|---|---|---|---|---:|
| DFM | D7 — delayed feedback / censored labels | [2014_KDD_DFM_Modeling-Delayed-Feedback.md](./read-papers/2014_KDD_DFM_Modeling-Delayed-Feedback.md) (2014) | Not specified in cards | 8 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 24 |
| ESMM | D5 — multi-stage / multi-task conversion chains | [2018_SIGIR_ESMM_Entire-Space-Multi-Task.md](./read-papers/2018_SIGIR_ESMM_Entire-Space-Multi-Task.md) (2018) | Not specified in cards | 7 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 21 |
| ZILN | D4 — retention / lifetime value / long-horizon value | [2019_arXiv_ZILN_Probabilistic-Customer-Lifetime-Value.md](./read-papers/2019_arXiv_ZILN_Probabilistic-Customer-Lifetime-Value.md) (2019) | Not specified in cards | 4 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 12 |
| BatchRL-MTF | D2 | [2022_KDD_BatchRL-MTF_Multi-Task-Fusion-Long-Term-Satisfaction.md](./read-papers/2022_KDD_BatchRL-MTF_Multi-Task-Fusion-Long-Term-Satisfaction.md) (2022) | Not specified in cards | 2 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 6 |
| ESM2 | D5 — multi-stage / multi-task conversion chains | [2020_SIGIR_ESM2_Post-Click-Behavior-Decomposition.md](./read-papers/2020_SIGIR_ESM2_Post-Click-Behavior-Decomposition.md) (2020) | Not specified in cards | 2 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 6 |
| FID | D2 | [2024_KDD_FID_Future-Impact-Decomposition-Request-Level.md](./read-papers/2024_KDD_FID_Future-Impact-Decomposition-Request-Level.md) (2024) | Kuaishou Technology | 1 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 3 |
| GRM | D1 | [2025_SIGIR_GRM_Generative-List-Level-Multi-Objective-Reranking.md](./read-papers/2025_SIGIR_GRM_Generative-List-Level-Multi-Objective-Reranking.md) (2025) | Taobao | 1 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 3 |
| KuaiSim | D2 | [2023_arXiv_KuaiSim_Comprehensive-Recommender-System-Simulator.md](./read-papers/2023_arXiv_KuaiSim_Comprehensive-Recommender-System-Simulator.md) (2023) | City University of Hong Kong and Kuaishou Technology | 1 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 3 |
| LOPE | D3 | [2024_SpotifyResearch_LOPE_Estimating-Long-Term-Outcome-Algorithms.md](./read-papers/2024_SpotifyResearch_LOPE_Estimating-Long-Term-Outcome-Algorithms.md) (2024) | Not specified in cards | 1 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 3 |
| NSW | D8 | [2026_arXiv_NSW_Fair-High-Match-Reciprocal-Recommendation.md](./read-papers/2026_arXiv_NSW_Fair-High-Match-Reciprocal-Recommendation.md) (2026) | Not specified in cards | 1 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 3 |
| OneRec | D9 | [2025_arXiv_OneRec_Unifying-Retrieve-Rank.md](./read-papers/2025_arXiv_OneRec_Unifying-Retrieve-Rank.md) (2025) | Not specified in cards | 1 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 3 |
| RLUR | D2 | [2023_WWW_RLUR_Reinforcing-User-Retention-Billion-Scale.md](./read-papers/2023_WWW_RLUR_Reinforcing-User-Retention-Billion-Scale.md) (2023) | Not specified in cards | 1 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 3 |
| SlateQ | D2 | [2019_IJCAI_SlateQ_Tractable-RL-Recommendation-Sets.md](./read-papers/2019_IJCAI_SlateQ_Tractable-RL-Recommendation-Sets.md) (2019) | Google | 1 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 3 |
| Stickiness | D2 | [2023_arXiv_Stickiness_Optimizing-Audio-Recommendations-Long-Term.md](./read-papers/2023_arXiv_Stickiness_Optimizing-Audio-Recommendations-Long-Term.md) (2023) | Not specified in cards | 1 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 3 |
| ValueRL | D2 | [2019_WWW_ValueRL_Value-Aware-Recommendation-Profit-Maximization.md](./read-papers/2019_WWW_ValueRL_Value-Aware-Recommendation-Profit-Maximization.md) (2019) | Not specified in cards | 0 | 1 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 2 |
| AITM | D5 — multi-stage / multi-task conversion chains | [2021_KDD_AITM_Sequential-Multi-Step-Conversions.md](./read-papers/2021_KDD_AITM_Sequential-Multi-Step-Conversions.md) (2021) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| AURO | D2 | [2025_arXiv_AURO_Adaptive-User-Retention-Optimization.md](./read-papers/2025_arXiv_AURO_Adaptive-User-Retention-Optimization.md) (2025) | Nanyang Technological University and Kuaishou Technology | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| AUUCmax | D6 — causal uplift / incrementality | [2020_arXiv_AUUCmax_Treatment-Targeting-AUUC.md](./read-papers/2020_arXiv_AUUCmax_Treatment-Targeting-AUUC.md) (2020) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| BudgetSplit | D6 — causal uplift / incrementality | [2020_arXiv_BudgetSplit_Trustworthy-Marketplace-Experimentation.md](./read-papers/2020_arXiv_BudgetSplit_Trustworthy-Marketplace-Experimentation.md) (2020) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| CBDF | Not specified | [2021_SIGIR_CBDF_Counterfactual-Delayed-Streaming.md](./read-papers/2021_SIGIR_CBDF_Counterfactual-Delayed-Streaming.md) (2021) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| CC-OR-Net | D4 | [2026_WWW_CC-OR-Net_Unified-LTV-Structural-Decoupling.md](./read-papers/2026_WWW_CC-OR-Net_Unified-LTV-Structural-Decoupling.md) (2026) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| CDAF | D4 | [2023_AAAI_CDAF_Cross-Domain-Adaptative-LTV-Prediction.md](./read-papers/2023_AAAI_CDAF_Cross-Domain-Adaptative-LTV-Prediction.md) (2023) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| CFRR | D8 | [2025_TSMO_CFRR_Counterfactual-Reciprocal-Recommenders.md](./read-papers/2025_TSMO_CFRR_Counterfactual-Reciprocal-Recommenders.md) (2025) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| CM-DCM | D7 — delayed feedback / censored labels | [2026_SIGIR_CM-DCM_Counterfactual-Delayed-Conversion.md](./read-papers/2026_SIGIR_CM-DCM_Counterfactual-Delayed-Conversion.md) (2026) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| CRRS | Not specified | [2024_KDD_CRRS_Revisiting-Reciprocal-Metrics-Causal.md](./read-papers/2024_KDD_CRRS_Revisiting-Reciprocal-Metrics-Causal.md) (2024) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| CUPID | D8 | [2024_arXiv_CUPID_Real-Time-Session-Reciprocal-Recommendation.md](./read-papers/2024_arXiv_CUPID_Real-Time-Session-Reciprocal-Recommendation.md) (2024) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| DASI | D3 | [2021_arXiv_DASI_Dynamically-Adjusted-Surrogate-Index.md](./read-papers/2021_arXiv_DASI_Dynamically-Adjusted-Surrogate-Index.md) (2021) | Microsoft Research | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| DEFER | D7 — delayed feedback / censored labels | [2021_KDD_DEFER_Real-Negatives-Delayed-Feedback.md](./read-papers/2021_KDD_DEFER_Real-Negatives-Delayed-Feedback.md) (2021) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| DEFUSE | D7 — delayed feedback / censored labels | [2022_WWW_DEFUSE_Delayed-Feedback-Label-Correction.md](./read-papers/2022_WWW_DEFUSE_Delayed-Feedback-Label-Correction.md) (2022) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| DelayBuckets | D7 | [2021_arXiv_DelayBuckets_Handling-Many-Conversions-Per-Click.md](./read-papers/2021_arXiv_DelayBuckets_Handling-Many-Conversions-Per-Click.md) (2021) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| DiPS-DPR | D8 | [2025_RecSys_DiPS-DPR_Off-Policy-Matching-Markets.md](./read-papers/2025_RecSys_DiPS-DPR_Off-Policy-Matching-Markets.md) (2025) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| DRL | D2 | [2026_arXiv_DRL_Model-Agnostic-Downstream-Rewards-Learning.md](./read-papers/2026_arXiv_DRL_Model-Agnostic-Downstream-Rewards-Learning.md) (2026) | Pinterest | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| DRN | D2 | [2018_WWW_DRN_Deep-Reinforcement-Learning-News-Recommendation.md](./read-papers/2018_WWW_DRN_Deep-Reinforcement-Learning-News-Recommendation.md) (2018) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| E2E-Uplift | D6 | [2024_arXiv_E2E-Uplift_Cost-Effective-Incentive-Uplift-Recommendation.md](./read-papers/2024_arXiv_E2E-Uplift_Cost-Effective-Incentive-Uplift-Recommendation.md) (2024) | Renmin University of China and Tencent | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| ECDA | Not specified | [2026_arXiv_ECDA_Two-Sided-Dating-Recommendations.md](./read-papers/2026_arXiv_ECDA_Two-Sided-Dating-Recommendations.md) (2026) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| EDT4Rec | D2 | [2024_KDD_EDT4Rec_Max-Entropy-Reward-Relabeling.md](./read-papers/2024_KDD_EDT4Rec_Max-Entropy-Reward-Relabeling.md) (2024) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| ESCM2 | D5 | [2022_SIGIR_ESCM2_Entire-Space-Counterfactual-Multi-Task-Model.md](./read-papers/2022_SIGIR_ESCM2_Entire-Space-Counterfactual-Multi-Task-Model.md) (2022) | Ant Group | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| ESDF | D7 | [2021_AAAI_ESDF_Delayed-Feedback-Entire-Space-CVR.md](./read-papers/2021_AAAI_ESDF_Delayed-Feedback-Entire-Space-CVR.md) (2021) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| ESDFM | D7 — delayed feedback / censored labels | [2021_AAAI_ESDFM_Elapsed-Time-Sampling-Delayed-Feedback.md](./read-papers/2021_AAAI_ESDFM_Elapsed-Time-Sampling-Delayed-Feedback.md) (2021) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| Fair-Reciprocal-NSW | Not specified | [2024_RecSys_Fair-Reciprocal-NSW.md](./read-papers/2024_RecSys_Fair-Reciprocal-NSW.md) (2024) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| FNC | D7 — delayed feedback / censored labels | [2019_RecSys_FNC_Delayed-Feedback-Continuous-Training.md](./read-papers/2019_RecSys_FNC_Delayed-Feedback-Continuous-Training.md) (2019) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| GDFM | Not specified | [2022_NeurIPS_GDFM_Post-Click-Delayed-Feedback.md](./read-papers/2022_NeurIPS_GDFM_Post-Click-Delayed-Feedback.md) (2022) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| GenPage | D9 | [2026_RecSys_GenPage_End-to-End-Generative-Homepage.md](./read-papers/2026_RecSys_GenPage_End-to-End-Generative-Homepage.md) (2026) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| GenRec | D9 | [2026_arXiv_GenRec_LLM-Backed-Ranker-Netflix.md](./read-papers/2026_arXiv_GenRec_LLM-Backed-Ranker-Netflix.md) (2026) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| GFN4Retention | D2 | [2024_KDD_GFN4Retention_Modeling-User-Retention-Generative-Flow-Networks.md](./read-papers/2024_KDD_GFN4Retention_Modeling-User-Retention-Generative-Flow-Networks.md) (2024) | City University of Hong Kong and Kuaishou Technology | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| GRePO-LTV | D4 | [2025_KDD_GRePO-LTV_Mini-Game-Lifetime-Value-WeChat.md](./read-papers/2025_KDD_GRePO-LTV_Mini-Game-Lifetime-Value-WeChat.md) (2025) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| GSNO | D2 | [2025_arXiv_GSNO_Generative-Sequential-Notification-Optimization.md](./read-papers/2025_arXiv_GSNO_Generative-Sequential-Notification-Optimization.md) (2025) | LinkedIn | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| HM3 | D5 — multi-stage / multi-task conversion chains | [2021_SIGIR_HM3_Hierarchical-Micro-Macro-Behaviors.md](./read-papers/2021_SIGIR_HM3_Hierarchical-Micro-Macro-Behaviors.md) (2021) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| IDUM | D6 | [2025_ICML_IDUM_Invariant-Deep-Uplift-Incentive-Assignment.md](./read-papers/2025_ICML_IDUM_Invariant-Deep-Uplift-Incentive-Assignment.md) (2025) | Not specified in selected-source metadata | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| IF-DFM | Not specified | [2026_AAAI_IF-DFM_Delayed-Feedback-Influence-Functions.md](./read-papers/2026_AAAI_IF-DFM_Delayed-Feedback-Influence-Functions.md) (2026) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| ImpatientBandit | D2 | [2023_KDD_ImpatientBandit_Optimizing-Recommendations-Long-Term-Without-Delay.md](./read-papers/2023_KDD_ImpatientBandit_Optimizing-Recommendations-Long-Term-Without-Delay.md) (2023) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| Learning-to-Rank-Uplift-PCG | Not specified | [2020_TKDE_Learning-to-Rank-Uplift-PCG.md](./read-papers/2020_TKDE_Learning-to-Rank-Uplift-PCG.md) (2020) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| LiRank | D1 | [2024_KDD_LiRank_Industrial-Large-Scale-Ranking-LinkedIn.md](./read-papers/2024_KDD_LiRank_Industrial-Large-Scale-Ranking-LinkedIn.md) (2024) | LinkedIn | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| MBR | D8 | [2021_InfoQ-China_MBR_Model-Based-Recall-Momo-Social-Recommendation.md](./read-papers/2021_InfoQ-China_MBR_Model-Based-Recall-Momo-Social-Recommendation.md) (2021) | Momo / InfoQ China | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| MIAR | D1 | [2018_IJCAI_MIAR_Mutual-Influence-Aware-Ecommerce-Ranking.md](./read-papers/2018_IJCAI_MIAR_Mutual-Influence-Aware-Ecommerce-Ranking.md) (2018) | Not specified in selected-source metadata | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| MISS | Not specified | [2024_AAAI_MISS_Multi-Interval-Delayed-CVR.md](./read-papers/2024_AAAI_MISS_Multi-Interval-Delayed-CVR.md) (2024) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| MOLD | D1 | [2024_KDD_MOLD_Multi-Objective-Ranking-Model-Distillation.md](./read-papers/2024_KDD_MOLD_Multi-Objective-Ranking-Model-Distillation.md) (2024) | Not specified in selected-source metadata | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| MoSE | D1-D5 | [2020_KDD_MoSE_Multitask-Mixture-Sequential-Experts.md](./read-papers/2020_KDD_MoSE_Multitask-Mixture-Sequential-Experts.md) (2020) | Not specified in selected-source metadata | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| MTFM | D9 | [2026_arXiv_MTFM_Alignment-Free-Recommendation-Foundation-Model.md](./read-papers/2026_arXiv_MTFM_Alignment-Free-Recommendation-Foundation-Model.md) (2026) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| MTGR | D9 | [2025_arXiv_MTGR_Industrial-Scale-Generative-Recommendation-Meituan.md](./read-papers/2025_arXiv_MTGR_Industrial-Scale-Generative-Recommendation-Meituan.md) (2025) | Meituan | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| MTRS | Not specified | [2022_RecSys_MTRS_Online-Dating.md](./read-papers/2022_RecSys_MTRS_Online-Dating.md) (2022) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| MultiDR | D5 — multi-stage / multi-task conversion chains | [2020_WWW_MultiDR_Causal-Debiasing-Post-Click-CVR.md](./read-papers/2020_WWW_MultiDR_Causal-Debiasing-Post-Click-CVR.md) (2020) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| MUPL | D6 | [2026_arXiv_MUPL_Multi-Channel-Uplift-Policy-Learning.md](./read-papers/2026_arXiv_MUPL_Multi-Channel-Uplift-Policy-Learning.md) (2026) | Alibaba Group / Peking University | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| NoDeF | Not specified | [2018_arXiv_NoDeF_Nonparametric-Delayed-CVR.md](./read-papers/2018_arXiv_NoDeF_Nonparametric-Delayed-CVR.md) (2018) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| NVO | D4 — retention / lifetime value / long-horizon value | [2018_KDD_NVO_Notification-Volume-Control-Pinterest.md](./read-papers/2018_KDD_NVO_Notification-Volume-Control-Pinterest.md) (2018) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| OCARM | Not specified | [2026_arXiv_OCARM_Post-Conversion-Content-Retention.md](./read-papers/2026_arXiv_OCARM_Post-Conversion-Content-Retention.md) (2026) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| ODMN | D4 | [2022_CIKM_ODMN_Billion-User-LTV-Kuaishou.md](./read-papers/2022_CIKM_ODMN_Billion-User-LTV-Kuaishou.md) (2022) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| OneRec-V2 | D9 | [2025_arXiv_OneRec-V2_Lazy-Decoder-Real-Feedback.md](./read-papers/2025_arXiv_OneRec-V2_Lazy-Decoder-Real-Feedback.md) (2025) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| PDQ | D1 | [2026_arXiv_PDQ_Long-Term-Value-Prediction-Video-Ranking.md](./read-papers/2026_arXiv_PDQ_Long-Term-Value-Prediction-Video-Ranking.md) (2026) | Alibaba Group | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| PE-LTR | D1 | [2019_RecSys_PE-LTR_Pareto-Efficient-Multi-Objective-Ecommerce.md](./read-papers/2019_RecSys_PE-LTR_Pareto-Efficient-Multi-Objective-Ecommerce.md) (2019) | Not specified in selected-source metadata | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| PinnerFormer | D4 — retention / lifetime value / long-horizon value | [2022_KDD_PinnerFormer_Sequence-Modeling-User-Representation.md](./read-papers/2022_KDD_PinnerFormer_Sequence-Modeling-User-Representation.md) (2022) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| POPM | D3 | [2023_arXiv_POPM_Pareto-Optimal-Proxy-Metrics.md](./read-papers/2023_arXiv_POPM_Pareto-Optimal-Proxy-Metrics.md) (2023) | Google Inc. | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| PROXIMA | D3 | [2026_arXiv_PROXIMA_Proxy-Metric-Fragility.md](./read-papers/2026_arXiv_PROXIMA_Proxy-Metric-Fragility.md) (2026) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| Proximal-Surrogate-Index | D3 | [2026_arXiv_Proximal-Surrogate-Index_Unobserved-Confounding.md](./read-papers/2026_arXiv_Proximal-Surrogate-Index_Unobserved-Confounding.md) (2026) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| PUC | Not specified | [2025_ICML_PUC_Rethinking-Causal-Ranking.md](./read-papers/2025_ICML_PUC_Rethinking-Causal-Ranking.md) (2025) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| RAM | D2 | [2020_KDD_RAM_Jointly-Learning-Recommend-Advertise.md](./read-papers/2020_KDD_RAM_Jointly-Learning-Recommend-Advertise.md) (2020) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| RDSA | D4 — retention / lifetime value / long-horizon value | [2020_KDD_RDSA_Sleeping-Recovering-Bandit-Notifications.md](./read-papers/2020_KDD_RDSA_Sleeping-Recovering-Bandit-Notifications.md) (2020) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| REINFORCE-URM | D2 | [2021_WSDM_REINFORCE-URM_User-Response-Models-Improve-Recommender.md](./read-papers/2021_WSDM_REINFORCE-URM_User-Response-Models-Improve-Recommender.md) (2021) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| Rental-Ranking-Congestion | Not specified | [2023_arXiv_Rental-Ranking-Congestion.md](./read-papers/2023_arXiv_Rental-Ranking-Congestion.md) (2023) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| RERUM | D6 — causal uplift / incrementality | [2024_KDD_RERUM_Revenue-Uplift-Modeling.md](./read-papers/2024_KDD_RERUM_Revenue-Uplift-Modeling.md) (2024) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| ReSeq | D8 | [2023_RecSys_ReSeq_Reciprocal-Sequential-Recommendation.md](./read-papers/2023_RecSys_ReSeq_Reciprocal-Sequential-Recommendation.md) (2023) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| RevisitMTL | D4 | [2026_AAAI_RevisitMTL_Save-Revisit-Retain-User-Retention.md](./read-papers/2026_AAAI_RevisitMTL_Save-Revisit-Retain-User-Retention.md) (2026) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| RL-Pareto | D2 | [2026_arXiv_RL-Pareto_Personalized-Utility-Tuning-Pareto-Sweeping.md](./read-papers/2026_arXiv_RL-Pareto_Personalized-Utility-Tuning-Pareto-Sweeping.md) (2026) | Pinterest | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| RRS-Survey | Not specified | [2020_InformationFusion_RRS-Survey.md](./read-papers/2020_InformationFusion_RRS-Survey.md) (2020) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| SEC | D2 | [2025_CIKM_SEC_Stratified-Expert-Cloning-Retention-Aware.md](./read-papers/2025_CIKM_SEC_Stratified-Expert-Cloning-Retention-Aware.md) (2025) | Not specified in selected-source metadata | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| SLA | D1 | [2020_WWW_SLA_Product-Search-Stochastic-Label-Aggregation.md](./read-papers/2020_WWW_SLA_Product-Search-Stochastic-Label-Aggregation.md) (2020) | Not specified in selected-source metadata | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| SMILE | Not specified | [2018_NeurIPS_SMILE_Online-Reciprocal-Recommendation.md](./read-papers/2018_NeurIPS_SMILE_Online-Reciprocal-Recommendation.md) (2018) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| Social-Welfare-Ranking-Matching-Markets | Not specified | [2021_arXiv_Social-Welfare-Ranking-Matching-Markets.md](./read-papers/2021_arXiv_Social-Welfare-Ranking-Matching-Markets.md) (2021) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| SurrogateIndex | D3 — proxy/surrogate objectives | [2019_REStud_SurrogateIndex_Long-Term-Treatment-Effects.md](./read-papers/2019_REStud_SurrogateIndex_Long-Term-Treatment-Effects.md) (2019) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| TopK-OPE | D2 | [2019_WSDM_TopK-OPE_Top-K-Off-Policy-Correction-REINFORCE.md](./read-papers/2019_WSDM_TopK-OPE_Top-K-Off-Policy-Correction-REINFORCE.md) (2019) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| Trinity | D4 | [2024_KDD_Trinity_Multi-Long-Tail-Long-Term-Interests.md](./read-papers/2024_KDD_Trinity_Multi-Long-Tail-Long-Term-Interests.md) (2024) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| TS-DL | D7 | [2020_IJCAI_TS-DL_Attention-CVR-Post-Click-Calibration.md](./read-papers/2020_IJCAI_TS-DL_Attention-CVR-Post-Click-Calibration.md) (2020) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| TSCAC | D2 | [2023_WWW_TSCAC_Two-Stage-Constrained-Actor-Critic.md](./read-papers/2023_WWW_TSCAC_Two-Stage-Constrained-Actor-Critic.md) (2023) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| TSPR | Not specified | [2026_arXiv_TSPR_Marketplace-Experiments.md](./read-papers/2026_arXiv_TSPR_Marketplace-Experiments.md) (2026) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| Two-Sided-Experiment-Bias-Variance | Not specified | [2021_arXiv_Two-Sided-Experiment-Bias-Variance.md](./read-papers/2021_arXiv_Two-Sided-Experiment-Bias-Variance.md) (2021) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| UniROM | D9 | [2025_arXiv_UniROM_One-Model-to-Rank-Them-All.md](./read-papers/2025_arXiv_UniROM_One-Model-to-Rank-Them-All.md) (2025) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| VST | D1 | [2026_RecSys_VST_Multi-Objective-Live-Streaming-Ranking.md](./read-papers/2026_RecSys_VST_Multi-Objective-Live-Streaming-Ranking.md) (2026) | Twitch Interactive | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| Weighted-Training | Not specified | [2024_arXiv_Weighted-Training_AB-Loop-Interference.md](./read-papers/2024_arXiv_Weighted-Training_AB-Loop-Interference.md) (2024) | Not specified in cards | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |
| xMTF | D1 | [2025_WWW_xMTF_Formula-Free-RL-Multi-Task-Fusion.md](./read-papers/2025_WWW_xMTF_Formula-Free-RL-Multi-Task-Fusion.md) (2025) | Kuaishou | 0 | 0 | Not enough comparable cross-card metric evidence | N/A | N/A (0 in composite) | N/A (0 in composite) | 0 |

## Top Method Analysis

### Rank 1: DFM (Composite Score: 24)

- Why fundamental: Explicitly used or discussed as a baseline/comparator in 8 other cards; no unsupported simplicity or performance-consistency points were added.
- Representative paper: [2014_KDD_DFM_Modeling-Delayed-Feedback.md](./read-papers/2014_KDD_DFM_Modeling-Delayed-Feedback.md)
- Explicit baseline/comparator cards: 8
- Explicit derived-variant cards: 0
- Independent measured performance range: Not specified in cards in a comparable form.

### Rank 2: ESMM (Composite Score: 21)

- Why fundamental: Explicitly used or discussed as a baseline/comparator in 7 other cards; no unsupported simplicity or performance-consistency points were added.
- Representative paper: [2018_SIGIR_ESMM_Entire-Space-Multi-Task.md](./read-papers/2018_SIGIR_ESMM_Entire-Space-Multi-Task.md)
- Explicit baseline/comparator cards: 7
- Explicit derived-variant cards: 0
- Independent measured performance range: Not specified in cards in a comparable form.

### Rank 3: ZILN (Composite Score: 12)

- Why fundamental: Explicitly used or discussed as a baseline/comparator in 4 other cards; no unsupported simplicity or performance-consistency points were added.
- Representative paper: [2019_arXiv_ZILN_Probabilistic-Customer-Lifetime-Value.md](./read-papers/2019_arXiv_ZILN_Probabilistic-Customer-Lifetime-Value.md)
- Explicit baseline/comparator cards: 4
- Explicit derived-variant cards: 0
- Independent measured performance range: Not specified in cards in a comparable form.

### Rank 4: BatchRL-MTF (Composite Score: 6)

- Why fundamental: Explicitly used or discussed as a baseline/comparator in 2 other cards; no unsupported simplicity or performance-consistency points were added.
- Representative paper: [2022_KDD_BatchRL-MTF_Multi-Task-Fusion-Long-Term-Satisfaction.md](./read-papers/2022_KDD_BatchRL-MTF_Multi-Task-Fusion-Long-Term-Satisfaction.md)
- Explicit baseline/comparator cards: 2
- Explicit derived-variant cards: 0
- Independent measured performance range: Not specified in cards in a comparable form.

### Rank 5: ESM2 (Composite Score: 6)

- Why fundamental: Explicitly used or discussed as a baseline/comparator in 2 other cards; no unsupported simplicity or performance-consistency points were added.
- Representative paper: [2020_SIGIR_ESM2_Post-Click-Behavior-Decomposition.md](./read-papers/2020_SIGIR_ESM2_Post-Click-Behavior-Decomposition.md)
- Explicit baseline/comparator cards: 2
- Explicit derived-variant cards: 0
- Independent measured performance range: Not specified in cards in a comparable form.

### Rank 6: FID (Composite Score: 3)

- Why fundamental: Explicitly used or discussed as a baseline/comparator in 1 other card; no unsupported simplicity or performance-consistency points were added.
- Representative paper: [2024_KDD_FID_Future-Impact-Decomposition-Request-Level.md](./read-papers/2024_KDD_FID_Future-Impact-Decomposition-Request-Level.md)
- Explicit baseline/comparator cards: 1
- Explicit derived-variant cards: 0
- Independent measured performance range: Not specified in cards in a comparable form.

### Rank 7: GRM (Composite Score: 3)

- Why fundamental: Explicitly used or discussed as a baseline/comparator in 1 other card; no unsupported simplicity or performance-consistency points were added.
- Representative paper: [2025_SIGIR_GRM_Generative-List-Level-Multi-Objective-Reranking.md](./read-papers/2025_SIGIR_GRM_Generative-List-Level-Multi-Objective-Reranking.md)
- Explicit baseline/comparator cards: 1
- Explicit derived-variant cards: 0
- Independent measured performance range: Not specified in cards in a comparable form.

### Rank 8: KuaiSim (Composite Score: 3)

- Why fundamental: Explicitly used or discussed as a baseline/comparator in 1 other card; no unsupported simplicity or performance-consistency points were added.
- Representative paper: [2023_arXiv_KuaiSim_Comprehensive-Recommender-System-Simulator.md](./read-papers/2023_arXiv_KuaiSim_Comprehensive-Recommender-System-Simulator.md)
- Explicit baseline/comparator cards: 1
- Explicit derived-variant cards: 0
- Independent measured performance range: Not specified in cards in a comparable form.

### Rank 9: LOPE (Composite Score: 3)

- Why fundamental: Explicitly used or discussed as a baseline/comparator in 1 other card; no unsupported simplicity or performance-consistency points were added.
- Representative paper: [2024_SpotifyResearch_LOPE_Estimating-Long-Term-Outcome-Algorithms.md](./read-papers/2024_SpotifyResearch_LOPE_Estimating-Long-Term-Outcome-Algorithms.md)
- Explicit baseline/comparator cards: 1
- Explicit derived-variant cards: 0
- Independent measured performance range: Not specified in cards in a comparable form.

### Rank 10: NSW (Composite Score: 3)

- Why fundamental: Explicitly used or discussed as a baseline/comparator in 1 other card; no unsupported simplicity or performance-consistency points were added.
- Representative paper: [2026_arXiv_NSW_Fair-High-Match-Reciprocal-Recommendation.md](./read-papers/2026_arXiv_NSW_Fair-High-Match-Reciprocal-Recommendation.md)
- Explicit baseline/comparator cards: 1
- Explicit derived-variant cards: 0
- Independent measured performance range: Not specified in cards in a comparable form.
