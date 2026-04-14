# Attribution-Based Retention Paper Queue

## Survey Run 2 — execution notes

- **Phase 4 gate:** **Done ≥ 60 is satisfied (62 as of batch 2026-04-12h).** **Phase 3.7 complete** (2026-04-13): reverse citation map — see `phase3.7-summary.txt` (65 `read-papers/*.md` files scanned; **62** in **Done**). **Phase 4-A (2026-04-14):** full-notebook NotebookLM **Queries 1–7** completed (`nlm-phase4-raw-responses.md` replaced with verbatim answers). **Batch 2026-04-14:** four `read-papers/*` files from batch 2026-04-12h reprocessed with **12** per-source `notebook_query` calls (3×4 sources). **`literature-review.md`** refreshed from Phase 4-A text (Meta, Executive Summary, recommendations, Cross-notebook Q6–7, Phase 4-C). **Phase 5** (`executive-summary.md`, full requirements summary) not run in this pass.
- **NLM batch 2026-04-12h (historical):** initial `notebook_query` attempts hit **RESOURCE_EXHAUSTED**; corpus used PDF/arXiv text where needed. **Refresh 2026-04-14:** quota recovered — per-source and Phase 4-A queries **succeeded**; see `read-papers/` date lines and `nlm-phase4-raw-responses.md`.
- **Paywall rule:** Before marking a paper unavailable, log free-version attempts (arXiv, SSRN, Semantic Scholar, author homepage) in **Skipped** with explicit wording.
- **Core MTA sequencing:** Do not process **expansion** papers (MMM cluster, continuous-outcome-only discovery, extra industry blogs beyond reinstate list) until **Core MTA Done ≥ 50% of total Done** (see **Core MTA accounting**). CATE and survival items already in Done count toward total Done but **not** toward the Core MTA numerator.

## Core MTA accounting (for 50% threshold)

