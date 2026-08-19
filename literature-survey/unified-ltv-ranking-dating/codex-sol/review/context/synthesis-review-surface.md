# codex-sol synthesis review surface (refreshed)

Blocks are faithful verbatim excerpts. Line numbers are approximate source lines.

## Run metadata and URL validation

Source: `codex-sol/run-state.md`, lines 1–36; `codex-sol/url-validation.md`, lines 1–9 and resolution table.

```text
# Run State — codex-sol

- model_identifier: codex-sol
- runtime_model_family: gpt-5.6-sol
- topic_slug: unified-ltv-ranking-dating
- workplace: `codex-sol/`
- notebook_id: 67046a44-7490-4fe5-b54a-3f39ef37fdd3
- notebook_source_count: 146
- date_completed: 2026-08-18
- overall_status: Phase 4/5 complete
- card_status: complete with 118 source-evidence cards and 2 explicit metadata-only extraction failures
- comparison_status: 120 linked rows for 120 selected sources
- coverage_status: 31/31 requirements = 100%
- selected_source_count: 120 unique sources
- selected_sources_with_credible_urls: 120
- academic_source_count: 23
- industry_source_count: 97 (80.8%; floor 72 met)
- D1_count: 17 including 2 dual-tagged D1/D5
- D2_count: 22
- D3_count: 10
- D4_count: 11
- D5_count: 9 including 2 dual-tagged D1/D5
- D6_count: 10
- D7_count: 14
- D8_count: 22

totals: Working=120; Unreachable=0; Ambiguous=0
resolution: Verified working=24; Replacements=2; Unresolved=0
```

## Executive summary: utility, architectures, labels, uplift, causal design

Source: `codex-sol/executive-summary.md`, lines 16–21, 55–72, 85–106, 123–153.

```text
The preferred first production candidate is a **reciprocal multi-task LTV ranker** whose initial serving utility uses only calibrated **30-day binary return** and **30-day net recognized revenue**. Like, match, qualified conversation, engagement-count, receiver-load, and safety/quality heads provide auxiliary supervision or constraints; a 90-day revenue head is shadow-only until maturity, calibration, and surrogate gates are passed.

The recommendation is **not** to replace the current ranker with RL, a generative policy, or an unvalidated causal head on day one. The first system should be a constrained learned reranker with explicit outcome heads, maturity-aware labels, and receiver-side load/safety controls.

## Three ranked candidate architectures

| Rank | Architecture | Objective and labels | How it absorbs the current stack | Data needed | Main risk |
|---:|---|---|---|---|---|
| 1 | Reciprocal multi-task LTV ranker | Initial utility: 30-day return + 30-day net revenue; 90-day revenue shadow-only; hard eligibility/safety/capacity constraints | CTR/CVR heads remain auxiliaries. Current uplift is initially an audit benchmark, not a teacher or serving feature. | Exposure/candidate sets, both-side actions, maturity, finance-defined net revenue, receiver load, safety/quality, exploration bucket | Propensity masquerades as lift; surrogate failure; task conflict; success-paradox gaming |
| 2 | Bilateral causal-LTV ranker | Incremental 30-day viewer and receiver value under a defined pair-exposure intervention, plus cluster-level total-market policy effect | Add cross-fitted propensity/outcome heads only after randomized logging passes overlap and ESS gates | Randomized exposure, pair propensities, eligible non-exposed pairs, both-side outcomes, market descriptors | Pair estimands do not identify market interference |
| 3 | Slate value/RL or generative policy | Discounted cross-session reciprocal value with explicit congestion and safety constraints | Supervised Rank 1 initializes representations/reward models; causal claims still require experiments | Sequential states/actions, logged action probabilities, terminal outcomes, validated reward model, robust OPE, serving budget | Reward hacking, fragile OPE, interference, latency, popularity drift |

## Initial serving utility

The initial serving utility is intentionally narrow:

\[
U_0 = w_R \hat p_{R30} + w_V \widehat{E}[V30] - C_{load} - C_{risk}
\]

- $\hat p_{R30}$: calibrated probability of 30-day binary return.
- $\widehat{E}[V30]$: calibrated expected 30-day net recognized revenue.
- $C_{load}$: receiver-load and concentration penalty.
- $C_{risk}$: safety, eligibility, and quality constraints.

## Operational labels, losses, and maturity

| Outcome | Operational definition | Loss / handling |
|---|---|---|
| 30-day binary return (R30) | 1 if the member starts at least one user-initiated qualified session on days 1–30 after the anchor request; a qualified session has at least 30 foreground seconds or one core action. Same-day activity alone does not qualify. | Bernoulli cross-entropy with calibration loss; day-30 maturity mask. |
| 30-day engagement count | Number of distinct qualified active days in days 1–30; session count may be a separate diagnostic, not mixed into this label | Negative-binomial count loss; Poisson only if dispersion diagnostics support it; day-30 maturity mask. |
| 30-day net recognized revenue (V30) | Ledger revenue recognized in days 0–30: daily-recognized subscription revenue plus recognized a-la-carte revenue, minus refunds, credits, chargebacks, and indirect taxes under Finance policy | ZILN or hurdle-lognormal likelihood; report payer calibration and payer/nonpayer slices. |

## Role of the current uplift model

The current uplift model is initially a **frozen audit benchmark only**. Report correlation, calibration by treatment arm, policy-value estimates, and disagreement slices against ordinary outcome heads and the randomized experiment. Do not feed its score into Rank 1 serving or training by default.

## Causal intervention and estimands

- **Intervention:** all eligible requests in a persistent market cluster use Rank 1/2 versus the current CTR/CVR plus uplift-blend policy.
- **Primary estimand:** intent-to-treat change in total 30-day net value per eligible member, reported separately for active viewers and passive receivers, with R30, V30, qualified conversation, safety, coverage, and receiver-load components.

## Online evaluation under interference

- **Temporal validation:** use forward-chaining offline holdouts; a minimum 30-day outcome window plus accounting lag for the primary test; keep a 90-day shadow cohort plus accounting lag; include a pre-period and post-ramp washout chosen before assignment.
```

