Date: 2026-04-14
Topic: Multi-touch attribution & incrementality for retention-style labeling (attribution-based incremental user retention)
Paper count: 62

# Multi-touch attribution & incrementality for retention-style labeling — Literature Review

## Meta

- Corpus: **62** papers from `queue.md` **Done**, each with a matching `./read-papers/<file>.md` on disk (verified 2026-04-14).
- **NotebookLM Phase 4-A (2026-04-14):** seven full-notebook `notebook_query` calls (no `source_ids`) **succeeded**; verbatim answers are in `nlm-phase4-raw-responses.md`. This review’s **Executive Summary**, **Most Promising**, **Practical Recommendations**, and **Cross-notebook synthesis** sections were refreshed from those responses, with spot-checks against existing `read-papers/` notes where a claim ties to a specific paper file.
- `read-papers/` also contains **three** extra markdown files not listed in **Done** (not counted in the 62): `2016_Google_UDDA_Toward-Improving-Digital-Attribution-Model-Accuracy.md`, `2025_arXiv_CDA_Causal-Driven-Attribution-Channel-Influence-Aggregate-Data.md`, `2026_IPM_NA_Conversion-Rate-Prediction-Online-Advertising-Review.md`.

## Executive Summary

NotebookLM’s cross-corpus read (Query 1) clusters methods into **deep sequence models with attention** (fractional credit via learned weights), **Shapley / cooperative-game allocations** (fairness-structured credit), **causal and counterfactual identification** (potential outcomes, representation balancing, double machine learning, causal forests), **survival and point-process temporal models** (intensities, time-to-event MTA), **MMM and budget/bidding** layers (allocation and auction dynamics adjacent to touch credit), **privacy-limited measurement** (attribution sets, DP reporting), and **evaluation/benchmark culture** (Criteo-family logs, CVR multi-task suites). For **Phase 1** (per-interaction fractional **supervision** when “conversion” is **continuous engagement**), the same synthesis plus Queries 3 and 6–7 emphasize: **(i)** sequence MTA lines that **deconfound user activity** while still emitting **path-level weights**; **(ii)** **time-to-event / intensity** views as the closest native language for **ongoing** outcomes; **(iii)** **experiments** (RCT, geo, switchback) and industry calibration stories as the practical way to keep observational credits from training a downstream model on **pure selection**.

### Most Promising Approaches

1. **Deep sequence MTA with causal debiasing (CAMTA → CausalMTA → DCRMTA lineage in Query 1 / 5 baseline map):** explicitly discussed as the modern way to couple **attention-based fractional credit** with **confounding control**—aligned with Project Context’s “active users get more touches.”
2. **Continuous-time / intensity formulations (TEDDA-style time-to-event MTA, hazard/survival constructions, graphical point processes in Query 6):** map touches to **rates** and **removal-style** counterfactuals—closer to user-days-active than single purchase labels.
3. **Shapley-based credits on top of debiased or carefully scoped predictors (Query 1 cooperative-game thread + Query 6):** preserves **complete** additive decompositions at channel or feature granularity when paired with a model that does not trivially encode activity bias.

### Practical Recommendations

Short term (1–3 months):
- Treat **Criteo-style public logs** (Query 2) as **sanity benchmarks** for prototype labelers, not as proof of causal retention lift; pair any observational credit with **at least one** calibration channel called out in Query 7 (RCT where feasible; geo or switchback where interference or privacy breaks user-level RCT).
- Instrument **overlap and uncertainty** (Query 3 CATE discussion): wide intervals under overlap violations are a first-class risk for using credits as training targets.

Mid term (3–6 months):
- Close the gaps Query 3 flags most often: **integrate MTA outputs with bidding/RL**, **privacy-constrained learning** (attribution sets, DP budgets), **spillover/carryover**, and **interpretability vs black-box accuracy** for credits consumed by humans and by student models.
- Keep **CATE/uplift** as **segment-level evaluation or priors** (per Project Context alignment note in `requirements.md`), not as a wholesale substitute for per-touch fractional labels.

## Cross-notebook synthesis (NLM Queries 6–7)

**Query 6 (continuous engagement as outcome):** NLM argues that **continuous-time “ad stock”** constructions, **time-to-event / intensity models** (including TEDDA-style backwards elimination on intensities), **graphical point processes** with removal-effect scores, and **deep sequence models with causal attention / adversarial debiasing** are the closest matches for **fractional per-interaction credit** when the KPI behaves like a **rate or duration** (user-days-active analogy) rather than one purchase bit. **Axiomatic / Shapley** machinery appears as the **allocation rule on top of** a model whose increments are well-defined.

**Query 7 (selection bias and calibration):** NLM stresses **activity-induced endogeneity**—high-activity users accumulate touches **and** high baseline propensity—so naive path models conflate organic propensity with ad effect. It recommends anchoring “honest” path credits with **RCTs**, **geo experiments** (with designs aimed at noisy geo panels), and **switchback** style designs under interference, then using those increments to **audit or recalibrate** observational MTA outputs before they become supervision for a student model.

---

## 1. Core neural, causal & multi-attribution learning MTA (14 papers)

Sequence models, causal debiasing, attention/Shapley hybrids, and benchmarks that emit path-level weights usable (with caveats) as fractional credit signals.

