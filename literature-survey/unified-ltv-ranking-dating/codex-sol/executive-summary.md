---
model_identifier: codex-sol
date: 2026-08-18
topic: unified retention and revenue ranking model for a two-sided dating recommender
notebook_id: 67046a44-7490-4fe5-b54a-3f39ef37fdd3
notebook_source_count: 146
selected_source_count: 120
source_extraction: 118/120
url_validation: 120/120 resolved (94 direct HTTP, 24 browser-public, 2 canonical replacements)
status: strategic proposal; not implementation-ready
evidence_stage: claim-linked selected-corpus synthesis
---

# Unified Retention/Revenue Ranking Model for a Dating Recommender — Executive Summary

## Decision

The preferred first production candidate is a **reciprocal multi-task LTV ranker** whose initial serving utility uses only calibrated **30-day binary return** and **30-day net recognized revenue**. Like, match, qualified conversation, engagement-count, receiver-load, and safety/quality heads provide auxiliary learning, constraints, or guardrails. The **90-day revenue head is shadow-only** until its maturity, calibration, surrogate validity, and online decision value pass a separately pre-registered gate.

A **bilateral causal-LTV ranker** is Rank 2, contingent on an explicit randomized exposure policy, validated propensities, overlap, and an experiment that estimates market spillovers. A **slate RL or generative policy** is Rank 3 because sparse reciprocal rewards, long delay, OPE uncertainty, serving cost, and interference all become harder at once.

This is a research-backed strategic proposal, **not an implementation-ready specification**. Product owners, Finance, Trust & Safety, experimentation, and ML must still approve label definitions, accounting treatment, eligibility, capacity, non-inferiority margins, minimum detectable effects, and market clusters before launch.

## Evidence scope

The synthesis uses 120 selected sources; 118 cards contain substantive indexed extraction and two are metadata-only failures. Structural deliverable coverage is 31/31. URL validation resolved all 120 references: 94 direct HTTP successes, 24 public sources verified despite automated-request ambiguity, and 2 dead URLs replaced with canonical primary URLs. Claims are auditable in [claim-evidence-table.md](claim-evidence-table.md); all 120 selected references appear in [comparison-table.md](comparison-table.md), with URL evidence in [url-validation.md](url-validation.md).

Language such as “represented in the selected corpus” is deliberate. The curated sample cannot establish ecosystem-wide frequency or adoption prevalence.

## Q1–Q8 findings

1. **Q1 — Long-term objectives.** The selected corpus documents learned long-horizon fusion, explicit LTV/retention heads, and sequential value optimization. It does not support “most common in industry” comparisons. Source mechanisms are linked in the claim-evidence table; selecting the reciprocal multi-task architecture is **survey inference**.
2. **Q2 — Credit assignment.** Funnel factorization, request-to-item decomposition, slate Q-value decomposition, and trajectory reward propagation appear in selected cards. None identifies the causal contribution of one profile exposure to a later return amid many exposures and marketplace spillovers.
3. **Q3 — Labels and horizons.** Selected cards support multi-day future-action windows, 30/90/180/365-day LTV, zero-inflated heavy-tailed value losses, and censoring-aware delay models. The operational dating labels below are **survey definitions**, not source-reported standards.
4. **Q4 — Fusion.** Selected papers use learned RL fusion, distillation, stochastic aggregation, and explicit multi-task heads. The initial utility below uses calibrated heads and constrained monotone fusion; it is a project design inference, not a documented dating deployment.
5. **Q5 — Incrementality.** *Rankability-Enhanced Revenue Uplift Modeling* (KDD 2024), *Entire Space Counterfactual Multi-Task Model* (SIGIR 2022), and *Counterfactual Reciprocal Recommender Systems for User-to-User Matching* (KDD TSMO Workshop 2025) place causal correction inside ranking under their own treatment definitions. Conditional retention prediction must not be relabeled as causal lift.
6. **Q6 — Evaluation.** *Off-Policy Evaluation and Learning for Matching Markets* (RecSys 2025), *Interference, Bias, and Variance in Two-Sided Marketplace Experimentation: Guidance for Platforms* (2021/2022), and *Two-Sided Prioritized Ranking: A Coherency-Preserving Design for Marketplace Experiments* (2026) show why estimator assumptions, randomization unit, bias, variance, and spillovers must be explicit. Interleaving alone does not control market interference.
7. **Q7 — Two-sided constraints.** Direct dating and adjacent-market evidence represents reciprocity, congestion, receiver capacity, exposure concentration, and opportunity fairness. *Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach* (2026) is especially relevant but has a short horizon and mixed field results.
8. **Q8 — Migration.** The corpus supports the component steps below, but no selected source documents the exact end-to-end migration from this project’s CTR/CVR plus uplift blend. The sequence is **survey inference**.

