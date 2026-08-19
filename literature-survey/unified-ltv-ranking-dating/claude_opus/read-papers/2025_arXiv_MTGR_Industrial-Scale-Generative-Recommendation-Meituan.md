# Paper Analysis: MTGR: Industrial-Scale Generative Recommendation Framework in Meituan

**Source:** `/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/LLM_Ranking/2025 (Meituan) (Arxiv) [MTGR] MTGR - Industrial-Scale Generative Recommendation Framework in Meituan.pdf` (arXiv:2505.18654)
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** MTGR: Industrial-Scale Generative Recommendation Framework in Meituan
**Authors:** Ruidong Han, Bin Yin, Shangyu Chen, He Jiang, Fei Jiang, Xiang Li, Chi Ma, Mincong Huang, Xiaoguang Li, Chunzhen Jing, Yueming Han, Menglei Zhou, Lei Yu, Chuan Liu, Wei Lin (Meituan)
**Venue:** arXiv preprint, 2025 (arXiv:2505.18654)

**Abstract (paraphrased from source):** Scaling law has been validated broadly across deep learning, but in recommendation systems, traditional Deep Learning Recommendation Models (DLRM) scale poorly, while recent generative recommendation models (GRM) achieve scalability by discarding the carefully constructed cross features of DLRM — a trade that "degrades model performance significantly, and scaling up cannot compensate for it at all." MTGR (Meituan Generative Recommendation), built on the HSTU architecture, retains DLRM's cross features while achieving GRM's scalability. The paper introduces Group-Layer Normalization (GLN) to align different semantic spaces of heterogeneous feature domains, and a dynamic masking strategy to avoid information leakage; it also rebuilds the training framework on PyTorch/TorchRec to support 10–100x the computational complexity of DLRM without a proportional cost increase. MTGR achieves 65x FLOPs per sample for forward computation vs. the DLRM baseline, and delivers the largest offline/online gain in nearly two years at Meituan, the world's largest food-delivery platform, where it now handles the platform's main traffic.

**Key contributions:**
1. MTGR combines DLRM's cross features (including a target-candidate historical-CTR-style feature) with GRM's (HSTU-based) scalability, rather than choosing one or the other.
2. **Group-Layer Normalization (GLN)** — normalizes each feature-domain's tokens (user static, sequence behavior, real-time behavior, candidate) separately before shared self-attention, aligning heterogeneous semantic spaces.
3. A **dynamic masking strategy** with three rules: the static sequence is fully visible to all tokens; the dynamic (real-time) sequence uses causal masking so a token only sees tokens that occurred earlier; candidate tokens are visible only to themselves — avoiding both temporal and cross-candidate information leakage.
4. **User Sample Aggregation** — all K candidates for a given user in a training/inference window are aggregated into one sample that reuses a single shared user representation, making inference cost sub-linear (not linear) in the number of candidates.
5. A rebuilt PyTorch/TorchRec training system (dynamic hash tables, dynamic sequence-length load balancing, embedding ID de-duplication, automatic table merging, bf16 mixed precision, a custom cutlass-based FlashAttention-style kernel) improving training throughput 1.6x–2.4x over the TorchRec baseline at 100+ GPUs.

**Methodology.** Input features are organized per-user as U (static profile), S̄ (historical interaction sequence), R̄ (real-time interactions within the last few hours/day), C (cross features between user and candidates), and I (candidate-specific features). Each domain is embedded, projected to a unified token dimension, and concatenated into one long token sequence per user (encompassing all K candidates for that user). The HSTU-based self-attention encoder processes this sequence layer-wise: GLN first normalizes each domain's tokens with its own statistics, then the normalized input is projected to Q/K/V/U via MLPs; attention uses a SiLU-activated, length-normalized score with the customized visibility mask described above; the resulting value update is dot-producted with the projected U term, group-layer-normed again, and passed through a residual MLP block. The model outputs a per-candidate logit for CTR and CTCVR via a discriminative loss.

