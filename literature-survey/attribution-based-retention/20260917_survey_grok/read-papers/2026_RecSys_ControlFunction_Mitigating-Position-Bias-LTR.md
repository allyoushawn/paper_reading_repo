# A Control Function Framework for Mitigating Position Bias in Learning to Rank Systems [1]

**Source:** https://arxiv.org/pdf/2506.06989.pdf  
**Date analyzed:** 2026-09-24  
**NLM source id:** `7915e99c-f464-494a-9ea5-dfb873b4d91f`  
**Queue id:** G33  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *A Control Function Framework for Mitigating Position Bias in Learning to Rank Systems* [1]
* **Authors:** **Md Aminul Islam**¹, **Kathryn Vasilaky**², and **Elena Zheleva**¹ [1]
* **Affiliations:** ¹**University of Illinois Chicago** (Chicago, IL, USA); ²**California Polytechnic State University** (San San Luis Obispo, CA, USA) [1]
* **Year & Venue:** Published in **2026** at the *20th ACM Conference on Recommender Systems (RecSys ’26)*, September 27–October 02, 2026, Minneapolis, MN, USA [1–2].

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Learning-to-rank (LTR) systems depend on implicit user feedback (e.g., clicks), which is inherently skewed by position bias—higher-ranked items receive disproportionately more interactions regardless of actual relevance [1, 2]. Existing position bias correction approaches suffer from key operational trade-offs:
  1. *Click models* require repeated query-item observations, making them unreliable for sparse tail queries [3].
  2. *Propensity-based (IPW) methods* rely on intrusive result randomization (degrading user experience) or joint optimization (vulnerable to model misspecification) and require modifying the ranker's loss objective [3, 4].
  3. *Econometric methods (Heckman selection models)* assume linear outcome equations, failing to model high-dimensional feature interactions or sparse clicks [3-5].
  4. *Validation Gap:* Standard models assume access to unbiased validation data or tune hyperparameters directly on biased clicks, leading to suboptimal model selection [6, 7].
