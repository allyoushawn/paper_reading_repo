# NotebookLM synthesis queries 2–4 (2026-09-17)

Scope: the new sources of this run plus five parent anchors (LiDDA, Amazon Ads MTA, CausalMTA, MAL, PVM). Answers reproduced with NotebookLM's inline citation numbers removed. Paper names are as NotebookLM gave them; affiliations were cross-checked against the per-paper cards.

## Query 2 — Industry state of the art in attribution, 2025–2026

### 1. Who published what
- LinkedIn: LiDDA (Bencina et al., 2025) — transformer DDA with MMM calibration; "From Prediction to Incrementality: Causal Optimization for Targeting" (Wei, Bencina et al., 2026) — causal DragonNet-style transformer with LP allocation.
- Amazon: Amazon Ads MTA (Lewis et al., 2025) — ensemble of ML attribution models calibrated by RCTs.
- TikTok: "Attributed, But Not Incremental" (Li et al., ADKDD 2026) — experiment-calibrated cannibalization correction (ETDC + HCA).
- Alibaba: MAL (Chen et al., CIKM 2025) — multi-task learning across attribution rules; SILVA / LOTUS (Wu et al., CIKM 2026) — LLM touchpoint selection; also (per NotebookLM) "ReAlloc" simplex uplift policy learning (Liu et al., 2026 — appears to be the Multi-channel Uplift Policy Learning paper) and CanniUplift (He et al., 2026).
- Kuaishou: ALM-MTA (Liu, Xia et al., ICLR 2026) — front-door causal MTA with an adversarial proxy mediator.
- Snap: large-scale HTE framework (Fumagalli et al., 2025) — DCN-based CATE on intention-to-treat experiment logs.
- Konitzer (2026, "Media Measurement and the Assisted Own Goal") — ambient-audience ITT experiments plus an individual-level PIE extension (NotebookLM tagged this Meta / GrowthLoop; verify against the card).
- Baidu / Renmin: PVM "Beyond Last-Click" (An et al., 2025) — prior-derived verification mechanism.

### 2. Dominant mechanisms
- Attention / transformer sequence models: LiDDA (LinkedIn); SMEO (Amazon, CIKM 2026) for sequential evidence in carousels.
- Experiment-calibrated observational models: Amazon Ads MTA (observational features → RCT targets); TikTok ETDC+HCA (proxy-variable GLMs extrapolate sparse lift to daily channel attribution).
- Front-door causal adjustment: ALM-MTA (adversarial proxy mediator Y′ plus contrastive learning to bypass unobserved system confounders).
- LLM touchpoint selection: SILVA / LOTUS (implicitly related touchpoints missed by heuristic rules).
- Multi-attribution learning: MAL (shared-bottom multi-task, supervised by Cartesian-product labels across four attribution rules).
- Mechanism design: PVM (truthful mechanism removing misreporting incentives).

### 3. Treatment of last-touch / last-click
- Operational signal to replace or correct: TikTok treats last-touch as timely but causally biased (overstates incremental growth) and applies daily cannibalization scaling. Amazon Ads MTA, LinkedIn causal targeting, and ALM-MTA replace last-touch with RCT-calibrated or front-door causal uplift. Konitzer shows last-touch creates an "assisted own goal" wedge κ = 1 − τ(1 − φ) that defunds demand-generating upper-funnel channels. PVM proves last-click is not dominant-strategy incentive compatible.
- Auxiliary label view: Alibaba MAL keeps last-click as the primary system target but adds first-click, linear, and MTA labels as auxiliary supervision (+2.6% ROI).

### 4. Calibration of observational attribution to experiments
- Target-feature calibration models: Amazon Ads MTA trains calibration models that predict RCT treatment effects from an ensemble of observational attributions. LiDDA aligns attention weights a_DDA against IPW-weighted experiment attribution a_exp.
- Daily cannibalization rate: TikTok computes C_t = 1 − Lift_t / A_t from sparse A/B lift vs. nominal attribution A_t, predicts daily channel C_t via proxy-variable GLMs, and allocates non-incremental volume hierarchically.
- Ambient randomization and PIE: Konitzer embeds ITT experiments in every activated audience via salted hashing and fits CATE models to project lift without holdouts.

### 5. Reported failure modes
- Attribution–cannibalization mismatch: credit for organic or baseline conversions (TikTok ETDC+HCA; CanniUplift).
- "Assisted own goal" / signal-loss wedge: upper-funnel demand completes off-platform, invisible to last-touch pixels (Konitzer; Amazon Ads MTA).
- Unobserved system-level confounding: backdoor adjustments (DML, IPW) fail when unobserved preferences drive both exposure and conversion (ALM-MTA).
- Strategic timestamp misreporting under last-click (PVM).
- Endogenous truncation and position bias in sequence models (SMEO).

## Query 3 — Three replacement designs for the label-generation step (NotebookLM's ranking)

