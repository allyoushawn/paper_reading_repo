# Relevance index 1/10 — Project Relevance sections of all cards (generated)

### A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications [1]
`2020_KDD_RDSA_Sleeping-Recovering-Bandit-Notifications.md`
**Source:** https://research.duolingo.com/papers/yancey.kdd20.pdf  

### **Source Evaluation: *A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications***
*(Yancey & Settles, Duolingo, KDD 2020: `yancey.kdd20.pdf`)* [1, 2]

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**

**Neither.** [1-4]  
* **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** Published in August 2020 at KDD 2020 [1, 2], which falls outside the 2025-01 to 2026-09 window. Furthermore, it presents a multi-armed bandit algorithm for notification template selection rather than a multi-touch attribution (MTA) measurement system [1, 3].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The algorithm optimizes daily push notification and practice reminder emails using a multi-armed bandit (Recovering Difference Softmax Algorithm) based on a short 2-hour lesson completion reward [1, 4, 5]. It does **not** attribute overall user retention or active days back to individual past in-app user interaction touchpoints (e.g., swipes or messages) across historical sequences [1, 4].

---

### **(B) Q2 Class**

**NOT.** [1, 3, 6]  
* **Justification:** The paper presents a multi-armed bandit policy optimization framework (Recovering Difference Softmax Algorithm with a Softmax exploration policy) that selects optimal notification templates per user-round [1, 3, 6]. It does **not** output or publish a per-exposure retention credit table.

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction sequence attribution credit table.** [4, 7, 8]
* **Target Outcome:** **2-Hour Lesson Completion Rate (\\(r_t \in \{0, 1\}\\))** [4].
* **Mechanics:** A notification round assigns a reward of \\(1\\) if the user completes a lesson within **2 hours** of sending the reminder, and \\(0\\) otherwise (filtering out noisy organic app opens) [4]. Credit is evaluated at the **notification template (arm) level** by computing an IPW-adjusted relative difference score \\(\hat{s}_a = \frac{\hat{\mu}_a^+ - \hat{\mu}_a^-}{\hat{\mu}_a^-}\\) with empirical Bayes shrinkage and a recency decay penalty [7-9], rather than decomposing credit across past user interaction sequences.

---

### **(D) Replacing Last-Touch N7 → Latest Swipes**

* **How it Improves on Last-Touch:** Last-touch post-hoc rules assign 100% of an N7 retention label to recent swipes, ignoring conditional eligibility bias and user desensitization (novelty decay / fatigue) [10-12]. This paper replaces post-hoc last-touch attribution by treating re-engagement prompts / recommendations as a **recovering sleeping bandit problem** [1, 9-11]. It uses inverse propensity weighting (IPW) to control for conditional eligibility bias (\\(\mu_a^+ - \mu_a^-\\)) and applies an exponential recency decay penalty (\\(-\gamma \cdot 2^{-d_{a,t}/h}\\)) to prevent repetitive, fatigue-inducing recommendations [7, 9].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Notification / Candidate Re-engagement Arm (\\(a\\)):* Represents candidate re-engagement push notifications, profile match reminders, or candidate profiles in a swipe deck [1, 10].
  2. *Sleeping Arms (Conditional Eligibility):* Certain re-engagement prompts or profile categories are available only under specific user states (e.g., users with active streak wagers or pending matches) [11, 13]. The relative difference score \\(\hat{s}_a\\) controls for eligibility confounding by comparing outcome rates when eligible & shown (\\(\bar{\mu}_a^+\\)) vs. eligible & not shown (\\(\bar{\mu}_a^-\\)) [7, 8].
  3. *Recovering Recency Penalty (Anti-Fatigue):* If a candidate profile category, push copy, or match prompt was recently sent to user \\(u\\), an exponential decay penalty (\\(-\gamma \cdot 2^{-d_{a,t}/h}\\) with half-life \\(h = 15\\) days) reduces its score to prevent repetitive desensitization, encouraging variety across swiping and conversation pushes [9, 10, 14].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Inverse Propensity Weighted (IPW) Relative Difference Scoring:** Controls for conditional eligibility bias (sleeping arms) using Horvitz-Thompson weighted importance sampling on eligible historical rounds \\(H_a\\) [10–12]:
   \\[w_t^+ = b_t(a \mid t)^{-1}, \quad w_t^- = (1 - b_t(a \mid t))^{-1}\\[2pt]
   \bar{\mu}_a^+ = \frac{\sum w_t^+ r_t}{\sum w_t^+}, \quad \bar{\mu}_a^- = \frac{\sum w_t^- r_t}{\sum w_t^-}, \quad s_a = \frac{\bar{\mu}_a^+ - \bar{\mu}_a^-}{\bar{\mu}_a^-}\\]
