# Paper Analysis: MTFM: A Scalable and Alignment-free Foundation Model for Industrial Recommendation in Meituan

**Source:** https://arxiv.org/abs/2602.11235
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** MTFM: A Scalable and Alignment-free Foundation Model for Industrial Recommendation in Meituan
- **authors or company:** Xin Song, Zhilin Guan, Ruidong Han, Binghao Tang, Tianwen Chen, Bing Li, Zihao Li, Han Zhang, Fei Jiang, Qing Wang, Zikang Xu, Fengyi Li, Chunzhen Jing, Lei Yu, Wei Lin (Meituan)
- **venue:** arXiv
- **year:** 2026
- **URL:** https://arxiv.org/abs/2602.11235
- **source type:** industry paper
- **direction:** D1
- **problem setting:** Cross-scenario industrial ranking across three Meituan surfaces (Homepage restaurant, Pinhaofan food, Shenqiangshou coupon-package) with heterogeneous feature schemas — scale a single foundation backbone instead of per-scenario alignment or two-stage foundation-expert pipelines.
- **objective and label definition:** Per-scenario, per-task supervised labels: CTR and CTCVR on HP/PHF; CTR, CTCVR, IMD (30-minute redemption), WRITE (24-hour redemption) on SQS — immediate click/conversion/redemption events, no explicit multi-week retention or LTV horizon in training objective.
- **prediction or incrementality:** MMoE heads on final T-token embeddings output separate scenario-specific task scores — standard supervised prediction of short-horizon conversion events, not causal incrementality on long-term outcomes.
- **model architecture:** MTFM: heterogeneous tokenization (H-tokens from historical sequences, R-tokens from realtime sequences, T-tokens per exposure) fed to Hybrid Target Attention blocks (interleaved full-attention + target-attention layers with GQA); dynamic causal mask prevents leakage; scenario-specific subgraphs at inference; user-level multi-scenario sample aggregation; system co-design (CPU-GPU pipeline, fused kernels, 2:4 structured sparsity).
- **credit assignment:** Item/exposure-level labels per candidate T-token after user-level aggregation across scenarios; shared H/R tokens carry cross-scenario behavior — standard logged-label supervision, no delayed user-outcome attribution to individual exposures.
- **training data and counterfactual handling:** Industrial food-delivery logs — HP 18.53B exposures, PHF 15.29B, SQS 2.24B (Table 1); baselines include DCNv2, MMoE, RankMixer, MTGR, OneTrans, STAR, PEPNet; no counterfactual or IPS correction stated.
- **offline and online evaluation:** Offline AUC/GAUC per scenario and task; scaling curves vs model GFLOPs and training tokens; online A/B vs multi-year SOTA baseline on SQS and PHF (tens of millions of daily exposures).
- **reported gains:** Offline: MTFM best across scenarios — e.g. HP CTR GAUC 0.6954, CTCVR GAUC 0.6507; SQS CTR GAUC 0.8027. Online: SQS orders +2.98%, CTR +1.89%, UV_CTCVR +2.46%, latency −5ms; PHF orders +1.45%, CTR +1.53%, UV_CTCVR +1.03%, latency −6ms.
- **applicability note for a two-sided dating recommender:** Heterogeneous-token, alignment-free multi-scenario foundation modeling is a plausible infrastructure pattern if a dating ranker must share backbone across feeds (discovery, likes-you, boosts) with incompatible feature schemas without hand-aligning every cross-stat.
- **applicability note for a two-sided dating recommender:** Tasks are short-horizon CTR/CTCVR/redemption only — no retention/LTV objective, no reciprocal matching or congestion modeling; MTFM is representation scaling, not a recipe for unifying uplift blend into one long-term value head.
- **unverified claims:** Venue field in PDF is ACM placeholder text — formal publication venue beyond arXiv not confirmed in source.

## 1. Summary

MTFM is Meituan's alignment-free recommendation foundation model: disparate scenario features become H/R/T tokens processed by a hybrid sparse-dense attention backbone with MMoE multi-task heads. User-level aggregation and system optimizations enable cross-scenario scaling laws. Offline and online experiments on three food-delivery scenarios show consistent GAUC gains and order lifts without the see-saw effect of prior multi-scenario methods.