- **Total Done:** **62** (previous **58** plus **batch 2026-04-12h (+4)** Core MTA arXiv-only harvest: Peer-Validated Mechanism / PVM; Axiomatic Attribution for Multilinear Functions (ASS); Statistical Learning from Attribution Sets; Unraveling Consumer Purchase Journey (NN + Shapley touchpoints)).
- **Core MTA numerator:** **31** — **+4** batch 2026-04-12h: **Beyond Last-Click: Optimal Mechanism for Ad Attribution (PVM)** — DSIC peer-validated **last-platform** credit under strategic timestamps (path-level **cross-platform** allocation; complements sequence MTA for billing truthfulness); **Axiomatic Attribution for Multilinear Functions (Sun & Sundararajan)** — unique **ASS** credits for \(\Delta f\) on multilinear (+additive) conversion / retention surrogates (**per-dimension incremental** credit primitives); **Statistical Learning from Attribution Sets (Applebaum et al.)** — **candidate-click-level** unbiased ERM under privacy-style **attribution sets** + prior \(\pi\) (**probabilistic responsibility** over touches in each set); **Unraveling Consumer Purchase Journey (Churchill et al.)** — **Shapley explanations** over **touchpoint-type** features from an ensemble NN for **purchase** (tabular multi-channel **touch credit** from a joint predictor).
- **Not counted toward Core MTA numerator (still in Done for total / synthesis):** CFR/TARNet; DragonNet; DML; X-learner; Causal Forest; R-learner; DeepHit; pycox/Cox-Time; Trimmed Match (×2); DoorDash switchback; DoorDash flat experiments; Netflix causal survey; **Zhang et al. unified HTE/uplift survey (arXiv:2007.12769)**; **CausalMMM** (arXiv:2406.16728 / WSDM ’24 — shop/channel causal MMM, not per-touchpoint MTA); **DeepCausalMMM** (arXiv:2510.13087 — aggregate multi-region MMM, not per-touchpoint MTA); **Runge et al. Robyn packaging** (arXiv:2403.14674 — aggregate mMM + calibration workflow, not per-touchpoint MTA); **Brodersen et al. BSTS / CausalImpact** (arXiv:1506.00356 / AOAS 2015 — geo/aggregate time-series counterfactuals, not per-touchpoint MTA); **Lee et al. geo ASC vs panel-DML** (arXiv:2508.20335 — geo-level lift estimation benchmark, not per-touchpoint MTA / digital-attribution calibration); **Bojinov et al. optimal switchback experiments (arXiv:2009.00148)** — time-series / carryover experimental design, not per-touchpoint MTA label generation; **Ayala-Gómez et al. SKAdNetwork revenue attribution (arXiv:2102.08458)** — campaign-level revenue allocation from privacy-limited conversion-value counts, not multi-touch per-interaction credit for MTA-style training labels; **Aksu et al. ARA summary reports (arXiv:2311.13586)** — DP aggregate report utility optimization, not user-level MTA; **Delaney et al. DP ad conversion measurement (arXiv:2403.15224)** — DP configuration theory for measurement systems, not learnable per-touch path labels; **Ren et al. Bidding Machine (arXiv:1803.02194)** — profit-optimal RTB bidding, not multi-touch attribution credit for retention; **Yang et al. multivariable bid control (arXiv:1905.10928)** — PID-style feedback on bids using external CTR/CVR; not per-touch MTA label outputs; **Bateni et al. multiplicative bidding (arXiv:1404.6727)** — auction/representation limits of multiplicative bid languages; no touch-credit path labels; **Huang et al. generative bid shading (arXiv:2508.06550)** — first-price shading / surplus optimization; not MTA credit; **Zhang et al. RTB feedback control (arXiv:1603.01055)** — KPI stabilization and cross-channel budget control; not MTA credit; **Chiong et al. incentivized ads funnel (arXiv:1709.00197)** — rewarded-ad quasi-experiments / selection modeling; not multi-touch fractional credit; **Liu et al. individual advertising effect (arXiv:1903.04149)** — AD-day aggregate continuous treatment + leverage-rate bidding; explicitly not PV/impression MTA labels in source; **Geng et al. bandit audience evaluation (arXiv:1907.02178)** — overlapping TA allocation for creative testing; not MTA credit.
- **50% check:** ⌈0.5 × 62⌉ = **31** → **31 ≥ 31 (met).** Core MTA sequencing: **expansion-cluster harvesting unblocked** for subsequent runs (still gate large batches on queue health). **Phase 4 gate:** **62 ≥ 60** → **Phase 4 may start** per `requirements.md` (after Phase 3.7 cross-reference mapping is complete for the survey corpus).

## Engineering blog search log (requirements B1–B11)

Logged 2026-04-12 against `requirements.md` blog queries. Null or off-topic called out explicitly.

| ID | Query (abbrev) | Result |
|----|----------------|--------|
| B1 | `site:netflixtechblog.com attribution OR incrementality OR retention` | **Papers found:** Netflix TechBlog causal survey (`a-survey-of-causal-inference-applications-at-netflix`); proxy metrics / experiments / incremental Iceberg processing posts. **No posts titled specifically “multi-touch attribution.”** |
| B2 | `site:engineering.fb.com attribution OR incrementality` | **Papers found:** Instagram notification management (causal inference + incremental value of notifications; budget-style cohort selection). Other hits less on-topic (build tooling, infra). |
| B3 | `site:research.google multi-touch attribution` | **Papers found:** Google Research pubs on MTA (TEDDA time-to-event MTA; attribution evaluation user-matched paths; causal framework for digital attribution; pay-per-conversion multiple attribution; DASS simulation). |
| B4 | `site:ai.googleblog.com marketing mix OR attribution OR incrementality` | **Papers found:** Search ad incrementality / organic interaction posts (2011–2012); DP ads prediction (2022); TracIn (training data influence — peripheral). |
| B5 | `site:engineering.linkedin.com attribution OR incrementality OR multi-touch` | **Mixed:** GTM team page mentions MTA in passing; mostly A/B platform, UMP, DataFu “incremental” Hadoop processing — **no dedicated MTA engineering article in top results.** |
| B6 | `site:doordash.engineering incrementality` | **Papers found:** Marketing / causal posts (early attribution indicators; back-door pre/post; metrics layer). “Incrementality” word often appears for search indexing — marketing incrementality posts still surfaced. |
| B7 | `site:eng.uber.com causal inference attribution` | **Papers found:** Causal inference overview; mediation modeling; feature rollout regression attribution; offline inferences; experimentation platform (synthetic control / DiD). |
| B8 | `site:medium.com/airbnb-engineering attribution OR incrementality` | **Papers found:** ACE causal inference; selection bias in online experiments; listing LTV (incremental vs baseline); host marketing / channel measurement; KDD recap. |
| B9 | `site:medium.com/pinterest-engineering attribution` | **Hits found; not marketing MTA:** posts use “attribute” in ML/NLP sense (text attributes, product attributes, ads ranking context) — **no clear ad multi-touch attribution methodology post in top results.** |
| B10 | `site:shopify.engineering incrementality` | **No posts with “incrementality” in title surfaced;** quasi-experiments / counterfactuals and propensity matching (Shopify Capital) — **related causal measurement, not keyword “incrementality.”** |
| B11 | `site:stripe.com/blog/engineering attribution` | **no results from Stripe engineering blog** (for this exact query). |

