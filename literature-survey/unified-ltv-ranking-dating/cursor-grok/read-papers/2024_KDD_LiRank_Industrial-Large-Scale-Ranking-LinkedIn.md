# Paper Analysis: LiRank: Industrial Large Scale Ranking Models at LinkedIn

**Source:** https://arxiv.org/pdf/2402.06859.pdf
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** LiRank: Industrial Large Scale Ranking Models at LinkedIn
- **authors or company:** Fedor Borisyuk, Mohit Kothari, Chen Zhu, Daqi Sun, Yun Dai, Xun Luan, Sirou Zhu, Zhiwei Wang, Neil Daftary, Qianqi Shen, Chengming Jiang, Haichao Wei, Maneesh Varshney, Amol Ghoting, Souvik Ghosh (LinkedIn)
- **venue:** KDD
- **year:** 2024
- **URL:** https://arxiv.org/pdf/2402.06859.pdf
- **source type:** industry paper
- **direction:** D1
- **problem setting:** Unified large-scale ranking framework for LinkedIn Feed second-pass ranking, Ads CTR, and Jobs recommendation (JYMBII / Job Search) at production scale.
- **objective and label definition:** Multi-task pointwise ranking: Feed predicts like, comment, share, vote, click, long dwell per (member, post) pair; Ads CTR uses chargeability-based MTL with three heads; Jobs predict application and click probabilities. Long dwell defined as binary exceedance of context-dependent percentile thresholds (e.g., 90th) clustered by position, content type, platform.
- **prediction or incrementality:** Predicts probabilities of short-horizon engagement events and dwell exceedance; Thompson sampling on last-layer weights explores for long-term DAU gains—not causal incrementality modeling of exposure effects.
- **model architecture:** LiRank stack: Residual DCN (attention + skip on low-rank DCNv2), isotonic calibration layer, dense gating, TransAct transformer history encoder, grouping-strategy MTL towers, Fisher-regularized incremental training, QR hashing + middle-max 8-bit embedding quantization, Neural Linear Thompson sampling for explore/exploit.
- **credit assignment:** Pointwise (member, item) labels per impression; no session-level delayed outcome propagation to individual items stated; long dwell and session metrics evaluated at aggregate A/B level.
- **training data and counterfactual handling:** Production impression logs with multi-task labels; incremental training with Fisher information regularization against catastrophic forgetting; Thompson sampling posterior updated each offline training period; explore/exploit balances new items vs historical feedback exploitation.
- **offline and online evaluation:** Offline AUC/ablation tables on Feed, Ads, Jobs datasets; online A/B tests across surfaces; Feed dwell modeling reports +0.8% overall time spent, +1% time per post, +0.2% sessions offline; production lifts on sessions, qualified applications, Ads CTR.
- **reported gains:** +0.5% Feed member sessions; +1.76% qualified job applications (Jobs search/recommendations); +4.3% Ads CTR relative in online A/B; +0.06% professionals DAU from Thompson sampling; Ads quantization +0.9% CTR relative in online testing.
- **applicability note for a two-sided dating recommender:** Useful reference for unifying multi-head engagement ranking, dwell/long-session modeling, calibration, and incremental retraining under streaming data—patterns transferable to swipe/match funnels with multiple engagement types.
- **applicability note for a two-sided dating recommender:** Does not model bilateral match outcomes, reciprocity constraints, or user-level retention credit assignment to individual profile exposures; objectives remain engagement/CTR/dwell proxies per side-item pair.
- **unverified claims:** none

## 1. Summary

**Title:** LiRank: Industrial Large Scale Ranking Models at LinkedIn
**Authors:** Fedor Borisyuk et al. (LinkedIn)
**Abstract:** Presents LiRank, a production ranking framework combining Residual DCN, native isotonic calibration, TransAct history modeling, MTL grouping, incremental Fisher regularization, compression (QR hashing, quantization), and scalable training/serving for Feed, Ads, and Jobs.

**Key contributions:**
- Residual DCN layer with self-attention and skip connections atop DCNv2.
- Isotonic calibration as a trainable neural layer co-trained with ranking models.
- Production deep explore/exploit via Neural Linear Thompson sampling; 4D model parallelism and training speedups.

