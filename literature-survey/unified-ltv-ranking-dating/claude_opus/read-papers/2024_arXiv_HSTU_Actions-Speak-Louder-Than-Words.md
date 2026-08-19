# Paper Analysis: Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations

**Source:** /Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/2024 (Meta) (Arxiv) ** [GR] Actions Speak Louder than Words - Trillion-Parameter Sequential Transducers for Generative Recommendations.pdf
**Date analyzed:** 2026-08-17

## 1. Summary

Title: Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations. Authors: Jiaqi Zhai, Lucy Liao, Xing Liu, Yueming Wang, Rui Li, Xuan Cao, Leon Gao, Zhaojie Gong, Fangda Gu, Michael He, Yinghai Lu, Yu Shi (Meta AI). Published at ICML 2024 (also arXiv:2402.17152).

Abstract/contribution: proposes Generative Recommenders (GRs), reformulating ranking and retrieval as sequential transduction tasks over a unified sequence of heterogeneous features (unifying sparse/categorical and dense/numerical DLRM features into one time series of user actions). Introduces Hierarchical Sequential Transduction Units (HSTU), an attention variant designed for high-cardinality, non-stationary vocabularies, replacing softmax attention with pointwise aggregated attention. Also introduces training/serving techniques: generative (streaming) training that amortizes encoder cost across multiple emitted targets, Stochastic Length (SL) subsampling for sparsity, and M-FALCON, a cost-amortized inference algorithm for scoring many candidates.

Methodology: encoder-only stack of HSTU layers (pointwise projection, spatial aggregation via pointwise/normalized attention with relative attention bias, pointwise transformation via gating) replacing DLRM's feature-interaction and transformation modules. Ranking and retrieval are both cast as "sequential transduction tasks" over interleaved (item, action) tokens, using target-aware formulation via causal-masked cross-attention. Numerical/dense features are argued to become unnecessary given a sufficiently expressive sequential architecture with target-aware attention.

Datasets/baselines: public sequential-rec benchmarks (MovieLens-1M/20M, Amazon Books) against SASRec; industrial-scale proprietary datasets (100B examples, DLRM-equivalent) against production DLRM baselines (with DIN+DCN feature interactions), evaluated via Normalized Entropy (NE) for ranking and log perplexity/Hit Rate@K for retrieval.

Main results: HSTU outperforms SASRec by up to 65.8% NDCG on public benchmarks; is 5.3x–15.2x faster than FlashAttention-2 Transformers at 8192-length sequences; HSTU-based GRs at 1.5 trillion parameters improve online A/B test metrics by 12.4%; GR model quality scales as a power law with training compute across three orders of magnitude, up to GPT-3/LLaMA-2 scale.

## 2. Experiment Critique

Design: both offline (public + industrial-scale) and online (production A/B test) experiments are included. Offline industrial evaluation reports NE (not AUC) for ranking, following industry practice; retrieval reports log perplexity and Hit Rate@K (K=100,500). Public benchmark results follow prior work's full-shuffle, multi-epoch protocol, which the paper itself notes "differs significantly from industrial-scale settings" where full-shuffle/multi-epoch are not practical — a limitation acknowledged in-paper.

Statistical validity: no confidence intervals or significance tests are reported for offline metrics; industrial NE differences are asserted as meaningful using an internal heuristic ("a 0.001 reduction in NE is significant, leading to ~0.5% topline metric improvements"), not a formal statistical test.

Online experiments: reports a single online A/B result (12.4% improvement, deployed on multiple surfaces of an unnamed "large internet platform" — implicitly Meta) without confidence intervals, exposure duration, or randomization-unit detail.

Reproducibility: code is released (github.com/facebookresearch/generative-recommenders) for the architecture and public-dataset training; the industrial-scale datasets, production DLRM baseline configuration, and the 1.5-trillion-parameter deployed model are not public and cannot be independently reproduced.

## 3. Industry Contribution

Deployability: this is an industrial deployment paper (Meta), not just an academic proposal — HSTU-based GRs are stated to be deployed on multiple surfaces of a platform with billions of daily users. It directly targets ranking/retrieval engineering concerns: serving latency (M-FALCON reduces cross-attention cost from O((b_m+n)^2 d) to O((n+b_m)^2 d) via micro-batching, achieving up to 285x more model complexity within the same inference budget), activation memory (HSTU reduces linear layers from six to two and fuses layer norm/dropout/output MLP, cutting activation memory to enable >2x deeper networks vs. Transformers), and feature engineering (the paper explicitly proposes eliminating hand-engineered numerical/dense features in favor of a purely sequential, target-aware architecture).

Engineering cost: very high. This requires redesigning the entire feature pipeline (sequentializing categorical and compressing/removing numerical features), a custom fused attention kernel exploiting sequence sparsity, a new training paradigm (generative/streaming training that emits multiple targets per user sequence rather than one per impression), and custom inference batching (M-FALCON). The reported 1.5-trillion-parameter model represents three orders of magnitude more training compute than prior DLRM baselines.

## 4. Novelty vs. Prior Work

