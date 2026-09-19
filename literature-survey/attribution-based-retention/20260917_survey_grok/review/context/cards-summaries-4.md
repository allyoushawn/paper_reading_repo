# Card summaries 4/12 — Summary and Evidence sections of all cards (generated)

### **Part 1: Dating App Retention Project Evaluation**
`2024_KDD_FID_Future-Impact-Decomposition.md`
**Source:** https://arxiv.org/pdf/2401.16108.pdf  

**Summary.** ### **Part 1: Dating App Retention Project Evaluation**

#### **(A) Alignment: Q1 or Q2 or Both or Neither?**
* **Answer:** **Neither Q1 nor Q2** [1, 6–7].
* **Explanation:** 
  * *Q1 (Industry Attribution 2025–2026):* Published in August 2024 (KDD ’24), falling outside the 2025–2026 window [6–7].
  * *Q2 (Interaction-Level Retention Attribution):* Focuses on reinforcement learning (RL) policy optimization for list-wise recommendations rather than multi-touch causal attribution over historical user journey logs [8–12, 18].

---

#### **(B) Q2 Classification**
* **Classification:** **NOT** [15, 21–23, 31–36].
* **Justification:** The paper presents an RL actor-critic policy optimization method (**ItemA2C**) that decomposes list-level future value \\(V(s_{t+1})\\) down to individual items for policy gradient updates, rather than publishing an explicit per-exposure retention credit table or multi-touch attribution model [15–18, 35–41].

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Yes (in the form of an RL item-level advantage score)** [1-3]. 
* **Target Outcome & Formula:** Allocates cumulative session rewards and long-term state value \\(V(s_{t+1})\\) (which correlates with 7-day retention) to individual items \\(i_{t,k}\\) in list \\(a_t\\) via item target value \\(\Psi_w\\) and advantage \\(A\\):
  \\[\Psi_w(s_t, i_{t,k}) = r_{t,k} + w_{t,k} \gamma (1-d) V(s_{t+1})\\]
  \\[A(s_t, i_{t,k}, w_{t,k}) = \Psi_w(s_t, i_{t,k}) - \frac{V(s_t)}{K}\\]
  where \\(r_{t,k}\\) is the immediate item reward, \\(V(s_{t+1})\\) is the estimated future state value, and \\(w_{t,k}\\) is a reward-based or model-based item weight (\\(\sum_{k=1}^K w_{t,k} = 1\\)) [36, 39, 41, 47–48].

---

#### **(D) Improving on Last-Touch N7 → Latest Swipes**
* **How it Improves Last-Touch:** Last-touch assigns binary N7 labels exclusively to the most recent swipes, ignoring earlier swipes and intermediate value creation. **ItemA2C** provides a mathematically grounded RL framework to decompose long-term value \\(V(s_{t+1})\\) (which directly drives N7 retention) across all candidate recommendations in a session based on immediate engagement signals \\(r_{t,k}\\) and learned future impact weights \\(w_{t,k}\\) [15, 36–39].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Immediate Item Reward (\\(r_{t,k}\\)):* Formulated as a weighted sum of immediate candidate interaction events:
     \\[r(s_t, \text{candidate}_k) = w_1 \cdot \mathbb{1}[\text{swipe\_right}] + w_2 \cdot \mathbb{1}[\text{match}] + w_3 \cdot \mathbb{1}[\text{4-way\_conversation}]\\]
  2. *Value Function (\\(V(s_{t+1})\\)):* Estimates the user's expected cumulative long-term engagement / retention probability given their updated profile state \\(s_{t+1}\\) after the swiping session [31–32].
  3. *Item Credit Allocation (\\(w_{t,k}\\)):* Uses reward-based weighting (\\(w_{t,k} = r_{t,k} / R\\)) or adversarial model-based weighting (\\(w_{t,k} = w(i_{t,k}, s_t, s_{t+1}, r_{t,k})\\)) to assign fractional credit for \\(V(s_{t+1})\\) to each candidate profile shown [39, 43–45].

---

