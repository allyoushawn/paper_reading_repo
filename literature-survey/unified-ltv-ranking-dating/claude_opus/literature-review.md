---
title: Literature Review — Unified Retention/Revenue Ranking Model for a Dating Recommender
summary: Taxonomy and category-wise review of 133 references, organized around the project's decision points. Produced by the claude_opus run.
topics: [literature-survey, unified-model, LTV, retention, revenue, reciprocal-recommendation, two-sided-marketplace, delayed-feedback, uplift]
status: active
updated: 2026-08-17
---

# Literature Review — Unified Retention/Revenue Ranking Model for a Dating Recommender

**Corpus:** 133 papers, cards in [`read-papers/`](./read-papers/).
**Run:** `claude_opus`. **Project Context:** [`../README.md`](../README.md).

## How this taxonomy is organized

The categories below are **the project's decision points**, not academic subfields. A team migrating
from "CTR/CVR model + uplift blend" to one unified retention/revenue ranker has to answer a specific
sequence of questions, and each category answers one of them. Papers appear in the category matching
the question they help decide, which sometimes differs from the direction they were discovered under.

Read the categories in order — they follow the order the decisions have to be made.

---

## The one-paragraph answer

**Industry has solved the fusion problem and has not solved the objective problem.** Production
rankers at Meta, Kuaishou, Meituan and Momo optimize short-horizon objectives; Netflix reaches a
long-term objective only indirectly, by reweighting short-term labels. Separately, three research
literatures each hold one piece the project needs — long-horizon RL objectives, incrementality inside
a ranker, and reciprocity — and no paper holds all three. The nearest miss is precisely identifiable:
**CRRS (KDD 2024)** already does reciprocity *and* incrementality with a bilateral treatment, and
lacks only a long-horizon outcome. That gap is one well-defined extension, not an open research
programme.

---

## Category 1 — Making long-term value the ranking objective (12 papers)

The question: *can retention or revenue be the training objective at all, and who has done it?*

The honest answer is that the published production systems mostly have not. Meta's Instagram Explore
post defines a **"value model"** that is a fixed-weight linear fusion over short-term engagement
probabilities, with **no horizon or delay handling stated anywhere** — it is widely cited as
precedent for unified long-term ranking and does not do that. LinkedIn's LiRank is a systems and
architecture paper. The clearest genuinely long-horizon industrial framings are Pinterest's
**Save, Revisit, Retain** (1-day and 7-day revisit labels) and the **long-term value prediction
framework in video ranking**.

- [Scaling the Instagram Explore Recommendations System (Meta, 2023)](./read-papers/2023_Blog_VM_Scaling-Instagram-Explore-Recommendations.md) — the "value model", fixed weights, no horizon
- [Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention (Pinterest)](./read-papers/2026_AAAI_NA_Save-Revisit-Retain-Scalable-Retention-Framework.md) — 1d/7d revisit labels
- [A Long-term Value Prediction Framework in Video Ranking](./read-papers/2026_WWW_PDQ_Long-term-Value-Prediction-Framework-Video-Ranking.md)
- [LiRank: Industrial Large Scale Ranking Models at LinkedIn (KDD 2024)](./read-papers/2024_KDD_LiRank_Industrial-Large-Scale-Ranking-Models-LinkedIn.md)
- [Trinity: Syncretizing Multi-/Long-Tail/Long-Term Interests (ByteDance, KDD 2024)](./read-papers/2024_KDD_Trinity_Syncretizing-Multi-Long-Tail-Long-Term-Interests.md)
- [UniROM: One Model to Rank Them All (Meituan, 2025)](./read-papers/2025_arXiv_UniROM_One-Model-to-Rank-Them-All.md)
- [MTFM: Alignment-free Foundation Model (Meituan, 2026)](./read-papers/2026_arXiv_MTFM_Scalable-Alignment-free-Foundation-Model-Meituan.md)
- [Multi-Objective Ranking for Live-Streaming: Fresh vs Delayed Signals](./read-papers/2026_RecSys_FSM-MMoE-VST_Multi-Objective-Ranking-Live-Streaming.md) — **segment-aware targeting, fresh/delayed split**
- [Long-term User Engagement via Model-agnostic Downstream Rewards](./read-papers/2026_arXiv_NA_Long-term-Engagement-Downstream-Rewards-Learning.md)
- [A Pareto-Efficient Algorithm for Multiple Objective Optimization (Alibaba, RecSys 2019)](./read-papers/2019_RecSys_PE-LTR_Pareto-Efficient-Multi-Objective-Recommendation.md)
- [Multi-Objective Ranking Optimization via Stochastic Label Aggregation (Amazon, WWW 2020)](./read-papers/2020_WWW_NA_Multi-Objective-Ranking-Stochastic-Label-Aggregation.md)
- [Recommender System: Ranking Algorithms and Training Architectures (Alibaba Cloud)](./read-papers/2020_Blog_NA_Ranking-Algorithms-Training-Architectures.md)

**Decision this supports:** whether to expect a template. There is none for a deployed
retention-objective ranker; expect to build rather than adopt.

---

## Category 2 — Learning the fusion rather than hand-tuning it (6 papers)

The question: *if we keep separate heads, can the combination be learned instead of tuned?*

