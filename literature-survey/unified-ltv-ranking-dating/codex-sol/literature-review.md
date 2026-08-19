---
model_identifier: codex-sol
date: 2026-08-18
topic: unified retention and revenue ranking model for a two-sided dating recommender
notebook_id: 67046a44-7490-4fe5-b54a-3f39ef37fdd3
notebook_source_count: 146
status: strategic proposal; not implementation-ready
evidence_stage: claim-linked selected-corpus synthesis
selected_source_count: 120
source_extraction: 118/120
url_validation: pending
---

# Unified Retention/Revenue Ranking Model for a Dating Recommender — Literature Review

## Evidence status and reading guide

This review begins with seven independent all-source NotebookLM queries over 146 notebook sources, then tests the retained claims against 120 selected-source cards. Of those cards, 118 contain substantive indexed extraction and two are explicit metadata-only failures; unsupported details remain **Not specified in source**. URL reachability and source-identity validation were not recorded and remain pending. This is a research-backed strategic proposal, **not an implementation-ready specification**. The complete card view is [comparison-table.md](comparison-table.md), and Q1–Q8 are auditable in [claim-evidence-table.md](claim-evidence-table.md).

Evidence labels used throughout:

- **Selected-corpus/source-backed:** at least one linked selected-source card supports the scoped claim; this does not establish ecosystem-wide frequency or adoption.
- **Survey inference:** a proposed dating-system design or recommendation obtained by combining source-backed components. It is not a documented end-to-end deployment unless explicitly described as such.
- **Not specified in source:** the permitted inputs do not support the detail. It is intentionally not guessed.

## Executive synthesis

**Selected-corpus/source-backed.** The selected corpus clusters around seven recurring paradigms: entire-space multi-task learning, delayed-feedback modeling, multi-objective optimization, long-horizon reinforcement learning, causal uplift and surrogate indexing, reciprocal matching markets, and generative recommendation. Its strongest evidence is for components rather than a single end-to-end retention/revenue ranker. The represented organizations include Alibaba, Meituan, Criteo, Google, Kuaishou, YouTube, Spotify, Netflix, Pinterest, Sony, Wantedly, and CyberAgent; this list does not establish prevalence outside the curated corpus.

**Survey inference.** For the dating system in the brief, the best first architecture is a reciprocal shared-representation multi-task ranker with like, match, conversation, multi-horizon retention, and zero-inflated revenue heads, with delayed-feedback correction and a learned constrained utility layer. It retains the dense short-term heads as training support while making retention/revenue explicit objectives. A bilateral causal-LTV ranker is the second candidate once randomized exposure and pair-level propensities are dependable. Slate RL or a generative recommender is third because it adds the hardest credit-assignment, off-policy evaluation, and serving problems simultaneously.

### Most promising approaches

1. **Reciprocal multi-task LTV ranker:** lowest-risk path from the current CTR/CVR stack; uses short-term heads as auxiliaries and directly adds retention and revenue heads.
2. **Bilateral causal-LTV ranker:** ranks incremental, not merely conditional, retention/revenue while correcting reciprocal exposure bias.
3. **Slate value/RL ranker:** optimizes session or cross-session value and item/slate interactions, but only after logging and evaluation foundations are mature.

### Practical recommendation

- **Short term (1–3 months):** create leakage-safe exposure-to-outcome training tables; add shadow 7/14/30-day return and 7/30-day revenue heads; fit delayed/censored labels; validate calibration and historical surrogate stability without changing serving.
- **Mid term (3–6 months):** replace the manual blend with learned constrained fusion under receiver-load constraints; keep the current uplift score as an audit benchmark unless all alignment, cross-fitting, calibration, leakage, and ablation conditions pass; begin pair-level OPE and powered market-cluster experiments.
- **Later:** train bilateral treatment-effect heads on randomized or well-supported exposure; consider SlateQ/GFN-style value learning only after the production OPE stack predicts online direction reliably.

## 1. Taxonomy of unified long-term-value ranking approaches

