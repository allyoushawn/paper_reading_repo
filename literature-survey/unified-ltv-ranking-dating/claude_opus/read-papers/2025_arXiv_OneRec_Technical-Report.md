# Paper Analysis: OneRec Technical Report

**Source:** /Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/LLM_Ranking/2025 (Kuaishou) (Arxiv) [OneRec] OneRec Technical Report.pdf
**Date analyzed:** 2026-08-17

## 1. Summary

Title: OneRec Technical Report. Authors: OneRec Team (Kuaishou). arXiv:2506.13695 (16 Jun 2025).

Abstract/contribution: a detailed technical report on OneRec's second-generation production system, describing a full end-to-end generative recommendation architecture, its infrastructure, training framework, and reinforcement-learning-based post-training. Reports 10x higher computational FLOPs than the prior recommendation model, evidence of recommendation-system scaling laws, 23.7%/28.8% Model FLOPs Utilization (MFU) during training/inference (5.2x/2.6x over the prior ranking model), OPEX reduced to 10.6% of the traditional cascaded pipeline's cost, and deployment handling ~25% of total QPS on Kuaishou/Kuaishou Lite, improving App Stay Time by 0.54%/1.24% with 7-day Lifetime (LT7) also reported as an improved online metric.

Methodology: an encoder-decoder generative architecture. The tokenizer builds hierarchical semantic IDs via RQ-Kmeans on collaborative-aware multimodal item representations. The encoder ingests four multi-scale user-behavior pathways (static user features, short-term behavior [20 items], positive-feedback behavior [256 items], and a lifelong/ultra-long behavior pathway [up to 100,000 items] compressed hierarchically via K-means + QFormer). The decoder autoregressively generates target-item semantic IDs point-wise (not session-wise, unlike the companion OneRec paper), using MoE feed-forward layers with loss-free load balancing. Training objective is next-token-prediction cross-entropy (L_NTP). Post-training combines Reject Sampling Fine-Tuning (RSFT, filtering out the bottom 50% of exposure sessions by play duration) with reinforcement learning via a custom PPO/GRPO variant, Early Clipped GRPO (ECPO), optimized against a Reward System with three components: (1) a learned Preference Score (P-Score) fusing multiple engagement-objective towers (click, like/ltr, follow/wtr, comment/cmtr, long-view/lvtr) via a SIM-based multi-tower model into one personalized reward, replacing manual fixed-weight fusion; (2) a format reward penalizing illegal (non-mappable) generated semantic-ID sequences; (3) a "Specific Industrial Reward" that down-weights viral/low-quality-content-farm items to manage ecosystem/business constraints.

Datasets/baselines: proprietary Kuaishou production data (18B samples/day, ~300B tokens total pre-training exposure for the largest model); no external academic baselines are used — comparisons are against the company's own prior traditional cascaded recommendation system and internal ablations across model scale (0.015B–2.633B parameters), codebook size, and RL configuration.

Main results: RL (ECPO with P-Score reward) improves online App Stay Time and Watch Time relative to the model without RL across both Kuaishou and Kuaishou Lite; deployed online A/B test (Table 12) shows OneRec-with-RM-Selection achieving +0.54%/+1.24% App Stay Time and +1.98%/+3.28% Watch Time on Kuaishou/Kuaishou Lite respectively, versus the full traditional cascade; a separate Local Life Service business deployment shows 21.01% GMV growth, 17.89% order-volume increase, 18.58% buyer-number increase, and 23.02% new-buyer-acquisition increase, now at 100% QPS for that scenario.

## 2. Experiment Critique

Design: extensive ablations (parameter scaling, feature scaling, codebook scaling, inference Pass@K scaling, RL search-space/strategy/reference-model choices) use internal reward-model-based metrics (xtr metrics: lvtr/vtr/ltr/wtr/cmtr, and P-Score) rather than held-out ground-truth outcome metrics for most ablations — a degree of circularity since these xtr signals come from "a pre-trained ranking model" used both to construct the reward and to evaluate offline.

