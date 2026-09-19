# Stratified Expert Cloning for Retention-Aware Recommendation at Scale [1]

**Source:** https://arxiv.org/pdf/2504.05628.pdf  
**Date analyzed:** 2026-09-18  
**NLM source id:** `d9a6d934-5dad-4efc-8e08-c62a0184f137`  
**Queue id:** G10  
**Q2 class:** NOT

---

## 1. Summary

### **1. Title, Authors, Affiliations, Year, Venue**
* **Title:** *Stratified Expert Cloning for Retention-Aware Recommendation at Scale* [1]
* **Authors:** **Chengzhi Lin**\*¹, **Annan Xie**\*², **Shuchang Liu**¹, **Wuhong Wang**¹, **Chuyuan Wang**¹, **Yongqi Liu**¹, and **Han Li**¹ (\*Equal contribution) [1]
* **Affiliations:** 
  1. **Kuaishou Technology**, Beijing, China (`1132559107@qq.com`, `{liushuchang, wangwuhong, wangchuyuan, liuyongqi, lihan}@kuaishou.com`) [1]
  2. **Peking University**, Beijing, China (`2301210470@stu.pku.edu.cn`) [1]
* **Year:** **2025** (Published November 2025) [2, 3]
* **Venue:** *Proceedings of the 34th ACM International Conference on Information and Knowledge Management (CIKM ’25), November 10–14, 2025, Seoul, Republic of Korea* [2, 3]

---

### **2. Core Problem and Key Contribution**
* **Core Problem:** Standard recommender systems focus on short-term engagement metrics (e.g., click-through rates), failing to model the long-term temporal dynamics of user retention [1, 4]. While Reinforcement Learning (RL) methods can optimize long-term rewards, they suffer from severe challenges in large-scale recommender systems, including delayed credit assignment, high sample complexity/inefficiency, exploration risks (frustrating users with poor recommendations), and complex evolving user preferences [1, 5, 13–16].
* **Key Contribution:** Introduces **Stratified Expert Cloning (SEC)**, a novel imitation learning framework (specifically Behavior Cloning) that leverages abundant interaction logs from high-retention "expert" users to directly learn retention-oriented policies without trial-and-error RL exploration [5-8]. Key innovations include:
  1. **Multi-level Expert Stratification:** Stratifies expert users into \\(K\\) retention-based hierarchies and trains specialized recommendation policies \\(\pi_k\\) for each tier to capture behavior continuum dynamics [6, 9-11].
  2. **Action Entropy Regularization (AER):** Incorporates entropy regularization (nuclear norm maximization for continuous action matrices, or class probability entropy for discrete actions) to maintain recommendation diversity and prevent policy collapse [6, 9, 12-14].
  3. **Adaptive Expert Selection Mechanism:** Dynamically matches users to the most appropriate expert level policy during inference based on state embedding distance to cluster centroids, constrained by the user's historical retention floor (\\(k^* = \min(k^*, r_h)\\)) [6, 19, 33–35].

---

### **3. Proposed Method or Architecture in Detail**

#### **Architectural Components**
* **State Encoder (\\(f_\phi\\)):** Shared neural network encoder that maps user context and state \\(s_t\\) (demographics, preferences, recent interactions) into a compact state embedding \\(h_t = f_\phi(s_t)\\) [15-17].
* **Action Predictors (\\(g_{\theta_k}\\)):** Specialized action predictor heads for each expert level \\(k \in \{1, \dots, K\}\\), mapping \\(h_t\\) to recommendation action \\(a_t\\) [16, 17].

#### **Training Stage**
* **Multi-Level Behavior Cloning (\\(\mathcal{L}_{\text{BC}}^k\\)):** High-retention expert users are split into \\(K\\) levels based on retention scores (e.g., active days per month) [18]. Trains level-specific policies via MSE loss for continuous actions \\(\sum \|g_{\theta_k}(f_\phi(s)) - a\|^2\\) or cross-entropy loss for discrete actions \\(\sum -\log g_{\theta_k}(a \mid f_\phi(s))\\) [16, 17].
* **Action Entropy Regularization (\\(\mathcal{L}_{\text{AER}}^k\\)):** Maximizes the nuclear norm of the continuous action matrix \\(A_k \in \mathbb{R}^{B \times d}\\) (where \\(\mathcal{L}_{\text{AER}}^k = -|A_k|_* = -\sum_{i=1}^{\min(B,d)} \sigma_i(A_k)\\)) or categorical entropy \\(\sum_{j=1}^C p_{k,j} \log p_{k,j}\\) for discrete actions [13, 19].
* **Total Training Loss:** \\(\mathcal{L} = \sum_{k=1}^K \left( \mathcal{L}_{\text{BC}}^k + \lambda \mathcal{L}_{\text{AER}}^k \right)\\) [19].

