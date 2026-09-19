# Card summaries 11/12 — Summary and Evidence sections of all cards (generated)

### Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning [1, 2]
`2026_arXiv_DownstreamRewards_Long-Term-Engagement-Optimization.md`
**Source:** https://arxiv.org/html/2607.14192  

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**

* **Title:** *Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning* [1, 2]
* **Authors:** **Dingsu Wang**, **Filip Ryzner**, **Kelly He**, **Armando Ordorica**, **David Woo**\* (*Corresponding author*), **Aditya Mantha**, **Liyao Lu**, **Usha Amrutha Nookala**, **Haoran Guo**, **Jiacong He**, **Olafur Gudmundsson**, **Matt Chun**, **Krystal Benitez**, **Haibin Xie**, **Alekhya Pyla**, **Sameer Jain**, **Zhongjian Jiang**, **Shruthi Hariharan**, **Dhruvil Deven Badani**, and **Yijie Dylan Wang** (*All authors contributed equally*) [2].
* **Affiliation:** **Pinterest**, San Francisco, CA, USA [2].
* **Year & Venue:** Published in **August 2026** as an arXiv pre-print (`arXiv:2607.14192v3 [cs.LG]`, 21 Aug 2026) [2].

---

### **(2) Core Problem and Key Contribution**

* **Core Problem:** Optimizing long-term user retention in industrial recommender systems is notoriously difficult because revisitation labels are sparse, delayed, and difficult to attribute to individual recommendations [3, 4]. Direct Reinforcement Learning (RL) and long-horizon policy optimization methods suffer from massive action spaces, heavy interaction data requirements, data distribution shifts, and an inability to transfer reward designs cleanly across heterogeneous product surfaces (e.g., Homefeed, Search, Related Pins/P2P, Notifications) [3, 5].
* **Key Contributions:**
  1. **Offline Screening Framework:** Introduces a screening framework that evaluates hundreds of candidate session-level signals against three criteria—correlation with future retention, observability within the session, and incremental predictive power in multivariate models—narrowing hundreds of candidates down to a high-value subset [4, 6].
  2. **Model-Agnostic Downstream Reward (DR) Framework:** Proposes a unified downstream reward framework capturing three complementary aspects of user experience:
     * *Deeper Session Engagement:* Modeling Pin-to-Pin (P2P) "rabbit hole" exploration, saves, and closeups [3, 7].
     * *Negative Rewards:* Explicitly penalizing shallow closeups (\\(< 1\text{s}\\)) that lead to immediate session abandonment [7, 8].
     * *Use-Case Adoption:* Rewarding engagement with novel content outside a user's established interest clusters to expand user intent [7, 9].
  3. **Scalable DRv2 Infrastructure:** Builds a Ray-based dataloader infrastructure storing reusable daily event sequences, reducing idea-to-experiment iteration time **10× (from ~3 weeks to ~2 days)** with \\(<5\%\\) training step overhead [10, 11].
  4. **Multi-Surface Industrial Validation:** Validates the framework via extensive online A/B testing across Pinterest's Homefeed, Related Pins, Search, and Notifications, demonstrating statistically significant gains in user engagement and retention [3, 6, 12].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Mathematical Formulation & Reward Definitions**
* **Trajectory & Objective Formulation:** User interaction trajectories \\(\tau \sim (\pi_\theta, P_u)\\) are optimized to maximize discounted long-term rewards \\(\mathcal{J}_u(\theta) = \mathbb{E}\left[\sum_{t=0}^T \gamma^t \mathcal{R}_{u,t}(\mathbf{H}_{u,t}, x_{u,t})\right]\\) [13].
* **Proxy Downstream Reward Equation:**
  * *Entry Model (\\(p_\beta^{\text{enter}}\\)):* Estimates probability \\(\mathcal{E} \in \{0, 1\}\\) that candidate Pin \\(x_{u,t}\\) triggers a closeup and enters a P2P rabbit hole [14, 15].
  * *Downstream Trajectory Model (\\(p_\phi\\)):* Predicts the subsequent action sequence \\(\mathbf{S}_{u,t} = ((x_{u,t}, \text{closeup}), (x_{u,t+i}, A_{u,t+i}), \dots)\\) [14].
  * *Downstream Reward Estimation:*
    \\[\hat{\mathcal{R}}_{u,t}(\mathbf{H}_{u,t}, x_{u,t}) = \mathbb{E}_{\mathcal{E} \sim p_\beta^{\text{enter}}}\Big[\mathbb{E}_{\hat{\mathbf{S}} \sim p_\phi}\big[\mathbb{R}(\hat{\mathbf{S}})\big]\Big] \quad \text{where} \quad \mathbb{R}(\hat{\mathbf{S}}) = \sum_{i=1}^n r(\hat{A}_{u,t+i}) \quad [16].\\]
