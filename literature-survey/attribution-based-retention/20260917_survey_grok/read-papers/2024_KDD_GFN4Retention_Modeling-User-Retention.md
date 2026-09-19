# Modeling User Retention through Generative Flow Networks [1]

**Source:** https://arxiv.org/pdf/2406.06043.pdf  
**Date analyzed:** 2026-09-18  
**NLM source id:** `1000111e-44ac-4cc3-a39f-584e06ac7da6`  
**Queue id:** G8  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**
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
**Priority:** see queue.md `G8`
