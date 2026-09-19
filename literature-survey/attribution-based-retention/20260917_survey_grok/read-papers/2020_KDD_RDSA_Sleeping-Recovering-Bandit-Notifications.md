# A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications [1]

**Source:** https://research.duolingo.com/papers/yancey.kdd20.pdf  
**Date analyzed:** 2026-09-18  
**NLM source id:** `3f40b05f-169b-4e36-b317-fdadf7a86bc1`  
**Queue id:** G25  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**
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
**Priority:** see queue.md `G25`
