# Relevance index 9/10 — Project Relevance sections of all cards (generated)

### DCEO: Direct Causal Effect Optimization for Long-Term User Value Modeling in E-commerce Search [1]
`2026_arXiv_DCEO_Direct-Causal-Effect-Optimization.md`
**Source:** https://arxiv.org/html/2608.25635  

### **Source Evaluation: *DCEO: Direct Causal Effect Optimization for Long-Term User Value Modeling in E-commerce Search***
*(Zhang et al., Taobao & Tmall Group of Alibaba, arXiv:2608.25635, Aug 2026)* [1]

---

### **(A) Q1 or Q2 or Both or Neither?**

**Neither.** [2, 4, 7–8]  
* **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** While published on August 26, 2026 (`arXiv:2608.25635`) and deployed in live production at Alibaba (Taobao/Tmall), DCEO is a data-driven actor-critic framework for item-level proxy score learning in multi-objective search ranking, rather than an industry multi-touch attribution (MTA) measurement system [1–2, 5–6].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper optimizes a user-level \\(n\\)-day cumulative outcome (\\(4\\)-day cumulative GMV or purchase count) for e-commerce search, rather than attributing user retention, active days, or return visits across multi-touch interaction logs [2-5].

---

### **(B) Q2 Class**

**NOT.** [2, 5–8]  
* **Justification:** DCEO is an actor-critic multi-objective fusion framework that dynamically generates context-dependent weighting parameters (\\(\mathbf{w}_{ur}\\)) over upstream predicted scores to produce item-level proxy scores [2, 5, 19–20]. It does **not** publish or output a per-exposure retention credit table or causal multi-touch attribution model [5, 7–8].

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction sequence credit.** [3, 6, 7]
* **Target Outcome:** **User-Level Long-Term Objective (\\(Y_u\\))** accumulated over an \\(n\\)-day outcome window (specifically 4-day cumulative GMV or purchase count per user) [2, 4, 5, 8].
* **Mechanics:** The actor model (\\(f_\theta\\)) predicts request-specific fusion weights (\\(\mathbf{w}_{ur}\\)) over \\(M\\) selected upstream predicted scores (\\(\mathbf{v}_{uri}\\)) to calculate item proxy scores \\(p_{uri}(\theta) = \sum_{m=1}^M w_{ur}^m v_{uri}^m\\) [19–20]. These scores are aggregated into a calibrated user-level proxy metric \\(P_u(\theta)\\) and evaluated by a critic model (\\(h_\phi\\)) under a relative intervention (\\((1+\delta)P_u\\)) to optimize Relative Causal Effect (RCE) [5, 15–17, 20–21].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**

* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% of an \\(N7\\) retention label to recent swipes post-hoc, ignoring baseline activity and failing to distinguish predictive correlation from true causal impact [3–4, 12]. DCEO replaces post-hoc last-touch attribution by learning context-dependent fusion weights (\\(\mathbf{w}_{ur}\\)) at request time that directly maximize the **relative causal effect** of candidate profile scores on long-term user retention (\\(Y_u\\)) [4–5, 15–16].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Candidate Profile Request:* Triggered when a user requests a batch/deck of candidate profiles to swipe.
  2. *Upstream Predictions (\\(\mathbf{v}_{uri}\\)):* Multiple candidate profile score heads (e.g., predicted swipe-right, predicted match, predicted 10-message conversation, predicted profile duration) [5, 9, 10].
  3. *Actor Fusion (\\(f_\theta\\)):* Predicts request-specific weights (\\(\mathbf{w}_{ur}\\)) based on user features (\\(\mathbf{z}_u\\)) and request context (\\(\mathbf{z}_{ur}\\)) to construct an item-level proxy score \\(p_{uri}\\) [19–20].
  4. *Calibrated Aggregation & Causal Critic (\\(P_u \to h_\phi\\)):* Aggregates item proxy scores across a user's swiping session, calibrates them to a reference impression count (\\(C=100\\)), and uses a critic model (\\(h_\phi\\)) to evaluate the causal effect of increasing the proxy metric on \\(n\\)-day retention (\\(Y_u\\)), prioritizing profiles that causally drive retention rather than superficial swipes [5, 14–17, 20–21].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Calibrated User-Level Aggregation (\\(g_\psi\\)):** Calibrates the daily user proxy score \\(\hat{p}_u\\) to a fixed reference impression count (\\(C=100\\)), removing impression-count bias caused by ranking-induced user activity expansion [7, 11, 12].
