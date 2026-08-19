# Paper Analysis: Powered by AI: Instagram's Explore Recommender System

**Source:** https://ai.meta.com/blog/powered-by-ai-instagrams-explore-recommender-system/
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** Powered by AI: Instagram's Explore Recommender System
- **authors or company:** Ivan Medvedev, Haotian Wu, Taylor Gordon (Meta / Instagram)
- **venue:** Meta AI Blog
- **year:** 2019
- **URL:** https://ai.meta.com/blog/powered-by-ai-instagrams-explore-recommender-system/
- **source type:** blog
- **direction:** D1
- **problem setting:** Instagram Explore recommends public posts to users who do not follow the authors; system extracts 65B features and makes 90M model predictions per second via a 3-part ranking funnel over account-level retrieval (ig2vec account embeddings, IGQL candidate generation) and media ranking.
- **objective and label definition:** MTML final-pass model predicts positive actions (like, save) and negative actions (e.g., “See Fewer Posts Like This”); value model fuses head probabilities with tunable weights; short-horizon engagement labels—no retention/LTV horizon stated.
- **prediction or incrementality:** Predicts per-action probabilities combined via weighted arithmetic value model; predictive engagement scoring, not incremental long-term effect of an exposure.
- **model architecture:** Candidate generation (seed accounts → ig2vec KNN → media); 500 candidates sampled; 3-stage ranker (distillation 500→150, lightweight NN 150→50, deep MTML 50→25); shared MLP MTML; value model = w_like·P(Like) + w_save·P(Save) − w_negative·P(Negative Action) plus author/seed diversity penalties.
- **credit assignment:** Per media item in Explore grid; value model score ranks candidates; diversity heuristic downranks repeated authors/seed accounts deeper in batch; no user-level delayed outcome attribution to individual impressions described.
- **training data and counterfactual handling:** Account embeddings from ig2vec (account-ID sequences); distillation model trained on logged heavy-ranker outputs (NDCG loss); policy-violating and spam content filtered pre-ranking; no counterfactual training stated.
- **offline and online evaluation:** Offline replay tool plus Bayesian optimization for value-model weight tuning; no numeric A/B lift tables in source.
- **reported gains:** Not specified in source (qualitative claims of personalized discovery at scale; no percentage lifts stated).
- **applicability note for a two-sided dating recommender:** MTML + explicit value-model formula is a reusable pattern for fusing swipe-right, message, unmatch, and “see fewer” probabilities with tunable business weights and diversity penalties on repeated profiles.
- **applicability note for a two-sided dating recommender:** One-sided content discovery framing; no reciprocal match quality, supply-side congestion, or delayed retention labels—value model optimizes immediate engagement proxies only.
- **unverified claims:** Initial direct fetch of primary URL returned a Meta error page; card content verified from successful re-fetch of same URL (content matches published blog).

## 1. Summary

**Title:** Powered by AI: Instagram's Explore Recommender System
**Authors:** Ivan Medvedev, Haotian Wu, Taylor Gordon (Meta)
**Abstract:** First detailed overview of Instagram Explore’s AI stack: IGQL for rapid experimentation, ig2vec account embeddings for retrieval, ranking distillation, and MTML + value-model fusion for final ranking.

**Key contributions:**
- IGQL domain-specific language for composable candidate-generation and ranking pipelines.
- ig2vec account embeddings with FAISS KNN retrieval at millions-of-accounts scale.
- Ranking distillation preselecting 150/500 candidates before heavy MTML.
- Value model arithmetic fusion of calibrated action probabilities with diversity heuristics.

**Methodology:** Two-stage pipeline (candidate generation → 3-pass ranking); ~500 eligible media per request; MTML shared MLP over dense + sparse features in final pass.

**Main results:** Not specified in source (systems scale and design described; no quantitative metric lifts).

## 2. Experiment Critique

**Design:** Architecture overview post; embedding quality assessed via topic classifier on hold-out accounts.

**Statistical validity:** Not specified in source for end-to-end recommendation quality.

**Online experiments (if any):** Bayesian optimization and offline replay for value-model tuning; no A/B numbers reported.

**Reproducibility:** No public data, features, or model weights.

**Overall:** Canonical industrial reference for MTML + value model; lacks long-term objective or numeric evaluation.

## 3. Industry Contribution

**Deployability:** Production Explore serving billions-scale inventory with 90M predictions/sec.

**Problems solved:** Latency vs relevance via distillation funnel; account-level retrieval for thematic communities; fast experimentation via IGQL.

**Engineering cost:** Custom DSL, embedding infrastructure, multi-stage serving, and BO/replay tuning stack.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** IGQL, ig2vec retrieval, and integrated 3-part ranking funnel for Explore.

**Prior work comparison:** word2vec-style embeddings; standard multi-stage recommender patterns; Bayesian optimization for weight tuning.

**Verification:** Engineering integration narrative; MTML value fusion is now industry-standard pattern.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Instagram Explore production traffic | Not public | No | Scale metrics only |

**Offline experiment reproducibility:** Not specified in source.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** Short-horizon engagement proxies (like, save, negative feedback) fused via tunable value model—not retention, LTV, or revenue.

**(2) Credit assignment:** Per-item value-model score for one impression position in Explore grid; user-level delayed outcomes not specified in source.

**(3) Label and horizon definitions:** Immediate engagement event labels for MTML; delay/sparsity/censoring for long-term outcomes not specified in source.

**(4) Short-term + long-term heads:** MTML multi-event heads with fixed/tunable linear value-model fusion—no long-term head.

**(5) Prediction vs incrementality:** Predicts engagement probabilities; not exposure incrementality on retention.

**(6) Offline and online evaluation:** Offline replay + Bayesian optimization for weight tuning; no numeric retention A/B; two-sided interference not specified in source.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Author/seed diversity downranking only; bilateral market concerns not specified in source.

**(8) Migration path from CTR-like model:** Distillation + MTML + separable value-model weights—extends engagement-proxy ranking with faster tuning, not unified long-term model.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Ivan Medvedev, Haotian Wu, Taylor Gordon
**Affiliations:** Meta (Instagram)
**Venue:** Meta AI Blog
**Year:** 2019
**PDF:** unavailable (blog post)
**Relevance:** Core
**Priority:** 1