## Taxonomy represented in the selected corpus

| Family | Selected-corpus examples | Represented organizations; no prevalence claim |
|---|---|---|
| Entire-space cascade learning | *Entire Space Multi-Task Model*; *Entire Space Counterfactual Multi-Task Model* | Alibaba-affiliated work |
| Delayed-feedback correction | *Modeling Delayed Feedback in Display Advertising*; ESDF/DEFER/DEFUSE family | Criteo and selected advertising/recommendation teams |
| Learned multi-objective fusion | *Multi-Task Fusion via Reinforcement Learning for Long-Term User Satisfaction*; *Multi-objective Learning to Rank by Model Distillation* | Tencent, selected KDD/WWW papers |
| LTV distributions and horizons | *A Deep Probabilistic Model for Customer Lifetime Value Prediction*; *Billion-user Customer Lifetime Value Prediction* | Google, Kuaishou |
| Long-horizon value/RL | *SlateQ*; *Future Impact Decomposition*; *Modeling User Retention through Generative Flow Networks* | Google/YouTube, Kuaishou |
| Surrogate/downstream rewards | *The Surrogate Index*; *Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix* | Netflix, selected Spotify/Pinterest work |
| Causal uplift ranking | *Rankability-Enhanced Revenue Uplift Modeling*; ESCM²; CFRR | Selected revenue-ranking work, Sony |
| Reciprocal allocation/OPE | ECDA; fair reciprocal NSW; DiPS/DPR | CoupLink/LINKBAL, CyberAgent, Wantedly |
| Generative recommendation | *OneRec*; *GenRec*; *GenPage* | Kuaishou, Netflix |

## Three ranked candidate architectures

| Rank | Architecture | Serving objective | Current-stack transition | Main evidence gap |
|---:|---|---|---|---|
| 1 | Reciprocal multi-task LTV ranker | Initial utility: 30-day return + 30-day net revenue; 90-day revenue shadow-only; hard eligibility/safety/capacity constraints | CTR/CVR heads remain auxiliaries. Current uplift is initially an audit benchmark, not a teacher or serving feature. | Conditional value can masquerade as causal value; no end-to-end dating deployment |
| 2 | Bilateral causal-LTV ranker | Incremental 30-day viewer and receiver value under a defined pair-exposure intervention, plus cluster-level total-market policy effect | Add cross-fitted propensity/outcome heads only after randomized logging passes overlap and ESS gates | Pair estimands do not identify market spillovers; high variance and positivity failures |
| 3 | Slate value/RL or generative policy | Discounted cross-session reciprocal value with explicit congestion and safety constraints | Supervised Rank 1 initializes representations/reward models; causal claims still require experiments | Reward hacking, fragile OPE, interference, latency, and popularity feedback |

## Initial serving utility

The following is a **survey-proposed specification** to remove ambiguity:

$$
U(A,B)=w_r z_s(\hat p_{R30}(A,B))+w_v z_s(\widehat{E}[V30\mid A,B])-\lambda_L z_s(\hat L_B)-\lambda_C z_s(\hat C_B)
$$

- $\hat p_{R30}$: calibrated probability of 30-day binary return.
- $\widehat{E}[V30]$: calibrated expected 30-day net recognized revenue.
- $\hat L_B$: predicted receiver load.
- $\hat C_B$: predicted exposure concentration or capacity pressure.
- $z_s$: robust within-segment normalization fitted only on training data—median/IQR scaling, clipped to a pre-registered range—so scale drift cannot silently change trade-offs.
- $w_r,w_v\ge0$: non-negative monotone fusion weights learned in shadow mode on mature outcomes, then frozen for each experiment ramp.
- $\lambda_L,\lambda_C\ge0$: pre-registered soft-penalty weights. They can reduce rank but cannot override hard constraints.

