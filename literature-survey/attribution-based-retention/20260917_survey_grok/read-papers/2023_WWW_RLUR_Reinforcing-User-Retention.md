# Reinforcing User Retention in a Billion Scale Short Video Recommender System [1]

**Source:** https://arxiv.org/pdf/2302.01724.pdf  
**Date analyzed:** 2026-09-18  
**NLM source id:** `7d87bba2-fe8d-4f09-87ad-713b22aaca47`  
**Queue id:** G7  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**

* **Title:** *Reinforcing User Retention in a Billion Scale Short Video Recommender System* [1]
* **Authors:** **Qingpeng Cai**\*¹, **Shuchang Liu**\*¹, **Xueliang Wang**¹, **Tianyou Zuo**¹, **Wentao Xie**¹, **Bin Yang**¹, **Dong Zheng**¹, **Peng Jiang**†¹, and **Kun Gai**² (\*Co-first authors, †Corresponding author) [1, 2]
* **Affiliations:** 
  1. **Kuaishou Technology**, Beijing, China (`{caiqingpeng, liushuchang, wangxueliang03, zuotianyou, xiewentao, yangbin11, zhengdong, jiangpeng}@kuaishou.com`) [1]
  2. **Unaffiliated**, Beijing, China (`gai.kun@qq.com`) [3]
* **Year:** **2023** (April 30 – May 4, 2023) [2]
* **Venue:** *Proceedings of the ACM Web Conference 2023 (WWW ’23), Austin, Texas, USA* [2, 4]

---

### **(2) Core Problem and Key Contribution**

* **Core Problem:** Standard recommender models (point-wise or list-wise) predict immediate rewards (clicks, watch time) but cannot optimize **user retention** (the likelihood of returning to the app) or Daily Active Users (DAU) [2, 5–6]. Retention is a long-term, delayed feedback signal resulting from multiple interactions across sessions, making it difficult to decompose into individual items [2, 6–7]. Moreover, standard Reinforcement Learning (RL) methods fail when applied directly to retention optimization due to three challenges [3, 5]:
  1. **Uncertainty:** Retention is noisy and influenced by external non-system factors (e.g., social events) [5].
  2. **Bias:** Retention is heavily confounded by day of the week and user activity levels (highly active users naturally have shorter return gaps) [5].
  3. **Long Delay Time:** Retention feedback returns hours or days later, causing severe distribution shifts between the behavior policy and the learning policy [5].
* **Key Contributions:**
  1. **Infinite-Horizon MDP Formulation:** Models retention optimization as an infinite-horizon request-based Markov Decision Process (MDP) designed to minimize cumulative returning time (the time gap between consecutive sessions) [3, 6-8].
  2. **Reinforcement Learning for User Retention (RLUR):** Develops an RL framework featuring:
     * *Retention Normalization:* Uses a session-level returning time predictor to normalize rewards and reduce variance [9, 19–21].
     * *Grouped Policies:* Trains separate actor policies for high- and low-activity user groups to eliminate activity bias [9, 21–22].
     * *Soft Regularization:* Applies a policy-density-based exponential soft regularization term on the actor loss to stabilize training under long delays [9, 22–23].
     * *Dual Critics & Intrinsic Rewards:* Learns separate Retention (\\(Q_T\\)) and Immediate Response (\\(Q_I\\)) critics, augmented with Random Network Distillation (RND) intrinsic exploration rewards [9, 17–19].
  3. **Billion-Scale Industrial Launch:** Deployed on Kuaishou (serving hundreds of millions of users), achieving long-term, statistically significant gains in Day-1/Day-7 retention, app open frequency, and DAU [3, 7, 9, 10].

---

### **(3) Proposed Method or Architecture in Detail**

* **MDP Formulation & Architecture:**
  * **State (\\(s_{it}\\)):** Consists of user profile (age, gender, location), behavior history (user statistics, video IDs and feedback from the previous 3 requests), request context, and candidate video features [8, 11].
  * **Action (\\(a_{it}\\)):** An 8-dimensional continuous action vector \\(a_{it} \in [4]^8\\) output by the Actor network, representing dynamic ensemble weights for 8 underlying scoring models (predicting watch time, short view, long view, like, follow, forward, comment, and profile entry) [8, 11].
  * **Ranking & Selection:** A linear ensemble function \\(f(a_{it}, x_j) = \sum_{k=1}^8 a_{it,k} x_{jk}\\) ranks candidate videos and serves top 6 videos per request [11–12, 28].
  * **Objective:** Minimize cumulative returning time \\(\sum_{i=1}^\infty \gamma^{i-1} T(s_i)\\) across sessions (where \\(T(s_i)\\) is the returning time gap between session \\(i\\) and \\(i+1\\)) [7, 12–13].
* **Critic Models:**
  * **Retention Critic (\\(Q_T\\)):** Estimates cumulative returning time using Temporal Difference (TD) learning, setting discount factor \\(\gamma_{it} = 1\\) for intra-session requests and \\(\gamma = 0.95\\) for the session's terminal request [13–16].
  * **Immediate Response Critic (\\(Q_I\\)):** Estimates immediate user rewards (watch time + interactions) plus RND intrinsic novelty rewards [18–19, 28].
