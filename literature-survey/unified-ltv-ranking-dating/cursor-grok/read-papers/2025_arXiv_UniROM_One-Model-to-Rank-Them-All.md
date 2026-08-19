# Paper Analysis: One Model to Rank Them All: Unifying Online Advertising with End-to-End Learning

**Source:** https://arxiv.org/pdf/2505.19755.pdf
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** One Model to Rank Them All: Unifying Online Advertising with End-to-End Learning (EGA-V1 / UniROM)
- **authors or company:** Junyan Qiu, Ze Wang, Fan Zhang, Zuowu Zheng, Jile Zhu, Jiangke Fan, Teng Zhang, Haitao Wang, Yongkang Wang, Xingxing Wang (Meituan)
- **venue:** arXiv (CIKM 2025 as "UniROM: Unifying Online Advertising Ranking as One Model")
- **year:** 2025
- **URL:** https://arxiv.org/pdf/2505.19755.pdf
- **source type:** industry paper
- **direction:** D1
- **problem setting:** Meituan LBS online advertising uses a four-stage MCA (SASRec recall → DSSM pre-rank → DIN rank → GSP auction) filtering ~10^5 city-level ads to K slots; stage inconsistency and ignored ad-to-ad externalities degrade revenue and CTR.
- **objective and label definition:** Pretrain on binary click labels ζ^clk ∈ {0,1} for K exposed + N_s=2995 popularity-sampled unexposed ads per request; post-train with RLAF maximizing platform revenue (bid × permutation-aware pCTR) under IC/IR payment constraints—no retention or delayed user-level outcome labels.
- **prediction or incrementality:** Predicts permutation-aware pCTR and generates ad allocations maximizing expected revenue—prediction and slate-level revenue attribution via marginal contribution rewards, not user-level incremental retention from exposure.
- **model architecture:** Hybrid Feature Service (local ad embeddings + single RPC user/context broadcast) + RecFormer (Global Cluster-Former with cluster-attention O(N·N_c·d) + Mid-fusion Interest-Former) + AucFormer (non-autoregressive slot generator, permutation-aware evaluator, neural payment network); bi-stage training: CE pretrain then RLAF with frozen evaluator plus Lagrangian payment optimization.
- **credit assignment:** Slate/sequence-level: RL reward r_yi = marginal revenue contribution of ad y_i in generated sequence Y vs best sequence excluding it; supervised labels are per-ad clicks within request and session—not mapping delayed user retention to a single ranked item.
- **training data and counterfactual handling:** Meituan industrial logs Apr–Oct 2024 (200M requests, 2M+ users, ~10M ads): 200-day pretrain, 50-day sampled post-train, 14-day test; popularity-sampled unexposed ads for set-aware training; RLAF on-policy against learned reward model—no off-policy correction for logged bandit data.
- **offline and online evaluation:** Offline: Recall@50, AUC, eCTR, eRPM, IC regret Ψ on held-out 14 days (5 seeds); online A/B Nov 18–24, 2024 low-traffic slot vs deployed MCA measuring CTR, RPM, ROI, response time.
- **reported gains:** Offline vs FS-LTR: Recall@50 +20.4%, AUC +1.48%, eCTR +8.3%, eRPM +11.4%, Ψ 9.1%→2.3%; online vs MCA: CTR +5.2%, RPM +13.6%, ROI +3.1%, response time +2.2% (~5 ms) despite scoring ~100× more candidates.
- **applicability note for a two-sided dating recommender:** End-to-end unification pattern—pretrain on existing myopic click/match labels, then RL-post-train toward a platform objective—is a documented migration path from CTR model + post-hoc blend to one model, if reward swaps from ad RPM to retention/revenue with reciprocity constraints added.
- **applicability note for a two-sided dating recommender:** Ad auction setting has no bilateral matching, profile-side congestion, or 7–30 day retention labels; objective remains click/revenue per impression, not causal incremental LTV of showing a specific profile.
- **unverified claims:** "First industrial-grade" end-to-end unification (priority claim). Offline/online magnitudes noted as transformed for confidentiality in source.
