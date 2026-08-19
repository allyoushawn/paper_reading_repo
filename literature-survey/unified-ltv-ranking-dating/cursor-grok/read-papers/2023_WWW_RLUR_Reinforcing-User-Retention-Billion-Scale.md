# Survey Card

| Field | Value |
|-------|-------|
| **Title** | Reinforcing User Retention in a Billion Scale Short Video Recommender System |
| **Authors / Company** | Qingpeng Cai, Shuchang Liu, Xueliang Wang, Tianyou Zuo, Wentao Xie, Bin Yang, Dong Zheng, Peng Jiang, Kun Gai / Kuaishou Technology |
| **Venue / Year** | WWW 2023 |
| **URL** | https://arxiv.org/abs/2302.03322 |
| **Source type** | Industry paper |
| **Direction** | D2 |
| **Problem setting** | Kuaishou short-video feed ranking: RL agent outputs continuous 8-D score-ensemble weights per request; top-6 videos recommended; infinite-horizon session MDP minimizing cumulative returning time |
| **Objective + label + horizon + delay** | Primary: minimize inter-session returning time (proxy for retention/DAU); delayed session-end reward hours–days later; immediate reward = watch time + interactions per request; D1/D7 retention evaluated online |
| **Prediction or incrementality** | Policy optimization (DDPG-style actor–critic RL), not pointwise prediction ranking |
| **Architecture** | Actor outputs Gaussian policy over 8 ranking weights; dual critics (retention Q_T, immediate Q_I with RND intrinsic reward); separate actors for high/low activity cohorts; soft behavior-regularized off-policy training |
| **Credit assignment** | Session-level returning-time reward at last request only (γ=1 within session, γ=0.95 at terminal step); immediate heuristic + RND critics for per-step guidance; normalized retention reward divides true return time by predicted baseline |
| **Training / counterfactual** | Off-policy DDPG with soft policy-cloning weight vs behavior policy; variance reduction via predicted-return normalization; group-specific policies for activity bias |
| **Offline / online eval** | Offline KuaiRand + simulator (returning time, D1 retention); online long-run A/B vs CEM on app open frequency, DAU, D1/D7 retention |
| **Reported gains** | Offline: returning time 1.892 vs CEM 2.036 / TD3 2.009; retention 0.618 vs CEM 0.587 / TD3 0.592. Online (≈150 days): +0.450% app open frequency, +0.2% DAU, +0.053% D1 retention, +0.063% D7 retention vs CEM |
| **Dating applicability** | Closest industrial analog for optimizing delayed user return rather than per-match CTR. Weight-ensemble RL over existing scorers mirrors fusing engagement heads toward retention without retraining all pointwise models. |
| **Unverified claims** | WWW DOI in source listed as placeholder (XXXXXXX); arxiv 2302.03322 used per user hint. |

**Community Reaction:** No significant community discussion found.

---

## 1. Core Problem and Key Contribution

**Core problem:** Short-video platforms optimize **user retention** (DAU driver), but retention is long-term, noisy, biased by activity level and calendar effects, and delayed hours–days—making pointwise/listwise models and naive RL ill-suited.

**Key contributions:**
- Infinite-horizon **request-based MDP** minimizing cumulative returning time between sessions.
- **RLUR** framework addressing uncertainty (normalized retention reward), bias (separate high/low activity policies), and delay (immediate + RND critics, soft behavior regularization).
- Full production deployment on Kuaishou with sustained retention and DAU lifts.

## 2. Proposed Method or Architecture

**MDP:** State = profile + 3-request history + context + candidates. Action = 8-D weight vector in [0,4]^8 over scorers (watchtime, shortview, longview, like, follow, forward, comment, profile enter). Linear score fusion; top-6 videos shown.

**Retention critic Q_T:** DDPG TD loss; discount γ_it = 1 for non-terminal requests, γ = 0.95 at session end.

**Delayed reward handling:** Immediate reward critic Q_I with RND intrinsic exploration; actor loss L(θ) = β_T Q_T − β_I Q_I.