**This is the best-solved problem in the entire survey.** Tencent's BatchRL-MTF replaced grid-searched
fusion weights with a Batch-RL policy and reported +2.55% app dwell time and +9.65% positive-interaction
rate in a month-long A/B at hundreds of millions of users. Its successor xMTF removed the hand-specified
fusion formula entirely. Airbnb distils multiple objectives into one ranker. Pinterest's PRL-PUTS runs
Pareto sweeping in production.

- [Multi-Task Fusion via RL for Long-Term User Satisfaction (Tencent, KDD 2022)](./read-papers/2022_KDD_BatchRL-MTF_Multi-Task-Fusion-Reinforcement-Learning.md) — **brief seed; closest architectural template**
- [xMTF: Formula-Free RL-Based Multi-Task Fusion (Kuaishou)](./read-papers/2025_WWW_xMTF_Formula-Free-Reinforcement-Learning-Multi-Task-Fusion.md)
- [Multi-objective Learning to Rank by Model Distillation (Airbnb, KDD 2024)](./read-papers/2024_KDD_MO-LTR-MD_Multi-Objective-Learning-to-Rank-Model-Distillation.md)
- [A Production-Ready RL Framework with Pareto Sweeping (Pinterest)](./read-papers/2026_arXiv_PRL-PUTS_Production-Ready-RL-Pareto-Sweeping-Pinterest.md)
- [Recommending What Video to Watch Next (Google/YouTube, RecSys 2019)](./read-papers/2019_RecSys_MMoE_Recommending-What-Video-to-Watch-Next.md)
- [MoSE: Multitask Mixture of Sequential Experts (Google, KDD 2020)](./read-papers/2020_KDD_MoSE_Multitask-Mixture-Sequential-Experts-Activity-Streams.md)

**The catch that matters.** BatchRL-MTF's reward is **session-scoped with a discount factor of 0.95**
and it does **no delayed-label modelling**. Learned fusion is solved; learned fusion *over a 7-to-30
day outcome* is not demonstrated anywhere in this corpus.

---

## Category 3 — Retention as an RL reward, and its evidence problem (12 papers)

The question: *can a policy be trained directly on returning users?*

Yes, in research settings. Kuaishou's RLUR is the canonical case with a genuine billion-user online
A/B. GFN4Retention uses generative flow networks for delayed-return credit. Two-Stage Constrained
Actor-Critic handles competing constraints.

- [Reinforcing User Retention in a Billion Scale Short Video Recommender (Kuaishou, WWW 2023)](./read-papers/2023_WWW_RLUR_Reinforcing-User-Retention-Billion-Scale-Video.md) — **brief seed; online A/B**
- [Modeling User Retention through Generative Flow Networks (Kuaishou, KDD 2024)](./read-papers/2024_KDD_GFN4Retention_Modeling-User-Retention-Generative-Flow-Networks.md)
- [Two-Stage Constrained Actor-Critic (Kuaishou, WWW 2023)](./read-papers/2023_WWW_TSCAC_Two-Stage-Constrained-Actor-Critic-Short-Video.md)
- [AURO: RL for Adaptive User Retention Optimization (WWW 2025)](./read-papers/2025_WWW_AURO_Reinforcement-Learning-Adaptive-User-Retention.md)
- [Stratified Expert Cloning for Retention-Aware Recommendation](./read-papers/2025_CIKM_SEC_Stratified-Expert-Cloning-Retention-Aware-Recommendation.md)
- [Returning is Believing: Optimizing Long-term User Engagement (CIKM 2017)](./read-papers/2017_CIKM_r2Bandit_Returning-Is-Believing-Long-Term-Engagement.md)
- [Optimizing Audio Recommendations for the Long-Term (Spotify, 2023)](./read-papers/2023_arXiv_NA_Optimizing-Audio-Recommendations-Long-Term-RL.md) — **brief seed**
- [Top-K Off-Policy Correction for a REINFORCE Recommender (Google, WSDM 2019)](./read-papers/2019_WSDM_NA_Top-K-Off-Policy-Correction-REINFORCE-Recommender.md) — **brief seed**
- [User Response Models to Improve a REINFORCE Recommender (Google, WSDM 2021)](./read-papers/2021_WSDM_URL_User-Response-Models-REINFORCE-Recommender.md)
- [DRN: Deep RL Framework for News Recommendation (Microsoft, WWW 2018)](./read-papers/2018_WWW_DRN_Deep-Reinforcement-Learning-News-Recommendation.md)
- [Value-aware Recommendation via Reinforcement Profit Maximization (Alibaba, WWW 2019)](./read-papers/2019_WWW_Value-based-RL_Reinforced-Profit-Maximization-Ecommerce.md)
- [EDT4Rec: Max-Entropy Decision Transformer with Reward Relabelling](./read-papers/2024_KDD_EDT4Rec_Max-Entropy-Decision-Transformer-Reward-Relabelling.md)

### ⚠ Read this before citing any number from this category

**[KuaiSim](./read-papers/2023_NeurIPS_KuaiSim_Comprehensive-Simulator-Recommender-Systems.md), the
simulator several of these papers evaluate on, generates retention circularly.** Its retention signal
is a draw from `Geometric(p_ret)` where `p_ret` rises with the immediate reward the policy is
optimizing. **A policy that raises immediate reward mechanically raises its own simulated retention**,
regardless of whether that holds for real users.

