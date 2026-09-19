# Relevance index 4/10 — Project Relevance sections of all cards (generated)

### Learned Ranking Function: From Short-term Behavior Predictions to Long-term User Satisfaction [1]
`2024_RecSys_LRF_Learned-Ranking-Function-YouTube.md`
**Source:** https://arxiv.org/pdf/2408.06512.pdf  

### **Part 1: Dating App Retention Project Evaluation**

#### **(A) Q1 or Q2 or Both or Neither?**
* **Answer:** **Neither.** [1-3]
* **Explanation:**
  * **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** Published in October 2024 at RecSys '24 [1], which falls outside the 2025–2026 window. Furthermore, it is a slate optimization and candidate ranking framework for video recommendations, not a multi-touch attribution (MTA) measurement system [1-3].
  * **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** LRF predicts long-term user satisfaction lift (\\(R_{\text{lift}}\\)) at candidate ranking time using uplift modeling and cascade click probabilities [4-6], rather than attributing N7 retention or active days across past multi-touch user interaction sequences.

---

#### **(B) Q2 Class**
* **Classification:** **NOT** [3, 7, 8]
* **Justification:** As a slate ranking and RL policy optimization framework (**LRF**), it computes a candidate ranking score:
  \\[\text{Score}(u, v) = \frac{p_{\text{clk}}(u, v)}{p_{\text{clk}}(u, v) + p_{\text{abd}}(u, v)} \cdot R_{\text{lift}}(u, v)\\[5, 8]\\]
  to sort candidate profile slates, rather than publishing a per-exposure retention credit table or multi-touch sequence attribution model.

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction sequence attribution.**
* **Target Outcome:** At candidate ranking time, the model outputs item-level long-term reward lift:
  \\[R_{\text{lift}}(u, v) = R_{\text{clk}}(u, v) - R_{\text{abd}}(u)\\[4, 6]\\]
  representing expected long-term user satisfaction (e.g., total platform watch time / return visits) generated if user \\(u\\) clicks video \\(v\\) versus abandoning the slate [4, 9].

---

#### **(D) Replacing Last-Touch N7 → Latest Swipes**
* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% of an N7 retention label to recent interactions post-hoc, ignoring the baseline value of user abandonment and non-incremental activity. LRF replaces post-hoc last-touch attribution by scoring candidate profiles at ranking time using **uplift modeling against abandonment**:
  \\[\text{Score}(u, v) = \frac{p_{\text{clk}}(u, v)}{p_{\text{clk}}(u, v) + p_{\text{abd}}(u, v)} \cdot \big(R_{\text{clk}}(u, v) - R_{\text{abd}}(u)\big)\\[5, 6, 8]\\]
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Candidate Profile Ranking:* Evaluates candidate profile cards \\(v\\) for user \\(u\\) during a swiping session [10, 11].
  2. *Click/Match & Abandonment Propensities:* Predicts right-swipe/match probability \\(p_{\text{clk}}(u, v)\\) and session abandonment probability \\(p_{\text{abd}}(u, v)\\) (the user closing the app / leaving the swipe deck) [12, 13].
  3. *Long-Term Retention Lift (\\(R_{\text{lift}}\\)):* Models \\(R_{\text{clk}}(u, v) - R_{\text{abd}}(u)\\), isolating the net 7-day retention gain from a mutual match/conversation resulting from card \\(v\\) relative to the baseline retention \\(R_{\text{abd}}(u)\\) if the user abandons the swiping session [4, 6].

---

#### **(E) Selection-Bias & Confounding Handling**
1. **Cascade Click Model with Abandonment:** Explicitly models position bias and inspection probabilities in candidate slates, decomposing click probability into:
   \\[P_i^{\text{cascade}} = \left(\prod_{j=1}^{i-1} (1 - p_{\text{clk}} - p_{\text{abd}})\right) \cdot p_{\text{clk}}\\[12, 13]\\]
