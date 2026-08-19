# Paper Analysis: Mini-Game Lifetime Value Prediction in WeChat

**Source:** arXiv:2506.11037 (Tencent / WeChat); accepted KDD 2025 ADS Track (ACM DOI 10.1145/3711896.3737248)
**Date analyzed:** 2026-08-16

## 1. Summary

Chen, Niu, Gao, Sun, Liu, Chen, Liu, and Li (Tencent / WeChat) tackle lifetime-value (LTV) prediction for ad-driven mini-game user acquisition on WeChat. LTV prediction sits at the end of the advertising conversion funnel (exposure → click → register → purchase); the purchase rate among registered users is around 0.1%, so supervisory signal is severely sparse. A second, largely independent problem is that advertisers need LTV at multiple horizons (3-day, 7-day, 30-day) to balance short- and long-term bidding decisions, and co-training these highly correlated horizon-specific tasks on one shared backbone produces **gradient conflicts** — descending the gradient of one horizon's loss often increases another's, yielding skewed, unbalanced accuracy across horizons.

The proposed framework, **GRePO-LTV** (Graph-Represented Pareto-Optimal LTV prediction), attacks both problems. **Data sparsity** is addressed with unsupervised **Graph Representation Learning (GRL)**: homogeneous user and game graphs are built from user-game-user / game-user-game meta-paths (edge weight proportional to shared interaction count), and a masked-reconstruction objective (predicting concealed edges and node attributes) produces collaborative-signal embeddings without relying on the sparse downstream LTV labels themselves. **Multi-horizon conflict** is addressed with two-stage **Pareto optimization**: a Quadratic Programming step finds a non-dominating gradient direction inside the convex hull of the three horizons' task gradients (so no horizon's loss is made worse by an update aimed at another), followed by a search along the resulting Pareto front using predefined per-horizon importance weights. The shared backbone itself combines a Field-weighted Factorization Machine encoding layer, an EPNet + Partitioned-Norm domain-adaptation layer, and an AdaSparse tower with a Zero-Inflated Lognormal (ZILN) output head to model the highly zero-heavy, right-skewed distribution of purchase value.

Evaluated on a proprietary 3.73M-sample WeChat mini-game dataset plus a live WeChat A/B test, GRePO-LTV beats the strongest baseline offline by NMAE −14.0%, AUC +3.6%, N-GINI +1.6% (relative), and delivers an average +8.4% GMV/LTV lift online across the three horizons, with the 3-day horizon showing the largest gain.

## 2. Experiment Critique

**Design.** The offline comparison spans 11 baselines across two families (time-series forecasting: TCN, LSTM, Informer, ARIMA; dedicated LTV models: GateNet, TSUR, CDLtvS, ADSNet, ZILN, Kuaishou, DeepFM), all forced to predict all three horizons from a single shared backbone for a fair comparison, plus two ablations (w/o GRL, w/o Pareto). A dedicated data-sparsity stress test (dropping increasing fractions of training data and tracking N-GINI decay) and a seed-stability analysis (20 training runs with/without Pareto, correlation matrix over 40 three-dimensional AUC vectors) directly test the two claimed contributions rather than just the headline metric.

**Statistical validity.** The main offline comparison table reports standard deviations across the three horizon tasks per method. The online A/B test uses four traffic arms (baseline, w/o GRL, w/o Pareto, full method) at 5% UV sampling each — enough to isolate each component's online contribution (w/o GRL degrades average GMV lift from +8.4% to +2.4%; w/o Pareto degrades it to +0.11%) — but no explicit significance test or confidence interval is reported for the online percentages themselves.

