# Paper Analysis: Reciprocal Sequential Recommendation

**Source:** https://arxiv.org/pdf/2306.14712
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Reciprocal Sequential Recommendation
- **authors or company:** Bowen Zheng et al. (RUCAIBox)
- **venue:** RecSys 2023
- **year:** 2023
- **URL:** https://arxiv.org/pdf/2306.14712
- **source type:** academic/industry
- **direction:** D8
- **problem setting:** Reciprocal recommender systems (online dating, recruitment) where both parties have evolving preferences over time; existing RRS work captures static preferences and one-sided sequential models ignore dual-role users.
- **objective and label definition:** Joint loss L = L_ma + λ·L_mi + μ·L_sd (macro BPR + micro BPR + Margin-MSE self-distillation); positive label is bilateral mutually-agreed interaction (interview-reached pairs in recruitment; matched questioner-answerer in Q&A); sequences truncated to current time step — no calendar retention window; delay and censoring not addressed.
- **prediction or incrementality:** Prediction only — predicts matching-degree score for user pairs; no causal or counterfactual effect of exposure.
- **model architecture:** Dual embedding matrices per user (active/preference and passive/feature) partially shared via matrix C; two Transformer encoders per side (unidirectional for active behavior, bidirectional for passive); macro dot-product matching plus micro TiSensiMatch co-attention; micro-to-macro self-distillation deploys only cheap macro module at serving.
- **credit assignment:** Pointwise per bilateral pair (u_i, v_j); no slate-level, impression-level, or coordinate-based credit assignment.
- **training data and counterfactual handling:** Historical observational sequential logs with 100 randomly sampled negatives per positive per side for BPR losses; no off-policy correction or propensity weighting.
- **offline and online evaluation:** Offline only: HR@5, NDCG@5, MRR@5 dual-perspective on five datasets (three Chinese recruitment, two Stack Exchange Q&A); per-batch serving latency to validate distillation speedup; no online A/B reported.
- **reported gains:** Design recruitment HR@5 0.4435 vs. DPGNN 0.2422 and SASRec 0.2033; Technology recruitment HR@5 0.7597 vs. DPGNN 0.4521; AskUbuntu HR@5 0.5259 vs. FMLP-Rec 0.2706; latency 0.2832 ms/batch (with distillation) vs. 8.7105 ms/batch (without) vs. 0.1024 ms/batch (SASRec).
- **applicability note for a two-sided dating recommender:** Dual-role sequential architecture directly analogous to dating where both A and B have evolving preferences; active/passive embeddings and train-fine-grained/deploy-cheap distillation pattern are reusable engineering patterns.
- **applicability note for a two-sided dating recommender:** No congestion or capacity treatment — matches scored independently with no shared-resource constraint; objective is short-term match propensity only, no retention/revenue term or incrementality framing.
- **unverified claims:** "First to consider dynamic behavior sequences of two parties in reciprocal recommendation" is self-reported; recruitment dataset gains cannot be independently reproduced (proprietary data); latency overhead vs. one-sided SASRec claimed "inevitable" not proven as lower bound.

## 1. Summary

Zheng et al. formulate reciprocal recommendation as sequence matching and propose ReSeq: separate active/passive user embeddings encoded by Transformers at macro (deployed) and micro (training-only) scales, with micro-to-macro self-distillation so only the cheap macro module serves in production. Macro matching is dot-product sum of dual perspectives; micro TiSensiMatch uses fine-grained co-attention with recency weighting. Evaluated on three recruitment and two Stack Exchange Q&A datasets against collaborative filtering, one-sided sequential, and person-job-fit baselines.

## Project Relevance

Relevant to **Q2** as pointwise per-pair architecture matching per-candidate-profile decision granularity, and **Q3** as confirmation that literature uses static resolved logs with no delay/censoring — gap vs. 7–30 day retention horizon. Main positive contribution is architectural (**Q8**): train-fine-grained/deploy-cheap distillation could let a unified retention model use rich two-sided signals in training with low inference cost. Reciprocity modeled as joint architecture with shared decomposed embeddings, not independent one-sided score fusion. Congestion explicitly not addressed. Clean negative for Q1/Q5: short-term match propensity only.

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | Bilateral match/interview propensity; retention/revenue not included. |
| **(2) Credit assignment** | Pointwise per-pair score; no slate or impression attribution. |
| **(3) Label / horizon; delay / sparsity / censoring** | Sequence truncation by position; no calendar-time retention window; delay/censoring not addressed. |
| **(4) Short-term vs long-term head fusion** | Not specified in source. |
| **(5) Prediction vs incrementality** | Prediction only. |
| **(6) Offline / online eval** | Offline HR@5/NDCG@5/MRR@5 plus latency; no online A/B. |
| **(7) Reciprocity / congestion / fairness / revenue vs match** | Joint dual-perspective reciprocity; congestion not modeled. |
| **(8) CTR → unified long-term migration** | Self-distillation serving pattern transferable; no LTV objective migration described. |

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Bowen Zheng et al.  
**Affiliations:** RUCAIBox / Beijing Key Laboratory of Big Data Management and Analysis Methods  
**Venue:** RecSys 2023  
**Year:** 2023  
**Relevance:** Core  
**Priority:** 1