Statistical validity: reports comparative percentage improvements over "sufficiently long observation windows" for online results and states experiments are "conducted within the same periods" for comparability, but no confidence intervals, p-values, or sample sizes are given anywhere in the text.

Online experiments: the most rigorous part of the paper — a real production 5%-traffic A/B test over one week on two major surfaces (Kuaishou main feed, Kuaishou Lite feed, 400M DAU), explicitly naming App Stay Time and LT7 as primary metrics, and explicitly stating the thresholds Kuaishou considers "statistically significant" (0.1% App Stay Time, 0.01% LT7) — unusually transparent about what counts as a meaningful online effect for an industry paper.

Reproducibility: fully proprietary (Kuaishou infrastructure, data, and reward model); the paper is candid about limitations, explicitly naming "Inference Stage Scaling" (scaling during inference is "not yet apparent") as an open limitation in its Conclusion.

## 3. Industry Contribution

Deployability: this is the fullest infrastructure-level industrial contribution in the batch — detailed compute (90 servers × 8 GPUs, 400Gbps NVLink/RDMA), training acceleration (GPU-based embedding parameter servers, ZERO1, BFloat16, compilation optimization), and inference infrastructure (NVIDIA L20, TensorRT, custom fused cross-attention/MoE kernels, 200Gb RDMA, batching + MPS) are all documented, alongside real production deployment at ~25% of Kuaishou/Kuaishou Lite QPS and 100% QPS for a Local Life Service scenario. Latency and online serving are addressed concretely (28.8% inference MFU, 5x throughput improvement via batching).

Problems solved: replaces a fragmented, "over 50% of serving resources spent on communication/storage rather than computation" cascaded pipeline with one end-to-end model; explicitly frames "objective collision" (hundreds of competing goals at Kuaishou) as a core problem the reward-system design (P-Score + format reward + industrial reward) is meant to solve by moving objective-weighting into a single learned/RL-optimized layer instead of manual patching across pipeline stages.

Engineering cost: very high — new tokenizer (RQ-Kmeans + collaborative-aware multimodal alignment), a four-pathway multi-scale user encoder including a novel ultra-long (100K-event) lifelong-behavior compression pipeline, MoE decoder, a three-part reward system, a custom RL algorithm (ECPO) with format-reward correction for a "squeezing effect" failure mode the authors discover and diagnose, and an external inference-service loop for on-policy RL sample generation synced every 1000 training steps.

## 4. Novelty vs. Prior Work