2. **Uplift Loss Formulation:** Uses an uplift loss:
   \\[\mathbb{E}\left[\left|R_{\text{lift}}(u_t, v_t) + R_{\text{abd}}(u_t) - \text{Reward}(\tau, t)\right|^2 \;\middle|\; c_t > 0\right]\\[6]\\]
   to directly estimate net differential reward \\(R_{\text{clk}} - R_{\text{abd}}\\), debiasing item scores against user baseline retention [6].

---

#### **(F) Deployed or Production Dataset Evidence**
* **Production Deployment:** Fully launched in live production on **YouTube’s Watch Page** recommendation pipeline [1, 3, 14, 15].
* **Quoted Numbers from the Source:**
  * **Initial LRF Deployment vs. Bayesian Optimization Control:** **+0.21%** lift (95% CI `[0.04, 0.38]`) in top-line metrics [15, 16].
  * **Cascade Click Model Impact (\\(\frac{p_{\text{clk}}}{p_{\text{clk}} + p_{\text{abd}}}\\) vs. CTR):** **+0.66%** lift (95% CI `[0.60, 0.72]`) in top-line metric over control [16].
  * **Setting \\(R_{\text{abd}} = 0\\) (Ignoring Abandonment):** **-0.46%** regression (95% CI `[0.43, 0.49]`) in top-line platform metrics (despite watch page local metric +0.20% `[0.14, 0.26]`) [17].
  * **Direct \\(R_{\text{lift}}\\)-Loss vs. Two-Model Uplift Baseline:** **+0.12%** lift (95% CI `[0.06, 0.18]`) in top-line metrics [18].

---

### **Part 2: Detailed Technical Breakdown of the Source**

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Learned Ranking Function: From Short-term Behavior Predictions to Long-term User Satisfaction* [1]
* **Authors:** **Yi Wu**\*¹, **Daryl Chang**\*¹, **Jennifer She**¹, **Zhe Zhao**¹, **Li Wei**¹, and **Lukasz Heldt**¹ (\*Equal contribution) [1]
* **Affiliations:** **Google / YouTube** (San Bruno, CA & Mountain View, CA, USA) [1, 19]
* **Year & Venue:** Published in **2024** at the *Proceedings of the 18th ACM Conference on Recommender Systems (RecSys ’24), October 14–18, 2024, Bari, Italy* [1].

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Large video recommendation systems make multi-task predictions for short-term user behavior (e.g., CTR, watch time after click) [2], but combining these predictions into a single ranking score typically relies on heuristic functions or manual hyperparameter tuning (e.g., Bayesian optimization) [7, 20]. These heuristics struggle to scale, adapt to changing platform objectives, or directly optimize for long-term user satisfaction across the platform [7, 20]. Furthermore, existing slate optimization frameworks assume zero future rewards when a user abandons a slate, which is unrealistic for platforms where users navigate between recommendation surfaces or return later [9].
* **Key Contributions:**
  1. **Learned Ranking Function (LRF):** Formulates slate ranking as a Markov Decision Process (MDP) and proves (Theorem 2.3) that maximizing slate-level long-term rewards under a cascade click model with abandonment reduces to an optimal user-item ranking function [3, 5, 10]:
     \\[\text{Score}(u, v) = \frac{p_{\text{clk}}(u, v)}{p_{\text{clk}}(u, v) + p_{\text{abd}}(u, v)} \cdot R_{\text{lift}}(u, v)\\[5]\\]
  2. **Lift Loss Formulation (\\(R_{\text{lift}}\\)):** Explicitly models the baseline value of user abandonment (\\(R_{\text{abd}}(u)\\)) and directly estimates \\(R_{\text{lift}}(u, v) = R_{\text{clk}}(u, v) - R_{\text{abd}}(u)\\) using an uplift modeling loss to isolate the true net satisfaction gain of clicking a video versus leaving the slate [4, 6].
  3. **Dynamic Linear Scalarization:** Develops a multi-objective constrained optimization algorithm with closed-form quadratic solutions to dynamically balance primary and secondary platform metrics during online inference [3, 8, 21].
  4. **Full Production Launch on YouTube:** Fully launched in live production on YouTube's Watch Page, outperforming existing Bayesian-optimized ranking functions [1, 3, 14, 15].

