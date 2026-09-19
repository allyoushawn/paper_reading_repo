# NotebookLM deep-research runs 3 and 4 (2026-09-17) — condensed record

The full prose reports were read by the lead and are condensed here. The comparison tables are verbatim.

## Run 3 — reciprocal / dating retention cluster (59 hits)

Query: retention-optimized reciprocal recommendation and two-sided matching: causal effect of matches, likes, or messages on user retention in dating apps and job-matching platforms; online experiments; churn-risk score boosting; retention-aware ranking; Tinder Hinge Bumble Kuaishou BOSS Zhipin CyberAgent

Relevant hits (index | title | url):
- 1/45/46 | Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching (MRet) — ICLR 2026, CyberAgent (Riku Togashi et al.) | https://arxiv.org/abs/2602.15752 — already a source.
- 2/16 | Not All Matches Are Equally Valuable (Wantedly Visit job-matching platform; RecSys in HR 2026 oral) | https://arxiv.org/abs/2609.01652 — already a source.
- 4/7 | Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method (causal formulation; BOSS Zhipin data) | https://arxiv.org/abs/2408.09748 — added 2026-09-17.
- 5 | Impatient Bandits: Optimizing Recommendations for the Long-Term Without Delay (Spotify, KDD 2023) | arXiv 2307.09943 — added 2026-09-17 (paper behind the Spotify blog post already in the queue).
- 6 | Reducing Recommendation Inequality via Two-Sided Matching: A Field Experiment of Online Dating | ResearchGate only — open version not yet located.
- 10 | Returning is Believing: Optimizing Long-term User Engagement in Recommender Systems (CIKM 2017) | ResearchGate only — background on return-time objectives.
- 14 | Effects of Market Size and Competition in Two-Sided Markets: Evidence from Online Dating (field experiment) | ResearchGate only — context.
- 31/32 | Modeling Churn in Recommender Systems with Aggregated Preferences | https://arxiv.org/abs/2502.18483 — added 2026-09-17.
- 54 | Positive Customer Churn: An Application to Online Dating | ResearchGate only — concept note: churn caused by success.
- 15 | Phoenix — Tinder's Testing Platform — Part III (experimentation infra, cluster randomization) — context only.
- Remaining hits: BOSS Zhipin reciprocal models (BAMBOO, MIRROR, quasi-metric person-job fit), fairness surveys, Kuaishou PEPNet, dating-app market studies — not attribution; not queued.

Key claims in the report (paraphrased):
- Retention as a function of cumulative matches is concave: large marginal gain below a threshold m*, near zero above it (cites 2609.01652 and 2602.15752).
- MRet ranks candidates by expected bilateral retention gain: ΔRet(x,y) = r(x,y) · [ (R_x(m_x+1) − R_x(m_x)) + (R_y(m_y+1) − R_y(m_y)) ], with personalized retention curves R_u(m; θ_u) learned by survival analysis or calibrated logistic models.
- Wantedly Visit deployed a post-processing score boost for churn-risk users (m_u < m*) above a relevance cut-off; online A/B: directional drop in candidate churn, no company-side deterioration, not significant at conventional levels.
- Reciprocal experiments violate SUTVA; cluster randomization (bipartite partitioning) and synthetic controls are used.

Verbatim comparison table from the report:

| Platform / Framework | Application Domain | Primary Optimization Objective | Core Algorithmic Framework | Key Operational / Empirical Result |
| :--- | :--- | :--- | :--- | :--- |
| **Wantedly Visit** | Job-Matching Platform | Churn-Risk Reduction via Match Redistribution | Post-Processing Score Boost (Ŝ = S + β_u) for m_u < m* | Directional drop in candidate churn; zero deterioration in company churn |
| **MRet (CyberAgent)** | Two-Sided Online Dating | System-Wide Long-Term User Retention | Dynamic LTR optimizing Joint Bilateral Retention Gain ΔRet(x,y) | Outperforms match-maximization & exposure fairness in overall platform retention |
| **BOSS Zhipin (BAMBOO)** | Online Recruitment Market | Bilateral Person-Job Fit & Mutual Adoption | Dual Expectation Transformer + Competitiveness HGNN + Quasi-Metric Space | Significant accuracy gains over baseline RecSys; balances supply/demand |
| **Kuaishou (PEPNet)** | High-Throughput Reciprocal Feeds | Multi-Task Alignment & Retention | Context-Gated Parameter Personalization (W_l ⊙ g_l) | >1% online metric uplift across 300M DAU deployment |
| **Hinge** | Mobile Romantic Matchmaking | Long-Term Relationship Formation | Granular Item-Level Collaborative Filtering (Likes on specific prompts/photos) | Higher signal density per interaction compared to binary swipes |
| **Tinder** | Mobile Romantic Matchmaking | Engagement & Monetization ("Who Likes You") | Two-Step Sequential Deferred Acceptance & Cluster Experimentation | Uncontrolled cross-side network size increases user selectivity and search friction |

## Run 4 — 2025–2026 arXiv multi-touch attribution cluster (25 hits)

Query: arXiv 2025 2026 multi-touch attribution papers: causal multi-touch attribution, counterfactual conversion path modeling, attention-based touchpoint credit, large language model attribution of touchpoints, attribution under privacy constraints, incrementality-calibrated data-driven attribution, Shapley conversion credit, survival or time-to-event attribution