### #1 User-prevalence-debiased downstream session reward (Pinterest "Downstream Rewards", 2026)
- Credit for a swipe at time t: R̂_{u,t} = Σ_{i=1..n_{u,t}} γ^{i−1} ( Σ_{a∈A_eng} w_a 1[A_{u,t+i} = a] ) − w_shallow 1[dwell_{u,t} < δ_state(u)].
- Selection bias: user-prevalence (UP) normalization x̂_{u,0} = r_{u,0} − r̃_u, subtracting each user's two-week median action density, so heavy swipers do not inflate credit through volume.
- Recurring outcome and heterogeneous touches: converts the delayed N7 return into a dense, undelayed downstream-trajectory reward; deep events weighted above shallow ones (w_message > w_match > w_like), shallow swipes penalized.
- Validation anchor: Pinterest A/B — +0.36% successful sessions, +0.35% time spent, significant DAU/WAU gains.
- Risk: dwell thresholds (δ_core = 1.0 s, δ_non-core = 0.5 s) must be calibrated per user state. Cost: medium.

### #2 Flow-matching trajectory credit (GFN4Retention, KDD 2024, Kuaishou)
- Credit via the detailed-balance loss L_DB = ( log F_R(s_t) + log P_F(s_{t+1}|s_t) − log F_R(s_{t+1}) − log P_B(s_t|s_{t+1}) − α r_t )², terminal state pinned to the retention reward.
- Selection bias: trajectory probability P(S) ∝ R_retention · e^{α Σ r_t} is aligned with the end-of-session retention reward rather than raw action frequency.
- Recurring outcome: back-propagates the return-time-gap reward through intermediate states; swipes, likes, matches, messages enter the step reward r_t = Σ ω_b y_{t,b}.
- Validation anchor: Kuaishou A/B — next-day retention +0.015% overall, +0.069% on target users; watch time +0.558%.
- Risk: high variance in continuous-action flow estimation if log offsets are miscalibrated. Cost: high.

### #3 Two-sided retention-curve marginal gain (MRet, ICLR 2026; Wantedly, RecSys in HR 2026)
- Credit for a swipe or match: Δf(x,y) = [ f_x(m_{1:τ}(x) + r(x,y)) − f_x(m_{1:τ}(x)) ] + [ f_y(m_{1:τ}(y) + r(x,y)) − f_y(m_{1:τ}(y)) ].
- Selection bias: concave retention curves (f″ < 0) give near-zero marginal credit to users already above their satisfactory match count b_x, shifting credit to users below the churn threshold.
- Recurring outcome: f(x, m) is retention probability as a function of cumulative matches; heterogeneous events modulate match probability r(x,y).
- Validation anchor: MRet — offline simulation on a real dating-platform dataset; Wantedly — live A/B with churn odds ratio 0.948–0.957 (not significant at conventional levels).
- Risk: depends on accurate per-user concave retention curves (XGBoost fit). Cost: low.

NotebookLM's "ship first" pick: #3, because it addresses selection bias through the concave curve without session-graph infrastructure and is a lightweight post-processing label layer.

## Query 4 — Selection-bias devices and evaluation without ground truth

### (A) Selection-bias devices
1. Instagram notification management (Meta): randomized 50% drop of candidate digest notifications to collect unconfounded uplift training logs; quantile score normalization for stable send rates.
2. CausalMTA (KDD 2022): journey re-weighting (IPW) for static user confounders plus invariant representation learning for dynamic features.
3. ALM-MTA (ICLR 2026): front-door mediator (adversarial proxy Y′) plus IPW to remove latent preference confounders.
4. RLUR (WWW 2023): separate policies for high- and low-activity cohorts; variance-normalized retention reward via a Markov-inequality lower bound on return time.
5. Retentive Relevance (Meta, 2025): covariate-balancing propensity scores for survey non-response; random contextual survey sampling across feed positions.
6. Taobao LTV framework (2026): position-aware debias quantile (PDQ) normalization within iso-frequency page groups.

### (B) Evaluation without per-interaction ground truth
1. Retentive Relevance: online A/B on sessions per user (+0.030%, p < 0.05, 14 days) plus 10-fold CV retention prediction.
2. RLUR: online A/B — +0.200% DAU, +0.063% 7th-day retention.
3. CDUM (Kuaishou coarse-to-fine uplift): online A/B — +0.048% Enter LT7, +0.034% next-day retention.
4. GFN4Retention: offline return-time proxy (1.893 → 1.479 days on ML-1M) and online next-day return gains.
5. TikTok ETDC+HCA: forward-in-time validation against channel-level RCT readouts — 91.38% error reduction vs. raw attribution; ~15 pp lower measured cannibalization after deployment.
6. ALM-MTA: online A/B — +0.04% DAU, +0.119% active-creator scale; offline non-personalized Shapley-sampling AUUC; precision 4.32% → 21.88% on a matching-and-activation criterion.
7. IURO (WeChat, RecSys 2023): online A/B — +0.76% next-day, +0.65% next-three-day retention.
8. Taobao LTV: online A/B — +0.21% LT3 return-visit rate.
