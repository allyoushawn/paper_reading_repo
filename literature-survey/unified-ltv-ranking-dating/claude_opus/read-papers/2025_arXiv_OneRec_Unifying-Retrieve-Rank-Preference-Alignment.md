# Paper Analysis: OneRec: Unifying Retrieve and Rank with Generative Recommender and Preference Alignment

**Source:** /Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/02_Matching/LLM_Matching/2025  (Kuaishou) (Arxiv)[OneRec] OneRec - Unifying Retrieve and Rank with Generative Recommender and Preference Alignment.pdf
**Date analyzed:** 2026-08-17

## 1. Summary

Title: OneRec: Unifying Retrieve and Rank with Generative Recommender and Preference Alignment. Authors: Jiaxin Deng, Shiyao Wang, Kuo Cai, Lejian Ren, Qigen Hu, Weifeng Ding, Qiang Luo, Guorui Zhou (Kuaishou Inc.). arXiv:2502.18965 (26 Feb 2025).

Abstract/contribution: proposes OneRec, replacing the traditional retrieve-and-rank cascade with a single end-to-end generative model that directly generates a session-wise list of candidate videos in an autoregressive manner, claimed as the first end-to-end generative model to significantly surpass complex cascaded recommenders in a real production system. Contributions: (1) an encoder-decoder architecture using sparse Mixture-of-Experts (MoE) to scale capacity without proportionally increasing FLOPs; (2) session-wise generation (generating a full session/list rather than point-by-point next-item prediction) to better capture coherence/diversity without hand-crafted list-assembly rules; (3) an Iterative Preference Alignment (IPA) module combining a trained reward model with Direct Preference Optimization (DPO), using self-hard-negative sampling from beam search (rather than random sampling) to build preference pairs.

Methodology: items are tokenized into hierarchical semantic IDs via a balanced K-means residual quantization of multi-modal item embeddings. The model is a T5-style encoder-decoder: encoder processes the user's historical behavior sequence (as semantic IDs), decoder autoregressively generates the target session's semantic IDs (5–10 videos per session) via next-token-prediction cross-entropy loss (L_NTP), with decoder FFN layers replaced by MoE. After seed-model training on session-wise list data, an Iterative Preference Alignment stage trains a personalized session-level reward model (RM) and applies DPO iteratively: at each iteration, the current model generates N candidate sessions via beam search for each user, the RM scores them, and the highest/lowest-reward sessions become the DPO winner/loser pair; the model is retrained on L_NTP + λ·L_DPO and the process repeats for T epochs.

Datasets/baselines: proprietary Kuaishou production logs (large-scale industry dataset); baselines are SASRec, BERT4Rec, FDSA (point-wise discriminative), and TIGER (point-wise generative), plus DPO variants (IPO, cDPO, rDPO, CPO, simPO, S-DPO) as preference-alignment ablations.

Main results: offline, OneRec-1B+IPA achieves the best watching-time metrics (swt mean 0.1025, vtr mean 0.6141) and interaction metrics (ltr mean 0.1203) among all compared methods, outperforming TIGER-1B, other DPO variants, and the non-aligned OneRec-1B baseline. Online, deployed on Kuaishou's main scene with hundreds of millions of DAU, OneRec achieved a 1.6% increase in watch-time in an online A/B test — described as substantial in a mature, heavily-optimized system.

## 2. Experiment Critique

Design: offline comparisons use held-out industry logs, evaluating multiple metrics (session watch-time, view-through rate, follow-through rate, like-through rate) via mean/max over test sessions, scored by the pre-trained reward model rather than ground-truth outcome logs — i.e., the offline "evaluation" is itself model-based (RM-scored), which risks circularity since the RM is also the DPO training signal.

Statistical validity: metrics are reported with ± standard-deviation ranges across repeated runs (e.g., "0.1025±0.009"), more rigorous than many industry papers, but no significance test is reported, and the number of runs averaged is not stated.

Online experiments: a single aggregate online A/B result (1.6% watch-time increase) is reported without confidence interval, traffic percentage, or test duration in the paper; deployment scope ("main scene of Kuaishou") is described qualitatively.

Reproducibility: dataset and reward model are proprietary Kuaishou production data; not released. Hyperparameters (learning rate, GPU type A800, DPO sample ratio 1%, N=128 responses per user, codebook size K=8192, MoE with 24 experts/2 active) are disclosed in detail, aiding conceptual reproducibility even though data is not shared.

## 3. Industry Contribution

