# Phase 3 Card Batch Log — Indices 41–60

- model_identifier: codex-sol
- notebook_id: 67046a44-7490-4fe5-b54a-3f39ef37fdd3
- selected-source indices: 41–60
- processed: 20
- skipped: 0
- failed: 0
- query policy: no conversation_id used
- plateau handling: card 41 completed from three successful independent source-scoped Phase 3 queries; after the query plateau, parent directed stopping new notebook queries and using one indexed-content extraction per remaining source.
- refusal normalization: no retained refusal language; absent evidence is rendered as “Not specified in source” or an explicit extraction limitation.
- fallback: indices 42–60 use NotebookLM source_get_content. Index 57's indexed source was arXiv abstract/metadata rather than the full paper; its card explicitly limits claims accordingly.

| Index | Source ID | Status | Evidence mode | Card |
|---:|---|---|---|---|
| 41 | 29080c52-b3ed-4ef6-b2ad-36e4c1da2d6e | Processed | 3 independent source-scoped queries | 2022_KDD_PinnerFormer_Sequence-Modeling-User-Representation.md |
| 42 | 58fc435a-363d-4c95-92d4-f6100f86547e | Processed | indexed-content fallback | 2020_KDD_RDSA_Sleeping-Recovering-Bandit-Notifications.md |
| 43 | a9ecf330-e216-4712-9780-8d9112d7a12d | Processed | indexed-content fallback | 2019_arXiv_ZILN_Probabilistic-Customer-Lifetime-Value.md |
| 44 | 1c974611-15e5-462d-93e8-7e59a8b17982 | Processed | indexed-content fallback | 2018_KDD_NVO_Notification-Volume-Control-Pinterest.md |
| 45 | 9056570a-ec35-4c30-af2b-808b91c53de9 | Processed | indexed-content fallback | 2023_CIKM_MTL_Immersive-Feed-No-More-Clicks.md |
| 46 | ad032348-2b1f-4018-8ed5-15768681767b | Processed | indexed-content fallback | 2021_SIGIR_HM3_Hierarchical-Micro-Macro-Behaviors.md |
| 47 | 876bc6f2-0112-448e-8fac-ae78057dc1f0 | Processed | indexed-content fallback | 2021_KDD_AITM_Sequential-Multi-Step-Conversions.md |
| 48 | e253a958-bfba-4cf7-aaf8-fb74b5fc6a14 | Processed | indexed-content fallback | 2020_SIGIR_ESM2_Post-Click-Behavior-Decomposition.md |
| 49 | 311e06b5-24ae-4a29-93fa-887ce0868211 | Processed | indexed-content fallback | 2020_WWW_MultiDR_Causal-Debiasing-Post-Click-CVR.md |
| 50 | f9d15f60-f3ba-4949-bab1-c1ce17615a03 | Processed | indexed-content fallback | 2018_SIGIR_ESMM_Entire-Space-Multi-Task.md |
| 51 | cfc316a0-65fd-4330-8add-d39b74011f4d | Processed | indexed-content fallback | 2024_KDD_RERUM_Revenue-Uplift-Modeling.md |
| 52 | b83e95c9-ea83-45f3-993e-ec1f8a956e8d | Processed | indexed-content fallback | 2020_arXiv_AUUCmax_Treatment-Targeting-AUUC.md |
| 53 | 519eb255-08ec-4750-a7f8-7321dc17fa15 | Processed | indexed-content fallback | 2020_arXiv_BudgetSplit_Trustworthy-Marketplace-Experimentation.md |
| 54 | 5ea68e79-8249-42ee-af99-0f0f4dd1840d | Processed | indexed-content fallback | 2026_SIGIR_CM-DCM_Counterfactual-Delayed-Conversion.md |
| 55 | d16aaef1-3541-47de-9542-b6cb80a8e3f4 | Processed | indexed-content fallback | 2022_WWW_DEFUSE_Delayed-Feedback-Label-Correction.md |
| 56 | adf6d4a9-2fef-4bed-a95e-da11d5b00a5e | Processed | indexed-content fallback | 2021_AAAI_ESDFM_Elapsed-Time-Sampling-Delayed-Feedback.md |
| 57 | 37991319-4bdb-4953-ac0c-c9206bc92413 | Processed | indexed abstract/metadata fallback | 2021_KDD_DEFER_Real-Negatives-Delayed-Feedback.md |
| 58 | ee57717b-2970-4b54-ac93-ab024d7e503a | Processed | indexed-content fallback | 2019_RecSys_FNC_Delayed-Feedback-Continuous-Training.md |
| 59 | 4eb91866-7a34-46eb-98ae-42405788f46c | Processed | indexed-content fallback | 2014_KDD_DFM_Modeling-Delayed-Feedback.md |
| 60 | 5f2155d9-f8d0-4247-a21e-eef7f102c721 | Processed | indexed-content fallback | 2023_RecSys_TU_Fast-Examination-Agnostic-Reciprocal.md |