| Approach | What it contributes | Representative references in the NLM synthesis | Industry adopters represented | Dating-system role | Evidence status |
|---|---|---|---|---|---|
| Entire-space sequential multi-task learning | Learns dense upstream tasks and sparse downstream tasks over all impressions; addresses sample-selection bias and sparsity through probability-chain structure and shared representations | Xiao Ma et al., *Entire Space Multi-Task Model: An Effective Approach for Estimating Post-Click Conversion Rate* (2018); Wen et al., *Entire Space Multi-Task Modeling via Post-Click Behavior Decomposition* (2020); Wang et al., *Entire Space Counterfactual Multi-Task Model* (2022); Xi et al., *Modeling the Sequential Dependence among Audience Multi-step Conversions with Multi-task Learning in Targeted Display Advertising* (KDD 2021) | Alibaba; Meituan | Impression → like → match → conversation cascade and dense-to-sparse representation transfer | Selected-corpus/source-backed; dating mapping is inference |
| Delayed-feedback and censoring correction | Avoids treating unresolved outcomes as negatives; balances fresh training data against label maturity | Olivier Chapelle, *Modeling Delayed Feedback in Display Advertising* (KDD 2014); Yoshikawa and Imai, *A Nonparametric Delayed Feedback Model* (2018); *Entire Space Delayed Feedback Model* (AAAI 2021); Gu et al., *Real Negatives Matter: Continuous Training with Real Negatives for Delayed Feedback Modeling* (KDD 2021); *Asymptotically Unbiased Estimation for Delayed Feedback via Label Correction* (WWW 2022) | Criteo; industrial advertising/recommendation teams represented by ESDF/DEFER/DEFUSE | Correct 7–30-day return and weeks-long purchase labels | Selected-corpus/source-backed |
| Multi-objective shared-expert ranking | Models related and conflicting tasks using shared experts, task gates, progressive extraction, stochastic aggregation, Pareto constraints, or distillation | Jiaqi Ma et al., *Modeling Task Relationships in Multi-Task Learning with Multi-gate Mixture-of-Experts* (2018); *A Pareto-Efficient Algorithm for Multiple Objective Optimization* (2019); *Multi-Objective Ranking Optimization Using Stochastic Label Aggregation* (2020); *Multi-objective Learning to Rank by Model Distillation* (KDD 2024) | Selected Meituan/Tencent and other industry papers; prevalence is not estimated | Learned fusion of like/match/conversation, retention, revenue, receiver load, and quality guardrails | Components are source-backed; the dating objective is inference |
| User-level LTV and multi-horizon value modeling | Handles zero mass, long tails, high-value users, and ordered horizons | Wang et al., *A Deep Probabilistic Model for Customer Lifetime Value Prediction* (2019); Kunpeng Li et al., *Billion-user Customer Lifetime Value Prediction: An Industrial-scale Solution from Kuaishou* (CIKM 2022) | Google; Kuaishou | ZILN revenue plus source-reported 30/90/180/365-day monotonic value heads; item-level use is inference | Selected-corpus/source-backed; item-level use is inference |
| Long-horizon value learning and RL | Treats recommendation as an MDP; decomposes slate value or propagates delayed terminal reward through actions/states; applies off-policy correction | Ie et al., *SlateQ: A Tractable Decomposition for Reinforcement Learning with Recommendation Sets* (IJCAI 2019); Chen et al., *Top-K Off-Policy Correction for a REINFORCE Recommender System* (WSDM 2019); *Long-Term Off-Policy Evaluation and Learning* (2024); *Modeling User Retention through Generative Flow Networks* (KDD 2024) | YouTube/Google; Spotify; Kuaishou | Session/slate credit assignment and eventual policy optimization | Selected-corpus/source-backed |
| Surrogate-index and downstream-reward modeling | Predicts long-run outcomes from early proxy vectors, screens proxy reliability across past experiments, or supplies downstream auxiliary rewards | Athey et al., *The Surrogate Index: Combining Short-Term Proxies to Estimate Long-Term Treatment Effects More Rapidly and Precisely* (NBER Working Paper 26463, 2019); *Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix*; Pinterest downstream-reward work; Spotify clickiness–stickiness work | Netflix; Pinterest; Spotify | Earlier feedback and experiment acceleration while mature outcomes remain the authority | Selected-corpus/source-backed |
| Uplift inside ranking | Optimizes ordering by incremental outcomes or corrects historical exposure with counterfactual objectives | *Rankability-Enhanced Revenue Uplift Modeling* (KDD 2024); Wang et al., *Entire Space Counterfactual Multi-Task Model* (2022); Kazuki Kawamura et al., *Counterfactual Reciprocal Recommender Systems for User-to-User Matching* (KDD TSMO Workshop 2025) | Industry revenue-ranking work; Sony | Replace post-hoc uplift blending with a trainable incremental-value head and pair-level propensity correction | Selected-corpus/source-backed; proposed integration is inference |
| Reciprocal matching and congestion-aware allocation | Combines bilateral interest; controls receiver capacity; optimizes stability, social welfare, Nash welfare, or market equilibrium | Tomita et al., *Matching Theory-based Recommender Systems in Online Dating* (2022); Tomita and Yokoyama, *Fair Reciprocal Recommendation in Matching Markets* (RecSys 2024); Yang et al., *Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method* (2024); *Off-Policy Evaluation and Learning for Matching Markets* (RecSys 2025) | CyberAgent/Tapple; Wantedly; Sony | Mutual acceptance, receiver attention budgets, coverage/fairness, interference-aware evaluation | Selected-corpus/source-backed |
| Generative recommendation | Unifies retrieval/ranking or directly generates slates; aligns outputs with preference/reward models | *Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers* (ICML 2024); *OneRec: Unifying Retrieve and Rank with Generative Recommender and Preference Alignment* (2025); *GenRec: An LLM-Backed Recommendation Ranker at Netflix* (2026) | Meta; Kuaishou; Netflix | Long-term option for joint retrieval/ranking and slate interaction | Selected-corpus/source-backed; applying item-token generation to human profiles is inference |

