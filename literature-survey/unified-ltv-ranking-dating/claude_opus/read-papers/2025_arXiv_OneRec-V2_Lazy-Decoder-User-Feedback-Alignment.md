# Paper Analysis: OneRec-V2 Technical Report

**Source:** `/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/LLM_Ranking/2025 (Kuaishou) (Arxiv) [OneRec-V2] OneRec Technical Report v2.pdf` (arXiv:2508.20900)
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** OneRec-V2 Technical Report
**Authors:** OneRec Team
**Venue:** arXiv preprint, 2025 (arXiv:2508.20900)

**Abstract (paraphrased from source):** OneRec-V1 showed strong empirical results as an industrial-scale generative recommendation framework that reformulates recommendation as end-to-end autoregressive generation, but two problems limited it: (1) inefficient computational allocation in its encoder-decoder architecture, where 97.66% of FLOPs go to encoding user context rather than generating the target item, capping model scale; and (2) reliance on reward-model-only reinforcement learning, which has limited sampling efficiency (rollouts affordable only for a small user subset) and is prone to reward hacking. OneRec-V2 addresses both: a Lazy Decoder-Only architecture that removes the encoder and simplifies cross-attention (no K/V projections), cutting total computation 94% and training resources 90% while enabling 16x parameter scaling (0.5B→8B); and a preference-alignment framework that uses real user feedback (duration-aware reward shaping plus explicit dislikes) instead of relying solely on a reward model. Online A/B tests on Kuaishou/Kuaishou Lite (400M DAU) show App Stay Time gains of 0.467% and 0.741% over OneRec-V1 without seesaw effects across objectives.

