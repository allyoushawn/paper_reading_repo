# Paper Analysis: Scaling the Instagram Explore Recommendations System

**Source:** https://engineering.fb.com/2023/08/09/ml-applications/scaling-instagram-explore-recommendations-system/
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Scaling the Instagram Explore Recommendations System
- **authors or company:** Vladislav Vorotilov, Ilnur Shugaepov (Meta / Instagram)
- **venue:** Meta Engineering Blog
- **year:** 2023
- **URL:** https://engineering.fb.com/2023/08/09/ml-applications/scaling-instagram-explore-recommendations-system/
- **source type:** blog
- **direction:** D1
- **problem setting:** Instagram Explore multi-stage funnel (retrieval → first-stage rank → second-stage rank → final rerank) serving hundreds of millions of daily users from billions of media candidates under latency constraints.
- **objective and label definition:** Short-horizon engagement events (click, like, see less, etc.) predicted by MTML second-stage ranker; combined via tunable value model (VM) weights into Expected Value score per item—not explicit retention/LTV labels.
- **prediction or incrementality:** Predicts probabilities of immediate engagement events; VM linearly fuses heads with tunable weights W_click, W_like, W_see_less, etc.
- **model architecture:** Two Towers NN for retrieval and first-stage ranking (with distillation label PSelect = top-K from second stage); second-stage MTML neural network with user-item interaction features; integrity/diversity reranking rules; hourly continual online fine-tuning; Bayesian optimization or offline metric-mapping for hundreds of tunable parameters.
- **credit assignment:** Per-item expected value from multi-event probabilities at ranking stage; no user-level delayed outcome attribution to individual exposures described.
- **training data and counterfactual handling:** Production interaction logs; first-stage distillation from second-stage teacher; precomputed recommendations for some users off-peak; rule-based filtering of low-quality history items before similarity retrieval.
- **offline and online evaluation:** Not specified in source for quantitative A/B tables; offline tuning maps offline metric changes to predicted online changes when historical offline/online metric pairs exist; online BO can take weeks/months to converge.
- **reported gains:** Not specified in source (no numeric lift percentages in blog post).
- **applicability note for a two-sided dating recommender:** Reference architecture for multi-stage funnel with distillation, MTML multi-event fusion, and VM weight tuning—applicable when candidate pools are large and latency forces lightweight early stages.
- **applicability note for a two-sided dating recommender:** Engagement VM on one-sided content consumption does not address match reciprocity, bilateral congestion, or retention labels beyond tunable short-term engagement weights.
- **unverified claims:** none

## 1. Summary

**Title:** Scaling the Instagram Explore Recommendations System
**Authors:** Vladislav Vorotilov, Ilnur Shugaepov (Meta)
**Abstract:** Engineering overview of Instagram Explore's scalable four-stage ranking funnel emphasizing caching, pre-computation, Two Towers models, MTML second-stage ranking, value-model fusion, and parameter tuning at Meta production scale.

**Key contributions:**
- Multi-stage funnel with Two Towers at retrieval and first-stage rank, MTML at second stage, and business-rule reranking.
- Knowledge distillation from heavy second-stage ranker to lightweight first stage (PSelect label).
- Continual hourly online training and dual approaches to tuning hundreds of system parameters (online BO vs offline metric mapping).

**Methodology:** Candidate retrieval from multiple sources (Two Towers ANN, user interaction history, heuristics); Expected Value = weighted sum of predicted engagement probabilities; integrity and diversity post-processing.

**Main results:** Not specified in source (qualitative claims of improved scalability and flexibility; no reported metric lifts).

## 2. Experiment Critique

**Design:** Conceptual architecture post; compares against legacy Word2Vec retrieval and heuristics; no controlled experiment tables.

**Statistical validity:** Not specified in source.

**Online experiments (if any):** Not specified in source beyond describing BO and offline tuning workflows.

**Reproducibility:** No datasets, metrics, or model weights disclosed.

**Overall:** Useful systems blueprint; insufficient for quantitative benchmarking; long-term objectives absent from VM formulation described.

## 3. Industry Contribution

**Deployability:** Describes production Explore stack at Meta scale with explicit latency/caching strategies.

**Problems solved:** Scaling heavy models via funneling, embedding caches, ANN retrieval, off-peak precomputation, and distillation.

**Engineering cost:** Very high operational complexity (hundreds of tunable parameters, multiple stages, hourly retraining).

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Clever caching/pre-computation across stages; Two Towers extending Word2Vec for multi-objective retrieval with arbitrary features.

**Prior work comparison:** Word2Vec embeddings, heuristic retrieval, standard multi-stage recommender funnel patterns.

**Verification:** Engineering evolution narrative rather than novel ML objective; distillation and MTML are established patterns.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Instagram Explore production traffic | Not public | No | Blog describes scale only |

**Offline experiment reproducibility:** Not specified in source.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** CTR-like engagement proxies (click, like, see less, etc.) fused via value model; maximizes tunable engagement tradeoffs—not retention, LTV, or revenue labels stated.

**(2) Credit assignment:** Per-item ranking score from VM over predicted event probabilities for one impression/slate position; user-level delayed outcomes not specified in source.

**(3) Label and horizon definitions:** Engagement event labels for MTML training; PSelect distillation label for first stage; delay, sparsity, censoring handling not specified in source.

**(4) Short-term + long-term heads:** MTML multi-event heads with fixed tunable linear fusion (value model weights)—fixed fusion, not learned long-term head.

**(5) Prediction vs incrementality:** Predicts engagement event probabilities; not effect of exposure on long-term outcome.

**(6) Offline and online evaluation:** Offline tuning via learned offline→online metric mapping; online Bayesian optimization; no numeric A/B retention results; two-sided interference not specified in source.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Not specified in source.

**(8) Migration path from CTR-like model:** Extends Word2Vec/heuristic retrieval to feature-rich Two Towers and MTML with VM weight tuning and distillation—stays within engagement-proxy fusion rather than unified long-term model.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Vladislav Vorotilov, Ilnur Shugaepov
**Affiliations:** Meta (Instagram)
**Venue:** Meta Engineering Blog
**Year:** 2023
**PDF:** unavailable (blog post)
**Relevance:** Core
**Priority:** 1