**Methodology:** Pointwise MTL with grouped towers; long dwell as multi-class binary exceedance of dynamic percentile thresholds; listwise training with industrial feature embeddings and compression for serving.

**Main results:** Significant relative lifts across Feed sessions (+0.5%), qualified job applications (+1.76%), and Ads CTR (+4.3%) in live A/B tests.

## 2. Experiment Critique

**Design:** Broad surface coverage with component ablations (DCN variants, MTL architectures, calibration, TransAct, quantization); compares Wide&Deep, DeepFM, xDeepFM, MMoE, PLE, etc.

**Statistical validity:** Online metrics reported as relative lifts; specific p-values not in extracted excerpts for main surface lifts; dwell ablations show granular offline gains.

**Online experiments (if any):** A/B tests on Feed, Ads CTR, Jobs; Thompson sampling +0.06% professionals DAU; quantization +0.9% Ads CTR.

**Reproducibility:** LinkedIn proprietary data; open-sourced Avro Tensor Dataset Loader; no public ranking datasets.

**Overall:** Strong engineering synthesis paper; long-term retention is indirect (sessions, DAU, dwell) rather than explicit LTV labels; multi-objective trade-offs fused via linear score combination in Feed rather than unified value head.

## 3. Industry Contribution

**Deployability:** Deployed across major LinkedIn ranking surfaces with CPU-serving constraints addressed via quantization and QR hashing.

**Problems solved:** Training divergence/overfitting when stacking SOTA layers; calibration at scale; catastrophic forgetting in incremental training; embedding memory and latency.

**Engineering cost:** High—many moving parts (RDCN, calibration, TransAct, Fisher incremental, compression, parallelism); but documents practical tuning lessons.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Residual DCN; native isotonic layer; production Neural Linear Thompson sampling; middle-max quantization; integrated LiRank recipe with proven cross-surface impact.

**Prior work comparison:** Builds on DCNv2, Wide&Deep, DeepFM, xDeepFM, AutoInt, MMoE, PLE, TransAct, Platt/isotonic calibration, DLRM parallelism.

**Verification:** Incremental architectural/engineering contributions rather than new long-term objective theory; production metrics support deployability claims.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| LinkedIn Feed / Ads / Jobs production logs | Not public | No | Sparse ID + dense features described in appendix |

**Offline experiment reproducibility:** Not reproducible without LinkedIn data.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** CTR-like and engagement proxies (click, like, comment, share, vote, long dwell); Ads CTR and chargeable clicks; session/time spent and DAU as longer-horizon business metrics—not explicit LTV/revenue retention labels in unified head.

**(2) Credit assignment:** Pointwise labels per (member, candidate) impression; long dwell thresholds per context cluster; no stated mapping of user-level delayed retention to single exposure credit.

**(3) Label and horizon definitions:** Binary engagement labels; long dwell = exceedance of dynamic percentile thresholds updated daily by cluster; noisy dwell handled via percentile/cluster approach rather than raw regression; sparsity across tasks handled via MTL grouping.

**(4) Short-term + long-term heads:** Multiple task heads (grouped towers) with linear combination into final Feed post score—fixed fusion of head outputs; separate heads for click/long dwell vs contribution actions.

**(5) Prediction vs incrementality:** Predicts event probabilities and calibrated scores; Thompson sampling explores for long-term DAU—not causal effect of a specific exposure on retention.

**(6) Offline and online evaluation:** Offline AUC/ablations; online A/B on sessions, qualified applications, CTR, DAU; dwell and session metrics; delayed retention via session/DAU surrogates; two-sided interference not specified in source.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Not specified in source.

**(8) Migration path from CTR-like model:** Evolves production CTR/engagement rankers by adding dwell modeling, calibration layer, history encoder, incremental training, and compression—still multi-head engagement fusion rather than single unified LTV model.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Fedor Borisyuk, Mohit Kothari, Chen Zhu, Daqi Sun, Yun Dai, Xun Luan, Sirou Zhu, Zhiwei Wang, Neil Daftary, Qianqi Shen, Chengming Jiang, Haichao Wei, Maneesh Varshney, Amol Ghoting, Souvik Ghosh
**Affiliations:** LinkedIn
**Venue:** KDD 2024
**Year:** 2024
**PDF:** https://arxiv.org/pdf/2402.06859.pdf
**Relevance:** Core
**Priority:** 1