The simulator encodes "immediate engagement causes retention" — the exact assumption the project's
success paradox calls into question. **Separate online-A/B evidence from simulator evidence and never
compare the two.** RLUR carries a real online result; several others do not.

---

## Category 4 — What to train on: long-horizon labels and losses (9 papers)

The question: *what is the label, over what window, and what loss?*

**ZILN is the single most transferable component found.** It models a zero-inflated, heavy-tailed
monetary outcome — most users spend nothing, a few spend heavily — which is exactly the shape of
dating-app revenue. It is cited by six other papers in this corpus and appears in three distinct
roles, including **inside RERUM's uplift ranking objective**.

- [A Deep Probabilistic Model for Customer Lifetime Value (Google, 2019 — ZILN)](./read-papers/2019_arXiv_ZILN_Deep-Probabilistic-Model-Customer-Lifetime-Value.md) — **brief seed; recommended revenue-head loss**
- [Billion-user Customer Lifetime Value Prediction (Kuaishou, CIKM 2022)](./read-papers/2022_CIKM_ODMN_Billion-user-Customer-Lifetime-Value-Prediction.md) — **brief seed**
- [PinnerFormer: Sequence Modeling for User Representation (Pinterest, KDD 2022)](./read-papers/2022_KDD_PinnerFormer_Sequence-Modeling-User-Representation-Pinterest.md) — **brief seed; 28-day dense all-action label**
- [CC-OR-Net: Unified LTV Prediction through Structural Decoupling](./read-papers/2026_WWW_CC-OR-Net_Unified-Framework-LTV-Prediction-Structural-Decoupling.md)
- [GRePO-LTV: Mini-Game Lifetime Value Prediction (WeChat)](./read-papers/2025_arXiv_GRePO-LTV_Mini-Game-Lifetime-Value-Prediction-WeChat.md)
- [OCARM: Distilling Post-Conversion Content for User Retention](./read-papers/2026_arXiv_OCARM_Break-Inaccessible-Boundary-Post-Conversion-Retention.md) — **models retention when post-conversion content is invisible: the post-match blind spot**
- [Notification Volume Control and Optimization at Pinterest (KDD 2018)](./read-papers/2018_KDD_NA_Notification-Volume-Control-Optimization-Pinterest.md) — **brief seed; fewer interventions raised long-term engagement**
- [A Sleeping, Recovering Bandit for Recurring Notifications (Duolingo, KDD 2020)](./read-papers/2020_KDD_RDSA_Sleeping-Recovering-Bandit-Recurring-Notifications.md) — **brief seed**
- [Generative Sequential Notification Optimization (2025)](./read-papers/2025_arXiv_DT_Generative-Sequential-Notification-Multi-Objective.md)

**Horizon precedents found:** 28 days (PinnerFormer dense all-action), 1 and 7 days (Pinterest
Save-Revisit-Retain), 10-day geometric cap (KuaiSim), 2–4 weeks (RERUM revenue).

**The volume/fatigue result matters for the success paradox.** Both notification papers find that
*fewer* interventions can raise long-term engagement — the direct analogue of a good match ending a
user's tenure.

---

## Category 5 — Acting before the horizon: surrogates and proxy metrics (12 papers)

The question: *how do we iterate without waiting 30 days per experiment?*

- [The Surrogate Index (Athey, Chetty, Imbens, Kang)](./read-papers/2019_arXiv_SurrogateIndex_Combining-Short-Term-Proxies-Long-Term-Effects.md) — **brief seed; foundation**
- [Evaluating the Surrogate Index Using 200 A/B Tests at Netflix](./read-papers/2023_arXiv_AutoSurrogate_Surrogate-Index-200-AB-Tests-Netflix.md) — **the empirical verdict**
- [Choosing a Proxy Metric from Past Experiments (Google, KDD 2024)](./read-papers/2024_KDD_NA_Choosing-Proxy-Metric-Past-Experiments.md) — **brief seed**
- [Pareto Optimal Proxy Metrics (Google, 2023)](./read-papers/2023_arXiv_ParetoProxy_Pareto-Optimal-Proxy-Metrics.md)
- [Impatient Bandits: Optimizing for the Long-Term Without Delay (Spotify, KDD 2023)](./read-papers/2023_KDD_ImpatientBandit_Optimizing-Recommendations-Long-Term-Without-Delay.md) — **brief seed**
- [Long-term Off-Policy Evaluation and Learning (WWW 2024)](./read-papers/2024_WWW_LOPE_Long-Term-Off-Policy-Evaluation-Learning.md) — **brief seed**
- [Evaluating for the Long Term: Learnings from Industry (~15 firms)](./read-papers/2026_arXiv_NA_Evaluating-Long-Term-Learnings-Industry.md) — **brief seed**
- [PROXIMA: Proxy Metric Validation with Segment-Level Fragility](./read-papers/2026_arXiv_PROXIMA_Proxy-Metric-Validation-Segment-Level-Fragility.md) — **segment fragility: revenue behaviour differs sharply by segment**
- [The Dynamically Adjusted Surrogate Index](./read-papers/2021_arXiv_NA_Dynamically-Adjusted-Surrogate-Index.md) — **for novel treatments with no history**
- [The Proximal Surrogate Index: Unobserved Confounding](./read-papers/2026_arXiv_ProximalSurrogateIndex_Long-Term-Effects-Unobserved-Confounding.md)
- [Learning the Covariance of Treatment Effects Across Many Weak Experiments (Netflix, KDD 2024)](./read-papers/2024_KDD_NA_Covariance-Treatment-Effects-Weak-Experiments.md)
- [Estimating Long-Term Outcome of Algorithms (Spotify Research)](./read-papers/2024_Blog_LOPE_Estimating-Long-Term-Outcome-Algorithms.md)