2. **Conditional Normalized Ranking Loss (\\(\mathcal{L}_{\text{CNR}}\\)):** Uses a normalization network \\(e_\zeta(\mathbf{z}_u)\\) to predict conditional mean and variance \\((\mu_P, \mu_Y, \sigma_P, \sigma_Y)\\) based on user baseline features \\(\mathbf{z}_u\\), normalizing proxy metrics and outcome labels before applying pairwise Bradley–Terry ranking loss [17, 23–24].
3. **Relative Causal Effect Optimization (\\(\mathcal{L}_{\text{CE}}\\)):** Evaluates outcome changes under a relative intervention \\((1+\delta)P_u(\theta)\\) vs. \\(P_u(\theta)\\) (\\(\delta = 0.05\\)), isolating incremental causal lift over baseline user expectations [5, 13, 14].

---

### **(F) Deployment and Production Dataset Evidence**

* **Production Deployment:** Fully deployed in live production on Taobao/Tmall's large-scale e-commerce search engine serving hundreds of millions of users, evaluated in a **41-day online A/B test** [2, 8, 15].
* **Offline Dataset:** Industrial search logs from Taobao/Tmall. Trained on **14 consecutive days** of search logs and evaluated on the **15th day** [5].
* **Quoted Numbers from the Source:**
  * **Online A/B Test (41-day test vs. conventional GMV proxy, Table 8):**
    * **GMV Lift:** **+0.36%** relative gain over control [2, 8, 16].
    * **Click Count Lift:** **+0.36%** relative gain over control [16].
    * **Purchase Count Lift:** **+0.12%** relative gain over control [16].
  * **Offline Relative Causal Effect (RCE, Table 3 & Section 5.3):**
    * *Predictive Association Optimization:* **RCE = 0.022** [17].
    * *Causal Effect Loss (\\(\mathcal{L}_{\text{CE}}\\) alone):* **RCE = 0.031** [17].
    * *Full DCEO (\\(\mathcal{L}_{\text{actor}} = \mathcal{L}_{\text{CE}} + \alpha \mathcal{L}_{\text{CNR}}\\)):* **RCE = 0.053** (**2.41x improvement** over predictive association optimization) [17, 18].
  * **Upstream Score Set Ablations (Table 5):**
    * `impr2gmv` only: **RCE = 0.027** [31–32].
    * Basic impression-level set: **RCE = 0.039** [31–32].
    * Conversion-funnel set: **RCE = 0.040** [31–32].
    * Value-aware set: **RCE = 0.041** [31–32].
    * Full 17-score set: **RCE = 0.053** [31–32].
  * **Objective Sensitivity Mean Actor Weights (Table 6):**
    * *4-day Click Count Objective:* `impr2click` weight = **0.999** [19, 20].
    * *4-day Purchase Count Objective:* `impr2click` = **0.531**, `click2pay` = **0.101**, `click2pay10` = **0.256** [19, 20].
    * *4-day GMV Objective:* `impr2click` = **0.404**, `click2pay` = **0.032**, `click2pay10` = **0.154**, `click2pay30` = **0.079**, `click2pay100` = **0.105**, `click2pay1000` = **0.205** [19, 20].
  * **Hyperparameters:** Reference impression count \\(C = 100\\), relative intervention \\(\delta = 0.05\\), ranking loss weight \\(\alpha = 0.3\\) [5].

---

💡 *Would you like to explore how DCEO's actor-critic relative causal effect loss (\\(\mathcal{L}_{\text{CE}}\\)) or calibrated user-level aggregation could be adapted to optimize candidate profile fusion weights for your dating app?*

---

### Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning [1, 2]
`2026_arXiv_DownstreamRewards_Long-Term-Engagement-Optimization.md`
**Source:** https://arxiv.org/html/2607.14192  