**Key contributions:**
1. **Lazy Decoder-Only Architecture** — a Context Processor turns heterogeneous user-feature pathways (static / short-term / long-term behavior) into layer-shared key-value pairs, consumed via a lazy cross-attention that drops K/V projection layers entirely and uses Grouped Query Attention, followed by causal self-attention and an FFN (with MoE variants in deeper layers).
2. **Preference Alignment with Real-World User Interactions** — Duration-Aware Reward Shaping (normalizes watch time against a user's own historical distribution for videos of similar duration) plus Adaptive Ratio Clipping via a new RL algorithm, **GBPO** (Gradient-Bounded Policy Optimization), which removes hard ratio clipping in favor of a dynamic bound tied to the sign of the advantage.
3. Comprehensive scaling experiments (dense 0.1B–8B and a 4B-total/0.5B-active MoE variant) showing the lazy decoder matches encoder-decoder convergence loss at roughly 10x fewer FLOPs.
4. A live 5%-traffic, one-week online A/B test on Kuaishou and Kuaishou Lite (400M DAU) at 1B parameters.

**Methodology.** Pretraining uses next-token-prediction cross-entropy over 3 semantic-ID tokens per target item (loss averaged, not summed, across the 3 tokens — a change from V1), with no explicit horizon: it is an immediate next-item generation task. Post-training (Section 3) keeps V1's streaming-exposure SFT phase unchanged, then applies GBPO-based RL. The reward is built from **Duration-Aware Reward Shaping**: historical videos in a user's watch history are bucketed by duration on a log scale (bucket function ⌊log_β(d+ε)⌋), and for a target video the paper computes the empirical percentile rank of its playing time within the user's own historical playtime distribution for that duration bucket. Samples in the top 25% quantile (per-batch threshold τ_B) get advantage +1; samples with an explicit "dislike" action get advantage −1; everything else is filtered out (advantage 0, no gradient). GBPO then uses this advantage in a policy-gradient objective that removes the standard PPO/GRPO ratio-clipping operation and instead bounds the *old*-policy term dynamically based on the sign of the advantage — for negative samples this bounds the RL gradient using the flatter, more-stable shape of a BCE-loss gradient, which the paper shows (Figure 8) produces substantially more stable gradients than V1's Early-Clipped GRPO (ECPO), especially for negative/dislike samples.

**Main results.** Online A/B (Table 8, vs. OneRec-V1 baseline): Kuaishou App Stay Time +0.467%, LT7 (7-day lifetime) +0.069%, Watch Time +1.367%, Like +3.924%, Comment +5.394%; Kuaishou Lite App Stay Time +0.741%, LT7 +0.034%, Watch Time +0.762%, Forward +7.958%. An ablation (Table 6) shows that incorporating on-policy OneRec-generated exposure samples into RL training (vs. training only on samples from the traditional pipeline) turns several metrics from negative to positive, e.g., Video View on Kuaishou moves from −0.901% to +0.716%. A second ablation (Table 7) compares Reward-Model-only, User-Feedback-only, and Hybrid RL: the reward model tends to favor interaction metrics (Comment +15.472% on Kuaishou) while user feedback tends to favor App Stay Time (+0.299% vs. +0.269% for the reward model), and the Hybrid setting balances the two.

## 2. Experiment Critique

**Design.** Architecture comparisons are controlled: the same convergence-loss metric is compared across encoder-decoder (1:1, 1:2 ratios), naive decoder-only, and lazy decoder-only models at matched parameter scales (0.1B–1B), plus a separate dense scaling sweep (0.1B–8B) and one MoE configuration. RL ablations use three parallel online A/B groups (Reward Model / User Feedback / Hybrid) against the same OneRec-V1 baseline.

**Statistical validity.** No confidence intervals or significance tests are reported for any of the online A/B deltas in the sections read; results are point percentages only. (OneRec-V1's card in this survey notes a stated 0.01% significance threshold for LT7; this specific threshold is not restated in the V2 sections read here.)

**Online experiments.** A genuine, sizable live test: 5% traffic on Kuaishou and Kuaishou Lite (400M combined DAU) over one week, with a 1B-parameter model at context length 3000 and beam size 512, deployed on L20 GPUs at 36ms latency and 62% MFU — a credible, large-scale production evaluation.

**Reproducibility.** All training and evaluation data are Kuaishou's proprietary streaming production logs (an explicit August 10–14, 2025 window for the architecture experiments); no public benchmark or released code is mentioned in the sections read, so none of the reported numbers are independently reproducible.

**Overall.** The architecture ablations are well-controlled and internally consistent; the RL ablations are informative about *why* user feedback and reward-model signals diverge (duration-correlated vs. multi-objective-fused reward) but rest entirely on proprietary online A/B percentages without variance reporting.

## 3. Industry Contribution

**Deployability.** Concrete production serving numbers are given: a 1B-parameter model at context length 3000, 36ms inference latency, 62% MFU on L20 GPUs, deployed to 5% of traffic across two apps serving 400M DAU.

**Problems solved.** Directly fixes OneRec-V1's two named bottlenecks: the lazy decoder eliminates the ~97.66%-of-FLOPs context-encoding overhead that limited scaling, and the user-feedback-based reward directly addresses V1's reward-hacking and limited-rollout-sampling weaknesses.

**Engineering cost.** Requires a new Context Processor abstraction, a custom lazy cross-attention (no K/V projection) with Grouped Query Attention, and a new RL algorithm (GBPO) replacing V1's ECPO — a nontrivial architectural and training-infrastructure investment, offset by a reported 94% reduction in total computation and 90% reduction in training resources at equivalent quality.

## 4. Novelty vs. Prior Work

**Claimed novelty.** Two contributions over OneRec-V1 (Zhou et al., 2025): the Lazy Decoder-Only architecture (removing the encoder and K/V projections entirely, unlike V1's encoder-decoder design) and real-user-feedback-driven preference alignment (Duration-Aware Reward Shaping + GBPO) in place of V1's reward-model-only RL (Early-Clipped GRPO).

**Prior work named in the source:**
- Zhou et al., OneRec-V1 (via Zhou et al., 2025), the direct predecessor this paper builds on and benchmarks against throughout.
- Schulman et al., "Proximal Policy Optimization Algorithms," 2017 — the PPO ratio-clipping formulation GBPO explicitly departs from.
- Shao et al., "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models," 2024 — source of the GRPO formulation referenced in the GBPO derivation.
- Yu et al., "DAPO," 2025 — a clip-higher relaxation strategy discussed as related but incomplete RL-stability work.
- Ainslie et al., "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints," 2023 — the Grouped Query Attention mechanism reused in the lazy cross-attention design.
- Liu et al., "DeepSeek-V3 Technical Report," 2024 — source of the auxiliary-loss-free MoE load-balancing strategy adopted for the sparse variant.
- Kaplan et al., "Scaling Laws for Neural Language Models," 2020 — the reference scaling-law framework the paper's own results are checked against (and found not to strictly follow) in the Limitations section.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| Kuaishou streaming production logs (Aug 10–14, 2025) | Short-video impression/exposure streams, 400M DAU platform | Not public | Used for architecture-scaling and key-value-sharing/GQA ablation experiments. |
| Kuaishou + Kuaishou Lite live traffic (one-week, 5% experimental group) | Online production A/B test traffic | Not public | Used for the online evaluation reported in Tables 6–8 and Section 4. |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | OneRec-V2 Technical Report; OneRec Team, Kuaishou; arXiv preprint, 2025 (arXiv:2508.20900); https://arxiv.org/abs/2508.20900 |
| 2 | Source type | Industry paper (technical report) |
| 3 | Direction | D9 |
| 4 | Problem setting | Scaling and preference-alignment limitations of OneRec-V1's encoder-decoder generative recommender for short-video feed ranking at Kuaishou (400M DAU): (a) computational-allocation inefficiency that limits model scale, and (b) reward-model-only RL's sampling inefficiency and reward-hacking risk. |
| 5 | Objective and label definition | Pretrain: next-token-prediction cross-entropy over 3 semantic-ID tokens of the target item, no explicit horizon (immediate next-item generation). Post-train reward: duration-aware quantile rank of same-session watch time within a log-duration-bucketed peer group (top-25% quantile → +1 advantage) combined with explicit dislike feedback (→ −1); all other samples filtered (advantage 0). No delay handling or censoring anywhere in the reward definition; LT7 (7-day lifetime) appears only as an online A/B evaluation metric, never as a training label. The authors state directly (Section 5, Limitation 2): "our current solution establishes rules linking short-term and long-term returns, rather than allowing the model to directly optimize its long-term value." |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. |
| 7 | Model architecture | Lazy Decoder-Only Transformer: a Context Processor converts heterogeneous user-feature pathways (static / short-term / long-term behavior) into layer-shared key-value pairs consumed via lazy cross-attention (no K/V projections) plus causal self-attention and an FFN (with MoE in deeper layers); scales dense models 0.1B–8B and one MoE configuration (4B total / 0.5B active, 53 routed + 1 shared expert, top-3 routing); trained via next-token prediction then post-trained with GBPO (Gradient-Bounded Policy Optimization), replacing V1's Early-Clipped GRPO. |
| 8 | Credit assignment | Item-level — GBPO computes a per-generated-item advantage (duration-aware engagement quantile or dislike flag) within a single user request; no mechanism attributes the delayed, user-level LT7 outcome back to individual items — LT7 is observed only in aggregate online A/B statistics. |
| 9 | Training data and counterfactual handling | Streaming production impression/exposure logs for pretraining and SFT; RL samples drawn from both the traditional serving pipeline and on-policy OneRec-generated exposures — an ablation (Table 6) shows on-policy samples materially improve results (e.g., Video View swings from −0.901% to +0.716% on Kuaishou). No propensity weighting or counterfactual correction is described. |
| 10 | Offline and online evaluation | Offline: generation cross-entropy loss, engagement-tower metrics, and architecture/scaling ablations (Tables 2–5). Online: 5%-traffic, one-week A/B test on Kuaishou and Kuaishou Lite (400M combined DAU), 1B-parameter model, context length 3000, beam size 512, tracking App Stay Time, LT7, and engagement actions (like, follow, comment, collect, forward). |
| 11 | Reported gains | Online A/B vs. OneRec-V1 (Table 8) — Kuaishou: App Stay Time +0.467%, LT7 +0.069%, Watch Time +1.367%, Like +3.924%, Comment +5.394%; Kuaishou Lite: App Stay Time +0.741%, LT7 +0.034%, Watch Time +0.762%, Follow +5.627%. Architecture: 94% FLOPs reduction and 90% training-resource reduction vs. V1's encoder-decoder at equivalent budget, enabling 16x parameter scaling (0.5B→8B). |
| 12 | Applicability to a two-sided dating recommender | The multi-pathway (static/short/long-term) user encoding and GBPO's stabilized-gradient RL are reusable engineering patterns for combining objective signals. But the entire alignment signal is same-session watch-time quantile plus dislike, and the authors' own limitations section confirms no direct long-term-value optimization exists yet — this paper offers no template for a retention/revenue training objective. |
| 13 | Unverified claims | The claim that duration-aware reward shaping "established a correlation between short-term video watching time and long-term satisfaction" is asserted from co-movement of two online metrics (App Stay Time and LT7 both rising) rather than any formal causal or statistical test reported in the sections read. The MoE scaling claim that gains "diminish" beyond 2B parameters rests on a single convergence-loss delta (0.03 from 2B→4B) with no confidence interval. |

## Project Relevance

Speaks to **Q1, Q3, Q4, Q8**. This is the direct sequel to the OneRec-V1 card already in this survey (`2025_arXiv_OneRec_Technical-Report.md`), and it sharpens rather than resolves that card's finding: where the V1 card had to *infer* that LT7 was measured but not optimized, OneRec-V2's own authors now state the gap explicitly in their own words (Section 5, Limitation 2, quoted above) — the reward system links short-term and long-term returns only by rule, not by directly optimizing long-term value. This is a clean, first-party confirmation of a "no long-horizon objective" finding, exactly the kind of legitimate negative result the batch brief anticipated. For **Q4/Q8**, the paper is genuinely useful: it documents a concrete, staged migration from reward-model-only RL (V1) to a hybrid real-user-feedback + reward-model RL system (V2), with online evidence that mixing the two reward sources balances competing objectives (interaction metrics vs. App Stay Time) better than either alone — a transferable pattern for combining a short-term event head with a longer (but still not multi-day-delayed) engagement signal. Q2, Q5, Q6, Q7 are not addressed: no reciprocity, congestion, incrementality, or slate-level credit assignment appears anywhere in the paper.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2026_RecSys_GenPage_End-to-End-Generative-Homepage-Construction.md](./2026_RecSys_GenPage_End-to-End-Generative-Homepage-Construction.md) | Related Work / Experiments | Names this paper's method (`OneRec-V2`) |
| [2026_arXiv_GenRec_LLM-Backed-Recommendation-Ranker.md](./2026_arXiv_GenRec_LLM-Backed-Recommendation-Ranker.md) | Related Work / Experiments | Names this paper's method (`OneRec-V2`) |

_2 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `OneRec-V2` across all 133 cards._

## Meta Information

- **Authors:** OneRec Team
- **Affiliations:** Kuaishou
- **Venue:** arXiv preprint (arXiv:2508.20900)
- **Year:** 2025
- **Relevance:** Related
- **Priority:** 2
- **nlm:af8ecac6**