### The Netflix result, stated precisely

A 14-day surrogate versus 63-day direct measurement across 200 tests and 1,098 arms:
**~95% overall agreement**, but on launch decisions specifically, **79% precision and 65% recall**,
with **zero false launches** on tests that were significantly negative at 63 days.

**The 95% figure misleads.** On the decision that matters, the surrogate **misses about a third of
genuinely good changes**. It is *safe but lossy* — it will not ship harm, but it quietly discards
wins. Netflix estimates ~53% more experiments are needed to compensate, an illustrative figure
resting on untested assumptions, not a validated operational result.

**Every paper in this category operates at the experiment level, not the item level.** They validate
ship decisions, not per-impression ranking scores.

---

## Category 6 — Delayed feedback: training on labels that have not arrived (18 papers)

The question: *how do we train when a label may still be pending?*

This is the corpus's largest and most mature category. **DFM (Chapelle, Criteo, KDD 2014)** is the
root, with ten-plus descendants, all sharing the insight that **a not-yet-converted sample is not a
negative sample** — exactly the structure of an unresolved 30-day retention label.

- [Modeling Delayed Feedback in Display Advertising (Criteo, KDD 2014)](./read-papers/2014_KDD_DFM_Modeling-Delayed-Feedback-Display-Advertising.md) — **brief seed; lineage root**
- [ES-DFM: Elapsed-Time Sampling (Alibaba, AAAI 2021)](./read-papers/2021_AAAI_ESDFM_Capturing-Delayed-Feedback-Elapsed-Time-Sampling.md) — **brief seed**
- [DEFER: Real Negatives Matter (Alibaba, KDD 2021)](./read-papers/2021_arXiv_DEFER_Real-Negatives-Matter-Continuous-Training.md) — **brief seed**
- [DEFUSE: Asymptotically Unbiased Estimation via Label Correction (Alibaba, WWW 2022)](./read-papers/2022_WWW_DEFUSE_Asymptotically-Unbiased-Estimation-Label-Correction.md)
- [FSIW: Feedback Shift Correction (WWW 2020)](./read-papers/2020_WWW_FSIW_Feedback-Shift-Correction-Delayed-Feedback.md)
- [FNW/FNC: Addressing Delayed Feedback for Continuous Training (Twitter, RecSys 2019)](./read-papers/2019_RecSys_FNW-FNC_Addressing-Delayed-Feedback-Continuous-Training.md)
- [Handling Many Conversions per Click (Google, 2021)](./read-papers/2021_arXiv_NA_Many-Conversions-Per-Click-Delayed-Feedback.md) — **multiple valued events from one exposure: the project's exact shape**
- [NBDFM: Negative Binomial Regression for Multiple Conversions (AdKDD 2020)](./read-papers/2020_AdKDD_NBDFM_Negative-Binomial-Regression-Multiple-Conversions.md)
- [CBDF: Counterfactual Reward Modification, Streaming (Tencent, SIGIR 2021)](./read-papers/2021_SIGIR_CBDF_Counterfactual-Reward-Modification-Streaming-Delayed-Feedback.md)
- [GDFM: Generalized Delayed Feedback with Post-Click Information (NeurIPS 2022)](./read-papers/2022_NeurIPS_GDFM_Generalized-Delayed-Feedback-Model-Post-Click-Information.md)
- [ESDF: Delayed Feedback for Entire Space CVR (Alibaba, AAAI 2021)](./read-papers/2021_AAAI_ESDF_Delayed-Feedback-Modeling-Entire-Space.md)
- [NoDeF: Nonparametric Delayed Feedback (2018)](./read-papers/2018_arXiv_NoDeF_Nonparametric-Delayed-Feedback-Model-Conversion.md)
- [TS-DL: Attention Model for CVR with Delayed Feedback (JD, IJCAI 2020)](./read-papers/2020_IJCAI_TS-DL_Attention-Model-CVR-Delayed-Feedback.md)
- [DLA-DF: Dual Learning for Delayed Conversions (SIGIR 2020)](./read-papers/2020_SIGIR_DLA-DF_Dual-Learning-Algorithm-Delayed-Conversions.md)
- [IF-DFM: Delayed Feedback with Influence Functions (AAAI 2026)](./read-papers/2026_AAAI_IF-DFM_Delayed-Feedback-Modeling-Influence-Functions.md)
- [MISS: Multi-Interval Screening and Synthesizing (AAAI 2024)](./read-papers/2024_AAAI_MISS_Online-Conversion-Rate-Prediction-Multi-Interval-Screening.md)
- [CM-DCM: Counterfactual Multi-task for Delayed Conversion (SIGIR 2026)](./read-papers/2026_SIGIR_CM-DCM_Counterfactual-Multi-task-Learning-Delayed-Conversion.md)
- [Learning Classifiers from Only Positive and Unlabeled Data (KDD 2008)](./read-papers/2008_KDD_NA_Learning-Classifiers-Positive-Unlabeled-Data.md) — foundational