#### **Inference Stage**
* **State Space Clustering:** K-means partitions the state space of each expert level into \\(C_k\\) clusters with centroids \\(\mu_{k,c}\\) [20].
* **Adaptive Selection:** Computes minimum distance \\(d_k = \min_c d(f_\phi(s), \mu_{k,c})\\) and assigns the user to expert level \\(k^* = \arg\min_k \{k \mid d_k \le \delta_k\}\\) [21, 22]. Applies historical constraint \\(k^* = \min(k^*, r_h)\\) to ensure recommendations match or exceed the user's historical retention pattern [22, 23].

#### **Credit Assignment Mechanics**
* **No explicit multi-touch credit assignment.** SEC bypasses temporal credit assignment entirely by formulating retention optimization as supervised imitation learning (Behavior Cloning) over expert state-action pairs \\((s_t, a_t)\\) [1, 6, 7, 11, 24]. Instead of decomposing delayed retention signals across past interactions, it trains policies to directly mimic the actions taken by high-retention expert users in given states [6, 8, 11].

---

### **4. Datasets, Production Deployment, and Comparison Baselines**
* **Datasets:**
  * **KuaiRand:** Sequential recommendation dataset with random video exposures (27,285 users, 7,551 items, 1,436,609 interactions, 0.70% density) [25]. Evaluated offline using the **KuaiSim retention simulator** [25].
* **Production Deployment:**
  * Deployed live on **Kuaishou** and **Kuaishou Lite** platforms, each serving **over 200 million Daily Active Users (DAU)** [26, 27].
  * Integrated across both 1st Ranking Stage and 2nd Ranking Stage, using multimodal video clustering for discrete action generation [28, 29]. Online A/B testing allocated 10% traffic to baseline and SEC-optimized versions over two weeks [29].
* **Comparison Baselines:**
  * *Offline Baselines:* CEM (Cross-Entropy Method), DIN (Deep Interest Network), TD3 (Twin Delayed DDPG), SAC (Soft Actor-Critic), RLUR (Reinforcing User Retention), and GFN (Generative Flow Networks) [30].
  * *Online Baselines:* Standard Behavior Cloning + Entropy Loss without multi-level expert stratification [29, 31].

---

### **5. Key Quantitative Results with Numbers**

* **Offline Benchmark (KuaiRand Dataset, Table 1):**
  * **Return Time** (average days until return, lower is better): SEC = **1.411** vs. GFN (**1.496**), RLUR (**1.786**), CEM (**1.889**), DIN (**1.947**), SAC (**2.373**), TD3 (**2.382**) — achieving a **5.7% reduction** in return time over GFN [32, 33].
  * **Click Rate:** SEC = **0.833** vs. GFN (**0.805**), SAC (**0.801**), TD3 (**0.800**), RLUR (**0.789**), DIN (**0.773**), CEM (**0.762**) — a **3.5% improvement** over GFN [32, 33].
  * **Long View Rate:** SEC = **0.825** vs. GFN (**0.794**), SAC (**0.795**), TD3 (**0.791**), RLUR (**0.778**) — a **3.9% improvement** over GFN [32, 33].
  * **Like Rate:** SEC = **0.806** vs. GFN (**0.885**), SAC (**0.857**), TD3 (**0.852**), RLUR (**0.831**) — 8.9% lower than GFN, demonstrating an explicit trade-off where optimizing for long-term retention sacrifices some immediate satisfaction metrics [32, 33].
* **Offline Ablation Study (Table 2):**
  * Removing Multi-level stratification increased Return Time to **1.423** (+0.9%) and decreased Click Rate to **0.821** (-1.2%) [32, 34].
  * Removing Action Entropy Regularization increased Return Time to **1.449** (+1.8%) and decreased Long View Rate to **0.805** (-2.4%) [32, 34].
* **Live Online Production A/B Testing Results (Table 3, Table 4, & Section 5.2.2):**
  * **Active Days (Users active within a 7-day window):**
    * *Behavior Cloning + Entropy Loss:* 1st Ranking Stage (**+0.034%** Kuaishou, **+0.037%** Kuaishou Lite); 2nd Ranking Stage (**+0.036%** Kuaishou, **+0.042%** Kuaishou Lite) [29, 31].
    * *Additional gain from Multi-Level Expert Stratification:* **+0.028%** on Kuaishou, **+0.043%** on Kuaishou Lite [29, 31].
    * *Cumulative Total Improvement:* **+0.098%** on Kuaishou, **+0.122%** on Kuaishou Lite [29, 31].
    * *DAU Business Impact:* Translates directly into **over 200,000 additional daily active users (DAU)** on each platform [5, 29, 31].
  * **User Interest Expansion (Table 4):** Valid interest clusters increased by **+1.31%** on Kuaishou and **+1.14%** on Kuaishou Lite [35].

