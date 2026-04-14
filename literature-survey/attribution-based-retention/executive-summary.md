# Executive Summary: Attribution-Based Retention Literature Survey

**Date:** 2026-04-11  
**Survey topic:** Multi-touch attribution and causal inference for user retention on a subscription/dating platform  
**Papers surveyed:** 23 papers across 4 research clusters  
**Coverage evaluation:** See Section 5

---

## 1. Core Problem

A subscription-based dating platform needs to answer: **"Which interventions (push notifications, emails, in-app prompts, match recommendations) causally increase user retention, and by how much?"** Standard attribution models (last-touch, first-touch, regression) are biased by user selection effects — users who are already engaged are targeted more and would have retained anyway. The incrementality gap (observed engagement − counterfactual engagement without intervention) is the true business metric.

---

## 2. What This Survey Found

### 2.1 The Field Has Converged on a Causal Framing

The MTA literature has moved decisively from prediction-based to causally-corrected models between 2018 and 2024:
- **2018**: DARNN, DNAMTA — pure sequence prediction, no causal correction
- **2020**: CAMTA — first GRL-based dynamic deconfounding; Criteo AUC 0.9591
- **2022**: CausalMTA — adds static deconfounding (VRAE); AUC 0.9659
- **2024**: DCRMTA — adds Causal Attention Module preserving causal user features; AUC 0.8009 (synthetic), 0.7991 (Criteo-custom)

The key architectural pattern: **Gradient Reversal Layer (GRL)** forces representations to be channel-invariant. Combined with Shapley value credit assignment, this produces causally-valid attribution weights.

### 2.2 Production-Validated Industry Methods Are Most Deployable

The highest-signal papers for a dating platform are not the most theoretically novel — they are the industry deployments with measured business outcomes:

| Paper | Production Result | Deployability |
|-------|-----------------|---------------|
| DoorDash HTE (2020) | 33% reduction in Promotional Cost/Incremental Delivery at 5% reach | Very high — S-learner + LightGBM |
| DoorDash Switchback (2022) | Incrementality scalar computed for ad calibration | Very high — alternating time design |
| Netflix Causal Survey (2022) | DML for localization; Causal Ranker for recommendations; Bellmania for LTV | High — DML is production-ready |
| CAMTA (2020) | 8.2% profit improvement on Taobao budget allocation | Moderate — requires GRL training |
| pycox/Cox-Time (2019) | Best IBS on KKBox 1.7M user churn dataset | Very high — pip install pycox |

### 2.3 Survival Analysis Is Underutilized in Attribution Systems

