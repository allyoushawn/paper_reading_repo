Date: 2026-04-12 (last updated — batch 2026-04-12h)
Topic: Multi-touch attribution and incrementality estimation for user retention

# Attribution-Based Retention - Methodology Fundamentality Tracking

This file is accumulated automatically while reading PDFs during Phase 3 batch processing.
Update after each batch. Final sorting happens in Phase 3.5.

## Methodology Table

| Method Name | Proposal Paper (Year) | Baseline Mention Count | Derived Variant Count | Independent Measured Performance (Dataset: metric | source) | Component Count | Simplicity Score (1-5) | Performance Consistency Score (1-5) | Fundamentality Composite Score |
|---------|----------------|-------------------|----------------|--------------------------------------|-------------|-----------------|----------------------|----------------|
| CFR (Counterfactual Regression) | Shalit et al. ICML 2017 | 5 (DragonNet, CAMTA, DeepMTA, DCRMTA, CausalMTA) | 3 (TARNet, DragonNet, SITE) | IHDP PEHE: 0.76 (CFR WASS) vs 2.1 (BNN) — Shalit 2017 | 3 (shared repr + 2 heads) | 4 | 4 | 35 |
| TARNet | Shalit et al. ICML 2017 | 4 (DragonNet, CAMTA, DeepMTA, DCRMTA) | 1 (DragonNet) | IHDP MAE: 0.13 — DragonNet 2019 | 2 (shared repr + 2 heads, no IPM) | 5 | 4 | 31 |
| Causal Forest / GRF | Wager & Athey JASA 2018 | 6 (CFR, DragonNet, X-learner, DML, CausalMTA, DeepHit) | 2 (GRF package, policy forests) | IHDP PEHE: 3.8 — Shalit 2017; MSE 0.02 as d→30 — Wager 2018 | 3 (honest splits + RF + infinitesimal jackknife) | 4 | 5 | 39 |
| X-learner | Kunzel et al. PNAS 2019 | 2 (DML, R-learner) | 1 (X-BART) | Voter turnout: beats T-learner in unbalanced designs — Kunzel 2019 | 3 (μ₀/μ₁ + imputation + propensity weighting) | 4 | 3 | 25 |
| T-learner | Kunzel et al. PNAS 2019 (formalized) | 3 (X-learner, R-learner, DML) | 0 | Standard CATE baseline across many papers | 2 (two separate outcome models) | 5 | 3 | 22 |
| S-learner | Kunzel et al. PNAS 2019 (formalized) | 2 (X-learner, R-learner) | 0 | Biased in small treatment groups | 1 (single model with treatment indicator) | 5 | 2 | 17 |
| DML (Double/Debiased ML) | Chernozhukov et al. EconJnl 2018 | 3 (R-learner, X-learner, DragonNet) | 2 (DML2, DDML R package) | 401k eligibility: ~$8k-10k (vs naive $19k) — Chernozhukov 2018 | 2 (Neyman ortho + K-fold crossfit) | 4 | 4 | 29 |
| DragonNet | Shi et al. NeurIPS 2019 | 3 (CAMTA, DeepMTA, DCRMTA) | 1 (targeted regularization variant) | ACIC 2018 MAE: 0.35 vs 1.45 baseline — Shi 2019 | 3 (shared repr + 2 outcome heads + 1 propensity head) | 4 | 4 | 29 |
| Trimmed Match (iROAS) | Chen & Au AnnAppStat 2022 | 1 (Trimmed Match Design) | 1 (Trimmed Match Design for geo) | RMSE 1.96 vs 20.09 (log-normal, n=40) — Chen 2022 | 2 (trimmed mean ratio estimation + CI inversion) | 5 | 4 | 24 |
| TMLE (Targeted Max Likelihood) | van der Laan & Rubin 2006 | 3 (DragonNet, DML, X-learner) | 0 (used as comparison) | Degrades catastrophically when initial estimate is poor — Shi 2019 | 4 (init + update + efficient influence curve) | 3 | 2 | 19 |
| IPW (Inverse Propensity Weighting) | Classical statistics | 5 (CFR, DML, X-learner, DragonNet, CausalForest) | 0 | Standard doubly robust component | 1 (propensity reweighting) | 5 | 3 | 28 |
| Infinitesimal Jackknife Variance | Efron; Wager et al. 2014 | 2 (CausalForest, R-learner) | 0 | Valid CI for forest estimators — Wager 2018 | 1 | 5 | 4 | 24 |
| DARNN (Dual Attention RNN) | Ren et al. CIKM 2018 | 3 (CAMTA, CausalMTA, DCRMTA) | 0 | AUC 0.868 on Taobao vs LR 0.801 — Ren 2018 | 4 (user LSTM + ad LSTM + dual attention + contribution scoring) | 3 | 3 | 22 |
| DNAMTA (Time-Decay Attention) | Arava et al. Adobe 2018 | 3 (CAMTA, CausalMTA, DCRMTA) | 0 | AUC 0.879 vs LR 0.846; display weight 0.642→0.411 w/ decay — Arava 2018 | 4 (LSTM + touchpoint att + time-decay att + fusion) | 3 | 3 | 22 |
| CAMTA (CRN + Adversarial Deconfounding) | Kumar et al. ICDM 2020 | 3 (CausalMTA, DCRMTA, DARNN) | 1 (DCRMTA extends it) | Criteo AUC 0.9591 vs DNAMTA 0.9119; Taobao 8.2% profit improvement — Kumar 2020 | 4 (CRN + GRL adversarial + hierarchical att + conversion pred) | 3 | 4 | 28 |
| CausalMTA (VRAE + Static/Dynamic Bias) | Yao et al. KDD 2022 | 2 (DCRMTA, industry refs) | 1 (DCRMTA) | Synthetic AUC 0.7749; budget allocation 32% conv at 10% cost — Yao 2022 | 5 (VRAE encoder + static deconf + dynamic GRL + Shapley + MLP) | 2 | 3 | 20 |
| DCRMTA (Causal Attention Module) | Tang et al. arXiv 2024 | 0 (newest) | 0 | Synthetic AUC 0.8009 vs CausalMTA 0.7749; Criteo-custom AUC 0.7991 — Tang 2024 | 3 (Causal Journey LSTM+GRL + CAM + fusion MLP) | 4 | 4 | 24 |
| Shapley Value MTA | Zhao et al. arXiv 2018 | 2 (JDMTA, DCRMTA) | 2 (JDMTA incremental variant, DeepMTA Shapley regression) | Simplified formula: (2n−1)× speedup over Shapley exact — Zhao 2018 | 2 (ordered Shapley + simplified formula) | 5 | 3 | 23 |
| Incremental Shapley (RNN + Mixed Exact/MC) | Du et al. JDMTA 2019 | 1 (DCRMTA) | 0 | 101.24 orders/min exact vs 4.2 MC; deployed 7B impressions — Du 2019 | 3 (bi-LSTM + incremental Shapley + mixed exact/MC) | 4 | 4 | 21 |
| DeepMTA (Phased-LSTM + Shapley Regression) | Zhong et al. eBay 2020 | 1 (GraphicalMTA) | 0 | AUC 0.91 eBay 100k; Natural Search 32.1%, Paid Search 20.5% — Zhong 2020 | 3 (Phased-LSTM + powerset masks + Shapley regression) | 4 | 3 | 19 |
| TEDDA (Poisson Process + Backwards Elimination) | Shender et al. Google JDS 2023 | 0 (recent) | 0 | AICPE matches ICPE (13.87% both, Scenario 4) — Shender 2023 | 3 (Poisson process + log-linear intensity + backwards elimination) | 4 | 3 | 19 |
| Graphical Point Process MTA | Tao et al. arXiv 2023 | 0 (recent) | 0 | TRE KL 0.008 vs DNAMTA 0.012; Fortune 500: display 14.2% TRE vs 10.7% DRE — Tao 2023 | 4 (Granger causality graph + conditional intensity + TRE + ADMM) | 3 | 3 | 18 |
| Cox-Time (Non-Proportional Neural Cox) | Kvamme et al. JMLR 2019 | 2 (DeepHit comparison, survival benchmarks) | 1 (pycox package) | KKBox IBS 0.107, IBLL −0.334 (best calibration, 1.7M users) — Kvamme 2019 | 2 (MLP/LSTM + time as covariate) | 5 | 4 | 25 |
| DeepHit (Discrete PMF Competing Risks) | Lee et al. AAAI 2018 | 4 (pycox, TEDDA, DeepMTA, survival benchmarks) | 1 (DeepHit variants for EHR) | KKBox C-index 0.858 (best rank); worst IBS/IBLL (worst calibration) — Kvamme 2019 | 3 (shared embedding + K cause heads + joint loss) | 4 | 3 | 25 |
| Trimmed Match Design (Non-bipartite Matching) | Chen, Longfils, Remy Google 2021 | 1 (companion to Trimmed Match Chen&Au 2022) | 0 | Reducing n 50→45 pairs cuts RMSE 50%; optimal pairing 3× RMSE reduction — Chen 2021 | 3 (optimal pairing + cross-validation + holdback simulation) | 4 | 4 | 23 |
| Switchback Incrementality Testing | DoorDash 2022 | 0 | 0 | Incrementality scalar computed for app marketplace; 95% CI bootstrap | 3 (alternating time design + bootstrapped CI + scalar calibration) | 4 | 3 | 19 |
| S-learner CATE (LightGBM + NCE) | DoorDash 2020 | 0 | 0 | 33% reduction Promotional Cost/Incremental Delivery at 5% reach — DoorDash 2020 | 2 (single LightGBM + noise contrastive estimation) | 5 | 3 | 22 |
| Causal Ranker Framework | Netflix 2022 | 0 | 0 | Production deployment; improved recommendation causal relevance — Netflix 2022 | 5 (impression attribution + true negative labels + causal est + offline eval + serving) | 2 | 3 | 15 |
| Bellmania (Markov Chain LTV) | Netflix 2022 | 0 | 0 | Enables optimal price discount policy — Netflix 2022 | 3 (on/off Netflix states + transition estimation + incremental LTV) | 4 | 3 | 19 |
| Markov Graph MTA (first/higher-order walks) | Anderl et al. IJRM 2016 | 0 | 0 | Substantial vs last-click on 4 multi-channel datasets — abstract-level summary Run 2 | 2 (graph transitions + Markov orders) | 4 | 3 | 20 |
| CASV + Markov Axiomatic Attribution | WWW 2019 | 0 | 0 | CASV ↔ adjusted unique-uniform under Markov funnel — theory + large-scale numerics cited | 3 (axioms + CASV + Markov funnel) | 3 | 3 | 19 |
| LiDDA (Transformer DDA + MMM calibration) | Bencina et al. arXiv 2025 | 0 | 0 | ROC/PR-AUC >0.97 offline; email holdout lift gaps ~−2% to +2.4% vs experiment — LinkedIn 2025 | 5+ (attention + imputation + calibration + sessionization + entity/LLM embeds) | 2 | 4 | 22 |
| Causal Calibration MTA (RCT + ML ensemble) | Lewis, Zettelmeyer et al. Amazon 2025 | 0 | 0 | System paper; corrects 488%–948% observational bias via RCT calibration — Amazon 2025 | 3 (RCT ground truth + LTA/MDA ensemble + calibration regression) | 4 | 3 | 19 |
| Probabilistic MTA (first-order empirical weights) | Geyik, Saxena, Dasdan ADKDD 2014 | 0 | 0 | MTA budget alloc >> LTA in 12-day live A/B; 63.5% budget→highest ROI line item — Turn 2014 | 2 (empirical action prob + normalized weight attribution) | 5 | 3 | 19 |
| HCC / Incrementality Bidding (IV + Hausman correction) | Lewis & Wong Netflix 2018 | 0 | 0 | HCC: OLS 1.82 → HCC 1.37 → 2SLS 1.31 (true 1.32) at N=400K sim — Lewis 2018 | 5 (continuous-time ad stock + ghost bid IV + HCC + Bayesian bootstrap + down-sampling) | 2 | 3 | 15 |
| Pre-Bid RCT DSP Incrementality | Chalasani et al. arXiv 2017 | 0 | 0 | Stable positive ATL/INC across seven MediaMath campaigns vs naive marginal/negative lift — production logs | 4 (hash pre-bid assign + win-bias ATT + Gibbs CIs + CID aggregation) | 3 | 3 | 17 |
| PIE (Predicted Incrementality by Experimentation) | Gordon et al. arXiv 2023 | 0 | 0 | Out-of-sample R² 0.88 vs 0.19 raw LCC-7D on 2,226 Meta Conversion Lift RCTs — paper | 2 (random forest mapping + pre/post campaign features) | 4 | 4 | 20 |
| MoAE (Mixture of Asymmetric Experts) | Wu et al. arXiv 2026 | 0 | 0 | GAUC +2.12pt vs BASE (last-click target) on MAC — paper Table 3/4 | 4 (MoE backbone + asymmetric transfer + per-mechanism MLP heads) | 3 | 3 | 19 |
| MAL (AKA + CAT + PTP) | Chen et al. CIKM 2025 | 0 | 0 | +0.51% GAUC / +2.6% ROI online Taobao display vs production Base — paper | 4 (multitask AKA towers + CAT combinatorial aux + PTP fusion) | 3 | 4 | 21 |
| Taxonomy CF CABB weighting (CABA/CABB multitask) | Zeng et al. KDD 2025 | 0 | 0 | NE 0.495 vs 0.575 last-click baseline; +0.25% online primary metric — paper | 4 (shared embeddings + dual heads + taxonomy/CF α weights + λ-balanced loss) | 4 | 3 | 20 |
| CausalMMM (GNN Granger MMM + carryover/saturation decoder) | Gong et al. WSDM 2024 | 0 | 0 | Sim AUROC +5.7–7.1% vs Granger/NGC/GVAR/InGRA; AirMMM MSE best at M=7 — paper | 4 (relational encoder + temporal module + saturation module + VI) | 3 | 3 | 18 |
| DeepCausalMMM (GRU + NO TEARS DAG + Hill + multi-region) | Tirumala arXiv 2025 | 0 | 0 | Holdout R² 0.918 vs train 0.947 (3% gap) on 190-DMA demo — paper | 5 (GRU + DAG opt + Hill + region heads + robust losses) | 3 | 3 | 17 |
| Robyn (Prophet + Ridge + Nevergrad tri-objective mMM) | Runge et al. arXiv 2024 / Meta | 0 | 0 | Community case studies (e.g., +17% sales Talisa; Lemonade +78% YoY cited) — paper | 5 (Prophet + ridge + Nevergrad + calibration hooks + allocator) | 3 | 3 | 17 |
| CausalImpact / BSTS counterfactual STS | Brodersen et al. AOAS 2015 | 0 | 0 | Geo ad lift 88,400 clicks vs 84,700 RCT linear baseline (<5% dev.) — paper | 4 (local trend + seasonality + spike-slab controls + MCMC) | 3 | 4 | 19 |
| Augmented SCM ridge (ASC-Y / ASC-DEM / ASC-DEM-LAG) | Ben-Michael et al. 2021 (`augsynth`) | 0 | 0 | Sim: severe bias/near-zero coverage under S1/S3–S5 stress vs DML — Lee 2025 workshop | 3 (ridge weights + optional covariates + lags) | 4 | 2 | 16 |
| Panel-aware DML (TWFE / WG / FD / CRE + XGBoost nuisances) | Lee et al. KDD CIMLIP workshop 2025 | 0 | 0 | WG-DML strong under nonlinear/shock; CRE-DML robust to control drift (S5) — paper | 5 (panel transform + cross-fit XGB + IPTW trim + WLS + cluster SE) | 2 | 3 | 16 |
| Minimax optimal switchback design (carryover-aware randomization) | Bojinov et al. arXiv 2020 | 0 | 0 | Worst-case risk 26.78 vs naive 33.67 ($T=120,m=2$ sim) — paper | 4 (minimax subset + HT estimator + exact/asymp tests + carryover-ID) | 3 | 3 | 17 |
| SKAdNetwork conversion-value → revenue attribution ($g$ optimizer) | Ayala-Gómez et al. arXiv 2021 | 0 | 0 | D7 RR + N within ~4% norm. error of D30 PV+U at $p=2$ — paper | 3 (schema $f$ + privacy sim + attribution function $g$) | 4 | 3 | 17 |
| ARA summary-report parameter optimization ($\mathrm{RMSRE}_\tau$) | Aksu et al. arXiv 2023 | 0 | 0 | Figure 5 dominates equal-budget baselines across $\varepsilon\in\{1,\ldots,64\}$ — paper | 4 (slice partition + clip/budget search + DLap noise + reconstructor $R$) | 3 | 3 | 17 |
| $C_0$-valid DP conversion measurement (rule × adjacency × enforcement) | Delaney et al. PoPETs 2024 | 0 | 0 | Classification of valid/invalid configs (Table 5) — paper | 4 (attribution map + bound point + adjacency + Laplace scale) | 2 | 4 | 18 |
| Bidding Machine (EU/RR profit gradients + landscape + linear bid) | Ren et al. arXiv 2018 | 0 | 0 | Online EU +25.5% profit vs CE (89M auctions) — paper | 5 (CTR $\theta$ + landscape $\phi$ + bid $b$ + FTRL loop + budget solve) | 2 | 4 | 18 |
| Bayesian MAR (decayed exposures + interactions + MCMC) | Sinha et al. arXiv 2022 | 0 | 0 | Synthetic parameter recovery + Adobe Analytics stratified sample — paper | 4 (link + decay + interaction + random effects) | 3 | 3 | 17 |
| GTMM (TU sum-game + bankruptcy PROP/CEL + fictitious players) | Molina et al. arXiv 2020 | 0 | 0 | Axiomatic toy campaigns — paper | 3 (sum-game + Shapley + bankruptcy rules) | 4 | 3 | 17 |
| Attribution-aware Bidder + AEU (decay × marginal attributed conv.) | Diemert et al. arXiv 2017 | 0 | 0 | +5.5% OEC online Criteo — paper | 3 (decay MLE + marginal factor + AEU replay) | 4 | 3 | 18 |
| AMTA (competing hazards + intrinsic conversion rate + EM) | Ji & Wang AAAI 2017 | 1 (Zhang ICDM 2014) | 0 | AUC vs LTA/FTL/Shapley Miaozhen — paper | 4 (hazard + EM + path likelihood credit) | 3 | 3 | 21 |
| ADDITIVEHAZARD / survival MTA (exp kernels + MM) | Zhang et al. ICDM 2014 | 0 | 1 (AMTA) | F1 vs heuristics Miaozhen — paper | 3 (additive intensity + MM + touch removal) | 4 | 3 | 18 |
| Causal Ω-Shapley channel attribution | Dalessandro et al. ADKDD 2012 | 1 (Molina 2020 cites) | 0 | 38–73% retargeting credit reallocation — paper | 3 (logistic model + Ω + Shapley) | 3 | 3 | 20 |
| Attribution-set unbiased ERM | Applebaum et al. arXiv 2026 | 0 | 0 | MNIST/CIFAR/Higgs with synthetic attribution windows vs baselines — paper | 3 (affine binary loss + set combinatorics + ERM) | 4 | 3 | 18 |
| UDDA (upstream-prefix matched incremental DDA) | Sapp & Vaver Google 2016 | 0 | 0 | DASS virtual-experiment curves vs matched-pairs DDA — paper | 3 (prefix match + incremental rate diff + aggregation) | 4 | 3 | 19 |
| PVM (path-based virtual valuation mechanism) | An et al. arXiv 2025 | 0 | 0 | DSIC/IR/welfare proofs + revenue vs SPwA examples — paper | 3 (second-price + PVM rule + product-form conversion) | 3 | 3 | 15 |
| CDA (PCMCI+ → SCM channel effects) | Filippou & Tsamardinos arXiv 2025 | 0 | 0 | Synthetic SCM + aggregated marketing series — paper | 4 (PCMCI+ graph + SCM encode + do-interventions) | 3 | 3 | 17 |
| CVR systematic review (taxonomy) | Xue et al. IPM/arXiv 2026 | 0 | 0 | PRISMA survey synthesis 2015–2025 — paper | 1 (narrative taxonomy) | 5 | 3 | 14 |
| Multivariable PID feedback bid control (budget + CPC constraints) | Yang et al. arXiv 2019 | 0 | 0 | RTB campaign simulations under dual constraints — paper | 4 (primal-dual LP + PID on hyperparameters + CTR/CVR plug-in + feedback loop) | 3 | 3 | 16 |
| Multiplicative bidding language / matroid-style approximation | Bateni et al. arXiv 2014 | 0 | 0 | Welfare vs unrestricted bids in stylized auctions — paper | 3 (multiplicative expressibility + LP relaxation + rounding) | 4 | 3 | 17 |
| Generative end-to-end bid shading (FPA RTB) | Huang et al. arXiv 2025 | 0 | 0 | Surplus vs two-stage OR shading baselines — paper | 3 (generative model + policy gradient + win-feedback debias) | 3 | 3 | 16 |
| Feedback control for RTB KPI regulation | Zhang et al. arXiv 2016 | 0 | 0 | eCPC/AWR stability vs fixed PID — paper | 4 (multi-channel budget + reference tracking + piecewise bidding + simulator) | 3 | 3 | 16 |
| Endogenous treatment + copula selection model (rewarded ads) | Chiong et al. arXiv 2017 | 0 | 0 | Install lift vs propensity baselines on mobile impressions — paper | 4 (selection + click + install system + Clayton copula + MALA) | 2 | 3 | 15 |
| Individual advertising effect (IAE) + leverage-rate bidding | Liu et al. arXiv 2019 | 0 | 0 | AD-day continuous treatment vs A/B uplift — paper | 4 (representation balancing + dose-response net + leverage metric + bid rule) | 3 | 3 | 16 |
| Contextual bandit overlapping audience evaluation | Geng et al. arXiv 2019 | 0 | 0 | Regret vs uniform / greedy allocation in simulations — paper | 3 (partition graph + UCB-style scoring + overlap constraints) | 4 | 3 | 17 |
| Peer-Validated Mechanism (PVM) last-click replacement | An et al. arXiv 2025 | 0 | 0 | Homogeneous \(n=2\) accuracy 0.75 vs LCM UB ≈0.343; sim gains up to +0.3041 accuracy at \(n=5\) — paper | 4 (peer thresholds + priors \(\beta_i\) + eligibility filter + KDE sim harness) | 3 | 3 | 17 |
| Aumann–Shapley–Shubik axiomatic multilinear attribution | Sun & Sundararajan EC 2011 / arXiv:1102.0989 | 0 | 0 | Uniqueness on multilinear+additive class under Dummy/Additivity/CN/ASI/Anonymity — paper | 2 (path integral of partials + axiom bundle) | 4 | 4 | 20 |
| Neural ensemble + Shapley touchpoint importance (tabular counts) | Churchill, Li, Xiu arXiv 2024 | 0 | 0 | Balanced accuracy ≈0.776 (3×10 sigmoid MLP ensemble) vs classical/GBDT baselines — paper | 4 (31-D counts + 10-seed ensemble + threshold + Shapley post) | 3 | 3 | 18 |

