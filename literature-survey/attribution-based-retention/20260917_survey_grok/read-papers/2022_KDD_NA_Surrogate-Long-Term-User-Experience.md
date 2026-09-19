# Surrogate for Long-Term User Experience in Recommender Systems [1]

**Source:** https://dl.acm.org/doi/pdf/10.1145/3534678.3539073  
**Date analyzed:** 2026-09-18  
**NLM source id:** `cb0d9351-5064-4c9b-b669-e5f25fe0203f`  
**Queue id:** G21  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**

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
**Priority:** see queue.md `G21`
