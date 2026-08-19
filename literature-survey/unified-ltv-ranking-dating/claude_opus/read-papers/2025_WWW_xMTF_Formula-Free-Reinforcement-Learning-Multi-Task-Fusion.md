# Paper Analysis: xMTF: A Formula-Free Model for Reinforcement-Learning-Based Multi-Task Fusion in Recommender Systems

**Source:** /Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/2504.05669.pdf
**Date analyzed:** 2026-08-17

## 1. Summary

Cao, Zhang, Chen, Zhan, and Wang (Kuaishou Technology / Peking University), "xMTF: A Formula-Free Model for Reinforcement-Learning-Based Multi-Task Fusion in Recommender Systems," WWW '25. Existing RL-based multi-task-fusion (MTF) methods — including the paper's direct predecessor BatchRL-MTF — are "formula-based": they fix a parametric fusion formula (e.g., a weighted sum or weighted log-sum over per-task predictions) and use RL only to tune the small number of coefficients inside that formula, which caps the achievable search space. xMTF removes the fixed formula. Leaning on the Sprecher Representation Theorem, the authors show any suitable monotonic fusion function can be decomposed into a sum of single-variable monotonic functions, one per prediction type. They replace each fixed coefficient with a learnable **Monotonic Fusion Cell (MFC)** — a small per-task MLP that also takes the user state as input, so the fusion function itself becomes personalized (different users get different fusion shapes for the same predictions, shown empirically in Figures 5–6), with monotonicity enforced by an auxiliary pairwise hinge loss rather than by architectural constraint. To make this larger, higher-dimensional search space trainable, xMTF uses a **Two-Stage Hybrid (TSH)** scheme: a low-parameter "outer stage" (a simple 2nd-order function with one scalar coefficient per task) is optimized directly by actor-critic RL against the long-term session reward, while the high-capacity "inner stage" (the actual MFC MLP) is trained by supervised knowledge transfer — a BPR-style ranking-consistency loss against the outer stage's output — rather than by RL directly. This keeps the RL action space small (dimension = number of tasks) while letting the expressive part of the model absorb the RL signal indirectly. Evaluated offline on a KuaiRand-based session simulator and online on a >100M-user Kuaishou short-video platform.

## 2. Experiment Critique

Offline evaluation is entirely within a custom simulator built on the public KuaiRand dataset, with defined session-exit rules — a reasonable substitute for online RL training data but a simulated, not observed, environment, and the simulator's fidelity to real user behavior is not independently validated in the sections read. Results are reported as mean ± std over 20 trials against 8 baseline variants plus 2 ablations, which is solid for a simulator study. Online results (7-day production A/B against UNEX-RL) report relative gains with confidence intervals, and the authors explicitly flag that the like and follow metric changes did not exceed their confidence intervals — a genuine negative/non-significant result stated plainly rather than omitted.

## 3. Industry Contribution

The central practical claim is that xMTF converges within two days when trained continuously online from scratch and has been fully deployed serving over 100 million users, which is a strong deployability signal. The RL action space stays low-dimensional (equal to the number of fused prediction types, K=6 offline), sidestepping the usual industrial complaint about RL-based MTF — training instability from high-dimensional actions — while still expanding the functional search space via the supervised inner stage.

## 4. Novelty vs. Prior Work

This is presented explicitly as the successor to formula-based RL-MTF work, including the batch's already-carded BatchRL-MTF (Zhang et al., KDD 2022) as well as TD3-based and TSCAC-based formula-constrained variants, and CEM as a non-RL, non-personalized formula-search baseline. What changed relative to BatchRL-MTF: BatchRL-MTF (and the other RL-MTF baselines compared here) fix a specific fusion formula (weighted sum, weighted log-sum, or weighted power-product; see the paper's Table 1) and let RL adjust only the coefficients inside it. xMTF instead learns the fusion function itself — a personalized, per-task monotonic transformation — replacing the "formula" with learnable MFCs, and solves the resulting training-difficulty problem via the two-stage RL/supervised split. "Formula-free" specifically means the hand-specified functional form is gone, not that the monotonicity constraint is gone — monotonicity is retained but now enforced via an explicit auxiliary loss instead of by the formula's structure. **Its horizon is not longer than BatchRL-MTF's.** Both use the same reward structure: a discounted (γ=0.9) sum of per-request rewards accumulated only until a user exits the current app session (T = session length in steps). The paper's online metric is reported as "Daily Watch Time," but that is a measurement/reporting cadence on the production platform, not the definition of the RL training objective's horizon — the training reward itself never extends beyond a single session. This paper does not discuss delayed labels, multi-day retention, or any calendar-day horizon.

## 5. Dataset Availability