---

#### **(3) Proposed Method or Architecture in Detail**
* **MDP Formulation & Cascade Click Model:**
  * User state \\(s = (u, V)\\), where \\(u\\) represents user state and \\(V\\) is a set of \\(n\\) candidate videos [10]. Action \\(\sigma\\) is a permutation ranking of \\(V\\) [11].
  * *Cascade Click Model with Abandonment:* For each position \\(i\\), the user either clicks with probability \\(p_{\text{clk}}(u, v)\\), abandons the slate with probability \\(p_{\text{abd}}(u, v)\\), or scrolls to position \\(i+1\\) with probability \\(1 - p_{\text{clk}} - p_{\text{abd}}\\) [12, 13].
* **Optimal User-Item Ranking Theorem (Theorem 2.3):**
  * Proves that maximizing cumulative long-term slate reward \\(Q^\pi(s, \sigma)\\) decomposes into ordering candidates by:
    \\[\text{Score}(u, v) = \frac{p_{\text{clk}}(u, v)}{p_{\text{clk}}(u, v) + p_{\text{abd}}(u, v)} \cdot R_{\text{lift}}(u, v)\\[5]\\]
  * Extended to multi-objective constrained optimization via weight vector \\(w = (1, w_2, \dots, w_m)\\):
    \\[\text{Score}(u, v) = \frac{p_{\text{clk}}(u, v)}{p_{\text{clk}}(u, v) + p_{\text{abd}}(u, v)} \cdot \langle R_{\text{lift}}(u, v; \theta), w \rangle\\[8]\\]
* **Training Stage:**
  * Uses on-policy Monte Carlo user trajectory buffers [22, 23].
  * *Uplift Network Loss:* Directly estimates \\(R_{\text{lift}}\\)-value using MSE loss on clicked items:
    \\[\mathbb{E}_{\tau \sim D, t} \left[ \left| R_{\text{lift}}(u_t, V_{\sigma(c_t)t}; \theta) + R_{\text{abd}}(u_t; \theta) - \text{Reward}(\tau, t) \right|^2 \;\middle|\; c_t > 0 \right]\\[6]\\]
  * *Click Network Loss:* Fits \\(p_{\text{clk}}\\) and \\(p_{\text{abd}}\\) using cross-entropy loss over cascade probabilities [6].
* **Credit Assignment Mechanics:**
  * Credit is assigned at the **individual candidate item level** by multiplying conditional click propensity \\(\frac{p_{\text{clk}}}{p_{\text{clk}} + p_{\text{abd}}}\\) by the long-term reward lift \\(R_{\text{lift}}(u, v)\\) [5, 8].
  * It does **not** perform multi-touch sequence attribution over past user interaction logs; rather, it uses uplift modeling (\\(R_{\text{clk}} - R_{\text{abd}}\\)) to score candidate items based on their expected incremental contribution to long-term user satisfaction [4, 6].

---

#### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets & Scale:** Trained on on-policy user trajectory logs collected directly from live YouTube traffic [22, 23].
* **Production Deployment:** Fully launched in live production on **YouTube’s Watch Page** recommendation pipeline [1, 3, 14, 15].
* **Comparison Baselines:**
  1. *Previous Production System:* Heuristic ranking function tuned using Bayesian optimization (Google Vizier) [15, 16, 24].
  2. *Without Cascade Click Model:* Ranking candidates by \\(\text{CTR} \cdot R_{\text{lift}}\\) [15, 16].
  3. *Without Lift Formulation (\\(R_{\text{abd}} = 0\\)):* Maximizing absolute click reward \\(R_{\text{clk}}\\) without subtracting abandonment baseline \\(R_{\text{abd}}\\) [17].
  4. *Two-Model Uplift Baseline:* Predicting \\(R_{\text{clk}}\\) and \\(R_{\text{abd}}\\) separately using two distinct models (\\(R_{\text{click}} - R_{\text{abd}}\\)) [17, 18].

