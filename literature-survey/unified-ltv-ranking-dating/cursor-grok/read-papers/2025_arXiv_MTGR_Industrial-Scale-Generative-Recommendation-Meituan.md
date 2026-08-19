# Paper Analysis: MTGR: Industrial-Scale Generative Recommendation Framework in Meituan

**Source:** https://arxiv.org/pdf/2505.18654.pdf
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** MTGR: Industrial-Scale Generative Recommendation Framework in Meituan
- **authors or company:** Ruidong Han, Bin Yin, Shangyu Chen, He Jiang, Fei Jiang, Xiang Li, Chi Ma, Mincong Huang, Xiaoguang Li, Chunzhen Jing, Yueming Han, Menglei Zhou, Lei Yu, Chuan Liu, Wei Lin (Meituan)
- **venue:** CIKM
- **year:** 2025
- **URL:** https://arxiv.org/pdf/2505.18654.pdf
- **source type:** industry paper
- **direction:** D9
- **problem setting:** Meituan food-delivery ranking at hundreds of millions of users: scale ranking models under high QPS while preserving DLRM cross features that pure generative recommenders (GRM/HSTU-style) discard, causing performance loss that scaling cannot recover.
- **objective and label definition:** Discriminative CTR and CTCVR prediction on user–candidate pairs reorganized as token sequences; labels are click and click-through-conversion events from industrial logs — no explicit retention, LTV, or revenue-per-user objective in training loss.
- **long-term retention/revenue reward:** **No.** Offline and online metrics are CTR/CTCVR AUC and PV_CTR/UV_CTCVR business growth metrics; UV_CTCVR is primary business metric but represents conversion, not stated retention or LTV horizon.
- **prediction or incrementality:** Predicts per-candidate CTR/CTCVR logits from unified token sequence — supervised ranking, not causal incrementality.
- **model architecture:** MTGR on HSTU backbone: retains full DLRM feature set including cross features by merging cross+item into candidate tokens; user-sample aggregation (one forward pass per user/request for K candidates); Group-Layer Normalization (GLN) for heterogeneous token types; dynamic masking (full-attention on user tokens, causal on realtime, self-only on targets) to prevent leakage; TorchRec training framework with dynamic hash tables, sequence balancing, embedding dedup — MTGR-large at 65× DLRM forward FLOPs per sample.
- **credit assignment:** Standard supervised CTR/CTCVR labels per candidate token after user aggregation; cross features encode user–candidate historical CTR/exposure — pointwise logged labels, no IPS or delayed-outcome user attribution.
- **training data and counterfactual handling:** Six months industrial takeaway logs with rich cross features and long behavior sequences; power-law scaling experiments on small and full data; no counterfactual correction stated.
- **offline and online evaluation:** Offline CTR/CTCVR AUC and GAUC vs DLRM variants (DNN-SIM, MoE-SIM, Wukong, UserTower); online A/B at 2% traffic vs 2-year-trained UserTower-SIM DLRM baseline; scaling-law curves over model sizes and training tokens.
- **reported gains:** MTGR-large vs DLRM baseline: offline CTR GAUC +0.8956%, CTCVR GAUC +1.4656%; online PV_CTR +1.31%, UV_CTCVR +1.22%; 65× forward FLOPs per sample with training cost unchanged and inference cost −12% vs DLRM; TorchRec throughput +1.6×–2.4×.
- **applicability note for a two-sided dating recommender:** Shows how to scale generative/HSTU-style ranking while keeping hand-crafted cross features (e.g., viewer–candidate historical match rate, exposure counts) that pure next-token GRMs drop — relevant if unified dating rankers need both sequence modeling and bilateral cross stats.
- **applicability note for a two-sided dating recommender:** CTR/CTCVR objectives and food-delivery conversion metrics do not model reciprocity, match probability, or delayed retention — architecture transfer only, not objective design for unified LTV ranking.
- **unverified claims:** none

## 1. Summary

MTGR combines DLRM feature richness (especially cross features) with GRM scalability via HSTU-based tokenization, user-level candidate aggregation, GLN, and dynamic attention masks. Optimized TorchRec training supports 10–100× compute vs DLRM without proportional cost increase. MTGR-large deployed on Meituan takeaway with largest offline/online gains in nearly two years: +1.22% UV_CTCVR and +1.31% PV_CTR online at 65× FLOPs with lower inference cost than DLRM.

## Project Relevance

**Q8** (migration): generative scaling path that preserves legacy cross features — directly relevant if dating unified models must retain viewer–candidate cross stats while adopting sequential transducers. **Q1** negative: CTR/CTCVR only. No reciprocity or retention horizon.

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | CTR and CTCVR conversion. |
| **(2) Credit assignment** | Supervised per-candidate labels with cross features. |
| **(3) Label / horizon; delay / sparsity / censoring** | Click/conversion labels; delay not specified. |
| **(4) Short-term vs long-term head fusion** | Single model with CTR + CTCVR heads. |
| **(5) Prediction vs incrementality** | Supervised prediction. |
| **(6) Offline / online eval** | AUC/GAUC offline; PV_CTR/UV_CTCVR online A/B. |
| **(7) Reciprocity / congestion / fairness / revenue vs match** | Not specified in source. |
| **(8) CTR → unified long-term migration** | Generative architecture at scale while retaining DLRM cross features. |

## Meta Information

**Authors:** Ruidong Han et al.  
**Affiliations:** Meituan  
**Venue:** CIKM 2025  
**DOI:** https://doi.org/10.1145/3746252.3761565  
**Relevance:** Core (D9 industrial generative ranking + feature retention)  
**Priority:** 1