**The scale mismatch, stated plainly.** This literature operates at **hours to days**. The project
needs **7–30 days for retention and multiple weeks for revenue**. The *framing* transfers directly.
The exponential-delay assumptions and the calibration timescales do not, and no paper here validates
at a multi-week horizon.

---

## Category 7 — Cascades with rare terminal events (9 papers)

The question: *how do we train a chain where later stages are rare and only observed after earlier ones?*

This is the project's structure exactly: impression → like → match → conversation → subscription.

- [ESMM: Entire Space Multi-Task Model (Alibaba, SIGIR 2018)](./read-papers/2018_SIGIR_ESMM_Entire-Space-Multi-Task-Model-Post-Click-Conversion.md) — **brief seed — but provably biased**
- [Multi-IPW / Multi-DR: Causal Debiasing of Post-Click CVR (Alibaba, WWW 2020)](./read-papers/2020_WWW_MultiDR_Causal-Debiasing-Post-Click-CVR-Multi-task.md) — **proves ESMM's bias**
- [ESCM2: Entire Space Counterfactual Multi-Task Model (Alibaba, SIGIR 2022)](./read-papers/2022_SIGIR_ESCM2_Entire-Space-Counterfactual-Multi-Task-Model.md) — **brief seed; adopt this variant**
- [AITM: Sequential Dependence among Multi-step Conversions (Meituan, KDD 2021)](./read-papers/2021_KDD_AITM_Sequential-Dependence-Audience-Multi-step-Conversions.md) — **brief seed; best fit for a 4-stage cascade**
- [ESM2: Post-Click Behavior Decomposition (Alibaba, SIGIR 2020)](./read-papers/2020_SIGIR_ESM2_Entire-Space-Multi-Task-Post-Click-Behavior-Decomposition.md)
- [HM3: Hierarchically Modeling Micro and Macro Behaviors (Alibaba, SIGIR 2021)](./read-papers/2021_SIGIR_HM3_Hierarchically-Modeling-Micro-Macro-Behaviors-Conversion.md)
- [Optimizing Airbnb Search Journey with Multi-task Learning (KDD 2023)](./read-papers/2023_KDD_JourneyRanker_Airbnb-Search-Journey-Multi-task-Learning.md) — **closest analogue: a two-sided marketplace funnel with negative milestones**
- [Multitask Ranking for Immersive Feed and No More Clicks (Google, CIKM 2023)](./read-papers/2023_CIKM_NA_Immersive-Feed-No-More-Clicks-SFV-Ranking.md)
- [MAL: Multi-Attribution Learning for CVR (Alibaba, CIKM 2025)](./read-papers/2025_CIKM_MAL_Multi-Attribution-Learning-Conversion-Rate-Prediction.md)

**Recommendation:** use **ESCM2's counterfactual correction** with **AITM's multi-step structure**.
Plain ESMM carries a proven bias, and the project's cascade is deeper than the two-stage advertising
case, compounding selection bias at every stage. **That combination is not reported by either paper**
— it is an integration the project would own.

**Airbnb's Journey Ranker is the closest structural analogue in the corpus**: a multi-stage funnel in
a two-sided marketplace, with **three negative-milestone heads** among its ten. Modelling outcomes
that look like progress but end badly is directly relevant to the success paradox.

---

## Category 8 — Incrementality inside the ranker (7 papers)

The question: *where does uplift live — beside the ranker, or inside its objective?*

- [RERUM: Rankability-enhanced Revenue Uplift Modeling (KDD 2024)](./read-papers/2024_KDD_RERUM_Rankability-Enhanced-Revenue-Uplift-Modeling.md) — **ranks by CATE on a 2–4 week revenue outcome using a ZILN loss**
- [CRRS: Revisiting Reciprocal Recommender Systems (KDD 2024)](./read-papers/2024_KDD_CFRR_Counterfactual-Reciprocal-Recommender-Systems.md) — **bilateral treatment, potential outcomes**
- [Learning to Rank for Uplift Modeling](./read-papers/2020_arXiv_PCG_Learning-To-Rank-For-Uplift-Modeling.md)
- [Treatment Targeting by AUUC Maximization](./read-papers/2020_arXiv_AUUCmax_Treatment-Targeting-AUUC-Maximization-Generalization-Guarantees.md)
- [Rethinking Causal Ranking: Uplift Model Evaluation (ICML 2025)](./read-papers/2025_ICML_PTONet_Rethinking-Causal-Ranking-Balanced-Uplift-Evaluation.md)
- [Off-Policy Evaluation and Learning for Matching Markets (RecSys 2025)](./read-papers/2025_RecSys_DiPS-DPR_Off-Policy-Evaluation-Learning-Matching-Markets.md) — **brief seed**
- [Invariant Deep Uplift Modeling for Incentive Assignment (ICML 2025)](./read-papers/2025_ICML_IDUM_Invariant-Deep-Uplift-Modeling-Incentive.md)

### The distinction this category exists to make