Relevant hits (index | title | url):
- 6/14 | ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization (ICLR 2026, Xia et al.; 400M-DAU platform) | https://arxiv.org/abs/2605.08881 — added 2026-09-17. Attributes a downstream in-app action (content upload) to prior consumption touchpoints with counterfactual deletion credit ΔU_k = P(Y=1|S) − P(Y=1|S∖{t_k}); front-door identification via an adversarially learned mediator.
- 5/18 | Sequential Multimodal Evidence Optimization for Product Media Ranking in E-Commerce (SMEO; Amazon, CIKM 2026) | https://arxiv.org/abs/2608.15662 — added 2026-09-17. Survival-weighted credit over an ordered slate; counterfactual masking yields per-asset credit without asset-level labels.
- 11 | A Fisher-Market Formulation for Fractional Credit Assignment Between Planned Tasks and Performed Actions | https://arxiv.org/abs/2607.20694 — added 2026-09-17.
- 1/17 | Can LLMs Identify Meaningful Touchpoints in Conversion Attribution? (SILVA benchmark + LOTUS; Wu et al., Alibaba / Nanjing Univ., CIKM 2026) — already a source.
- 2/20/21 | Attributed, But Not Incremental (ETDC + HCA; Li et al., TikTok, ADKDD 2026) — already a source.
- 7 | Integrated Marketing Attribution (IMA; Bhat et al., Lowe's Companies Inc.) — already a source; affiliation now known.
- 3/13/22 Amazon Ads MTA (2508.08209); 4/19/23 PVM (2511.22918); 8 MAC (2603.02184); 9/15/16/24 LiDDA (2505.09861); 10 MAL (2508.15217); 12 attribution sets (2602.06276) — all in the parent survey.

Verbatim comparison table from the report:

| Framework / Architecture | Key Authors & Institution | Core Methodology | Causal / Statistical Assumption | Performance Metric & Operational Impact |
| :--- | :--- | :--- | :--- | :--- |
| **Amazon Ads MTA** | Lewis et al., Amazon / Northwestern / NBER | Calibration factor ensemble combining observational ML with RCT holdouts | Unbiased RCT treatment effects correct observational ML prediction bias | Unbiased full-funnel budget allocation; balances upper and lower funnel tactics |
| **ALM-MTA** | Xia et al., ICLR 2026 | Front-door causal identification via adversarial mediator proxy and counterfactual deletion | Existence of an observable mediator distilling outcome signals under unobserved confounders | +40% Upload AUC; +1.5x attributable coverage; +670% exposure efficiency; +0.6% daily active creators |
| **ETDC + HCA** | Li et al., TikTok (ADKDD 2026) | Experiment-to-Daily Cannibalization (ETDC) with Hierarchical Allocation (HCA) | Sparse RCT lift signals act as ground-truth causal anchors for daily extrapolation | Reduces relative calibration error from +334% down to [-7%, 10%]; cuts cannibalization by 15 pp |
| **IMA** | Bhat et al., Lowe's Companies Inc. | Integrated Bayesian regression disaggregating weekly MMM adstock metrics into daily campaign contributions | Weekly MMM parameters regularize campaign coefficients via Truncated Normal priors | Granular, privacy-safe campaign attribution without third-party tracking or user logs |
| **LiDDA** | Bencina et al., LinkedIn | Attention-based deep journey modeling with tAPE encodings and downsampling | Multi-touch customer sequences exhibit temporal and seasonal interval dependencies | -78% training time; -99% inference latency vs. Shapley baselines; high prediction stability |
| **SILVA / LOTUS** | Wu et al., Alibaba / Nanjing Univ. (CIKM 2026) | Human-annotated implicit intent benchmark (SILVA) and pairwise LLM touchpoint selection (LOTUS) | Conversion journeys contain implicit semantic associations missed by collaborative filtering | Uncovers +14.91% implicit touchpoints; +0.35 pp GAUC gain in industrial CVR prediction |
| **PVM** | An et al., Baidu / Renmin Univ. | Game-theoretic Peer-Validated Mechanism decoupling platform payouts from self-reported logs | Strategic platforms manipulate reporting delays under Last-Click rules | Dominant Strategy Incentive Compatible (DSIC); +118% accuracy gain over Last-Click in multi-agent settings |
| **SMEO** | Dey et al., Amazon (CIKM 2026) | Trajectory utility model with multimodal encoders (CLIP, VideoMAE, Uni3D) and survival reward-to-go | Customer attention depletes sequentially; front-loading evidence minimizes interaction effort | +5.5% DR-CVR; -15% customer swipes to conversion; counterfactual media credit without asset labels |
| **MoAE / PyMAL** | Chen et al., PyMAL Benchmark | Mixture-of-Attribution-Experts architecture for Multi-Attribution Learning (MAL) in CVR models | Multi-view attribution signals provide complementary representations of user conversion intent | +2.00 pt AUC gain on Last-Click targets; +1.41 pt gain on DDA targets over single-view baselines |

Report's strategic conclusions (paraphrased): (1) unify observational attribution models with experimental anchors (Amazon MTA, TikTok ETDC+HCA); (2) use front-door identification where backdoor adjustment fails under latent user state (ALM-MTA); (3) anchor granular attribution to aggregate MMM priors under signal loss (IMA); (4) use LLM pairwise prompting to recover implicit touchpoints (LOTUS); (5) replace last-click with strategy-proof mechanisms (PVM).