2. **Empirical Bayes Shrinkage Regularization:** Regularizes relative scores \\(\bar{\mu}_a^+\\) and \\(\bar{\mu}_a^-\\) towards a Bayesian prior \\(\mu_a = \frac{\sum r_t}{|H_a|}\\) using Kish's effective sample sizes (\\(n_a^+, n_a^-\\)) and variance hyperparameter \\(\sigma \approx 10^5\\), preventing small-sample noise from causing degenerate bandit loops [12, 14–16].
3. **Short-Window Reward Filtering:** Restricts reward evaluation to a **2-hour window** following the notification to minimize noise from organic (non-notification-driven) app opens [4].
4. **Continuous 5% Uniform Random Holdout:** Maintains a permanent 5% uniform random arm selection policy in production to collect unconfounded evaluation data and prevent high importance weighting variance [15, 16].

---

### **(F) Deployment and Production Dataset Evidence**

* **Production Deployment:** Deployed live in production at **Duolingo** optimizing millions of daily push reminders and practice emails, evaluated via a continuous **5% uniform holdout set** and a large-scale online A/B test [1, 15, 17].
* **Quoted Numbers from the Source:**
  * **Offline Evaluation Scale:** Captured **34 days** of historical uniform random logs divided into a **15-day training set (88 million rows)** and a **19-day test set (114 million rows)** [21, Table 3].
  * **Offline Relative Lifts over Uniform Random Baseline (Table 5, Table 6, Table 7):**
    * *Template-only arms:* **+1.2% relative lift** [18].
    * *Template + UI Language arms:* **+1.8% relative lift** (\\(0.1318\\) vs. \\(0.1295\\)) [24, Table 6].
    * *Template + UI Language with Recency Penalty (\\(\gamma = 0.017, h = 15\\) days):* **+1.9% relative lift** (\\(0.1320\\) vs. \\(0.1295, p < 0.1\\)) [25–27, Table 6].
    * *Re-use Last Template policy:* **-0.5% regression** (\\(0.1289\\) vs. \\(0.1295\\)) [27, Table 6].
    * *Softmax exploration (\\(\tau = 0.0025\\)):* **+1.9% relative lift** (\\(0.1319\\) vs. \\(0.1295\\)), preserving \\(>90\%\\) of argmax potential gain while maintaining **17% exploration** [28, 30, Table 7].
  * **Live Operational Production A/B Test Results (Table 8):**
    * **Daily Active Users (DAUs):** **+0.5%** (\\(p < 0.05\\)) [1, 32, Table 8].
    * **Total Lessons Completed:** **+0.4%** (\\(p < 0.05\\)) [32, Table 8].
    * **Existing User D1 Retention:** **+0.5%** (\\(p < 0.05\\)) [32, Table 8].
    * **Existing User D7 Retention:** **+0.2%** (not statistically significant) [32, Table 8].
    * **New User D1 Retention:** **+2.2%** (\\(p < 0.05\\)) [1, 32, Table 8].
    * **New User D7 Retention:** **+2.0%** (\\(p < 0.05\\)) [32, Table 8].
  * **5-Month Long-Term Holdout Verification:** Re-evaluation after 5 months showed the 95% bandit policy maintained **2.5% higher reward** than the 5% uniform holdout set [15, 19].
  * **Small-Sample Variance Statistics:** 90% of large arms (\\(>100,000\\) effective sample size) fell within \\(\pm 3.4\%\\), whereas **38% of small-sample arms** had dubious scores outside \\(\pm 5\%\\) [20].
  * **Empirical Bayes Hyperparameter:** Variance hyperparameter \\(\sigma \approx 10^5\\) [21].

---

💡 *Would you like to explore how Duolingo's recovering recency penalty or sleeping arm relative score (\\(\hat{s}_a\\)) could be adapted to prevent repetitive profile recommendations or push fatigue in your dating app's candidate ranker?*

---

### Surrogate for Long-Term User Experience in Recommender Systems [1]
`2022_KDD_NA_Surrogate-Long-Term-User-Experience.md`
**Source:** https://dl.acm.org/doi/pdf/10.1145/3534678.3539073  

### **Source Evaluation: *Surrogate for Long-Term User Experience in Recommender Systems***
*(Wang et al., Google Research / Brain Team, KDD 2022: `https://doi.org/10.1145/3534678.3539073`)* [1, 2]

---