**Using IPS or doubly-robust estimation to debias a prediction is not the same as estimating uplift.**
Several papers here look causal and are not. CFRR and ESCM2 debias predictions; **RERUM and CRRS
estimate effects**. Every card records which.

**The treatment matters too.** In marketing-uplift work the treatment is a coupon or a campaign
contact — *not* the act of showing an item in a ranked list. The project needs the incremental effect
of an **exposure within a ranking**, which is a different treatment and a different estimand.

---

## Category 9 — Credit assignment: from a delayed outcome back to one item (4 papers)

The question, and research question Q2: *a retention outcome is user-level and delayed; a decision is
item-level. How do they connect?*

- [SlateQ (Google, IJCAI 2019)](./read-papers/2019_IJCAI_SlateQ_Tractable-Decomposition-Recommendation-Sets.md) and [the extended arXiv version](./read-papers/2019_arXiv_SlateQ_Reinforcement-Learning-For-Slate-Based-Recommenders.md) — **brief seed**
- [Future Impact Decomposition in Request-level Recommendations (Kuaishou, KDD 2024)](./read-papers/2024_KDD_ItemA2C_Future-Impact-Decomposition-Request-level-Recommendations.md) — **brief seed**
- [Globally Optimized Mutual Influence Aware Ranking (Alibaba, IJCAI 2018)](./read-papers/2018_IJCAI_NA_Globally-Optimized-Mutual-Influence-Ranking.md)

**SlateQ is the cleanest decomposition and its assumptions fail here.** *Single Choice* assumes the
user consumes at most one item per slate — viewers like several candidates per session.
*Reward/Transition Dependence on Selection* assumes reward depends only on the selected item — **but a
match requires the other person to like back**, an external, delayed action outside its single-agent
MDP. Its LP and top-k machinery remain reusable once item-level values exist; the decomposition does
not transfer without extension to a two-agent reward.

**ItemA2C is assumption-lighter and carries a valuable negative result.** It splits slate-level future
value across items via weights summing to one, with a learned weighting beating both equal-weight and
reward-proportional heuristics. Critically, the authors **also tried decomposing the critic's
TD-target to item level and it failed** — they conclude the critic must stay at list level to capture
item-item interaction. It splits a *value estimate*, not a causal effect, and uses a bootstrapped
discount rather than a calendar horizon.

**Net:** item-level credit assignment for a **reciprocal, long-horizon** outcome is unsolved in the
published literature.

---

## Category 10 — Reciprocity: scoring a pair, not an item (13 papers)

The question: *how do we score a pair when a match needs both sides to act?*

- [Reciprocal Recommender Systems: A Survey (Palomares et al., Information Fusion 2021)](./read-papers/2021_arXiv_NA_Reciprocal-Recommender-Systems-Survey.md) — **brief seed; field taxonomy**
- [Matching Theory-based Recommender Systems in Online Dating (2022)](./read-papers/2022_arXiv_MTRS_Matching-Theory-based-Recommender-Systems-Online-Dating.md) — **domain-native**
- [CRRS: Revisiting Reciprocal Recommender Systems (KDD 2024)](./read-papers/2024_KDD_CFRR_Counterfactual-Reciprocal-Recommender-Systems.md) — **the nearest miss**
- [Fast and Examination-agnostic Reciprocal Recommendation (CyberAgent, RecSys 2023)](./read-papers/2023_RecSys_TU_Fast-Examination-Agnostic-Reciprocal-Recommendation.md) — **brief seed**
- [Fair Reciprocal Recommendation in Matching Markets (CyberAgent, RecSys 2024)](./read-papers/2024_RecSys_NSW_Fair-Reciprocal-Recommendation-Matching-Markets.md) — **brief seed**
- [Reciprocal Sequential Recommendation (ReSeq, RecSys 2023)](./read-papers/2023_RecSys_ReSeq_Reciprocal-Sequential-Recommendation.md)
- [CUPID: Real-Time Session-Based Reciprocal Recommendation (2024)](./read-papers/2024_arXiv_CUPID_Real-Time-Session-Based-Reciprocal-Recommendation.md)
- [Online Reciprocal Recommendation with Theoretical Guarantees (SMILE, NeurIPS 2018)](./read-papers/2018_NeurIPS_SMILE_Online-Reciprocal-Recommendation-Guarantees.md)
- [Balancing Fairness and High Match Rates: Nash Social Welfare (2026)](./read-papers/2026_arXiv_NSW_Balancing-Fairness-High-Match-Rates-Reciprocal.md)
- [Powering Tinder — The Method Behind Our Matching (2019)](./read-papers/2019_Blog_NA_Powering-Tinder-Method-Behind-Matching.md) — **brief seed**
- [Automated Decision Making at Grindr (2023)](./read-papers/2023_Blog_NA_Automated-Decision-Making-Grindr.md) — **states it runs no recommendation algorithm**
- [Model-based Recall in Momo Social Recommendation](./read-papers/2021_Blog_NA_Model-based-Recall-Momo-Social-Recommendation.md)
- [Learning Hiring Preferences: The AI Behind LinkedIn Jobs (2019)](./read-papers/2019_Blog_NA_Learning-Hiring-Preferences-LinkedIn-Jobs.md) — **closest published two-sided analogue**

### The horizon problem, in three categories