## How to Compute the Fundamentality Composite Score

Composite score = (baseline mention count × 3) + (derived variant count × 2) + (simplicity score × 1) + (performance consistency score × 2)

- baseline mention count: in how many other papers this method was used as a comparison baseline
- derived variant count: number of papers that directly modified/extended this method
- simplicity score: 5 = 1–2 components, 4 = 3 components, 3 = 4 components, 2 = 5 components, 1 = 6+ components
- performance consistency score: higher when reported numbers across independent papers have lower variance (5 = stddev < 0.5%, 1 = > 3%)

## Top Method Analysis (Phase 3.5 — Sorted by Composite Score)

Sorted by Fundamentality Composite Score (desc):

| Rank | Method | Score | Why It Matters |
|------|--------|-------|----------------|
| 1 | Causal Forest / GRF | 39 | Highest citation baseline count (6); used as baseline in virtually every CATE paper; strong across many regimes |
| 2 | CFR (Counterfactual Regression) | 35 | Foundational neural CATE method; spawned TARNet, DragonNet; widely cited in MTA papers |
| 3 | TARNet | 31 | Simplified CFR (no IPM); most common neural CATE baseline |
| 4 | DML (Double/Debiased ML) | 29 | Semiparametric gold standard for production CATE; used at Netflix, industry-wide |
| 5 | DragonNet | 29 | Best NeurIPS 2019 neural CATE; adds propensity head to TARNet; strong on IHDP/ACIC |
| 6 | IPW | 28 | Classical doubly-robust building block; referenced in 5 papers |
| 7 | CAMTA | 28 | Best causal MTA method with solid benchmark results; spawned DCRMTA |
| 8 | X-learner | 25 | Handles unbalanced treatment groups; standard CATE toolkit entry |
| 9 | Cox-Time | 25 | Best calibration survival model; directly applicable to subscription churn (KKBox) |
| 10 | DeepHit | 25 | Best C-index survival model; competing risks; standard benchmark baseline |
| 11 | Shapley Value MTA | 23 | Foundational MTA attribution method; spawned incremental Shapley variants |
| 12 | Trimmed Match Design | 23 | Google's gold-standard geo experiment design; open source |
| 13 | T-learner | 22 | Simplest CATE baseline; always referenced as lower bound |
| 14 | DARNN | 22 | First deep RNN MTA model; cited as baseline by all subsequent MTA papers |
| 15 | DNAMTA | 22 | First attention MTA model; standard baseline in causal MTA papers |
| 16 | S-learner (DoorDash) | 22 | Simplest possible CATE (one model); noise contrastive estimation for non-RCT data |
| 17 | Trimmed Match (iROAS) | 24* | Robust nonparametric geo iROAS estimator; open source trimmed_match package |
| 18 | DCRMTA | 24 | Latest causal MTA (2024); Causal Attention Module improves on CausalMTA |
| 19 | Infinitesimal Jackknife Var | 24 | Valid CI for random forests; cited in CausalForest and R-learner |