**Uncertainty:** Normalize returning-time reward r = clip(T / ((1−T'(x))·T_β), α) using session-level classifier T' (60th percentile threshold, α=3).

**Bias:** Separate policies π(·|θ_high) and π(·|θ_low).

**Stability:** Soft regularization exp(max{λ(log p − log p_b), 0}) · L(θ) instead of hard behavior cloning (λ=1.5).

## 3. Datasets and Baselines

**Offline:** KuaiRand logs + simulator (immediate feedback, leave, return modules; K=10 days).

**Baselines:** CEM (ranking weight search); TD3; RLUR naive (retention critic only, γ∈{0, 0.9}).

**Online:** Kuaishou production A/B vs CEM (TD3 excluded—unstable training).

## 4. Key Quantitative Results

**Offline (avg last 50 episodes):**

| Algorithm | Returning time ↓ | User retention ↑ |
|-----------|------------------|------------------|
| CEM | 2.036 | 0.587 |
| TD3 | 2.009 | 0.592 |
| RLUR (naive, γ=0) | 2.001 | 0.596 |
| RLUR (naive, γ=0.9) | 1.961 | 0.601 |
| **RLUR** | **1.892** | **0.618** |

**Online vs CEM (converged gaps):** +0.450% app open frequency; +0.2% DAU; +0.053% D1 retention; +0.063% D7 retention. Authors note 0.01% retention and 0.1% DAU improvements are statistically significant at short-video scale.

## 5. Limitations and Failure Modes

- Retention influenced by external/social factors beyond recommendation (uncertainty).
- TD3 training unstable in production; excluded from live test.
- Hard behavior-cloning regularization either fails to stabilize or hurts sample efficiency.
- Returning-time reward delayed hours–days → large off-policy distribution shift.
- Does not decompose retention to individual items; optimizes ensemble weights over existing scorers.

## 6. Top Cited Prior Works

1. DDPG (Lillicrap et al.) — actor–critic backbone.
2. TD3 (Fujimoto et al.) — continuous RL baseline.
3. CEM — production weight-tuning baseline.
4. Random Network Distillation (Burda et al.) — intrinsic exploration.
5. KuaiRand (Gao et al.) — offline evaluation dataset.
6. Prior RL-for-recsys literature (DRN, SlateQ, etc.) — cited as optimizing immediate not retention rewards.
7. Markov inequality — bound for expected returning-time predictor.

---

## Project Relevance (Q3)

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | **Retention / DAU proxy** via minimizing cumulative **returning time** between sessions; immediate CTR-like proxies (watch time, likes, follows, etc.) used as auxiliary/heuristic rewards only. |
| **(2) Credit assignment** | Session-end **returning-time reward** on last request only; immediate per-request rewards via separate critic; authors state retention is hard to decompose to items—RL optimizes **ranking-weight actions**, not per-item labels. |
| **(3) Label / horizon; delay / sparsity / censoring** | Returning time observed at next session start (hours–days delay); D1/D7 retention metrics online; uncertainty and sparsity explicitly discussed; censoring not specified in source. |
| **(4) Short-term vs long-term head fusion** | **Learned** continuous ensemble weights (8-D action) combining existing short-term scorers; dual critic weighting β_T=β_I=1.0. |
| **(5) Prediction vs incrementality** | **Policy optimization / incrementality** via RL actor adjusting ranking weights—not training new pointwise predictors. |
| **(6) Offline / online eval; delayed retention; two-sided interference** | Offline simulator + KuaiRand; long online A/B measuring delayed D1/D7 retention and DAU. Two-sided interference not specified in source. |
| **(7) Reciprocity, congestion, fairness, revenue vs match quality** | Not specified in source. |
| **(8) Migration path from CTR-like model to unified long-term model** | Keep existing pointwise scoring models; add RL layer learning **linear fusion weights** toward retention with immediate rewards as heuristic bridge. |

---

## Reverse Citation Map

*(blank)*

---

## Meta Information

| Field | Value |
|-------|-------|
| **Date analyzed** | 2026-08-16 |
| **Workplace** | cursor-grok |
| **NLM source ID** | 192447f1-df6d-4e75-a91b-b1e550047316 |
| **Notebook ID** | 67046a44-7490-4fe5-b54a-3f39ef37fdd3 |