## 2. Answers to Q1–Q8

### Q1. How does retention, LTV, or revenue become the ranking objective?

**Selected-corpus/source-backed.** The literature does not reveal one standard replacement for CTR. It shows four recurring transitions:

1. Add long-horizon heads to a shared multi-task ranker while preserving dense short-term tasks for representation learning. ESMM-family probability chains and shared-expert models are recurring primitives in the selected corpus; no ecosystem prevalence claim is made.
2. Learn a multi-objective utility or Pareto-efficient policy instead of fixing hand-tuned score weights.
3. Estimate explicit user value with zero-inflated/long-tail losses (ZILN) and ordered multi-horizon LTV heads (ODMN/MDME).
4. Optimize cumulative value using RL, item/slate Q-values, flow matching, or an aligned generative policy.

The corpus also indicates that long-run objectives are often reached indirectly: Pinterest-style downstream rewards, Netflix surrogate indices, and Spotify clickiness–stickiness make the training/evaluation loop faster without claiming that the proxy itself is the final business outcome.

**Survey inference.** The dating model should not collapse all outcomes immediately into a single opaque scalar. The initial serving utility uses calibrated 30-day binary return and 30-day net recognized revenue, with receiver-load/concentration penalties and hard safety, eligibility, and capacity constraints. The 90-day revenue head is shadow-only until a separate maturity/calibration/experiment gate. Like, match, and qualified conversation remain auxiliary or guardrail heads.

### Q2. How is a user-level delayed outcome attributed to an exposure or slate?

**Selected-corpus/source-backed.** Four mechanisms recur:

- **Sequential factorization:** entire-space models tie an impression to later funnel stages through joint probabilities and shared representations.
- **Delay-aware attribution:** DFM/ESDF/DEFER-style models use survival probabilities, day slots, or mature real negatives so unresolved outcomes are not prematurely assigned as failures.
- **Value decomposition:** SlateQ maps slate LTV to item-level values under Single Choice and Reward/Transition Dependence on Selection assumptions. Those assumptions must be checked in a dating feed, where multiple candidates can be liked and interact through congestion.
- **Trajectory reward propagation:** GFN4Retention propagates terminal cross-session return reward to intermediate session actions; Pinterest aggregates downstream behavior over a seven-day rolling window; surrogate-index methods predict long-run outcomes from early proxy vectors.

**Survey inference.** Use a hierarchy rather than one attribution rule: exposure-level supervised heads for the funnel, request/slate-level long-term loss for retention/revenue, and user-day aggregation to prevent a prolific session from receiving multiplicatively more long-term credit. Retain an explicit “unattributed/background” component because active users may return without any particular shown profile.

### Q3. Which labels and horizons should be used, and how should delay, sparsity, and censoring be handled?

**Selected-corpus/source-backed.** The corpus treats multi-day return as a long-term retention signal. Kuaishou’s *Billion-user Customer Lifetime Value Prediction: An Industrial-scale Solution from Kuaishou* uses 30/90/180/365-day cumulative revenue, while Pinterest’s *PinnerFormer: Sequence Modeling for User Representation at Pinterest* evaluates 14-day future actions and trains up to 28 days. The Netflix card confirms 1,098 test arms from 200 A/B tests but does not preserve the exact early-versus-mature horizons, so those are **Not specified in source** here. Revenue is zero-inflated and heavy-tailed in *A Deep Probabilistic Model for Customer Lifetime Value Prediction*. Chapelle’s DFM and later delayed-feedback cards show that immature outcomes require censoring/delay treatment rather than automatic negative labels.

**Survey inference — recommended dating labels:**

| Head | Label | Horizon | Delay/censoring treatment | Purpose |
|---|---|---:|---|---|
| Return | Any active return after the exposure day | 1, 7, 14, 30 days | Maturity mask or survival/day-slot likelihood | Separates fast habit from durable return |
| Active depth | Number of active days or qualified sessions | 7 and 30 days | Count likelihood plus observation-window mask | More informative than one binary return |
| Reciprocal outcome | Like, mutual match, qualified conversation | Same session; 1, 7 days | Entire-space cascade; real negatives only after maturity | Dense/sparse auxiliary supervision |
| Subscription revenue | Net recognized subscription revenue | 7, 30, 90 days | ZILN or hurdle distribution; refund/cancel maturity | Recurring monetization |
| A-la-carte revenue | Net spend on boosts, super likes, and similar products | 7 and 30 days | ZILN/hurdle distribution; purchase-delay mask | Captures non-subscription value |
| Success/quality guardrail | Durable reciprocal-quality proxy, complaint/block rate, and app-exit-with-success proxy where measurable | 7 and 30 days | Separate head; do not equate churn with failure | Prevents the “success paradox” from rewarding unnecessary tenure |