**Hard constraints:** legal/age/distance/preference eligibility; blocks and prior safety exclusions; candidate availability; receiver capacity cap; and any Trust & Safety exclusion. These are never exchanged for revenue.

**Safety/quality gates:** no ramp unless the upper 95% confidence bound for block/report harm is below its pre-approved non-inferiority margin, the lower 95% bound for qualified-conversation and reciprocal-quality change is above its margin, severe safety events do not exceed the escalation threshold, and receiver-load p95/p99 stay below approved caps. Margins and caps must be fixed from historical risk and power analysis before assignment.

**90-day revenue:** predicted and calibrated in shadow only. It may enter serving only after complete 90-day plus refund/chargeback maturity, stable segment calibration, validated incremental information beyond V30, and a powered experiment whose mature 90-day decision agrees with the earlier release rule.

## Operational labels, losses, and maturity

All definitions below are **project proposals** and require owner approval.

| Target | Operational definition | Loss | Maturity / exclusions |
|---|---|---|---|
| 30-day binary return (R30) | 1 if the member starts at least one user-initiated qualified session on days 1–30 after the anchor request; a qualified session has at least 30 foreground seconds or one core action. Same-day activity alone does not qualify. | Bernoulli cross-entropy with calibration loss | Train only after day 30; exclude bots, staff/test accounts, fraud, and sessions invalidated by safety systems |
| 30-day engagement count | Number of distinct qualified active days in days 1–30; session count may be a separate diagnostic, not mixed into this label | Negative-binomial count loss; Poisson only if dispersion diagnostics support it | Day-30 maturity mask; cap/winsorization fixed before training and reported |
| Qualified conversation | A mutual match followed within 7 days by at least two non-deleted messages from each member; safety-deleted/spam messages do not count | Entire-space binary head with BCE or focal loss only if pre-registered rare-event diagnostics justify it | Match cohort matures after 7 days; conversation is auxiliary/quality, not evidence of a date |
| Success exit | 1 only when a member explicitly selects “met someone / in a relationship” in deactivation feedback, or both members confirm an in-person date through product instrumentation within 30 days | Binary guardrail head; not included in serving utility until label coverage and bias are audited | Never infer success from inactivity alone; missing feedback is missing, not negative |
| Receiver load | Primary: predicted distinct inbound likes delivered to B in the next 24 hours divided by B’s trailing-28-day capacity, where capacity is the median daily inbound-like count on days B responded without exceeding approved response-latency/quality limits. Secondary diagnostics: open matches and active qualified conversations in seven days. | Regression/count model; used as soft penalty plus hard cap | Recompute daily; cold-start capacity uses a conservative segment prior |
| 30-day net recognized revenue (V30) | Ledger revenue recognized in days 0–30: daily-recognized subscription revenue plus recognized a-la-carte revenue, minus refunds, credits, chargebacks, and indirect taxes under Finance policy | ZILN or hurdle-lognormal likelihood; report payer calibration and positive-spend tail error separately | Day 30 plus Finance-approved refund/chargeback lag; no provisional gross bookings |
| 90-day net recognized revenue (V90) | Same accounting definition over days 0–90 | Same as V30 | Shadow-only until day 90 plus accounting lag and explicit release gate |

## Role of the current uplift model

The current uplift model is initially a **frozen audit benchmark only**. Report correlation, calibration by treatment arm, policy-value estimates, and disagreement slices against ordinary outcome heads and the randomized experiment. Do not feed its score into Rank 1 serving or training by default.

Teacher/feature use is allowed only if all of the following hold:

1. Its treatment, control, unit, horizon, eligibility set, and revenue/retention labels exactly match the new head.
2. Predictions are out-of-fold/cross-fitted and generated without post-treatment features or future leakage.
3. Calibration is checked on randomized or otherwise defensible treatment data by arm and key segment.
4. The score is stop-gradient if used as a teacher and is excluded from propensity estimation.
5. Ablations show incremental predictive or policy value over ordinary heads without degrading calibration, overlap, safety, quality, or receiver-load metrics.
6. Removing the teacher at serving does not change the causal estimand.