## Literature review: Rank-1 horizon consistency and evaluation

Source: `codex-sol/literature-review.md`, lines 60–99, 113–181, 183–225.

```text
### Q1. How does retention, LTV, or revenue become the ranking objective?

The corpus contains three recurring patterns: explicit long-horizon value heads, learned multi-objective fusion, and sequential value/policy optimization. The project should combine these patterns rather than assume that a single scalar long-term target is sufficient.

**Survey inference.** The dating model should not collapse all outcomes immediately into a single opaque scalar. The initial serving utility uses calibrated 30-day binary return and 30-day net recognized revenue, with receiver-load/concentration penalties and hard safety, eligibility, and capacity constraints.

### Q3. Which labels and horizons should be used, and how should delay, sparsity, and censoring be handled?

**Selected-corpus/source-backed.** The corpus treats multi-day future action as a long-term retention signal. Kuaishou’s *Billion-user Customer Lifetime Value Prediction from Kuaishou* uses 30/90/180/365-day cumulative revenue, while Pinterest’s *PinnerFormer* uses multi-day future-action windows. DFM/ESDF/DEFER/DEFUSE provide survival, elapsed-time, real-negative, or label-correction mechanisms for delayed outcomes.

The primary production objective should use 30-day retention and 30-day net revenue, while 1/7/14-day heads regularize and accelerate learning. A 90-day revenue head can be trained and calibrated offline before it affects serving. The exact qualified-conversation and success labels are **Not specified in source** and require product definitions.

### Q5. Where does incrementality sit inside the ranker?

Outcome prediction and incrementality are separate estimands. Causal correction can enter ranking through uplift objectives, IPS/DR learning, or pair-level reciprocal SNIPS/DR, but a bilateral incremental retention/revenue head is not documented end to end and requires randomized support.

### Q6. How should the system be evaluated offline and online under slow effects and interference?

Offline evaluation should report calibration, rare-outcome discrimination, revenue tail behavior, reciprocal coverage/load, and OPE support diagnostics. Online evaluation should randomize at a persistent market-cluster level when viewer-level randomization spills through shared receivers; report active viewers and passive receivers separately.

## 2.1 Operational definitions and identification gates

The launch estimand is separate: persistent market clusters use the new policy versus the current blend for all eligible requests. Clusters combine geography, reciprocal-preference pools, and interaction-graph connectivity to minimize cross-arm edges. Report direct active-viewer and passive-receiver effects.

## 3. Ranked candidate architectures

### Rank 1 — Reciprocal multi-task LTV ranker with delayed-label heads

**Objective.** Initial serving utility uses calibrated 30-day binary return and 30-day net recognized revenue. The 90-day revenue head is shadow-only. Receiver-load and concentration terms are soft penalties; safety, eligibility, and capacity are hard constraints; qualified conversation and reciprocal quality remain explicit heads or guardrails.

### Rank 2 — Bilateral causal-LTV ranker

**Objective.** Rank pairs by incremental 30-day retention and incremental 30/90-day revenue, jointly for viewer and receiver, under coverage/load constraints.

### Rank 3 — Slate value/RL or generative policy

**Objective.** Maximize discounted cross-session reciprocal value for a generated slate or request, including retention, revenue, mutual quality, and congestion penalties.
```

