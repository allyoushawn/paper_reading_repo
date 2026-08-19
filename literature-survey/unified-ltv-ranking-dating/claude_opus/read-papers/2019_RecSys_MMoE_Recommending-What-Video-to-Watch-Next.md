# Paper Analysis: Recommending What Video to Watch Next: A Multitask Ranking System

**Source:** NotebookLM notebook `unified-ltv-ranking-dating` (source_id `a130cd67-9f8e-488b-b844-aa91ba854ef2`), https://dl.acm.org/doi/10.1145/3298689.3346997
**Date analyzed:** 2026-08-16

## 1. Summary

**Title:** Recommending What Video to Watch Next: A Multitask Ranking System
**Authors:** Zhe Zhao, Lichan Hong, Li Wei, Jilin Chen, Aniruddh Nath, Shawn Andrews, Aditee Kumthekar, Maheswaran Sathiamoorthy, Xinyang Yi, Ed Chi (Google, Inc.)
**Venue / Year:** RecSys 2019 (13th ACM Conference on Recommender Systems, Copenhagen, Denmark)

**Abstract (paraphrased):** A large-scale multi-objective ranking system for "what to watch next" on YouTube. The system must handle multiple, sometimes conflicting, ranking objectives and implicit selection bias in user feedback (chiefly position bias) which creates a self-reinforcing feedback loop. The authors extend Multi-gate Mixture-of-Experts (MMoE) for multi-objective learning and add a Wide & Deep-style shallow side-tower to model and remove position bias.

**Key contributions:**
- An end-to-end, pointwise multi-objective ranking system scoring hundreds of candidates in real time.
- An extended MMoE architecture (soft-parameter sharing via shared experts + per-task gating networks) that coordinates representation learning across conflicting engagement and satisfaction objectives, with a 10% gating-network dropout to prevent "expert polarization."
- A Wide & Deep-inspired shallow side-tower that learns and removes position/selection bias without randomized experiments: the side-tower consumes position (crossed with device type) and outputs a bias term added to the main tower's logit; at serving time position is treated as missing.
- Large-scale live validation on YouTube showing gains in both engagement and satisfaction metrics.

**Methodology:** Objectives are split into "engagement" behaviors (clicks — binary cross-entropy; watch time/completion — regression, squared loss) and "satisfaction" behaviors (likes/dismissals — binary cross-entropy; survey ratings — regression). An MMoE layer sits above one shared hidden layer: several expert MLPs are shared, and each task has its own softmax gating network selecting how to blend expert outputs. Final ranking score is a **manually tuned weighted multiplication** of the individual task predictions. The shallow side-tower is trained jointly with the main tower, taking a position×device feature (10% feature dropout during training) and adding its scalar output to the main logit; at serving, position is fixed to missing so the main tower must rank on debiased utility alone.

**Main results:** In live A/B testing on YouTube, MMoE (8 experts, 6.1M multiplications) improved the engagement metric by +0.45% and the satisfaction metric by +3.07% over an equal-complexity Shared-Bottom baseline (which reached only +0.1%/+1.89% over its own smaller-complexity version). The shallow-tower debiasing approach improved live engagement by +0.24%, versus -0.07% for a naive "position as input feature" baseline and +0.01% for an adversarial-loss baseline.

## 2. Experiment Critique

**Design:** Two separate ablations are run — one isolating the MMoE multi-task gain (vs. Shared-Bottom at matched model complexity) and one isolating the position-bias mitigation gain (vs. two other debiasing baselines) — which cleanly separates the paper's two contributions. Both offline (AUC / squared error) and live A/B metrics are reported.

**Statistical validity:** The paper reports live A/B deltas as percentages without confidence intervals or p-values in the excerpted tables, which is a gap given how small some of the reported deltas are (e.g., +0.01% for the adversarial-loss baseline, which is plausibly noise).

**Online experiments:** The paper explicitly and candidly states that offline metrics (AUC, squared error) frequently fail to transfer to live gains, and that this offline/online misalignment pushed the authors toward preferring simpler models that generalize better online — a notable, self-critical methodological point rather than a purely self-promotional one.

