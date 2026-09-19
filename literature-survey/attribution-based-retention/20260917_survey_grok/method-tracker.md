
Date: 2026-09-18  
Topic: Attribution-based retention

# Attribution-based Retention — Methodology Fundamentality Tracking

## Scoring

Composite = production evidence \(P\), 0–3 + per-interaction credit \(I\), 0–3 + selection-bias device \(B\), 0–2 + transfer \(T\), 0–2.

- \(P=3\): deployment or production experiment with a number; \(2\): deployed without a reported number; \(1\): production data only; \(0\): no production evidence.
- \(I=3\): reusable touch-level credit; \(2\): item-level surrogate or policy-internal decomposition; \(1\): candidate/arm score; \(0\): none.
- \(B=2\): randomization, IPW, front-door identification, or equivalent explicit device; \(1\): partial calibration or normalization; \(0\): none.
- \(T=2/1/0\): direct/adaptable/background for per-swipe N7.
- Ties are ordered by transfer, then causal validation. Baseline counts, variants, component counts, and consistent simplicity scores are not reported in the compact cards.

## Methodology Table

| Method | Proposal paper; venue/year; company | Unit of credit | Outcome | Bias device | Deployment evidence | P/I/B/T = score | Baseline mentions | Variants | Simplicity |
|---|---|---|---|---|---|---:|---|---|---|
| Front-door removal MTA | Liu et al., *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization*, arXiv 2026; Kuaishou | Consumed item | Binary upload | Front door, proxy mediator, InfoNCE, IPW | 400M DAU; 30B samples | 3/3/2/1 = **9** | n/a in cards | n/a in cards | n/a in cards |
| Experiment-calibrated Transformer DDA | Bencina et al., *Buyer Journey Insights with Data-Driven Attribution*, LinkedIn Engineering 2025 | Marketing touch | Conversion | Holdout/MMM calibration; impression imputation | Production; result scale not reported in card | 2/3/2/1 = **8** | n/a | n/a | n/a |
| Save–revisit surrogate | Jiang et al., *Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems*, AAAI 2026; Pinterest | Saved Pin | 0–6-day revisit; active users | No identified adjustment | 500M+ users; 24M-user A/B; +0.10% active users | 3/2/0/2 = **7** | n/a | n/a | n/a |
| BCMIL item-retention scoring | Ding et al., *Interpretable User Retention Modeling in Recommendation*, RecSys 2023; Tencent | Historical item | Next-3-day retention | None identified | Production A/B; exact result not reported in card | 2/3/0/2 = **7** | n/a | IURO+ | n/a |
| BCMIL item-retention scoring, extended | Ding et al., *Rethinking User Retention Modeling in Recommendation*, TOIS 2026; Tencent | Click/impression | Next-3-day retention | None identified | Production evidence; number not reported in card | 2/3/0/2 = **7** | n/a | IURO | n/a |
| Deep Twin incremental targeting | Vlontzos et al., *Incremental Recommendation via Causal Models*, arXiv 2026; Spotify | Candidate impression | Stream conversion | Always-on holdback; treated/organic modeling | Millions of users; −7.1% impressions (card) | 3/1/2/1 = **7** | n/a | n/a | n/a |
| Interleaving/counterfactual evaluation | Zhang et al., *Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking*, KDD 2025 | Search occurrence | Booking | Team-draft interleaving; position correction | Production; up to 100× evaluation velocity | 3/1/2/1 = **7** | n/a | n/a | n/a |
| Recovering Difference Softmax | Yancey and Settles, *A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications*, KDD 2020; Duolingo | Notification arm | Two-hour lesson; D1/D7 metrics | IPW, eligibility correction, shrinkage | DAU +0.5%; D1/D7 retention +2% | 3/1/2/1 = **7** | n/a | n/a | n/a |
| Message holdback (stub; unscored) | Netflix, *Incrementality-Focused Messaging Measurement*, industry blog 2023 | Message | Downstream viewing | Randomized withholding claimed in discovery, not verified | Stub; NLM/jina/WebFetch failed | unscored | n/a | n/a | n/a |
| Progressive-feedback bandit | Zhang et al., *Impatient Bandits: Optimizing for the Long-Term Without Delay*, JMLR 2026; Spotify | Content arm | 60-day active days | Bayesian progressive feedback | Live deployment; scale described but exact result not reported | 3/1/1/1 = **6** | n/a | n/a | n/a |
| ItemA2C/FID | Wang et al., *Future Impact Decomposition in Request-level Recommendations*, KDD 2024; Kuaishou | Slate item | Future value; next-week return | No causal identification | Retention +0.016%; DAU +0.028% | 3/2/0/1 = **6** | n/a | n/a | n/a |
| DCEO | Zhang et al., *DCEO: Direct Causal Effect Optimization for Long-Term User Value Modeling in E-commerce Search*, arXiv 2026; Alibaba | Item proxy | Four-day GMV/purchases | Relative proxy intervention | Production; GMV +0.36% | 3/1/1/1 = **6** | n/a | n/a | n/a |
| Producer HTE | Lada et al., *Long-run User Value Optimization in Recommender Systems through Content Creation Modeling*, arXiv 2022; Meta | Producer | Future creation | 2% randomized boost, T-learner | Production experiment | 3/0/2/0 = **5** | n/a | n/a | n/a |
| LOTUS | Wu et al., *Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?*, CIKM 2026; Alibaba | Behavior touch | Purchase | None identified | Production-scale offline evaluation; number not reported | 1/3/0/1 = **5** | n/a | pair/list prompting | n/a |
| GFN4Retention | Liu et al., *Modeling User Retention through Generative Flow Networks*, KDD 2024; Kuaishou | Policy step | Return time | None identified | Deployed; result not reported in card | 2/1/0/1 = **4** | n/a | n/a | n/a |
| AURO | Xue et al., *AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems*, WWW 2025; Kuaishou | Ranking action | Return time | Guarded exploration, not identification | Live platform, about 25M DAU | 3/0/0/1 = **4** | n/a | n/a | n/a |
| SEC | Lin et al., *Stratified Expert Cloning for Retention-Aware Recommendation at Scale*, CIKM 2025; Kuaishou | Policy action | Active days | None identified | Two platforms, 200M+ DAU | 3/0/0/1 = **4** | n/a | n/a | n/a |
| Learned Ranking Function | Wu et al., *Learned Ranking Function: From Short-term Behavior Predictions to Long-term User Satisfaction*, RecSys 2024; YouTube | Candidate score | Satisfaction/watch-return surrogate | None identified | Industrial system; number not reported | 1/1/0/1 = **3** | n/a | n/a | n/a |
| Downstream rewards | Wang et al., *Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning*, arXiv 2026; Pinterest | Candidate score | Downstream session behavior | User-prevalence normalization | Multiple live surfaces; number not reported | 2/1/0/1 = **4** | n/a | n/a | n/a |
| IMA | Bhat et al., *Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM*, arXiv 2026; Lowe’s | Daily campaign | Incremental sales | MMM prior anchoring | Three years of retail data; no result reported | 2/0/1/0 = **3** | n/a | n/a | n/a |
| RLUR | Cai et al., *Reinforcing User Retention in a Billion Scale Short Video Recommender System*, WWW 2023; Kuaishou | Request action | Return-time gap | None identified | Billion-scale deployment; result not reported | 3/0/0/0 = **3** | n/a | n/a | n/a |
| Long-term-experience surrogate | Wang et al., *Surrogate for Long-Term User Experience in Recommender Systems*, KDD 2022; Google | Reward modifier | Five-month visit frequency | None identified | Industrial data; no deployment number reported | 1/1/0/1 = **3** | n/a | n/a | n/a |
| OCARM | Ma et al., *Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling*, arXiv 2026; Kuaishou | User/ad context | LT1/LT7/LT30 | Teacher–student distillation | Live RTB system; number not reported | 2/0/0/0 = **2** | n/a | n/a | n/a |
| MRet | Kishimoto et al., *Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching*, ICLR 2026 | Candidate policy score | Joint retention | None identified | Simulation/real data; no deployment | 0/0/0/2 = **2** | n/a | n/a | n/a |
| DT4Rec | Zhao et al., *User Retention-oriented Recommendation with Decision Transformer*, WWW 2023 | List action | Login frequency | None identified | Offline datasets | 0/0/0/0 = **0** | n/a | n/a | n/a |
| DT4IER | Authors not reported in card, *Sequential Recommendation for Optimizing Both Immediate Feedback and Long-term Retention*, arXiv 2024 | List action | CTR and return frequency | None identified | Offline evidence | 0/0/0/0 = **0** | n/a | n/a | n/a |
| Agentic causal workflow | Netflix, *A Human-Augmenting Agentic Workflow for Causal Inference*, Netflix Technology Blog 2026 | Treatment | Retention CATE | Overlap/trimming workflow | Stub; evidence not retrievable | 0/0/1/0 = **1** | n/a | n/a | n/a |