## Q1–Q8 claim-evidence links

Source: `codex-sol/claim-evidence-table.md`, lines 9–25.

```text
This table makes the synthesis auditable at claim level. “Selected-corpus evidence” means a linked card supports the stated mechanism or empirical result; it does not establish ecosystem-wide prevalence. Dating-system designs and ordering decisions are explicitly labeled **survey inference**.

| Question | Exact retained claim | Linked source cards | Supported scope | Evidence / inference boundary |
|---|---|---|---|---|
| Q1 — long-term objective | The selected corpus contains three concrete ways to move beyond a fixed CTR/CVR blend: learn request-specific fusion against a longer-horizon reward, add explicit long-horizon value heads, or optimize sequential value. | BatchRL-MTF; ODMN; GFN4Retention | These papers demonstrate components in short-video/LTV systems; they do not establish which approach is most common across industry. | Choosing a reciprocal multi-task LTV ranker as Rank 1 is survey inference. |
| Q2 — credit assignment | Selected papers use funnel factorization, request-to-item future-impact decomposition, slate-value decomposition, or trajectory reward propagation to connect delayed/request-level value to decisions. None solves attribution of a dating user’s later return across many interfering profile exposures. | ESMM; FID; SlateQ; GFN4Retention | Source-backed for each stated decomposition within its assumptions and domain. | The proposed hierarchy is survey inference. |
| Q3 — labels and horizons | The selected cards support multi-day future-action labels, 30/90/180/365-day cumulative revenue, zero-inflated heavy-tailed value losses, and censoring-aware delayed outcomes. They do not specify the project’s exact qualified-conversation or success-exit label. | PinnerFormer; ODMN; ZILN; DFM | Horizons/losses are source-backed in their original one-sided domains. | Dating definitions and initial 30-day serving horizon are survey inference. |
| Q4 — fusion | The selected corpus contains fixed-score replacement through learned RL fusion, multi-objective distillation, stochastic label aggregation, and explicit multi-task heads. It does not show that one fusion method is universally dominant. | BatchRL-MTF; MOLD; SLA | Mechanisms and source-specific evaluations only; no ecosystem frequency claim. | The constrained monotone utility is survey inference. |
| Q5 — incrementality | Selected sources place causal correction inside ranking through revenue-uplift objectives, IPS/DR entire-space learning, or pair-level reciprocal SNIPS/DR. Conditional outcome prediction remains distinct from treatment-effect estimation. | RERUM; ESCM2; CFRR | Source-backed for original treatment/outcome definitions and logged-data assumptions. | Bilateral incremental 30-day heads are survey inference contingent on randomized support. |
| Q6 — evaluation | Selected papers show staged OPE for sparse bilateral rewards and quantify bias/variance problems in two-sided experiments. Pair-level OPE and interleaving do not identify market-wide spillovers. | DiPS-DPR; Two-Sided Experiment Bias-Variance; TSPR; Netflix SI | Source-backed for estimator/design properties; TSPR evidence is semi-synthetic. | Experiment, thresholds, and cluster construction are survey inference. |
| Q7 — two-sided constraints | Direct dating and adjacent-market cards show bilateral acceptance, congestion, exposure concentration, receiver capacity, and opportunity fairness can change ranking value beyond pair relevance. | ECDA; Fair Reciprocal NSW; Rental Congestion; CFRR | Source-backed for matching, fairness, and congestion mechanisms. | Receiver-load penalties and success-quality gates are survey inference. |
| Q8 — migration | The corpus supports individual migration components but no linked source documents the exact end-to-end dating migration. | BatchRL-MTF; MOLD; DiPS-DPR; GFN4Retention | Component-level evidence only. | The six-stage order and release gates are survey inference. |
```

