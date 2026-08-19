# Paper Analysis: Generative Sequential Notification Optimization via Multi-Objective Decision Transformers

**Source:** `/Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/2509.02458.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** Generative Sequential Notification Optimization via Multi-Objective Decision Transformers
**Authors:** Borja Ocejo, Ruofan Wang, Ke Liu, Rohit Patra, Haotian Shen, David Liu, Yiwen Yuan, Gokulraj Mohanasundaram, Fedor Borisyuk, Prakruthi Prabhakar (LinkedIn, Mountain View, CA)
**Venue/Year:** arXiv:2509.02458, 2 Sep 2025

**Abstract (paraphrased):** Notifications require sequential decision-making under fatigue constraints and long-horizon objectives. Offline RL methods such as Conservative Q-Learning (CQL) have been deployed for this at scale but face instability, distribution-shift sensitivity, limited reproducibility, and poor explainability. The paper presents a Decision Transformer (DT) based framework that reframes policy learning as return-conditioned supervised sequence modeling. Contributions include a real-world comparison with CQL, a quantile-regression approach to return-to-go conditioning for non-episodic tasks, and a production-ready circular-buffer sequence infrastructure for near-real-time inference. The DT-based approach achieved a +0.72% increase in sessions versus a multi-objective CQL agent by making notifications more relevant, while reducing notification volume and maintaining CTR.

**Key contributions:**
- Reframes notification decision-making (send/drop, which channel) as return-conditioned supervised learning (Decision Transformer) instead of value-based offline RL, motivated by CQL's documented instability and poor explainability at LinkedIn scale.
- A quantile-regression method for state-dependent return-to-go (RTG) prediction — since actual future rewards (e.g., CTR) are not realized before the next action must be chosen — that also allows inference-time "prompting" at any target quantile without retraining.
- A vector (not hand-collapsed) multi-objective reward representation, letting DT learn an implicit functional combination of reward dimensions rather than requiring human-engineered fusion weights.
- A circular-buffer, partial-update sequence-persistence architecture on LinkedIn's Venice key-value store, integrated with the nearline Air Traffic Controller (ATC) service, supporting up to 150K QPS.

**Methodology:** Trajectory τ = (s1, R1, a1, r1, ..., sT, RT, aT, rT); notification decision-making has no natural episode boundary, so it is chunked into finite-horizon episodes of length T+H via a sliding context window (T = historical context length, H = look-ahead horizon). States encode notification-send history, user profile, time since last visit, historical visit rates, and content signals. Actions: send-badge, send-push, or don't-send (or combinations). Rewards r_t ∈ R^{|R|} are a vector spanning predicted notification-value signals, actual observed user visits between states, and adaptive fatigue/volume-penalty terms. A causal transformer decoder predicts return-to-go via quantile regression (pinball loss, M fixed quantile levels, with linear interpolation for arbitrary inference-time quantile prompts) and predicts the next action via cross-entropy loss conditioned on the RTG token and the eligible-action-set embedding.

**Main results:** Offline: best DT policy reaches 96.7% action-prediction accuracy with pinball loss 0.358 for RTG quantile estimation. Online A/B (Table 1, one-week tests, 2% of LinkedIn users): overall DT vs. CQL baseline — Sessions +0.72%, Notification Volume -1.68%, CTR change not statistically significant. A prompt-tuning case study (Figure 4) shows online CTR lift rising from 0% (not significant) at quantile prompt α=0.5 to a peak of 1.24% at α=0.95.

## 2. Experiment Critique

**Design:** A real production replacement of an existing baseline (CQL) with training data collected via a controlled epsilon-greedy rollout of that *same* incumbent policy (avoiding a stale/mismatched logging-policy confound), followed by a sequence of A/B tests that isolate each individual DT enhancement (basic DT, +learned prompts, +longer context) against the same CQL baseline (Table 1). This incremental-ablation-in-production structure is a notable strength versus the other three papers in this batch, none of which decompose their production gains into per-component online contributions this cleanly.

**Statistical validity:** Table 1 explicitly flags "NSS" (not statistically significant) on specific metric/row combinations — a real strength most industry papers omit — but no confidence intervals or p-values are given even for the flagged-significant rows. Table 2/3's ± values are standard deviations over five training random seeds, offline only.

**Online experiments:** Yes — multiple one-week online A/B tests at 2% of LinkedIn's user base, plus a dedicated prompt-tuning sweep (Figure 4) where each point is described as an independent online A/B test.

**Reproducibility:** Proprietary LinkedIn production data and infrastructure (ATC, Venice, Samza); no code or data released. The architecture and losses are specified with substantial mathematical detail (Eqs. 1-6, Figure 1), but key hyperparameters (look-ahead horizon H, discount factor γ, reward-vector dimensionality |R|, number of quantile levels M, loss weight λ) are not numerically disclosed in the source text.

## 3. Industry Contribution

**Deployability:** Fully deployed in LinkedIn production, replacing the existing CQL-based system, served via a purpose-built nearline architecture (ATC + Venice circular buffer) handling 100K QPS average and up to 150K QPS peak — one of the strongest deployment/scale stories in this batch, with explicit migration-from-an-existing-system detail.

**Problems solved:** Documents specific operational pain points with the prior CQL system (training instability, poor cross-run reproducibility, limited explainability, degraded performance as the state-feature space grew) and shows DT resolves them: the paper reports DT maintaining stable training with "more than tenfold" the feature dimensionality that was infeasible with CQL, and over 3x more consistent results across training runs/configurations.

**Engineering cost:** Requires serving a causal-transformer-decoder sequence model per user with variable-length historical context (production settled on context length 4 as an accuracy/serving-cost tradeoff), a purpose-built circular-buffer storage layer in Venice with a partial-update API (Figure 2), decoupled cloud-based model serving with per-tenant isolation, and offline Airflow data-hygiene workflows. This is a substantially heavier infrastructure lift than Papers 1 or 3 in this batch, and involves more elaborate production-serving engineering (nearline sequence persistence at very high QPS) than any other paper here.

## 4. Novelty vs. Prior Work

Positions Decision Transformer (return-conditioned supervised learning) directly against the authors' own prior production system, CQL-based value RL, citing CQL's training instability, distribution-shift sensitivity, reproducibility, and explainability problems as motivation. Novel contributions over the original Decision Transformer (Chen et al., NeurIPS 2021): (1) quantile-regression RTG prediction instead of a manually-set RTG prompt, directly addressing the documented Return-Conditioned Supervised Learning (RCSL) weakness that "arbitrary conditioning values can lead to poor performance" (citing Waypoint Transformer and related RCSL follow-ups), while enabling post-hoc queries at arbitrary target quantiles without retraining; (2) a vector, non-collapsed multi-objective reward representation, letting DT learn an implicit fusion function rather than requiring hand-engineered weights — directly relevant to the project's Q4; (3) the circular-buffer nearline-serving infrastructure, a distinct production-systems contribution. The paper also explicitly cites Pinterest's notification volume-control system (Paper 1 of this batch) as related, non-sequence-model prior notification-optimization work.

## 5. Dataset Availability

| Dataset | Public? | Size | Notes |
|---|---|---|---|
| LinkedIn production notification interaction logs (epsilon-greedy CQL-policy rollout, 1 week) | No — proprietary/internal | 2% of LinkedIn users over one week; 70/30 train/val split | Not released; no public benchmark used |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Value |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Generative Sequential Notification Optimization via Multi-Objective Decision Transformers," Borja Ocejo, Ruofan Wang, Ke Liu, Rohit Patra, Haotian Shen, David Liu, Yiwen Yuan, Gokulraj Mohanasundaram, Fedor Borisyuk, Prakruthi Prabhakar (LinkedIn), arXiv:2509.02458, 2025. URL: https://arxiv.org/abs/2509.02458 |
| 2 | Source type | Industry paper (arXiv preprint, LinkedIn) |
| 3 | Direction | D4 |
| 4 | Problem setting | Sequential, multi-objective notification send/drop decision-making (badge / push / don't-send) at LinkedIn scale, replacing an existing Conservative Q-Learning (CQL) offline-RL production system with a Decision Transformer to improve training stability, reproducibility, and explainability while balancing notification value against user fatigue. |
| 5 | Objective and label definition | No single retention label; a vector reward r_t across multiple objective dimensions (predicted notification value/click-likelihood, actual observed user visits between decision states, adaptive fatigue/volume-penalty signals). Training target is return-to-go R_t = discounted sum of future rewards over a finite look-ahead horizon H, learned via quantile regression rather than a point estimate. Notification decision-making is continuous/infinite-horizon, artificially chunked into fixed-length trajectories via sliding context windows. No explicit censoring treatment for the delayed "actual visits" reward component. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. DT is trained via return-conditioned supervised (imitation-style) learning on logged trajectories from the incumbent CQL policy; it is not framed or evaluated as a causal-effect (uplift) estimator of the send decision. |
| 7 | Model architecture | Decision Transformer — causal transformer decoder over (state, return-to-go, action, reward) tokens; return-to-go predicted via a two-layer MLP producing quantile estimates at M fixed levels (pinball loss), with linear interpolation enabling arbitrary-quantile queries at inference without retraining; action predicted via cross-entropy loss over eligible-action-set-conditioned output. Production context length 4. |
| 8 | Credit assignment | Per-decision-cycle, per-notification-candidate-batch granularity — each state-action step (a send/drop decision at a nearline evaluation cycle) is credited with the return-to-go computed from the multi-objective reward vector over the look-ahead horizon H, including the delayed "actual user visits" component. |
| 9 | Training data and counterfactual handling | Epsilon-greedy exploration data from deploying the existing CQL baseline policy to 2% of LinkedIn users over one week (70/30 train/val split); no explicit counterfactual/causal-inference machinery — DT learns via return-conditioned imitation of the logged, baseline-policy-generated trajectories. |
| 10 | Offline and online evaluation | Offline: three-class action-prediction accuracy (96.7% best policy) and pinball loss (0.358) for RTG quantile regression, plus context-length ablation (Table 2) and state-representation ablation (Table 3). Online: a series of one-week A/B tests (2% of users) against the CQL baseline tracking Sessions, Notification Volume, and CTR (Table 1), decomposed into incremental per-enhancement tests, plus a CTR-prompt-tuning online sweep (Figure 4). |
| 11 | Reported gains | LinkedIn production A/B test (Table 1): overall DT vs. CQL baseline — Sessions +0.72%, Notification Volume -1.68%, CTR change not statistically significant. Prompt-tuning sweep (Figure 4): online CTR lift rises from 0% (not significant) at quantile prompt α=0.5 to a peak of 1.24% at α=0.95. |
| 12 | Applicability to a two-sided dating recommender | The vector (non-collapsed) multi-objective reward design is directly relevant to Q4 — it demonstrates letting a sequence model learn the fusion of short-term event signals and long-term/fatigue signals implicitly, rather than hand-engineering the CTR/CVR-plus-uplift blend the project wants to replace. The quantile-conditioned RTG-prompting mechanism is a concrete answer to obtaining controllable behavior from one unified model without retraining. It does not address reciprocity or congestion, and its per-user sequential-decision framing does not directly map onto ranking a slate of candidate profiles for another user. |
| 13 | Unverified claims | The claims of "more than tenfold" feature-dimensionality increase and ">3x" more consistent training results are the authors' own comparisons against their own prior system, not independently benchmarked against a third-party CQL implementation. Several Table 1 rows are marked NSS but no p-values or confidence intervals are given for the significant rows either. Exact numeric values for H, γ, \|R\|, and M are not disclosed in the source text. |

## Project Relevance

Directly answers **Q4** (vector multi-objective reward, letting the model implicitly learn the short-term/long-term fusion function instead of a hand-engineered blend — precisely the "blend disappears" target design in the project's README) and **Q8** (a fully documented, staged, in-production migration from an existing value-based offline-RL system, CQL, to a sequence-model-based unified policy, with per-enhancement online ablations — arguably the clearest migration-path evidence in this batch). This is also the batch's second direct instance of the volume/fatigue trade-off: Table 1 shows Notification Volume -1.68% alongside Sessions +0.72% — sending fewer notifications while increasing long-term engagement — the paper's own headline result and a direct empirical analogue to the project's success-paradox concern. The paper explicitly cites Paper 1 of this batch (Pinterest) as related prior notification-optimization work, confirming a citation link within the corpus. Low relevance to **Q2** (no user-level delayed-outcome-to-item attribution beyond the standard per-decision RTG mechanism) and **Q7** (no two-sided/reciprocal element); per field 6, this remains a prediction/imitation-learning paper, not an incrementality paper, so it does not answer Q5.

## Papers That Mention This Paper (Reverse Citation Map)

_This paper proposes no distinctively-named method, so no automated reverse-citation match was possible._

## Meta Information

- **Authors:** Borja Ocejo, Ruofan Wang, Ke Liu, Rohit Patra, Haotian Shen, David Liu, Yiwen Yuan, Gokulraj Mohanasundaram, Fedor Borisyuk, Prakruthi Prabhakar
- **Affiliations:** LinkedIn, Mountain View, CA
- **Venue:** arXiv preprint
- **Year:** 2025
- **Relevance:** Core
- **Priority:** 2
- **nlm:a52e5813**