**Main results.** Offline, on a proprietary 10-day Meituan take-away dataset (Table 1: 0.21B train users, 4.30B items, 23.74B exposures, 1.08B clicks, 0.18B purchases), MTGR-large beats the strongest DLRM baseline (UserTower-SIM/E2E, underlined in Table 3) by CTR AUC +0.8956%, CTR GAUC +1.0748%, CTCVR AUC +0.4990%, CTCVR GAUC +1.4656% (the team treats a 0.001 absolute GAUC change as significant based on prior experience). Ablation (Table 4, MTGR-small) shows removing cross features causes the largest single degradation (CTR AUC 0.7631→0.7495), with GLN and dynamic masking removal each causing a comparable-magnitude drop. A power-law scaling relationship (Figure 3d) holds between CTCVR GAUC gain and log-FLOPs across HSTU-block count, model dimension, and sequence length. Online, a 2%-traffic A/B test on Meituan Take-away against UserTower-SIM (continuously trained for 2 years) shows MTGR-large PV_CTR +1.90% and UV_CTCVR +1.02%, with training cost roughly unchanged and inference cost reduced 12% despite 65x FLOPs/sample, via the sub-linear User Sample Aggregation design.

## 2. Experiment Critique

**Design.** Offline comparison spans six DLRM baselines (DNN-SIM, MoE-SIM, MultiEmbed-SIM, Wukong-SIM, UserTower-SIM, UserTower-E2E) against three MTGR scales (small/medium/large) on one proprietary 10-day dataset, plus a component ablation (cross features, GLN, dynamic masking) on MTGR-small.

**Statistical validity.** No p-values or confidence intervals are reported; the paper relies on an internal team heuristic ("an increase of 0.001 in our offline metric is considered significant") rather than a formal significance test.

**Online experiments.** A real 2%-traffic A/B test on a single platform (Meituan Take-away, "millions of exposures per day") against a DLRM baseline matured over 2 years of continuous training — a reasonably strong comparison, but the paper does not state the A/B test's duration, and all evidence comes from one vertical (food delivery) on one platform.

**Reproducibility.** Both the training data and the DLRM baseline configuration are Meituan-internal; the paper explicitly notes public recommendation datasets are unsuitable because they lack the cross features central to MTGR's design, so none of the reported numbers can be independently reproduced outside Meituan.

**Overall.** The ablation study is the paper's most rigorous evidence (isolating cross features, GLN, and masking individually), but the headline offline and online gains rest on proprietary data and an internal, not statistically formalized, significance bar.

## 3. Industry Contribution

**Deployability.** MTGR-large is already deployed, serving hundreds of millions of users on the Meituan Take-away platform, with reported training cost roughly unchanged and inference cost reduced 12% relative to the DLRM baseline despite 65x more FLOPs per sample for forward computation.

**Problems solved.** Directly resolves the GRM-vs-DLRM trade-off the paper identifies: GRM (HSTU-style) scales but "excluding cross features severely damages the model's performance, and this degeneration cannot be compensated for by scaling up at all," while DLRM has hand-crafted cross features but scales poorly. MTGR keeps both.

**Engineering cost.** Substantial: a full training-framework rewrite from TensorFlow to PyTorch/TorchRec, custom dynamic hash tables for streaming sparse-embedding growth, dynamic per-GPU sequence-length load balancing, embedding ID de-duplication with automatic table merging, and a custom cutlass-based fused-attention kernel — offset by a reported 1.6x–2.4x training-throughput improvement over the TorchRec baseline at 100+ GPUs.

## 4. Novelty vs. Prior Work

**Claimed novelty.** Combining DLRM's cross-feature strength with GRM's HSTU-based scalability (rather than choosing one), Group-Layer Normalization for aligning heterogeneous feature-domain semantic spaces, and User Sample Aggregation for sub-linear per-candidate inference cost.