### **Source Evaluation: *Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning***  
*(Wang et al., Pinterest, arXiv pre-print: `2607.14192v3`, August 21, 2026) [1]*

---

### **(A) Q1 or Q2 or Both or Neither?**
* **Neither** [3–4, 10, 21, 32–33].
* **Explanation:**
  * **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** While published in August 2026 (`arXiv:2607.14192v3`) and deployed live across multiple surfaces at Pinterest, it presents a **model-agnostic downstream reward framework** (surrogate reward learning) for candidate recommendation models rather than an industry multi-touch attribution (MTA) measurement system [2–4, 21].
  * **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** It predicts expected near-term downstream session trajectory rewards (Pin-to-Pin rabbit hole exploration, shallow closeups, new use-case adoption) at candidate ranking time [4, 7–9], rather than attributing overall retention or active days across historical user interaction logs to individual actions [10, 32–33].

---

### **(B) Q2 Class**
* **Classification:** **NOT** [2-5].
* **Justification:** It is a surrogate reward and policy optimization framework that models expected near-term downstream trajectory rewards (\\(\hat{\mathcal{R}}_{u,t}\\)) and tunes serving weights out-of-graph via HyperOPT [7–8, 21]. It does **not** generate or publish a per-exposure retention credit table [3, 5].

---

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction sequence attribution credit table** [3, 5].
* **Target Outcome:** Predicts expected downstream session trajectory rewards \\(\hat{\mathcal{R}}_{u,t}(\mathbf{H}_{u,t}, x_{u,t}) = \mathbb{E}_{\mathcal{E}}\left[\mathbb{E}_{\hat{\mathbf{S}}}[\mathbb{R}(\hat{\mathbf{S}})]\right]\\) for candidate items \\(x_{u,t}\\) at candidate ranking time [7–9] across three complementary reward families [2, 6]:
  1. *Deeper Session Engagement:* Probability of entering a Pin-to-Pin (P2P) "rabbit hole" and generating downstream actions (saves, closeups, clicks, downloads) [4, 7–8].
  2. *Negative Rewards:* Explicitly penalizes shallow closeups (duration \\(< 1\text{s}\\) with zero downstream action) that lead to immediate session abandonment [17, 25–26].
  3. *Use-Case Adoption Rewards (\\(\mathbb{R}^{\text{UCA}}\\)):* Rewarding engagement with novel content outside a user's established interest clusters (cosine similarity threshold \\(\tau = 0.6\\)) [7, 8].

---

### **(D) Replacing Last-Touch N7 → Latest Swipes**
* **How it Improves on Last-Touch:** Last-touch post-hoc rules assign 100% of an N7 retention label to recent interactions, ignoring session depth, negative shallow interactions, and intent expansion. This paper replaces post-hoc last-touch attribution by scoring candidate recommendations at ranking time using **predictive downstream near-term session trajectories**:
  \\[s(x) = \sum_{i=1}^N w_i p_i(x)\text{}\\]
  where serving weights \\(\{w_i\}\\) are tuned out-of-graph using HyperOPT to keep immediate engagement neutral while maximizing long-term retention metrics [4].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Candidate Profile Impression (\\(x_{u,t}\\)):* Evaluates candidate profile card \\(x_{u,t}\\) for user \\(u\\) [9, 10].
  2. *Deeper Session Engagement (Rabbit Hole / Conversation Trajectory):* Predicts whether matching/swiping card \\(x\\) triggers a deeper conversation trajectory (e.g., initiating a 4-way chat, profile browsing, image saving) [4, 7–8].
  3. *Negative Reward (Shallow Swiping Penalty):* Penalizes "shallow right-swipes" or "cursory profile opens" (e.g., right-swiping or opening a profile for \\(< 1\text{s}\\) without sending a message), reducing the score of clickbait profiles that cause immediate session abandonment [17, 25–26].
  4. *Use-Case Adoption / Novelty Expansion:* Rewards matches/interactions with candidate profiles outside the user's usual demographic/interest clusters (cosine similarity \\(\tau = 0.6\\)), expanding user match preferences and preventing filter bubbles [7, 8].

