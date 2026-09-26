# A Self-Triggered Agentic Push Recommendation System [1]

**Source:** https://arxiv.org/pdf/2608.01949.pdf  
**Date analyzed:** 2026-09-24  
**NLM source id:** `9419d0b9-b40e-4e9c-8b49-5f24c45408ec`  
**Queue id:** G30  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *A Self-Triggered Agentic Push Recommendation System* [1]
* **Authors:** **Zhao-Yu Zhang**\*, **Qingying Chen**\*, **Chunyuan Zheng**\*, **Jing Zhou**, **Jian Sun**, **Siqi Chen**, **Leiying Chen**, **Chuan Zhou**, **Huiyou Jiang**†, **Xin Tao**, **Haoxuan Li**, and **Zhouchen Lin** (\*Equal contribution, †Corresponding author) [2, 3]
* **Affiliations:** **ByteDance** (Beijing, China) and **Peking University** (Beijing, China) [2]
* **Year & Venue:** Published in **2026** at the *20th ACM Conference on Recommender Systems (RecSys ’26)*, September 27–October 2, 2026, Minneapolis, MN, USA [3–4]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Large-scale mobile push notification systems face a complex "whether and when" delivery problem under strict system resource constraints and high QPS [4, 5]. Existing industrial solutions suffer from rigid paradigms:
  1. *Pre-planned frequency methods:* Calculate delivery schedules offline via uplift modeling and integer programming, lacking real-time context adaptability [6–7, 10].
  2. *Fixed-interval triggering methods:* Periodically poll the system at fixed intervals, creating a severe trade-off between excessive computational overhead and missing optimal delivery moments [6–7, 10].
* **Key Contribution:**
  * **STEPS Framework:** Introduces a proactive, **Self-Triggered End-to-end Agentic Push Recommendation System** that reformulates push optimization as a closed-loop agentic process where the system decides both whether to send a push and when to activate itself next [2, 8–9].
  * **Three-Agent System Architecture:**
    1. *Planning Agent:* Uses a Decision Transformer with a novel **Gated-RTG mechanism** and **Gated Ordinal Regression** (\\(K=100\\) equal-frequency buckets) to generate the continuous time gap \\(\Delta t\\) for the next system invocation [2, 18–19].
    2. *Execution Agent:* Uses a Decision Transformer with **Bellman RTG value-guided learning** to decide whether to send a push based on user trajectory rewards [2, 20–22].
    3. *Filtering Agent:* A lightweight 3-layer MLP operating solely on user and environment features (omitting item features) to prune low-potential requests before invoking compute-heavy item-sorting pipelines [4, 6].
  * **Billion-Scale Industrial Impact:** Fully deployed live on **Douyin** serving >1 billion users, significantly driving long-term re-engagement while slashing system resource consumption [4, 7].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Architectural Components**
* **Planning Agent (\\(\pi_P\\)):**
  * Inputs user/environment state \\(s_t\\) and target Return-to-Go (\\(R_t\\)) [8].
  * *Gated-RTG Mechanism:* Upscales scalar \\(R_t\\) via MLP and modulates state embeddings via element-wise multiplication (\\(e_{\text{gated}} = e_s \odot \text{MLP}(R_t)\\)) to prevent high-dimensional state features from overwhelming the condition signal [8].
  * *Ordinal Regression:* Discretizes continuous time gaps \\(\Delta t \in (0, 24\text{h}]\\) into \\(K=100\\) equal-frequency buckets, predicting probabilities \\(z_k = P(\Delta t > \tau_k)\\) optimized via BCE loss \\(\mathcal{L}_{\text{next}}\\) [18–19].
* **Execution Agent (\\(\pi_A\\)):**
  * Evaluates \\(s_t\\) and \\(R_t\\) at activation time to output a binary decision \\(a_t \in \{0, 1\}\\) [9, 10].
  * *Bellman Value-Guided Learning:* Learns action-value functions \\(Q(s_t, a_t \mid \lambda_n)\\) via Bellman equation / MSE loss \\(\mathcal{L}_Q\\) over positive/negative RTG trajectories (\\(R_t = R_t^+ - \lambda_n R_t^-\\)), reweighting action policy loss \\(\mathcal{L}_\pi\\) with advantage weights \\(w_t = \text{Sigmoid}(\alpha_r (Q(s_t, a_t) - Q(s_t, 1-a_t)))\\) [20–22].