The primary production objective should use 30-day retention and 30-day net revenue, while 1/7/14-day heads regularize and accelerate learning. A 90-day revenue head can be trained and calibrated offline before it affects serving. The exact qualified-conversation and success labels are **Not specified in source** and require product definition.

### Q4. How are short-term and long-term heads combined?

**Selected-corpus/source-backed.** The observed design space is:

- fixed or manually chosen weights, which are simple but unstable across objectives and segments;
- shared-bottom multi-task models and MMoE/PLE-style task-specific gates;
- Pareto-efficient, constrained, stochastic-label, or distillation-based multi-objective ranking;
- RL-based fusion that learns weights/policies against long-term reward;
- one generative/value model, an emerging but operationally expensive direction.

**Survey inference.** Use separate calibrated heads with a learned monotone utility layer constrained by business guardrails. This is “one model” without erasing observability. Do not start with a single unconstrained value head: it hides whether a score shift came from short-term engagement, retention, revenue, or congestion and makes the success paradox difficult to diagnose.

### Q5. Where does incrementality sit inside the ranker?

**Selected-corpus/source-backed.** The corpus distinguishes predict-then-optimize from treatment-effect ranking. RERUM uses revenue-distribution modeling and a rankability objective for uplift. ESCM² applies IPS/DR corrections in an entire-space architecture. CFRR estimates pair-level propensities and uses self-normalized IPS, with truncation or doubly robust augmentation, to correct the historical overexposure of popular profiles. The corpus also warns that conventional outcome losses rank high-propensity users, not necessarily persuadable users.

**Survey inference.** The present uplift model begins as a frozen audit benchmark, not a teacher, feature, or serving input. Teacher/feature use is allowed only when treatment, control, unit, horizon, eligibility, and labels align; predictions are out-of-fold; randomized-arm calibration and leakage checks pass; and an ablation shows value over ordinary heads without harming overlap, safety, quality, or load. Only after explicit randomized exposure provides adequate support should a bilateral incremental-value head be considered. Never reinterpret a conditional retention head as causal lift.

### Q6. How should the system be evaluated offline and online under slow effects and interference?

**Selected-corpus/source-backed.** Benchmarks represented in the selected corpus—Criteo conversion/uplift, Ali-CCP/Taobao, MovieLens/Netflix, Hillstrom, KuaiRand/KuaiRec, and specialist matching logs—test isolated method properties but do not reproduce a dating market. Matching-market OPE uses staged estimators such as DiPS/DPR for sparse bilateral reward; CFRR uses pair-level SNIPS. TSPR and marketplace-interference theory show that prioritized ranking or one-side randomization has identifying assumptions and residual bias. Interleaving can diagnose rank preference but does not solve marketplace interference.

**Survey inference — evaluation stack:**

| Layer | Metrics/tests | Required guardrail |
|---|---|---|
| Per-head prediction | AUC/PR-AUC and calibration for binary heads; normalized Gini, deciles, calibration, and tail error for revenue; error by label age/horizon | Slice by activity, tenure, market, payer status, and receiver popularity |
| Ranking | NDCG/Recall at k for like/match/conversation; value-weighted NDCG; receiver coverage and exposure Gini; expected receiver load | Report both viewer and receiver outcomes |
| Incrementality/OPE | IPS/SNIPS/DR with effective sample size, weight tails, overlap, and sensitivity analyses; staged DiPS/DPR for like→reciprocation | Refuse policy conclusions when overlap/effective sample size is inadequate |
| Surrogates | Historical experiment effect correlation, directional agreement, ship-decision consistency, and segment fragility; compare against early observations of the target itself | Mature R30/V30 and shadow V90 holdouts remain the authority |
| Online | Interleaving/prioritized ranking only for short-run diagnostics; persistent market clusters for total policy effects under interference | Track active-viewer direct, passive-receiver spillover, and cross-cluster effects with 95% intervals |
| Business outcome | 7/14/30-day return; 30/90-day revenue; matches, qualified conversations, blocks/reports, receiver load, and coverage | Never accept revenue/retention wins with degraded reciprocal quality or concentrated burden |

### Q7. What is specific to two-sided or reciprocal markets?