---

### **(E) Selection-Bias & Confounding Handling**
1. **Offline Screening Framework & User-Prevalence (UP) Normalization:** Normalizes daily action features by comparing action density to the user's 2-week baseline:
   \\[\hat{x}_{u,0}^{(j)} = r_{u,0}^{(j)} - \tilde{r}_u^{(j)}\text{}\\]
   This controls for exposure volume and filters out shallow browsing signals (which flip from positive under percentile normalization to negative under UP normalization) [12–13].
2. **Segmented Thresholds by User State:** Addresses user heterogeneity and cross-surface cannibalization by setting separate shallow closeup thresholds for core vs. non-core users (\\(\delta_{\text{core}} = 1\text{s}, \delta_{\text{non-core}} = 0.5\text{s}\\)) [25–26].
3. **Out-of-Graph Weight Tuning via HyperOPT:** Decouples reward head weight tuning from model training, adjusting serving weights \\(w_i\\) to maintain immediate engagement neutrality while maximizing retention metrics [4].

---

### **(F) Deployment and Production Dataset Evidence**
* **Production Deployment:** Fully deployed live in production at **Pinterest** across Homefeed, Related Pins (P2P), Search, and Notifications [4–5, 28–29]. Homefeed online A/B tests ran on **1.5% of total traffic for 3–4 weeks** [11].
* **Production Datasets & Numbers Quoted from Source:**
  * **Offline Screening Dataset:** Per-user daily observations centered on pivot day \\(t=0\\) for low-engagement users (\\(D_u(-2) \le 1\\) and \\(D_u(-1) \le 1\\) active days/week), predicting transitions to sustained higher engagement (\\(D_u(+1) \ge 3\\) and \\(D_u(+2) \ge 3\\), representing a **~4% transition rate**). Expanded **174 base features** into **~1,000 crossed candidates** [11–12].
  * **Markov Session Analysis (Table 2):** Homefeed Save + Closeup yields **7.80 expected feedviews** (vs. Homefeed entry alone: **4.45**); Related Pins Save + Closeup yields **7.45 expected feedviews** (vs. Related Pins alone: **4.39**); Homefeed Closeup alone yields **7.36 expected feedviews**; Search Save + Closeup yields **7.26 expected feedviews** (vs. Search alone: **3.60**) [14–15].
  * **Live Homefeed A/B Test Results (Table 3):**
    * *Deeper Session Rewards:* Successful Sessions (SS) **+0.24%** (Core) and **+0.48%** (Non-Core); Total Time Spent **+0.09%** (Core) and **+0.10%** (Non-Core) [12].
    * *Negative Rewards (\\(\delta_{\text{core}}=1\text{s}, \delta_{\text{non-core}}=0.5\text{s}\\)):* SS **+0.16%** (Core/Non-Core); Unsuccessful Sessions **-0.40%**; Total Time Spent **+0.35%** overall (**+0.46%** Core / **+0.24%** Non-Core); Homefeed time spent **+0.2%**, Related Pins time spent **+0.5%** [12, 13].
    * *Use-Case Adoption Rewards (\\(\tau = 0.6\\)):* SS **+0.10%** (Core/Non-Core); Total Time Spent **+0.16%** (Core) and **+0.11%** (Non-Core) [8, 12].
  * **Multi-Surface Scaling A/B Results (Table 4):**
    * *Search:* Search Fulfillment Rate **+0.25%** [14].
    * *Related Pins (P2P):* Successful Sessions **+0.15%**, accompanied by sustained **WAU gains** [14].
    * *Notifications:* Successful Sessions **+0.14%**, WAU **+0.11%** [14].
  * **Infrastructure Efficiency (DRv2 vs. DRv1):** Reduced idea-to-experiment iteration time **10× (from ~3 weeks to ~2 days)** with **<5%** incremental training step time overhead [15].

---

💡 *Would you like to explore how Pinterest's P2P rabbit hole trajectory modeling or use-case adoption rewards (\\(\mathbb{R}^{\text{UCA}}\\)) could be adapted to evaluate deep messaging engagement and profile exploration for your dating platform's ranker?*

---

### Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM [1]
`2026_arXiv_IMA_Integrated-Marketing-Attribution.md`
**Source:** https://arxiv.org/pdf/2606.16878.pdf  

### **Source Evaluation: Integrated Marketing Attribution (IMA) Framework**
*(Bhat et al., Lowe’s Companies, Inc., arXiv 2026: `2606.16878`)* [1]

---

### **(A) Query Categorization: Q1 vs. Q2**
* **Category:** **Q1 Only** (Industry/Production Attribution 2025-01 to 2026-09) [1].
* **Explanation:** Published in 2026, this paper presents an enterprise-scale production attribution architecture deployed at Lowe's Companies, Inc., built on 3 years of real-world retail marketing data [1-3]. It addresses aggregate, campaign-level marketing attribution rather than user-level retention sequence modeling.

---

### **(B) Q2 Class**
* **Classification:** **NOT**
* **Justification:** The paper explicitly rejects user-level multi-touch tracking due to privacy restrictions and third-party cookie deprecation [4, 5]. It operates entirely on aggregated, daily campaign-level media series and produces no per-interaction or per-exposure retention credit tables [6, 7].

---

### **(C) Credit Granularity and Target Outcome**
* **Per-Interaction Credit:** **No.** Credit is assigned at the **daily campaign level** (e.g., adstocked spend, impressions, or clicks for a specific campaign within a channel), not to individual user interactions or swiping events [6, 7].
* **Target Outcome:** **Daily channel-level incremental sales contribution (in dollars)** [6, 7]. This daily target is temporally disaggregated from a weekly Marketing Mix Model (MMM) that measures macro incremental sales lift [11–12].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**
* **Direct Mapping:** **Not directly applicable.** Because IMA is designed for aggregate macroeconomic data, it cannot directly parse an individual user's swiping, matching, or messaging sequence [4, 6].
* **Conceptual Transfer & Strategic Extension:**
  1. **Two-Stage Anchor-Disaggregation Framework:** Rather than assigning 100% of an N7 retention label to the final swipe (last-touch), you could structure retention attribution as a two-stage Bayesian model:
     * *Stage 1 (Aggregate Macro Anchor):* Estimate overall cohort-level or daily baseline retention lift for different feature categories or candidate cohorts using aggregated holdout metrics (analogue to MMM) [11–12].
     * *Stage 2 (Bayesian Disaggregation):* Use Bayesian regression anchored to those aggregate cohort priors to allocate retention credit across preceding interaction types (swipes, matches, 4-way conversation starts) based on campaign/feature intensity [13, 16–17].
  2. **Adstock Carry-Over Lags:** Adapts the paper’s **Adstock transformation** (peak delay \\(P\\), decay rate \\(D\\), window \\(L\\)) to model the lingering impact of early mutual matches and deep messaging conversations on retention across the 7-day window [14–15].

---

### **(E) Selection Bias & Confounding Correction**
* **Bayesian Shrinkage via Anchored Priors:** To combat severe campaign-level multicollinearity (e.g., overlapping promotional flights causing unstable coefficients and sign reversals), campaign effectiveness parameters \\(\beta_j\\) are constrained using Truncated Normal priors centered on the aggregate channel-level MMM effectiveness coefficient \\(\beta_c\\) [16–17, 19–20]:
  \\[\beta_j \sim \text{TruncatedNormal}(\beta_c, \sigma_\beta; \text{lower} = 0)\\]
* **Adstock Decay & Delay Modeling:** Uses parameterized adstock functions to decouple immediate exposure spikes from delayed downstream impact [14–15].
* *Note:* The paper does not use individual user-level propensity scores or IPW because it intentionally avoids user tracking [4, 5].

---