#### **(E) Selection-Bias & Confounding Handling**
1. **Critic Baseline Subtraction (Advantage Formulation):** Subtracts the mean expected state baseline \\(V(s_t)/K\\) from the item target value \\(\Psi_w(s_t, i_{t,k})\\) to compute the item advantage \\(A(s_t, i_{t,k}, w_{t,k})\\), preventing naturally hyper-active users (who have high baseline \\(V(s_t)\\)) from inflating individual item scores [3, 4].
2. **Quantile Normalization:** Uses quantile-based discretization for continuous engagement signals (e.g., watch time) to prevent extreme outlier sessions from skewing reward distributions [5].

---

#### **(F) Deployment and Dataset Evidence**
* **Datasets & Deployment:** Evaluated offline on MovieLens-1M (ML1M), KuaiRand1K, and the KuaiSim simulator [50–52]. Deployed live in the **refined ranking stage** (ranking ~500 candidates down to \\(K=6\\)) of Kuaishou's short-video platform serving **over 100 million Daily Active Users (DAU)** [75–78, 81].
* **Quoted Quantitative Results:**
  * **Offline Simulator (KuaiRand1K, \\(K=6\\), Table 1):** `ItemA2C-M` achieved **Total Reward = 16.03 ± 0.53** and **Depth = 16.59 ± 0.45** vs. standard request-level `A2C` (**10.01 ± 0.86 / 11.56 ± 0.72**) and state-of-the-art `HAC` (**12.65 ± 0.26 / 13.72 ± 0.22**), representing a **+26.7% reward increase** (\\(p < 0.05\\)) [55–56, 64].
  * **Live Production A/B Test (Table 3, 100M+ DAU Platform):**
    * *`ItemA2C` vs. `request-level A2C`:* **+0.129% Watch Time**, **+1.103% Like Rate**, **+0.300% Follow Rate**, **+0.963% Collect Rate**, **+0.221% Comment Rate** (\\(p < 0.05\\)) [6].
    * *`ItemA2C-W (\alpha=1)` vs. `ItemA2C`:* Additional **+0.451% Like Rate**, **+0.636% Follow Rate**, **+0.616% Collect Rate**, **+0.258% Comment Rate** [6].
    * *Macro Platform Impact:* Generated a **+0.028% increase in Daily Active Users (DAU)** and a **+0.016% increase in 7-day User Retention** [7].

---

### **Part 2: Detailed Technical Breakdown of the Source**

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Full Title:** *Future Impact Decomposition in Request-level Recommendations* [8, 9]
* **Authors:** **Xiaobei Wang**\*†, **Shuchang Liu**\*, **Xueliang Wang**, **Qingpeng Cai**‡, **Lantao Hu**, **Han Li**, **Peng Jiang**‡, **Kun Gai**, and **Guangming Xie**‡ (\*Equal contribution; †Work done during internship at Kuaishou; ‡Corresponding authors) [8, 9]
* **Author Affiliations:**
  1. **Peking University**, Beijing, China (`wangxiaobei@stu.pku.edu.cn`, `xiegming@pku.edu.cn`) [1–2]
  2. **Kuaishou Technology**, Beijing, China (`{liushuchang, wangxueliang03, caiqingpeng, hulantao, lihan08, jiangpeng}@kuaishou.com`) [1–2]
  3. **Unaffiliated**, Beijing, China (`gai.kun@qq.com`) [10]
* **Year & Venue:** Published in **2024** at the *30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD ’24), August 25–29, 2024, Barcelona, Spain* [6–7].

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** In recommender systems, reinforcement learning (RL) policies typically recommend a *list* of \\(K\\) items per request to efficiently process continuous user browsing [2–3, 10]. In the corresponding Markov Decision Process (MDP), user state transitions are updated at the *request level* [3, 11–12]. However, this list-wise mechanism is fundamentally inconsistent with individual user behaviors (users pay attention to one item at a time, and state transitions occur per item) [11, 12]. Standard request-level RL methods optimize cumulative list-wise rewards, inducing severe information loss on item characteristics and failing to distribute an item's future impact properly [1, 13].
* **Key Contributions:**
  1. **Request-Level MDP with Item-Wise Rewards:** Formulates a practical request-level MDP framework where state transitions occur per request but item-level immediate rewards are observable [12–13, 18, 27–31].
  2. **ItemA2C Framework:** Proposes an item-decomposed advantage actor-critic framework (**ItemA2C**) that decomposes both temporal difference (TD) critic targets and actor advantage objectives into item-level optimizations [15, 35–37].
  3. **Future Impact Reweighting:** Introduces heuristic **reward-based re-weighting** (`itemA2C-W`) and **model-based adversarial re-weighting** (`itemA2C-M`) to allocate long-term future value \\(V(s_{t+1})\\) across individual items in a list rather than splitting it uniformly [16–18, 38–46].
  4. **Mathematical Consistency:** Proves that the item-wise target function sums up to reconstruct the original request-level TD target (\\(\sum_{k=1}^K \Psi_w(s_t, i_{t,k}) = \Psi(s_t, a_t)\\)), ensuring theoretical consistency [18, 47–48].

