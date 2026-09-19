# Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning [1, 2]

**Source:** https://arxiv.org/html/2607.14192  
**Date analyzed:** 2026-09-18  
**NLM source id:** `1a74145c-f8bc-438b-a5ea-965b29abab16`  
**Queue id:** G23  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**

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
**Priority:** see queue.md `G23`