The paper's core novelty claim is treating "user actions as a new modality" and unifying the DLRM feature space (sparse + dense features) into a single sequential representation, then reformulating both ranking and retrieval as generative sequential transduction tasks rather than as separate feature-interaction/pooling problems. It positions itself against DLRM literature (Zhou et al. DIN, Wang et al. DCN, Mudigere et al. DLRM systems) and against prior sequential recommenders (Kang & McAuley SASRec, Hidasi et al. GRU4Rec) and Transformer efficiency work (Dao FlashAttention-2, Touvron LLaMA/Transformer++). It claims to be the first work to show pure sequential-transduction architectures significantly outperform DLRMs in large-scale industrial settings, and the first to show a compute scaling law (à la Kaplan et al.) holding for recommendation systems.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| MovieLens-1M / MovieLens-20M | Public academic benchmark | Yes | Full-shuffle, multi-epoch sequential-rec evaluation vs. SASRec |
| Amazon Books | Public academic benchmark | Yes | Same protocol as above |
| Industrial-scale datasets (~100B examples, DLRM-equivalent) | Proprietary, streaming | No | Used for one-pass streaming NE/log-perplexity evaluation and the deployed 1.5T-parameter model; not released |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations." Zhai, Liao, Liu, Wang, Li, Cao, Gao, Gong, Gu, He, Lu, Shi (Meta AI). ICML 2024. arXiv:2402.17152. |
| 2 | Source type | Industry paper (Meta AI), peer-reviewed at ICML. |
| 3 | Direction | D9. |
| 4 | Problem setting | Industrial-scale ranking and retrieval for recommendation platforms with billions of daily active users and billion-scale, non-stationary item/feature vocabularies; reformulates both tasks as sequential transduction over interleaved item/action tokens. |
| 5 | Objective and label definition | Next-token prediction over a sequentialized stream of (item, action) tokens — predicting the next action a user takes on the next content, and/or the next content itself for retrieval. Labels are the immediate next engagement action (e.g., like, skip, video completion+share) observed in the user's streaming interaction log; no explicit retention, revenue, or delayed-outcome horizon is defined. Training is done in a streaming, single-pass fashion (not full-shuffle/multi-epoch) in the industrial setting. Not specified in source: any explicit delay window or censoring treatment for long-horizon outcomes — the paper does not address them. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. |
| 7 | Model architecture | Encoder-only stack of Hierarchical Sequential Transduction Units (HSTU) — pointwise projection, pointwise (non-softmax) aggregated attention with relative positional/temporal bias, and gated pointwise transformation (SwiGLU-like) — applied to a single sequentialized stream merging categorical and (removed) numerical DLRM features; ranking uses target-aware causal-masked cross-attention, retrieval uses next-item distribution modeling. |
| 8 | Credit assignment | Not addressed — the model attaches a training/prediction signal to each emitted (item, action) token in the user's immediate interaction sequence (one impression → one predicted next action), not to any delayed or user-level outcome. There is no mechanism mapping a delayed or aggregate outcome back to a specific exposure. |
| 9 | Training data and counterfactual handling | Trained on logged user interaction sequences (implicit feedback from production traffic) in a streaming setting; no counterfactual correction, propensity weighting, or off-policy correction is described. Not specified in source: any exposure-selection bias handling. |
| 10 | Offline and online evaluation | Offline — NDCG@K/HR@K on public sequential-rec benchmarks (full-shuffle/multi-epoch protocol); Normalized Entropy (ranking) and log perplexity/Hit Rate@K (retrieval) on industrial one-pass streaming data. Online — a single production A/B test reporting aggregate topline metric improvement. |
| 11 | Reported gains | Up to 65.8% higher NDCG@200 vs. SASRec (2023) on the Amazon Books dataset (public benchmark); 5.3x–15.2x training/inference speedup vs. FlashAttention-2 Transformers at 8192-length sequences; 12.4% improvement in unspecified online production metrics in A/B testing on a large internet platform (implicitly Meta); GR performance scales as a power law with training compute up to GPT-3/LLaMA-2-scale compute (three orders of magnitude), whereas DLRM baselines plateau. |
| 12 | Applicability to a two-sided dating recommender | The unified sequential-feature architecture and target-aware attention could plausibly be reused as a backbone encoder for a dating recommender's short-term event prediction, but the paper's objective is pure next-action/engagement prediction with no retention, revenue, or reciprocity treatment. Nothing in the paper addresses two-sided matching, reciprocity, or congestion — it is a single-sided content feed (video/product) setting. |
| 13 | Unverified claims | The "12.4% improvement" online metric is not tied to a named metric (e.g., watch time, revenue) in the paper, nor is a confidence interval given — asserted without full disclosure. The claim that GR "paves the way for the first foundation models in recommendations" is a forward-looking, unverified claim about future impact rather than a demonstrated result. |

## Project Relevance

**Low project relevance.** The paper's training objective is immediate next-action/engagement prediction, not retention, revenue, or LTV; it does not address delayed labels, credit assignment for delayed outcomes, prediction-vs-incrementality, or two-sided/reciprocal-market dynamics — no long-term objective is present anywhere in the paper. Its only relevant contribution is architectural (Q4-adjacent, at most): a demonstration that engagement-style short-term event heads can be unified into a single generative sequence model rather than a cascade of separate DLRM stages — relevant only as a possible backbone if the team later wants to unify short-term event prediction, not as evidence for unifying retention/revenue objectives. It is a strong reference for architecture/scaling, not for the survey's causal/LTV questions (Q1–Q3, Q5–Q8 are all unaddressed).

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2025_arXiv_MTGR_Industrial-Scale-Generative-Recommendation-Meituan.md](./2025_arXiv_MTGR_Industrial-Scale-Generative-Recommendation-Meituan.md) | Related Work / Experiments | Names this paper's method (`HSTU`) |

_1 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `HSTU` across all 133 cards._

## Meta Information

- Authors: Jiaqi Zhai, Lucy Liao, Xing Liu, Yueming Wang, Rui Li, Xuan Cao, Leon Gao, Zhaojie Gong, Fangda Gu, Michael He, Yinghai Lu, Yu Shi
- Affiliations: Meta AI
- Venue: ICML 2024 (PMLR 235); also arXiv:2402.17152
- Year: 2024
- Relevance: Low (D9, architecture-only; no long-term objective)
- Priority: 2
- nlm:1b098b2b