Failure of any condition returns the model to audit-only status.

## Staged migration and gates

1. **Instrumentation and randomized logging.** Log request ID, full eligible set, scores, positions, both-side actions, assignment, known propensity, maturity, finance events, and receiver load. Begin a small explicit exploration bucket only after safety review. Gate: replay reproduces assignments/propensities and leakage tests pass.
2. **Shadow outcome heads.** Train R30, active-day count, qualified conversation, V30, and shadow V90. Gate: temporal holdout calibration/discrimination by lifecycle, payer status, market, and receiver popularity; V30 adds information beyond user-only baselines.
3. **Frozen utility shadow, then limited rerank.** Fit constrained non-negative fusion, freeze normalization/weights per ramp, and enforce hard filters/caps. Gate: all safety/quality non-inferiority and load caps pass; V90 remains shadow.
4. **Reciprocal allocation.** Add bilateral acceptance and congestion-aware reranking. Gate: both-side qualified conversations and coverage improve or remain non-inferior without load concentration.
5. **Causal value.** Train pair-level treatment-effect/OPE heads only under the definition below. Promotion depends on both pair-support diagnostics and a powered cluster-level market experiment.
6. **Optional sequential policy.** Consider conservative SlateQ/GFN/actor-critic or generative ranking only after mature Rank 1/2 experiments, reliable OPE directionality, and an incremental gain over the simpler system.

## Causal intervention and estimands

Two levels must remain separate:

**Pair/request estimand for model learning**

- **Intervention:** for an eligible request from viewer A, candidate B is placed in the randomized top-(K) exposure set versus B remains eligible but is not shown in top-(K).
- **Unit:** eligible request–candidate pair; repeated pairs are clustered by viewer and receiver.
- **Eligibility:** both users pass hard constraints and B appears in the pre-policy eligible candidate set under both arms.
- **Outcome:** viewer and receiver R30/V30 plus qualified-conversation guardrails, anchored at the request.
- **Estimand:** conditional average effect of top-(K) exposure within this eligible exploration population. It is not the total marketplace effect.
- **Propensity:** emitted by the assignment service from the explicit randomized exploration distribution, checked by replay, sum-to-one/support audits, and empirical assignment calibration.
- **Overlap/ESS proposal:** primary analysis requires $0.05\le e(X)\le0.95$ for the binary exposure contrast after restriction; stabilized-weight ESS $(\sum w)^2/\sum w^2$ must be at least 1,000 and at least 10% of raw eligible pairs overall and in every launch-critical slice. Otherwise no causal-head promotion.
- **Uncertainty:** cross-fitted DR/SNIPS estimates, cluster-robust 95% confidence intervals over viewers and receivers, cluster bootstrap sensitivity, and reported weight tails/clipping sensitivity.

**Market policy estimand for launch**

- **Intervention:** all eligible requests in a persistent market cluster use Rank 1/2 versus the current CTR/CVR plus uplift-blend policy.
- **Unit/randomization:** market cluster, constructed from geography, reciprocal-preference pools, and interaction-graph connectivity to minimize predicted cross-cluster edges; assignment persists through the mature horizon and washout.
- **Primary estimand:** intent-to-treat change in total 30-day net value per eligible member, reported separately for active viewers and passive receivers, with R30, V30, qualified conversation, safety, coverage, and receiver-load components.
- **Spillovers:** estimate receiver-side/passive-member effects inside treated and control clusters; measure cross-cluster interactions and run sensitivity bounds. Pair OPE, viewer randomization, and interleaving do not identify this total effect.

## Online evaluation under interference