**Selected-corpus/source-backed.** A dating recommendation is not a one-sided item click. Both users are decision-makers; the receiver’s attention is limited; popularity creates feedback loops; and changing one viewer’s ranking changes the opportunity set of others. Reciprocal systems combine both sides’ probabilities, use stable matching/social-welfare/equilibrium formulations, and constrain receiver capacity. Offline estimators must model both the initial action and reciprocation. Ordinary user-level A/B tests violate SUTVA because treatment and control share the same candidate pool.

The literature also describes the **success paradox**: a better long-term match can shorten product tenure and lower revenue. Retention is therefore not a sufficient north star for dating quality.

**Survey inference.** The unified score should be pair- and market-aware:

\[
U(A,B)=w_r z_s(\hat p_{R30})+w_v z_s(\widehat{E}[V30])-\lambda_L z_s(\hat L_B)-\lambda_C z_s(\hat C_B),
\]

where robust segment normalization is fitted on training data and clipped, $w_r,w_v\ge0$, and the load/concentration penalties are non-negative. Eligibility, safety, and receiver capacity are hard constraints outside the tradable utility. V90 is shadow-only. This is a design proposal, not a source-reported formula.

### Q8. What migration path is supported?

**Selected-corpus/source-backed.** The selected corpus contains the component steps, though not one dating-company migration: auxiliary multi-task heads; entire-space/deferred-label learning; distillation; downstream reward or surrogate models; off-policy correction; reciprocal re-ranking; and, later, RL or generative policies. Their ordering below is survey inference.

**Survey inference — staged migration:**

| Stage | System change | Data prerequisite | Release criterion and measurement |
|---|---|---|---|
| 0. Instrumentation | Freeze exposure/request IDs; log full eligibility sets, assignment, ranks, known propensities, both-side actions, label maturity, Finance events, and receiver load; start a safety-approved exploration bucket | Deterministic joins and explicit randomized assignment | Replay reproduces assignment/propensities; completeness, support, and leakage tests pass |
| 1. Shadow long-term heads | Add separate R30 binary, active-day count, qualified-conversation, V30, and shadow V90 heads; serving unchanged | Mature cohorts and accounting/censoring pipeline | Temporal calibration, count dispersion, tail error, and segment stability versus user-only baselines |
| 2. Learned multi-objective reranker | Use normalized R30/V30 in a frozen constrained utility; keep V90 shadow and the uplift model audit-only; old blend remains champion | Stable shadow metrics and receiver-load/capacity features | Safety/quality non-inferiority, load caps, offline value/ranking lift, and latency |
| 3. Reciprocal allocation | Add bilateral compatibility and receiver-capacity/congestion penalty or constrained post-processing | Reliable both-side response models | Match/conversation lift without receiver overload, fairness loss, or safety regression |
| 4. Incremental objective | Add cross-fitted DR/SNIPS pair-exposure heads only for the defined eligible request–candidate intervention; keep uplift audit-only unless strict alignment/ablation conditions pass | Logged randomized exposure with validated propensity, overlap, and ESS | Cluster-robust 95% CI, weight/ESS diagnostics, and agreement with a powered market-cluster experiment |
| 5. Direct policy optimization | Optimize slate/request value using SlateQ/GFN or a conservative actor-critic | OPE predicts online direction; trusted reward model | Long-term holdout gains, policy safety, no proxy gaming, acceptable latency |
| 6. Generative unification (optional) | Unify retrieval/ranking or generate slates with reward alignment | Mature semantic IDs, reward model, large serving budget | Clear incremental benefit over Stage 5, robustness to popularity drift and interest amnesia |

## 2.1 Operational definitions and identification gates

These are **survey-proposed project definitions**, not source claims.

| Quantity | Definition | Loss / maturity |
|---|---|---|
| Binary return R30 | 1 when the member starts at least one user-initiated qualified session on days 1–30 after the anchor request; qualified means at least 30 foreground seconds or one core action; same-day-only use does not count | Bernoulli cross-entropy plus calibration; mature after day 30; exclude bots, tests, fraud, and invalidated sessions |
| Engagement count | Number of distinct qualified active days in days 1–30; do not mix this count with binary return | Negative-binomial loss unless dispersion supports Poisson; day-30 maturity mask |
| Qualified conversation | Mutual match followed within seven days by at least two non-deleted messages from each member | Entire-space binary head; cohort matures seven days after match; spam/safety-deleted messages excluded |
| Success exit | Explicit “met someone / in a relationship” deactivation reason, or both-side product confirmation of an in-person date within 30 days | Binary guardrail; missing is missing, not negative; inactivity alone never implies success |
| Receiver load | Predicted distinct inbound likes in the next 24 hours divided by B’s trailing-28-day response-safe capacity; open matches and active qualified conversations are secondary diagnostics | Count/regression model, daily refresh, conservative segment prior for cold start; soft penalty plus approved hard cap |
| Net recognized revenue V30/V90 | Finance-ledger subscription revenue recognized daily plus recognized a-la-carte revenue, less refunds, credits, chargebacks, and indirect taxes | ZILN/hurdle-lognormal; mature after horizon plus Finance-approved accounting lag; V90 shadow-only initially |