**Reproducibility:** No dataset or code is released (YouTube's proprietary logs); the architecture is described in enough mathematical and diagrammatic detail (MMoE gating equations, dropout rates, feature-crossing choices) to reproduce the method on a different platform, but not to reproduce the reported numbers.

**Overall:** The explicit acknowledgment of gating-network polarization (20% of runs under distributed training before the dropout fix) and of offline/online metric misalignment are honest, useful negative-result disclosures rarely seen in industry papers of this scale. The lack of statistical testing on the live deltas is the main weakness.

## 3. Industry Contribution

- **Deployability:** MMoE is specifically engineered for serving-time efficiency — the shared bottleneck hidden layer keeps the expert layer from operating directly on the (much higher-dimensional) input layer, controlling both training and serving cost. Point-wise scoring is chosen explicitly over pairwise/listwise for real-time scalability to score hundreds of candidates per query.
- **Problems solved:** Directly solves two production-recommender problems relevant to this project — (a) combining conflicting objectives via automatic soft parameter sharing rather than hand-built separate models, and (b) removing position/selection bias from implicit-feedback training data without running costly randomized experiments to estimate propensity scores.
- **Engineering cost:** The final score is still a "manually tuned weighted multiplication" of task outputs — the paper solves representation sharing but not the score-fusion weight-tuning problem it describes YouTube as facing. Feature engineering cost is modest (one extra position×device cross feature, plus dropout hyperparameters); the gating-dropout and feature-dropout fixes are cheap, targeted interventions rather than architecture rewrites.
- **Ranking pipeline fit:** Fits directly into a two-stage (candidate generation → ranking) industrial pipeline; the shallow tower adds no serving-time latency beyond the main tower since position is simply fixed to missing at serving.

## 4. Novelty vs. Prior Work

**Claimed novelty:** Extends MMoE (previously validated on smaller-scale, non-recommendation multi-task problems) to a real-time, industrial-scale ranking system with a multimodal feature space, and combines it for the first time (per the authors) with a Wide & Deep-style side-tower for position-bias removal that avoids randomized experiments.

**Prior work it builds on / compares against:**
- Covington et al., "Deep Neural Networks for YouTube Recommendations" (2016) — baseline architecture for candidate generation/ranking on YouTube.
- Ma et al., "Modeling Task Relationships in Multi-task Learning with Multi-gate Mixture-of-Experts" (2018) — the MMoE architecture being extended.
- Cheng et al., "Wide & Deep Learning for Recommender Systems" (2016) — structural inspiration for the main-tower/side-tower split.
- Joachims et al. — foundational position-bias analysis in implicit feedback.
- Wang et al., "Learning to Rank with Selection Bias in Personal Search" (2016) — comparison point for propensity estimation without randomized trials.
- Jacobs et al., "Adaptive Mixtures of Local Experts" (1991) — origin of the Mixture-of-Experts concept.

## 5. Dataset Availability

| Dataset | Type | Size | Public? |
|---|---|---|---|
| YouTube user logs (offline) | Proprietary, real-world implicit feedback | Hundreds of billions of logs/day, trained sequentially in temporal order | Not public |
| YouTube "Up Next" live traffic | Proprietary, online A/B | Live A/B test, scale unspecified beyond "1.9 billion monthly active users" platform | Not public |

## 6. Community Reaction

Not assessed in NotebookLM mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors or company, venue, year, URL | Recommending What Video to Watch Next: A Multitask Ranking System; Zhe Zhao, Lichan Hong, Li Wei, Jilin Chen, Aniruddh Nath, Shawn Andrews, Aditee Kumthekar, Maheswaran Sathiamoorthy, Xinyang Yi, Ed Chi (Google, Inc.); RecSys 2019; https://dl.acm.org/doi/10.1145/3298689.3346997 |
| 2 | Source type | Industry paper (Google/YouTube, peer-reviewed at RecSys) |
| 3 | Direction | D1 |
| 4 | Problem setting | Real-time ranking of a few hundred video candidates per query on YouTube, under multiple competing engagement/satisfaction objectives and implicit position/selection bias in the training logs that creates a feedback loop. |
| 5 | Objective and label definition | Multi-task pointwise prediction of user behaviors, grouped as engagement (clicks — binary cross-entropy; watch time — regression) and satisfaction (likes/dismissals — binary cross-entropy; survey ratings — regression); final score is a manually tuned weighted multiplication of task outputs. No time horizon is defined and no delayed-feedback or censoring handling is addressed — all labels are immediate, single-impression behaviors. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. Explicit quote: "the ranking model predicts the probabilities of user taking actions such as clicks, watches, likes, and dismissals." The side-tower separates *selection-bias propensity* from *user utility*, but this is bias correction, not causal-effect (uplift) estimation. |
| 7 | Model architecture | Extended Wide & Deep model: shared hidden layer feeding an MMoE layer (multiple shared expert MLPs, one softmax gating network per task, 10% gating dropout), plus a shallow side-tower (position × device feature, 10% feature dropout) added to the main tower's logit for bias correction. |
| 8 | Credit assignment | None beyond the single impression: pointwise approach, one prediction per candidate item per query; the paper explicitly does not map any delayed or session-level outcome back to a slate or sequence of impressions. |
| 9 | Training data and counterfactual handling | Hundreds of billions of daily YouTube user logs, trained sequentially in temporal order to track distribution drift. No counterfactual/propensity correction beyond the learned position-bias side-tower, which substitutes for (rather than uses) randomized propensity experiments. |
| 10 | Offline and online evaluation | Offline: AUC for classification tasks, squared error for regression tasks. Online: live A/B testing on YouTube measuring an engagement metric (time spent) and a satisfaction metric (survey ratings), plus serving-time computation cost. The paper explicitly notes offline and online metrics are often misaligned. |
| 11 | Reported gains | Live A/B, MMoE vs. equal-complexity Shared-Bottom: at 6.1M multiplications, engagement +0.45% and satisfaction +3.07% (8 experts), vs. Shared-Bottom's own +0.1%/+1.89% at the same budget. Live A/B, bias mitigation vs. baselines: Shallow Tower engagement +0.24%, vs. Input-Feature baseline -0.07% and Adversarial-Loss baseline +0.01%. |
| 12 | Applicability to a two-sided dating recommender | Low direct applicability: all objectives are same-side, immediate engagement/satisfaction signals with no reciprocity or two-sided mechanism modeled. The MMoE soft-sharing pattern and the position-debiasing side-tower are both reusable engineering components regardless of that gap — MMoE is a plausible backbone for combining a dating app's short-term (like/match) and long-term (retention/revenue) heads. |
| 13 | Unverified claims | The claim that a 20% "gating network polarization" rate is fixed by exactly a 10% dropout rate is reported as an empirical finding for this dataset only, with no ablation over dropout rate shown in the excerpted text. The magnitude of the offline/online metric misalignment is asserted qualitatively ("often observe misalignment") without a quantified correlation figure. |

## Project Relevance

Directly relevant to **Q4** (fixed vs. learned vs. single-head fusion): MMoE is the canonical industry example of *soft parameter sharing* for combining conflicting objectives inside the network, even though the final score fusion across task outputs remains a hand-tuned weighted multiplication — i.e., representation learning is shared/learned, but score combination is not. Also relevant to **Q6** (offline/online evaluation under noisy, sometimes-misaligned metrics) via its explicit discussion of offline-online metric misalignment, and tangentially to **Q2/Q8** since the shallow side-tower's "factorize user utility from a bias/propensity term" pattern is architecturally close to the reasoning a retention/revenue vs. exposure-probability disentanglement would need, even though the paper applies it only to position bias, not to causal exposure effects.

**Low project relevance** for the survey's core retention/revenue objective: all labels are same-session engagement/satisfaction signals with no delayed outcome, no horizon, no censoring, and no reciprocal or two-sided market mechanism (Q3, Q5, Q7 are all unaddressed). Its value to this survey is architectural (MMoE as a candidate backbone, and the bias/utility factorization pattern), not as a template for the retention/revenue label itself.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2020_KDD_MoSE_Multitask-Mixture-Sequential-Experts-Activity-Streams.md](./2020_KDD_MoSE_Multitask-Mixture-Sequential-Experts-Activity-Streams.md) | Related Work / Experiments | Names this paper's method (`MMoE`) |
| [2020_SIGIR_ESM2_Entire-Space-Multi-Task-Post-Click-Behavior-Decomposition.md](./2020_SIGIR_ESM2_Entire-Space-Multi-Task-Post-Click-Behavior-Decomposition.md) | Related Work / Experiments | Names this paper's method (`MMoE`) |
| [2021_KDD_AITM_Sequential-Dependence-Audience-Multi-step-Conversions.md](./2021_KDD_AITM_Sequential-Dependence-Audience-Multi-step-Conversions.md) | Related Work / Experiments | Names this paper's method (`MMoE`) |
| [2022_CIKM_ODMN_Billion-user-Customer-Lifetime-Value-Prediction.md](./2022_CIKM_ODMN_Billion-user-Customer-Lifetime-Value-Prediction.md) | Related Work / Experiments | Names this paper's method (`MMoE`) |
| [2022_SIGIR_ESCM2_Entire-Space-Counterfactual-Multi-Task-Model.md](./2022_SIGIR_ESCM2_Entire-Space-Counterfactual-Multi-Task-Model.md) | Related Work / Experiments | Names this paper's method (`MMoE`) |
| [2023_CIKM_NA_Immersive-Feed-No-More-Clicks-SFV-Ranking.md](./2023_CIKM_NA_Immersive-Feed-No-More-Clicks-SFV-Ranking.md) | Related Work / Experiments | Names this paper's method (`MMoE`) |
| [2024_KDD_LiRank_Industrial-Large-Scale-Ranking-Models-LinkedIn.md](./2024_KDD_LiRank_Industrial-Large-Scale-Ranking-Models-LinkedIn.md) | Related Work / Experiments | Names this paper's method (`MMoE`) |
| [2025_CIKM_MAL_Multi-Attribution-Learning-Conversion-Rate-Prediction.md](./2025_CIKM_MAL_Multi-Attribution-Learning-Conversion-Rate-Prediction.md) | Related Work / Experiments | Names this paper's method (`MMoE`) |
| [2025_WWW_xMTF_Formula-Free-Reinforcement-Learning-Multi-Task-Fusion.md](./2025_WWW_xMTF_Formula-Free-Reinforcement-Learning-Multi-Task-Fusion.md) | Related Work / Experiments | Names this paper's method (`MMoE`) |
| [2026_AAAI_NA_Save-Revisit-Retain-Scalable-Retention-Framework.md](./2026_AAAI_NA_Save-Revisit-Retain-Scalable-Retention-Framework.md) | Related Work / Experiments | Names this paper's method (`MMoE`) |
| [2026_RecSys_FSM-MMoE-VST_Multi-Objective-Ranking-Live-Streaming.md](./2026_RecSys_FSM-MMoE-VST_Multi-Objective-Ranking-Live-Streaming.md) | Related Work / Experiments | Names this paper's method (`MMoE`) |
| [2026_arXiv_MTFM_Scalable-Alignment-free-Foundation-Model-Meituan.md](./2026_arXiv_MTFM_Scalable-Alignment-free-Foundation-Model-Meituan.md) | Related Work / Experiments | Names this paper's method (`MMoE`) |

_12 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `MMoE` across all 133 cards._

## Meta Information

- **Authors:** Zhe Zhao, Lichan Hong, Li Wei, Jilin Chen, Aniruddh Nath, Shawn Andrews, Aditee Kumthekar, Maheswaran Sathiamoorthy, Xinyang Yi, Ed Chi
- **Affiliations:** Google, Inc.
- **Venue:** RecSys 2019 (13th ACM Conference on Recommender Systems)
- **Year:** 2019
- **Relevance:** Core
- **Priority:** 1
- **NotebookLM source:** `nlm:a130cd67-9f8e-488b-b844-aa91ba854ef2`
