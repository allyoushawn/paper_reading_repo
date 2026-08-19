# Phase 3 Batch Log — Indices 021–040

model_identifier: codex-sol  
notebook_id: 67046a44-7490-4fe5-b54a-3f39ef37fdd3  
date: 2026-08-18

## Status

| Index | Filename | Source ID | Query 1 | Query 2 | Project query | Fallback |
|---:|---|---|---|---|---|---|
| 21 | `2024_WWW_LOPE_Long-term-Off-Policy-Evaluation-Learning.md` | `7fee3f6b-6faa-436e-aa21-d9477fef7739` | success | success | success | not needed |
| 22 | `2024_KDD_GFN4Retention_Modeling-User-Retention-Generative-Flow-Networks.md` | `3183e5a0-4ebb-4f26-bd56-5be0441fe5a5` | success | success | success | not needed |
| 23 | `2023_KDD_ImpatientBandit_Optimizing-Recommendations-Long-Term-Without-Delay.md` | `5a389db3-49b0-4a99-b6da-bfa1d0e295c5` | not completed: generative throttling plateau | not completed: generative throttling plateau | not completed: generative throttling plateau | `source_get_content` success |
| 24 | `2023_arXiv_Stickiness_Optimizing-Audio-Recommendations-Long-Term.md` | `69ceeb8b-8273-4163-8aa6-2a347b6b6d7d` | not completed: generative throttling plateau | not completed: generative throttling plateau | not completed: generative throttling plateau | `source_get_content` success |
| 25 | `2023_WWW_RLUR_Reinforcing-User-Retention-Billion-Scale.md` | `192447f1-df6d-4e75-a91b-b1e550047316` | not completed: generative throttling plateau | not completed: generative throttling plateau | not completed: generative throttling plateau | `source_get_content` success |
| 26 | `2023_WWW_TSCAC_Two-Stage-Constrained-Actor-Critic.md` | `7b46f4f0-1894-4ce7-a0e3-603669e259f8` | not completed: generative throttling plateau | not completed: generative throttling plateau | not completed: generative throttling plateau | `source_get_content` success |
| 27 | `2022_KDD_BatchRL-MTF_Multi-Task-Fusion-Long-Term-Satisfaction.md` | `b0d40032-08a0-4c62-ad6b-c138b9a2649d` | not run: plateau escape | not run: plateau escape | not run: plateau escape | `source_get_content` success |
| 28 | `2021_WSDM_REINFORCE-URM_User-Response-Models-Improve-Recommender.md` | `2d129fa5-3f44-4781-ad86-aafac5b1edde` | not run: plateau escape | not run: plateau escape | not run: plateau escape | `source_get_content` success |
| 29 | `2020_KDD_RAM_Jointly-Learning-Recommend-Advertise.md` | `d75e5cef-8c37-462c-942c-6c3740f90d53` | not run: plateau escape | not run: plateau escape | not run: plateau escape | `source_get_content` success |
| 30 | `2019_WSDM_TopK-OPE_Top-K-Off-Policy-Correction-REINFORCE.md` | `7a977c61-586e-4d30-bdfb-ed4d50db5e0e` | not run: plateau escape | not run: plateau escape | not run: plateau escape | `source_get_content` success |
| 31 | `2019_WWW_ValueRL_Value-Aware-Recommendation-Profit-Maximization.md` | `24671e17-db74-4dee-a39b-a66615a2c8b7` | not run: plateau escape | not run: plateau escape | not run: plateau escape | `source_get_content` success |
| 32 | `2018_WWW_DRN_Deep-Reinforcement-Learning-News-Recommendation.md` | `dba8d2e4-c664-491b-8f06-58fbfca958e7` | not run: plateau escape | not run: plateau escape | not run: plateau escape | `source_get_content` success |
| 33 | `2024_SpotifyResearch_LOPE_Estimating-Long-Term-Outcome-Algorithms.md` | `f5a62abd-107f-4425-81cc-c84115c70732` | not run: plateau escape | not run: plateau escape | not run: plateau escape | `source_get_content` success |
| 34 | `2024_KDD_TC_Covariance-Treatment-Effects-Weak-Experiments.md` | `c1ecf43e-b2fb-4390-b230-51e1467ae520` | not run: plateau escape | not run: plateau escape | not run: plateau escape | `source_get_content` success |
| 35 | `2026_WWW_CC-OR-Net_Unified-LTV-Structural-Decoupling.md` | `a419bd95-0f0d-4c80-aada-666d4e466722` | not run: plateau escape | not run: plateau escape | not run: plateau escape | `source_get_content` success |
| 36 | `2026_AAAI_RevisitMTL_Save-Revisit-Retain-User-Retention.md` | `ab9db06f-530d-4123-adce-92e44aa285ad` | not run: plateau escape | not run: plateau escape | not run: plateau escape | `source_get_content` success |
| 37 | `2025_KDD_GRePO-LTV_Mini-Game-Lifetime-Value-WeChat.md` | `d1771ff1-bd8d-4afc-bd1a-2641e505512f` | not run: plateau escape | not run: plateau escape | not run: plateau escape | `source_get_content` success |
| 38 | `2024_KDD_Trinity_Multi-Long-Tail-Long-Term-Interests.md` | `9f0afe43-389d-484d-9739-aa4aab3a141e` | not run: plateau escape | not run: plateau escape | not run: plateau escape | `source_get_content` success |
| 39 | `2023_AAAI_CDAF_Cross-Domain-Adaptative-LTV-Prediction.md` | `f0fa7383-2d13-484c-b3fc-51757c2c2d9d` | not run: plateau escape | not run: plateau escape | not run: plateau escape | `source_get_content` success |
| 40 | `2022_CIKM_ODMN_Billion-User-LTV-Kuaishou.md` | `80cf2edd-3189-41ee-8bb3-15129f84505a` | not run: plateau escape | not run: plateau escape | not run: plateau escape | `source_get_content` success |

## Counts

- Assigned: 20
- Cards created: 20
- Query-complete cards: 2
- Indexed-source fallback cards: 18
- Skipped: 0
- Failed: 0
- Missing cards: 0

## Failure / Extraction Note

The independent generative queries succeeded for indices 21–22. The next four-source query batch plateaued under NotebookLM generative throttling and was terminated without reliable per-query completion status. Per the orchestration plateau escape, no further generative queries were started; each remaining source was read once with NotebookLM `source_get_content`. Every fallback card is marked `Extraction mode: NotebookLM indexed source content fallback (generative query throttling)`, and absent fields use `Not specified in source.` No `conversation_id` was used.