---

#### **(5) Key Quantitative Results with Numbers**
* **Initial Deployment vs. Production Control (Section 4.2.1):**
  * LRF outperformed the production Bayesian optimization baseline by **+0.21%** (95% CI `[0.04, 0.38]`) in top-line long-term satisfaction metrics [15, 16].
* **Cascade Click Model Impact (Section 4.2.2):**
  * Replacing standard CTR with cascade probability \\(\frac{p_{\text{clk}}}{p_{\text{clk}} + p_{\text{abd}}}\\) yielded a **+0.66%** lift (95% CI `[0.60, 0.72]`) in top-line metrics over control [16].
* **Importance of Lift Formulation (\\(R_{\text{abd}} = R_{\text{clk}} - R_{\text{lift}}\\), Section 4.2.4):**
  * Setting \\(R_{\text{abd}} = 0\\) (ignoring user abandonment value) regressed top-line metrics by **-0.46%** (95% CI `[0.43, 0.49]`) [17].
  * *(Insight)*: Although watch page local recommendations increased by **+0.20%** (95% CI `[0.14, 0.26]`), overall platform-wide metrics regressed, proving that ignoring \\(R_{\text{abd}}\\) causes greedy local recommendations that harm long-term retention [17].
* **Direct Lift Loss vs. Two-Model Uplift Baseline (Section 4.2.5):**
  * Direct \\(R_{\text{lift}}\\)-network training outperformed the separate Two-Model baseline by **+0.12%** (95% CI `[0.06, 0.18]`) in top-line metrics [17, 18].

---

#### **(6) Limitations, Failure Modes, or Negative Results**
1. **Severe Metric Regression when Ignoring Abandonment (\\(R_{\text{abd}} = 0\\)):** Setting \\(R_{\text{abd}} = 0\\) regressed top-line platform metrics by **-0.46%**, proving that optimizing local item rewards without accounting for user abandonment baseline values harms platform-level retention [17].
2. **Sub-optimality of Separate Two-Model Uplift:** Predicting \\(R_{\text{clk}}\\) and \\(R_{\text{abd}}\\) separately (two-model approach) was inferior to directly predicting \\(R_{\text{lift}}\\) via uplift modeling loss (losing **0.12%** in top-line metrics) [17, 18].
3. **Cascade Click Model Assumptions:** Relies on a single-pass cascade click model assumption (users inspect items sequentially from top to bottom and either click, scroll, or abandon), which may not fully hold for non-linear grid layouts or multi-click sessions [12, 13].
4. **On-Policy Data Dependency:** Relies on an on-policy Monte Carlo data buffer; off-policy Q-learning and Temporal Difference (TD) learning are noted as future work [18, 22, 23, 25].

---

#### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Ie et al. (2019) [Ref 13 / SlateQ]:** *SlateQ: A tractable LLM/RL approach to slate recommendation* (IJCAI '19 / NeurIPS '19) [7, 26].
2. **Craswell et al. (2008) [Ref 9 / Cascade Click Model]:** *An experimental comparison of click position-bias models* (WSDM '08) [9, 11, 12].
3. **Covington, Adams, & Sargin (2016) [Ref 8 / YouTube DNN]:** *Deep Neural Networks for YouTube Recommendations* (RecSys '16) [2, 10].
4. **Sutton & Barto (2018) [Ref 16 / RL Book]:** *Reinforcement learning: An introduction* (MIT Press) [13, 18, 22].
5. **Golovin et al. (2017) [Ref 11 / Vizier]:** *Google Vizier: A Service for Black-Box Optimization* (KDD '17) [15, 24].
6. **Gutierrez & Gérardy (2017) [Ref 12 / Uplift Modeling]:** *Causal inference and uplift modelling: A review* [6, 18, 27].
7. **Wilhelm et al. (2018) [Ref 18 / DPP Diversity]:** *Practical diversified recommendations on youtube with determinantal point processes* (CIKM '18) [2, 22, 28].

---

💡 *Would you like to explore how YouTube's uplift formulation (\\(R_{\text{clk}} - R_{\text{abd}}\\)) or dynamic linear scalarization could be adapted to balance candidate profile matches against session abandonment risk for your dating platform?*

---

### Sequential Recommendation for Optimizing Both Immediate Feedback and Long-term Retention
`2024_arXiv_NA_Sequential-Rec-Immediate-Feedback-Long-term-Retention.md`
**Source:** https://arxiv.org/html/2404.03637  

### **Source Evaluation: *Sequential Recommendation for Optimizing Both Immediate Feedback and Long-term Retention***
*(arXiv pre-print, April 2024: `arXiv:2404.03637v2`)*

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**

**Neither.** [1, 3, 11–12, 19]
* **Q1 (Industry/Production Attribution 2025-01 to 2026-09):** **No.** Published in April 2024 (`arXiv:2404.03637v2`), which falls outside the 2025–2026 window [1]. Furthermore, it is evaluated on offline benchmark datasets rather than an industry production attribution system [1, 2].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** DT4IER formulates long short-term multi-task sequential recommendation using an offline Reinforcement Learning / Decision Transformer framework [3, 4]. It generates candidate item sequences conditioned on multi-reward Return-to-Go (RTG) prompts rather than calculating per-touch attribution credit across historical interaction logs [3, 8, 11–12].

---

### **(B) Q2 Class**

**NOT.** [3, 8, 11–12]
* **Justification:** DT4IER is an offline RL / Decision Transformer sequence modeling framework that predicts recommended item lists conditioned on Return-to-Go (RTG) prompts [3, 8, 10–12]. It does **not** produce or publish a per-exposure retention credit table or multi-touch attribution decomposition.

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction credit table.** [8, 10–12]
* **Target Outcome & Formula:** Replaces temporal value estimation with autoregressive sequence generation. Given an input trajectory:
  \\[\tau = \left(\hat{\mathbf{R}}_1, \mathbf{s}_1, \mathbf{a}_1, \dots, \hat{\mathbf{R}}_t, \mathbf{s}_t, \mathbf{a}_t, \dots, \hat{\mathbf{R}}_T, \mathbf{s}_T\right)\\]
  it predicts future action sequence embeddings \\(\hat{\mathbf{E}}^A\\) conditioned on a 2D Return-to-Go prompt \\(\hat{\mathbf{R}}_t = [\hat{R}_{s,t}, \hat{R}_{l,t}] = [\sum_{i=t}^T r_{s,i}, \sum_{i=t}^T r_{l,i}]\\) [5, 6].
  * **Short-term indicator (\\(r_{s,t}\\)):** Click-Through Rate (CTR) for recommended list \\(\mathbf{a}_t\\) at session \\(t\\) [6].
  * **Long-term indicator (\\(r_{l,t}\\)):** Return frequency for session \\(t\\) measuring user retention [6].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**

* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% of the binary N7 retention label to recent swipes post-hoc, ignoring earlier swiping patterns and short- vs. long-term trade-offs. DT4IER replaces post-hoc last-touch rule assignment by modeling candidate profile generation autoregressively using a Decision Transformer [3, 10–11]. It conditions recommendation generation on an adaptively balanced multi-reward Return-to-Go prompt \\(\hat{\mathbf{R}}_t\\) (balancing immediate match/click rates and long-term 7-day retention/return frequency based on user features) [5, 11–15].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *State (\\(\mathbf{s}_t\\)):* Encodes historical swiping, matching, and 4-way conversation interactions (user-clicked/engaged profile IDs zero-padded to length \\(H=30\\)) using a GRU state-action encoder [6, 7].
  2. *Action (\\(\mathbf{a}_t\\)):* Generated candidate profile card recommendation list of length \\(N=30\\) [6].
  3. *Adaptive RTG Balancing:* Reweights short-term RTG (immediate right-swipe / match rate) and long-term RTG (7-day retention / return frequency) using user-specific attributes to resolve trade-off conflicts [14–15].
  4. *Contrastive Learning (\\(\mathcal{L}_{\text{contra}}\\)):* Treats low-performing swiping sessions (where both match rate \\(r_{s,t}\\) and retention reward \\(r_{l,t}\\) fall below **0.6**) as negative samples \\(\Omega^-\\), preventing action embeddings for distinct reward prompts from converging too closely and steering the ranker away from low-retention swiping patterns [8].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Adaptive RTG Balancing Module:** Reweights short-term (CTR) and long-term (return frequency) RTG sequences using user-specific attributes to balance immediate feedback with long-term retention [14–15].
2. **Contrastive Learning Objective (\\(\mathcal{L}_{\text{contra}}\\)):** Defines negative samples \\(\Omega^-\\) as session data points where short- and long-term rewards are consistently below **0.6** (falling below average in both click rate and retention metrics) [8]. The contrastive loss \\(\mathcal{L}_{\text{contra}} = -\sum_{\hat{\mathbf{E}}^{A-} \in \Omega^-} D(\hat{\mathbf{E}}^A, \hat{\mathbf{E}}^{A-})\\) ensures action embeddings for distinct reward prompts do not converge too closely [8].
3. **Cross-Entropy Loss over One-Hot Discrete Actions:** Converts discrete action space elements (item IDs of length **30**) into one-hot encoded labels and optimizes via cross-entropy loss \\(\mathcal{L}_{\text{cross}} = -\sum_{z=1}^Z y_{o,z} \log(p_{o,z})\\) combined with \\(\alpha \mathcal{L}_{\text{contra}}\\) (\\(\alpha = \mathbf{0.1}\\)) [17–18].
4. *Note:* Does not use explicit Inverse Propensity Weighting (IPW) or formal causal graph identification for user swiping selection bias.

---

### **(F) Deployment and Production Dataset Evidence**

* **Production Deployment:** **Not specified in source** (evaluated offline on benchmark datasets) [2].
* **Offline Datasets:**
  * **Kuairand-Pure:** Unbiased sequential recommendation dataset featuring random video exposures [2].
  * **MovieLens-25M (ML-25M):** Large-scale sparse benchmark for sequential recommender systems [2].
  * **RetailRocket:** Real-world e-commerce recommendation dataset [2].
* **Quoted Quantitative Results:**
  * **Ablation Study Improvements (Section 4.6 & Passage 21):**
    * *Adaptive RTG Balancing (DT4IER vs. NAW):* **+1.50% in BLEU**, **+1.90% in NDCG**, **+0.08% in SB-URS**.
    * *Multi-Reward Encoder (DT4IER vs. NRE):* **+1.80% in BLEU**, **+2.30% in NDCG**, **+0.19% in SB-URS**.
    * *Contrastive Loss (DT4IER vs. NCL):* **+1.02% in BLEU**, **+1.60% in NDCG**, **+0.03% in SB-URS**.
  * **RTG Prompting Saturation Analysis (Section 4.7 & Passages 22–23):** Performance (BLEU and NDCG) increases consistently as RTG prompt proportion increases from **0.4 to 0.8**, achieving peak accuracy at **0.8** (prompting beyond 0.8 shows saturation without additional gains).
  * **Model Hyperparameters (Section 4.4 & Passage 20):** Trajectory length \\(T = \mathbf{20}\\); maximum state/action sequence length \\(H = N = \mathbf{30}\\); **2** Transformer layers; **8** heads; embedding size **128**; Adam optimizer batch size **128**; learning rate **0.005** (Kuairand-Pure) and **0.02** (ML-25M, RetailRocket); contrastive loss negative threshold **0.6**; contrastive loss weight \\(\alpha = \mathbf{0.1}\\); balancing term \\(\gamma = \mathbf{0.5}\\).

---

💡 *Would you like to explore how DT4IER's adaptive RTG balancing block or contrastive loss could be adapted to condition candidate profile generation on both immediate match feedback and 7-day retention for your dating app?*

---