## Repaired representative comparison rows

Source: `codex-sol/comparison-table.md`, lines 72 and 90.

```text
| 41 | [PinnerFormer: Sequence Modeling for User Representation at Pinterest](read-papers/2022_KDD_PinnerFormer_Sequence-Modeling-User-Representation.md) | 2022; Pinterest; industry paper; D4; priority 1; Related; [source](https://arxiv.org/pdf/2205.04507) | Limitations of Myopic "Next Action" Prediction: Traditional sequential recommender models are optimized to predict a user's immediate next action . Extreme Infrastructure and Computational Cost: Serving sequential models in real time is computationally expensive, requiring the system to fetch a user's entire history and perform inference on complex models… | Its dense all-action objective targets a window of future engagements, allowing daily batch embeddings to retain much of the value of real-time sequence inference. | Not specified in source | Input and Feature Encoding The model takes a user's sequence of actions \\(AU = \{A1, A2, \dots, AS\}\\) over the past year, truncated to the \\(M\\) most recent actions . Model Architecture Transformer Core: Projected features are added to learnable positional encodings to form \\(V^{(0)} \in \mathbb{R}^{M \times H}\\) . The sequence is processed through alternating multi-head self-attention… | Input and Feature Encoding The model takes a user's sequence of actions \\(AU = \{A1, A2, \dots, AS\}\\) over the past year, truncated to the \\(M\\) most recent actions . It focuses on predicting positive engagement: Pin saves (Repins), close-ups lasting \\(>10\\) seconds, and link clicks lasting \\(>10\\) seconds on the Homefeed . | Evaluation Dataset & Setup: Evaluation Window: Disjoint evaluation cohorts are constructed at a fixed training end-time \\(t\\) . Comparison Baselines: PinnerSage (Previous Production Champion): A multi-embedding clustering model . To evaluate accuracy, it uses an oracle baseline selecting the closest of \\(c\\) user clusters (e.g., 5 or 20 clusters) to the positive pin . | (1) Key Quantitative Results and Improvements over Baselines Offline Evaluation (Recall@10, Diversity, and Coverage): PinnerFormer vs. PinnerSage (Table 1): The single-embedding PinnerFormer significantly outperforms the previous multi-embedding PinnerSage baseline on the 14-day engagement task . Even when evaluating PinnerSage using an optimistic oracle selection over 5 or 20 clusters,… | Offline Evaluation (Recall@10, Diversity, and Coverage): PinnerFormer vs. Even when evaluating PinnerSage using an optimistic oracle selection over 5 or 20 clusters, PinnerFormer achieves a Recall@10 of 0.229, compared to 0.026 for PinnerSage (5 clusters) and 0.046 for PinnerSage (20 clusters) . Daily Batch Gap (Table 2): A sequential model trained on standard next-item prediction (SASRec) suffers a severe 13.9% performance drop in Recall@10 when moving from real-time updates to daily batch… | Survey Inference: Dating Recommender Alignment: Viewer A’s sequential swiping stream (skips, likes, matches, chats) can be compiled chronologically. PinnerFormer's multi-day target horizon aligns perfectly with tracking whether viewer A will establish a delayed, high-value connection (e.g., active chat or subscription) with candidate B over a 7-to-30 day window. | Unavailable dimensions are marked Not specified in source; dating transfer is survey inference. |
| 59 | [Modeling Delayed Feedback in Display Advertising](read-papers/2014_KDD_DFM_Modeling-Delayed-Feedback.md) | 2014; KDD; industry paper; D7; priority 1; Related; [source](https://doi.org/10.1145/2623330.2623634) | DFM jointly fits conversion probability and a conditional exponential delay distribution using positive events and right-censored nonconversions. Recent unlabeled clicks contribute little as negatives until elapsed time exceeds their predicted delay. | DFM jointly fits conversion probability and a conditional exponential delay distribution using positive events and right-censored nonconversions. Recent unlabeled clicks contribute little as negatives until elapsed time exceeds their predicted delay. | Not specified in source | DFM jointly fits conversion probability and a conditional exponential delay distribution using positive events and right-censored nonconversions. Recent unlabeled clicks contribute little as negatives until elapsed time exceeds their predicted delay. | Recent unlabeled clicks contribute little as negatives until elapsed time exceeds their predicted delay. | Toy recovery study, empirical delay fit, seven test days with rolling three-week/≈6M-example training sets, recent-campaign slice, and several heuristics. | Design: Toy recovery study, empirical delay fit, seven test days with rolling three-week/≈6M-example training sets, recent-campaign slice, and several heuristics. Statistical validity: Calibration/NLL is appropriate for bidding; uncertainty is shown for toy simulations but not the real-data headline table. Online experiments: None. | On Criteo traffic, DFM improved NLL nearly 3% over naive training and approached an oracle; naive predictions underpredicted conversion 21%. | Core survival-model framing for weeks-long retention/payment labels and censoring at training cutoff. | Unavailable dimensions are marked Not specified in source; dating transfer is survey inference. |
```

