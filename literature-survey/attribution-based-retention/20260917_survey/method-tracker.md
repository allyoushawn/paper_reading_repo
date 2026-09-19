Date: 2026-09-17 (last updated)  
Topic: Attribution-based retention

# Attribution-based retention — Methodology Fundamentality Tracking

The composite is:

`production evidence + per-interaction credit + selection-bias device + transfer rating`

Scoring:

- Production evidence: 3 = live deployment with quantified outcomes; 2 = production use without a quantified outcome; 1 = offline production data; 0 = no production evidence.
- Per-interaction credit: 3 = explicit touch/item credit; 2 = request/item value or surrogate; 1 = user/policy/channel credit; 0 = no credit assignment.
- Selection-bias device: 2 = randomization or explicit causal/debiasing estimator; 1 = normalization, stratification, or implicit correction; 0 = none.
- Transfer rating: direct 2, adaptable 1, background 0, following the supplied cards.

## Methodology Table

| Method | Paper | Year | Venue | Company | Unit of credit | Outcome | Bias device | Deployment evidence | Score |
|---|---|---:|---|---|---|---|---|---|---:|
| Front-door deletion MTA | ALM-MTA | 2026 | ICLR | Kuaishou | Consumed video | Upload probability | Front-door proxy mediator, IPW, InfoNCE | 400M DAU; DAU +0.04%, active creators +0.6% | 3+3+2+1=9 |
| IURO attention credit | Interpretable User Retention Modeling in Recommendation | 2023 | RecSys | WeChat/Tencent | User-item interaction | Next-day/next-three-day retention | Activity weighting, contrastive “aha” items, future anchors | 3M+ users; retention +0.76%/+0.65% | 3+3+1+1=8 |
| Downstream Rewards | Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning | 2026 | RecSys | Pinterest | Recommended Pin | DAU/WAU/MAU proxies and successful sessions | User-Prevalence normalization | Multiple live tests; successful sessions +0.36% | 3+2+1+1=7 |
| Multi-dimensional LTV attribution | A Long-term Value Prediction Framework in Video Ranking | 2026 | WWW | Alibaba/Taobao | Recommended video | LT1/LT3 and seven-day author value | PDQ position debiasing, attribution weights | LT3 +0.21% for Author Time | 3+2+2+1=8 |
| Detailed-balance retention flow | Modeling User Retention through Generative Flow Networks | 2024 | KDD | Kuaishou | Recommendation step | Return time and retention | Reward-proportional trajectory flow | Next-day retention +0.015%; low-activity +0.069% | 3+3+1+1=8 |
| Randomized causal uplift | Improving Instagram Notification Management with Machine Learning and Causal Inference | 2022 | Meta Engineering | Meta | Notification | Incremental activeness | 50/50 send/drop randomization | Deployed; lower volume without activity loss, no lift number | 2+3+2+1=8 |
| Item-level retentive relevance | Retentive Relevance | 2025 | arXiv | Meta | User-item pair | Next-day retention/sessions | CBPS and random survey sampling | Sessions/user +0.030% | 3+2+2+1=8 |
| Counterfactual media masking | SMEO | 2026 | CIKM | Amazon | Media asset | Conversion | PAL, variable-depth supervision, survival weighting | Production-scale serving; offline DR-CVR +5.4% | 2+3+2+1=8 |
| Snap HTE T-learner | Large Scale HTE Framework | 2025 | arXiv | Snap | User-treatment | Incremental conversion/engagement | Randomized ITT logs | Production; 20% mean AUUC gain for sensitivity models | 3+1+2+1=7 |
| Causal incrementality transformer | From Prediction to Incrementality | 2026 | arXiv | LinkedIn | User-action allocation | LTV/conversion | DragonNet, targeted regularization, exploration | LTV +7.20% | 3+1+2+1=7 |
| CanniUplift | CanniUplift | 2026 | KDD | Alibaba/Taobao | User-seller/incentive | Incremental GMV | Redemption decomposition, global consistency | Incremental GMV +4.08% | 3+2+2+1=8 |
| CDUM | Coarse-to-fine Dynamic Uplift Modeling | 2025 | RecSys | Kuaishou | Request treatment | LT7/LT30, usage | Potential-outcome uplift on RCT logs | Enter LT7 +0.048% | 3+2+2+1=8 |
| HMUM | Heterogeneous Multi-treatment Uplift Modeling | 2026 | arXiv | Kuaishou | Request treatment | Usage time/views | RCT logs, KL baseline alignment | Usage time +0.044% to +0.073% | 3+2+2+1=8 |
| Cannibalization calibration | Attributed, But Not Incremental | 2026 | ADKDD | TikTok | Channel-day/hierarchy | Incremental acquisition | RCT-calibrated ETDC and constrained HCA | Calibration error reduced 91.38% | 3+1+2+0=6 |
| RL retention critic | Reinforcing User Retention in a Billion Scale Short Video Recommender System | 2023 | WWW | Kuaishou | Request | Return time/N7 retention | Activity cohorts, uncertainty normalization | DAU +0.20%; N7 +0.063% | 3+2+1+1=7 |
| Save–revisit surrogate | Save, Revisit, Retain | 2026 | AAAI | Pinterest | Saved Pin | 28-day activity proxy | Same-item linkage, unique-user normalization | Active-user propensity +0.08% | 3+2+1+1=7 |
| Future Incremental Value | How Airbnb Measures Future Value | 2021 | Airbnb Engineering | Airbnb | Platform action | Long-run value | Propensity-score matching, common support | 150+ actions; no lift disclosed | 2+3+2+1=8 |
| DML promotion uplift | Smarter Promotions with Causal Machine Learning | 2025 | DoorDash Engineering | DoorDash | Promotion | Incremental order probability | Double ML | Near-equal orders at about half the cost | 3+2+2+1=8 |
| MRet retention curve | Retention-Optimized Two-Sided Matching | 2026 | ICLR | Hanjuku-kaso | Candidate pair/ranking decision | Monthly retention | Concave retention curve; no causal correction | Offline real dating data; 66.5% retention | 1+2+0+1=4 |
| Wantedly churn-risk boost | Not All Matches Are Equally Valuable | 2026 | RecSys in HR | Wantedly | Candidate ranking | Four-week churn | Randomized test; covariate adjustment | OR 0.957/0.948, not significant | 3+1+2+1=7 |
| Surrogate Index | The Surrogate Index | 2025 | Review of Economic Studies | Academic | Treated individual | Long-term outcome | Randomization, DR influence function | RCT benchmark; no platform deployment | 0+1+2+1=4 |
| Proximal Surrogate Index | The Proximal Surrogate Index | 2026 | arXiv | Academic | Treated individual | Long-term outcome | Dual proxies and bridge functions | Job Corps benchmark only | 0+1+2+1=4 |
| Progressive-feedback bandit | Impatient Bandits | 2023 | KDD | Spotify | Candidate show | 60-day active days | No selection correction | Offline, real Spotify podcast-discovery logs | 1+2+0+1=4 |
| LOPE | Estimating Long-term Outcome of Algorithms | 2024 | WWW/Spotify Research | Spotify | Policy/action | Long-term policy value | Importance weighting plus residual action effect | Spotify A/B logs; 36–71% MSE reduction | 1+1+2+1=5 |
| Ambient ITT/PIE | Media Measurement and the Assisted Own Goal | 2026 | arXiv | GrowthLoop | User assignment | Channel-complete conversion | Salted-hash ITT and CATE | Production hashing; simulated causal recovery | 2+1+2+0=5 |
| LLM selection/LOTUS | Can Large Language Models Identify Meaningful Touchpoints | 2026 | CIKM | Alibaba/Taobao | Touchpoint class | Conversion | Human labels; no causal correction | Production CVR GAUC +0.35pp | 3+3+0+1=7 |
| ReAlloc | Multi-channel Uplift Policy Learning | 2026 | arXiv | Alibaba/Taobao | Budget allocation | Orders/income | DML orthogonalization, support guard | Orders +3.53% | 3+1+2+0=6 |
| Bayesian MMM anchoring | Integrated Marketing Attribution | 2026 | arXiv | Lowe’s | Campaign-day | Incremental sales | MMM priors and non-negativity | Three years of Lowe’s data; R²=0.98 reconstruction | 1+1+1+0=3 |