Extends the companion OneRec paper (Deng et al., arXiv:2502.18965) into a full production technical report with substantially more infrastructure, scaling-law, and RL detail; explicitly contrasts itself with LLM/VLM scaling-law and RL literature (Kaplan et al. scaling laws; Ouyang et al., Rafailov et al. RLHF/DPO for LLMs; Shao et al. GRPO) which it argues has not previously translated well into cascaded recommendation architectures due to "fundamental architectural barriers," and proposes ECPO as its own modification of GRPO (Liu et al., 2024) to address a training-instability/"squeezing effect" problem specific to legality-constrained generative recommendation (citing Ren and Sutherland, 2024, on squeezing effects). It also contrasts its RQ-Kmeans tokenizer against RQ-VAE (used in TIGER-style prior work), reporting improved reconstruction loss and codebook utilization.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| Kuaishou production interaction logs (~18B samples/day) | Proprietary, industrial-scale | No | Pre-training and RSFT data; not released |
| Kuaishou / Kuaishou Lite main feed, 5% traffic, 400M DAU | Proprietary, online | No | Online A/B test (App Stay Time, LT7, engagement metrics) |
| Local Life Service business scenario | Proprietary, online | No | Secondary online deployment (GMV, order volume, buyer metrics) |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "OneRec Technical Report." OneRec Team (Kuaishou). arXiv:2506.13695, 2025. |
| 2 | Source type | Industry paper (Kuaishou), arXiv preprint/technical report. |
| 3 | Direction | D9. |
| 4 | Problem setting | End-to-end generative recommendation replacing the full retrieval/pre-ranking/ranking cascade in a large-scale short-video platform, addressing "fragmented compute," "objective collision" across hundreds of competing business goals, and the gap between recommendation-system and LLM-community engineering practice. |
| 5 | Objective and label definition | Pre-training objective is next-token-prediction cross-entropy on target-item semantic IDs — an immediate next-item prediction task with no explicit horizon. Post-training reward (P-Score) is a learned fusion of multiple immediate engagement-objective towers — click, like (ltr), follow (wtr), comment (cmtr), and long-view (lvtr) through-rates — each a binary same-session/same-exposure engagement label, trained via BCE. A "Specific Industrial Reward" additionally down-weights viral/low-quality content. Online evaluation additionally tracks App Stay Time and 7-day Lifetime (LT7) — LT7 is the one place in this four-paper batch where a multi-day retention-like metric appears — but LT7 is used exclusively as an online A/B **evaluation** metric, never as a training label, reward-model target, or optimization objective. No delay handling, censoring treatment, or explicit label horizon for LT7 is specified anywhere in the paper; it is reported as a downstream observed outcome of a model trained entirely on same-session engagement signals. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. |
| 7 | Model architecture | Encoder-decoder Transformer with RQ-Kmeans hierarchical semantic-ID tokenization (collaborative-aware multimodal alignment); encoder fuses four multi-scale user-behavior pathways (static/short-term/positive-feedback/lifelong, the last compressed via hierarchical K-means + QFormer for sequences up to 100,000 events); MoE decoder (up to 2.633B parameters, 24 experts) trained via next-token prediction, then post-trained with combined RSFT + reinforcement learning (Early Clipped GRPO) against a three-part reward system (P-Score preference reward, format/legality reward, industrial/business-alignment reward). |
| 8 | Credit assignment | The RL reward (P-Score) is computed per generated item/video (via a target-aware SIM-style preference model) and used as a per-item advantage in ECPO — i.e., credit is assigned at the single generated-item level within one user request, not to a delayed or multi-day outcome. The online-reported LT7 metric is a user-level, delayed (7-day) aggregate, but the paper does not describe any mechanism attributing that delayed outcome back to specific items or exposures — it is only observed in aggregate at the A/B-test level, not used as a training/credit signal. |
| 9 | Training data and counterfactual handling | Trained on logged production interaction streams (pre-training) and on RSFT-filtered high-play-duration sessions; RL samples are generated on-policy via an external inference service (1% of users, N=512 items) with rewards from the reward model, synced back via message queue every 1000 steps. No counterfactual/propensity correction is described; training data reflects exposure from the prior production system. |
| 10 | Offline and online evaluation | Offline — cross-entropy/NTP loss curves, P-Score, and xtr-metric (lvtr/vtr/ltr/wtr/cmtr) comparisons across model scale, feature configuration, codebook size, and RL ablations (search space, search strategy, reference model). Online — a 5%-traffic, one-week A/B test on Kuaishou main feed and Kuaishou Lite (400M DAU) tracking App Stay Time and LT7, plus a separate 100%-QPS deployment for the Local Life Service business line tracking GMV/order/buyer metrics. |
| 11 | Reported gains | Online A/B test vs. traditional cascade (Table 12) — OneRec with RM Selection: +0.54% App Stay Time and +1.98% Watch Time on Kuaishou; +1.24% App Stay Time and +3.28% Watch Time on Kuaishou Lite; reward-model selection also improved LT7 (+0.05% Kuaishou, +0.08% Kuaishou Lite), both above Kuaishou's stated 0.01% significance threshold for LT7. Local Life Service: +21.01% GMV, +17.89% order volume, +18.58% buyer numbers, +23.02% new-buyer acquisition. Infrastructure: 23.7%/28.8% training/inference MFU (5.2x/2.6x over prior ranking model); OPEX at 10.6% of the traditional pipeline. |
| 12 | Applicability to a two-sided dating recommender | The four-pathway multi-scale encoder (especially the lifelong/ultra-long-sequence compression) and the reward-system pattern (learned preference fusion + format/legality reward + business-constraint reward) are architecturally reusable ideas for combining multiple objective heads without manual weight tuning. Nothing in the paper addresses reciprocity, congestion, or two-sided fairness; and although LT7 shows the platform does track a retention-like metric online, it is not fed back into training, so the paper offers no evidence on how to make a delayed outcome the training objective itself. |
| 13 | Unverified claims | The claim that RL "previously had shown limited impact in traditional architectures" but "demonstrate[s] substantial potential" here is asserted rather than benchmarked against a specific prior RL-in-cascade result. The statement that OneRec "remarkably matched the performance of the entire complex recommendation system" using "a pure generative model" is a strong claim not accompanied by a formal equivalence test — it rests on the same internal significance thresholds described above. |

