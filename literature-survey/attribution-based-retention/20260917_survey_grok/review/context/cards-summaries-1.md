# Card summaries 1/12 — Summary and Evidence sections of all cards (generated)

### A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications [1]
`2020_KDD_RDSA_Sleeping-Recovering-Bandit-Notifications.md`
**Source:** https://research.duolingo.com/papers/yancey.kdd20.pdf  

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications* [1]
* **Authors:** **Kevin P. Yancey** (`kyancey@duolingo.com`) and **Burr Settles** (`burr@duolingo.com`) [1]
* **Affiliation:** **Duolingo** (Pittsburgh, Pennsylvania, USA) [1]
* **Year & Venue:** Published in **August 2020** at the *Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD ’20)* [2]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Online and mobile applications rely on recurring daily push notifications to drive user engagement, but conventional multi-armed bandit algorithms fail due to two key real-world complications [1, 3]:
  1. *Sleeping Arms (Conditional Eligibility):* Certain notification templates are available only under specific user conditions (e.g., streak wagers or specific language courses) [4, 5]. Standard bandits confound an arm's intrinsic quality with the activity level of the eligible user segment [8–9].
  2. *Recovering Arms (Novelty Effects):* Unseen or "fresh" templates exert a strong positive impact, whereas repeatedly sending the same notification desensitizes users and degrades engagement over time [3, 6].
* **Key Contribution:**
  * **Recovering Difference Softmax Algorithm:** Proposes a practical bandit framework combining inverse propensity weighted relative scoring, empirical Bayes shrinkage, and a cognitively inspired exponential recency penalty [1, 10–12, 16].
  * **Large-Scale Industrial Impact:** Deployed to optimize millions of daily reminders at Duolingo, delivering a **+0.5% lift in DAUs** and a **+2.0% lift in new user D7 retention** over a highly optimized production baseline [1, 7].

---

### **(3) Proposed Method or Architecture in Detail**
* **Binary Short-Window Reward Definition:**
  \\[r_t \in \{0, 1\}\\]
  Reward is \\(1\\) if the user completes a lesson within **2 hours** of sending the notification, and \\(0\\) otherwise (filtering out noisy organic app opens) [8].
* **Controlling for Sleeping Arms (Relative Difference Score):**
  Uses Horvitz-Thompson weighted importance sampling on eligible historical rounds \\(H_a\\) to estimate typical reward when arm \\(a\\) is selected (\\(\bar{\mu}_a^+\\)) vs. when \\(a\\) is eligible but a different arm is chosen (\\(\bar{\mu}_a^-\\)) [7, 10–12]:
  \\[w_t^+ = b_t(a \mid t)^{-1}, \quad w_t^- = (1 - b_t(a \mid t))^{-1}\\]
  \\[s_a = \frac{\bar{\mu}_a^+ - \bar{\mu}_a^-}{\bar{\mu}_a^-}\quad [9, 10]\\]
* **Small Sample Regularization (Empirical Bayes Shrinkage):**
  Regularizes scores towards a Bayesian prior \\(\mu_a = \frac{\sum r_t}{|H_a|}\\) using Kish's effective sample sizes \\(n_a^+, n_a^-\\) and variance hyperparameter \\(\sigma \approx 105\\) [12, 15–16]:
  \\[\hat{\mu}_a^+ = \frac{\bar{\mu}_a^+ n_a^+ + \mu_a \sigma}{n_a^+ + \sigma}, \quad \hat{\mu}_a^- = \frac{\bar{\mu}_a^- n_a^- + \mu_a \sigma}{n_a^- + \sigma}, \quad \hat{s}_a = \frac{\hat{\mu}_a^+ - \hat{\mu}_a^-}{\hat{\mu}_a^-}\quad [6]\\]
* **Handling Recovering Arms (Recency Penalty):**
  Applies an exponential decay penalty based on the number of days \\(d_{a,t}\\) since arm \\(a\\) was last sent to user \\(u\\), using half-life \\(h = 15\\) days and decay weight \\(\gamma = 0.017\\) [6, 11]:
  \\[s_{a,t}^* = \hat{s}_a - \gamma \cdot 2^{-d_{a,t} / h}\quad [6]\\]
* **Arm Selection & Exploration:**
  Selects eligible arms using a Softmax policy with exploration temperature \\(\tau = 0.0025\\) [12, 13]:
  \\[\pi(a \mid t) = \frac{\exp(s_{a,t}^* / \tau)}{\sum_{a' \in A_t} \exp(s_{a',t}^* / \tau)}\quad [12]\\]