### **(A) Q1 or Q2 or Both or Neither?**
* **Neither.** [2-4]
* **Explanation:**
  * **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** Published in August 2022 at KDD 2022 (`KDD '22`), which falls outside the 2025-01 to 2026-09 window [2]. Furthermore, it evaluates a reward surrogate framework for Reinforcement Learning (RL) recommenders rather than an industry multi-touch attribution (MTA) measurement system [3-6].
  * **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper identifies medium-term user behavioral patterns (such as entropy diversity and homepage revisit times) to serve as multiplicative reward surrogates in REINFORCE RL recommender systems [3, 7-9], rather than attributing overall retention or active days across historical interaction sequences.

---

### **(B) Q2 Class**
* **Classification:** **NOT** [3, 6, 8, 10]
* **Justification:** The paper presents an RL reward transformation framework (REINFORCE with multiplicative surrogate multipliers based on medium-term behaviors like entropy-based diversity \\(D_{\text{entropy}}\\) and homepage revisit speed \\(T_{\text{revisit}}(\text{Home})\\)) [6, 8, 9]. It does **not** publish or calculate a per-exposure retention credit table.

---

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction credit table.** [8, 11-13]
* **Target Outcome:** At recommendation serving time, the immediate engagement reward \\(R_{0t}(s_t, a_t)\\) of a recommended item \\(a_t\\) is modulated by a medium-term surrogate multiplier [8, 9]:
  1. *Entropy Diversity Surrogate:* \\(R_t(s_t, a_t) = R_{0t}(s_t, a_t) \cdot \exp\left[ m \left(D_{\text{entropy}}(S_t) - D_{\text{entropy}}(S_{t-1})\right) \right]\\) (where \\(m = 5\\)) [8].
  2. *Homepage Revisit Surrogate:* \\(R_t(s_t, a_t) = R_{0t}(s_t, a_t) \cdot \left[1 + c \cdot \mathbb{1}(T_{\text{revisit}}(S, \text{Home}) < T_0)\right]\\) (where \\(c = 10\\)) [9].
* If the recommended item is not consumed (\\(R_{0t} = 0\\)), the surrogate multiplier has zero effect [13].

---

### **(D) Replacing Last-Touch N7 → Latest Swipes**
* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% of the binary N7 retention label to recent interactions post-hoc, ignoring early interactions and failing to encourage healthy medium-term user habits [14, 15]. This paper replaces post-hoc last-touch attribution with **medium-term behavioral surrogates** (e.g., consumption diversity or return frequency) integrated directly into the recommender's reward function [3, 8, 15]. Instead of waiting 7 or 150 days to observe long-term retention directly, the system nudges user behavior toward sustainable engagement habits during live interactions [3, 15].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Immediate Engagement Base Reward (\\(R_{0t}\\)):* Immediate right-swipe, mutual match, or initial messaging interaction [8, 11].
  2. *Sequential Diversity / Discovery Surrogate:* Modulates candidate profile scores by whether right-swiping/matching a candidate profile broadens the user's category/interest diversity (e.g., across hobbies, personality traits, or distance buckets) over a 2-week window (\\(D_{\text{entropy}}\\)) [8].
  3. *Homepage / App Revisit Surrogate:* Boosts base match/swipe rewards if the interaction leads to high-quality messaging conversations that bring the user back to the app's home feed within threshold time \\(T_0\\) [9].

---

### **(E) Selection-Bias & Confounding Handling**
1. **Random Forest Feature Importance Slicing:** Trains Random Forest classifiers across stratified user activity slices (based on 14-day consumption volume) to isolate surrogates (entropy diversity and homepage revisit times) whose feature importance remains robust across user distributions, reducing spurious correlations [7, 16, 17].
2. **Sequential Delta Features (\\(D^{\text{diff}}\\)):** Incorporates differential behavior features between 14-day time buckets (e.g., \\(D_{\text{entropy}}^{\text{diff}}\\), \\(T_{\text{revisit}}^{\text{diff}}\\)) to capture evolving behavioral shifts while controlling for baseline visiting frequency confounding [16, 18].
3. **Off-Policy Importance Sampling:** Corrects for off-policy distribution shift between the learned policy \\(\pi_\theta(a \mid s)\\) and logging behavior policy \\(\beta(a \mid s)\\) during batch REINFORCE training [12].

---