## Project Relevance

**Low project relevance for making retention/revenue the training objective (Q1, Q3)**, despite reporting LT7 (7-day Lifetime) as an online metric — the closest any paper in this batch comes to a multi-day retention signal. This paper is directly useful as a *negative/gap finding*: LT7 is measured, not optimized. The trained objective (P-Score reward, RL) remains entirely same-session engagement (click/like/follow/comment/long-view), even at a company sophisticated enough to track and report a 7-day retention metric online. This is a positive finding for Q4/Q8: a documented industry migration from cascade to unified generative model, and a documented pattern for replacing manual multi-objective fusion weights with a learned reward system (P-Score) plus auxiliary format/business rewards. Q2, Q5, Q6, Q7 are not addressed.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2025_arXiv_MTGR_Industrial-Scale-Generative-Recommendation-Meituan.md](./2025_arXiv_MTGR_Industrial-Scale-Generative-Recommendation-Meituan.md) | Related Work / Experiments | Names this paper's method (`OneRec`) |
| [2025_arXiv_OneRec-V2_Lazy-Decoder-User-Feedback-Alignment.md](./2025_arXiv_OneRec-V2_Lazy-Decoder-User-Feedback-Alignment.md) | Related Work / Experiments | Names this paper's method (`OneRec`) |
| [2025_arXiv_OneRec_Unifying-Retrieve-Rank-Preference-Alignment.md](./2025_arXiv_OneRec_Unifying-Retrieve-Rank-Preference-Alignment.md) | Related Work / Experiments | Names this paper's method (`OneRec`) |
| [2026_RecSys_GenPage_End-to-End-Generative-Homepage-Construction.md](./2026_RecSys_GenPage_End-to-End-Generative-Homepage-Construction.md) | Related Work / Experiments | Names this paper's method (`OneRec`) |
| [2026_arXiv_GenRec_LLM-Backed-Recommendation-Ranker.md](./2026_arXiv_GenRec_LLM-Backed-Recommendation-Ranker.md) | Related Work / Experiments | Names this paper's method (`OneRec`) |
| [2026_arXiv_NA_Tencent-Advertising-Algorithm-Challenge-Generative-Recommendation.md](./2026_arXiv_NA_Tencent-Advertising-Algorithm-Challenge-Generative-Recommendation.md) | Related Work / Experiments | Names this paper's method (`OneRec`) |

_6 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `OneRec` across all 133 cards._

## Meta Information

- Authors: OneRec Team
- Affiliations: Kuaishou
- Venue: arXiv preprint (arXiv:2506.13695)
- Year: 2025
- Relevance: Low for retention/revenue-as-objective (Q1/Q3), but a valuable negative finding on that point; moderate for cascade-to-unified migration and reward-fusion pattern (Q4/Q8)
- Priority: 2
- nlm:4df9b0a4