**Online experiments.** A one-month live test on WeChat mini-game traffic, with a dedicated day-over-day prediction-stability metric ("Diff," comparing predictions from models pushed on adjacent days on the same fixed sample batch) — a genuinely production-relevant check that the other three papers in this batch do not include. GRePO-LTV's Diff is reported as roughly half the baseline's, which the authors also use to argue the accuracy comparison itself is more trustworthy (a less stable model's online accuracy numbers would be noisier).

**Reproducibility.** The dataset is proprietary and not released; feature schemas (user/game/behavior-level fields) are described but not exact preprocessing code. Architecture and training procedure (QP formulation, ZILN definition, meta-path construction) are specified in enough mathematical detail to reimplement conceptually. No code release is mentioned in the retrieved material.

**Overall.** One of the more thorough evaluations in this batch — component-level online ablations plus a stability metric are unusual and valuable — but, like the other industry papers here, absolute numbers rest on a single, proprietary deployment and a single one-month window.

## 3. Industry Contribution

The central engineering claim is a **single shared backbone serving three horizon-specific value heads**, replacing what would otherwise be three separately maintained models (3-day, 7-day, 30-day) — directly reducing serving and retraining surface area, echoed in the paper's explicit design choice to force every baseline in Table 1 through the same single-backbone constraint for a fair comparison. The GRL component has a real offline feature-engineering cost the authors are candid about in their "Lessons Learned from Deployment" section: building useful graph embeddings requires data from a game's **entire lifespan**, not a rolling window, so the graph-construction pipeline needs long-horizon batch access that a purely online feature pipeline would not provide. The authors also flag that launch-day and limited-time-event traffic produces distributional outliers the trained model cannot handle well, and recommend increasing retraining frequency around such events — a concrete operational recommendation rather than an abstract limitation. The day-over-day prediction-stability ("Diff") metric is itself a piece of production tooling: it exists specifically to catch a model-push regression (large swings in LTV predictions for the same fixed sample) before it reaches the bidding system that consumes these scores.

## 4. Novelty vs. Prior Work

The claimed novelty is combining graph-based collaborative signal (to fight sparsity) with a Pareto-optimal multi-horizon training procedure (to fight gradient conflict) in a single industrial LTV system. Prior work discussed: **Fader, Hardie & Lee, "RFM and CLV: Using iso-value curves for customer base analysis," Journal of Marketing Research 2005,** and **Fader, Hardie & Lee, "'Counting your customers' the easy way: An alternative to the Pareto/NBD model," Marketing Science 2005** — the classical statistical LTV baselines (RFM, Pareto/NBD) the paper positions itself against as insufficiently able to capture non-linear behavior. **Wang, Liu & Miao, "A deep probabilistic model for customer lifetime value prediction," arXiv:1912.07753, 2019** — source of the Zero-Inflated Lognormal (ZILN) output distribution GRePO-LTV's tower layer reuses directly. **Li, Shao, Yang, Fang & Song, "Billion-user customer lifetime value prediction: an industrial-scale solution from Kuaishou," CIKM 2022** — the strongest prior industrial LTV baseline (models ordered dependencies between horizons via network structure rather than Pareto optimization) and the second-best baseline in Table 1. **Xing et al., "Learning reliable user representations from volatile and sparse data to accurately predict customer lifetime value," KDD 2021** — the TSUR baseline, a temporal-structural user representation approach to the same sparsity problem. **Lin et al., "A pareto-efficient algorithm for multiple objective optimization in e-commerce recommendation" (PE-LTR), RecSys 2019** — the pioneering Pareto-efficient multi-objective framework the paper's Pareto-optimization stage builds on. **Chang et al., "PEPNet: Parameter and embedding personalized network for infusing with personalized prior information," KDD 2023** — source of the EPNet/Gate-NU domain-adaptation mechanism reused in the adaptation layer. **Sheng et al., "One model to serve all: STAR topology adaptive recommender for multi-domain CTR prediction," CIKM 2021** — source of the Partitioned Norm mechanism reused for domain-shift handling.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| WeChat Mini-Game Recommendation dataset | Offline (3,730,392 samples, ~21,000 new registrations/day over 6 months) | No — proprietary, no public LTV dataset exists for this domain per the authors | User/game/behavior-level features; 7:2:1 train/val/test split |
| WeChat mini-game live traffic | Online (1-month A/B test, 5% UV sampling per arm, 4 arms) | No — proprietary | Baseline, w/o GRL, w/o Pareto, and full-method arms |

## 6. Community Reaction

Not assessed in NotebookLM mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Mini-Game Lifetime Value Prediction in WeChat," Aochuan Chen, Yifan Niu, Ziqi Gao, Yujie Sun, Shoujun Liu, Gong Chen, Yang Liu, Jia Li (Tencent / WeChat), arXiv, 2025, https://arxiv.org/abs/2506.11037 (also KDD 2025 ADS Track, ACM DOI 10.1145/3711896.3737248) |
| 2 | Source type | Industry paper (arXiv preprint; accepted KDD 2025 ADS Track) |
| 3 | Direction | D4 |
| 4 | Problem setting | Predicting user LTV for ad bidding in mini-game advertising under extreme purchase-rate sparsity (~0.1%) and gradient-conflicting multi-horizon (3/7/30-day) co-training on a shared backbone |
| 5 | Objective and label definition | Label is **"t-Value"**: the cumulative monetary payment a user contributes to a specific game within a fixed t-day window after registration (t ∈ {3, 7, 30}). The paper explicitly defines true LTV as the limiting case "∞-Value," but the model only ever trains and evaluates against the finite, truncated windows — LTV itself is never the directly observed label, only approximated by these truncations. **Censoring is not statistically modeled** (no survival analysis, no hazard-rate correction for users whose eventual spend is still accruing) — instead the authors sidestep censoring by construction, drawing users from a 6-month historical cohort so every included user's 3/7/30-day windows have already fully elapsed by data-collection time. Payments beyond day 30, or from users too recently registered to have a complete window, are simply excluded rather than corrected for |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. It "endeavors to forecast the cumulative purchase contribution of a user," and the model is mathematically defined as a direct regression ŷ = f(u, x_u, i, x_i \| Θ) ∈ [0, +∞) |
| 7 | Model architecture | GRL-pretrained user/game graph embeddings (masked meta-path edge + attribute reconstruction) feeding a shared backbone — FwFM encoding layer, EPNet + Partitioned-Norm domain-adaptation layer, AdaSparse tower — with a Zero-Inflated Lognormal (ZILN) output head per horizon, trained jointly via two-stage Pareto optimization (non-dominating QP gradient descent, then weighted Pareto-front search) across the three horizon losses |
| 8 | Credit assignment | Not applicable in the slate/item sense — this is a pointwise (user, game) LTV regression, not a ranking or slate decomposition. The paper's actual "assignment" problem is temporal/multi-task: allocating gradient credit across the 3/7/30-day horizon losses via the non-dominating Pareto gradient, not mapping a user outcome onto one of several candidate items |
| 9 | Training data and counterfactual handling | 3.73M logged (user, game) payment records from ad-driven registrations over a 6-month window, chronologically split 7:2:1. No counterfactual, inverse-propensity, or causal adjustment is applied — pure supervised regression on observed payments; exposure/selection bias from the ad-serving policy that generated the logged data is not addressed |
| 10 | Offline and online evaluation | Offline: NMAE, AUC, and N-GINI on a held-out 10% split, plus a data-sparsity ablation (dropping training-data fractions) and a 20-run seed-stability analysis. Online: 1-month WeChat live A/B test, four 5%-UV-sampled arms (baseline, w/o GRL, w/o Pareto, full method), measured on per-horizon LTV/GMV lift and a day-over-day prediction-stability ("Diff") metric |
| 11 | Reported gains | Offline: NMAE improved 14.0%, AUC +3.6%, N-GINI +1.6% (relative to the second-best baseline, averaged across 3/7/30-day tasks) on the WeChat mini-game dataset (3.73M samples). Online: average GMV/LTV +8.4% over the production baseline in a 1-month WeChat A/B test, with the 3-day horizon showing the largest single-horizon gain (LTV3 +9.91%, GMV3 +9.83%) |
| 12 | Applicability to a two-sided dating recommender | Single-sided (advertiser/player) LTV regression with no reciprocity, congestion, or match-fairness treatment. The finite-window "t-Value" label design and the multi-horizon Pareto co-training procedure are directly reusable for defining a dating app's 7/30-day retention-and-revenue label under the same gradient-conflict problem the survey's target system will face when unifying short- and long-term heads |
| 13 | Unverified claims | The headline "+8.4% average GMV" is a single-market, single-window (1-month) result on one ad-recommendation surface; generalization to other verticals or longer timeframes is asserted, not independently demonstrated in this paper. The "Lessons Learned" claim that GRL "requires data from the entire lifespan of each game" is stated as a deployment lesson, not backed by a controlled ablation over partial-lifespan graphs in the paper's own result tables |

## Project Relevance

Directly and heavily on **Q3** (label and horizon definitions): the explicit "t-Value vs. ∞-Value" framing — defining LTV operationally as a set of finite, fully-observed truncated windows rather than attempting to model the true infinite-horizon quantity or its censoring — is one of the clearest, most citable finite-horizon LTV-label precedents anywhere in this survey, and directly informs how the target dating-app system should define its own 7–30 day retention/revenue label. Partially on **Q4**: a single ZILN value head per horizon is closer to the "one value head" end of the survey's fusion spectrum, though GRePO-LTV never fuses this with a *separate* short-term CTR/CVR-style head the way the survey's target system needs to. Partially on **Q1**: the objective (cumulative payment/GMV) is a revenue proxy, not retention, so it only half-answers "training objective is retention/LTV/revenue directly." Touches **Q6** with both an offline and online evaluation protocol, though without addressing two-sided interference.

Does **not** address **Q2** (no item/slate-level credit assignment — this is pointwise user-item regression, not a ranking decision), **Q5** (no incrementality/causal treatment), or **Q7** (no two-sided, reciprocal, or congestion treatment). Also does not address **Q8** — GRePO-LTV is trained as a fresh unified backbone from the start, with no staged-migration narrative from an existing production system. As one of only four D4 papers in the entire survey, it carries weight beyond its Priority-2 label specifically for the horizon/label/censoring question (Q3), even though its relevance to credit assignment (Q2) and incrementality (Q5) is essentially nil.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `GRePO-LTV`._

## Meta Information

- **Authors:** Aochuan Chen, Yifan Niu, Ziqi Gao, Yujie Sun, Shoujun Liu, Gong Chen, Yang Liu, Jia Li
- **Affiliations:** Tencent / WeChat
- **Venue:** arXiv preprint 2506.11037 (2025); accepted KDD 2025 ADS Track (31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining, DOI 10.1145/3711896.3737248)
- **Year:** 2025
- **Relevance:** Core
- **Priority:** 2
- **nlm:d1771ff1-bd8d-4afc-bd1a-2641e505512f**