**Prior work named in the source:**
- Zhai et al., "Actions Speak Louder Than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations," 2024 — the HSTU architecture MTGR is built on.
- Zhang et al., "Wukong: Towards a Scaling Law for Large-Scale Recommendation," 2024 — a stackable feature-interaction scaling baseline (Wukong-SIM) and a named cross-module scaling approach.
- Guo et al., "On the Embedding Collapse When Scaling Up Recommendation Models," 2023 — the multi-embedding strategy motivating the MultiEmbed-SIM baseline.
- Ivchenko et al., "TorchRec: a PyTorch Domain Library for Recommendation Systems," 2022 — the training framework MTGR's system is rebuilt on and optimized against.
- Deng et al., "OneRec: Unifying Retrieve and Rank with Generative Recommender and Iterative Preference Alignment," 2025 — cited as a related generative-recommendation approach combining DPO-style optimization with HSTU.
- Shin et al., "Scaling Law for Recommendation Models: Towards General-Purpose User Representations," 2023 — cited scaling-law precedent for user-representation models.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| Meituan Take-away production logs (10-day train/test) | Food-delivery impression/click/purchase logs with cross features | Not public | Table 1: 0.21B train users, 4.30B items, 23.74B exposures, 1.08B clicks, 0.18B purchases (test: 3.02M users, 3.14M items, 76.86M exposures, 4.55M clicks, 769K purchases). |
| Meituan Take-away production logs (6-month, online experiment) | Same platform, extended window for online-comparable training | Not public | Used to train MTGR to compare against the 2-year-trained DLRM baseline in the online A/B test. |
| Public recommendation datasets | — | N/A | Explicitly rejected by the authors: "public datasets widely use independent ID and attribute features... cross features are seldom introduced," making them unsuitable for validating MTGR's core contribution. |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | MTGR: Industrial-Scale Generative Recommendation Framework in Meituan; Ruidong Han, Bin Yin, Shangyu Chen, He Jiang, Fei Jiang, Xiang Li, Chi Ma, Mincong Huang, Xiaoguang Li, Chunzhen Jing, Yueming Han, Menglei Zhou, Lei Yu, Chuan Liu, Wei Lin (Meituan); arXiv preprint, 2025 (arXiv:2505.18654); https://arxiv.org/abs/2505.18654 |
| 2 | Source type | Industry paper |
| 3 | Direction | D9 |
| 4 | Problem setting | Reconciling the scalability of generative recommendation models (GRM, HSTU-based) with the hand-crafted cross-feature strength of traditional DLRM for Meituan's food-delivery ranking, where dropping cross features "severely damages the model's performance, and this degeneration cannot be compensated for by scaling up at all." |
| 5 | Objective and label definition | Multi-task prediction of CTR (click given impression) and CTCVR (click-then-purchase given impression) via per-candidate discriminative logits. No explicit time horizon is stated beyond the training/test window (a 10-day production log split for offline experiments); no delay or censoring handling is described anywhere in the sections read. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. |
| 7 | Model architecture | HSTU-based self-attention encoder over a token sequence formed by concatenating user-static (U), sequence-behavior (S̄), real-time-behavior (R̄), cross-feature (C), and per-candidate (I) tokens. Group-Layer Normalization (GLN) normalizes each feature-domain's tokens separately before shared self-attention; a customized attention mask gives the static sequence full visibility, causal masking to the real-time dynamic sequence, and self-only visibility to candidate tokens; User Sample Aggregation batches all K candidates for one user into a single sample sharing one user representation. |
| 8 | Credit assignment | Item-level within an aggregated multi-candidate sample — each candidate token receives its own logit/outcome (click, purchase) via the customized attention mask, while sharing the same user-context computation across all K candidates; no slate-level or delayed multi-day attribution mechanism is described. |
| 9 | Training data and counterfactual handling | Meituan Take-away production logs, 10-day training/test split (Table 1); public datasets explicitly rejected as unsuitable because they lack the hand-crafted cross features central to the model. No propensity weighting or counterfactual correction is described. |
| 10 | Offline and online evaluation | Offline: AUC and GAUC (group/per-user-averaged AUC) on CTR and CTCVR against six DLRM baselines (DNN-SIM, MoE-SIM, MultiEmbed-SIM, Wukong-SIM, UserTower-SIM, UserTower-E2E). Online: a 2%-traffic A/B test on Meituan Take-away (millions of exposures/day) against UserTower-SIM, a DLRM baseline continuously trained for 2 years, tracking PV_CTR and UV_CTCVR. |
| 11 | Reported gains | Offline, MTGR-large vs. strongest underlined DLRM baseline on the 10-day Meituan take-away dataset: CTR AUC +0.8956%, CTR GAUC +1.0748%, CTCVR AUC +0.4990%, CTCVR GAUC +1.4656%. Online A/B on Meituan Take-away: MTGR-large PV_CTR +1.90%, UV_CTCVR +1.02%. Infrastructure: 65x FLOPs per sample vs. the DLRM baseline for forward computation, training cost roughly unchanged, inference cost reduced 12%; training throughput improved 1.6x–2.4x over the TorchRec baseline at 100+ GPUs. |
| 12 | Applicability to a two-sided dating recommender | The Group-Layer-Normalization plus customized-mask pattern for combining heterogeneous feature domains (static, sequential, real-time, cross, candidate) without losing hand-crafted pairwise cross features is directly reusable for a dating ranker that also needs A–B cross features. But the objective remains CTR/CTCVR only — no retention, revenue, or reciprocity signal is modeled anywhere in the paper. |
| 13 | Unverified claims | The claim that excluding cross features "cannot be compensated for by scaling up at all" is asserted from a single ablation on MTGR-small (Table 4) rather than a systematic scaling sweep with cross features removed at every model scale. The power-law scaling relationship (Figure 3d) is fit to a small number of configuration points without a reported goodness-of-fit statistic. |