The initial utility uses robust within-segment median/IQR normalization fitted only on training data, clipped to a pre-registered range. Retention/revenue weights are non-negative and learned in shadow mode, then frozen per ramp. Receiver load and concentration are soft penalties. Legal/age/distance/preference eligibility, blocks, safety exclusions, availability, and receiver capacity are hard constraints. Safety/quality promotion requires pre-registered non-inferiority margins: the upper 95% bound for block/report harm stays below its margin, the lower 95% bounds for qualified conversation and reciprocal quality stay above theirs, severe-event escalation does not trigger, and load p95/p99 remain under approved caps.

For causal learning, treatment is placing eligible candidate B in viewer A’s randomized top-K set versus retaining eligibility without top-K display for the request. The unit is the eligible request–candidate pair; eligibility must be invariant across arms. The pair estimand is the conditional effect on viewer/receiver R30/V30 within the exploration population, not the total market effect. Propensities come from the assignment service and must pass replay, sum-to-one/support, and empirical calibration checks. Proposed promotion criteria are $0.05\le e(X)\le0.95$, stabilized-weight ESS at least 1,000 and at least 10% of raw eligible pairs overall and per launch-critical slice, cross-fitted DR/SNIPS, viewer/receiver-clustered 95% intervals, cluster-bootstrap sensitivity, and reported clipping/weight-tail diagnostics.

The launch estimand is separate: persistent market clusters use the new policy versus the current blend for all eligible requests. Clusters combine geography, reciprocal-preference pools, and interaction-graph connectivity to minimize cross-arm edges. Report direct active-viewer and passive-receiver effects plus total 30-day value per eligible member. Pair OPE, viewer randomization, prioritized ranking, and interleaving do not identify total spillovers.

## 3. Ranked candidate architectures

### Rank 1 — Reciprocal multi-task LTV ranker with delayed-label heads

**Objective.** Initial serving utility uses calibrated 30-day binary return and 30-day net recognized revenue. The 90-day revenue head is shadow-only. Receiver-load and concentration terms are soft penalties; safety, eligibility, and capacity are hard constraints; qualified conversation and reciprocal quality are non-inferiority gates.

**Architecture.** Shared embeddings and task-specific experts; explicit heads for like, match, qualified conversation, binary return, active-day count, V30, shadow V90, bilateral response, and success-quality guardrails. Use entire-space funnel losses and delayed-label maturity masks. A monotone utility/reranking layer combines training-only robust-normalized R30/V30 outputs, while receiver load/concentration are penalties and hard filters/caps are applied outside the tradable utility.

**How it absorbs the current system.** Existing CTR/CVR heads become auxiliary tasks. The current uplift model is initially a frozen audit benchmark only. It may become a stop-gradient teacher or feature only with aligned treatment/unit/horizon/eligibility/labels, out-of-fold predictions, randomized-arm calibration, leakage checks, and a successful ablation. The external hand blend disappears only after the constrained utility passes shadow and cluster-experiment gates.

**Data needed.** Full eligible/candidate sets; assignment and logged propensities; both-side actions; user-day retention; Finance-defined net recognized revenue with accounting maturity; receiver load/capacity; randomized exposure; safety and quality guardrails.

**Main risk.** The model can learn conditional user propensity rather than exposure effect, and a chosen short-term surrogate can fail. It is also vulnerable to task conflict and the success paradox.

**Evidence split.** MMoE/ESMM, ZILN/ODMN, delayed-feedback models, and congestion mechanisms are source-backed components. Their assembly into this dating architecture and its rank are survey inference.

### Rank 2 — Bilateral causal-LTV ranker

**Objective.** Rank eligible request–candidate pairs by the conditional effect of randomized top-K exposure on viewer and receiver R30/V30, while separately estimating the cluster-level total-market policy effect. V90 remains shadow until its own gate.

**Architecture.** Shared reciprocal encoder with potential-outcome heads for exposure/no exposure; pair-level propensity model; SNIPS/DR training; entire-space funnel auxiliaries; a constrained reciprocal allocator or reranker. Revenue response uses a zero-inflated long-tail likelihood.

**How it absorbs the current system.** The uplift model remains an audit benchmark unless the strict alignment, cross-fitting, calibration, leakage, and ablation conditions pass. CTR/CVR heads remain outcome/nuisance and representation-learning tasks; the randomized assignment service—not a CTR/CVR head—supplies authoritative propensities.

**Data needed.** Randomized or quasi-random candidate exposure, logged propensities, non-exposed eligible pairs, both-side outcomes, market capacity and interference descriptors, long-horizon retention/revenue.

**Main risk.** Positivity failures and high-variance weights can silently produce unstable rankings; pair-level counterfactuals do not by themselves solve market-wide interference.