* **Three Complementary Reward Families:**
  1. *Deeper Session Engagement:* Rewards downstream actions inside P2P rabbit holes (closeups, saves, clicks, downloads) [3, 16].
  2. *Negative Rewards:* Penalizes shallow closeups (\\(< 1\text{s}\\) duration with zero downstream action) using negative utility weights, offsetting high-volume low-intent clicks [8, 17].
  3. *Use-Case Adoption Reward (\\(\mathbb{R}_{u,x}^{\text{UCA}}\\)):* Assigns a binary reward of \\(1\\) when an engaged item belongs to a new interest cluster (cosine similarity threshold \\(\tau = 0.6\\) against the user's historical interest vector), encouraging intent expansion [9, 18].
* **Serving & Score Combination:** Candidate items \\(x\\) are scored via linear combination \\(s(x) = \sum_{i=1}^N w_i p_i(x)\\), where serving weights \\(\{w_i\}\\) are tuned out-of-graph using **HyperOPT** to maintain immediate engagement neutrality while maximizing retention metrics [17].

#### **Credit Assignment Mechanics**
* The framework does **not** compute a formal causal multi-touch attribution (MTA) credit decomposition table across historical interactions [3, 19].
* Instead, credit is assigned to individual source items \\(x_{u,t}\\) at candidate ranking time by predicting expected downstream near-term trajectory rewards \\(\hat{\mathcal{R}}_{u,t}\\) (e.g., probability of initiating a deep P2P session, triggering a shallow closeup, or expanding into a new use case) [3, 15, 16].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets & Scale:** Internal Pinterest production logs covering billions of user activity events [3, 20].
  * *Offline Screening Dataset:* Centered on pivot days (\\(t=0\\)), analyzing low-engagement users (\\(D_u(-2) \le 1\\) and \\(D_u(-1) \le 1\\) active days/week) and predicting transitions to sustained higher engagement (\\(D_u(+1) \ge 3\\) and \\(D_u(+2) \ge 3\\), representing a **~4% transition rate**) [21]. Expanded **174 base features** into **~1,000 crossed candidates** [22].
  * *Session-Level Markov Analysis:* Built an empirical Markov transition matrix over surface-action states on live traffic to calculate expected downstream feedviews [23].
* **Production Deployment:** Fully deployed in live production at **Pinterest** across Homefeed, Related Pins (P2P), Search, and Notifications [3, 12, 24]. Homefeed A/B tests ran on **1.5% of total traffic for 3–4 weeks** [20].
* **Comparison Baselines:**
  * Multi-task production recommendation rankers (**TransAct / Pinnability**) trained solely on immediate engagement actions (clicks, closeups, saves) without downstream reward heads [3, 12, 20].
  * Offline feature normalization baselines: **Percentile Normalization (Pctl)** vs. **User-Prevalence Normalization (UP)** [22, 25].

---

### **(5) Key Quantitative Results with Numbers**

* **Markov Session Length Analysis (Table 2):**
  * *Homefeed Save + Closeup:* **7.80 expected feedviews** (vs. Homefeed entry alone: **4.45**) [23, 26].
  * *Related Pins (RP) Save + Closeup:* **7.45 expected feedviews** (vs. Related Pins alone: **4.39**) [23, 26].
  * *Homefeed Closeup alone:* **7.36 expected feedviews** [23, 26].
  * *Search Save + Closeup:* **7.26 expected feedviews** (vs. Search alone: **3.60**) [23, 26].
* **Live Production A/B Testing on Homefeed (Table 3):**
  * *Deeper Session Rewards:* **Successful Sessions (SS)** increased by **+0.24%** (Core Users) and **+0.48%** (Non-Core Users); **Total Time Spent** increased by **+0.09%** (Core) and **+0.10%** (Non-Core) [27].
  * *Negative Rewards (Segmented Thresholds \\(\delta_{\text{core}}=1\text{s}, \delta_{\text{non-core}}=0.5\text{s}\\)):* **Successful Sessions** **+0.16%** (Core/Non-Core); **Unsuccessful Sessions** **-0.40%**; **Total Time Spent** **+0.46%** (Core) and **+0.24%** (Non-Core) [overall platform time spent **+0.35%**] [27, 28]. Homefeed time spent **+0.2%**, Related Pins time spent **+0.5%** [28].
  * *Use-Case Adoption Rewards (\\(\tau = 0.6\\)):* **Successful Sessions** **+0.10%** (Core/Non-Core); **Total Time Spent** **+0.16%** (Core) and **+0.11%** (Non-Core) [18, 27].
* **Multi-Surface Scaling Lifts (Table 4):**
  * *Search:* **Search Fulfillment Rate +0.25%** [12].
  * *Related Pins (P2P):* **Successful Sessions +0.15%**, accompanied by sustained **WAU gains** [12].
  * *Notifications:* **Successful Sessions +0.14%**, **WAU +0.11%** [12].
* **Infrastructure Efficiency (DRv2 vs DRv1):**
  * Reduced idea-to-experiment iteration time **10× (from ~3 weeks to ~2 days)** [11].
  * Kept incremental training step overhead within **<5%** [11].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Initial Single-Threshold Failure for Negative Rewards:** Launching a uniform shallow closeup threshold (\\(\delta = 1\text{s}\\)) across all users caused negative retention trends for non-core users due to activity heterogeneity and cross-surface cannibalization [29]. The authors had to segment thresholds by user state (\\(\delta_{\text{core}} = 1\text{s}, \delta_{\text{non-core}} = 0.5\text{s}\\)) to restore positive retention [28].
2. **Divergence of Shallow vs. Deep Diversity Signals:** Raw univariate activity counts (e.g., shallow diverse engagement, pin clicks, surface diversity) appeared positive under percentile normalization but flipped to negative under User-Prevalence (UP) exposure normalization, proving that high-volume shallow browsing is misleading and negatively associated with long-term retention [25].
3. **Absence of Public Benchmark Evaluation:** The authors explicitly note that they could not evaluate downstream rewards on public datasets because public benchmarks lack the rich downstream action sequences (P2P trajectories, closeups, saves) required to construct the reward labels [20].
4. **Heuristic Out-of-Graph Weight Tuning:** Serving weights \\(w_i\\) must be tuned outside the ranker using HyperOPT to enforce immediate engagement neutrality, rather than being learned end-to-end within model training [17].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Xia et al. (2023) [Ref 47 / TransAct]:** *TransAct: Transformer-based realtime user action model for recommendation at pinterest* (KDD '23) [3, 20, 29, 30].
2. **Wang et al. (2022) [Ref 44 / Google Surrogate]:** *Surrogate for long-term user experience in recommender systems* (KDD '22) [5, 19, 31, 32].
3. **Cai et al. (2023) / Xue et al. (2023, 2025) [Refs 6, 49, 50 / RL Retention]:** *Reinforcing User Retention in a Billion Scale Short Video Recommender System* (WWW '23) & *AURO: Reinforcement learning for adaptive user retention optimization* (WWW '25) [5, 19, 30].
4. **Liu et al. (2024) [Ref 31 / DT4IER]:** *Sequential recommendation for optimizing both immediate feedback and long-term retention* (SIGIR '24) [17, 19, 32].
5. **Tang et al. (2023) [Ref 38 / Netflix Reward Innovation]:** *Reward innovation for long-term member satisfaction* (RecSys '23) [31, 32].
6. **Guo et al. (2017) / Cheng et al. (2016) / Wang et al. (2017, 2021) [Refs 13, 23, 42, 43 / Deep Ranking]:** *DeepFM*, *Wide & Deep*, *DCN*, & *DCNv2* [32-34].
7. **Wu et al. (2017) [Ref 46]:** *Returning is believing: Optimizing long-term user engagement in recommender systems* (CIKM '17) [19, 30].

---

💡 *Would you like to explore how Pinterest's P2P rabbit hole trajectory modeling or use-case adoption rewards (\\(\mathbb{R}^{\text{UCA}}\\)) could be adapted to evaluate deep messaging engagement and profile exploration for your dating platform's ranker?*

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM [1]
`2026_arXiv_IMA_Integrated-Marketing-Attribution.md`
**Source:** https://arxiv.org/pdf/2606.16878.pdf  

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM* [1]
* **Authors:** Meghana R. Bhat, Ankit Umare, Utsav Aggarwal, Richard Vecsler, Arunkumar Mani, Karthik Nair, and Chandhu Nair [1]
* **Affiliations:** Lowe’s Companies, Inc. [1]
* **Year:** 2026 (arXiv e-print: `2606.16878`) [1]
* **Venue:** Not specified in source (arXiv pre-print) [1]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** The tension between privacy/robustness and granularity in retail marketing measurement [1, 2]. Traditional Multi-Touch Attribution (MTA) relies on deterministic user-level tracking and third-party cookies, which are failing due to privacy restrictions and signal loss [3, 4]. Conversely, Marketing Mix Modeling (MMM) is privacy-safe and robust at the channel level, but too coarse for short-term campaign-level optimization because estimating MMM at the campaign level causes severe overfitting, multicollinearity, and parameter instability [5-7].
* **Key Contributions:**
  1. **Integrated Marketing Attribution (IMA) Framework:** A unified, privacy-safe three-stage attribution architecture that decomposes weekly channel-level incremental sales contributions from MMM down to daily, campaign-level effects using aggregated media data without user-level tracking [1, 6, 8].
  2. **Channel-Specific Bayesian Prior Anchoring:** A Bayesian regression methodology per channel that uses channel-level MMM effectiveness coefficients as informative priors to regularize campaign-level estimates and overcome high dimensionality and multicollinearity [6, 9-11].
  3. **Enterprise Retail Validation:** Demonstrates a concrete, operational methodology validated on three years of real-world retail marketing data across Search, Social, and Display channels [4, 12, 13].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Architectural Pipeline (Three Stages)**
1. **Stage 1: MMM Estimation:** Fits a weekly Bayesian MMM using aggregated weekly sales, pricing/promotions, macroeconomic variables, and weekly channel-level media series [14]. Outputs weekly channel incremental sales contributions along with channel-level adstock parameters (\\(L, P, D\\)) and effectiveness coefficients \\(\beta_c\\) [10, 14].
2. **Stage 2: Temporal Disaggregation:** Temporally disaggregates weekly channel incremental sales into daily resolution using daily media data transformed by MMM adstock parameters (converted from weekly to daily scale), preserving learned media carryover dynamics [14-16].
3. **Stage 3: Channel-Specific Attribution Modeling:** Fits independent Bayesian linear regression models for each media channel \\(c\\) using PyMC and Automatic Differentiation Variational Inference (ADVI) [9, 12, 17]:
   * **Target (\\(Y\\)):** Daily channel-level incremental sales contribution (\\(y_t \sim \mathcal{N}(\mu_t, \sigma^2)\\)) [9, 10, 17].
   * **Inputs (\\(X\\)):** Adstock-transformed daily campaign-level media inputs (\\(x^*_{j,t}\\), e.g., adstocked impressions, spend, or clicks) [9, 17].
   * **Priors & Constraints:** 
     \\[\beta_j \sim \text{TruncatedNormal}(\beta_c, \sigma_\beta; \text{lower} = 0)\\]
     \\[\alpha \sim \text{TruncatedNormal}(\alpha_c, \sigma_\alpha; \text{lower} = 0)\\]
     \\[\sigma \sim \text{HalfNormal}(10)\\]
     where \\(\beta_c\\) and \\(\alpha_c\\) are the aggregate channel-level effectiveness coefficient and offset derived from MMM [10].

#### **Credit Assignment Mechanics**
* Credit is assigned **per daily campaign-level media input** within a channel (e.g., adstocked campaign spend or impressions), **not** to individual user touchpoints, user interactions, or swipes [8, 9, 17]. 
* It mathematically decomposes aggregate channel-level sales incrementality across daily campaigns via Bayesian shrinkage anchored to MMM priors, guaranteeing that campaign allocations sum up to channel incremental totals without relying on user journeys [6, 9, 18].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets:** Three years of historical daily marketing data across digital media channels at Lowe's Companies, Inc. (exact dates, channel names, and absolute revenue amounts are withheld for confidentiality) [9, 12].
* **Production Deployment:** Applied operationally at Lowe's Companies, Inc. to guide tactical optimization across thousands of concurrent digital advertising campaigns without third-party cookies [13, 19].
* **Comparison Baselines:** Benchmarked against the primary weekly channel-level MMM model target outputs (evaluating whether daily campaign attribution aggregated to weekly resolution accurately reconstructs weekly MMM channel-level incremental sales) [9, 11, 12].

---

### **(5) Key Quantitative Results with Numbers**
* **Channel-Level Reconstruction Fit (\\(R^2\\)):** Aggregated weekly campaign-level predictions track weekly MMM incremental channel sales contributions with an **\\(R^2\\) of 0.98** for a representative channel [11].
* **Weekly Mean Absolute Percentage Error (MAPE) by Channel:**
  * **Search:** **4.10%** [20]
  * **Social:** **5.97%** [20]
  * **Display:** **3.25%** [20]
* Aggregate error remains sub-6% weekly MAPE across major digital channels, representing only slight degradation compared to the primary weekly MMM baseline (~2% MAPE) while supplying campaign-level resolution [13, 20, 21].

---

### **(6) Limitations, Failure Modes, or Negative Results**
1. **Higher Error than Primary MMM:** Weekly MAPE is 3–6% vs. ~2% for primary MMM because IMA operates on secondary incremental sales target contributions that have lower signal-to-noise ratios and higher volatility than total raw sales [20, 21].
2. **Severe Campaign-Level Multicollinearity:** Unregularized campaign regression fails due to visible block correlations and overlapping campaign flighting patterns (resulting in inflated variance, sign reversals, and unstable parameters if run without Bayesian priors) [7, 11].
3. **Lack of Cross-Channel Interaction Modeling:** IMA operates independently per channel without cross-channel interaction terms or cross-channel smoothing [21, 22].
4. **Omission of Geo Heterogeneity & Dynamic Priors:** The core model uses static channel priors rather than rolling sequential Bayesian updates or hierarchical geo-level pooling (noted as future work) [22].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Jin et al. (2017):** *Bayesian methods for media mix modeling with carryover and shape effects* (Google Research) [15, 23, 24]
2. **Google (2022):** *Unified marketing measurement: The power of blending methodologies* (Think with Google) [23, 25]
3. **Gordon et al. (2019):** *A comparison of approaches to advertising measurement: Evidence from big field experiments at facebook* (Marketing Science) [23, 26]
4. **Churchill, Li, & Xiu (2025):** *Modeling aggregate consumer journeys in a cookie-free environment: A two-stage framework for marketing mix models* [4, 27, 28]
5. **Salvatier, Wiecki, & Fonnesbeck (2016):** *Probabilistic programming in Python using PyMC3* [10, 17, 29]
6. **Kucukelbir et al. (2017):** *Automatic Differentiation Variational Inference* (JMLR) [12, 24]
7. **Chan & Perry (2017):** *Challenges and opportunities in media mix modeling* (Google Research) [23, 28]

---

💡 *Would you like to explore how IMA's Bayesian prior anchoring or temporal disaggregation technique could be adapted to disaggregate user-level engagement down to campaign features for your platform?*

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