* **Filtering Agent:**
  * Distills downstream execution knowledge into a 3-layer MLP using user and environment features only [6].
  * Bypasses the 10\\(\times\\) more expensive downstream item recall, pre-ranking, and ranking stages for low-value requests [6].

#### **Credit Assignment Mechanics**
* **No Multi-Touch Sequence Attribution:** Does **not** perform multi-touch sequence attribution or per-item fractional credit assignment across past user interaction logs.
* **Trajectory-Level Step Credit:** Credit is assigned at the **trajectory step level** using Return-to-Go (\\(R_t = \sum_{j=t}^T (r_j^+ - \lambda_n r_j^-)\\)) with Bellman Q-value iteration over user active days (\\(r_t^+ = 1\\) if user becomes active) and notification disablement (\\(r_t^-\\)) [13–14, 20–21].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets & Scale:** Offline logs spanning >6 months of production data from over **1 billion Douyin users** [27–28].
* **Production Deployment:** Fully deployed live in production on **Douyin** (>1 billion users) for a **14-day online A/B test** with completely randomized user device assignments, handling millions of QPS [4, 7, 11, 12].
* **Comparison Baselines:**
  * **Pre-Planned Frequency:** Previous production baseline at Douyin (offline uplift modeling + integer programming solver under global budget) [12, 13].
  * **Fixed-Interval Triggering:** Industrial Decision Transformer model periodically polling at fixed short time intervals [12, 13].

---

### **(5) Key Quantitative Results with Numbers**

* **Live Production Online A/B Test Results vs. Pre-Planned Baseline (Table 1):**
  * **User Active Days (UAD):** **+0.2843%** relative increase (vs. Fixed-Interval Triggering at **-0.0670%**) [3, 14, 15].
  * **Negative Experience (NE / Push Disablement):** **-1.9089%** reduction (vs. Fixed-Interval at **+0.0205%**) [3, 14, 15].
  * **Resource Consumption:** **-79.42%** reduction in computational overhead (vs. Fixed-Interval at **+6.548%**) [3, 14, 15].
* **Agent Component Ablation Study (Table 2):**
  * *Planning Agent alone:* **+0.1808% UAD**, **-0.9781% NE**, **-4.54% Resource** [31–32].
  * *Execution Agent addition:* **+0.1035% UAD**, **-0.6843% NE** [31–32].
  * *Filtering Agent addition:* **-0.2465% NE**, **-74.88% Resource** [31–32].
* **Inter-Push Gap & Sending Behavior (Table 4 & Table 5):**
  * Extreme short-interval push clusters (0–20 min) dropped by **-35.93%**, while well-spaced gaps (3–6 h) increased by **+179.84%** [16].
  * Moderate daily push volume (1–20 sends/day) increased by **+20.31%**, while extreme sends (>30 sends/day) dropped by **-9.30%** [17].
* **Downstream Pass Rates (Table 3):**
  * Filtering agent pass rate increased by **+12.3%**, execution agent pass rate increased by **+2.3%** [16].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Failure of Naive Feature Concatenation (Feature Overwhelming):** Standard Decision Transformers with naive RTG feature concatenation failed completely (correlation ratio between predicted gap and target RTG fluctuated randomly around 1.0), as high-dimensional state embeddings overwhelmed the 1D RTG scalar. Gated-RTG was strictly required to achieve stable condition-action alignment (correlation ratio ~1.8) [18, 33–34].