### **(F) Deployment and Production Dataset Evidence**
* **Production Deployment:** Deployed operationally at **Lowe's Companies, Inc.** across major digital advertising channels (Search, Social, Display) to guide tactical budget optimization across thousands of concurrent campaigns [1-3, 8].
* **Dataset:** 3 years of historical daily marketing data across Search, Social, and Display channels [2, 7].
* **Key Quoted Quantitative Results:**
  * **Channel-Level Reconstruction Fit (\\(R^2\\)):** Aggregated daily campaign predictions track weekly MMM incremental channel sales with an **\\(R^2 = 0.98\\)** for a representative channel [9].
  * **Weekly Mean Absolute Percentage Error (MAPE) by Channel:**
    * **Search:** **4.1%** (or 4.10%) [10]
    * **Social:** **5.97%** [10]
    * **Display:** **3.25%** [10]
  * **Aggregate Accuracy:** Sub-6% weekly MAPE across major digital channels, representing minimal degradation compared to the primary weekly MMM baseline (~2% MAPE) while supplying granular campaign-level visibility [23–24, 26].

---

💡 *Would you like to explore how to adapt IMA's Bayesian prior anchoring or Adstock carry-over transformations to build an aggregate cohort disaggregation model for your dating platform?*

---

### Incremental Recommendation via Causal Models [1]
`2026_arXiv_NA_Incremental-Recommendation-Causal-Models.md`
**Source:** https://arxiv.org/pdf/2608.26804.pdf  

### **Source Evaluation: *Incremental Recommendation via Causal Models***
*(Vlontzos et al., Spotify & Imperial College London, 2026: `arXiv:2608.26804`)* [1]

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**
* **Neither.** [1-4]
* **Explanation:**
  * *Q1 (Industry/Production Attribution 2025-01 to 2026-09):* **No.** While published in August 2026 and evaluated in live production at Spotify on millions of users [1, 5, 6], it is an incremental recommendation targeting framework (uplift modeling) designed to prune non-incremental impressions, rather than a multi-touch attribution (MTA) measurement system [1-4].
  * *Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):* **No.** The paper predicts short direct-response stream probability \\(\hat{p}_1(\mathbf{x})\\) vs. 2-day organic stream probability \\(\hat{p}_0(\mathbf{x})\\) at recommendation serving time [5–6, 9–10], rather than attributing overall user retention, active days, or return visits to past interaction sequences [1, 3, 4].

---

### **(B) Q2 Class**
* **Classification:** **NOT** [1, 3, 4, 7]
* **Justification:** As an uplift modeling / policy optimization framework, it presents a Causal Deep Twin Network and a dual-threshold targeting policy \\(\pi(\mathbf{x}) = \mathbb{1}[\hat{p}_1(\mathbf{x}) \ge \theta_1] \cdot \mathbb{1}[\hat{p}_0(\mathbf{x}) \le \theta_0]\\) to filter out "always-takers" at serving time [3, 8], without producing a per-exposure retention credit table or causal multi-touch attribution model [1, 3, 4, 7].

---

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction credit.** [1, 3, 7]
* **Target Outcome:** At recommendation candidate serving time, the model outputs two separate stream probability scores for a candidate item \\(\mathbf{x}\\) [9–10, 13]:
  1. **\\(\hat{p}_1(\mathbf{x})\\) (Treated Stream Probability):** Probability of a stream occurring within a **short direct-response window (minutes to hours)** when recommended [2, 9].
  2. **\\(\hat{p}_0(\mathbf{x})\\) (Holdback Organic Stream Probability):** Probability of an organic stream occurring within a **two-day window** when withheld [10, 11].
* It does not calculate fractional credit across past multi-touch user interaction sequences [1, 3, 7].

---

