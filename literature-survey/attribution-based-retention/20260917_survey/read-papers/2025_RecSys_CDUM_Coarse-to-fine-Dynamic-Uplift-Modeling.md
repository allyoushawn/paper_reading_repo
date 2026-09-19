# Coarse-to-fine Dynamic Uplift Modeling for Real-time Video Recommendation

**Source:** https://arxiv.org/pdf/2410.16755.pdf | **NLM source id:** 0cd04f39-39ef-4623-9cea-98612bd68d7c | **Year / venue:** RecSys 2025 | **Authors / affiliation:** Chang Meng, Chenhao Zhai, Xueliang Wang, Shuchang Liu, Xiaoqiang Feng, Lantao Hu, Han Li (Kuaishou Technology); Chenhao Zhai, Xiu Li (Tsinghua Shenzhen International Graduate School); Kun Gai (Unaffiliated) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Video recommendation pipelines rely on non-personalized strategy modules (e.g., uniform video-duration-distribution adjustment) that ignore individual preference. Applying uplift modeling here faces two challenges: (1) user responses (watch time vs. commercialization metrics) trade off against each other, and (2) static offline daily-level features can't capture rapid real-time interest shifts. CDUM proposes two modules: Coarse-grained Preference Modeling (CPM), an offline multi-treatment module splitting treatment embeddings into guidance embeddings (filter/extract user features) and indicator embeddings (mask tower outputs) to model long-term preference; and Fine-grained Interest Capture (FIC), an online MTL module using request-level real-time context to output an interest score r_i^k that dynamically corrects the offline preference score.

Unit of credit: per user request / request-level treatment assignment (treatment = adjusting the exposure distribution across K video-duration categories), not per individual past interaction. Outcome optimized: long-term retention/engagement — Enter/Slide LT7, LT30, next-day retention, 7-day retention, app usage time, watch time. Selection/confounding bias is handled via the Neyman-Rubin potential-outcome framework, estimating individual treatment effect τ_k(x_i) = E[y_i^k|t_i^0=k,x_i] − E[y_i^0|t_i^0=k,x_i] to isolate incremental lift from organic baseline activity; the treatment-refine (guidance/indicator) mechanism further reduces multi-treatment gradient interference and exposure bias.

## 2. Evidence
- **LAZADA** (offline, e-commerce voucher): CPM QINI=0.0265, AUUC=0.0037, LIFT@30=0.0087, significantly beating best baseline SNet (QINI 0.0238, AUUC 0.0034).
- **CRITEO** (~14M ad instances): CPM QINI=0.0942, AUUC=0.0371, LIFT@30=0.0310 vs. best baseline FlexTENet (QINI 0.0924, AUUC 0.0363).
- **Kuaishou offline** (~8.5M instances/treatment group, 14-day pre-RCT window): CPM AUUC_avg=0.01143 vs. MESI 0.01053, PLE 0.00998, MMOE 0.00947, CausalForestDML 0.00914, T-Learner 0.00787.
- **Kuaishou live A/B** (18 days, 20% vs. 20% traffic, hundreds of millions of DAU): Enter LT7/LT30 +0.048%/+0.041%; Slide LT7/LT30 +0.039%/+0.041%; next-day retention +0.034%; 7-day retention +0.038%; app usage time (total/per-capita) +0.135%/+0.131%; watch time +0.188%. (At this DAU scale, 0.01%-level LT lifts are considered significant.) Ablation: removing FIC costs +0.078% app usage time / +0.129% watch time.
- Baselines: S-/T-Learner, BNN, TARNet, CFRNet, CEVAE, GANITE, DragonNet, FlexTENet, SNet, EUEN, DESCN, EFIN, CausalForestDML, Shared Bottom, MMOE, PLE, MESI.

## 3. Limitations
- User response metrics (watch time, app usage, commercialization) constrain/trade off against each other; single-treatment optimization can't balance them.
- Existing baseline uplift models show severe cross-domain performance variance (e.g., EUEN, DESCN swing between Lazada/Criteo), lacking generalizability — motivating but not fully solved by CDUM.
- Deployment scope limited to the video-duration-bucket adjustment module inside the Cascading Ranker; not yet applied to other pipeline stages (e.g., primary candidate scoring).

## 4. Prior works named
- Künzel et al. 2019 — *Meta-learners for estimating heterogeneous treatment effects using machine learning* (S-/T-/X-Learner paradigms)
- Ma et al. 2018 — *Modeling task relationships in multi-task learning with multi-gate mixture-of-experts* (MMOE, used in FIC)
- Rubin 2005 — *Causal inference using potential outcomes: Design, modeling, decisions* (Neyman-Rubin framework)
- Ke et al. 2021 (EUEN) / Zhong et al. 2022 (DESCN) / Liu et al. 2023 (EFIN) — deep uplift modeling baselines for online advertising
- Cen et al. 2020 / Li et al. 2019 / Meng et al. 2022 — multi-interest learning framework (source of guidance/indicator embedding design)

## 5. Project Relevance
- **Answers:** both
- **Attributes retention to individual interactions?** no — CDUM estimates request-level individual treatment effects for a macro strategy decision (enable/disable a duration-bucket treatment), not fractional credit across a user's individual past swipes/likes/matches.
- **Transferable components:** the coarse-to-fine two-stage paradigm (offline long-term-preference model + online real-time-interest model correcting it); the guidance/indicator treatment-refine mechanism for handling multiple heterogeneous treatments without gradient interference; use of unbiased LT7/LT30-style metrics as validation targets.
- **Required changes:** move from macro per-request bucket-enablement decisions to micro-level per-interaction sequence attribution with counterfactual credit differentials; replace average-pooled interaction embeddings with event-type-aware (swipe/like/match/message) sequence modeling; re-anchor the outcome to a daily-recurring rolling N7 retention target rather than a single treatment window.
- **On last-touch:** does not name last-touch/last-click explicitly, but critiques static offline-feature uplift models and non-causal heuristics for failing to isolate true incremental effect from organic baseline activity — directly analogous to the selection-bias critique of last-touch attribution.
- **Transfer rating:** adaptable — a request-level causal uplift framework, not a multi-touch attribution model, but its two-stage offline/online design and bias-aware treatment effect estimation are strong building blocks for retention-credit modeling.