| Dataset | Public? | Size | Access |
|---|---|---|---|
| KuaiRand (used inside a custom offline session simulator) | Yes — public | 27,285 users, 32,038,725 items | Published dataset (Gao et al., CIKM '22); code for xMTF referenced at github.com/zxcvbnm678122/xMTFwww2025 |
| Kuaishou production short-video platform logs (online deployment) | No — internal industrial | >100M users | Not released |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "xMTF: A Formula-Free Model for Reinforcement-Learning-Based Multi-Task Fusion in Recommender Systems," Yang Cao, Changhao Zhang, Xiaoshuang Chen, Kaiqiao Zhan, Ben Wang — Kuaishou Technology / Peking University; WWW '25 (ACM Web Conference 2025), Sydney, Australia; 2025; https://arxiv.org/abs/2504.05669 |
| 2 | Source type | Industry paper |
| 3 | Direction | D1 |
| 4 | Problem setting | Multi-task fusion (MTF): combining K per-task predictions (CTR, like rate, long-view rate, etc., produced by an upstream MTL model) into a single score for item ranking, using RL to optimize for long-term session satisfaction rather than a fixed formula |
| 5 | Objective and label definition | RL reward = discounted (γ=0.9) sum of per-request rewards, accumulated over steps `t=1..T` where T is the step at which the user exits the current app session; offline evaluation metric is Total Watch Time of a complete simulated session. **This is a session-scoped discount factor, not a genuine multi-day horizon** — no calendar-day window, delay, or censoring is modeled anywhere in the objective, matching the same limitation identified in its predecessor BatchRL-MTF. Online business reporting uses "Daily Watch Time" as an aggregation/measurement cadence, but the underlying training reward horizon remains within-session. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. |
| 7 | Model architecture | Per-task Monotonic Fusion Cells (MFCs) — small MLPs conditioned on user state — replace a fixed fusion formula; trained via Two-Stage Hybrid (TSH) learning: a low-dimensional actor-critic RL "outer stage" optimizes long-term session reward directly, and a high-capacity supervised "inner stage" (the actual MFC) learns via a BPR-style knowledge-transfer loss from the outer stage's induced ranking. This is a **learned, per-task fusion function** (not a fixed hand-tuned formula, and not a single unified value head) — the clearest "learned fusion" data point in this batch for the Q4 taxonomy. Per-task predictions themselves come from an off-the-shelf MMoE model, which is explicitly out of scope for this paper's contribution. |
| 8 | Credit assignment | Item-level scoring (each candidate item i in a request gets its own fused score `z_i` from its own K predictions), but the long-term reward signal used to train the RL outer stage is a **session-level** aggregate (total watch time across the session) applied via standard actor-critic temporal-difference updates to shared fusion parameters — there is no per-item attribution mechanism beyond the MDP's own credit-assignment dynamics (contrast with Paper 1's explicit multi-dimensional attribution). |
| 9 | Training data and counterfactual handling | Offline: a custom simulator built on the public KuaiRand dataset (27,285 users, 32M items) with defined session-exit rules, replayed via a replay buffer. Online: continuous streaming retraining from production session logs on a >100M-user platform. No counterfactual or causal correction is applied anywhere. |
| 10 | Offline and online evaluation | Offline: mean ± std Total Watch Time per simulated session over 20 trials, against CEM, TD3, BatchRL-MTF, TSCAC, and MR-MPL baselines (2 formula variants each) plus 2 ablations (xMTF without outer stage, xMTF without inner stage). Online: 7-consecutive-day production A/B against UNEX-RL (the most recent production baseline), reporting relative gain with 95% confidence intervals on Daily Watch Time, Play Counts, Comment, Share, Like, Follow. |
| 11 | Reported gains | Offline (KuaiRand simulator, Total Watch Time in seconds): xMTF 1279.7±12.9 vs. best baseline MR-MPL-2 1189.6±12.3 and BatchRL-MTF-2 1185.4±12.6; ablation xMTF-without-inner-stage (degenerating to a fixed formula-based MTF) drops to 1106.3±11.2, and xMTF-without-outer-stage drops to 1092.8±9.1. Online (Kuaishou production, 7-day A/B vs. UNEX-RL): Daily Watch Time +0.833% [-0.11%,0.11%], Play Counts +0.583% [-0.14%,0.14%], Comment +2.391% [-1.26%,1.26%], Share +2.205% [-0.81%,0.81%]; Like and Follow changes did not exceed their confidence intervals (stated as non-significant by the authors). |
| 12 | Applicability to a two-sided dating recommender | The core mechanism — replacing a fixed fusion formula with a personalized, learned, monotonic per-task fusion function trained via a low-dimensional RL outer stage plus a supervised inner stage — is a directly transferable answer to Q4's "learned fusion" category. Its complete absence of a multi-day horizon (session-only reward) means it does not, by itself, solve the project's delayed-label (7–30 day retention) problem; it would need to be paired with a delayed-label construction like Paper 2's before it fits the project's horizon requirement. |
| 13 | Unverified claims | The choice of RL algorithm family (actor-critic) is stated as "orthogonal to the contribution" and not otherwise justified or ablated against alternatives (DDPG, SAC) beyond citation. The claim that xMTF "converges within two days" online is asserted without showing the convergence curve or criterion in the sections read. |

## Project Relevance

Speaks most directly to **Q4** — this is the batch's clearest example of *learned* fusion (as opposed to Paper 1 and Paper 2's fixed hand-tuned weights), and its explicit contrast with formula-based RL-MTF predecessors (BatchRL-MTF, TD3, TSCAC) gives the taxonomy real texture. Also relevant to **Q1** in a limited sense (RL directly optimizes a long-term-within-session reward rather than a short-term click/like proxy), but **the horizon is not long-term by the project's definition** — no calendar-day window, so it does not speak to Q3. Does not address incrementality (Q5), two-sided/reciprocal markets (Q7), or credit assignment beyond standard MDP mechanics (Q2 only weakly). No staged migration narrative (Q8).

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `xMTF`._

## Meta Information

- **Authors:** Yang Cao, Changhao Zhang, Xiaoshuang Chen, Kaiqiao Zhan, Ben Wang
- **Affiliations:** Kuaishou Technology (Beijing, China); Peking University (Beijing, China)
- **Venue:** WWW '25 (ACM Web Conference 2025), Sydney, NSW, Australia
- **Year:** 2025
- **Relevance:** Core
- **Priority:** 3
- **nlm:da625059**
