# Paper Analysis: Scaling the Instagram Explore Recommendations System

**Source:** https://engineering.fb.com/2023/08/09/ml-applications/scaling-instagram-explore-recommendations-system/
**Date analyzed:** 2026-08-17

## 1. Summary

Meta engineers Vladislav Vorotilov and Ilnur Shugaepov describe the multi-stage ranking architecture behind Instagram Explore, a one-sided content-discovery surface serving hundreds of millions of people daily. The pipeline has four stages: retrieval (multiple candidate sources, including a Two Tower NN extending Word2Vec, feeding an ANN service such as FAISS or HNSW), first-stage ranking (a cacheable Two Tower NN trained to distill the second-stage ranker's top-K output), second-stage ranking (a heavier multi-task multi-label — MTML — neural network predicting per-event probabilities such as P(click), P(like), P(see less)), and final reranking (rule-based integrity and diversity filters). The key contribution for this survey is the **value model (VM)**: the second-stage probabilities are combined into one ranking score via a fixed linear formula, `Expected Value = W_click*P(click) + W_like*P(like) - W_see_less*P(see less) + etc.`, with per-signal weights tuned via either online Bayesian optimization or offline tuning (learning a mapping from offline to online metric changes). No dataset, baseline, or quantitative result of any kind is reported anywhere in the post.

## 2. Experiment Critique

There is no experiment section. The post is an architecture explainer with no reported metrics, no A/B test description, and no statistical methodology — only a qualitative description of two parameter-tuning strategies (online Bayesian optimization; offline tuning via a learned offline-to-online metric mapping, which the authors state requires "a strong correlation between offline and online metrics"). Reproducibility is effectively zero: no hyperparameters, no loss functions, no feature lists, no evaluation numbers.

## 3. Industry Contribution

This is a rare, explicit public description of how a top-tier platform turns several independently trained event-probability heads into one deployable ranking score. Deployability concerns raised: Two Tower architectures are chosen specifically for cacheability (embeddings can be precomputed and served via ANN lookup), at the stated cost of being unable to consume user-item interaction features; the second-stage MTML model is heavier and partly precomputed offline during off-peak hours to manage serving load; models are retrained/fine-tuned hourly via continual online training to track behavior shifts. The first-stage-distills-second-stage pattern (`PSelect = media in top K results ranked by the second stage`) is a concrete, reusable knowledge-distillation recipe for funnel-style ranking systems.

## 4. Novelty vs. Prior Work

The post does not position itself against prior work — there is no related-work section or citation list. It links to, but does not describe in detail, Word2Vec, Two Tower NNs, FAISS, and HNSW as established building blocks, and cross-links three other Meta engineering posts (News Feed ranking, Instagram notification management with causal inference, and ML data ingestion at Meta) without summarizing their content or claiming novelty relative to them.

## 5. Dataset Availability

| Dataset | Public/Private | Size | Access |
|---|---|---|---|
| Not specified in source | — | — | — |

No dataset, internal or public, is named anywhere in the post.

## 6. Community Reaction

Not assessed in text-source mode.

## 7. Reference Card

| # | Field | Value |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Scaling the Instagram Explore Recommendations System"; Vladislav Vorotilov, Ilnur Shugaepov (Meta); Meta Engineering Blog; 2023; https://engineering.fb.com/2023/08/09/ml-applications/scaling-instagram-explore-recommendations-system/ |
| 2 | Source type | blog |
| 3 | Direction | D1 |
| 4 | Problem setting | Multi-stage candidate ranking for a large-scale one-sided content-discovery surface (Instagram Explore), combining several predicted engagement probabilities into one final ranking score. |
| 5 | Objective and label definition | Second-stage MTML predicts multiple short-term engagement-event probabilities (click, like, "see less", etc.); first-stage ranker's label is distillation-based (top-K membership from the second stage), not an engagement label. No horizon or delay handling stated anywhere. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. |
| 7 | Model architecture | Two Tower NN (retrieval and first-stage ranking, Word2Vec-style, ANN-servable); MTML neural network (second-stage ranking, per-event probabilities); Value Model — a fixed linear weighted-sum formula combining those probabilities; rule-based final reranking layer for integrity/diversity. |
| 8 | Credit assignment | Not addressed — scoring is per single impression/item; no mapping from a delayed or user-level outcome to an item-level decision is discussed. |
| 9 | Training data and counterfactual handling | Not specified in source. No dataset description; no counterfactual or off-policy correction discussed. |
| 10 | Offline and online evaluation | Not specified in source beyond parameter-tuning methodology: online Bayesian optimization (stated to sometimes take "more than a month" to converge), or offline tuning via a learned offline→online metric mapping (contingent on offline/online correlation). |
| 11 | Reported gains | Not specified in source — no dataset, no metric, and no quantitative result of any kind is reported. |
| 12 | Applicability to a two-sided dating recommender | The Value Model formula is a directly transferable pattern for combining a dating app's like/match/conversation probability heads into one weighted ranking score. It does not, however, address reciprocity, congestion, or the long-horizon retention/revenue objectives a dating recommender needs. |
| 13 | Unverified claims | "The end goal of tuning weights is to find a good tradeoff that maximizes our goals without hurting other important metrics" is asserted with no supporting experiment or number. The claim that hourly retraining is necessary "to adapt to changing trends... very quickly" is likewise asserted without evidence in this post. |

## Project Relevance

Speaks directly to **Q4** — the Value Model is a documented, explicit example of the "fixed fusion" branch of combining short-term event heads into one score via a hand-tuned linear formula, one of the very few public statements of this pattern from a major platform. Secondarily relevant to **Q1** as a negative data point: it confirms that at Meta's scale, the ranking objective is still a set of short-term engagement events (click, like, "see less"), blended after prediction — exactly the "predict-then-blend" pattern this survey's target design aims to replace, not an example of a unified retention/revenue objective. Does not address Q2, Q3, Q5, Q6, Q7, or Q8.

## Papers That Mention This Paper (Reverse Citation Map)

_This paper proposes no distinctively-named method, so no automated reverse-citation match was possible._

## Meta Information

- **Authors:** Vladislav Vorotilov, Ilnur Shugaepov
- **Affiliation:** Meta (Instagram)
- **Venue:** Meta Engineering Blog
- **Year:** 2023
- **Relevance:** Core
- **Priority:** 1
- **Source ID:** nlm:f11ef30f
