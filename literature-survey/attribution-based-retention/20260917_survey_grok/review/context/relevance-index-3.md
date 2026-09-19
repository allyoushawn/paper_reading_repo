# Relevance index 3/10 — Project Relevance sections of all cards (generated)

### Reinforcing User Retention in a Billion Scale Short Video Recommender System [1]
`2023_WWW_RLUR_Reinforcing-User-Retention.md`
**Source:** https://arxiv.org/pdf/2302.01724.pdf  

### **Source Evaluation: Reinforcing User Retention in a Billion Scale Short Video Recommender System**
*(Cai et al., Kuaishou Technology, WWW 2023 / arXiv: `2302.01724`)* [1–4]

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**
* **Neither.**  
* **Explanation:** 
  * *Q1 (Industry/Production Attribution 2025-01 to 2026-09):* **No.** The paper was published in WWW 2023 (April 30 – May 4, 2023), falling outside the 2025–2026 timeframe [3–4].
  * *Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):* **No.** The authors explicitly state that *"retention reward is a long-term feedback after multiple interactions... and it is hard to decompose retention reward to each item or a list of items"* [2, 6–7]. The paper focuses on reinforcement learning (RL) policy optimization for request-level ranking weights rather than multi-touch attribution sequence modeling [7, 11–12].

---

### **(B) Q2 Class**
* **Classification:** **NOT**  
* **Justification:** As an RL policy optimization framework (**RLUR**), it outputs an 8-dimensional continuous action vector \\(a_{it} \in [1]^8\\) representing dynamic ensemble weights for ranking models, rather than producing a per-exposure or per-item retention credit table [2, 11–12, 28].

---

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No.** Credit is assigned at the **request level to a continuous 8-dimensional ensemble weight action vector (\\(a_{it}\\))**, which combines scoring model predictions (watch time, short view, long view, like, follow, forward, comment, profile entry) [11–12, 28].
* **Target Outcome:** **Cumulative returning time gap (\\(T(s_i)\\))** between consecutive app sessions in an infinite-horizon MDP, which directly maximizes **app open frequency, Day-1/Day-7 user retention, and Daily Active Users (DAU)** [2, 7, 12–13].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**
* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% of the binary N7 label to the user's latest swipes [11–12]. RLUR bypasses rule-based attribution labeling entirely by framing candidate ranking as an infinite-horizon MDP that directly learns to minimize future session return gaps [7, 12–13].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Dynamic Ensemble Action Vector (\\(a_{it}\\)):* Replaces fixed swipe-ranking heuristics with dynamic weights \\(a_{it} = [a_{\text{swipe}}, a_{\text{match}}, a_{\text{chat}}, \dots]\\) that balance multiple candidate interaction heads [11–12, 28].
  2. *Immediate Response (\\(I(s_{it}, a_{it}\\))):* Aggregates short-term session signals (e.g., total right swipes, mutual matches, and 4-way conversation starts) across candidate profile exposures in a request [11–12, 28].
  3. *Retention Critic (\\(Q_T(s_{it}, a_{it}\\))):* Predicts expected returning time gaps [13–14]. Candidate profiles are ranked by combining immediate interaction predictions with long-term retention value to maximize 7-day revisitation [11–13, 21–22].

---