## Structural versus substantive coverage

Source: `codex-sol/coverage-evaluation.md`, lines 12–88.

```text
The package has **31/31 structural requirements represented**. This is not a claim of complete evidence validation. Substantive indexed extraction exists for **118/120** selected sources; two selected blog sources have metadata-only failure cards. Several fallback cards contain incomplete fields. URL validation resolved **120/120** selected references: 94 responded directly over HTTP, 24 were verified as public browser-accessible sources, and 2 dead URLs were replaced with canonical primary URLs.

## Per-source artifacts — structural 3/3; substantive 118/120

| Requirement | Recorded evidence | Status boundary |
|---|---|---|
| One card per selected source | 120 Markdown card files | File presence 120/120 |
| One linked comparison row per source | 120 unique linked rows | Structural presence 120/120 |
| Required card dimensions | All 13 dimensions exist as columns | Schema present; substantive extraction 118/120 and some fallback fields incomplete |

## Research questions — structurally represented 8/8

Each question has a scoped claim, linked cards, supported scope, and inference caveat in [claim-evidence-table.md](claim-evidence-table.md).

## Outstanding validation

- Repair or re-extract incomplete comparison/card fields if 120/120 substantive evidence is required.
- Power the market-cluster experiment and quantify cross-cluster interactions.
- Validate assignment propensities, overlap, ESS, and CI coverage before causal-head promotion.
- Do not describe the package as implementation-ready or fully evidence-validated.
```

## URL resolution evidence

Source: `codex-sol/url-validation.md`, lines 8–39.

```text
## Resolution pass

Method: explicit web search/open of canonical publishers and primary mirrors; ACM/Medium bot-blocks were treated as public when an exact DOI/title record was found. Replacement URLs are canonical primary pages.

| Index | Original URL | Verdict | Replacement canonical URL | Evidence |
|---:|---|---|---|---|
| 3 | https://dl.acm.org/doi/10.1145/3726302.3731935 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 11 | https://medium.com/pinterest-engineering/multi-task-learning-and-calibration-for-utility-based-home-feed-ranking-64087a7bcbad | working-browser |  | Exact Pinterest Engineering title/page found by web search; Medium endpoint returned 403. |
| 14 | https://ai.meta.com/blog/powered-by-ai-instagrams-explore-recommender-system/ | replacement-found | https://engineering.fb.com/2023/08/09/ml-applications/scaling-instagram-explore-recommendations-system/ | Canonical primary Meta Engineering page verified. |
| 30 | https://dl.acm.org/doi/10.1145/3289600.3290999 | working-browser |  | Exact DOI bibliographic record and public arXiv mirror found; ACM endpoint returned 403. |
| 59 | https://dl.acm.org/doi/10.1145/2623330.2623634 | working-browser |  | Exact DOI bibliographic record found; ACM endpoint returned 403. |
| 69 | https://www.alphaxiv.org/overview/2309.12645v2 | replacement-found | https://arxiv.org/abs/2309.12645 | Canonical arXiv abstract/PDF verified. |
| 110 | https://dl.acm.org/doi/10.1145/3404835.3462892 | working-browser |  | Exact DOI bibliographic record and public mirror found; ACM endpoint returned 403. |
```