2. **Extreme Compute Overhead of Item Sorting:** The execution agent per 1k requests consumes **>50\\(\times\\) more compute** than the filtering agent (57.72 vs 1.00 relative cost) due to item recall/ranking pipelines. Skipping early-stage filtering would render the agentic system computationally unviable at massive QPS [6, 18].
3. **Instability of Upstream Critic/Q-Learning:** Introducing a critic into the upstream planning agent caused severe instability and reward hacking under high continuous-time prediction noise; value-guided learning was strictly restricted to the binary execution agent [19].
4. **Disproportionate Value Loss at Coarse Filter Thresholds:** Over-filtering with an average trigger gap of 60 minutes caused a sharp collapse in UAD gains; a conservative minute-scale threshold was required to preserve user value [38–39].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Chen et al. (2021) [Ref 8]:** *Decision Transformer: Reinforcement Learning Via Sequence Modeling* (NeurIPS '21) [20].
2. **Janner, Li, & Levine (2021) [Ref 13]:** *Offline Reinforcement Learning as One Big Sequence Modeling Problem* (Trajectory Transformer, NeurIPS '21) [21].
3. **Yancey & Settles (2020) [Ref 32]:** *A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications* (KDD '20) [22].
4. **Gupta et al. (2016) [Ref 10]:** *Email Volume Optimization at LinkedIn* (KDD '16) [23].
5. **Gao et al. (2025) [Ref 9]:** *Generative Auto-Bidding With Value-Guided Explorations* (GAVE, SIGIR '25) [20].
6. **Yamagata, Khalil, & Santos-Rodriguez (2023) [Ref 31]:** *Q-Learning Decision Transformer: Leveraging Dynamic Programming for Conditional Sequence Modelling in Offline RL* (ICML '23) [22].
7. **Zhao et al. (2018) [Ref 36]:** *Notification Volume Control and Optimization System at Pinterest* (KDD '18) [24].

---

💡 *Would you like to explore how STEPS's Gated-RTG mechanism or ordinal time-gap generation could be adapted to optimize notification timing and user re-engagement for your dating app?*

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

### **Source Evaluation: *A Self-Triggered Agentic Push Recommendation System***  
*(Zhang et al., ByteDance & Peking University, RecSys ’26, September 2026)* [1, 2]

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**

**Neither.** [3-5]
* **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** While published in RecSys 2026 and deployed in live production at Douyin, STEPS is a **proactive agentic push notification recommendation system** (comprising Decision Transformer-based Planning, Execution, and Filtering Agents) designed to optimize delivery timing and notification decisions [2–3, 8–9]. It is not an industry multi-touch attribution (MTA) measurement system.
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** STEPS determines "whether and when" to deliver push notifications using generative RL (Decision Transformer) to maximize long-term re-engagement (User Active Days, UAD) and minimize permission disablements (Negative Experience, NE) [2, 13–14]. It does not attribute user retention or active days back to individual past in-app interaction touchpoints (such as swipes or messages) across historical logs.

---

### **(B) Q2 Class**

**NOT.** [2, 13–16]
* **Justification:** STEPS is a generative RL decision-transformer policy optimization framework for push notification delivery and activation scheduling [2, 8, 16–17]. It does **not** produce or publish a per-exposure or per-touchpoint retention credit table.

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction sequence attribution credit table.**
* **Target Outcome:** Measures and optimizes **User Active Days (UAD)** (user re-engagement / active days) and **Negative Experience (NE)** (push permission disablement rate) via trajectory Return-to-Go (\\(R_t = \sum_{j=t}^T (r_j^+ - \lambda_n r_j^-)\\)) with Bellman value-guided learning [3, 13–14, 20–22].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**

* **How it Improves/Informs Product Strategy:** STEPS is not a post-hoc attribution model, but a **proactive closed-loop agentic framework** for re-engagement timing and delivery [3, 5]. It replaces rigid pre-planned offline schedules or wasteful fixed-interval polling with a Decision Transformer setup [3, 6]:
  1. *Planning Agent (\\(\pi_P\\)):* Predicts the optimal next system invocation time gap \\(\Delta t \in (0, 24\text{h}]\\) via gated ordinal regression over \\(K=100\\) equal-frequency buckets [2, 18–19].
  2. *Filtering Agent:* A 3-layer MLP operating on user/environment features (omitting heavy candidate profile features) to prune low-potential requests before invoking expensive recall and ranking pipelines [7, 8].
  3. *Execution Agent (\\(\pi_A\\)):* Evaluates real-time candidate items to make a binary decision \\(a_t \in \{0, 1\}\\) via Bellman value-guided learning [2, 20–22].
* **Dating Platform Mapping (Swipe / Match / Conversation / Push):**
  * *State (\\(s_t\\)):* Encodes user swiping history, match activity, messaging status, time since last app open, and environmental context [9, 10].
  * *Planning Agent:* Schedules the next optimal re-engagement trigger (\\(\Delta t\\)) based on trajectory RTG (e.g., waiting longer if a user was recently active, or scheduling an alert when a match/message is pending) [10, 11].
  * *Filtering Agent:* Prunes low-value re-engagement checks before invoking compute-heavy profile candidate recall and ranking pipelines, saving ~75% in compute [7, 8].
  * *Execution Agent:* Evaluates real-time candidate matches or chat reminders to output binary push decisions (\\(a_t \in \{0, 1\}\\)) [11, 12].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Bellman Value-Guided Learning:** Resolves offline log suboptimality and behavioral distribution shifts by learning action-value functions \\(Q(s_t, a_t \mid \lambda_n)\\) via the Bellman equation over trajectory rewards (\\(R_{t+1}\\)), rather than directly regressing policy on observed offline RTG (which suffers from historical action bias) [20–22].
2. **Gated-RTG Mechanism:** Solves the "condition-ignoring" / feature-overwhelming problem in Decision Transformers where high-dimensional state embeddings overwhelm the 1D scalar RTG signal, using element-wise gating \\(e_{\text{gated}} = e_s \odot \text{MLP}(R_t)\\) to achieve stable condition-action alignment [18, 33–34].
3. **Equal-Frequency Ordinal Discretization (\\(K=100\\)):** Replaces standard regression over long-tailed, non-Gaussian continuous time gaps with ordinal regression across equal-mass buckets [18–19].

---

### **(F) Deployed or Production Dataset Evidence**

* **Production Deployment:** Fully deployed live in production on **Douyin** serving over **1 billion users** for a **14-day online A/B test** with completely randomized user device assignments [3, 13].
* **Quoted Numbers from the Source:**
  * **Scale:** Trained on >6 months of production logs from over **1 billion Douyin users** [2, 27–28].
  * **Live Online A/B Test Results vs. Pre-Planned Baseline (Table 1 & Abstract):**
    * **User Active Days (UAD):** **+0.2843%** relative increase (vs. Fixed-Interval Triggering at **-0.0670%**) [7, 14, 15].
    * **Negative Experience (NE / Push Disablement):** **-1.9089%** reduction (vs. Fixed-Interval Triggering at **+0.0205%**) [7, 14, 15].
    * **Resource Consumption:** **-79.42%** reduction in overall computational cost (vs. Fixed-Interval Triggering at **+6.548%**) [7, 14, 15].
  * **Ablation Study Contributions (Table 2):**
    * *Planning Agent alone:* **+0.1808% UAD**, **-0.9781% NE**, **-4.54% Resource** [31–32].
    * *Execution Agent addition:* **+0.1035% UAD**, **-0.6843% NE** [31–32].
    * *Filtering Agent addition:* **-0.2465% NE**, **-74.88% Resource** [31–32].
  * **Inter-Push Gap Changes (Table 4):** Extreme short-interval push clusters (0–20 min) dropped by **-35.93%**, while well-spaced intervals (3–6 h) increased by **+179.84%** [16].
  * **User-Level Daily Sends (Table 5):** Moderate sends (1–20/day) increased by **+20.31%**, frequent sends (21–30) dropped by **-6.87%**, extreme sends (>30) dropped by **-9.30%**, zero-send cases dropped by **-4.06%** [17].
  * **Downstream Pass Rates (Table 3):** Filtering agent pass rate increased by **+12.3%**, execution agent pass rate increased by **+2.3%** [16].
  * **Resource Overhead per 1k Requests (Table 6):** Filtering agent = **1.00**, Planning agent = **1.27**, Execution agent = **57.72** (over **50\\(\times\\) more expensive** due to candidate item sorting) [18].
  * **Filtering Request Drop Rates (Table 7):** Overall request drop rate = **74.88%** (pruning **78.86%** on inactive users and **85.65%** on fully-active users) [15, 19].

---

💡 *Would you like to explore how STEPS's Gated-RTG mechanism or ordinal time-gap generation could be adapted to optimize notification timing and user re-engagement for your dating app?*

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
**Priority:** see queue.md `G30`