- **Interleaving/request randomization:** use only for short-horizon relevance or ranker-comparison diagnostics when exposure effects are local. It is not a substitute for interference control and cannot approve long-horizon causal value.
- **Cluster design:** precompute clusters, balance pre-period market tightness/outcomes, and exclude or separately analyze high cross-cluster interaction edges. Use cluster-robust or randomization-inference intervals.
- **Power:** before launch, estimate pre-period variance, intracluster correlation, expected attrition, baseline rates, and business-approved minimum detectable effects; require at least 80% power at two-sided alpha 0.05 for R30/V30 and enough clusters for the planned variance estimator. If power is inadequate, do not reinterpret a null as safety.
- **Temporal validation:** use forward-chaining offline holdouts; a minimum 30-day outcome window plus accounting lag for the primary test; keep a 90-day shadow cohort plus accounting lag; include a pre-period and post-ramp washout chosen before assignment.
- **Ramp:** shadow → 1% exploration/logging → 5% → 10% → 25% → 50% by whole randomized clusters where cluster assignment is required. Each step waits for telemetry, safety, quality, load, and the available mature outcomes; no mid-ramp weight retraining.
- **Stop rules:** immediate stop for severe safety escalation, assignment/propensity corruption, hard-cap breach, or data leakage; statistical stop/rollback when sequentially adjusted 95% intervals cross a pre-registered harm boundary for safety, qualified conversation, either side’s R30/V30, or receiver load. Use alpha-spending or another pre-specified sequential procedure.
- **OPE reporting:** point estimate, 95% CI, cluster definition, ESS, overlap range, weight percentiles, clipping sensitivity, model cross-fitting, and disagreement with online results. A point estimate alone is not a gate.

## Open questions and gaps

- No selected source combines reciprocal ranking with incremental long-horizon retention and revenue in one deployed dating system.
- Success-exit instrumentation may be sparse and selectively missing.
- Receiver capacity is behavior- and market-dependent; the proposed load definition requires validation.
- Cross-cluster interactions may remain too high for clean market isolation.
- The pair-exposure estimand may not transport to a full policy change.
- Paid features change both assignment and monetization, complicating revenue counterfactuals.
- Exact safety/quality non-inferiority margins and business MDEs are not specified in sources and must be pre-approved.
- Two metadata-only cards limit substantive evidence completeness.

## Top-10 reading order

1. Xiao Ma et al., *Entire Space Multi-Task Model: An Effective Approach for Estimating Post-Click Conversion Rate* (SIGIR 2018).
2. Jiaqi Ma et al., *Modeling Task Relationships in Multi-Task Learning with Multi-gate Mixture-of-Experts* (2018; venue not specified in selected evidence).
3. Olivier Chapelle, *Modeling Delayed Feedback in Display Advertising* (KDD 2014).
4. Siyu Gu et al., *Real Negatives Matter: Continuous Training with Real Negatives for Delayed Feedback Modeling* (KDD 2021).
5. Xiaojing Wang et al., *A Deep Probabilistic Model for Customer Lifetime Value Prediction* (arXiv 2019).
6. Kunpeng Li et al., *Billion-user Customer Lifetime Value Prediction: An Industrial-scale Solution from Kuaishou* (CIKM 2022).
7. Susan Athey, Raj Chetty, Guido W. Imbens, and Hyunseung Kang, *The Surrogate Index: Combining Short-Term Proxies to Estimate Long-Term Treatment Effects More Rapidly and Precisely* (NBER / Review of Economic Studies; 2019, revised 2024).
8. Vickie Zhang et al., *Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix* (arXiv 2023).
9. Kazuki Kawamura et al., *Counterfactual Reciprocal Recommender Systems for User-to-User Matching* (KDD TSMO Workshop 2025).
10. Yudai Hayashi, Shuhei Goda, and Yuta Saito, *Off-Policy Evaluation and Learning for Matching Markets* (RecSys 2025).

**Next:** Eugene Ie et al., *SlateQ: A Tractable Decomposition for Reinforcement Learning with Recommendation Sets* (IJCAI 2019), then *Modeling User Retention through Generative Flow Networks* (KDD 2024).

## Scope summary

- Selected references: 120; substantive extraction: 118; metadata-only: 2.
- Structural deliverables: 31/31.
- Industry/company/industry-lab rows: 97/120, a property of this curated selection—not an estimate of global practice.
- URL validation: 120/120 resolved; see [url-validation.md](url-validation.md).
- Project-context mapping: all eight constraints are represented structurally; implementation validation is pending.