## To Process — active

*(empty — Core MTA 50% threshold **met** after batch 2026-04-12h: numerator **31** vs ⌈0.5×**62**⌉=**31**.)*

## To Process — on hold

*(empty)*

## To Process — backlog (Semantic Scholar / harvest)

*(empty — harvest as needed; Semantic Scholar may still rate-limit — prefer arXiv `pdf/` URLs + `arxiv.org/abs` metadata checks.)*

## Done

- 2017_arXiv_PreBidRandomization_Counterfactual-Incrementality-Ad-Buying-Platform.md | Counterfactual-based Incrementality Measurement in a Digital Ad-Buying Platform | 2026-04-12 | nlm:1da934c4-41ee-4ccf-97fd-edf2debcbb40
- 2023_arXiv_PIE_Predicted-Incrementality-Experimentation-Ad-Measurement.md | Predicted Incrementality by Experimentation (PIE) for Ad Measurement | 2026-04-12 | nlm:277ebfa5-b5d7-4529-a3b1-a29633d8c2ec
- 2026_arXiv_MoAE_MAC-Multiple-Attribution-Benchmark.md | MAC: Conversion Prediction Benchmark Under Multiple Attribution Mechanisms | 2026-04-12 | nlm:2932b65c-3ee5-45d4-a96f-8711f1665661
- 2025_CIKM_MAL_Multi-Attribution-Learning-Conversion-Prediction.md | See Beyond a Single View: Multi-Attribution Learning for Conversion Prediction | 2026-04-12 | nlm:c2192f82-8a4d-402a-95f3-3c168dffd6d9
- 2025_KDD_CABB_Taxonomy-Weighting-Click-Buy-Recommendations.md | Click A, Buy B: Rethinking Conversion Attribution in E-Commerce Recommendations | 2026-04-12 | nlm:e49f28e4-94f0-4041-853f-3a67bfcaf09e
- 2025_arXiv_CausalCalibration_Amazon-Ads-Multi-Touch-Attribution.md | Amazon Ads Multi-Touch Attribution (Lewis, Zettelmeyer et al.) | 2026-04-12 | nlm:e8d0aa30-63dc-4243-a285-4d2a88d3139a
- 2015_ADKDD_ProbMTA_Multi-Touch-Attribution-Budget-Allocation.md | Multi-Touch Attribution Based Budget Allocation in Online Advertising (Geyik, Saxena, Dasdan) | 2026-04-12 | nlm:e1878a23-cd60-4a4b-b283-fb93f60261b6
- 2018_arXiv_HCC_Incrementality-Bidding-Attribution.md | Incrementality Bidding & Attribution (Lewis, Wong) | 2026-04-12 | nlm:e1f2b067-916b-49a5-a443-d90783a7dc18
- 2025_arXiv_LiDDA_Data-Driven-Attribution-LinkedIn.md | LiDDA: Data Driven Attribution at LinkedIn (Bencina et al.) | 2026-04-12 | nlm:437bfd53-c6c5-420c-8bcc-074f64a6fd2d
- 2021_ACMCS_NA_Unified-Survey-Treatment-Effect-Heterogeneity-Uplift.md | A Unified Survey of Treatment Effect Heterogeneity Modelling and Uplift Modelling (Zhang, Li, Liu; arXiv:2007.12769) | 2026-04-12 | nlm:571ee251-c19f-4cf6-ae53-79ad8a628a02
- 2019_WWW_CASV_Shapley-Meets-Uniform-Axiomatic-Attribution.md | Shapley Meets Uniform: An Axiomatic Framework for Attribution in Online Advertising (WWW 2019) | 2026-04-12 | nlm:f0e879c2-d3ea-4d92-86ee-b570c1d0488a
- 2016_IJRM_MarkovWalk_Mapping-Customer-Journey-Attribution.md | Mapping the customer journey: Lessons learned from graph-based online attribution modeling (Anderl et al., IJRM 2016) | 2026-04-12 | nlm:23a07141-c384-4be6-a302-88e7e28634ef
- 2017_ICML_CFR-TARNet_Estimating-Individual-Treatment-Effect.md | Estimating Individual Treatment Effect: Generalization Bounds and Algorithms (Shalit, Johansson, Sontag) | 2026-04-11 | nlm:6f515f41-7002-4b13-8a01-261ef2116b66
- 2019_NeurIPS_DragonNet_Adapting-Neural-Networks-Treatment-Effects.md | Adapting Neural Networks for the Estimation of Treatment Effects (Shi, Blei, Veitch) | 2026-04-11 | nlm:7ef430d5-29ca-43d4-9db2-753d806884e6
- 2018_EconJnl_DML_Double-Debiased-Machine-Learning-Treatment.md | Double/Debiased Machine Learning for Treatment and Structural Parameters (Chernozhukov et al.) | 2026-04-11 | nlm:2d9499a9-7a57-4a1d-b418-8a5847f8400a
- 2019_PNAS_X-learner_Meta-learners-Heterogeneous-Treatment-Effects.md | Meta-learners for Estimating Heterogeneous Treatment Effects using Machine Learning (Kunzel et al.) | 2026-04-11 | nlm:144a3c4d-fddd-432f-a564-4118c4513db6
- 2018_JASA_CausalForest_Estimation-Inference-Heterogeneous-Treatment-Random-Forests.md | Estimation and Inference of Heterogeneous Treatment Effects using Random Forests (Wager, Athey) | 2026-04-11 | nlm:c3bd72c8-4b16-4b59-b84c-2c8201d0c6ad
- 2022_AnnAppStat_TrimmedMatch_Robust-Causal-Inference-Geo-Experiments.md | Robust Causal Inference for Incremental Return on Ad Spend with Randomized Paired Geo Experiments (Chen, Au) | 2026-04-11 | nlm:df7e94ad-9a0d-4e99-be9d-8867fc981a3c
- 2022_KDD_CausalMTA_Eliminating-User-Confounding-Bias.md | CausalMTA: Eliminating the User Confounding Bias for Causal Multi-touch Attribution (Yao et al.) | 2026-04-11 | nlm:e95f1aa5-c182-46f8-9f69-f0e93981e653
- 2018_CIKM_DARNN_Multi-touch-Conversion-Attribution-Dual-Attention.md | Learning Multi-touch Conversion Attribution with Dual-attention Mechanisms for Online Advertising (Ren et al.) | 2026-04-11 | nlm:a360ce91-2838-4e83-8be9-8fa7393b43da
- 2021_Biometrika_R-learner_Quasi-Oracle-Heterogeneous-Treatment-Effects.md | Quasi-Oracle Estimation of Heterogeneous Treatment Effects (Nie, Wager) | 2026-04-11 | nlm:495692a6-2740-4dd8-87bc-b70999d3bea3
- 2018_arXiv_ShapleyMTA_Shapley-Value-Methods-Attribution-Online-Advertising.md | Shapley Value Methods for Attribution Modeling in Online Advertising (Zhao et al.) | 2026-04-11 | nlm:fd869ed4-f4b2-415f-b4cc-7b28ceb22839
- 2019_arXiv_JDMTA_Causally-Driven-Incremental-Multi-Touch-Attribution-RNN.md | Causally Driven Incremental Multi Touch Attribution Using a Recurrent Neural Network (Du et al.) | 2026-04-11 | nlm:e152841e-f9e6-4fb7-a5bc-0be02b2aba0c
- 2018_arXiv_DNAMTA_Deep-Neural-Net-Attention-Multi-touch-Attribution.md | Deep Neural Net with Attention for Multi-channel Multi-touch Attribution (Arava et al.) | 2026-04-11 | nlm:45051c3b-fe0d-4758-a9b3-09a16014ca7d
- 2020_ICDM_CAMTA_Causal-Attention-Model-Multi-touch-Attribution.md | CAMTA: Causal Attention Model for Multi-touch Attribution (Kumar et al.) | 2026-04-11 | nlm:c45bf88d-cbf3-4626-a6e9-8d34151d96d1
- 2020_arXiv_DeepMTA_Interpretable-Deep-Learning-Multi-touch-Attribution.md | Interpretable Deep Learning Model for Online Multi-touch Attribution (DeepMTA) | 2026-04-11 | nlm:81cf5e57-0a1d-487c-8693-0674e7651e45
- 2023_JDS_TEDDA_Time-to-Event-Framework-Multi-touch-Attribution.md | A Time To Event Framework For Multi-touch Attribution (Shender et al.) | 2026-04-11 | nlm:4613bfca-6fd7-40b1-b2c0-ddb48d84e79a
- 2023_arXiv_GraphicalMTA_Graphical-Point-Process-Framework-Multi-Touch-Attribution.md | A Graphical Point Process Framework for Understanding Removal Effects in Multi-Touch Attribution (Tao et al.) | 2026-04-11 | nlm:785eb7f5-2763-42fd-9aca-6826a7952265
- 2024_arXiv_DCRMTA_Unbiased-Causal-Representation-Multi-touch-Attribution.md | DCRMTA: Unbiased Causal Representation for Multi-touch Attribution (Tang et al.) | 2026-04-11 | nlm:3b866824-d85f-4e0e-a9e9-b2db65966090
- 2019_JMLR_pycox_Time-to-Event-Neural-Networks-Cox-Regression.md | Time-to-Event Prediction with Neural Networks and Cox Regression (Kvamme et al.) | 2026-04-11 | nlm:b489cad2-ad49-42ab-b821-b36e2ba93787
- 2021_arXiv_TrimmedMatchDesign_Randomized-Paired-Geo-Experiments.md | Trimmed Match Design for Randomized Paired Geo Experiments (Chen, Longfils, Remy) | 2026-04-11 | nlm:7767c144-accb-4137-8c79-b51b3c2582c9
- 2020_DoorDash_CausalHTE_Leveraging-Causal-Modeling-Flat-Experiment-Results.md | Leveraging Causal Modeling to Get More Value from Flat Experiment Results (DoorDash) | 2026-04-11 | nlm:a8d42764-41f4-4e19-8d19-fbfbcbfe5a29
- 2022_DoorDash_Switchback_Incrementality-App-Marketplace-Search-Ads.md | Adapted Switch-back Testing to Quantify Incrementality for App Marketplace Search Ads (DoorDash) | 2026-04-11 | nlm:b0a03f3d-57e9-477a-bb8f-3aadb44f1838
- 2022_Netflix_CausalInference_Survey-Applications-at-Netflix.md | A Survey of Causal Inference Applications at Netflix | 2026-04-11 | nlm:5d32e0d2-953e-4394-a3fd-14872e301647
- 2018_AAAI_DeepHit_Deep-Learning-Survival-Analysis-Competing-Risks.md | DeepHit: A Deep Learning Approach to Survival Analysis With Competing Risks (Lee et al.) | 2026-04-11 | nlm:bc8bd9c0-e5e9-4a30-b326-f47421301d84
- 2024_WSDM_CausalMMM_Learning-Causal-Structure-Marketing-Mix-Modeling.md | CausalMMM: Learning Causal Structure for Marketing Mix Modeling | 2026-04-12 | nlm:00df251e-e6b0-4930-9df7-3d0ed6402586
- 2025_arXiv_DeepCausalMMM_Deep-Learning-MMM-Causal-Inference.md | DeepCausalMMM: Deep Learning MMM with Causal Inference | 2026-04-12 | nlm:9d4780a1-6cdc-444e-a19b-e5d2b120c984
- 2024_arXiv_Robyn_Packaging-Media-Mix-Modeling-Open-Source.md | Packaging Up Media Mix Modeling: Introduction to Robyn’s Open-Source Approach | 2026-04-12 | nlm:fadcf6fc-8429-452f-a072-ff6c4eae3f4f
- 2015_AnnAppStat_CausalImpact_Bayesian-Structural-Time-Series.md | Inferring Causal Impact Using Bayesian Structural Time-Series Models | 2026-04-12 | nlm:1435a2fe-68b9-42d6-abed-bd213385393b
- 2025_KDDWorkshop_GeoPanelDML_Dynamic-Synthetic-Controls-Panel-DML.md | Dynamic Synthetic Controls vs Panel-Aware DML for Geo-Level Marketing Impact Estimation | 2026-04-12 | nlm:84dc637b-b17b-4047-8e68-2ebfb0723fac
- 2020_arXiv_MinimaxSwitchback_Design-Analysis-Switchback-Experiments.md | Design and Analysis of Switchback Experiments (Bojinov, Simchi-Levi, Zhao) | 2026-04-12 | nlm:55ddfd32-d84a-4b99-937a-78a6d3f28b7e
- 2021_arXiv_ConversionValue_Revenue-Attribution-iOS14-F2P-Games.md | Show me the Money: Measuring Marketing Performance in Free-to-Play Games using Apple’s App Tracking Transparency Framework | 2026-04-12 | nlm:ea001aae-dbdb-4145-b8be-3c596f153c24
- 2023_arXiv_ARA-SummaryReports_Optimization-Privacy-Sandbox-Attribution-Reporting.md | Summary Reports Optimization in the Privacy Sandbox Attribution Reporting API | 2026-04-12 | nlm:18707385-4385-4b47-b3a0-a78ff573da47
- 2024_PETS_DP_Ad-Conversion-Measurement.md | Differentially Private Ad Conversion Measurement | 2026-04-12 | nlm:d33597b7-ba44-4162-8ab9-f0463ee4ff9f
- 2018_arXiv_BiddingMachine_Learning-Bid-Profit-Display-Advertising.md | Bidding Machine: Learning to Bid for Directly Optimizing Profits in Display Advertising | 2026-04-12 | nlm:6c2aafec-9a4b-4e45-8c09-7d4273e010bf
- 2022_arXiv_BayesianMAR_Bayesian-Modeling-Marketing-Attribution.md | Bayesian Modeling of Marketing Attribution | 2026-04-12 | nlm:55e68092-c6ed-4cf2-bc0e-870e1dba46b6
- 2020_arXiv_GTMM_Some-Game-Theoretic-Marketing-Attribution-Models.md | Some game theoretic marketing attribution models (Molina, Tejada, Weiss) | 2026-04-12 | nlm:69d1b0ed-25eb-49de-8aea-f3c4f0d5f144
- 2017_arXiv_AAB_Attribution-Modeling-Efficiency-Bidding-Display-Advertising.md | Attribution Modeling Increases Efficiency of Bidding in Display Advertising (Diemert et al.) | 2026-04-12 | nlm:1d1ac7e0-f9ca-4380-be36-53d791cb14b0
- 2017_AAAI_AMTA_Additional-Multi-Touch-Attribution-Online-Advertising.md | Additional Multi-Touch Attribution for Online Advertising (Ji & Wang, AAAI 2017) | 2026-04-12 | nlm:686dbad6-be4b-49cd-a060-8e103a93e03e
- 2014_ICDM_STMTA_Multi-Touch-Attribution-Survival-Theory-Online-Advertising.md | Multi-touch Attribution in Online Advertising with Survival Theory (Zhang, Yuan, Wang, ICDM 2014) | 2026-04-12 | nlm:fbbf4a49-1b58-44d8-998c-950d1de2dc47
- 2012_ADKDD_CMAR_Causally-Motivated-Attribution-Online-Advertising.md | Causally Motivated Attribution for Online Advertising (Dalessandro et al., ADKDD 2012) | 2026-04-12 | nlm:bdc6ea29-e9fe-412d-b1b6-c04d75cab910
- 2019_arXiv_PID-MVC_Bid-Optimization-Multivariable-Control-Display-Advertising.md | Bid Optimization by Multivariable Control in Display Advertising | 2026-04-12 | nlm:fa77e466-5ad4-4754-a7db-11192b7a5457
- 2014_arXiv_MultiplicativeBidding_Online-Advertising.md | Multiplicative Bidding in Online Advertising | 2026-04-12 | nlm:e3eebd7e-33b3-4131-a724-a60f884bf04d
- 2025_arXiv_GenerativeBidShading_Real-Time-Bidding-Advertising.md | Generative Bid Shading in Real-Time Bidding Advertising | 2026-04-12 | nlm:36fc13ad-a3ec-42c2-bf5f-e3db3fa69bda
- 2016_arXiv_FeedbackControl_Real-Time-Display-Advertising.md | Feedback Control of Real-Time Display Advertising | 2026-04-12 | nlm:2ef85ff4-30b3-421d-8033-46af2019b42b
- 2017_arXiv_RewardedAds_Incentivized-Advertising-Conversion-Funnel.md | Understanding the Effect of Incentivized Advertising along the Conversion Funnel | 2026-04-12 | nlm:f149cf93-82eb-4f7e-8ab4-f9ed574704ae
- 2019_arXiv_IAE-LeverageRate_Estimating-Individual-Advertising-Effect-E-Commerce.md | Estimating Individual Advertising Effect in E-Commerce | 2026-04-12 | nlm:87cc65ee-2606-4173-9f06-a076bedab630
- 2019_arXiv_ContextualBandit_Audience-Evaluation-Targeted-Advertising.md | Online Evaluation of Audiences for Targeted Advertising via Bandit Experiments | 2026-04-12 | nlm:4c7c9646-a696-4ad9-9569-4607b93d040f
- 2025_arXiv_PVM_Beyond-Last-Click-Optimal-Mechanism-Ad-Attribution.md | Beyond Last-Click: Optimal Mechanism for Ad Attribution (Peer-Validated Mechanism / PVM) | 2026-04-12 | nlm:d46a683f-6ac4-47b3-994d-52b1e4418699
- 2011_arXiv_ASS_Axiomatic-Attribution-Multilinear-Functions.md | Axiomatic Attribution for Multilinear Functions (Sun & Sundararajan) | 2026-04-12 | nlm:a1aa3e37-f43b-4be5-9190-df6139a2d913
- 2026_arXiv_NA_Statistical-Learning-from-Attribution-Sets.md | Statistical Learning from Attribution Sets | 2026-04-12 | nlm:2be1c16e-7de3-477e-a788-f47e9f1b1b6d
- 2024_arXiv_NA_Unraveling-Consumer-Purchase-Journey-Neural-Networks.md | Unraveling Consumer Purchase Journey Using Neural Network Models | 2026-04-12 | nlm:52dc09e5-3135-4632-8145-acbcbf64f56e

## Skipped

- Multiply-Robust Causal Change Attribution (2024) | tangentially relevant — focuses on population-level attribution shifts, not user-level MTA
- Rosenbaum & Rubin 1983 propensity score paper | seminal but pre-2015 and theory-only, no direct MTA application — add to background reading queue if needed
- Multiple Treatments Causal Effects Estimation with Task Embeddings (2025) | too new, insufficient citations, peripheral to core MTA
- Data-driven multi-touch attribution models (Shao & Li — KDD 2011) | https://dl.acm.org/doi/10.1145/2020408.2020453 | nlm:failed:paywall (ACM DL) — **free-version attempts (Run 2, 2026-04-12):** `site:arxiv.org` / arXiv title search — no ACM-equivalent preprint found; SSRN — no obvious canonical preprint in quick search; Semantic Scholar — not re-queried this session; author homepage — not re-queried this session. Remains skipped until an **institutionally or publisher-authorized** open PDF is confirmed (do not ingest unverified third-party mirrors without license check).