**Evidence split.** RERUM, ESCM², CFRR, DiPS/DPR, and SNIPS/DR are source-backed. A single bilateral retention/revenue treatment-effect ranker is survey inference.

### Rank 3 — Slate value/RL or generative policy

**Objective.** Maximize discounted cross-session reciprocal value for a generated slate or request, including retention, revenue, mutual quality, and congestion penalties.

**Architecture.** SlateQ-style decomposed item Q-values or GFN flow matching over session trajectories; conservative off-policy learning; optionally HSTU/OneRec-style sequence encoder and slate generator with reward-model alignment.

**How it absorbs the current system.** Current supervised heads initialize representations, choice models, and the reward model. The uplift model remains an audit benchmark unless the strict treatment-alignment, cross-fitting, calibration, leakage, and ablation conditions above pass; even then it cannot establish market-level incremental value without experimental identification.

**Data needed.** Sequential state/action logs, logged action probabilities, candidate sets, session transitions, return/revenue terminal rewards, reward-model preference data, counterfactual/OPE infrastructure, and high-throughput serving.

**Main risk.** Credit assignment depends on assumptions that may fail when users consume multiple profiles; OPE is fragile under sparse reciprocal rewards; generative serving is expensive and susceptible to proxy gaming, popularity drift, and interest amnesia.

**Evidence split.** SlateQ, Top-K off-policy correction, GFN4Retention, HSTU, and OneRec are source-backed. Applying them end to end to human-profile ranking is survey inference.

## 4. All-reference comparison

The structurally complete [comparison table](comparison-table.md) contains exactly one linked row for each of the 120 selected sources and all 13 required dimensions. Two rows—Pinterest Engineering’s *Multi-task Learning and Calibration for Utility-based Home Feed Ranking* and Meta’s *Instagram Explore Recommender System*—are metadata-only extraction failures; unsupported dimensions remain **Not specified in source**. The remaining 118 cards contain substantive indexed extraction, but some fallback cards retain placeholders or incomplete dimensions. Therefore this table establishes deliverable presence, not 120/120 substantive evidence validation. URL validation is pending. The applicability column is survey inference.

## 5. Offline and online evaluation plan under two-sided interference

### Offline sequence

1. **Label audit:** estimate empirical maturity curves for match, qualified conversation, return, purchase, renewal, refund, and cancellation. Verify no future-only feature crosses the serving boundary.
2. **Outcome models:** compare against user-only and current-model baselines. A unified pair model must add incremental information beyond “this user usually retains/pays.”
3. **Calibration before ranking:** calibrate each horizon and side. A learned utility built from uncalibrated heads merely learns scale artifacts.
4. **Counterfactual diagnostics:** report propensity overlap, weight distribution, effective sample size, and sensitivity to clipping/truncation. Use staged DiPS/DPR for like→match where appropriate.
5. **Market replay:** compute both-side outcomes, receiver load, coverage, exposure Gini, and capacity violations. Static NDCG alone is insufficient.
6. **Surrogate backtest:** use completed experiments to compare proxy treatment effects with mature R30, V30, and shadow V90 effects overall and by lifecycle/activity/popularity segment. Report 95% intervals and decision disagreement, not only individual prediction accuracy.

### Online sequence

1. **Shadow:** forward-chain temporal holdouts and monitor normalization, calibration, maturity, and segment drift without changing ranks.
2. **Exploration/logging:** randomize eligible request–candidate top-K exposure with assignment-service propensities. Interleaving may test short-run ordering but does **not** solve market interference or approve long-horizon causal value.
3. **Power before treatment:** estimate pre-period variance, intracluster correlation, attrition, baseline rates, and business-approved MDEs. Require at least 80% power at two-sided alpha 0.05 and enough clusters for cluster-robust/randomization inference; otherwise do not interpret a null as safety.
4. **Market experiment:** randomize persistent clusters built from geography, reciprocal-preference pools, and interaction-graph connectivity; balance pre-period market tightness and both-side outcomes; monitor cross-cluster edges. Report active-viewer direct effects, passive-receiver spillovers, and total value per eligible member.
5. **Temporal holdout:** keep the primary cohort through 30 days plus Finance accounting lag, and a separate V90 shadow cohort through 90 days plus lag. Pre-period, ramp, and washout durations are fixed before assignment.
6. **Ramp:** shadow → 1% logging → 5% → 10% → 25% → 50% by whole clusters where cluster assignment is required; freeze weights within each ramp.
7. **Stop/ship:** immediately stop for severe safety escalation, assignment/propensity corruption, leakage, or hard-cap breach. Use a pre-specified sequential procedure and roll back when adjusted 95% intervals cross harm boundaries for safety, qualified conversation, either side’s R30/V30, or receiver load. Ship only when all pre-registered non-inferiority and value gates pass.