## Project Relevance

Speaks to **Q1, Q2, Q3, Q4, Q8**. Direct negative/gap finding for **Q1/Q3**: the training objective is CTR and CTCVR only, both immediate per-impression events — retention, LTV, and any multi-day horizon are absent from the paper entirely, exactly the kind of "no long-horizon objective" result the batch brief flags as legitimate. Positive relevance for **Q8**: MTGR is a documented, currently-deployed industrial migration path from DLRM to a generative/HSTU-based unified ranker that deliberately preserves hand-crafted cross features rather than discarding them for scale — useful evidence that a unified architecture need not sacrifice engineered pairwise features, which matters for a reciprocity-heavy dating ranker. Positive for **Q2**: the User Sample Aggregation plus customized-masking pattern is a clean, reusable answer for assigning one outcome per candidate item while sharing user-side computation, independent of what the eventual label becomes. Q5, Q6, Q7 are not addressed — no incrementality, no online design under interference, and no reciprocity or congestion treatment appears anywhere in the paper.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2026_RecSys_GenPage_End-to-End-Generative-Homepage-Construction.md](./2026_RecSys_GenPage_End-to-End-Generative-Homepage-Construction.md) | Related Work / Experiments | Names this paper's method (`MTGR`) |
| [2026_arXiv_GenRec_LLM-Backed-Recommendation-Ranker.md](./2026_arXiv_GenRec_LLM-Backed-Recommendation-Ranker.md) | Related Work / Experiments | Names this paper's method (`MTGR`) |
| [2026_arXiv_MTFM_Scalable-Alignment-free-Foundation-Model-Meituan.md](./2026_arXiv_MTFM_Scalable-Alignment-free-Foundation-Model-Meituan.md) | Related Work / Experiments | Names this paper's method (`MTGR`) |

_3 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `MTGR` across all 133 cards._

## Meta Information

- **Authors:** Ruidong Han, Bin Yin, Shangyu Chen, He Jiang, Fei Jiang, Xiang Li, Chi Ma, Mincong Huang, Xiaoguang Li, Chunzhen Jing, Yueming Han, Menglei Zhou, Lei Yu, Chuan Liu, Wei Lin
- **Affiliations:** Meituan
- **Venue:** arXiv preprint (arXiv:2505.18654)
- **Year:** 2025
- **Relevance:** Core
- **Priority:** 2
- **nlm:3e635d25**