Reciprocal work has essentially **no calendar-time objective**, but the precise picture is three-way:

| Category | Papers | What "time" means |
|---|---|---|
| **Static snapshot** — the majority | Palomares survey, ReSeq, CyberAgent TU, NSW, MTRS, CUPID | No time. A fixed historical interaction matrix. |
| **Calendar window** — one | ECDA | A real 2-week realized-outcome window, daily refresh |
| **Round count** — one | SMILE | Login rounds, not calendar time |

**CUPID makes an instructive distinction:** it is real-time and session-based, yet its horizon is
`none — static snapshot`, because its label is the **chat duration of the current call**. A real-time
architecture is not a long horizon.

### The dating industry publishes almost nothing

Match Group, Bumble, Coffee Meets Bagel, Tantan and Soul returned **null results**. Only Tinder's 2019
pressroom post and Momo's InfoQ article exist, and **Grindr publicly states it runs no recommendation
algorithm at all** — distance-sorted search only. Evidence must transfer from adjacent two-sided
markets: LinkedIn Jobs, Airbnb, and online recruitment.

---

## Category 11 — Congestion: candidate attention is a shared, limited resource (5 papers)

The question: *how do we handle many viewers competing for the same candidate?*

- [Optimizing Rankings for Recommendation in Matching Markets (WWW 2022)](./read-papers/2022_WWW_SWR_Optimizing-Rankings-Matching-Markets.md) — **the ranking is the decision variable: directly usable**
- [Managing Congestion in Two-Sided Platforms: Online Rentals (2023)](./read-papers/2023_arXiv_NA_Managing-Congestion-Two-Sided-Platforms-Online-Rentals.md) — **ranking order plus personalization degree**
- [ECDA: Integrating Predictive Models into Two-Sided Recommendations (2026)](./read-papers/2026_arXiv_ECDA_Integrating-Predictive-Models-Two-Sided-Matching.md) — **2-week window plus per-receiver exposure quota**
- [Assortment Planning for Two-Sided Sequential Matching Markets (2019)](./read-papers/2019_arXiv_NA_Assortment-Planning-Two-Sided-Sequential-Matching.md) — assortment, not ranking
- [Understanding Guest Preferences and Optimizing Two-sided Marketplaces (Airbnb, 2026)](./read-papers/2026_arXiv_NA_Understanding-Guest-Preferences-Two-sided-Marketplaces.md)

**Two of five optimize the ranking directly** — the project's actual lever. One assumes control of the
assortment, which a ranking-only platform can only approximate by truncating a list.

**The architectural consequence is concrete.** ECDA's exposure quota is defined on **expected likes or
dates per receiver**, not headcount, and enforcing it requires coordination **across viewers**. A
purely per-request ranker cannot express that. Congestion control needs a **cross-request budgeting
layer above the ranker** — an architecture decision, not a modelling detail.

---

## Category 12 — Measuring a change when both sides interfere (6 papers)

The question, and research question Q6: *how do we run a valid experiment when treating one viewer
changes what other viewers see?*

- [Interference, Bias, and Variance in Two-Sided Marketplace Experimentation (WWW 2022)](./read-papers/2022_WWW_NA_Interference-Bias-Variance-Two-Sided-Marketplace.md)
- [UniCoRn: A/B Testing for Recommenders in a Two-sided Marketplace (LinkedIn, NeurIPS 2021)](./read-papers/2021_NeurIPS_UniCoRn_AB-Testing-Recommender-Systems-Two-sided-Marketplace.md)
- [Seller-Side Experiments under Feedback-Loop Interference (2024)](./read-papers/2024_arXiv_NA_Seller-Side-Experiments-Feedback-Loop-Interference.md)
- [Tackling Interference from Data Training Loops: A Weighted Training Approach (2023)](./read-papers/2023_arXiv_WeightedTraining_Tackling-Interference-Data-Training-Loops.md)
- [Trustworthy Marketplace Experimentation with Budget-split Design (2020)](./read-papers/2020_arXiv_BudgetSplit_Trustworthy-Marketplace-Experimentation.md)
- [Two-Sided Prioritized Ranking (2025)](./read-papers/2025_arXiv_TSPR_Two-Sided-Prioritized-Ranking.md)

**The failure mode most likely to be discovered late: interference through the training data.** When a
treatment changes what the model learns from, the control group is contaminated **through the shared
model**. A unified retention model retrained on logged data inherits the treatment's effects. Two
papers here address it directly and it is easy to miss entirely.

---

## Category 13 — Generative rankers: unified architecture, short-term objective (9 papers)

The question: *do generative recommenders solve unification?*

**They unify the cascade, not the objective.**