### **(D) Replacing Last-Touch N7 → Latest Swipes**
* **How it Improves on Last-Touch:** Last-touch post-hoc rules assign 100% of a downstream outcome to recent interactions, ignoring organic baseline engagement and "always-takers" (users who would engage regardless) [1–2]. This paper replaces post-hoc last-touch attribution with a **counterfactual dual-threshold targeting policy** \\(\pi(\mathbf{x}) = \mathbb{1}[\hat{p}_1(\mathbf{x}) \ge \theta_1] \cdot \mathbb{1}[\hat{p}_0(\mathbf{x}) \le \theta_0]\\) at candidate recommendation time [1, 3]. It explicitly models what the user would have done organically without the recommendation [3, 12].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Candidate Profile Impression (\\(\mathbf{x}\\)):* Evaluates whether presenting a specific profile card will drive an incremental right-swipe/match [9, 13].
  2. *Treated Stream Head (\\(\hat{p}_1(\mathbf{x})\\)):* Predicts the probability of an immediate right-swipe or match within a short direct-response window (e.g., minutes/hours of profile exposure) [2, 9].
  3. *Holdback Organic Head (\\(\hat{p}_0(\mathbf{x})\\)):* Predicts the organic probability that the user would discover, match, or converse with this user organically over a multi-day window (e.g., 2 days) through organic search or browse surfaces [10, 11].
  4. *Pruning Non-Incremental Swipes (\\(\theta_0\\)):* Filters out profile recommendations where \\(\hat{p}_0(\mathbf{x}) > \theta_0\\) (users who would organically discover/match anyway), saving scarce recommendation slots for profiles where recommendations are both effective (\\(\hat{p}_1(\mathbf{x}) \ge \theta_1\\)) and necessary (\\(\hat{p}_0(\mathbf{x}) \le \theta_0\\)) [1, 13–14].

---

### **(E) Selection-Bias & Confounding Handling**
1. **Randomized Holdback Experiments (\\(\mathcal{D}_0\\)):** Utilizes routine holdback randomized experiments where recommendations are withheld from a small randomized fraction of eligible users, providing unconfounded samples from the counterfactual organic distribution \\(Y(0)\\) [1–2, 10–11].
2. **Partitioned Loss Function:** Trains the Deep Twin Network using partitioned binary cross-entropy loss [11–12]:
   \\[\mathcal{L} = \frac{1}{|\mathcal{D}_1|} \sum_{i \in \mathcal{D}_1} \ell_{\text{bce}}(y_i, \hat{p}_1(\mathbf{x}_i)) + \frac{1}{|\mathcal{D}_0|} \sum_{j \in \mathcal{D}_0} \ell_{\text{bce}}(y_j, \hat{p}_0(\mathbf{x}_j)) \quad \text{[14]}\\]
   where treated examples update *only* the treated head (\\(\hat{p}_1\\)) and holdback examples update *only* the holdback head (\\(\hat{p}_0\\)), while both update the deep shared trunk \\(\mathbf{z}\\) [11–12]. This prevents conflating the different temporal attribution windows (minutes/hours vs. 2 days) [7, 14].
3. **Handling Mismatch & Backend-Client Discrepancies:** Acknowledges an approximate **30% discrepancy** between backend recommendation servings (holdback log events \\(\mathcal{D}_0\\)) and client-side impressions (treated log events \\(\mathcal{D}_1\\)) due to latency and client-side rendering [15]. The dual-threshold policy avoids naive subtraction \\(\hat{p}_1(\mathbf{x}) - \hat{p}_0(\mathbf{x})\\) (which is mathematically invalid due to window mismatch and distributional differences) and instead treats the two scores as independent binary decision levers [7–8, 13].

---

### **(F) Deployment and Production Dataset Evidence**
* **Production Deployment:** Deployed live in production at **Spotify** on mobile and desktop recommendation surfaces across a 2-week A/B test on millions of users [1, 3–4, 17–18].
* **Quoted Numbers from the Source:**
  * **Recommendation Impressions Reduction:** **-7.1%** (`[-7.2%, -6.9%]`, 95% CI) reduction in recommendation impressions per user [1, 16].
  * **Recommended Content Consumption:** **-0.37%** (`[-0.86%, +0.21%]`, 95% CI) — **no statistically significant reduction** in overall consumption of recommended content or listener satisfaction guardrails [1, 16].
  * **Backend vs. Client-Side Discrepancy:** Approximately **30% discrepancy** between backend recommendation servings (holdback log events) and client-side impressions (treated log events) [15].
  * **Temporal Attribution Windows:** Treated streams are attributed within a **short direct-response window (on the order of minutes to hours)**; holdback organic streams are attributed within a **two-day window** [5–6].

---

💡 *Would you like to explore how Spotify's dual-threshold policy (\\(\pi(\mathbf{x})\\)) or holdback Deep Twin Network architecture could be adapted to prune non-incremental candidate profile impressions for your dating platform?*

---