The MTA literature almost universally treats conversion as binary, ignoring right-censoring. For dating platform retention, every active user is a right-censored observation. **Cox-Time** (best calibration, IBS 0.107 on 1.7M-user KKBox churn) and **TEDDA** (Google's Poisson process + attribution credit) provide the missing bridge between survival analysis and multi-touch attribution. This combination is the most novel actionable gap identified in this survey.

### 2.4 Geo Experiments Provide Causal Ground Truth

The Trimmed Match + Trimmed Match Design pipeline (Google, open source) is the gold standard for measuring true channel incrementality when user-level randomization is impractical. The incrementality scalar pattern (DoorDash) provides a practical approach for channels where geo-targeting isn't available. Any MTA model deployed in production should be calibrated against such experimental measurements.

---

## 3. Recommended Methodology Stack for a Dating Platform

The optimal stack combines methods from all four research clusters:

### Step 1: Establish experimental ground truth
- Run **holdback A/B tests** (Netflix pattern) for core retention features; cumulative effect measurement over 90+ days
- Run **switchback or geo experiments** (Trimmed Match / DoorDash) for notification and ad channel incrementality
- Compute **incrementality scalars** for each channel to calibrate attribution model output

### Step 2: Build causal attribution model
- Start with **CAMTA** (ICDM 2020) — proven, code available, Criteo benchmark validated
- For features with strong user-feature confounding, upgrade to **CausalMTA** (KDD 2022)
- Use **Shapley values** for final credit assignment (tractable via JDMTA mixed exact/MC algorithm)
- Calibrate Shapley weights against experimental incrementality scalars from Step 1

### Step 3: Build churn prediction system
- Deploy **Cox-Time** (pycox package) for subscription churn with calibrated probabilities
- Use calibrated 30-day churn probability as the intervention threshold signal
- For competing risks (cancellation vs inactivity vs app delete), add **DeepHit** for discrimination

### Step 4: Targeted retention intervention
- Train **X-learner** or **DML** for heterogeneous treatment effects of retention interventions
- Identify the subpopulation who would respond to each intervention type (S-learner for simple cases, X-learner for unbalanced designs)
- Build targeting curves (audience reach vs incremental cost) as in the DoorDash pattern

### Step 5: LTV-aware discount optimization
- Apply **Bellmania/Markov chain LTV** (Netflix pattern) to price discount optimization
- Model on-platform and off-platform states using subscription/cancellation transition data
- Compute incremental LTV as the causal value of each retention intervention

---

## 4. Key Method Recommendations Summary

| Task | Recommended Method | Package / Tool | Complexity |
|------|------------------|----------------|------------|
| CATE estimation (balanced groups) | DML or Causal Forest | `econml`, `grf` | Low-medium |
| CATE estimation (unbalanced) | X-learner | `econml` | Low-medium |
| CATE (neural, high-dim) | DragonNet | PyTorch | Medium |
| MTA attribution (causal) | CAMTA → CausalMTA | Custom PyTorch | Medium-high |
| MTA attribution (interpretable) | Shapley MTA | Custom implementation | Medium |
| Churn prediction (calibrated) | Cox-Time | `pycox` | Low |
| Churn prediction (ranking) | DeepHit | `pycox` | Low |
| Geo incrementality (design) | Trimmed Match Design | `trimmed_match` | Low |
| Geo incrementality (estimation) | Trimmed Match | `trimmed_match` | Low |
| Time-series incrementality | DoorDash Switchback | Custom | Low |
| LTV optimization | Bellmania Markov chain | Custom | Medium |

---

## 5. Coverage Evaluation

### 5.1 What Is Well-Covered

- **Causal MTA sequence models**: Comprehensive — DARNN through DCRMTA; full lineage from associative to causal
- **CATE/HTE methods**: Comprehensive — all major frameworks (CFR, DML, Causal Forest, meta-learners, DragonNet, R-learner)
- **Survival analysis for retention**: Good — DeepHit + pycox; TEDDA provides the MTA bridge
- **Geo experiments**: Comprehensive — Trimmed Match estimation + design; DoorDash switchback
- **Industry applications**: Good — DoorDash (HTE + switchback), Netflix (survey covering DML, synthetic control, Causal Ranker, Bellmania)
- **Shapley MTA**: Good — Zhao et al. theoretical + JDMTA production + DeepMTA

### 5.2 Gaps in Current Coverage

The following areas are not covered in this survey and represent expansion candidates if the coverage assessment warrants it:

1. **Markov chain / HMM-based MTA** (Shao & Li KDD 2011 is paywalled; earlier probabilistic MTA baseline missing)
2. **Budget allocation optimization** (Berman 2018 equilibrium; mechanism design for attribution contracts)
3. **Reinforcement learning for sequential retention** (RL-based notification timing optimization, related to causal bandit literature)
4. **Bayesian structural time series / synthetic control** (Brodersen et al. 2015 — the Bayesian synthetic control foundation used by Google KA)
5. **Privacy-preserving attribution** (differential privacy for user-level tracking; relevant given iOS ATT changes)
6. **Long-range causal effects** (seasonal and multi-week treatment effects in dating context; not well-addressed by any surveyed paper)

### 5.3 Coverage Assessment

**Coverage of the core dating platform problem: ~80%**

- MTA and CATE methods: 95% coverage
- Survival/retention prediction: 80% coverage (DeepHit + Cox-Time; missing RL-based timing)
- Experimental design: 90% coverage (Trimmed Match + switchback + holdback)
- Industry deployment examples: 75% coverage (DoorDash, Netflix; missing Airbnb, Spotify, LinkedIn)
- LTV/Markov methods: 60% coverage (Netflix Bellmania; missing the full CLV literature)
- Privacy-aware attribution: 0% coverage

**Verdict: Coverage is sufficient to proceed.** The 23 papers cover all critical methodological areas needed for building a production attribution + retention system. The uncovered areas (RL-based timing, Bayesian synthetic control, privacy-preserving attribution) are useful extensions but not blockers.

---

## 6. Top 5 Most Important Papers for a Dating Platform Attribution System

Ranked by expected near-term business impact:

1. **CausalMTA** (KDD 2022) — Most rigorous causal MTA method with complete deconfounding pipeline; Alibaba production validation; Shapley credit assignment included
2. **pycox / Cox-Time** (JMLR 2019) — Best churn prediction calibration on subscription service (KKBox); immediately deployable via pip
3. **X-learner / Meta-learners** (PNAS 2019) — Foundational CATE framework; best method for targeting at-risk users for retention interventions
4. **DML** (EconJnl 2018) — Production-grade CATE for high-dimensional feature settings; Netflix uses this directly
5. **Trimmed Match** + **Trimmed Match Design** (Google 2021/2022) — Ground-truth incrementality validation; calibrates the attribution model; open source

---

*Survey completed: 2026-04-11. All papers in `/read-papers/`. Method scores in `method-tracker.md`. Full analysis in `literature-review.md`.*