- [OneRec-V2 (Kuaishou, 2025)](./read-papers/2025_arXiv_OneRec-V2_Lazy-Decoder-User-Feedback-Alignment.md) — **reward is a same-session watch-time quantile; 7-day return is evaluation-only, stated in the authors' own Limitations**
- [MTGR (Meituan, 2025)](./read-papers/2025_arXiv_MTGR_Industrial-Scale-Generative-Recommendation-Meituan.md) — CTR/CTCVR, no retention signal
- [GenRec: An LLM-Backed Recommendation Ranker at Netflix (2026)](./read-papers/2026_arXiv_GenRec_LLM-Backed-Recommendation-Ranker.md) — **states long-term member utility as the target, operationalized by reward-weighting short-term labels**
- [GenPage: End-to-End Generative Homepage Construction at Netflix (2026)](./read-papers/2026_RecSys_GenPage_End-to-End-Generative-Homepage-Construction.md) — same reward-weighting pattern
- [HSTU: Actions Speak Louder than Words (Meta, ICML 2024)](./read-papers/2024_arXiv_HSTU_Actions-Speak-Louder-Than-Words.md) — **brief seed**
- [OneRec: Unifying Retrieve and Rank (Kuaishou, 2025)](./read-papers/2025_arXiv_OneRec_Unifying-Retrieve-Rank-Preference-Alignment.md) — **brief seed**
- [OneRec Technical Report](./read-papers/2025_arXiv_OneRec_Technical-Report.md)
- [SORT-Gen: Generative Re-ranking for List-level Multi-objective Optimization (Alibaba, SIGIR 2025)](./read-papers/2025_SIGIR_SORT-Gen_Generative-Re-ranking-List-level-Multi-objective.md)
- [Tencent Advertising Algorithm Challenge 2025](./read-papers/2026_arXiv_NA_Tencent-Advertising-Algorithm-Challenge-Generative-Recommendation.md)

**The Netflix pattern is the useful finding here** and is described in the executive summary as a
migration candidate: keep short-term labels, learn a reward model scoring each event by its
association with a long-horizon outcome, and use those scores as **per-example weights** in the
ranking loss. Its limitation is that **a weight is not an effect**.

---

## References — surveyed but low project relevance

- [Deep RL for Search, Recommendation and Advertising: A Survey (2019)](./read-papers/2019_arXiv_NA_Deep-RL-Search-Recommendation-Advertising-Survey.md) — predates the retention line
- [Neural Interactive Collaborative Filtering (JD, SIGIR 2020)](./read-papers/2020_SIGIR_NICF_Neural-Interactive-Collaborative-Filtering.md)
- [Customer Lifetime Value Prediction Using Embeddings (KDD 2017)](./read-papers/2017_KDD_NA_Customer-Lifetime-Value-Prediction-Embeddings.md)
- [Cross-Domain Adaptative Learning for Advertisement LTV (AAAI)](./read-papers/2023_AAAI_CDAF_Cross-Domain-Adaptative-Learning-Advertisement-LTV.md)
- [RankUp: High-Rank Representations for Advertising Recommenders (2026)](./read-papers/2026_arXiv_RankUp_High-Rank-Representations-Advertising-Recommenders.md)
- [Managing Diversity in Airbnb Search (KDD 2020)](./read-papers/2020_KDD_NA_Managing-Diversity-Airbnb-Search.md)
- [RAM: Jointly Learning to Recommend and Advertise (ByteDance, KDD 2020)](./read-papers/2020_KDD_RAM_Jointly-Learning-Recommend-Advertise.md)
- [OCPC: Optimized Cost per Click in Taobao (Alibaba, KDD 2019)](./read-papers/2017_KDD_OCPC_Optimized-Cost-per-Click-Taobao-Advertising.md)
- [E3IR: End-to-End Cost-Effective Incentive Recommendation](./read-papers/2024_RecSys_E3IR_End-to-End-Cost-Effective-Incentive-Recommendation.md)
- [ReAlloc: Multi-channel Uplift Policy Learning](./read-papers/2026_arXiv_ReAlloc_Multi-channel-Uplift-Policy-Learning.md)
- [KuaiSim (NeurIPS 2023)](./read-papers/2023_NeurIPS_KuaiSim_Comprehensive-Simulator-Recommender-Systems.md) — infrastructure, with the circularity caveat above

---

## Coverage and limitations of this review

**Corpus:** 133 papers. **Industry share:** 62%, only just above the brief's 60% floor, and **only 3
sources are company engineering blogs**. The brief ranks blogs above academic venues precisely because
they reveal deployed practice — the survey cleared the floor on industry-*track papers* instead,
because dating platforms publish nothing and most engineering blogs are Medium-hosted and unfetchable.
**The evidence therefore leans toward what companies write up for conferences rather than what they
run.**

**Direction balance:** D1:14 D2:13 D3:11 D4:9 D5:9 D6:5 D7:18 D8:23 D9:7. D1–D4 hold 43% against the
brief's 50% floor — a **documented deviation**: D8 was expanded from 5 papers to 23 because it carries
the project's defining constraints, and cutting it would have removed the most relevant material.

**Not retrieved.** Six sources are confirmed to exist but were unreachable, including two brief seeds:
**Netflix, "Reward Innovation for Long-Term Member Satisfaction" (RecSys 2023)** — the keystone of the
reward-weighting pattern in Category 13 — and **Meta, "Learning Robust, Long-run Surrogate Metrics"
(KDD 2026)**. Nine further HTML-only sources were not carded.

**Two harvest candidates could change conclusions** and remain unread: **"User Retention: A Causal
Approach with Triple Task Modeling" (IJCAI 2021)** — causal reasoning applied to retention, the exact
dimension CRRS lacks — and **"Surrogate for Long-Term User Experience in Recommender Systems"
(Google, KDD 2022)**, a surrogate built for a recommender rather than an experiment.