## Top Method Analysis

### Rank 1: Front-door removal MTA (Score 9)

Liu et al., *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization*, arXiv 2026 is the strongest structural template: it emits one removal score per touch and explicitly attacks unobserved confounding with a front-door mediator, adversarial proxy learning, contrastive overlap control, and IPW. Its outcome is upload, not N7, so transferring it requires validating the mediator assumptions. Until then, its deletion score must be called a model-based removal effect, not incremental N7 lift.

### Rank 2: Experiment-calibrated Transformer DDA (Score 8)

Bencina et al., *Buyer Journey Insights with Data-Driven Attribution*, LinkedIn Engineering 2025 combines sequence-wide fractional credit with aggregate experiment/MMM calibration. This is the most useful v2 architecture because it separates scalable observational allocation from causal anchors. Attention weights remain explanatory shares rather than per-swipe causal effects.

### Rank 3: Save–revisit surrogate attribution (Score 7)

Jiang et al., *Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems*, AAAI 2026 is the closest deployed bridge from a specific action to a recurring return event. A save maps naturally to a right-swipe or match, while a revisit maps to renewed profile or conversation activity. Its acknowledged confounding prevents a TRUE causal-MTA classification.

### Rank 4: BCMIL item-retention scoring (Score 7)

Ding et al., *Rethinking User Retention Modeling in Recommendation*, TOIS 2026 directly produces per-item scores for next-3-day retention and handles the offline-user-label/online-item-score gap. This is the closest direct template for per-swipe training labels, but BCMIL attention and contrastive “aha item” scores are predictive, not identified incremental effects.

### Rank 5: Always-on holdback plus Deep Twin targeting (Score 7)

Vlontzos et al., *Incremental Recommendation via Causal Models*, arXiv 2026 supplies the best selection-bias lesson: explicitly model recommended consumption and organic consumption so high-affinity “always-takers” do not absorb credit. Its mismatched observation windows prevent simple \(p_1-p_0\) subtraction, and it returns a serving policy rather than historical MTA labels, but the holdback design is an excellent calibration anchor.