## 6. Open questions and evidence gaps

### Corpus-reported gaps

- Live online A/B evidence is scarce relative to offline simulations and static benchmarks.
- Robust OPE for sparse bilateral rewards remains immature.
- Attribution of one delayed user-level return to one exposure among many remains unresolved.
- Surrogacy assumptions can fail through unobserved confounding and user heterogeneity.
- Reciprocal models often use static preferences despite users acting as both proposers and receivers over time.
- Matching/equilibrium solvers can be too expensive at industrial scale.
- Highly active users dominate logs, biasing retention labels away from users most at risk of churn.
- Streaming models face temporal gradient dependence and forgetting as delayed positives arrive after earlier updates.
- Strategy-proofness is understudied: observed likes may reflect anticipated competition rather than true preference.

### Dating-specific gaps inferred from the corpus

- No source in the permitted synthesis documents an end-to-end dating ranker trained directly on both long-horizon incremental retention and incremental revenue.
- The causal meaning of “no exposure” for one viewer-candidate pair is unclear when either user can encounter the other later or through another surface.
- The success paradox needs a measurable quality/success outcome; retention alone can reward frustrating users into staying.
- Market-wide interference is not solved by pair-level propensity correction.
- Receiver-capacity constraints need a product definition: expected likes, conversations, concurrent matches, or attention time.
- Paid-feature exposure can change both the recommendation policy and the outcome mechanism, complicating revenue incrementality.
- Sparse safety harms and distributional fairness must be modeled as constraints, not merely averaged into value.

## 7. Top-10 reading order

This order is optimized for the migration decision, not chronology. Venue details are included only where supported by the permitted raw synthesis or shared requirements.

1. **Xiao Ma et al., *Entire Space Multi-Task Model: An Effective Approach for Estimating Post-Click Conversion Rate* (SIGIR 2018).** Establishes the dense-to-sparse entire-space funnel scaffold.
2. **Jiaqi Ma et al., *Modeling Task Relationships in Multi-Task Learning with Multi-gate Mixture-of-Experts* (2018; venue not specified in source).** Establishes learned sharing/gating for competing heads.
3. **Olivier Chapelle, *Modeling Delayed Feedback in Display Advertising* (KDD 2014).** Establishes censoring-aware delayed-outcome modeling.
4. **Siyu Gu et al., *Real Negatives Matter: Continuous Training with Real Negatives for Delayed Feedback Modeling* (KDD 2021).** Connects delay correction to fresh continuous training.
5. **Xiaojing Wang et al., *A Deep Probabilistic Model for Customer Lifetime Value Prediction* (2019; venue not specified in source).** Supplies the transferable ZILN revenue loss and evaluation logic.
6. **Kunpeng Li et al., *Billion-user Customer Lifetime Value Prediction: An Industrial-scale Solution from Kuaishou* (CIKM 2022).** Supplies ordered multi-horizon LTV structure.
7. **Athey et al., *The Surrogate Index: Combining Short-Term Proxies to Estimate Long-Term Treatment Effects More Rapidly and Precisely* (NBER Working Paper 26463, 2019).** Defines the identification assumptions behind surrogate use.
8. **Vickie Zhang et al., *Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix* (arXiv, 2023).** Provides large-scale operational evidence for early observations of a long-run target.
9. **Kazuki Kawamura et al., *Counterfactual Reciprocal Recommender Systems for User-to-User Matching* (KDD TSMO Workshop, 2025).** Connects pair-level exposure correction, reciprocity, coverage, and popularity bias.
10. ***Off-Policy Evaluation and Learning for Matching Markets* (RecSys 2025).** Provides the two-stage OPE lens needed before causal or RL deployment.

**Next readings after the first ten:** Eugene Ie et al., *SlateQ: A Tractable Decomposition for Reinforcement Learning with Recommendation Sets* (IJCAI 2019), then *Modeling User Retention through Generative Flow Networks* (KDD 2024). They are intentionally later because the project should first establish labels, delay handling, reciprocity, and trustworthy OPE.

## 8. Final conclusion

**Selected-corpus/source-backed.** The selected corpus contains building blocks for multi-task funnels, delayed labels, LTV distributions, surrogates, long-horizon credit, reciprocal ranking, and matching-market evaluation. It contains substantially weaker evidence for their end-to-end combination, particularly with online validation in a dating market.

**Survey inference.** The migration should therefore unify training and serving incrementally, not jump directly to a monolithic reward model. First make retention and revenue explicit, calibrated heads in the current ranker; then learn constrained fusion and reciprocal allocation; then introduce causal value when exposure support is adequate; and only then consider slate RL or generative ranking. The decisive technical asset is not a larger model—it is a trustworthy exposure-to-long-horizon outcome and experiment data system that preserves both sides of the market.