Deployability: this is a deployed industrial system (Kuaishou's main video-recommendation scene, hundreds of millions of DAU) — a genuine production replacement of the cascade, not a lab prototype. It directly addresses ranking-pipeline engineering: replacing a three-stage retrieve/pre-rank/rank cascade with one autoregressive generation call, avoiding the "effectiveness of each isolated stage upper-bounding the next" problem it identifies in cascades. Latency/serving: uses beam search (beam size 128) with KV-cache and float16 quantization for inference; MoE keeps only 13% of parameters active during inference. Feature engineering: replaces the traditional multi-tower ranking feature set with a single sequentialized user-behavior-history input plus target-aware attention in the reward model.

Problems solved: it removes the retrieve-then-rank division of labor entirely for its production traffic slice, and it introduces a mechanism (reward model + DPO) for the generative model to be optimized beyond simple imitation of past exposed-item distributions, which it argues point-wise generative methods (e.g., TIGER) cannot do as effectively.

Engineering cost: substantial — requires building a session-wise-list-quality reward model, an iterative DPO training loop with self-hard-negative mining via beam search, a hierarchical semantic-ID tokenizer, and MoE infrastructure; the paper states this is deployed at production scale, so the cost was evidently justified for Kuaishou.

## 4. Novelty vs. Prior Work

The paper positions itself as the first end-to-end generative model that "significantly surpasses" a well-designed cascaded system in a real production deployment (rather than only matching or slightly beating academic baselines), differentiating it from prior generative-retrieval work (GENRE, DSI, TIGER — cited as retrieval-stage-only generative selectors) and from RLHF/DPO literature developed for LLMs (Rafailov et al. DPO; also IPO, cDPO, rDPO, CPO, simPO variants), which it adapts to the sparse, non-explicit preference-annotation setting of recommendation via a learned reward model and self-hard-negative mining, distinguishing it from concurrent work S-DPO (multi-negative preference for LM-based recommenders).

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| Kuaishou production interaction logs | Proprietary, industrial-scale | No | Used for session-training and IPA/DPO; not released |
| Kuaishou main-scene production traffic | Proprietary, online | No | Used for the online A/B test (1.6% watch-time gain) |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "OneRec: Unifying Retrieve and Rank with Generative Recommender and Preference Alignment." Deng, Wang, Cai, Ren, Hu, Ding, Luo, Zhou (Kuaishou Inc.). arXiv:2502.18965, 2025. |
| 2 | Source type | Industry paper (Kuaishou), arXiv preprint. |
| 3 | Direction | D9. |
| 4 | Problem setting | Single-stage generative recommendation replacing the traditional retrieve-and-rank cascade in a large-scale short-video platform; generates a full session (list) of recommended videos autoregressively instead of scoring candidates from a fixed pool. |
| 5 | Objective and label definition | Two-stage objective. (a) Seed-model training: next-token-prediction cross-entropy over semantic IDs of "high-value sessions" — sessions defined by hand-set heuristic thresholds (≥5 videos actually watched, total watch duration exceeding a threshold, or presence of like/collect/share interaction) — a same-session, immediate-horizon label, not a delayed outcome. (b) Preference alignment: a session-level reward model trained via binary cross-entropy on multi-target labels — session watch-time (swt), view-through rate (vtr), follow-through rate (wtr), and like-through rate (ltr) — all measured within the same recommendation session/request, i.e., an immediate-horizon signal. No delay window, censoring, or long-horizon (multi-day) outcome is defined anywhere in the paper. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. |
| 7 | Model architecture | T5-style Transformer encoder-decoder over hierarchical semantic IDs (balanced K-means residual quantization of multi-modal item embeddings); decoder FFN layers replaced with sparse MoE; trained first via next-token-prediction (session-wise list generation) then refined via Iterative Preference Alignment combining a personalized session-level reward model with DPO on self-hard-negative-mined preference pairs (best beam-search response vs. worst beam-search response, scored by RM). |
| 8 | Credit assignment | A user-level session outcome (the reward model's predicted session watch-time/view/follow/like probabilities) is assigned to the entire generated session (a list of 5–10 items) as a single reward signal — i.e., credit is assigned at the session/slate level, not decomposed to individual items within the session, and not connected to any outcome beyond the immediate session/request. |
| 9 | Training data and counterfactual handling | Trained on logged (observational) high-value session data from production traffic; reward model is trained on logged multi-target engagement labels (swt/vtr/wtr/ltr) from the same logs. No counterfactual correction, propensity weighting, or off-policy correction is described — training data reflects whatever the prior cascade system exposed to users. |
| 10 | Offline and online evaluation | Offline — reward-model-scored comparison across swt/vtr/wtr/ltr against point-wise discriminative (SASRec, BERT4Rec, FDSA), point-wise generative (TIGER), and other DPO-variant baselines. Online — an A/B test on Kuaishou's main scene reporting an aggregate watch-time improvement. |
| 11 | Reported gains | OneRec-1B+IPA vs. TIGER-1B — 1.78% higher maximum session watch-time (swt) and 3.36% higher maximum like-through-rate (ltr) on Kuaishou production offline evaluation data; OneRec-1B+IPA vs. non-aligned OneRec-1B — 4.04% higher maximum swt and 5.43% higher maximum ltr with only 1% DPO sample ratio; online A/B test on Kuaishou's main scene — 1.6% increase in watch-time. |
| 12 | Applicability to a two-sided dating recommender | The session-wise generative architecture and reward-model-based preference alignment are architecturally transferable, but the reward model here is built entirely from same-session immediate engagement signals (watch-time, view/follow/like probability) with no retention or revenue horizon. Nothing in the paper addresses reciprocity, congestion, or a two-sided market — it is a single-sided content (short video) feed with no requirement for mutual consent between two users. |
| 13 | Unverified claims | "to the best of our knowledge, this is the first end-to-end generative model that significantly surpasses current complex and well-designed recommender systems in real-world scenarios" is a first-to-claim assertion not independently verifiable from the paper alone. The 1.6% online watch-time gain is called "a substantial improvement" without disclosing traffic allocation, test duration, or statistical significance. |

## Project Relevance

**Low project relevance** for the survey's central questions (Q1, Q3, Q5): the preference-alignment/reward-model stage — the part of the paper most likely to resemble "moving beyond a CTR-like proxy" — is itself trained on immediate engagement signals (session watch-time, view/follow/like probability), not retention or revenue, so it does not answer Q1 or Q3. It is more relevant to Q4/Q8 as an example of an industry migration path from cascade to a single unified model (directly on-topic for Q8's staged-migration question) and as an example of combining multiple short-term event heads via a learned reward model rather than fixed fusion weights (Q4-adjacent), though the fused signal is still short-horizon. The crux finding for this paper: OneRec's preference alignment targets immediate session engagement, not a longer-horizon outcome.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2025_arXiv_MTGR_Industrial-Scale-Generative-Recommendation-Meituan.md](./2025_arXiv_MTGR_Industrial-Scale-Generative-Recommendation-Meituan.md) | Related Work / Experiments | Names this paper's method (`OneRec`) |
| [2025_arXiv_OneRec-V2_Lazy-Decoder-User-Feedback-Alignment.md](./2025_arXiv_OneRec-V2_Lazy-Decoder-User-Feedback-Alignment.md) | Related Work / Experiments | Names this paper's method (`OneRec`) |
| [2025_arXiv_OneRec_Technical-Report.md](./2025_arXiv_OneRec_Technical-Report.md) | Related Work / Experiments | Names this paper's method (`OneRec`) |
| [2026_RecSys_GenPage_End-to-End-Generative-Homepage-Construction.md](./2026_RecSys_GenPage_End-to-End-Generative-Homepage-Construction.md) | Related Work / Experiments | Names this paper's method (`OneRec`) |
| [2026_arXiv_GenRec_LLM-Backed-Recommendation-Ranker.md](./2026_arXiv_GenRec_LLM-Backed-Recommendation-Ranker.md) | Related Work / Experiments | Names this paper's method (`OneRec`) |
| [2026_arXiv_NA_Tencent-Advertising-Algorithm-Challenge-Generative-Recommendation.md](./2026_arXiv_NA_Tencent-Advertising-Algorithm-Challenge-Generative-Recommendation.md) | Related Work / Experiments | Names this paper's method (`OneRec`) |

_6 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `OneRec` across all 133 cards._

## Meta Information

- Authors: Jiaxin Deng, Shiyao Wang, Kuo Cai, Lejian Ren, Qigen Hu, Weifeng Ding, Qiang Luo, Guorui Zhou
- Affiliations: Kuaishou Inc.
- Venue: arXiv preprint (arXiv:2502.18965)
- Year: 2025
- Relevance: Low for retention/revenue objective (Q1/Q3); moderate for migration-path/fusion architecture (Q4/Q8)
- Priority: 2
- nlm:3e16b474