*Trimmed Match score from original tracker (24) — listed here for reference.

### Key Insights for Dating Platform Attribution

**Top-tier for direct deployment (Scores ≥28 + industry validated):**
1. **Causal Forest / GRF** — best for heterogeneous treatment effect estimation; handles any feature set; grf R package production-ready
2. **DML** — best for high-dimensional confounders; Netflix deploys this for localization incremental value
3. **CFR / TARNet / DragonNet** — neural CATE; best when user features are high-dimensional and MLP embedding helps

**Top MTA methods for multi-touch sequence attribution:**
1. **CAMTA** (Score 28) — best benchmark results; GRL deconfounding removes user bias; Taobao 8.2% profit validated
2. **DCRMTA** (Score 24) — extends CAMTA with Causal Attention Module; best 2024 results
3. **Shapley Value MTA + Incremental Shapley** — interpretable; simplified formula tractable at scale

**Best survival models for churn prediction:**
1. **Cox-Time** (Score 25) — best calibration; directly applicable to subscription churn (KKBox 1.7M users)
2. **DeepHit** (Score 25) — best discrimination; competing risks (cancellation vs inactivity vs delete)

**Geo/incrementality measurement:**
1. **Trimmed Match + Trimmed Match Design** — Google open source; best-in-class iROAS estimation + robust design
2. **Switchback Testing** (DoorDash) — applicable when no user-level randomization available

**Caution:** CausalMTA (Score 20) and pure S-learner (Score 22) have lower scores — CausalMTA overcorrects by eliminating all user influence; S-learner is biased under unbalanced treatment. Prefer DCRMTA over CausalMTA; prefer X-learner or DML over S-learner for CATE.