### A Graphical Point Process Framework for Understanding Removal Effects in Multi-Touch Attribution (Tao et al.) (arXiv preprint 2023)

- Source: arXiv preprint 2023
- Detailed analysis: [read-papers/2023_arXiv_GraphicalMTA_Graphical-Point-Process-Framework-Multi-Touch-Attribution.md](./read-papers/2023_arXiv_GraphicalMTA_Graphical-Point-Process-Framework-Multi-Touch-Attribution.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Point-process/graphical framework for removal-effect style multi-touch reasoning.

---

### A Time To Event Framework For Multi-touch Attribution (Shender et al.) (Journal of Data Science 2023)

- Source: Journal of Data Science 2023
- Detailed analysis: [read-papers/2023_JDS_TEDDA_Time-to-Event-Framework-Multi-touch-Attribution.md](./read-papers/2023_JDS_TEDDA_Time-to-Event-Framework-Multi-touch-Attribution.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Google time-to-event MTA formulation linking intensities to attribution.

---

### CAMTA: Causal Attention Model for Multi-touch Attribution (Kumar et al.) (ICDM 2020)

- Source: ICDM 2020
- Detailed analysis: [read-papers/2020_ICDM_CAMTA_Causal-Attention-Model-Multi-touch-Attribution.md](./read-papers/2020_ICDM_CAMTA_Causal-Attention-Model-Multi-touch-Attribution.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Adversarial deconfounding plus hierarchical attention yields path weights aligned with causal MTA goals for confounded engagement sequences.

---

### Causally Driven Incremental Multi Touch Attribution Using a Recurrent Neural Network (Du et al.) (arXiv preprint 2019)

- Source: arXiv preprint 2019
- Detailed analysis: [read-papers/2019_arXiv_JDMTA_Causally-Driven-Incremental-Multi-Touch-Attribution-RNN.md](./read-papers/2019_arXiv_JDMTA_Causally-Driven-Incremental-Multi-Touch-Attribution-RNN.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
RNN with incremental Shapley-style credit for scalable industrial MTA.

---

### CausalMTA: Eliminating the User Confounding Bias for Causal Multi-touch Attribution (Yao et al.) (KDD 2022)

- Source: KDD 2022
- Detailed analysis: [read-papers/2022_KDD_CausalMTA_Eliminating-User-Confounding-Bias.md](./read-papers/2022_KDD_CausalMTA_Eliminating-User-Confounding-Bias.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Formal static+dynamic user confounding in MTA; Shapley credits on a debiased sequential predictor—closest methodological analog to dating-style activity bias.

---

### Click A, Buy B: Rethinking Conversion Attribution in E-Commerce Recommendations (KDD 2025)

- Source: KDD 2025
- Detailed analysis: [read-papers/2025_KDD_CABB_Taxonomy-Weighting-Click-Buy-Recommendations.md](./read-papers/2025_KDD_CABB_Taxonomy-Weighting-Click-Buy-Recommendations.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Taxonomy-aware multitask weighting for click→buy mismatch; adjacent to attribution label noise in recommender conversions.

---

### DCRMTA: Unbiased Causal Representation for Multi-touch Attribution (Tang et al.) (arXiv preprint 2024)

- Source: arXiv preprint 2024
- Detailed analysis: [read-papers/2024_arXiv_DCRMTA_Unbiased-Causal-Representation-Multi-touch-Attribution.md](./read-papers/2024_arXiv_DCRMTA_Unbiased-Causal-Representation-Multi-touch-Attribution.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Extends causal MTA by preserving causal user features while debiasing sequences; strong recent benchmark for path-level Shapley credits.

---

### Deep Neural Net with Attention for Multi-channel Multi-touch Attribution (Arava et al.) (arXiv preprint 2018)

- Source: arXiv preprint 2018
- Detailed analysis: [read-papers/2018_arXiv_DNAMTA_Deep-Neural-Net-Attention-Multi-touch-Attribution.md](./read-papers/2018_arXiv_DNAMTA_Deep-Neural-Net-Attention-Multi-touch-Attribution.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Time-decay attention LSTM MTA baseline preceding causal extensions.

---

### Interpretable Deep Learning Model for Online Multi-touch Attribution (DeepMTA) (arXiv preprint 2020)

- Source: arXiv preprint 2020
- Detailed analysis: [read-papers/2020_arXiv_DeepMTA_Interpretable-Deep-Learning-Multi-touch-Attribution.md](./read-papers/2020_arXiv_DeepMTA_Interpretable-Deep-Learning-Multi-touch-Attribution.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Interpretable phased LSTM with Shapley regression for e-commerce style paths.

---

### Learning Multi-touch Conversion Attribution with Dual-attention Mechanisms for Online Advertising (Ren et al.) (CIKM 2018)

- Source: CIKM 2018
- Detailed analysis: [read-papers/2018_CIKM_DARNN_Multi-touch-Conversion-Attribution-Dual-Attention.md](./read-papers/2018_CIKM_DARNN_Multi-touch-Conversion-Attribution-Dual-Attention.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Early dual-attention RNN MTA baseline still used in causal MTA comparisons.

---

### MAC: Conversion Prediction Benchmark Under Multiple Attribution Mechanisms (arXiv preprint 2026)

- Source: arXiv preprint 2026
- Detailed analysis: [read-papers/2026_arXiv_MoAE_MAC-Multiple-Attribution-Benchmark.md](./read-papers/2026_arXiv_MoAE_MAC-Multiple-Attribution-Benchmark.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Mixture-of-experts benchmark across multiple attribution mechanisms—useful for evaluating label robustness under mechanism shift.

---

### See Beyond a Single View: Multi-Attribution Learning for Conversion Prediction (CIKM 2025)

- Source: CIKM 2025
- Detailed analysis: [read-papers/2025_CIKM_MAL_Multi-Attribution-Learning-Conversion-Prediction.md](./read-papers/2025_CIKM_MAL_Multi-Attribution-Learning-Conversion-Prediction.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Multi-attribution learning consumes partial-credit labels to improve conversion metrics—downstream of label generation.

---

### Statistical Learning from Attribution Sets (arXiv preprint 2026)

- Source: arXiv preprint 2026
- Detailed analysis: [read-papers/2026_arXiv_NA_Statistical-Learning-from-Attribution-Sets.md](./read-papers/2026_arXiv_NA_Statistical-Learning-from-Attribution-Sets.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Learning under coarse attribution sets—bridges privacy-style ambiguity to supervised objectives.

---

### Unraveling Consumer Purchase Journey Using Neural Network Models (arXiv preprint 2024)

- Source: arXiv preprint 2024
- Detailed analysis: [read-papers/2024_arXiv_NA_Unraveling-Consumer-Purchase-Journey-Neural-Networks.md](./read-papers/2024_arXiv_NA_Unraveling-Consumer-Purchase-Journey-Neural-Networks.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Neural ensemble plus Shapley over tabular touchpoint counts—empirical Shapley credit from predictors.

---

## 2. Shapley, axiomatic & causally motivated ad attribution (5 papers)

Cooperative-game and axiomatic credit rules that define unique or structured allocations over channels or touches.

### Axiomatic Attribution for Multilinear Functions (Sun & Sundararajan) (arXiv preprint 2011)

- Source: arXiv preprint 2011
- Detailed analysis: [read-papers/2011_arXiv_ASS_Axiomatic-Attribution-Multilinear-Functions.md](./read-papers/2011_arXiv_ASS_Axiomatic-Attribution-Multilinear-Functions.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Aumann–Shapley–Shubik style credits for multilinear conversion surrogates—per-dimension incremental primitives.

---

### Causally Motivated Attribution for Online Advertising (Dalessandro et al., ADKDD 2012) (AdKDD / KDD applied 2012)

- Source: AdKDD / KDD applied 2012
- Detailed analysis: [read-papers/2012_ADKDD_CMAR_Causally-Motivated-Attribution-Online-Advertising.md](./read-papers/2012_ADKDD_CMAR_Causally-Motivated-Attribution-Online-Advertising.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Early causally motivated Ω-Shapley channel attribution in logistic models.

---

### Shapley Meets Uniform: An Axiomatic Framework for Attribution in Online Advertising (WWW 2019) (WWW 2019)

- Source: WWW 2019
- Detailed analysis: [read-papers/2019_WWW_CASV_Shapley-Meets-Uniform-Axiomatic-Attribution.md](./read-papers/2019_WWW_CASV_Shapley-Meets-Uniform-Axiomatic-Attribution.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Axiomatic Shapley–uniform framework tying unique credits to Markov funnels.

---

### Shapley Value Methods for Attribution Modeling in Online Advertising (Zhao et al.) (arXiv preprint 2018)

- Source: arXiv preprint 2018
- Detailed analysis: [read-papers/2018_arXiv_ShapleyMTA_Shapley-Value-Methods-Attribution-Online-Advertising.md](./read-papers/2018_arXiv_ShapleyMTA_Shapley-Value-Methods-Attribution-Online-Advertising.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Foundational ordered-Shapley approximations for scalable MTA.

---

### Some game theoretic marketing attribution models (Molina, Tejada, Weiss) (arXiv preprint 2020)

- Source: arXiv preprint 2020
- Detailed analysis: [read-papers/2020_arXiv_GTMM_Some-Game-Theoretic-Marketing-Attribution-Models.md](./read-papers/2020_arXiv_GTMM_Some-Game-Theoretic-Marketing-Attribution-Models.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Game-theoretic TU games and bankruptcy-style allocation toy models for marketing splits.

---

## 3. Markov journeys, hazards & probabilistic path models (5 papers)

Graph- or intensity-based path formulations, survival/hazard MTA, and Bayesian decay models complementary to deep MTA.

### Additional Multi-Touch Attribution for Online Advertising (Ji & Wang, AAAI 2017) (AAAI 2017)

- Source: AAAI 2017
- Detailed analysis: [read-papers/2017_AAAI_AMTA_Additional-Multi-Touch-Attribution-Online-Advertising.md](./read-papers/2017_AAAI_AMTA_Additional-Multi-Touch-Attribution-Online-Advertising.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Competing-hazard MTA with EM path likelihood credit.

---

### Bayesian Modeling of Marketing Attribution (arXiv preprint 2022)

- Source: arXiv preprint 2022
- Detailed analysis: [read-papers/2022_arXiv_BayesianMAR_Bayesian-Modeling-Marketing-Attribution.md](./read-papers/2022_arXiv_BayesianMAR_Bayesian-Modeling-Marketing-Attribution.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Bayesian hierarchical MAR with decay/interactions for path credit uncertainty.

---

### Mapping the customer journey: Lessons learned from graph-based online attribution modeling (Anderl et al., IJRM 2016) (IJRM 2016)

- Source: IJRM 2016
- Detailed analysis: [read-papers/2016_IJRM_MarkovWalk_Mapping-Customer-Journey-Attribution.md](./read-papers/2016_IJRM_MarkovWalk_Mapping-Customer-Journey-Attribution.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Classic graph/Markov customer-journey attribution reference.

---

### Multi-Touch Attribution Based Budget Allocation in Online Advertising (Geyik, Saxena, Dasdan) (AdKDD / KDD applied 2015)

- Source: AdKDD / KDD applied 2015
- Detailed analysis: [read-papers/2015_ADKDD_ProbMTA_Multi-Touch-Attribution-Budget-Allocation.md](./read-papers/2015_ADKDD_ProbMTA_Multi-Touch-Attribution-Budget-Allocation.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Turn-style probabilistic first-order MTA tied to budget allocation uplift.

---

### Multi-touch Attribution in Online Advertising with Survival Theory (Zhang, Yuan, Wang, ICDM 2014) (ICDM 2014)

- Source: ICDM 2014
- Detailed analysis: [read-papers/2014_ICDM_STMTA_Multi-Touch-Attribution-Survival-Theory-Online-Advertising.md](./read-papers/2014_ICDM_STMTA_Multi-Touch-Attribution-Survival-Theory-Online-Advertising.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Survival-theoretic multi-touch attribution with additive hazards.

---

## 4. Industry measurement, incrementality & production-style systems (16 papers)

Large-platform write-ups and methods linking experiments, calibration, or transformer-scale attribution to deployment constraints.

### A Survey of Causal Inference Applications at Netflix (Netflix TechBlog 2022)

- Source: Netflix TechBlog 2022
- Detailed analysis: [read-papers/2022_Netflix_CausalInference_Survey-Applications-at-Netflix.md](./read-papers/2022_Netflix_CausalInference_Survey-Applications-at-Netflix.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Broad causal inference deployment patterns including measurement adjacent to attribution.

---

### Amazon Ads Multi-Touch Attribution (Lewis, Zettelmeyer et al.) (arXiv preprint 2025)

- Source: arXiv preprint 2025
- Detailed analysis: [read-papers/2025_arXiv_CausalCalibration_Amazon-Ads-Multi-Touch-Attribution.md](./read-papers/2025_arXiv_CausalCalibration_Amazon-Ads-Multi-Touch-Attribution.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Amazon Ads RCT calibration of observational MTA ensembles—gold template for debiasing label pipelines.

---

### Attribution Modeling Increases Efficiency of Bidding in Display Advertising (Diemert et al.) (arXiv preprint 2017)

- Source: arXiv preprint 2017
- Detailed analysis: [read-papers/2017_arXiv_AAB_Attribution-Modeling-Efficiency-Bidding-Display-Advertising.md](./read-papers/2017_arXiv_AAB_Attribution-Modeling-Efficiency-Bidding-Display-Advertising.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Shows attributed marginal conversions improve bidding efficiency—uses external MTA signals.

---

### Beyond Last-Click: Optimal Mechanism for Ad Attribution (Peer-Validated Mechanism / PVM) (arXiv preprint 2025)

- Source: arXiv preprint 2025
- Detailed analysis: [read-papers/2025_arXiv_PVM_Beyond-Last-Click-Optimal-Mechanism-Ad-Attribution.md](./read-papers/2025_arXiv_PVM_Beyond-Last-Click-Optimal-Mechanism-Ad-Attribution.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Mechanism-design last-platform attribution under strategic reporting—peripheral to per-touch retention labels.

---

### Bid Optimization by Multivariable Control in Display Advertising (arXiv preprint 2019)

- Source: arXiv preprint 2019
- Detailed analysis: [read-papers/2019_arXiv_PID-MVC_Bid-Optimization-Multivariable-Control-Display-Advertising.md](./read-papers/2019_arXiv_PID-MVC_Bid-Optimization-Multivariable-Control-Display-Advertising.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Multivariable control for bid hyperparameters under plug-in CTR/CVR.

---

### Bidding Machine: Learning to Bid for Directly Optimizing Profits in Display Advertising (arXiv preprint 2018)

- Source: arXiv preprint 2018
- Detailed analysis: [read-papers/2018_arXiv_BiddingMachine_Learning-Bid-Profit-Display-Advertising.md](./read-papers/2018_arXiv_BiddingMachine_Learning-Bid-Profit-Display-Advertising.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Profit-optimal bidding using landscape learning—not MTA label output.

---

### Counterfactual-based Incrementality Measurement in a Digital Ad-Buying Platform (arXiv preprint 2017)

- Source: arXiv preprint 2017
- Detailed analysis: [read-papers/2017_arXiv_PreBidRandomization_Counterfactual-Incrementality-Ad-Buying-Platform.md](./read-papers/2017_arXiv_PreBidRandomization_Counterfactual-Incrementality-Ad-Buying-Platform.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
DSP-level pre-bid RCT for counterfactual incrementality at campaign scale.

---

### Estimating Individual Advertising Effect in E-Commerce (arXiv preprint 2019)

- Source: arXiv preprint 2019
- Detailed analysis: [read-papers/2019_arXiv_IAE-LeverageRate_Estimating-Individual-Advertising-Effect-E-Commerce.md](./read-papers/2019_arXiv_IAE-LeverageRate_Estimating-Individual-Advertising-Effect-E-Commerce.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Individual advertising effect with leverage-rate bidding—aggregate continuous treatment framing.

---

### Feedback Control of Real-Time Display Advertising (arXiv preprint 2016)

- Source: arXiv preprint 2016
- Detailed analysis: [read-papers/2016_arXiv_FeedbackControl_Real-Time-Display-Advertising.md](./read-papers/2016_arXiv_FeedbackControl_Real-Time-Display-Advertising.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
RTB feedback control for KPI tracking.

---

### Generative Bid Shading in Real-Time Bidding Advertising (arXiv preprint 2025)

- Source: arXiv preprint 2025
- Detailed analysis: [read-papers/2025_arXiv_GenerativeBidShading_Real-Time-Bidding-Advertising.md](./read-papers/2025_arXiv_GenerativeBidShading_Real-Time-Bidding-Advertising.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Generative shading in first-price auctions.

---

### Incrementality Bidding & Attribution (Lewis, Wong) (arXiv preprint 2018)

- Source: arXiv preprint 2018
- Detailed analysis: [read-papers/2018_arXiv_HCC_Incrementality-Bidding-Attribution.md](./read-papers/2018_arXiv_HCC_Incrementality-Bidding-Attribution.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Hausman-corrected incrementality bidding linking ghost-bid IV to attributed outcomes.

---

### LiDDA: Data Driven Attribution at LinkedIn (Bencina et al.) (arXiv preprint 2025)

- Source: arXiv preprint 2025
- Detailed analysis: [read-papers/2025_arXiv_LiDDA_Data-Driven-Attribution-LinkedIn.md](./read-papers/2025_arXiv_LiDDA_Data-Driven-Attribution-LinkedIn.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
LinkedIn transformer data-driven attribution with experiment calibration—production MTA reference.

---

### Multiplicative Bidding in Online Advertising (arXiv preprint 2014)

- Source: arXiv preprint 2014
- Detailed analysis: [read-papers/2014_arXiv_MultiplicativeBidding_Online-Advertising.md](./read-papers/2014_arXiv_MultiplicativeBidding_Online-Advertising.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Auction expressivity of multiplicative bid languages.

---

### Online Evaluation of Audiences for Targeted Advertising via Bandit Experiments (arXiv preprint 2019)

- Source: arXiv preprint 2019
- Detailed analysis: [read-papers/2019_arXiv_ContextualBandit_Audience-Evaluation-Targeted-Advertising.md](./read-papers/2019_arXiv_ContextualBandit_Audience-Evaluation-Targeted-Advertising.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Overlapping audience bandit evaluation for creatives.

---

### Predicted Incrementality by Experimentation (PIE) for Ad Measurement (arXiv preprint 2023)

- Source: arXiv preprint 2023
- Detailed analysis: [read-papers/2023_arXiv_PIE_Predicted-Incrementality-Experimentation-Ad-Measurement.md](./read-papers/2023_arXiv_PIE_Predicted-Incrementality-Experimentation-Ad-Measurement.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Meta-style predicted incrementality from large RCT corpus—calibration layer, not touch credit.

---

### Understanding the Effect of Incentivized Advertising along the Conversion Funnel (arXiv preprint 2017)

- Source: arXiv preprint 2017
- Detailed analysis: [read-papers/2017_arXiv_RewardedAds_Incentivized-Advertising-Conversion-Funnel.md](./read-papers/2017_arXiv_RewardedAds_Incentivized-Advertising-Conversion-Funnel.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Selection/copula model along incentivized install funnels.

---

## 5. Marketing mix modeling & aggregate channel causal structure (3 papers)

Shop- or market-level time series and deep MMM variants—aggregate complements to user-level MTA, not per-touch label generators.

### CausalMMM: Learning Causal Structure for Marketing Mix Modeling (WSDM 2024)

- Source: WSDM 2024
- Detailed analysis: [read-papers/2024_WSDM_CausalMMM_Learning-Causal-Structure-Marketing-Mix-Modeling.md](./read-papers/2024_WSDM_CausalMMM_Learning-Causal-Structure-Marketing-Mix-Modeling.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Causal graph discovery for channel-level MMM.

---

### DeepCausalMMM: Deep Learning MMM with Causal Inference (arXiv preprint 2025)

- Source: arXiv preprint 2025
- Detailed analysis: [read-papers/2025_arXiv_DeepCausalMMM_Deep-Learning-MMM-Causal-Inference.md](./read-papers/2025_arXiv_DeepCausalMMM_Deep-Learning-MMM-Causal-Inference.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Causal graph discovery for channel-level MMM.

---

### Packaging Up Media Mix Modeling: Introduction to Robyn’s Open-Source Approach (arXiv preprint 2024)

- Source: arXiv preprint 2024
- Detailed analysis: [read-papers/2024_arXiv_Robyn_Packaging-Media-Mix-Modeling-Open-Source.md](./read-papers/2024_arXiv_Robyn_Packaging-Media-Mix-Modeling-Open-Source.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Meta open-source mMM workflow with calibration hooks.

---

## 6. Geo, panel & switchback experimental designs (5 papers)

Design and analysis tools for market- or time-randomized lift when user-level RCTs are infeasible.

### Adapted Switch-back Testing to Quantify Incrementality for App Marketplace Search Ads (DoorDash) (DoorDash engineering 2022)

- Source: DoorDash engineering 2022
- Detailed analysis: [read-papers/2022_DoorDash_Switchback_Incrementality-App-Marketplace-Search-Ads.md](./read-papers/2022_DoorDash_Switchback_Incrementality-App-Marketplace-Search-Ads.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Adapted switchback incrementality for marketplace search ads.

---

### Design and Analysis of Switchback Experiments (Bojinov, Simchi-Levi, Zhao) (arXiv preprint 2020)

- Source: arXiv preprint 2020
- Detailed analysis: [read-papers/2020_arXiv_MinimaxSwitchback_Design-Analysis-Switchback-Experiments.md](./read-papers/2020_arXiv_MinimaxSwitchback_Design-Analysis-Switchback-Experiments.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Carryover-aware switchback randomization theory.

---

### Inferring Causal Impact Using Bayesian Structural Time-Series Models (Annals of Applied Statistics 2015)

- Source: Annals of Applied Statistics 2015
- Detailed analysis: [read-papers/2015_AnnAppStat_CausalImpact_Bayesian-Structural-Time-Series.md](./read-papers/2015_AnnAppStat_CausalImpact_Bayesian-Structural-Time-Series.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
BSTS counterfactual time series for aggregate interventions.

---

### Robust Causal Inference for Incremental Return on Ad Spend with Randomized Paired Geo Experiments (Chen, Au) (Annals of Applied Statistics 2022)

- Source: Annals of Applied Statistics 2022
- Detailed analysis: [read-papers/2022_AnnAppStat_TrimmedMatch_Robust-Causal-Inference-Geo-Experiments.md](./read-papers/2022_AnnAppStat_TrimmedMatch_Robust-Causal-Inference-Geo-Experiments.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Robust iROAS estimator for paired geo experiments.

---

### Trimmed Match Design for Randomized Paired Geo Experiments (Chen, Longfils, Remy) (arXiv preprint 2021)

- Source: arXiv preprint 2021
- Detailed analysis: [read-papers/2021_arXiv_TrimmedMatchDesign_Randomized-Paired-Geo-Experiments.md](./read-papers/2021_arXiv_TrimmedMatchDesign_Randomized-Paired-Geo-Experiments.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Robust iROAS estimator for paired geo experiments.

---

## 7. Privacy-limited measurement & sandbox reporting (3 papers)

DP and summary-report mechanisms for conversion measurement under restricted identifiers.

### Differentially Private Ad Conversion Measurement (PoPETs 2024)

- Source: PoPETs 2024
- Detailed analysis: [read-papers/2024_PETS_DP_Ad-Conversion-Measurement.md](./read-papers/2024_PETS_DP_Ad-Conversion-Measurement.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Theory of valid DP ad conversion measurement configurations.

---

### Show me the Money: Measuring Marketing Performance in Free-to-Play Games using Apple’s App Tracking Transparency Framework (arXiv preprint 2021)

- Source: arXiv preprint 2021
- Detailed analysis: [read-papers/2021_arXiv_ConversionValue_Revenue-Attribution-iOS14-F2P-Games.md](./read-papers/2021_arXiv_ConversionValue_Revenue-Attribution-iOS14-F2P-Games.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
SKAdNetwork-style revenue attribution from privacy-limited conversion values.

---

### Summary Reports Optimization in the Privacy Sandbox Attribution Reporting API (arXiv preprint 2023)

- Source: arXiv preprint 2023
- Detailed analysis: [read-papers/2023_arXiv_ARA-SummaryReports_Optimization-Privacy-Sandbox-Attribution-Reporting.md](./read-papers/2023_arXiv_ARA-SummaryReports_Optimization-Privacy-Sandbox-Attribution-Reporting.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Optimizes Privacy Sandbox attribution summary reports under DP noise.

---

## 8. Survival & time-to-event baselines (2 papers)

Neural survival models for engagement/churn timelines—background for time-to-event MTA but not generic per-interaction credit.

### DeepHit: A Deep Learning Approach to Survival Analysis With Competing Risks (Lee et al.) (AAAI 2018)

- Source: AAAI 2018
- Detailed analysis: [read-papers/2018_AAAI_DeepHit_Deep-Learning-Survival-Analysis-Competing-Risks.md](./read-papers/2018_AAAI_DeepHit_Deep-Learning-Survival-Analysis-Competing-Risks.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Deep competing risks survival—discrimination-strong churn baseline.

---

### Time-to-Event Prediction with Neural Networks and Cox Regression (Kvamme et al.) (JMLR 2019)

- Source: JMLR 2019
- Detailed analysis: [read-papers/2019_JMLR_pycox_Time-to-Event-Neural-Networks-Cox-Regression.md](./read-papers/2019_JMLR_pycox_Time-to-Event-Neural-Networks-Cox-Regression.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Neural Cox/time-to-event toolkit baseline used in survival comparisons.

---

## 9. Background CATE, uplift & heterogeneous treatment learners (9 papers)

Scalar effect estimators and surveys used as statistical background and deconfounding baselines, not primary per-touch label engines.

### A Unified Survey of Treatment Effect Heterogeneity Modelling and Uplift Modelling (Zhang, Li, Liu; arXiv:2007.12769) (ACM Computing Surveys 2021)

- Source: ACM Computing Surveys 2021
- Detailed analysis: [read-papers/2021_ACMCS_NA_Unified-Survey-Treatment-Effect-Heterogeneity-Uplift.md](./read-papers/2021_ACMCS_NA_Unified-Survey-Treatment-Effect-Heterogeneity-Uplift.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Broad HTE/uplift survey—background for incrementality literacy.

---

### Adapting Neural Networks for the Estimation of Treatment Effects (Shi, Blei, Veitch) (NeurIPS 2019)

- Source: NeurIPS 2019
- Detailed analysis: [read-papers/2019_NeurIPS_DragonNet_Adapting-Neural-Networks-Treatment-Effects.md](./read-papers/2019_NeurIPS_DragonNet_Adapting-Neural-Networks-Treatment-Effects.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Targeted regularization neural CATE—common deep baseline.

---

### Double/Debiased Machine Learning for Treatment and Structural Parameters (Chernozhukov et al.) (Econometric Journal 2018)

- Source: Econometric Journal 2018
- Detailed analysis: [read-papers/2018_EconJnl_DML_Double-Debiased-Machine-Learning-Treatment.md](./read-papers/2018_EconJnl_DML_Double-Debiased-Machine-Learning-Treatment.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Double/debiased ML for high-dimensional nuisance functions.

---

### Dynamic Synthetic Controls vs Panel-Aware DML for Geo-Level Marketing Impact Estimation (KDD workshop 2025)

- Source: KDD workshop 2025
- Detailed analysis: [read-papers/2025_KDDWorkshop_GeoPanelDML_Dynamic-Synthetic-Controls-Panel-DML.md](./read-papers/2025_KDDWorkshop_GeoPanelDML_Dynamic-Synthetic-Controls-Panel-DML.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Benchmarks geo panel estimators vs synthetic controls for marketing impact.

---

### Estimating Individual Treatment Effect: Generalization Bounds and Algorithms (Shalit, Johansson, Sontag) (ICML 2017)

- Source: ICML 2017
- Detailed analysis: [read-papers/2017_ICML_CFR-TARNet_Estimating-Individual-Treatment-Effect.md](./read-papers/2017_ICML_CFR-TARNet_Estimating-Individual-Treatment-Effect.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Neural representation balancing for CATE—baseline machinery in causal MTA papers.

---

### Estimation and Inference of Heterogeneous Treatment Effects using Random Forests (Wager, Athey) (JASA 2018)

- Source: JASA 2018
- Detailed analysis: [read-papers/2018_JASA_CausalForest_Estimation-Inference-Heterogeneous-Treatment-Random-Forests.md](./read-papers/2018_JASA_CausalForest_Estimation-Inference-Heterogeneous-Treatment-Random-Forests.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Honest forests for heterogeneous treatment effects.

---

### Leveraging Causal Modeling to Get More Value from Flat Experiment Results (DoorDash) (DoorDash engineering 2020)

- Source: DoorDash engineering 2020
- Detailed analysis: [read-papers/2020_DoorDash_CausalHTE_Leveraging-Causal-Modeling-Flat-Experiment-Results.md](./read-papers/2020_DoorDash_CausalHTE_Leveraging-Causal-Modeling-Flat-Experiment-Results.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
S-learner style causal modeling on flat experiments—industrial uplift, not path credit.

---

### Meta-learners for Estimating Heterogeneous Treatment Effects using Machine Learning (Kunzel et al.) (PNAS 2019)

- Source: PNAS 2019
- Detailed analysis: [read-papers/2019_PNAS_X-learner_Meta-learners-Heterogeneous-Treatment-Effects.md](./read-papers/2019_PNAS_X-learner_Meta-learners-Heterogeneous-Treatment-Effects.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Meta-learner for heterogeneous effects with unbalanced arms.

---

### Quasi-Oracle Estimation of Heterogeneous Treatment Effects (Nie, Wager) (Biometrika 2021)

- Source: Biometrika 2021
- Detailed analysis: [read-papers/2021_Biometrika_R-learner_Quasi-Oracle-Heterogeneous-Treatment-Effects.md](./read-papers/2021_Biometrika_R-learner_Quasi-Oracle-Heterogeneous-Treatment-Effects.md)

Relevance to multi-touch attribution & incrementality for retention-style labeling:
Risk minimization formulation for CATE.

---

## References (Low Relevance)

Papers whose `read-papers` **Project Relevance** sections are explicitly flagged **Low project relevance** for Phase 1 per-touch fractional labels (still useful for budgeting, auctions, aggregate measurement, or background reading):

- [Multiplicative Bidding in Online Advertising](./read-papers/2014_arXiv_MultiplicativeBidding_Online-Advertising.md)
- [Inferring Causal Impact Using Bayesian Structural Time-Series Models](./read-papers/2015_AnnAppStat_CausalImpact_Bayesian-Structural-Time-Series.md)
- [Feedback Control of Real-Time Display Advertising](./read-papers/2016_arXiv_FeedbackControl_Real-Time-Display-Advertising.md)
- [Counterfactual-based Incrementality Measurement in a Digital Ad-Buying Platform](./read-papers/2017_arXiv_PreBidRandomization_Counterfactual-Incrementality-Ad-Buying-Platform.md)
- [Understanding the Effect of Incentivized Advertising along the Conversion Funnel](./read-papers/2017_arXiv_RewardedAds_Incentivized-Advertising-Conversion-Funnel.md)
- [Online Evaluation of Audiences for Targeted Advertising via Bandit Experiments](./read-papers/2019_arXiv_ContextualBandit_Audience-Evaluation-Targeted-Advertising.md)
- [Estimating Individual Advertising Effect in E-Commerce](./read-papers/2019_arXiv_IAE-LeverageRate_Estimating-Individual-Advertising-Effect-E-Commerce.md)
- [Bid Optimization by Multivariable Control in Display Advertising](./read-papers/2019_arXiv_PID-MVC_Bid-Optimization-Multivariable-Control-Display-Advertising.md)
- [A Unified Survey of Treatment Effect Heterogeneity Modelling and Uplift Modelling (Zhang, Li, Liu; arXiv:2007.12769)](./read-papers/2021_ACMCS_NA_Unified-Survey-Treatment-Effect-Heterogeneity-Uplift.md)
- [Predicted Incrementality by Experimentation (PIE) for Ad Measurement](./read-papers/2023_arXiv_PIE_Predicted-Incrementality-Experimentation-Ad-Measurement.md)
- [CausalMMM: Learning Causal Structure for Marketing Mix Modeling](./read-papers/2024_WSDM_CausalMMM_Learning-Causal-Structure-Marketing-Mix-Modeling.md)
- [Packaging Up Media Mix Modeling: Introduction to Robyn’s Open-Source Approach](./read-papers/2024_arXiv_Robyn_Packaging-Media-Mix-Modeling-Open-Source.md)
- [See Beyond a Single View: Multi-Attribution Learning for Conversion Prediction](./read-papers/2025_CIKM_MAL_Multi-Attribution-Learning-Conversion-Prediction.md)
- [Dynamic Synthetic Controls vs Panel-Aware DML for Geo-Level Marketing Impact Estimation](./read-papers/2025_KDDWorkshop_GeoPanelDML_Dynamic-Synthetic-Controls-Panel-DML.md)
- [Click A, Buy B: Rethinking Conversion Attribution in E-Commerce Recommendations](./read-papers/2025_KDD_CABB_Taxonomy-Weighting-Click-Buy-Recommendations.md)
- [DeepCausalMMM: Deep Learning MMM with Causal Inference](./read-papers/2025_arXiv_DeepCausalMMM_Deep-Learning-MMM-Causal-Inference.md)
- [Generative Bid Shading in Real-Time Bidding Advertising](./read-papers/2025_arXiv_GenerativeBidShading_Real-Time-Bidding-Advertising.md)
- [Beyond Last-Click: Optimal Mechanism for Ad Attribution (Peer-Validated Mechanism / PVM)](./read-papers/2025_arXiv_PVM_Beyond-Last-Click-Optimal-Mechanism-Ad-Attribution.md)

## NLM consistency check (Phase 4-C)

NotebookLM Phase 4-A **Queries 4–5** returned full text (see `nlm-phase4-raw-responses.md`). Below are **three** claims drawn from those answers, each checked against specific `read-papers/*.md` files (on-disk analyses, not the NLM prose alone).

1. **Claim (Query 5-style baseline map):** *DARNN (Ren et al., CIKM 2018) is used as a comparative baseline inside later MTA papers such as CAMTA.* **Read:** `2020_ICDM_CAMTA_Causal-Attention-Model-Multi-touch-Attribution.md`. **Result:** **Consistent** — the CAMTA write-up lists **DARNN** among eight baselines and reports comparative AUC/log-loss vs DARNN on Criteo.

2. **Claim (Query 5-style baseline map):** *Logistic / data-driven MTA (Shao & Li-style LR) appears as a baseline in the DARNN paper’s experimental table.* **Read:** `2018_CIKM_DARNN_Multi-touch-Conversion-Attribution-Dual-Attention.md`. **Result:** **Consistent** — the DARNN summary explicitly lists **LR** among five baselines and cites Shao & Li (2011) LR as a non-sequential comparator.

3. **Claim (Query 4 “foundational” narrative):** *CausalMTA positions CAMTA as a close predecessor and compares against it on Criteo.* **Read:** `2022_KDD_CausalMTA_Eliminating-User-Confounding-Bias.md`. **Result:** **Consistent with minor nuance** — the file states CausalMTA **beats CAMTA** on Criteo metrics and discusses CAMTA’s limitations (click pseudo-feedback); DCRMTA (separate file) then critiques CausalMTA’s treatment of user signals—a lineage nuance the short Query 4 blurb does not spell out.
