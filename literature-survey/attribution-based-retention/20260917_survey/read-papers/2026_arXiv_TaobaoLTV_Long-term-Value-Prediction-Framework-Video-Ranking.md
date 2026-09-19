# A Long-term Value Prediction Framework In Video Ranking

**Source:** https://arxiv.org/pdf/2602.17058.pdf | **NLM source id:** fcca450b-5415-4dee-b49a-2a2c79a2d751 | **Year / venue:** WWW 2026 | **Authors / affiliation:** Huabin Chen, Xinao Wang, Huiping Chu, Keqin Xu, Chenyi Wang, Kai Meng, Yuning Jiang (Alibaba Group, Hangzhou); Chenhao Zhai (Tsinghua University, Shenzhen) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Ranking-stage LTV modeling for short-video recommendation faces three flaws: (1) position bias — raw subsequent playtime is distorted because later exposure positions are reached by naturally more-active users; (2) attribution ambiguity — naively summing subsequent playtimes counts noise from causally unrelated content; (3) temporal scope limitation — intra-session accumulation misses cross-day re-engagement (e.g., creator-driven return). The framework has three modules: Position-aware Debias Quantile (PDQ), which partitions requests into page groups and converts continuous slide time into bounded, group-specific quantile labels (isofrequency thresholds D_{k,j}=F_k^{-1}(j/T)) to decouple content appeal from positional advantage; Multi-Dimensional Value Attribution, which learns continuous per-video attribution weights c_ji across 5+ dimensions (position co-occurrence, collection transitions, retrieval consistency, V2V similarity, multimodal similarity, author association, category coherence) via a combined MSE+Tweedie (ρ=1.5) loss to filter unrelated subsequent videos; and Cross-Temporal Author Value Modeling, extending LTV to a rolling 7-day, creator-centric re-engagement window with a dual-stream (real-time + N-day-delayed) co-training scheme and stop-gradient to prevent delayed-label gradient corruption.

Unit of credit: per recommended video item / user-video pair (u_i,v_i) at exposure position n. Outcomes: session-level attributed slide time S_j=Σc_ji·t_i; day-level author-centric 7-day value with exponential decay; online metrics N-day return-visit rate (LT1, LT3), watch time, video views, quality-author engagement. Bias handling: PDQ explicitly targets the selection bias that highly active users reach and inflate later positions; the multi-dimensional attribution weights filter confounding "credit" from unrelated co-occurring content; Tweedie+MSE loss corrects target underestimation from zero-inflation.

## 2. Evidence
- **Dataset:** Taobao production logs, 15 consecutive days, 23M users / 22M videos; train = first 14 days (7G instances), test = day 15 (523M instances).
- **PDQ offline:** XAUC 0.6252→0.6378 (+0.0126), MSE 4.9847→0.0946, MAE 1.7434→0.2402, XAUC-2=0.6894. Gains vary by page group (e.g., pages 16-29: +0.1680 XAUC); page-0 XAUC actually drops (0.4917→0.3936) due to external-promotion traffic.
- **Multi-dimensional attribution offline:** Attributed ST+MSE: XAUC 0.6253→0.6371, MSE −0.8755; adding Tweedie loss further cuts MSE to 3.7971 and improves PCOC 0.8485→0.9184.
- **Author-time co-training vs. single model:** co-training XAUC 0.7795 vs 0.7704, MSE 1.4231 vs 1.4677, PCOC 0.9916 vs 0.9008.
- **Live A/B (Taobao App):** PDQ: +2.49% video views, +0.02% LT3. Attributed Slide Time: +1.23% watch time, +0.08% LT1, +0.11% LT3, at a −1.92% VV cost. Author Time: +0.16% LT1, +0.21% LT3 (statistically significant), +4.03% quality-author VV, +2.60% quality-author watch time.

## 3. Limitations
- Cross-temporal modeling currently covers only the author/creator dimension; extensible to topics/styles/memes but not yet done.
- Does not incorporate explicit negative signals (skips, disinterest, quick exits) into LTV targets.
- Attributed Slide Time trades off watch time (+1.23%) against video views (−1.92%).
- Page-0 anomaly: PDQ underperforms baseline there due to externally-promoted, non-standard traffic.

## 4. Prior works named
- Zhan et al. 2022 — *Deconfounding duration bias in watch-time prediction for video recommendation* (KDD'22; XAUC metric, duration debiasing)
- Covington, Adams & Sargin 2016 — *Deep neural networks for YouTube recommendations* (watch-time prediction formulation)
- Sun et al. 2024, CREAD — classification-restoration discretization for watch-time prediction
- Yang et al. 2021 / Wang et al. 2023 — delayed feedback / unbiased delayed-label correction (basis for N-day label handling)
- Chang et al. 2023, PEPNet/PPNet — personalized multi-task architecture (used for task isolation)

## 5. Project Relevance
- **Answers:** Q2
- **Attributes retention to individual interactions?** partly — attributes subsequent intra-session engagement to individual recommended items via learned attribution weights, and aggregates multi-day creator watch time into an author-level LTV target that improves LT1/LT3; does not perform micro-level multi-touch sequence attribution (e.g., Shapley/counterfactual masking) across a full swipe/like/match/message history for a single retention outcome.
- **Transferable components:** PDQ position-debiasing (directly analogous to correcting for power-swipers reaching more profiles); multi-dimensional attribution weights to filter unrelated subsequent activity noise; Tweedie+MSE loss for zero-inflated, heavy-tailed retention/engagement targets; dual-stream co-training with stop-gradient for handling N7-delayed retention labels alongside real-time signals.
- **Required changes:** shift from video-exposure attribution to heterogeneous dating-funnel touch types (swipe, like, match, message) with event-type and time-gap features; replace author-centric aggregation with profile-cluster or funnel-stage aggregation; re-anchor the day-level target from a 3-day return-visit rate to a daily-recurring rolling N7 active-retention indicator.
- **On last-touch:** does not name last-touch/last-click explicitly, but explicitly critiques naive unattributed aggregation of subsequent interactions as failing to establish causal relationships and introducing noise — directly analogous to the critique of assigning all credit to only the last touch.
- **Transfer rating:** adaptable — a session/day-level LTV attribution framework for video ranking, not a multi-touch swipe-credit model, but its position-debiasing, learned attribution weights, and delayed-label co-training are directly adaptable building blocks for per-swipe retention credit.
