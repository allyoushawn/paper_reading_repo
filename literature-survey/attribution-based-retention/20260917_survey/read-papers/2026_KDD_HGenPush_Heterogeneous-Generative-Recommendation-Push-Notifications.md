# HGenPush: A Heterogeneous Generative Recommendation Architecture for Industrial Push Notification Systems

**Source:** https://arxiv.org/pdf/2607.03362.pdf | **NLM source id:** 0fea3f6f-1070-40ed-8ecc-0d28bd996c7e | **Year / venue:** KDD 2026 (v.2) | **Authors / affiliation:** Xiao Liang, Jiali Feng, Xin Feng, Yiqing Wang, Baolin Ye, Siyao Feng, Zhihui Deng, Cunyi Zhang, Huajin Sun, Xuanping Li, Kaiqiao Zhan, Yanan Niu, Kun Gai (Kuaishou Technology, Beijing) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Industrial generative recommendation has two bottlenecks: it generates only homogeneous item types (can't jointly recommend, e.g., videos and trusted authors), and autoregressive semantic-ID decoding is too slow for strict push-notification QPS/latency budgets. HGenPush is a decoder-only, dual-branch architecture: a Hybrid User Behavior Understanding module fuses long/short-term feed behavior with push click/send sequences; a Heterogeneous Generative Recommendation module uses Chained Multi-Token Prediction (Chained-MTP) — anchoring generation to a global user-interest vector and accumulating preceding semantic-ID embeddings instead of full autoregressive decoding — to jointly generate video and (mixed video+author) semantic IDs; and a User Consumption Preference Alignment (UCPA) module trained via RLVR with a new Group Sequence Importance Sampling Policy Optimization (GSISPO) algorithm that optimizes post-click session behavior rather than raw clicks, to eliminate clickbait.

Unit of credit: per push-notification candidate / generated semantic-ID tuple (video or mixed author+video). Outcome optimized: short-term push CTR via supervised multi-token cross-entropy, plus long-term engagement/retention (DAU, app usage duration, post-click consumption quality) via the RL reward. Bias handling: since clicks reflect curiosity, not content value, UCPA groups videos consumed in a post-click session and computes a normalized relative group advantage A_g=(r_g−mean(R))/std(R), with reward shaping (+2 valid play/profile-entry/comment-stay, +1 like/follow/share/comment, −2 short play, −5 dislike, −10 report) — this is within-group normalization against the user's own session, not an explicit counterfactual/selection-bias correction across users. GSISPO's clipped importance-sampling weights preserve gradient signal from niche high-value behavior while preventing semantic fragmentation.

## 2. Evidence
- **Dataset:** Kuaishou push-notification system, continuous streaming logs, 400M+ DAU.
- **Offline HitRate@100:** video branch HGenPush 0.3915 vs. TIGER 0.3802 vs. SASRec 0.3093; author branch HGenPush 0.4848 vs. TIGER 0.4677 vs. SASRec 0.3495.
- **Inference throughput:** Chained-MTP 1.70k QPS/device vs. DeepSeek-MTP 1.27k QPS (+33.86%) at comparable HitRate@100 (0.3915 vs 0.3954).
- **Scaling:** HitRate@100 0.3432 (0.016B) → 0.3915 (0.064B) → 0.4043 (0.170B MoE).
- **Live A/B on Kuaishou (400M+ DAU):** full HGenPush: +0.181% DAU (p=0.04), +1.577% CTR (p=0.11), +0.148% app usage duration (p=0.75). UCPA module alone: +0.43% push play duration, +0.37% valid play rate, +0.90% complete play rate, +0.75% like rate, +7.57% forward rate.
- Baselines: SASRec, TIGER, Parallel-MTP, DeepSeek-MTP, Encoder-Decoder, direct sample reweighting.

## 3. Limitations
- Directly reweighting training samples by watch time collapsed offline HitRate@100 from 0.3964 to 0.3394 — naive engagement-reweighting damages the base generative model (motivates UCPA's group-relative approach instead).
- Diminishing returns from MoE scaling (0.064B→0.170B: +3.27% vs. +14.07% for 0.016B→0.064B).
- Generated candidates still depend on downstream multi-stage ranking models for final presentation order — not a fully end-to-end replacement.

## 4. Prior works named
- Rajput et al. 2023, TIGER — *Recommender systems with generative retrieval* (RQ-VAE semantic ID generation)
- Deng et al. 2025, OneRec — *Unifying retrieve and rank with generative recommender and iterative preference alignment* (video semantic ID quantization, preference alignment)
- Zheng et al. 2025, GSPO — *Group sequence policy optimization* (sequence-level policy optimization basis for GSISPO)
- Chen et al. 2025, CISPO/MiniMax-M1 — clipped importance-sampling weight design
- Kang & McAuley 2018, SASRec — *Self-attentive sequential recommendation* (baseline)

## 5. Project Relevance
- **Answers:** Q2 (background)
- **Attributes retention to individual interactions?** no — generates and ranks push-notification candidates using post-click session reward signals; does not attribute retention/engagement/active-days to individual historical interactions (swipes/likes/matches) via fractional credit.
- **Transferable components:** post-exposure session reward shaping (rewarding deep post-swipe/post-match engagement like conversation continuation, penalizing quick bounces/unmatches) as an RLVR-style signal; group-relative advantage normalization to strip out user-level baseline activity variance when comparing candidate profiles; hybrid long/short-term + channel-specific behavior fusion for building a user-interest representation.
- **Required changes:** shift from generating/ranking candidate lists to per-touch sequence attribution; replace video/author semantic IDs with heterogeneous dating-funnel event types (swipe, like, match, message) with event and time-gap embeddings; re-anchor the reward from within-session consumption quality to a daily-recurring rolling N7 active-retention indicator.
- **On last-touch:** does not name last-touch/last-click explicitly, but shows relying on immediate clicks alone (a myopic/proximate signal, structurally similar to last-touch) produces clickbait-like recommendations, while incorporating post-click/post-exposure session behavior via RL improves long-term engagement and drives the observed DAU gain.
- **Transfer rating:** background — an industrial generative-retrieval and post-click preference-alignment architecture for push notifications, not an attribution or retention-credit model; its reward-shaping and group-normalization ideas are conceptually adjacent but not a direct building block for per-swipe fractional credit.