### **(E) Selection-Bias & Confounding Correction**
1. **User Activity Stratification:** Because highly active users naturally have much shorter return gaps than low-activity users, training an unstratified model causes parameter learning to be dominated by hyper-active users [8, 21–22]. RLUR trains separate actor policies (\\(\pi_{\text{high}}\\) and \\(\pi_{\text{low}}\\)) for high- and low-activity user groups [21–22].
2. **Retention Reward Variance Normalization:** To handle external noise (e.g., social events), RLUR normalizes returning times using a session-level classification model \\(T'\\) that predicts return probability, creating a bounded reward [8, 19–21]:
   \\[r(s_{it}, a_{it}) = \text{clip}\left\{0, \frac{T(s_i)}{(1 - T'(x)) \cdot T_\beta}, \alpha\right\}\text{ [20–21]}\\]
3. **Soft Regularization for Long Reward Delays:** To prevent off-policy training instability caused by hours/days of reward delay, RLUR applies an exponential soft penalty based on policy density shift \\(\exp(\max\{\beta \cdot (\log p(a_{it}|s_{it}) - \log p_b(a_{it}|s_{it})), 0\})\text{ [8, 22–23]}\n\\).

---

### **(F) Deployment and Production Dataset Evidence**
* **Production Deployment:** Fully launched and deployed in live production on the **Kuaishou app** serving over a **billion users** [2-4].
* **Offline Benchmark Dataset:** **KuaiRand** (an unbiased sequential short-video interaction dataset) used to build a multi-session user behavior and return simulator [5].
* **Quoted Quantitative Results:**
  * **Offline Simulator Benchmark (KuaiRand, Table 1):**
    * *CEM Baseline:* Returning time = **2.036**, User retention = **0.587** [6, 7].
    * *TD3 Baseline:* Returning time = **2.009**, User retention = **0.592** [6, 7].
    * *RLUR (naive, \\(\gamma=0\\)):* Returning time = **2.001**, User retention = **0.596** [6, 7].
    * *RLUR (naive, \\(\gamma=0.9\\)):* Returning time = **1.961**, User retention = **0.601** [6, 7].
    * *RLUR (Full Framework):* Returning time = **1.892** (lowest), User retention = **0.618** (highest) [6, 7].
  * **Live Online A/B Test (Kuaishou Platform vs. CEM Baseline, Converged >Day 100):**
    * **App Open Frequency:** Converged to **+0.450%** [8].
    * **Daily Active Users (DAU):** Converged to **+0.2%** [8].
    * **Day-1 User Retention:** Converged to **+0.053%** [8].
    * **Day-7 User Retention:** Converged to **+0.063%** [8].
    * *Statistical Significance Note:* The paper explicitly notes that *"0.01% improvement of user retention and 0.1% improvement of DAU are statistically significant in short video platforms"* [8].

---

💡 *Would you like to explore how RLUR's activity group stratification or returning time normalization technique could be integrated into your dating app's candidate profile ranking pipeline?*

---

### **Part 1: Dating App Retention Project Evaluation**
`2024_KDD_FID_Future-Impact-Decomposition.md`
**Source:** https://arxiv.org/pdf/2401.16108.pdf  

### **Source Evaluation: ItemA2C (*Future Impact Decomposition in Request-level Recommendations*)**
*(Wang et al., Peking University & Kuaishou Technology, KDD 2024: `arxiv:2401.16108`)* [1, 6–7]

---

### **(A) Query Categorization: Q1 vs. Q2**
* **Answer:** **Neither Q1 nor Q2.**
* **Explanation:** 
  * *Q1 (Industry Attribution 2025–2026):* Published in August 2024 (KDD ’24), which falls outside the specified 2025–2026 timeframe [6–7].
  * *Q2 (Interaction-Level Retention Attribution):* Focuses on reinforcement learning (RL) policy optimization for list-wise recommendations rather than multi-touch causal sequence attribution over historical user journey logs [8–12, 18].

---

### **(B) Q2 Class**
* **Classification:** **NOT**
* **Justification:** The paper presents an RL actor-critic policy optimization method (**ItemA2C**) that decomposes list-level future value \\(V(s_{t+1})\\) down to individual items for policy gradient updates, rather than publishing an explicit per-exposure retention credit table or multi-touch attribution model [15–18, 35–41].

---

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Yes (in the form of an RL item-level advantage score)** [39–41].
* **Target Outcome & Formula:** Allocates cumulative session rewards \\(R(s_t, a_t) = \sum r_{t,k}\\) and long-term state value \\(V(s_{t+1})\\) (which drives user retention) to individual items \\(i_{t,k}\\) in list \\(a_t\\) via item target value \\(\Psi_w\\) and advantage \\(A\\) [1-4]:
  \\[\Psi_w(s_t, i_{t,k}) = r_{t,k} + w_{t,k} \gamma (1-d) V(s_{t+1}) \quad [3]\\]
  \\[A(s_t, i_{t,k}, w_{t,k}) = \Psi_w(s_t, i_{t,k}) - \frac{V(s_t)}{K} \quad [4]\\]
  where \\(r_{t,k}\\) is the immediate item reward, \\(V(s_{t+1})\\) is the estimated future state value, and \\(w_{t,k}\\) is a reward-based or model-based item weight (\\(\sum_{k=1}^K w_{t,k} = 1\\)) [36, 39, 43–44, 47].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**
* **How it Improves Last-Touch:** Last-touch assigns binary N7 retention labels exclusively to the most recent swipes, ignoring earlier swipes and intermediate value creation. **ItemA2C** provides a mathematically grounded RL framework to decompose long-term value \\(V(s_{t+1})\\) (which directly drives N7 retention) across all candidate recommendations in a swiping session based on immediate engagement signals \\(r_{t,k}\\) and learned future impact weights \\(w_{t,k}\\) [15, 36–39].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Immediate Item Reward (\\(r_{t,k}\\)):* Formulated as a weighted sum of immediate candidate interaction events [76–77]:
     \\[r(s_t, \text{candidate}_k) = w_1 \cdot \mathbb{1}[\text{swipe\_right}] + w_2 \cdot \mathbb{1}[\text{match}] + w_3 \cdot \mathbb{1}[\text{4-way\_conversation}] \quad [5]\\]
  2. *Value Function (\\(V(s_{t+1})\\)):* Estimates the user's expected cumulative long-term engagement and retention probability given their updated profile state \\(s_{t+1}\\) after the swiping session [31–32].
  3. *Item Credit Allocation (\\(w_{t,k}\\)):* Uses reward-based weighting (\\(w_{t,k} = r_{t,k} / R\\)) or adversarial model-based weighting (\\(w_{t,k} = w(i_{t,k}, s_t, s_{t+1}, r_{t,k})\\)) to assign fractional credit for \\(V(s_{t+1})\\) to each candidate profile shown [39, 43–45].

---

### **(E) Selection-Bias & Confounding Handling**
1. **Critic Baseline Subtraction (Advantage Formulation):** Subtracts the mean expected state baseline \\(V(s_t)/K\\) from the item target value \\(\Psi_w(s_t, i_{t,k})\\) to compute the item advantage \\(A(s_t, i_{t,k}, w_{t,k})\\), preventing naturally hyper-active users (who have high baseline \\(V(s_t)\\)) from artificially inflating individual item scores [4].
2. **Quantile Normalization:** Uses quantile-based discretization for continuous engagement signals (e.g., watch time) to prevent extreme outlier sessions from skewing reward distributions [5].

---

### **(F) Deployment and Dataset Evidence**
* **Production Deployment:** Deployed in the **refined ranking stage** (ranking ~500 candidates down to list size \\(K=6\\)) of Kuaishou's short-video platform serving **over 100 million Daily Active Users (DAU)** [75–78, 81].
* **Datasets:** Evaluated offline on **MovieLens-1M (ML1M)**, **KuaiRand1K**, and the **KuaiSim** simulator [50–52].
* **Quoted Quantitative Results:**
  * **Offline Simulator (KuaiRand1K, \\(K=6\\), Table 1):** `ItemA2C-M` achieved **Total Reward = 16.03 ± 0.53** and **Depth = 16.59 ± 0.45** vs. standard request-level `A2C` (**10.01 ± 0.86 / 11.56 ± 0.72**) and state-of-the-art `HAC` (**12.65 ± 0.26 / 13.72 ± 0.22**), representing a **+26.7% reward increase** (\\(p < 0.05\\)) [55–56, 64].
  * **Live Online A/B Test (Table 3, 100M+ DAU Platform):**
    * *`ItemA2C` vs. `request-level A2C`:* **+0.129% Watch Time**, **+1.103% Like Rate**, **+0.300% Follow Rate**, **+0.963% Collect Rate**, **+0.221% Comment Rate** (\\(p < 0.05\\)) [6].
    * *`ItemA2C-W (\alpha=1)` vs. `ItemA2C`:* Additional **+0.451% Like Rate**, **+0.636% Follow Rate**, **+0.616% Collect Rate**, **+0.258% Comment Rate** [6].
    * *Macro Platform Metrics:* Generated a **+0.028% increase in Daily Active Users (DAU)** and a **+0.016% increase in 7-day User Retention** [7].

---

💡 *Would you like to explore how ItemA2C's advantage formulation or adversarial future-impact reweighting (\\(w_{t,k}\\)) can be adapted to structure per-swipe retention credit labels for your ranking pipeline?*

---

### Modeling User Retention through Generative Flow Networks [1]
`2024_KDD_GFN4Retention_Modeling-User-Retention.md`
**Source:** https://arxiv.org/pdf/2406.06043.pdf  

### **Source Evaluation: GFN4Retention (*Modeling User Retention through Generative Flow Networks*)**
*(Liu et al., City University of Hong Kong & Kuaishou Technology, KDD 2024: `arxiv:2406.06043`)* [1, 2]

---

### **(A) Query Categorization: Q1 vs. Q2**
* **Answer:** **Neither Q1 nor Q2.**
* **Explanation:** 
  * *Q1 (Industry Attribution 2025–2026):* Published in August 2024 (KDD ’24), which falls outside the 2025–2026 timeframe [2, 3].
  * *Q2 (Interaction-Level Retention Attribution):* Focuses on generative flow policy optimization for session-wise recommendations rather than multi-touch causal sequence attribution over historical user journey logs [6–9].

---

### **(B) Q2 Class**
* **Classification:** **NOT**
* **Justification:** The paper presents a Generative Flow Network (GFN) reinforcement learning framework that optimizes session trajectory generation by back-propagating terminal retention flows via Detailed Balance loss [8–10, 20, 26]. It does **not** publish an explicit per-exposure retention credit table or multi-touch attribution model [6–8].

---

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Yes (via step-wise probabilistic flow matching / Detailed Balance loss)** [4-7].
* **Target Outcome & Formula:** Combines the delayed terminal session retention reward \\(\mathcal{R}\\) (reciprocal user return time gap between consecutive sessions) with non-discounted immediate engagement rewards \\(r_t = \sum \omega_b y_{t,b}\\) (clicks, likes, watch time) via an integrated multiplicative reward product [8-10]:
  \\[R(\mathcal{S}) = \mathcal{R} \cdot e^{\alpha \sum_{t=1}^{T-1} r_t}\\]
  The Detailed Balance loss (\\(\mathcal{L}_{\text{DB}}\\)) back-propagates this integrated terminal reward across intermediate recommendation steps \\(t \in \{1, \dots, T-1\}\\) [22–26]:
  \\[\mathcal{L}_{\text{DB}} = \left( \log \mathcal{F}_{\mathcal{R}}(s_t) + \log P_F(s_{t+1}|s_t) - \log \mathcal{F}_{\mathcal{R}}(s_{t+1}) - \log P_B(s_t|s_{t+1}) - \alpha r_t \right)^2\\]

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**
* **How it Improves Last-Touch:** Last-touch heuristically assigns 100% of an N7 retention label to the final swipe before Day 7. GFN4Retention models a user's swiping session as a generative flow trajectory \\(\mathcal{S} = \{s_1 \to s_2 \to \dots \to s_T\}\\) [4, 11, 12]. Its flow-matching Detailed Balance objective propagates the terminal session retention reward \\(\mathcal{R}\\) backward to intermediate steps, crediting each interaction based on both immediate session engagement \\(r_t\\) and future retention flow \\(\mathcal{F}_{\mathcal{R}}(s_{t+1})\\) [4-7].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Immediate Step Reward (\\(r_t\\)):* Formulated as a weighted sum of immediate in-app engagement events:
     \\[r_t = w_1 \cdot \mathbb{1}[\text{swipe\_right}] + w_2 \cdot \mathbb{1}[\text{match}] + w_3 \cdot \mathbb{1}[\text{4-way\_conversation}]\\]
  2. *Session Retention Reward (\\(\mathcal{R}\\)):* Set to the user's reciprocal return time or 7-day retention indicator \\(\mathbb{1}[\text{active on Day 7}]\\) [8, 13].
  3. *Step Flow Matching (\\(\mathcal{F}_{\mathcal{R}}(s_t)\\)):* Back-propagates the N7 retention signal across every swipe, match, and messaging step in the session using Detailed Balance loss [6, 7]. Early candidate swipes and mutual matches that lead to high downstream messaging engagement and retention receive appropriate fractional credit alongside the final swipe [4-7].

---

### **(E) Selection-Bias & Confounding Handling**
1. **Context-Detection Module:** Combines user static features \\(\mathbf{A}_u\\) and Transformer-encoded interaction history \\(\mathbf{H}_{u,t}\\) with a DNN context-detection module (producing embedding \\(\psi_u\\)) to capture dynamic user activity patterns [14].
2. **Generative Flow Exploration:** Generative Flow Networks sample trajectory generation policies proportional to terminal rewards (\\(P(\mathcal{S}) \propto R(\mathcal{S})\\)), overcoming the exploration-exploitation trade-offs and variance instability suffered by standard RL algorithms (e.g., TD3, SAC) on sparse retention signals [6–8, 11, 20].
3. *Note:* The paper does not utilize propensity score weighting (IPW), counterfactual estimation, or explicit selection-bias debiasing.

---

### **(F) Deployment and Dataset Evidence**
* **Production Deployment:** Deployed live on Kuaishou's short-video platform serving **billions of daily user requests** across candidate pools of **several million videos** [13, 15]. Deployed in the ranking score ensemble modules across two distinct multi-stage ranking pipelines (1st Ranking Stage and 2nd Ranking Stage) holding out 10% online traffic vs. 20% baseline [13, 15].
* **Datasets (Evaluated in KuaiSim Retention Simulator):**
  * **KuaiRand-Pure:** Unbiased sequential recommendation dataset (27,285 users, 7,551 items, 1,436,609 interactions, 0.70% density) [16, 17].
  * **MovieLens-1M:** 6,400 users, 3,706 items, 1,000,208 interactions (4.22% density) [16, 17].
* **Quoted Quantitative Results:**
  * **Offline Simulator Performance (KuaiRand-Pure, Table 2):**
    * *Return Time:* GFN4Retention = **1.496** vs. RLUR (**1.786**), CEM (**1.889**), DIN (**1.947**), SAC (**2.373**), TD3 (**2.382**) — **lowest return time** (\\(p < 0.05\\)) [18].
    * *Retention Score:* GFN4Retention = **0.163** vs. RLUR (**0.159**), CEM (**0.156**), DIN (**0.154**), TD3 (**0.151**), SAC (**0.150**) — **highest retention** (\\(p < 0.05\\)) [18].
    * *Immediate Engagement:* Click Rate = **0.805** (vs. SAC 0.801), Like Rate = **0.862** (vs. SAC 0.857) [18].
  * **Offline Simulator Performance (MovieLens-1M, Table 2):**
    * *Return Time:* GFN4Retention = **1.479** vs. RLUR (**1.723**), CEM (**1.814**), DIN (**1.893**), SAC (**2.246**), TD3 (**2.258**) (\\(p < 0.05\\)) [19].
    * *Retention Score:* GFN4Retention = **0.165** vs. RLUR (**0.160**), CEM (**0.158**), DIN (**0.153**) (\\(p < 0.05\\)) [19].
  * **Live Online A/B Test Lifts (Table 3, Kuaishou Platform):**
    * *1st Ranking Stage:* **+0.015% overall next-day retention** (\\(p < 0.05\\)), **+0.069% target low-activity user next-day retention** (\\(p < 0.05\\)), and **+0.558% watch time** (\\(p < 0.05\\)) [13, 20].
    * *2nd Ranking Stage:* **+0.002% overall next-day retention**, **+0.056% target low-activity user next-day retention** (\\(p < 0.05\\)), and **+0.224% watch time** (\\(p < 0.05\\)) [13, 20].
  * **Ablation Study Impacts (KuaiRand-Pure, Section 4.6):**
    * *Removing Context Detection (`NCD`):* **+6.7% increase in return time** [21].
    * *Removing Immediate Feedback (`NIF`):* **-45% drop in click rate**, **-5% drop in like rate**, and **+4.7% increase in return time** [21].
    * *Simplified Terminal Feedback (`SIF`):* **-40% drop in click rate**, **-4% drop in like rate**, and **+4% increase in return time** compared to full GFN4Retention [21].

---

💡 *Would you like to explore how GFN4Retention's Detailed Balance loss (\\(\mathcal{L}_{\text{DB}}\\)) or integrated reward formulation could be adapted to structure per-swipe retention credit labels for your dating platform?*

---