---

#### **(3) Proposed Method or Architecture in Detail**
* **MDP Formulation:** Action \\(a_t = [i_{t,1}, \dots, i_{t,K}] \in \mathcal{I}^K\\). Immediate list reward \\(R(s_t, a_t) = \sum_{k=1}^K r_{t,k}\\) where item rewards \\(r_{t,k} = r(s_t, i_{t,k})\\) are observable [28–29].
* **Decomposed Item Target Function:**
  \\[\Psi_w(s_t, i_{t,k}) = r_{t,k} + w_{t,k} \gamma (1-d) V(s_{t+1})\\]
  where \\(w_{t,k}\\) determines how the future state value \\(V(s_{t+1})\\) is allocated across items in the list [2, 14].
* **Reweighting Schemes (\\(w_{t,k}\\)):**
  * *Equal-Weight Decomposition (`itemA2C`, \\(\alpha=0\\)):* \\(w_{t,k} = 1/K\\) [2, 14].
  * *Reward-Based Strategy (`itemA2C-W`):* \\(w_{t,k} = \frac{\alpha r_{t,k} + (1-\alpha)}{\alpha R(s_t, a_t) + (1-\alpha)K}\\). Setting \\(\alpha=1.0\\) yields pure reward-proportional weights \\(w_{t,k} = r_{t,k} / R(s_t, a_t)\\) [39–40].
  * *Model-Based Adversarial Strategy (`itemA2C-M`):* Paramterizes weights as a neural network \\(w_{t,k} = w(i_{t,k}, s_t, s_{t+1}, r_{t,k})\\) with softmax output across the list [43–44]. Trained via an adversarial objective \\(\mathcal{L}_{weight} = -\sum_{k=1}^K \mathcal{L}_{actor}(i_{t,k})\\), forcing the actor to learn from "harder" item decompositions [45–46].
* **Actor Loss Function:**
  \\[\mathcal{L}_{actor}(i_{t,k}) = -A(s_t, i_{t,k}, w_{t,k}) \log \pi_\theta(i_{t,k} | s_t)\\]
  \\[A(s_t, i_{t,k}, w_{t,k}) = \Psi_w(s_t, i_{t,k}) - \frac{V(s_t)}{K}\\]
* **Credit Assignment Mechanics:** Assigns credit to individual items \\(i_{t,k}\\) within a list/request \\(a_t\\) by splitting both immediate reward \\(r_{t,k}\\) and weighted long-term future value \\(w_{t,k} V(s_{t+1})\\). This evaluates each item's individual contribution to both short-term feedback and long-term user retention [2, 3, 14].

---

#### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets:**
  * **MovieLens-1M (ML1M):** 10-core filtered movie ratings dataset [15].
  * **KuaiRand1K:** Unbiased sequential short-video dataset [15].
  * **KuaiSim:** Session-based user simulator environment [16, 17].
* **Production Deployment:** Deployed in the **refined ranking stage** (ranking ~500 candidates down to list size \\(K=6\\)) of Kuaishou's short-video platform serving **100+ million Daily Active Users (DAU)** [75–78, 81].
* **Comparison Baselines:**
  * *Request-level RL:* DDPG (continuous vector hyper-actions), A2C (standard list-level A2C), HAC (Hyper-Action Representation + Actor-Critic) [55–58].
  * *Supervised Learning:* SASRec Transformer encoder + BCE loss [18, 19].
  * *Item-decomposed RL:* SlateQ (DQN slate decomposition under single-choice assumption) [18, 20, 21].

---