* **Credit Assignment Mechanics:**
  * **Action-Level Allocation:** Credit is assigned to the continuous **request-level ensemble weight vector (\\(a_{it}\\))** rather than to individual video items directly [11–12, 28].
  * **Immediate Reward Aggregation:** Immediate feedback \\(I(s_{it}, a_{it})\\) is calculated as the unweighted sum of total watch time (in seconds) and total interaction counts across the 6 recommended videos in the request [8, 11].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets & Scale:**
  * **Offline Benchmark:** **KuaiRand**, an unbiased sequential short video dataset, used to construct a multi-session user interaction simulator incorporating immediate feedback, session-exit, and 10-day return probability modules [12].
  * **Live Production System:** Deployed live on the **Kuaishou app**, a short video platform serving over a **billion users** [3, 7, 9].
* **Production Deployment:** Fully deployed in production as a core ranking weight controller [2, 10, 26–27].
* **Comparison Baselines:**
  * **Cross Entropy Method (CEM):** A black-box optimization heuristic widely used for ranking parameter search [25–26].
  * **TD3 (Twin Delayed DDPG):** State-of-the-art continuous off-policy RL baseline [13].
  * **RLUR Ablations:** `RLUR (naive, \gamma=0)` (single-session retention) and `RLUR (naive, \gamma=0.9)` (multi-session retention without noise/bias/delay fixes) [13].

---

### **(5) Key Quantitative Results with Numbers**

* **Offline Simulator Benchmark (KuaiRand, Table 1):**
  * **CEM:** Returning Time = **2.036**, User Retention = **0.587** [13].
  * **TD3:** Returning Time = **2.009**, User Retention = **0.592** [13].
  * **RLUR (naive, \\(\gamma=0\\)):** Returning Time = **2.001**, User Retention = **0.596** [13].
  * **RLUR (naive, \\(\gamma=0.9\\)):** Returning Time = **1.961**, User Retention = **0.601** [13].
  * **RLUR (Full Framework):** Returning Time = **1.892** (lowest), User Retention = **0.618** (highest) [13].
* **Live Online Production A/B Test (Kuaishou Platform vs. CEM Baseline, Converged >Day 100):**
  * **App Open Frequency:** Converged to a steady **+0.450% improvement** [10].
  * **Daily Active Users (DAU):** Converged to a steady **+0.2% improvement** [10].
  * **Day-1 User Retention:** Converged to a steady **+0.053% improvement** [10].
  * **Day-7 User Retention:** Converged to a steady **+0.063% improvement** [10].
  * *Statistical Significance Note:* The authors explicitly note that a **+0.01%** gain in retention and a **+0.1%** gain in DAU are commercially and statistically significant at billion-user platform scale [10].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Instability of Standard RL in Production:** Standard off-policy algorithms (e.g., TD3) failed to train stably in the live production system due to huge distribution shifts caused by hours/days of reward delay, preventing direct TD3 online deployment [5, 9, 14].
2. **Failure of Single-Session Retention Optimization:** `RLUR (naive, \gamma=0)` performed worse than `RLUR (naive, \gamma=0.9)` (retention 0.596 vs. 0.601), proving that optimizing immediate next-session retention without considering multi-session cumulative returning time is sub-optimal [13].
3. **Bias toward Active Users:** Without user activity stratification (\\(\pi_{\text{high}}\\) vs. \\(\pi_{\text{low}}\\)), policy gradient updates become dominated by hyper-active users whose returning times are naturally very short [8, 21–22].
4. **Lack of Item-Level Retention Credit:** The model optimizes request-level score ensemble weights \\(a_{it}\\) rather than allocating per-item or per-swipe retention attribution labels to individual candidate videos [11–12, 28].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Covington, Adams, & Sargin (2016) [Ref 6]:** *Deep neural networks for youtube recommendations* (RecSys '16) [15].
2. **Lillicrap et al. (2015) [Ref 15]:** *Continuous control with deep reinforcement learning* (DDPG / ICLR '16) [16].
3. **Burda et al. (2018) [Ref 2]:** *Exploration by random network distillation* (RND) [17].
4. **Fujimoto, Hoof, & Meger (2018) / Fujimoto & Gu (2021) [Refs 7, 8]:** *Addressing function approximation error in actor-critic methods* (TD3 / ICML '18) & *A minimalist approach to offline reinforcement learning* (BCQ / NeurIPS '21) [15].
5. **Wu et al. (2017) [Ref 30]:** *Returning is believing: Optimizing long-term user engagement in recommender systems* (CIKM '17) [18].
6. **Zou et al. (2019) / Xue et al. (2022) [Refs 32, 45]:** *Reinforcement learning to optimize long-term user engagement in recommender systems* (KDD '19) & *ResAct: Reinforcing Long-term Engagement in Sequential Recommendation with Residual Actor* [19, 20].
7. **Gao et al. (2022) [Ref 10]:** *KuaiRand: An Unbiased Sequential Recommendation Dataset with Randomly Exposed Videos* (CIKM '22) [21].

---

💡 *Would you like to explore how RLUR's returning time normalization or dual-critic architecture (\\(Q_T / Q_I\\)) could be adapted to optimize candidate scoring for your dating platform's N7 retention ranker?*

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
**Priority:** see queue.md `G7`