---

### **6. Limitations, Failure Modes, or Negative Results**
1. **Dependence on Expert User Availability:** Effectiveness is fundamentally contingent on having a sufficiently large and diverse set of high-retention "expert" users; it may perform poorly on nascent platforms or in niche domains lacking rich expert logs [36].
2. **Cold-Start Bottleneck:** Adaptive expert selection relies on high-quality user state embeddings \\(f_\phi(s)\\), which are sparse or unreliable for new users [36].
3. **Trade-Off with Immediate Satisfaction:** Offline Like Rate was **8.9% lower** than GFN (0.806 vs. 0.885), showing that optimizing strictly for long-term retention can slightly degrade immediate user feedback signals [33].
4. **Unproven Cross-Domain Generalizability:** Evaluated primarily on short-video platforms; applicability to e-commerce or news recommendation remains unverified due to differing definitions of expert behavior and retention metrics [36].

---

### **7. Top 5–7 Most Heavily Cited Prior Works**
1. **Cai et al. (2023) [RLUR / Retention RL]:** *Reinforcing User Retention in a Billion Scale Short Video Recommender System* (WWW '23) [37, 38].
2. **Liu et al. (2024) [GFN4Retention]:** *Modeling User Retention through Generative Flow Networks* (KDD '24) [39].
3. **Zhao et al. (2023) [DT4Rec]:** *User retention-oriented recommendation with decision transformer* (WWW '23) [40].
4. **Zhao et al. (2023) [KuaiSim Simulator]:** *KuaiSim: A comprehensive simulator for recommender systems* (NeurIPS '23) [40].
5. **Pomerleau (1991) / Ross et al. (2011) [Behavior Cloning Foundations]:** *Efficient training of artificial neural networks for autonomous navigation* & *A reduction of imitation learning and structured prediction to no-regret online learning* [41, 42].
6. **Ho & Ermon (2016) [GAIL] / Ng & Russell (2000) [IRL]:** *Generative adversarial imitation learning* & *Algorithms for inverse reinforcement learning* [43, 44].
7. **Ding et al. (2023) [IURO]:** *Interpretable User Retention Modeling in Recommendation* (RecSys '23) [45].

---

💡 *Would you like to explore how SEC's multi-level expert stratification or action entropy regularization could be adapted to guide candidate profile selection for your dating app's retention ranker?*

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

### **Source Evaluation: Stratified Expert Cloning for Retention-Aware Recommendation at Scale**
*(Lin et al., Kuaishou Technology & Peking University, CIKM 2025: `arxiv:2504.05628`)* [1]

---

### **(A) Q1 or Q2 or Both or Neither?**
* **Answer:** **Neither.**
* **Explanation:**
  * *Q1 (Industry/Production Attribution 2025–2026):* **No.** While published at CIKM 2025 (November 2025) and deployed on live production platforms, the paper presents an **imitation learning / behavior cloning recommendation framework**, not an attribution measurement system [1, 2].
  * *Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):* **No.** The authors explicitly highlight that retention optimization suffers from "delayed impact and credit assignment" [3]. Rather than performing multi-touch sequence attribution over past interactions, the paper bypasses credit assignment entirely by using Behavior Cloning over high-retention expert user logs [1, 6, 16–17].

---

### **(B) Q2 Class**
* **Classification:** **NOT**
* **Justification:** As an imitation learning / policy optimization framework (**SEC**), it learns action predictors via Behavior Cloning over stratified expert state-action pairs without generating or publishing a per-exposure retention credit table [6, 19, 23–26].

---

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction credit.**
* **Mechanism:** Bypasses temporal credit assignment by casting retention optimization as supervised imitation learning over expert state-action pairs \\((s_t, a_t)\\) [16–18, 24–26]. It trains expert policy heads \\(g_{\theta_k}(f_\phi(s))\\) using Mean Squared Error (MSE) loss for continuous actions or Cross-Entropy loss for discrete actions to directly mimic expert choices [25–26].
* **Target Outcome:** **Active Days within a 7-day window** (and reduced **Return Time** in days until next app visit) [4-7].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**
* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% of an N7 retention label to the final swipe before Day 7. **SEC** replaces rule-based attribution entirely with **Behavior Cloning (imitation learning) on high-retention "expert" users** [1, 8, 9]. Instead of attempting to back-propagate an N7 label to individual swipes, SEC identifies users who achieve high 7-day retention ("experts"), stratifies them into \\(K\\) retention tiers, and trains neural policies to directly mimic the candidate selection actions taken by those expert users in any given state [6, 19, 22–24].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *State Encoder (\\(f_\phi(s_t)\\)):* Encodes the user's current context and state (demographics, recent swipe history, active matches, messaging activity) [10, 11].
  2. *Multi-Level Expert Stratification (\\(U_1^E, U_2^E, U_3^E\\)):* Segments highly retained users into \\(K\\) expert tiers based on historical active days or retention scores [22–23].
  3. *Adaptive Policy Execution (\\(k^* = \min(k^*, r_h)\\)):* Matches a swiping user's state embedding to the nearest expert cluster centroid, bounded by their historical retention floor \\(r_h\\), and uses expert policy \\(\pi_{k^*}\\) to recommend candidate profiles whose match/engagement potential aligns with successful long-term retained users [33–36].

---

### **(E) Selection-Bias & Confounding Handling**
1. **Multi-Level Expert Stratification:** Rather than using a binary expert/non-expert classification (which introduces severe selection bias by attempting to force average users to mimic unachievable top-1% behavior), SEC stratifies expert users into \\(K\\) retention hierarchies, modeling user behavior along a natural continuum [6, 21–23].
2. **Adaptive Selection with Historical Floor Constraint:** During inference, a user's selected expert level is constrained by their historical retention level (\\(k^* = \min(k^*, r_h)\\)), preventing unrealistic policy assignments and ensuring recommendation quality does not degrade [34–35].
3. **Action Entropy Regularization (AER):** Maximizes the nuclear norm of the continuous action matrix (\\(\mathcal{L}_{\text{AER}}^k = -|A_k|_*\\)) or categorical class entropy to prevent policy collapse and ensure recommendation diversity across user interests [6, 27–31].

---

### **(F) Deployment and Production Dataset Evidence**

* **Production Deployment:** Deployed live on **Kuaishou** and **Kuaishou Lite**, two major video platforms serving **over 200 million Daily Active Users (DAU)** each [4, 12, 13]. Evaluated in online A/B testing holding out 10% traffic for over two weeks across both 1st Ranking Stage and 2nd Ranking Stage pipelines [7, 13].
* **Offline Benchmark Dataset:** **KuaiRand** (27,285 users, 7,551 items, 1,436,609 interactions, 0.70% density) evaluated using the **KuaiSim retention simulator** [6, 14].
* **Quoted Quantitative Results:**
  * **Offline Simulator Benchmark (KuaiRand, Table 1):**
    * **Return Time (lower is better):** **1.411** days (SEC) vs. GFN (**1.496**), RLUR (**1.786**), CEM (**1.889**), DIN (**1.947**), SAC (**2.373**), TD3 (**2.382**) — achieving a **5.7% reduction in return time** over GFN [6, 15].
    * **Click Rate:** **0.833** (SEC) vs. GFN (**0.805**), SAC (**0.801**), TD3 (**0.800**), RLUR (**0.789**), DIN (**0.773**), CEM (**0.762**) — a **3.5% improvement** over GFN [6, 15].
    * **Long View Rate:** **0.825** (SEC) vs. GFN (**0.794**), SAC (**0.795**), TD3 (**0.791**), RLUR (**0.778**) — a **3.9% improvement** over GFN [6, 15].
    * **Like Rate:** **0.806** (SEC) vs. GFN (**0.885**), SAC (**0.857**), TD3 (**0.852**), RLUR (**0.831**) — **8.9% lower** than GFN, demonstrating an explicit trade-off where optimizing for long-term retention sacrifices some immediate satisfaction [15, 16].
  * **Live Online A/B Testing Results (Table 3 & Table 4):**
    * **Active Days (Users active within a 7-day window):**
      * *Behavior Cloning + Entropy Loss:* 1st Ranking (**+0.034%** Kuaishou, **+0.037%** Kuaishou Lite); 2nd Ranking (**+0.036%** Kuaishou, **+0.042%** Kuaishou Lite) [7].
      * *Additional gain from Multi-Level Expert Stratification:* **+0.028%** on Kuaishou, **+0.043%** on Kuaishou Lite [7].
      * *Cumulative Total Improvement:* **+0.098%** on Kuaishou, **+0.122%** on Kuaishou Lite [4, 7].
      * *DAU Business Impact:* Translates directly into **over 200,000 additional daily active users (DAU)** on each platform [4, 17, 18].
    * **User Interest Expansion (Table 4):** Valid interest clusters increased by **+1.31%** on Kuaishou and **+1.14%** on Kuaishou Lite [19].

---

💡 *Would you like to explore how SEC's multi-level expert stratification or action entropy regularization could be adapted to guide candidate profile selection for your dating platform's retention ranker?*

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
**Priority:** see queue.md `G10`