### **(F) Deployment & Production Dataset Evidence**
* **Production Deployment:** Fully deployed live in online A/B testing on a large industrial recommendation platform (Google / YouTube) serving **billions of users** [5, 19, 20].
* **Longitudinal Dataset:** User visiting logs over a **20-week (5-month) period** covering **2 million low-frequency users** (extended to 40 weeks for transition time distribution analysis) [21-23].
* **Quoted Numbers from the Source:**
  * **Sparsity:** Among the **2 million users** who started as low-frequency users, only about **2.3%** of them became high-frequency users at the end of 5 months [22].
  * **Time Horizon:** The average time for a low-frequency user to become high-frequency is **15.32 weeks** (median **14 weeks**) [23].
  * **High-Quality Consumption:** Transitioning users more than doubled their high-quality consumption ratio from **<20.0% to 46.0%** [24].
  * **Persistent Topics:** Persistent topic ratio more than tripled from **15.3% to 46.9%** among transitioning users [25].
  * **Predictive Modeling AUC:** Random Forest feature importance modeling achieved an AUC of **0.57 to 0.63** across user activity slices (**0.61 overall**) [17].
  * **Live Online A/B Test Results (Entropy Diversity Surrogate, \\(m = 5\\)):** Statistically significant improvements in top-line user enjoyment (**~+0.14%** relative lift at peak) and long-term user visiting frequency (**~+0.12%** relative lift) [20].
  * **Live Online A/B Test Results (Homepage Revisit Surrogate, \\(c = 10\\)):** Delivered statistically significant lifts in overall user visiting frequency (**+0.08% to +0.12%**), low-frequency user segment visiting frequency (**+0.25% to +0.30%**), homepage visits (**+0.40% to +0.55%**), and satisfied consumptions (**+0.20% to +0.30%**) [13, 26].
  * *Not specified in source*: Specific duration and completion ratio thresholds (\\(X, Y, Z, A, B, T_0, c_1 \dots c_5\\)) were omitted from publication for business-compliance reasons [11, 21, 27, 28].

---

💡 *Would you like to explore how Google's multiplicative surrogate reward structure or entropy-based diversity metric could be adapted to modulate candidate profile ranking scores for your dating app?*

---

### Long-run User Value Optimization in Recommender Systems through Content Creation Modeling [1]
`2022_arXiv_NA_Long-run-User-Value-Optimization-Meta.md`
**Source:** https://arxiv.org/pdf/2204.11421.pdf  

### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Long-run User Value Optimization in Recommender Systems through Content Creation Modeling*
* **Authors:** **Akos Lada**, **Xiaoxuan Liu**, **Jens Rischbieth**, **Yi Wang**, and **Yuwen Zhang**
* **Affiliation:** **Facebook (Meta)**, Menlo Park / Seattle, USA
* **Year & Venue:** Published in **2022** (arXiv pre-print: `arXiv:2204.11421`, submitted April 2022) / Meta Research.

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Standard recommender systems optimize short-term, single-period individual user satisfaction (immediate clicks, likes, or watch time). This myopic focus ignores dynamic multi-period user-to-user spillovers and creator supply incentives. Showing content only to maximize immediate 1-period engagement fails to reward content creators who produce long-term value. As a result, creators reduce or stop creating content, shrinking future inventory and degrading overall long-term platform user value [3–6, 9–10].
* **Key Contributions:**
  1. **Microeconomic Foundation & Proof:** Formalizes multi-period discounted user value maximization and proves (**Theorem 1**) that short-horizon 1-period ranking (\\(R'_{it}\\)) is strictly sub-optimal compared to multi-period ranking (\\(R''_{it}\\)) whenever inter-temporal content creation spillovers exist [3–4, 6–12].
  2. **Two-Step Causal ML Framework:** Combines a producer-level distribution-boosting A/B experiment with heterogeneous treatment effects (HTE) machine learning (T-Learner / Meta-Learner using GBDTs or Neural Networks) to estimate individual creator posting elasticity when receiving engagement [2, 13–15].
  3. **Production Deployment on Facebook Feed:** Fully deployed in production on **Facebook App's Feed ranking system** via Meta's **FbLearner** ML platform, scoring content producers and feeding producer scores directly into production feed ranking [2, 16–18].

---

### **(3) Proposed Method or Architecture in Detail**
* **Two-Step Causal Framework:**
  1. *Experimental Variation:* Runs an A/B test boosting the distribution of a randomly selected 2% of content producers to their followers while keeping a 2% control group [1-3].
  2. *Heterogeneous Treatment Effect Estimation:* Fits separate treatment and control models (\\(m_{\text{treatment}}\\), \\(m_{\text{control}}\\)) using pre-experiment producer features \\(x_i\\) (e.g., follower count, historical posting frequency) via Gradient Boosted Decision Trees (GBDTs) or Neural Networks. The Individual Treatment Effect (ITE) is calculated as:
     \\[\hat{\tau}_i = m_{\text{treatment}}(x_i) - m_{\text{control}}(x_i)\\]
  3. *Production Ranking Integration:* Generates producer-level scores based on \\(\hat{\tau}_i\\) via Meta's **FbLearner** ML system and feeds them into the Feed ranking system. Content from producers who create more valuable content in response to engagement receives a distribution boost [1, 4, 5].
* **Credit Assignment Mechanics:**
  * Does **not** perform per-touchpoint multi-touch attribution or fractional credit assignment across user interaction logs.
  * Instead, it assigns a **producer-level uplift score** based on the creator's estimated content creation elasticity (\\(\hat{\tau}_i\\)) when receiving engagement [1, 4, 6].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets & Scale:** Production user interaction logs and content producer activity logs from the Facebook App.
* **Production Deployment:** Fully deployed live in production on **Facebook App's Feed ranking system** via Meta's **FbLearner** ML platform [1, 4, 5].
* **Comparison Baselines:**
  * Short-term myopic ranking algorithms (\\(R'_{it}\\)) that optimize only 1-period individual user satisfaction without modeling producer feedback loops [6–8, 10–12].
  * Control group of producers in the A/B experiment who did not receive the distribution boost [1-3].

---

### **(5) Key Quantitative Results with Numbers**
* **Producer Distribution Boosting A/B Experiment:**
  * Boosted **2% of producers at random**, compared against a **2% control producer group** [3].
  * Treated producers received a **+26% increase in likes** and a **+9% increase in comments** compared to control [3].
  * In response to engagement, treated producers increased their content posting frequency by **+0.19% on average** [3].
* **Production Retraining Cadence:** Retrained every **1 week** on a small holdout producer group to maintain model freshness and guard against data drift [16–17].

---

### **(6) Limitations, Failure Modes, or Negative Results**
1. **Inefficacy in Low-Discount or Homogeneous Environments:** If the discount factor \\(\beta\\) is near zero, or if short-run top creators are identical to long-run top creators, multi-period optimization yields no improvement over myopic short-term ranking [7].
2. **Distribution Volatility & Producer Frustration Risk:** Unstable producer scores cause distribution volatility, making it difficult for creators to predict reach or justify investing effort into high-quality content. To mitigate this, models must rely on stable pre-experiment features [4].
3. **Dependence on Continuous Holdout Data:** Requires maintaining a permanent producer holdout to collect control data for periodic retraining; without weekly retraining, the model degrades [16–17].
4. **Scope Constraint:** Evaluation was restricted to connected distribution (feed distribution to existing followers) rather than un-connected recommendation surfaces [3].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Kohavi et al. (2013) [Ref 20]:** *Online controlled experiments at large scale* (A/B testing methodology).
2. **Künzel et al. (2019) [Ref 20]:** *Metalearners for estimating heterogeneous treatment effects using machine learning* (T-Learner / Meta-Learner architecture).
3. **Wager & Athey (2018) [Ref 22]:** *Estimation and inference of heterogeneous treatment effects using random forests*.
4. **Rubin (2011) / Pearl (2009) [Refs 21, 22]:** *Causal inference using potential outcomes* & *Causality* (Potential outcomes & causal inference foundation).
5. **Friedman (2001) [Ref 19]:** *Greedy Function Approximation: A Gradient Boosting Machine* (GBDTs for Meta-Learners).
6. **Peysakhovich & Eckles (2018) [Ref 21]:** *Learning causal effects from many randomized experiments using regularized instrumental variables*.
7. **Mas-Colell & Whinston (1995) [Ref 21]:** *Microeconomic Theory* (Microeconomic inter-temporal optimization foundation).

---

💡 *Would you like to explore how Meta's producer elasticity model (T-Learner CATE estimation) could be adapted to identify high-response active profile creators for your dating platform's ranker?*

---

### Incrementality-Focused Messaging Measurement (Netflix) — stub
`2023_NetflixBlog_NA_Incrementality-Focused-Messaging-Measurement.md`
**Source:** https://medium.com/notificationsblog/incrementality-focused-messaging-measurement-all-the-time-everywhere-94ef0c229368  

- **Answers:** Q2 adjacent (notification incrementality), not swipe MTA.
- **Q2 class:** PARTIAL (touchpoint holdback, not in-app item).
- **Per-interaction credit:** per **message** incremental viewing, not per-swipe N7.
- **Last-touch replacement:** holdout incrementality is a calibration device for observational credit, analogous to Amazon Ads MTA's RCT calibration, not a full multi-touch retention labeler.
- **Transfer rating:** adaptable as a **notification-level** incrementality fixture, not as swipe attribution.

**Low project relevance** for swipe-level N7 labels; useful as a measurement pattern.

---

