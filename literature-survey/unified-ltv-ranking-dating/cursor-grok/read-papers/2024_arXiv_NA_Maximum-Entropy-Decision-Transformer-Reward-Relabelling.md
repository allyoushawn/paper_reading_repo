# Paper Analysis: Maximum-Entropy Regularized Decision Transformer with Reward Relabelling for Dynamic Recommendation

**Source:** https://arxiv.org/abs/2406.00725
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** Maximum-Entropy Regularized Decision Transformer with Reward Relabelling for Dynamic Recommendation
- **authors or company:** Xiaocong Chen, Siyu Wang, Lina Yao (Data61 CSIRO / UNSW)
- **venue:** KDD (arXiv 2406.00725)
- **year:** 2024
- **URL:** https://arxiv.org/abs/2406.00725
- **source type:** academic
- **direction:** D2
- **problem setting:** Offline RL for recommendation using a Decision Transformer backbone; addresses trajectory "stitching" (combining sub-optimal offline segments) and insufficient exploration during online fine-tuning on converted static rating/click logs plus VirtualTaobao simulator.
- **objective and label definition:** Binary click reward per interaction—ratings above 75% of max scale count as positive; return-to-go (RTG) = sum of future rewards conditions the DT; no multi-day retention or revenue horizon defined.
- **prediction or incrementality:** Prediction/policy optimization for expected discounted click reward; no causal incrementality or treatment-effect framing.
- **model architecture:** Causal Decision Transformer on (RTG, state, action) token triples with context window K; stochastic Gaussian policy; max-entropy exploration via Lagrangian-relaxed sequence-level entropy constraint (Eq. 5–8); RTG relabeling (Algorithm 1) uses CQL-trained Q-function lower bound, selectively replacing RTG when Q̂ exceeds observed RTG and backward-propagating through trajectory.
- **credit assignment:** RTG relabeling propagates revised return estimates backward across trajectory timesteps using CQL Q-values—credit from other trajectories sharing states, but for click-level reward only, not delayed retention/revenue.
- **training data and counterfactual handling:** Offline (state, action, reward) tuples from six public datasets; top-N highest-return trajectories seeded into replay buffer refreshed with online rollouts (Algorithm 2); CQL provides Q lower bound under distributional shift—offline/counterfactual correction, not causal treatment inference.
- **offline and online evaluation:** Offline: Recall, Precision, nDCG on six datasets vs DDPG, SAC, TD3, DT, DT4Rec, CDT4Rec (Table 1, 95% CI). Online: CTR in VirtualTaobao over 100,000 timesteps (Figure 3); ablations EDT4Rec-E (no exploration) and EDT4Rec-R (no relabeling) in Figure 4.
- **reported gains:** KuaiRand-1k: EDT4Rec Recall 31.256±0.241% vs CDT4Rec 30.322±0.208%; similar margins on LibraryThing, Book-Crossing, GoodReads, MovieLens-20M, Netflix (Table 1). VirtualTaobao: higher average CTR with tighter variance than DT/DT4Rec/CDT4Rec (Figure 3a; no single summary percentage in text).
- **applicability note for a two-sided dating recommender:** RTG-relabeling / CQL backward propagation is a transferable credit-assignment pattern if re-derived against multi-week retention/revenue reward rather than per-click binary feedback.
- **applicability note for a two-sided dating recommender:** Reward is generic click with no reciprocity, congestion, or two-sided market structure—low direct dating applicability beyond the credit-propagation idea.
- **unverified claims:** none

## 1. Summary

**Title:** Maximum-Entropy Regularized Decision Transformer with Reward Relabelling for Dynamic Recommendation (EDT4Rec)
**Authors:** Xiaocong Chen, Siyu Wang, Lina Yao
**Abstract:** Identifies DT-based RS weaknesses—no stitching of sub-optimal trajectories and poor online exploration—and proposes max-entropy sequence-level exploration plus CQL-guided RTG relabeling, validated on six offline datasets and VirtualTaobao.

**Key contributions:**
- Max-entropy enhanced exploration adapted from SAC at DT sequence level.
- RTG relabeling with CQL lower-bound Q-values for trajectory stitching.
- Comprehensive experiments vs DT4Rec and CDT4Rec baselines.

**Methodology:** EDT4Rec extends causal DT with stochastic policy, entropy constraint, and two-pass RTG relabeling (Algorithm 1–2).

**Main results:** Best offline metrics across six datasets; online VirtualTaobao CTR advantage over DT-family baselines.

## 2. Experiment Critique

**Design:** Six diverse offline datasets plus simulator; ablations isolate exploration vs relabeling components.

**Statistical validity:** 95% confidence intervals in Table 1; VirtualTaobao comparison by figure without formal significance tests.

**Online experiments (if any):** VirtualTaobao simulator only—no real-platform deployment.

**Reproducibility:** Public datasets listed; reward conversion protocol follows prior DT4Rec/CDT4Rec work.

**Overall:** Solid offline-RL methodology paper; click-only reward limits retention/LTV relevance.

## 3. Industry Contribution

**Deployability:** Research-stage offline RL; no production claims.

**Problems solved:** DT stitching and online fine-tuning exploration for sparse offline recommendation trajectories.

**Engineering cost:** Transformer + CQL pretraining + online replay buffer maintenance.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Sequence-level max-entropy exploration and CQL-based RTG relabeling for DT recommenders.

**Prior work comparison:** Extends DT4Rec (retention-focused DT) and CDT4Rec (causal DT); baselines include DDPG, SAC, TD3.

**Verification:** Table 1 and ablation Figure 4 support both components; retention claims of baselines not tested on retention outcomes.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| KuaiRand-1k | Public | Yes | Video sequential logs |
| LibraryThing, MovieLens-20M, GoodReads, Netflix, Book-Crossing | Public | Yes | Converted to binary-click RL trajectories |
| VirtualTaobao | Public simulator | Yes | Online CTR evaluation |

**Offline experiment reproducibility:** Public datasets; conversion to RL environments documented.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** Optimizes click-based return-to-go, not retention/LTV/revenue ranking objectives.

**(2) Credit assignment:** RTG relabeling with CQL is the core backward credit mechanism—applicable in principle to delayed outcomes if reward redefined.

**(3) Label and horizon definitions:** Binary click per interaction; 75% rating threshold; no D1/D7 retention horizon.

**(4) Short-term + long-term heads:** Single DT policy conditioned on RTG—not multi-head short/long fusion.

**(5) Prediction vs incrementality:** Policy learning, not uplift/incremental exposure effect.

**(6) Offline and online evaluation:** Offline ranking metrics + simulator CTR; no delayed retention or two-sided interference evaluation.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Not addressed.

**(8) Migration path from CTR-like model to unified long-term model:** Not specified; offline RL fine-tuning path from logged trajectories.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Xiaocong Chen, Siyu Wang, Lina Yao
**Affiliations:** Data61, CSIRO; University of New South Wales
**Venue:** KDD 2024
**Year:** 2024
**PDF:** https://arxiv.org/pdf/2406.00725.pdf
**Relevance:** Related
**Priority:** 3
