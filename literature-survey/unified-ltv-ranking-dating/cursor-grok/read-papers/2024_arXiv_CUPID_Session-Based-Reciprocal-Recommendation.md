# Paper Analysis: CUPID: A Real-Time Session-Based Reciprocal Recommendation System for a One-on-One Social Discovery Platform

**Source:** https://arxiv.org/pdf/2410.18087.pdf  
**Date analyzed:** 2026-08-16  
**Workplace:** cursor-grok

## Survey Card

- **title:** CUPID: A Real-Time Session-Based Reciprocal Recommendation System for a One-on-One Social Discovery Platform
- **authors or company:** Beomsu Kim, Sangbum Kim, Minchan Kim, Joonyoung Yi, Sungjoo Ha, Suhyun Lee, Youngsoo Lee, Gihoon Yeom, Buru Chang, Gihun Lee (Hyperconnect; Sogang University)
- **venue:** arXiv (cs.IR)
- **year:** 2024
- **URL:** https://arxiv.org/pdf/2410.18087.pdf
- **source type:** industry paper
- **direction:** D8
- **problem setting:** Real-time one-on-one social discovery (Azar video chat) where users enter a dynamic matching pool; reciprocal pairing must satisfy both parties; preferences evolve within a session; strict latency constraints prohibit synchronous session modeling on each match request.
- **objective and label definition:** Maximize overall user satisfaction proxied by total chat duration across pairs; label y_ij = observed chat duration per match history m_i,k = (u_i, u_j, y_ij); training loss is MSE on log-scaled chat durations; no retention/LTV horizon or delayed-feedback censoring in source.
- **prediction or incrementality:** Predicts expected chat duration ŷ_ij = f(u_i, u_j) for all pairs in matching pool U(t); scores feed business-logic matching algorithms; not incrementality or causal treatment-effect modeling.
- **model architecture:** Asynchronous causal Transformer session embedding (Wide&Deep per match history) stored in embedding memory; synchronous Wide&Deep user-feature embedding; chat-duration head with separate linear projections and exponential transform on dot product; n×n score matrix via BLAS dot products.
- **credit assignment:** Pair-level regression to realized chat duration; no slate-level, impression-level, or multi-step retention credit assignment.
- **training data and counterfactual handling:** Billion-scale Azar matching histories over one month (last two days validation/test); two-phase training freezes embeddings then trains prediction layer; auxiliary counterpart feature embedding in phase 1; no off-policy correction reported.
- **offline and online evaluation:** Offline MSE and AUROC (quality match = duration above threshold) on Entire/Warm-Warm/Warm-Cold/Cold-Cold segments; online Switchback test in Azar production (shared pool precludes A/B); latency at 90th/99th percentile.
- **reported gains:** Online vs Wide&Deep baseline: average chat duration +6.8% (warm-start), +5.9% (cold-start); long-match ratio +12.6%/+12.9%; latency −79.7% (p90) and −75.9% (p99) vs synchronous session modeling; offline AUROC up to 0.8735 (Warm-Warm) vs 0.8497 (Wide&Deep-S).
- **applicability note for a two-sided dating recommender:** Async session embedding + two-phase training is a concrete pattern for reciprocal rank/match systems where both sides are items and inference must stay sub-second at pool scale.
- **applicability note for a two-sided dating recommender:** Objective is immediate interaction quality (chat duration), not LTV/retention; Switchback (not user-level A/B) and Azar one-to-one video setting may not transfer directly to swipe-based dating catalogs.
- **unverified claims:** none