## Top Method Analysis

Score-8 ties were broken by closeness to the Q2 problem (per-interaction retention credit), not by composite uniqueness.

### Rank 1: Front-door deletion MTA (Composite Score: 9)

ALM-MTA is the strongest template for the eventual causal attributor because it produces explicit deletion credit for every touchpoint, addresses unobserved system-level confounding through a front-door proxy mediator, and reports deployment at 400M DAU. Its dating adaptation should replace the upload outcome with N7 and use match/conversation progression as candidate mediator signals.

### Rank 2: IURO attention credit (Composite Score: 8)

IURO is the closest demonstrated per-item retention-credit system. It assigns a retention score to each historical item, avoids uniform credit through attention and contrastive “aha item” learning, and improved next-day and next-three-day retention online. Its activity weighting is weaker than randomized causal identification, so it should inform the architecture rather than supply final causal labels alone.

### Rank 3: Downstream Rewards (Composite Score: 7)

Pinterest’s Downstream Rewards offers the cleanest low-cost response to the “engaged users swipe more” bias: User-Prevalence normalization compares activity with the same user’s historical baseline. Its weighted downstream trajectories also map naturally from impression→deep engagement to swipe→match→message. It remains proxy reward learning rather than full multi-touch causal attribution.

### Rank 4: Multi-dimensional LTV attribution (Composite Score: 8)

Taobao’s LTV framework combines position debiasing, learned per-item attribution weights, delayed multi-day labels, and real-time/delayed co-training. These components map directly to swipe-feed depth, unrelated downstream-event filtering, and rolling N7 labels. The limitation is that its evidence concerns video value and LT1/LT3 rather than explicit counterfactual retention credit.

### Rank 5: Detailed-balance retention flow (Composite Score: 8)

GFN4Retention is the strongest sequence-level mechanism for propagating terminal retention through non-last actions. Its live tests show that intermediate recommendations carry useful retention flow. It is expensive and lacks a fully explicit causal selection-bias correction, making it a later-stage option after experimental anchors and simpler removal effects are stable.