* **Credit Assignment Mechanics:**
  Credit is assigned at the **individual notification template (arm)** level by estimating the relative lift in 2-hour lesson completion when chosen vs. when unchosen among eligible rounds (\\(\hat{s}_a\\)) [6, 8, 9]. It does **not** calculate multi-touch sequence credit across past user interactions.

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets & Offline Scale:**
  Captured 34 days of historical logs from a legacy uniform random template policy [14]:
  * *Training Set:* **15 days, 88 million rows** [14].
  * *Test Set:* **19 days, 114 million rows** [14].
* **Production Deployment:**
  Deployed at scale on Duolingo's daily practice reminder pipeline using daily batch processing (via decision/event log pipelines) and a continuous **5% uniform random holdout** set for baseline tracking and data collection [32, 38, 40–41].
* **Comparison Baselines:**
  * Uniform random baseline (legacy production policy) [14, 15].
  * "Reuse Last Template" policy (always re-sending the user's last template) [11, 16].
  * Template-only arms vs. Template + UI Language pair arms [16, 17].
  * Softmax exploration variations (\\(\tau \in \{0.02, 0.01, 0.005, 0.0025\}\\) and argmax \\(\tau=0\\)) [13, 15].

---

### **(5) Key Quantitative Results with Numbers**
* **Offline Log Experiments:**
  * Template + UI Language arms: **+1.8% relative lift** in average reward over random baseline (\\(0.1318\\) vs \\(0.1295\\)) [16, 17].
  * Adding Recency Penalty (\\(\gamma = 0.017, h = 15\\) days): **+1.9% relative lift** over random baseline (\\(0.1320\\) vs \\(0.1295, p < 0.1\\)) [25–27].
  * Reusing Last Template baseline: **-0.5% regression** compared to random baseline (\\(0.1289\\) vs \\(0.1295\\)) [16].
  * Softmax \\(\tau = 0.0025\\): **+1.9% relative lift** over random baseline (\\(0.1319\\) vs \\(0.1295\\)), preserving \\(>90\%\\) of argmax potential gain while maintaining 17% exploration [13, 15].
* **Live Production Operational A/B Test Results (Table 8):**
  * **Daily Active Users (DAUs):** **+0.5%** (\\(p < 0.05\\)) [1, 32–33].
  * **Total Lessons Completed:** **+0.4%** (\\(p < 0.05\\)) [32–33].
  * **Existing User D1 Retention:** **+0.5%** (\\(p < 0.05\\)) [32–33].
  * **Existing User D7 Retention:** **+0.2%** (not statistically significant) [7].
  * **New User D1 Retention:** **+2.2%** (\\(p < 0.05\\)) [1, 32–33].
  * **New User D7 Retention:** **+2.0%** (\\(p < 0.05\\)) [32–33].
* **Long-Term 5-Month Holdout Verification:**
  Re-evaluation after 5 months showed the bandit policy maintained **2.5% higher reward** than the 5% uniform holdout set [32–33].

---

### **(6) Limitations, Failure Modes, or Negative Results**
1. **Baseline Drift Counter-Intuitiveness (\\(\bar{\mu}_a^-\\)):** As the policy improves, alternative baseline rewards (\\(\bar{\mu}_a^-\\)) increase, causing raw template scores to drift downward over time, which appears counter-intuitive to internal team members [18].
2. **High Small-Sample Variance:** Small-sample arms exhibit severe score volatility (\\(\pm 5\%\\) for 38% of small arms), causing degenerate loops if unregularized by empirical Bayes shrinkage [12–13].
3. **Combinatorial Explosion for User Features:** Splitting arms by user attributes (e.g., country, device) multiplies data requirements, requiring future contextual/hierarchical bandit extensions [17].
4. **24-Hour Batch Feedback Delay:** Updating arm scores via daily batch processing delays feedback by up to a day [19].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Kleinberg, Niculescu-Mizil, & Sharma (2010) [Ref 10]:** *Regret bounds for sleeping experts and bandits* [4, 20].
2. **Pike-Burke & Grunewalder (2019) [Ref 12]:** *Recovering Bandits* [20].
3. **Auer, Cesa-Bianchi, & Fischer (2002) / Auer et al. (2002) [Refs 2, 3]:** *Finite-time analysis of the multiarmed bandit problem* & *The nonstochastic multiarmed bandit problem* [4, 21].
4. **Chu et al. (2011) [Ref 5]:** *Contextual bandits with linear payoff functions* [17, 22].
5. **Horvitz & Thompson (1952) [Ref 8]:** *A generalization of sampling without replacement from a finite universe* (Inverse propensity weighting) [22, 23].
6. **Kish (1965) [Ref 9]:** *Survey Sampling* (Kish's effective sample size) [6, 20].
7. **Sutton & Barto (2018) [Ref 17]:** *Reinforcement learning: An introduction* [12, 23-25].

---

💡 *Would you like to explore how Duolingo's recovering recency penalty or sleeping arm relative score (\\(\hat{s}_a\\)) could be adapted to prevent repetitive profile recommendations in your dating app's candidate ranker?*

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Surrogate for Long-Term User Experience in Recommender Systems [1]
`2022_KDD_NA_Surrogate-Long-Term-User-Experience.md`
**Source:** https://dl.acm.org/doi/pdf/10.1145/3534678.3539073  

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**

* **Title:** *Surrogate for Long-Term User Experience in Recommender Systems* [1]
* **Authors:** **Yuyan Wang**¹, **, Mohit Sharma**², **Can Xu**², **Sriraj Badam**², **Qian Sun**², **Lee Richardson**², **Lisa Chung**², **Ed H. Chi**¹, and **Minmin Chen**¹ [1]
* **Affiliations:** 
  1. **Google Research, Brain Team** (`{yuyanw, edchi, minminc}@google.com`) [1]
  2. **Google** (`{mohitsharma, canxu, srirajdutt, qians, leerich, lchung}@google.com`) [1]
* **Year:** **2022** (August 14–18, 2022) [2]
* **Venue:** *Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD ’22)*, Washington, DC, USA [2]

---

### **(2) Core Problem and Key Contribution**

* **Core Problem:** Recommender systems struggle to directly optimize long-term user experience (measured as platform revisit frequency over months) due to extreme signal sparsity (only **2.3%** of low-frequency users become high-frequency over 5 months), low signal-to-noise ratio, and a multi-week temporal delay between individual recommendations and return visits [1, 3, 4].
* **Key Contributions:**
  1. **Behavioral Measurement Metrics:** Defines metrics capturing users' sequential medium-term consumption patterns (entropy diversity, KL-divergence diversity, repeated consumption, high-quality completion ratio, persistent topics, and page revisit times) [5-10].
  2. **Longitudinal Analytical Insights:** Identifies sequential consumption patterns associated with long-term platform revisitation across a 20-week (5-month) window on a large industrial recommendation platform [5, 10, 11].
  3. **Standardized Surrogate Selection:** Establishes a Random Forest feature importance procedure to select robust medium-term surrogates (entropy-based diversity \\(D_{\text{entropy}}\\)` and homepage revisit time \\(T_{\text{revisit}}(\text{Home})\\)) [5, 12, 13].
  4. **RL Integration & Online Validation:** Incorporates surrogate multipliers into a production REINFORCE RL recommender system, demonstrating statistically significant gains in overall user engagement and long-term visiting frequency in live A/B tests [5, 14-17].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Reinforcement Learning Framework & Surrogate Formulations**
* **Base Architecture:** Formulates recommendation as a Markov Decision Process (MDP) over \\((S, A, P, R, \gamma)\\) using a REINFORCE policy \\(\pi_\theta(a \mid s_t) = \frac{\exp(u_{s_t}^\top v_a)}{\sum_{a'} \exp(u_{s_t}^\top v_{a'})}\\) with off-policy importance sampling [18-20].
* **Multiplicative Surrogate Reward Formulations:**
  1. **Entropy-Based Diversity Surrogate:**
     \\[R_t(s_t, a_t) = R_{0t}(s_t, a_t) \cdot \exp\left[ m \left(D_{\text{entropy}}(S_t) - D_{\text{entropy}}(S_{t-1})\right) \right]\\]
     where \\(D_{\text{entropy}}(S) = -\sum_i p_i \log(p_i)\\) over a 2-week window [6, 21]. If a consumed item increases consumption diversity (\\(D_{\text{entropy}}(S_t) - D_{\text{entropy}}(S_{t-1}) > 0\\)), the original reward \\(R_{0t}\\) is amplified by a multiplier \\(> 1\\) (scaled by \\(m=5\\)) [21].
  2. **Homepage Revisits Surrogate:**
     \\[R_t(s_t, a_t) = R_{0t}(s_t, a_t) \cdot \left[1 + c \cdot \mathbb{1}(T_{\text{revisit}}(S, \text{Home}) < T_0)\right]\\]
     where \\(c=10\\) boosts the immediate engagement reward \\(R_{0t}\\) if the recommended item is consumed with high quality and the user returns to the homepage within \\(T_0\\) time [17].

#### **Credit Assignment Mechanics**
* Credit is assigned to individual recommended items \\(a_t\\) at interaction time by modulating their immediate engagement reward \\(R_{0t}(s_t, a_t)\\) with a surrogate multiplier based on medium-term behavioral changes (e.g., incremental 2-week diversity gain or homepage return speed) [17, 21].
* If the recommended item is not consumed (\\(R_{0t} = 0\\)), the surrogate multiplier has zero effect (\\(R_t = 0\\)) [22].
* The paper does **not** publish a formal causal multi-touch attribution (MTA) credit decomposition table across historical touchpoints.

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets & Scale:** User visiting logs from one of the largest industrial recommendation platforms (Google/YouTube) over a **20-week (5-month) period** covering **2 million low-frequency users** (extended to 40 weeks for duration distribution analysis) [4, 10, 23].
* **Production Deployment:** Live online A/B testing on an industrial recommendation platform serving **billions of users** [10, 11, 15, 16].
* **Comparison Baselines:** Standard production REINFORCE recommender optimizing original immediate engagement rewards \\(R_{0t}\\) without surrogate multipliers [15, 16].

---

### **(5) Key Quantitative Results with Numbers**

* **Empirical Longitudinal Log Analysis (2M low-frequency users over 5 months):**
  * **Sparsity:** Only **2.3%** of low-frequency users transitioned to high-frequency users over 5 months [4].
  * **Time Horizon:** Transitioning from low-frequency to high-frequency takes an average of **15.32 weeks** (median **14 weeks**) [23].
  * **High-Quality Consumption:** Users who became high-frequency more than doubled their high-quality consumption ratio from **<20.0% to 46.0%** [24].
  * **Persistent Topics:** Persistent topic ratio more than tripled from **15.3% to 46.9%** among transitioning users [25].
* **Random Forest Surrogate Selection:**
  * Entropy diversity \\(D_{\text{entropy}}\\)` and average homepage revisit time \\(T_{\text{revisit}}(\text{Home})\\) achieved the highest feature importance across user activity slices (prediction AUC ranging from **0.57 to 0.63** across slices, **0.61 overall**) [13, 26].
* **Live Online Production A/B Test Results:**
  * **Entropy-Based Diversity Surrogate (\\(m=5\\)):** Delivered statistically significant gains in top-line overall user enjoyment (**~+0.14%** relative lift over baseline at peak) and long-term visiting frequency (**~+0.12%** relative lift), along with a continuous increase in consumed topic clusters over time [16].
  * **Homepage Revisits Surrogate (\\(c=10\\)):** Delivered statistically significant lifts in overall user visiting frequency (**+0.08% to +0.12%**), low-frequency user segment visiting frequency (**+0.25% to +0.30%**), homepage visits (**+0.40% to +0.55%**), and satisfied consumptions (**+0.20% to +0.30%**) [17].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Cardinality Confounding in Entropy Diversity:** Entropy diversity naturally grows with item set cardinality (a uniform distribution over 2 topics has entropy \\(\sim 0.69\\), while 5 topics yields \\(\sim 1.61\\)), requiring KL-divergence \\(D_{\text{KL}}\\)` to evaluate distribution shape independent of support size [6, 27].
2. **Zero-Reward Inertia:** Because the surrogate operates multiplicatively (\\(R_t = R_{0t} \cdot \text{multiplier}\\)), if an item receives zero immediate reward (\\(R_{0t} = 0\\)), the surrogate has no effect, failing to reward diversity when immediate engagement is absent [22].
3. **Manual Hyperparameter Sensitivity:** Requires manual tuning of surrogate multiplier strength parameters (\\(m=5\\), \\(c=10\\)) [17, 21].
4. **Omission of Business Constants:** Specific duration and threshold constants (\\(X, Y, Z, A, B, T_0, c_1 \dots c_5\\)) were omitted from publication due to corporate compliance policies [8-10, 26].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Chen et al. (2019) [Ref 11]:** *Top-k off-policy correction for a REINFORCE recommender system* (WSDM '19) [28].
2. **Athey et al. (2019) [Ref 4]:** *The surrogate index: Combining short-term proxies to estimate long-term treatment effects more rapidly and precisely* (NBER Working Paper) [29].
3. **Wu et al. (2017) [Ref 58]:** *Returning is believing: Optimizing long-term user engagement in recommender systems* (CIKM '17) [30].
4. **Zheng et al. (2018) [Ref 69]:** *DRN: A deep reinforcement learning framework for news recommendation* (WWW '18) [31].
5. **Prentice (1989) [Ref 42]:** *Surrogate endpoints in clinical trials: definition and operational criteria* (Statistics in Medicine) [32].
6. **Williams (1992) [Ref 57]:** *Simple statistical gradient-following algorithms for connectionist reinforcement learning* (Machine Learning / REINFORCE) [30].
7. **Covington, Adams, & Sargin (2016) [Ref 15]:** *Deep neural networks for youtube recommendations* (RecSys '16) [33].

---

💡 *Would you like to explore how Google's multiplicative surrogate reward structure or entropy-based diversity metric could be adapted to modulate candidate profile ranking scores for your dating app?*

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

