# Paper Analysis: OneRec Technical Report

**Source:** https://arxiv.org/pdf/2506.13695.pdf
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** OneRec Technical Report
- **authors or company:** OneRec Team (Kuaishou)
- **venue:** arXiv
- **year:** 2025
- **URL:** https://arxiv.org/pdf/2506.13695.pdf
- **source type:** industry paper
- **direction:** D9
- **problem setting:** End-to-end generative short-video recommendation at Kuaishou/Kuaishou Lite, replacing multi-stage retrieve–pre-rank–rank cascades with a unified encoder–decoder that generates semantic item IDs.
- **objective and label definition:** Pre-training: next-token prediction (LNTP) on tokenized video semantic IDs from multi-scale user behavior (short, positive-feedback, lifelong compressed histories). Post-training: RSFT filters bottom 50% sessions by play duration; RL aligns via reward model combining P-Score (learned fusion of ctr, lvtr, ltr, vtr, wtr, cmtr towers), format reward, and industrial rewards (e.g., viral-content suppression). Online evaluation includes App Stay Time, Watch Time, and 7-day Lifetime (LT7).
- **long-term retention/revenue reward:** **Yes.** LT7 is an explicit online success metric; P-Score reward model includes an `ltr` tower and fuses multi-objective engagement labels into a single RL reward; vtr/Watch Time/App Stay Time used as RL rewards and online targets.
- **prediction or incrementality:** Predicts generative item distributions and optimizes policy rewards from a learned preference model—not causal incrementality of a single exposure on retention/revenue.
- **model architecture:** Tokenizer (RQ-Kmeans on collaborative-aware multimodal embeddings) → multi-scale encoder (user/context + short/positive/lifelong pathways with QFormer compression) → decoder (autoregressive semantic-ID generation) → optional reward-based selection; sparse MoE variants up to 2.633B parameters; ECPO (Early Clipped GRPO) for RL alignment.
- **credit assignment:** Session-level generative outputs scored by reward model on (user, generated item) pairs; RSFT drops low-duration sessions; RL samples 512 items per user with per-item P-Score rewards—credit at generated-item level within session, not explicit user-level delayed LTV attribution to one impression.
- **training data and counterfactual handling:** ~18B samples/day pre-training; online post-training on real-time streams with 1% users for RL sample generation via external inference service; on-policy ECPO with beam search; no explicit counterfactual correction for delayed retention labels stated.
- **offline and online evaluation:** Offline: LNTP loss, P-Score, scaling-law curves, RL ablations (pass@k, group size, beam vs top-k). Online A/B: deployed at 25% QPS on main/Lite apps—App Stay Time +0.54% / +1.24%; LT7 improvements reported; P-Score RL adds +0.21%/+0.26% Watch Time and +0.26%/+0.22% App Stay Time (Kuaishou/Lite); training MFU 23.7%, inference MFU 28.8%; OPEX 10.6% of cascaded pipeline.
- **reported gains:** 10× FLOPs vs prior ranker; 5.2×/2.6× MFU vs original ranking model; online App Stay Time and LT7 lifts; RL with vtr reward: up to +5.84% Watch Time, +1.82% App Stay Time (pass@128, group 2048 ablation).
- **applicability note for a two-sided dating recommender:** Strong reference for unifying ranking into one generative model with RL reward shaping that can include retention proxies (LT7 analogue) alongside short-term engagement heads—relevant to replacing CTR/CVR + uplift blend with a single policy-aligned scorer.
- **applicability note for a two-sided dating recommender:** Does not address reciprocity, bilateral match outcomes, or congestion; reward model fuses engagement towers rather than modeling subscription revenue or causal retention uplift per profile exposure.
- **unverified claims:** none

## 1. Summary

**Title:** OneRec Technical Report
**Authors:** OneRec Team (Kuaishou)
**Abstract:** Describes Kuaishou's production end-to-end generative recommender replacing cascaded DLRM pipelines with an encoder–decoder that generates semantic video IDs, scaled to multi-billion-parameter MoE variants with RL-based preference alignment and infrastructure co-design.

**Key contributions:**
- Unified generative architecture with collaborative-aware multimodal tokenization and multi-scale behavior encoding.
- Reward system (P-Score, format, industrial) enabling ECPO-based RL post-training in production.
- Demonstrated scaling laws, high MFU, and online lifts on App Stay Time and LT7 at 25% traffic.

**Methodology:** LNTP pre-training → RSFT + on-policy RL with external inference for sample generation; rewards from multi-tower preference model.

**Main results:** Production deployment with material stay-time and LT7 gains; RL and P-Score ablations show measurable online improvements on duration metrics.

## 2. Experiment Critique

**Design:** Extensive offline scaling, tokenizer, and RL ablations; production A/B on two apps.

**Statistical validity:** Online relative improvements reported; formal significance tests not stated for main A/B headline metrics.

**Online experiments (if any):** 25% QPS deployment; multiple duration and LT7 metrics; RL ablations on sub-traffic.

**Reproducibility:** Kuaishou proprietary data; no public code or logs.

**Overall:** Credible industrial systems report with explicit long-horizon metric (LT7) in reward and evaluation stack; retention credit assignment remains session/item-level via learned reward fusion, not causal LTV modeling.

## 3. Industry Contribution

**Deployability:** Live at scale on Kuaishou main and Lite feeds with documented MFU and OPEX savings.

**Problems solved:** Cascade fragmentation, RL integration for recommendations, generative item generation at billion-item scale.

**Engineering cost:** Very high—custom training infra, external RL inference service, MoE at billion-parameter scale.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First large-scale end-to-end generative recommender with production RL alignment and scaling-law characterization in recsys.

**Prior work comparison:** Builds on SIM, TIGER-style semantic IDs, GRPO/DPO alignment literature, and Kuaishou prior OneRec work.

**Verification:** Online metrics and deployment scope support industrial claims; independent replication not possible.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Kuaishou production logs | Not public | No | Short-video interaction and reward labels |

**Offline experiment reproducibility:** Not reproducible without Kuaishou data.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** Moves toward unified generative ranking with RL rewards that explicitly include long-horizon proxies (LT7, stay time) fused via P-Score—not a single LTV head but closer than pure CTR.

**(2) Credit assignment:** Item/session-level reward model scoring; no user-level delayed retention attribution to individual exposures.

**(3) Label and horizon definitions:** Multi-tower labels (ctr, lvtr, ltr, vtr, etc.) with LT7 as online long-horizon metric; RSFT duration filtering handles some label quality.

**(4) Short-term + long-term heads:** P-Score learns fusion across towers for RL reward; pre-training remains next-token prediction on exposed items.

**(5) Prediction vs incrementality:** Predicts and ranks generative candidates; rewards correlate with retention but do not estimate causal exposure effects.

**(6) Offline and online evaluation:** Rich offline RL ablations; online A/B on stay time, LT7, video view; two-sided interference not addressed.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Industrial reward can down-weight viral content; no two-sided market modeling.

**(8) Migration path from CTR-like model:** Documents staged path: cascaded DLRM → generative pre-train → RSFT + RL with reward model absorbing multi-objective blend.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** OneRec Team
**Affiliations:** Kuaishou
**Venue:** arXiv 2025
**Year:** 2025
**PDF:** https://arxiv.org/pdf/2506.13695.pdf
**Relevance:** Core
**Priority:** 2