#### **(5) Key Quantitative Results with Numbers**
* **Offline Simulator Performance (KuaiRand1K, \\(K=6\\), Table 1):**
  * `itemA2C-M` achieved **Total Reward = 16.03 ± 0.53** and **Depth = 16.59 ± 0.45** vs. standard request-level `A2C` (**10.01 ± 0.86 / 11.56 ± 0.72**) and `HAC` (**12.65 ± 0.26 / 13.72 ± 0.22**), representing a **+26.7% reward gain** (\\(p < 0.05\\)) [55–56, 64].
  * `itemA2C-W (\alpha=1)` achieved **15.48 ± 0.61 Reward**; `itemA2C (\alpha=0)` achieved **13.45 ± 0.08 Reward** [22].
* **Offline Simulator Performance (ML1M, \\(K=6\\), Table 1):**
  * `itemA2C-M` achieved **Total Reward = 17.94 ± 0.47** and **Depth = 18.24 ± 0.40** vs. `HAC` (**17.53 ± 0.13 / 17.90 ± 0.12**) and `A2C` (**16.88 ± 0.58 / 17.32 ± 0.50**) [54–55].
* **Live Online A/B Test (Table 3, 100M+ DAU Short-Video Platform):**
  * *`ItemA2C` vs. `request-level A2C`:* **+0.129% Watch Time**, **+1.103% Like Rate**, **+0.300% Follow Rate**, **+0.963% Collect Rate**, **+0.221% Comment Rate** (\\(p < 0.05\\)) [6].
  * *`ItemA2C-W (\alpha=1)` vs. `ItemA2C`:* Additional **+0.451% Like Rate**, **+0.636% Follow Rate**, **+0.616% Collect Rate**, **+0.258% Comment Rate** [6].
  * *Macro Platform Metrics:* Driven a **+0.028% increase in Daily Active Users (DAU)** and a **+0.016% increase in 7-day User Retention** [7].

---

#### **(6) Limitations, Failure Modes, or Negative Results**
1. **SlateQ Failure under Multi-Interaction:** SlateQ performs poorly (Total Reward 3.39 on KuaiRand vs 16.03 for `itemA2C-M`) because its "single-choice" assumption fails when users engage with multiple items in a list [20, 22, 23].
2. **List Size Degradation:** As list size \\(K\\) increases (\\(K \in \{1, 2, 4, 6, 8, 16, 32\}\\)), performance of all methods gradually deteriorates (e.g., `itemA2C-M` reward drops from 16.93 at \\(K=1\\) to 11.39 at \\(K=32\\) on KuaiRand), confirming the growing mismatch between request-level MDPs and item-level user attention [24, 25].
3. **Model-Based Reweighting Training Overhead:** `itemA2C-M` introduces additional adversarial modeling and training overhead during offline policy learning (though zero extra compute during online inference) [84–85].
4. **Dependence on Linear Reward Additivity:** Assumes list-wise immediate reward is a linear sum of item-wise rewards (\\(R = \sum r\\)), which does not account for complex non-linear intra-list effects such as diversity [26, 27].
5. **Inability to Directly Serve Early Retrieval Stages:** Suited for refined ranking or re-ranking stages (\\(K\\) small); accommodating early retrieval/pre-ranking where candidate pools are huge and output size is not \\(K\\) requires additional modifications [81, 86–87].

---

#### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Ie et al. (2019) [SlateQ]:** *SlateQ: A Tractable Decomposition for Reinforcement Learning with Recommendation Sets* (IJCAI '19) [20, 28].
2. **Liu et al. (2023) [HAC]:** *Exploration and Regularization of the Latent Action Space in Recommendation* (WWW '23) [29, 30].
3. **Cai et al. (2023) [Two-Stage Constrained Actor-Critic / Retention RL]:** *Reinforcing User Retention in a Billion Scale Short Video Recommender System* & *Two-Stage Constrained Actor-Critic for Short Video Recommendation* (WWW '23) [9, 31-33].
4. **Mnih et al. (2016) [A2C / Asynchronous Actor-Critic]:** *Asynchronous methods for deep reinforcement learning* (ICML '16) [34, 35].
5. **Lillicrap et al. (2016) [DDPG]:** *Continuous control with deep reinforcement learning* (ICLR '16) [36, 37].
6. **Zhao et al. (2023) [KuaiSim] & Gao et al. (2022) [KuaiRand]:** *KuaiSim: A comprehensive simulator for recommender systems* & *KuaiRand: An Unbiased Sequential Recommendation Dataset* [16, 38-40].
7. **Kang & McAuley (2018) [SASRec]:** *Self-attentive sequential recommendation* (ICDM '18) [19].

---

💡 *Would you like to explore how to adapt ItemA2C's advantage formulation or adversarial future-impact reweighting (\\(w_{t,k}\\)) to construct an N7 retention ranking pipeline for your dating platform?*

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Modeling User Retention through Generative Flow Networks [1]
`2024_KDD_GFN4Retention_Modeling-User-Retention.md`
**Source:** https://arxiv.org/pdf/2406.06043.pdf  

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Modeling User Retention through Generative Flow Networks* [1]
* **Authors:** **Ziru Liu**†¹, **Shuchang Liu**†², **Bin Yang**², **Zhenghai Xue**³, **Qingpeng Cai**\*², **Xiangyu Zhao**\*¹, **Zijian Zhang**¹, **Lantao Hu**², **Han Li**², and **Peng Jiang**\*² (*†Co-first authors, \*Corresponding authors*) [1]
* **Author Affiliation:**
  1. **City University of Hong Kong**, Hong Kong, China [1]
  2. **Kuaishou Technology**, Beijing, China [1]
  3. **Nanyang Technological University**, Singapore [1]
* **Year:** **2024** (Published August 2024) [3–4]
* **Venue:** *Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD ’24), August 25–29, 2024, Barcelona, Spain* [3–4]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Standard recommender systems optimize for immediate item-level feedback (clicks, likes, watch time) [2]. However, these short-term metrics fail to capture long-term user satisfaction and retention (return-to-app behavior) [5–6]. Optimizing retention is difficult due to its between-session nature, delayed/sparse return signals, unobservable user activity between sessions, and the uncertain relationship between immediate item feedback and return time [3, 4]. Standard Reinforcement Learning (RL) approaches suffer from severe exploration-exploitation trade-offs and rely on cumulative immediate rewards as indirect surrogates without investigating step-wise retention credit ("retention attribution") [6–7].
* **Key Contribution:**
  1. **GFN4Retention Framework:** Introduces a Generative Flow Network (GFN) architecture for session-wise recommendation that directly models user retention as the probabilistic generation flow of a session trajectory [8–10].
  2. **Integrated Reward & Refined Detailed Balance Objective:** Formulates a combined reward structure multiplying terminal retention rewards by non-discounted cumulative immediate feedback rewards, deriving a refined Detailed Balance (DB) loss that back-propagates retention rewards to intermediate steps ("retention attribution") [8–9, 22–26].
  3. **Continuous Action Space Extension:** Extends GFN probabilistic flow matching from small discrete action spaces to continuous vector action spaces for list-wise item selection [9, 18, 58–59].
  4. **Empirical Validation:** Validates the framework using the KuaiSim retention simulator on two public benchmarks and proves scalability via live A/B tests on Kuaishou's industrial platform serving billions of daily requests [2, 28, 44–46].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Architectural Components**
1. **User State Encoding Module:** Processes user history \\(H_{u,t}\\) via a Transformer encoder and combines it with user static features \\(A_u\\) to generate embedding \\(e_u\\) [5]. Merges this with a DNN context-detection module embedding \\(\psi_u\\) to form the composite user state \\(s_t = [e_u, \psi_u]\\) [5].
2. **Recommendation Policy as Forward Flow (\\(P_F\\)):** Outputs Gaussian distribution parameters \\(\mu, \sigma = \phi_{\text{fw}}(s_t)\\) and samples continuous action vector \\(a_t \sim \mathcal{N}(\mu, \sigma)\\), which maps to a list of items via top-\\(K\\) deterministic selection [6].
3. **Flow Estimation & Backward Flow (\\(P_B\\)):** Uses neural network \\(\phi_{\text{bw}}(s_t, a_t, s_{t+1})\\) to model the backward posterior probability, while flow estimator \\(\mathcal{F}(s_t)\\) assesses state reachability likelihood [7].

#### **Integrated Reward & Refined Detailed Balance Loss**
* **Session Trajectory Reward Design:** Combines the delayed retention reward \\(\mathcal{R}\\) (reciprocal return time gap) with immediate rewards \\(r_t = \sum \omega_b y_{t,b}\\) via a multiplicative formulation [15, 22–23]:
  \\[R(\mathcal{S}) = \mathcal{R} \cdot e^{\alpha \sum_{t=1}^{T-1} r_t}\\]
* **Flow Estimator Decomposition:** Splits total state flow into a non-parametric immediate reward flow \\(\mathcal{F}_{\mathcal{I}}(s_t) = e^{\sum_{j=1}^{t-1} r_j}\\) and a learned retention flow \\(\mathcal{F}_{\mathcal{R}}(s_t)\\) [8]:
  \\[\mathcal{F}(s_t) = \mathcal{F}_{\mathcal{R}}(s_t) \cdot (\mathcal{F}_{\mathcal{I}}(s_t))^\alpha\\]
* **Refined Detailed Balance (DB) Loss:**
  \\[\mathcal{L}_{\text{DB}} = \begin{cases} \left( \log \mathcal{F}_{\mathcal{R}}(s_t) + \log P_F(s_{t+1}|s_t) - \log \mathcal{F}_{\mathcal{R}}(s_{t+1}) - \log P_B(s_t|s_{t+1}) - \alpha r_t \right)^2 & 1 \le t \le T-1 \\ \left( \log \mathcal{F}_{\mathcal{R}}(s_T) - \log \mathcal{R} \right)^2 & t = T \end{cases}\\]

#### **Credit Assignment Mechanics**
* Credit is assigned **per recommendation request/step** along the session trajectory [8, 25–26]. 
* The flow-matching Detailed Balance objective back-propagates the terminal session retention reward \\(\mathcal{R}\\) backwards step-by-step through intermediate state flows \\(\mathcal{F}_{\mathcal{R}}(s_t)\\) [9-11]. An increased action probability \\(P_F(a_t|s_t)\\) is explicitly conditioned on achieving higher immediate rewards \\(r_t\\) or higher future retention flow \\(\mathcal{F}_{\mathcal{R}}(s_{t+1})\\) [25–26].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets (Evaluated in KuaiSim Retention Simulator):**
  1. **KuaiRand-Pure:** Unbiased sequential recommendation dataset (27,285 users, 7,551 items, 1,436,609 interactions, 0.70% density) [12, 13]. Uses 6 positive feedback signals (click, view time, like, comment, follow, forward) and 2 negative signals (hate, leave) [14].
  2. **MovieLens-1M:** 6,400 users, 3,706 items, 1,000,208 interactions, 4.22% density (ratings \\(>3\\) treated as 'like', \\(\le 3\\) as 'hate') [29–30].
  3. **Simulator Setup:** Evaluated via KuaiSim simulator modeling session exit and daily return probability distributions [13].
* **Production Deployment:**
  * Deployed live on Kuaishou's short-video platform serving **billions of daily user requests** across candidate pools of millions of videos [15].
  * Integrated into the **ranking score ensemble modules** across two distinct multi-stage ranking pipelines (1st Ranking Stage and 2nd Ranking Stage) [15]. The model outputs action \\(a_t\\) as dynamic fusion weights combining candidate scores from multiple underlying prediction models [15].
* **Comparison Baselines:**
  * *Offline Baselines:* TD3, SAC, DIN, CEM, and RLUR (Reinforcing User Retention, Cai et al., 2023) [16].
  * *Online Baselines:* Fixed linear score combination (1st Stage) and RL score-search baseline (2nd Stage) [15].

---

### **(5) Key Quantitative Results with Numbers**
* **Offline Benchmark Metrics (Table 2):**
  * **KuaiRand-Pure:**
    * **Return Time:** GFN4Retention = **1.496** vs. RLUR (**1.786**), CEM (**1.889**), DIN (**1.947**), SAC (**2.373**), TD3 (**2.382**) — **lowest return time** (\\(p < 0.05\\)) [17].
    * **Retention Score:** GFN4Retention = **0.163** vs. RLUR (**0.159**), CEM (**0.156**), DIN (**0.154**), TD3 (**0.151**), SAC (**0.150**) — **highest retention** (\\(p < 0.05\\)) [17].
    * **Immediate Engagement:** Click Rate = **0.805** (vs. SAC 0.801), Like Rate = **0.862** (vs. SAC 0.857) [17].
  * **MovieLens-1M:**
    * **Return Time:** GFN4Retention = **1.479** vs. RLUR (**1.723**), CEM (**1.814**), DIN (**1.893**), SAC (**2.246**), TD3 (**2.258**) (\\(p < 0.05\\)) [18].
    * **Retention Score:** GFN4Retention = **0.165** vs. RLUR (**0.160**), CEM (**0.158**), DIN (**0.153**) [18].
* **Live Online A/B Test (Table 3, Kuaishou Platform):**
  * **1st Ranking Stage:** **+0.015% overall next-day retention** (\\(p < 0.05\\)), **+0.069% target low-activity user retention** (\\(p < 0.05\\)), and **+0.558% watch time** (\\(p < 0.05\\)) [45–46].
  * **2nd Ranking Stage:** **+0.056% target low-activity user retention** (\\(p < 0.05\\)) and **+0.224% watch time** (\\(p < 0.05\\)) [45–46].
* **Ablation Study (KuaiRand-Pure, Figure 5):**
  * Removing context detection (`NCD`): Causes a **+6.7% increase in return time** [19].
  * Removing immediate feedback (`NIF`): Drops click rate by **-45%**, like rate by **-5%**, and increases return time by **+4.7%** [19].
  * Simplified terminal feedback (`SIF`): Drops click rate by **-40%** and increases return time by **+4%** compared to full GFN4Retention [19].

---

### **(6) Limitations, Failure Modes, or Negative Results**
1. **Numerical Instability at Zero Probabilities:** Log-scale forward probabilities \\(\log P_F(\cdot)\\) approach negative infinity when probabilities drop near zero, causing gradient variance. Requires smoothing offsets (\\(\beta_F, \beta_B, \beta_r\\)) to maintain training stability [20].
2. **Sensitivity to Immediate Reward Weight (\\(\alpha\\)):** Setting \\(\alpha\\) too low (\\(\alpha=0.5\\)) causes a severe drop in click rate and increases return time; setting \\(\alpha\\) too high (\\(\alpha=1.5\\)) over-emphasizes immediate feedback, causing a **~2% drop in click rate** and degrading return time (Figure 6) [40–42].
3. **Absence of Intermediate Retention Signals:** Relies on the assumption that retention cannot be directly measured mid-session, forcing total dependence on back-propagating terminal session rewards \\(\mathcal{R}\\) [3, 4, 11].
4. **Continuous Vector Flow Approximation:** Generates Continuous Gaussian action vectors \\(a_t \sim \mathcal{N}(\mu, \sigma)\\) mapped via top-\\(K\\) selection, which relies on neural network functional approximations (\\(\phi_{\text{fw}}, \phi_{\text{bw}}, \mathcal{F}\\)) rather than exact tabular flow balances [18–19, 58–59].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Bengio et al. (2021, 2023) [GFN Foundations / GFlowNets]:** *Flow network based generative models for non-iterative diverse candidate generation* (NeurIPS '21) & *Gflownet foundations* (JMLR '23) [21, 22].
2. **Cai et al. (2023) [RLUR / Retention RL]:** *Reinforcing User Retention in a Billion Scale Short Video Recommender System* (WWW '23 Companion) [4].
3. **Liu et al. (2023) [GFN for Listwise Recommendation]:** *Generative flow network for listwise recommendation* (KDD '23) [23].
4. **Zhao et al. (2023) [KuaiSim Simulator]:** *KuaiSim: A comprehensive simulator for recommender systems* (NeurIPS '23) [24].
5. **Zhao et al. (2023) [Decision Transformer for Retention]:** *User Retention-oriented Recommendation with Decision Transformer* (WWW '23) [25].
6. **Fujimoto et al. (2018) [TD3] & Haarnoja et al. (2018) [SAC]:** *Addressing function approximation error in actor-critic methods* & *Soft actor-critic: Off-policy maximum entropy deep reinforcement learning* [8, 26].
7. **Cai et al. (2023) [Two-Stage Constrained Actor-Critic]:** *Two-Stage Constrained Actor-Critic for Short Video Recommendation* (WWW '23) [27].

---

💡 *Would you like to explore how GFN4Retention's flow-matching Detailed Balance loss (\\(\mathcal{L}_{\text{DB}}\\)) or integrated reward formulation could be adapted to back-propagate N7 retention credit across individual swiping sessions for your dating platform?*

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

