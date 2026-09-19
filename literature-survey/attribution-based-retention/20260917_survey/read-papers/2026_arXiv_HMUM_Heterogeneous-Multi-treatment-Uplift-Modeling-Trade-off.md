# Heterogeneous Multi-treatment Uplift Modeling for Trade-off Optimization in Short-Video Recommendation

**Source:** https://arxiv.org/pdf/2511.18997.pdf | **NLM source id:** aafa7891-e78a-4b0d-9fdd-e5b869bfa23e | **Year / venue:** arXiv 2511.18997, 2026 (Kuaishou) | **Authors / affiliation:** Chenhao Zhai, Chang Meng, Xueliang Wang, Shuchang Liu, Xiaolong Hu, Shisong Tang, Xiaoqiang Feng (Kuaishou Technology); Chenhao Zhai, Xiu Li (Tsinghua Shenzhen International Graduate School) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Industrial short-video platforms run multiple complementary recommendation strategies (heterogeneous "treatments"). Existing uplift approaches either jointly model all treatments (causing gradient conflicts from mutually exclusive effects) or model each treatment independently (missing synergies and suffering non-treatment/y0 baseline distribution shift across branches). Separately, user responses (consumption-side usage time vs. commercialization-side view counts) trade off, and fixed-weight balancing lacks personalization. HMUM has two modules: Offline Hybrid Uplift Modeling (HUM) — per-treatment branches with a feature-selection attention mechanism, jointly optimized with a KL-divergence constraint forcing non-treatment (y0) representations to align across branches; and Online Dynamic Decision-Making (DDM) — an MMOE-style network predicting real-time, user-specific response value weights w_ir that combine relative uplifts into a comprehensive score.

Unit of credit: per user request / request-level treatment assignment (treatment k ∈[1,K] = enabling/enhancing a recommendation strategy or scorer). Outcome optimized: multi-response engagement/commercialization metrics — app usage time and video view counts (plus public ad/e-commerce conversion targets). Bias handling: Neyman-Rubin potential-outcome ITE estimation τ_k^r(x_i)=E[y_ik^r|t_i=k,x_i]−E[y_i0^r|t_i=0,x_i]; trained on RCT logs with covariate re-shuffling over 7-day windows to satisfy unconfoundedness/SUTVA; KL-divergence baseline alignment removes cross-branch non-treatment noise; relative uplift scaling δ_k^r(x_i)=ŷ_ik^r/y_{0,*}^r − 1 normalizes across heterogeneous metric scales.

## 2. Evidence
- **LAZADA:** HUM QINI=0.0278, AUUC=0.0039 (best baseline SNet: 0.0238/0.0034). **CRITEO:** HUM QINI=0.0933, AUUC=0.0366 (best baseline FlexTENet: 0.0924/0.0363).
- **Kuaishou industrial dataset** (~6M instances, 14-day pre-RCT window, 2 treatments): HUM outperforms S-/T-Learner, TARNet, EFIN, M3TN on QINI/AUUC for both app-usage-time and view-count responses under both treatments (e.g., Treatment-2 app usage: HUM QINI=19.90×10⁻⁴ vs. TARNet 13.18×10⁻⁴; several baselines show negative "downlift" down to -22.14×10⁻⁴). Ablation: removing the KL term drops Treatment-1 app-usage QINI from 14.55 to 10.87.
- **Live A/B (Kuaishou):** Ranking stage (13 days): app usage time +0.044%, per-capita +0.055%, view counts +0.007%. Edge Rerank stage (8 days): app usage +0.073%, per-capita +0.072%, view counts +0.002%. Static single-strategy ablations show the trade-off HMUM avoids (e.g., Single s1: +0.125% usage but -0.227% views).
- Baselines: S-/T-Learner, BNN, TARNet, CFRNet, CEVAE, GANITE, DragonNet, FlexTENet, SNet, EUEN, DESCN, EFIN, M3TN.

## 3. Limitations
- Naive joint multi-treatment modeling causes severe negative "downlift" (gradient conflict) — motivates but is only partly solved.
- Consumption vs. commercialization metrics intrinsically conflict; single-objective optimization fails regardless of model.
- Non-treatment baseline shift across independent branches remains a risk without the KL constraint.
- Small but nonzero online inference overhead (+0.026% latency, +0.021% CPU) — deemed statistically insignificant.

## 4. Prior works named
- Künzel et al. 2019 — *Meta-learners for estimating heterogeneous treatment effects using machine learning* (S-/T-/X-Learner)
- Ma et al. 2018 — *Modeling task relationships in multi-task learning with multi-gate mixture-of-experts* (MMOE, used in DDM)
- Rubin 2005 — *Causal inference using potential outcomes: Design, modeling, decisions* (Neyman-Rubin framework)
- Meng et al. 2024, CDUM — *Coarse-to-fine Dynamic Uplift Modeling for Real-time Video Recommendation* (single-treatment predecessor extended here)
- Sun & Chen 2024 (M3TN) / Zhong et al. 2022 (DESCN) / Ke et al. 2021 (EUEN) / Liu et al. 2023 (EFIN) — deep uplift baselines

## 5. Project Relevance
- **Answers:** both
- **Attributes retention to individual interactions?** no — estimates request-level ITEs for macro strategy-enablement decisions, not fractional credit across a user's individual historical touchpoints (swipes/likes/matches/messages).
- **Transferable components:** KL-divergence non-treatment baseline alignment (removes cross-branch noise when comparing candidate-profile categories); online dynamic value-weighting (MMOE) for balancing competing outcomes (e.g., match conversion vs. N7 retention) using real-time context; relative uplift scaling to bridge heterogeneous metric scales; RCT-based causal incrementality isolation to de-bias engaged users who'd act anyway.
- **Required changes:** shift from request-level strategy-enablement to micro-level counterfactual credit assignment across individual touchpoint sequences; replace average-pooled interaction embeddings with event-type-aware (swipe/like/match/message) sequence modeling with funnel stage and time-gap features; re-anchor target from aggregate session metrics to a daily-recurring rolling N7 active-retention indicator.
- **On last-touch:** does not name last-touch/last-click explicitly, but shows static population-wide strategy rules create severe trade-off penalties versus personalized causal modeling — analogous critique of any non-causal heuristic, including last-touch.
- **Transfer rating:** adaptable — a request-level multi-treatment uplift framework, not a multi-touch attribution model, but its bias-correction (KL alignment) and dynamic value-weighting modules are directly adaptable building blocks for per-swipe retention credit.