* **Key Contributions:**
  1. **Control Function-based Correction (CFC):** Introduces a novel two-stage econometrics-inspired framework that corrects for position bias without explicit propensity estimation or modifying the ranker's loss function [1, 6–7].
  2. **Stage 1 (Residualization):** Models the historical ranking process using observable features to isolate exogenous ranking residuals (\\(\epsilon_{y,q,m}\\)) representing feature-unexplained ranking variation [6, 18–20].
  3. **Stage 2 (Click Modeling with Control Functions):** Incorporates residual transformations and feature interaction terms (leveraging Lewbel's identification theory for feature-dependent heteroskedasticity) as control functions in the click model [6, 24–27].
  4. **Algorithm & Objective Agnostic:** Compatible with any linear or nonlinear, pointwise, pairwise, or listwise LTR algorithm (e.g., LambdaMART, Deep Neural Networks) under both weak/strong and deterministic/stochastic logging policies [7–8, 31–32].
  5. **Validation Click Debiasing Strategy:** Proposes a method to partial out position effects from validation clicks, enabling reliable hyperparameter tuning when ground-truth relevance labels are unavailable [8, 40–42].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Architectural Components**
* **Stage 1 (Ranking Residualization):**
  * Models historical item position \\(r(y \mid \pi_q) = m(\mathbf{x}_q^y) + \epsilon_{q,m}^y\\), where \\(m(\mathbf{x}_q^y)\\) captures feature-driven rank predictable from query-item features \\(\mathbf{x}_q^y\\) [19–20].
  * Extracts ranking residuals \\(\hat{\epsilon}_{q,m}^y = r(y \mid \pi_q) - \hat{m}(\mathbf{x}_q^y)\\), representing unobserved factors (e.g., system noise, unobserved biases, or randomization) [19–20]. \\(m(\cdot)\\) can be any lightweight model (e.g., Ridge regression, Logistic Regression, SVM, or XGBoost) [8-10].
* **Stage 2 (Click Model Correction via Control Functions):**
  * Following Lewbel's identification framework, constructs control function interaction terms \\(\Phi(\mathbf{x}_q^y, T(\hat{\epsilon}_{q,m}^y)) = (\mathbf{x}_q^y - \bar{\mathbf{x}}_q) \odot T(\hat{\epsilon}_{q,m}^y)\\), where \\(\bar{\mathbf{x}}_q\\) is the query-level feature mean, \\(\odot\\) denotes element-wise multiplication, and \\(T(\cdot)\\) is a residual transformation [7, 11].
  * Formulates the click model:
    \\[C_q^y = \mathbb{I}\left[ s\left( \mathbf{x}_q^y, \Phi\left(\mathbf{x}_q^y, T(\hat{\epsilon}_{q,m}^y)\right) \right) + \epsilon_{q,g}^y > 0 \right]\\]
  * **Inference Phase:** At test time for new queries, the control function terms are set to zero (\\(\Phi = 0\\)), so predictions rely strictly on the learned unbiased feature parameters: \\(\mathbb{E}[C_q^y \mid \mathbf{x}_q^y] = g(\mathbf{x}_q^y)\\) [12].
* **Residual Transformations (\\(T(\hat{\epsilon}_{q,m}^y)\\)):**
  Treats residual transformation as a validation-tuned hyperparameter across 4 variants [36–40]:
  1. *Min-Max Normalization* (\\(T_1\\)) [13].
  2. *Parametric PDF* assuming normal distribution (\\(T_2\\)) [14].
  3. *Parametric Inverse Mills Ratio (IMR) / Hazard Ratio* assuming normal distribution (\\(T_3\\)) [15].
  4. *Nonparametric Hazard Ratio* using Kernel Density Estimation (KDE / fastKDE) (\\(T_4\\)) [9, 16].
* **Debiasing Validation Clicks for Hyperparameter Tuning:**
  Fits a function \\(C_q^y = D(T(\hat{\epsilon}_{q,m}^y)) + \epsilon_{q,D}^y\\) on validation data. The residual \\(\hat{\epsilon}_{q,D}^y = C_q^y - \hat{D}(T(\hat{\epsilon}_{q,m}^y))\\) represents clicks with position effects partialed out, serving as an unbiased proxy for true relevance during hyperparameter tuning [41–43].

#### **Credit Assignment Mechanics**
* **Not specified in source / Does NOT assign per-touchpoint credit.**
* CFC is an unbiased learning-to-rank (ULTR) framework that corrects position bias in click-through logs during ranker training [1, 6–7]. It does not perform multi-touch sequence attribution or assign fractional credit across past user interaction touchpoints.

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets & Scale:**
  1. **Yahoo! Learning to Rank Challenge (Set1 / C14B):** 19,944 train / 2,994 valid / 6,983 test queries; 700-dimensional features; ~24 items/query [97–98].
  2. **MSLR-WEB10K (Fold-1):** 6,000 train / 2,000 valid / 2,000 test queries; 136-dimensional features; ~121 items/query; click density **~0.36%** [52, 97–98].
  3. **Istella-S:** 19,245 train / 7,211 valid / 6,562 test queries; 220-dimensional features; ~103 items/query; click density **~1.10%** [52, 98–99].
  4. **Baidu-ULTR (Industrial Real-World Search Engine Dataset):** 1,779,017 train queries (14,526,276 docs) / 1,727 valid / 3,455 test queries; 18-dimensional features [48, 98–99]. Collected from Baidu search engine click logs, generated by a strong production ranker with real user clicks and unbiased ground-truth relevance labels for evaluation [17-19].
  * *Semi-Synthetic Setup:* Initial ranker (RankSVM on 1% labeled data) generates initial rankings \\(\pi_q\\) [20]. Clicks generated via Position-Based Model (PBM) with observation probability \\(P(O=1) = (1/r)^\eta\\) (\\(\eta=1.0\\) default bias severity) and relevance probability \\(P(R=1) = \epsilon + (1-\epsilon)\frac{2^{\text{rel}}-1}{2^{\text{rel}_{\max}}-1}\\) (\\(\epsilon=0.0\\) default noise) over 10 training passes [45–47].
* **Production Deployment:** Evaluated on real-world industrial search click logs from **Baidu's search engine** (Baidu-ULTR dataset) [17-19].
* **Comparison Baselines:**
  * *IPW / Counterfactual Methods:* **DLA** (Dual Learning Algorithm), **REM** (Regression-based EM), **UPE** (Unconfounded Propensity Estimation), **PairD** (Pairwise Debiasing LambdaMART) [21, 22].
  * *Click Model Methods:* **PAL** (Position-bias Aware Learning 2-tower model) [21, 22].
  * *Econometric Methods:* **PIJD** (Propensity-Independent Joint Debiasing via Heckman selection) [21, 22].
  * *Doubly Robust Methods:* **MULTR** (Model-based Unbiased LTR) [21, 22].
  * *Uncorrected Baselines:* Naive **LambdaMART** (LightGBM) and **DNN** (3-layer MLP) trained directly on biased clicks [49–50, 100, 102].
  * *Upper Bound:* **Oracle** (trained directly on human-annotated ground-truth relevance labels) [21, 22].

---

### **(5) Key Quantitative Results with Numbers**

* **Public Benchmark Datasets Overall Performance (Table 1):**
  * **Yahoo (LambdaMART):** CFC **ERR@10 = 0.462\*** (vs. PIJD **0.455**, PairD **0.452**, Naive LambdaMART **0.447**; Oracle **0.474**); CFC **NDCG@10 = 0.801\*** (vs. PIJD **0.788**, PairD **0.789**, Naive **0.786**; Oracle **0.817**) [23].
  * **Yahoo (DNN):** CFC **ERR@10 = 0.456** (vs. MULTR **0.453**, REM **0.452**, DLA **0.444**, Naive DNN **0.452**); CFC **NDCG@10 = 0.794** (vs. MULTR **0.789**, REM **0.788**, DLA **0.782**, Naive **0.788**) [23].
  * **MSLR-WEB10k (LambdaMART):** CFC **ERR@10 = 0.324\*** (vs. PairD **0.285**, PIJD **0.277**, Naive **0.270**; Oracle **0.342**); CFC **NDCG@10 = 0.489\*** (vs. PairD **0.464**, PIJD **0.440**, Naive **0.457**) [23].
  * **MSLR-WEB10k (DNN):** CFC **ERR@10 = 0.306** (vs. MULTR **0.303**, REM **0.301**, DLA **0.256**); CFC **NDCG@10 = 0.467** (vs. MULTR **0.462**, REM **0.457**, DLA **0.448**) [23].
  * **Istella-S (LambdaMART):** CFC **ERR@10 = 0.717\*** (vs. PairD **0.690**, PIJD **0.681**, Naive **0.694**); CFC **NDCG@10 = 0.766\*** (vs. PairD **0.741**, PIJD **0.694**, Naive **0.740**) [23].
  * **Istella-S (DNN):** CFC **ERR@10 = 0.689** (vs. MULTR **0.689**, REM **0.681**, DLA **0.672**); CFC **NDCG@10 = 0.721** (vs. MULTR **0.715**, REM **0.710**, DLA **0.705**) [23].
* **Industrial Search Engine (Baidu-ULTR Dataset, Table 2):**
  * **LambdaMART:** CFC **ERR@10 = 0.275** (vs. PIJD **0.234**, PairD **0.234**, Naive **0.238**); CFC **NDCG@10 = 0.525** (vs. PairD **0.448**, PIJD **0.442**, Naive **0.454**) [24].
  * **DNN:** CFC **ERR@10 = 0.291** (vs. REM **0.279**, MULTR **0.262**, PIJD **0.247**, DLA **0.223**, Naive **0.213**); CFC **NDCG@10 = 0.553** (vs. REM **0.532**, MULTR **0.502**, PIJD **0.475**, DLA **0.415**, Naive **0.434**) [24].
* **Validation Tuning on Debiased Clicks (Table 3 vs. Table 13):**
  * When true relevance is unavailable, tuning on debiased validation clicks (CFC) maintains high performance: Yahoo LambdaMART **ERR@10 = 0.458 / NDCG@10 = 0.792**; MSLR **ERR@10 = 0.321 / NDCG@10 = 0.490**; Istella-S **ERR@10 = 0.715 / NDCG@10 = 0.762** [25, 26].
  * Tuning directly on raw biased clicks (CFC-BC) degrades performance: Yahoo **ERR@10 = 0.438 / NDCG@10 = 0.784**; MSLR **ERR@10 = 0.315 / NDCG@10 = 0.481**; Istella-S **ERR@10 = 0.699 / NDCG@10 = 0.754** [26].
* **Heteroskedasticity Validation & Speed:**
  * Nonparametric Fligner–Killeen (FK) test confirms statistically significant feature-dependent heteroskedasticity across all datasets (\\(p \approx 10^{-6}\text{--}10^{-5} < 0.05\\)) [27, 28].
  * Stage 1 Ridge regression model trains rapidly in **10.4s** (Yahoo), **7.4s** (MSLR), and **15.3s** (Istella-S) [10].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Incomplete Separation of Feature-Relevance and Bias Interactions:** Control function terms can interact with features during Stage 2 training [29]. Setting control function terms to zero at inference (\\(\Phi = 0\\)) may inadvertently remove a portion of learned feature-control function interactions [29].
2. **Dependence on Feature-Dependent Heteroskedasticity:** Identification relies on ranking errors exhibiting feature-dependent heteroskedasticity (\\(\text{Var}(\epsilon_m \mid X)\\) varies systematically with features) [30, 31]. If ranking errors were perfectly homoskedastic, interaction terms would fail to provide identifying exogenous variation [30, 31].
3. **Out-of-Scope Bias Types:** The validation click debiasing procedure specifically removes position bias and does not account for other distortion sources (e.g., trust bias or click noise) during hyperparameter tuning [32].
4. **DNN Baseline Parity in Isolated Settings:** On MSLR-WEB10K under DNN rankers, MULTR occasionally performs comparably or slightly better (ERR@10 = **0.303** vs. **0.306**), as MULTR is specifically optimized for DNN architectures [33, 34].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Ai et al. (2018) [Ref 2 / DLA]:** *Unbiased learning to rank with unbiased propensity estimation* (ACM SIGIR '18) [35, 36].
2. **Joachims, Swaminathan, & Schnabel (2017) [Ref 26]:** *Unbiased learning-to-rank with biased feedback* (ACM WSDM '17) [37, 38].
3. **Ovaisi, Vasilaky, & Zheleva (2020, 2021) [Refs 43, 44 / PIJD]:** *Correcting for selection bias in learning-to-rank systems* (ACM WWW '20) & *Propensity-independent bias recovery in offline learning-to-rank systems* (ACM SIGIR '21) [32, 39, 40].
4. **Lewbel (2012) [Ref 31]:** *Using heteroscedasticity to identify and estimate mismeasured and endogenous regressor models* (Journal of Business & Economic Statistics '12) — Identifies control functions from heteroskedasticity [41, 42].
5. **Wooldridge (2010, 2015) [Refs 58, 59]:** *Econometric Analysis of Cross Section and Panel Data* & *Control function methods in applied econometrics* (Journal of Human Resources '15) — Econometric foundations of control functions [24, 43, 44].
6. **Luo et al. (2023, 2024) [Refs 33, 34 / UPE, MULTR]:** *Model-based unbiased learning to rank* (ACM WSDM '23) & *Unbiased Learning-to-Rank Needs Unconfounded Propensity Estimation* (ACM SIGIR '24) [12, 45-47].
7. **Guo et al. (2019) [Ref 18 / PAL]:** *PAL: a position-bias aware learning framework for CTR prediction in live recommender systems* (ACM RecSys '19) [48, 49].

---

💡 *Would you like to explore how CFC's control function framework or validation click debiasing method could be applied to correct position bias in offline click/swipe logs for your dating app's candidate profile ranker?*

---

## 2. Evidence

See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

## 3. Limitations

See limitations in §1 if present. Replace any NLM refusal with: Not specified in source.

---

## 4. Prior works named

See cited prior works in §1.

---

## 5. Project Relevance

### **Part 1: Detailed Technical Breakdown of *ControlFunction_2506.06989.pdf***

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *A Control Function Framework for Mitigating Position Bias in Learning to Rank Systems* [1]
* **Authors:** **Md Aminul Islam**¹, **Kathryn Vasilaky**², and **Elena Zheleva**¹ [1]
* **Affiliations:** ¹**University of Illinois Chicago** (Chicago, IL, USA); ²**California Polytechnic State University** (San Luis Obispo, CA, USA) [1]
* **Year & Venue:** Published in **2026** at the *20th ACM Conference on Recommender Systems (RecSys ’26)*, September 27–October 02, 2026, Minneapolis, MN, USA [2]

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Learning-to-rank (LTR) systems rely on implicit user feedback (e.g., clicks), which is heavily skewed by position bias—higher-ranked items receive disproportionately more interactions regardless of actual relevance [1, 3]. Existing position bias correction approaches face major operational trade-offs [4]:
  1. *Click models* require repeated query–item observations, failing on sparse tail queries [4].
  2. *Propensity-based (IPW) methods* rely on intrusive result randomization (degrading user experience) or joint optimization (vulnerable to model misspecification) and require modifying the ranker's loss objective [4, 5].
  3. *Econometric methods (Heckman selection models)* assume linear outcome equations, failing to handle high-dimensional feature interactions or sparse clicks [4, 5].
  4. *Validation Gap:* Standard models assume access to unbiased validation data or tune hyperparameters directly on biased clicks, leading to suboptimal model selection [6].
* **Key Contribution:**
  1. **Control Function-based Correction (CFC):** A novel two-stage econometrics-inspired framework that corrects position bias without explicit propensity estimation, result randomization, or modifying the ranker's loss objective [1, 6–7].
  2. **Stage 1 (Residualization):** Models the historical ranking process using observable features to isolate exogenous ranking residuals (\\(\hat{\epsilon}_{q,m}^y\\)) capturing feature-unexplained ranking variation [6, 18–20].
  3. **Stage 2 (Click Modeling with Control Functions):** Incorporates residual transformations and feature interaction terms (leveraging Lewbel's identification theory for feature-dependent heteroskedasticity) as control functions in the click model [6, 24–27].
  4. **Algorithm & Objective Agnostic:** Compatible with any linear or nonlinear, pointwise, pairwise, or listwise LTR algorithm (e.g., LambdaMART, Deep Neural Networks) under both weak and strong logging policies [7–8, 31–32].
  5. **Validation Click Debiasing Strategy:** Introduces a procedure to partial out position effects from validation clicks, enabling reliable hyperparameter tuning when ground-truth relevance labels are unavailable [8, 40–43].

---

#### **(3) Proposed Method or Architecture in Detail**

##### **Architectural Components**
* **Stage 1 (Ranking Residualization):**
  * Models historical item position \\(r(y \mid \pi_q) = m(\mathbf{x}_q^y) + \epsilon_{q,m}^y\\), where \\(m(\mathbf{x}_q^y)\\) captures feature-driven rank predictable from query–item features \\(\mathbf{x}_q^y\\) [19–20].
  * Extracts ranking residuals \\(\hat{\epsilon}_{q,m}^y = r(y \mid \pi_q) - \hat{m}(\mathbf{x}_q^y)\\), representing unobserved factors (e.g., system noise, unobserved biases, or randomization) [19–20]. \\(m(\cdot)\\) can be any model (e.g., Ridge, Logistic Regression, SVM, XGBoost) [7].
* **Stage 2 (Click Model Correction via Control Functions):**
  * Following Lewbel's identification framework, constructs control function interaction terms \\(\Phi(\mathbf{x}_q^y, T(\hat{\epsilon}_{q,m}^y)) = (\mathbf{x}_q^y - \bar{\mathbf{x}}_q) \odot T(\hat{\epsilon}_{q,m}^y)\\), where \\(\bar{\mathbf{x}}_q\\) is the query-level feature mean, \\(\odot\\) denotes element-wise multiplication, and \\(T(\cdot)\\) is a residual transformation [8].
  * Formulates the click model:
    \\[C_q^y = \mathbb{I}\left[ s\left( \mathbf{x}_q^y, \Phi\left(\mathbf{x}_q^y, T(\hat{\epsilon}_{q,m}^y)\right) \right) + \epsilon_{q,g}^y > 0 \right]\\] [8, 9]
  * **Inference Phase:** At test time for new queries, the control function terms are set to zero (\\(\Phi = 0\\)), so predictions rely strictly on the learned unbiased feature parameters: \\(\mathbb{E}[C_q^y \mid \mathbf{x}_q^y] = g(\mathbf{x}_q^y)\\) [33–34].
* **Residual Transformations (\\(T(\hat{\epsilon}_{q,m}^y)\\)):**
  Treats residual transformation as a hyperparameter tuned on validation data across 4 options [36–40]:
  1. *Min-Max Normalization* (\\(T_1\\)) [36–37].
  2. *Parametric PDF* assuming normal distribution (\\(T_2\\)) [10].
  3. *Parametric Inverse Mills Ratio (IMR) / Hazard Ratio* assuming normal distribution (\\(T_3\\)) [11].
  4. *Nonparametric Hazard Ratio* using Kernel Density Estimation (KDE / fastKDE) (\\(T_4\\)) [12, 13].
* **Debiasing Validation Clicks for Hyperparameter Tuning:**
  Fits \\(C_q^y = D(T(\hat{\epsilon}_{q,m}^y)) + \epsilon_{q,D}^y\\) on validation data [41–42]. The residual \\(\hat{\epsilon}_{q,D}^y = C_q^y - \hat{D}(T(\hat{\epsilon}_{q,m}^y))\\) represents clicks with position effects partialed out, serving as an unbiased proxy for true relevance during hyperparameter tuning [42–43].

##### **Credit Assignment Mechanics**
* **Not specified in source / Does NOT assign per-touchpoint credit.** [1, 6–7]
* CFC is an unbiased learning-to-rank (ULTR) framework that corrects position bias in click-through logs during ranker training [1, 6–7]. It does not perform multi-touch sequence attribution or assign fractional credit across past user interaction touchpoints.

---

#### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets & Scale:**
  1. **Yahoo! Learning to Rank Challenge (Set1 / C14B):** 19,944 train / 2,994 valid / 6,983 test queries; 700 features; ~24 items/query [97–98].
  2. **MSLR-WEB10K (Fold-1):** 6,000 train / 2,000 valid / 2,000 test queries; 136 features; ~121 items/query; click density **~0.36%** [52, 97–98].
  3. **Istella-S:** 19,245 train / 7,211 valid / 6,562 test queries; 220 features; ~103 items/query; click density **~1.10%** [52, 98–99].
  4. **Baidu-ULTR (Industrial Real-World Search Engine Dataset):** 1,779,017 train queries (14,526,276 docs) / 1,727 valid / 3,455 test queries; 18 features [48, 98–99]. Collected from Baidu search engine click logs with real user clicks and unbiased ground-truth relevance labels for evaluation [14-16].
* **Production Deployment:** Evaluated on real-world industrial search click logs from **Baidu's search engine** (Baidu-ULTR dataset) [14, 17].
* **Comparison Baselines:**
  * *Counterfactual / IPW Methods:* **DLA** (Dual Learning Algorithm), **REM** (Regression-based EM), **UPE** (Unconfounded Propensity Estimation), **PairD** (Pairwise Debiasing LambdaMART) [18, 19].
  * *Click Model Methods:* **PAL** (Position-bias Aware Learning 2-tower model) [18, 19].
  * *Econometric Methods:* **PIJD** (Propensity-Independent Joint Debiasing via Heckman selection) [18, 19].
  * *Doubly Robust Methods:* **MULTR** (Model-based Unbiased LTR) [18, 19].
  * *Uncorrected Baselines:* Naive **LambdaMART** (LightGBM) and **DNN** (3-layer MLP) trained directly on biased clicks [49–50, 100, 102].
  * *Upper Bound:* **Oracle** (trained directly on human-annotated ground-truth relevance labels) [18, 19].

---

#### **(5) Key Quantitative Results with Numbers**

* **Public Benchmark Datasets Overall Performance (Table 1):**
  * **Yahoo (LambdaMART):** CFC **ERR@10 = 0.462\*** (vs. PIJD **0.455**, PairD **0.452**, Naive LambdaMART **0.447**; Oracle **0.474**); CFC **NDCG@10 = 0.801\*** (vs. PIJD **0.788**, PairD **0.789**, Naive **0.786**; Oracle **0.817**) [20].
  * **Yahoo (DNN):** CFC **ERR@10 = 0.456** (vs. MULTR **0.453**, REM **0.452**, DLA **0.444**, Naive DNN **0.452**); CFC **NDCG@10 = 0.794** (vs. MULTR **0.789**, REM **0.788**, DLA **0.782**, Naive **0.788**) [20].
  * **MSLR-WEB10k (LambdaMART):** CFC **ERR@10 = 0.324\*** (vs. PairD **0.285**, PIJD **0.277**, Naive **0.270**; Oracle **0.342**); CFC **NDCG@10 = 0.489\*** (vs. PairD **0.464**, PIJD **0.440**, Naive **0.457**) [20].
  * **MSLR-WEB10k (DNN):** CFC **ERR@10 = 0.306** (vs. MULTR **0.303**, REM **0.301**, DLA **0.256**); CFC **NDCG@10 = 0.467** (vs. MULTR **0.462**, REM **0.457**, DLA **0.448**) [20].
  * **Istella-S (LambdaMART):** CFC **ERR@10 = 0.717\*** (vs. PairD **0.690**, PIJD **0.681**, Naive **0.694**); CFC **NDCG@10 = 0.766\*** (vs. PairD **0.741**, PIJD **0.694**, Naive **0.740**) [20].
  * **Istella-S (DNN):** CFC **ERR@10 = 0.689** (vs. MULTR **0.689**, REM **0.681**, DLA **0.672**); CFC **NDCG@10 = 0.721** (vs. MULTR **0.715**, REM **0.710**, DLA **0.705**) [20].
* **Industrial Search Engine (Baidu-ULTR Dataset, Table 2):**
  * **LambdaMART:** CFC **ERR@10 = 0.275** (vs. PIJD **0.234**, PairD **0.234**, Naive **0.238**); CFC **NDCG@10 = 0.525** (vs. PairD **0.448**, PIJD **0.442**, Naive **0.454**) [21].
  * **DNN:** CFC **ERR@10 = 0.291** (vs. REM **0.279**, MULTR **0.262**, PIJD **0.247**, DLA **0.223**, Naive **0.213**); CFC **NDCG@10 = 0.553** (vs. REM **0.532**, MULTR **0.502**, PIJD **0.475**, DLA **0.415**, Naive **0.434**) [21].
* **Validation Tuning on Debiased Clicks (Table 3 vs. Table 13):**
  * When true relevance is unavailable, tuning on debiased validation clicks (CFC) maintains high performance: Yahoo LambdaMART **ERR@10 = 0.458 / NDCG@10 = 0.792**; MSLR **ERR@10 = 0.321 / NDCG@10 = 0.490**; Istella-S **ERR@10 = 0.715 / NDCG@10 = 0.762** [22].
  * Tuning directly on raw biased clicks (CFC-BC) degrades performance: Yahoo **ERR@10 = 0.438 / NDCG@10 = 0.784**; MSLR **ERR@10 = 0.315 / NDCG@10 = 0.481**; Istella-S **ERR@10 = 0.699 / NDCG@10 = 0.754** [23].
* **Heteroskedasticity Validation & Speed:**
  * Nonparametric Fligner–Killeen (FK) test confirms statistically significant feature-dependent heteroskedasticity across all datasets (\\(p \approx 10^{-6}\text{--}10^{-5} < 0.05\\)) [24].
  * Stage 1 Ridge regression model trains rapidly in **10.4s** (Yahoo), **7.4s** (MSLR), and **15.3s** (Istella-S) [7].

---

#### **(6) Limitations, Failure Modes, or Negative Results**
1. **Incomplete Separation of Feature-Relevance and Bias Interactions:** Control function terms can interact with features during Stage 2 training [25]. Setting control function terms to zero at inference (\\(\Phi = 0\\)) may inadvertently remove a portion of learned feature-control function interactions [25].
2. **Dependence on Feature-Dependent Heteroskedasticity:** Identification relies on ranking errors exhibiting feature-dependent heteroskedasticity (\\(\text{Var}(\epsilon_m \mid X)\\) varies systematically with features) [26, 27]. If ranking errors were perfectly homoskedastic, interaction terms would fail to provide identifying exogenous variation [28, 29].
3. **Out-of-Scope Bias Types:** The validation click debiasing procedure specifically removes position bias and does not account for other distortion sources (e.g., trust bias or click noise) during hyperparameter tuning [25, 30].
4. **DNN Baseline Parity in Isolated Settings:** On MSLR-WEB10K under DNN rankers, MULTR occasionally performs comparably or slightly better (ERR@10 = **0.303** vs. **0.306**), as MULTR is specifically optimized for DNN architectures [20, 31, 32].

---

#### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Ai et al. (2018) [Ref 2 / DLA]:** *Unbiased learning to rank with unbiased propensity estimation* (ACM SIGIR '18) [2, 33].
2. **Joachims, Swaminathan, & Schnabel (2017) [Ref 26]:** *Unbiased learning-to-rank with biased feedback* (ACM WSDM '17) [28, 34].
3. **Ovaisi, Vasilaky, & Zheleva (2020, 2021) [Refs 43, 44 / PIJD]:** *Correcting for selection bias in learning-to-rank systems* (ACM WWW '20) & *Propensity-independent bias recovery in offline learning-to-rank systems* (ACM SIGIR '21) [30, 35, 36].
4. **Lewbel (2012) [Ref 31]:** *Using heteroscedasticity to identify and estimate mismeasured and endogenous regressor models* (Journal of Business & Economic Statistics '12) — Identifies control functions from heteroskedasticity [26, 28, 37, 38].
5. **Wooldridge (2010, 2015) [Refs 58, 59]:** *Econometric Analysis of Cross Section and Panel Data* & *Control function methods in applied econometrics* (Journal of Human Resources '15) — Econometric foundations of control functions [21, 39-43].
6. **Luo et al. (2023, 2024) [Refs 33, 34 / UPE, MULTR]:** *Model-based unbiased learning to rank* (ACM WSDM '23) & *Unbiased Learning-to-Rank Needs Unconfounded Propensity Estimation* (ACM SIGIR '24) [4, 6, 44-47].
7. **Guo et al. (2019) [Ref 18 / PAL]:** *PAL: a position-bias aware learning framework for CTR prediction in live recommender systems* (ACM RecSys '19) [48-51].

---

### **Part 2: Dating App Retention Attribution Project Evaluation**

#### **(A) Q1 or Q2 or Both or Neither?**
**Neither.**
* **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** While published in RecSys 2026 (`RecSys ’26`), CFC is an **unbiased learning-to-rank (ULTR) position-bias correction framework for click logs**, not an industry multi-touch attribution (MTA) measurement system [1, 2, 6–7].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** CFC corrects position-dependent display distortions in logged click data to learn unbiased item relevance scores for ranking, rather than attributing overall user retention or active days back to individual past interaction touchpoints across historical user logs [1, 3, 14–17].

---

#### **(B) Q2 Class**
**NOT.** [1, 6–7]
* **Justification:** CFC is an econometrics-inspired unbiased learning-to-rank position-bias correction framework [1, 50, 52]. It does **not** produce or publish a per-exposure retention credit table.

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction sequence attribution credit table.** [1, 6–7]
* **Target Outcome:** **Unbiased Click Probability / Ranking Relevance Score Prediction** (\\(\text{Pr}(C_q^y = 1 \mid \mathbf{x}_q^y) = g(\mathbf{x}_q^y)\\)) evaluated via Expected Reciprocal Rank (ERR@10) and Normalized Discounted Cumulative Gain (NDCG@10) [14, 33–34, 49].

---

#### **(D) How This Replaces or Improves Last-Touch N7 → Latest Swipes**
* **How it Improves/Informs Strategy:** CFC is not a post-hoc attribution model, but it provides two critical capabilities for **training and validating candidate profile rankers on logged swipe/click data**:
  1. *Unbiased Profile Ranker Training:* Users swipe far more frequently on top-positioned profile cards regardless of true match potential [3, 53]. Standard ranker training directly on swipe logs overestimates top-ranked profiles. CFC uses Stage 1 ranking residuals \\(\hat{\epsilon}\\) and control function interaction terms \\(\Phi = (\mathbf{x} - \bar{\mathbf{x}}) \odot T(\hat{\epsilon})\\) to absorb position bias without requiring intrusive result randomization or explicit propensity estimation [6–7, 27].
  2. *Debiasing Validation Swipes for Hyperparameter Tuning:* Partialing out position effects from validation swipes (\\(\hat{\epsilon}_{q,D}^y = C_q^y - \hat{D}(T(\hat{\epsilon}_{q,m}^y))\\)) enables reliable profile ranker hyperparameter selection when ground-truth match/retention labels are unavailable on validation sets [8, 41–43].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  * *Query (\\(\mathbf{x}_q\\)):* Active user searching/swiping session context and user preference features [40].
  * *Candidate Profiles (\\(y\\)):* Candidate profile cards displayed in the recommendation feed [53, 54].
  * *Clicks/Swipes (\\(C_q^y\\)):* Observed profile swipe-right / "like" actions [13–14].
  * *Position Bias (\\(r(y \mid \pi_q)\\)):* The screen display position of the candidate profile card in the user's feed [53, 54].

---

#### **(E) Selection-Bias & Confounding Handling**
1. **Position Bias & Policy-Induced Endogeneity Handling:**
   * *Stage 1 Residualization:* Isolates exogenous ranking variation \\(\hat{\epsilon}_{q,m}^y = r(y \mid \pi_q) - \hat{m}(\mathbf{x}_q^y)\\) not predictable from observable features [19–20].
   * *Stage 2 Control Functions:* Constructs feature interaction terms \\((\mathbf{x}_q^y - \bar{\mathbf{x}}_q) \odot T(\hat{\epsilon}_{q,m}^y)\\) leveraging feature-dependent heteroskedasticity (Lewbel's identification method) to absorb position-dependent endogeneity without conditioning directly on rank [24–27].
2. **Validation Click Debiasing:** Fits \\(C = D(T(\hat{\epsilon})) + \epsilon_D\\) on validation data to remove position-induced effects from validation clicks, preventing distribution shift during hyperparameter selection [41–43, 131].

---

#### **(F) Deployed or Production Dataset Evidence**
* **Production Dataset Evidence:** Evaluated on real-world industrial search click logs from **Baidu's search engine** (Baidu-ULTR dataset, containing **1,779,017 training queries** and **14,526,276 items**) [14, 16, 17].
* **Quoted Numbers from Source:**
  * **Public Benchmark Overall Performance (Table 1):**
    * *Yahoo (LambdaMART):* CFC **ERR@10 = 0.462\*** (vs. PIJD **0.455**, PairD **0.452**, Naive **0.447**; Oracle **0.474**); CFC **NDCG@10 = 0.801\*** (vs. PIJD **0.788**, PairD **0.789**, Naive **0.786**; Oracle **0.817**) [20].
    * *Yahoo (DNN):* CFC **ERR@10 = 0.456** (vs. MULTR **0.453**, REM **0.452**, DLA **0.444**, Naive **0.452**); CFC **NDCG@10 = 0.794** (vs. MULTR **0.789**, REM **0.788**, DLA **0.782**, Naive **0.788**) [20].
    * *MSLR-WEB10k (LambdaMART):* CFC **ERR@10 = 0.324\*** (vs. PairD **0.285**, PIJD **0.277**, Naive **0.270**; Oracle **0.342**); CFC **NDCG@10 = 0.489\*** (vs. PairD **0.464**, PIJD **0.440**, Naive **0.457**) [20].
    * *MSLR-WEB10k (DNN):* CFC **ERR@10 = 0.306** (vs. MULTR **0.303**, REM **0.301**, DLA **0.256**); CFC **NDCG@10 = 0.467** (vs. MULTR **0.462**, REM **0.457**, DLA **0.448**) [20].
    * *Istella-S (LambdaMART):* CFC **ERR@10 = 0.717\*** (vs. PairD **0.690**, PIJD **0.681**, Naive **0.694**); CFC **NDCG@10 = 0.766\*** (vs. PairD **0.741**, PIJD **0.694**, Naive **0.740**) [20].
    * *Istella-S (DNN):* CFC **ERR@10 = 0.689** (vs. MULTR **0.689**, REM **0.681**, DLA **0.672**); CFC **NDCG@10 = 0.721** (vs. MULTR **0.715**, REM **0.710**, DLA **0.705**) [20].
  * **Industrial Search Engine Baidu-ULTR Performance (Table 2):**
    * *LambdaMART:* CFC **ERR@10 = 0.275** (vs. PIJD **0.234**, PairD **0.234**, Naive **0.238**); CFC **NDCG@10 = 0.525** (vs. PairD **0.448**, PIJD **0.442**, Naive **0.454**) [21].
    * *DNN:* CFC **ERR@10 = 0.291** (vs. REM **0.279**, MULTR **0.262**, PIJD **0.247**, DLA **0.223**, Naive **0.213**); CFC **NDCG@10 = 0.553** (vs. REM **0.532**, MULTR **0.502**, PIJD **0.475**, DLA **0.415**, Naive **0.434**) [21].
  * **Validation Tuning on Debiased Clicks (Table 3 vs. Table 13):**
    * *CFC (Debiased Validation):* Yahoo LambdaMART **ERR@10 = 0.458 / NDCG@10 = 0.792**; MSLR **ERR@10 = 0.321 / NDCG@10 = 0.490**; Istella-S **ERR@10 = 0.715 / NDCG@10 = 0.762** [22].
    * *CFC-BC (Biased Validation):* Yahoo LambdaMART **ERR@10 = 0.438 / NDCG@10 = 0.784**; MSLR **ERR@10 = 0.315 / NDCG@10 = 0.481**; Istella-S **ERR@10 = 0.699 / NDCG@10 = 0.754** [23].
  * **Residual Model Computation Speed:** Stage 1 Ridge regression model trains rapidly in **10.4s** (Yahoo), **7.4s** (MSLR), and **15.3s** (Istella-S) [7].

---

💡 *Would you like to explore how CFC's control function framework or validation click debiasing procedure could be applied to correct position bias in offline swipe logs for your dating app's candidate profile ranker?*

---

## 6. Community Reaction

No significant community discussion searched at card-write time; extraction is NLM-scoped.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**PDF:** ingested via NotebookLM  
**Relevance:** Core if Q2 class is TRUE or PARTIAL or Q1 industry system; else Related  
**Priority:** see queue.md `G33`
