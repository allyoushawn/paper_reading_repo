# Relevance index 6/10 — Project Relevance sections of all cards (generated)

### AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems [1, 2]
`2025_WWW_AURO_Adaptive-User-Retention-Optimization.md`
**Source:** https://arxiv.org/pdf/2310.03984.pdf  

### **Part 1: Detailed Technical Breakdown of the Source**

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems* [1, 2]
* **Authors:** **Zhenghai Xue**¹, **Qingpeng Cai**\*², **Bin Yang**², **Lantao Hu**², **Peng Jiang**², **Kun Gai**³, and **Bo An**¹ (*\*Corresponding author*) [1–2]
* **Author Affiliations:**
  1. **Nanyang Technological University**, Singapore / Skywork AI [1–2]
  2. **Kuaishou Technology**, Beijing, China [1]
  3. **Unaffiliated**, Beijing, China [1]
* **Year:** **2025** (Published at WWW ’25; arXiv pre-print `arXiv:2310.03984`) [3–4]
* **Venue:** *Proceedings of the ACM Web Conference 2025 (WWW ’25)*, April 28–May 2, 2025, Sydney, NSW, Australia [3–4]

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Reinforcement Learning (RL) algorithms for user retention struggle with environment non-stationarity driven by shifting user behavior patterns (such as fluctuating interaction rates and user return-time distributions) [2-5]. Shifting environments cause policy performance degradation, while "implicit cold-start" scenarios force policies to continually interact with users exhibiting novel behaviors [3, 6].
* **Key Contributions:**
  1. **AURO Framework:** Formulates user retention under environment non-stationarity using Hidden Parameter MDPs (HiP-MDP) [3, 7].
  2. **Value-Based State Abstraction Module:** Introduces a state abstraction network trained with a value-based contrastive loss (\\(J(\phi)\\)) [2, 16–17]. It aligns latent outputs with estimated state values (\\(V\\)) to detect environmental changes universally and notify the policy to adapt [3, 8, 9].
  3. **Guarded Online Exploration:** Implements optimistic exploration (\\(\nabla_a Q_{\text{UB}}\\)) combined with rejection sampling over candidate action particles to safely adapt to novel user behavior without causing user disengagement or churn [2, 27–30].
  4. **Industrial-Scale Deployment:** Fully launched on Kuaishou's short-video recommendation platform serving 25 million daily active users [3, 10].

---

#### **(3) Proposed Method or Architecture in Detail**

##### **MDP Formulation & Model Architecture**
* **HiP-MDP Formulation:** Models non-stationary environments using Hidden Parameter MDPs \\(\langle S, A, \Theta, T, r, \gamma, \rho_0 \rangle\\) where hidden parameters \\(\theta \sim \Theta\\) govern dynamic shifts [9–10].
  * **State Space (\\(s_t\\)):** Low-dimensional vector concatenating user features, item features, and interaction history (processed via embedding layers and Transformers) with state abstraction vector \\(\phi(s_t)\\) [15, 18–19].
  * **Action Space (\\(a_t \in \mathbb{R}^k\\)):** \\(k\\)-dimensional continuous action vector used to compute final ranking scores alongside a scoring model [8–9].
  * **Retention Reward (\\(r_t\\)):** Assigned at the final step of an episode as \\(r_t = \lambda \times \text{user return time}\\) (set to \\(0\\) for intermediate steps; discount factor \\(\gamma = 0.9\\), \\(\lambda = -0.1\\)) [11, 12].
* **Value-Based State Abstraction Loss (\\(J(\phi)\\)):** Ranks a batch of states by their state value function \\(V(s)\\), divides them into \\(n\\) categories (\\(n=4\\)), and minimizes:
  \\[J(\phi) = \frac{2B}{n} \sum_{k=0}^n \sum_{i} \|\phi(s_i) - \bar{\phi}_k\|_2^2 - \frac{B^2}{n^2} \sum_{k=0}^n \sum_{m>k} \|\bar{\phi}_k - \bar{\phi}_m\|_2^2\\]
  where \\(\bar{\phi}_k\\) is the moving average abstraction vector for category \\(k\\) [21, 23–25].
* **Guarded Online Exploration Module:** Generates \\(N\\) candidate action particles around base policy action \\(a_T\\) along the gradient of upper-bound Q-value \\(Q_{\text{UB}}(s, a) = \mu_Q(s, a) + \beta \sigma_Q(s, a)\\):
  \\[a_k = a_T + k \delta \frac{\nabla_a Q_{\text{UB}}(s, a)}{\|\nabla_a Q_{\text{UB}}(s, a)\|}\\]
  and selects exploration action \\(a_E = \arg\max_{a_k} \mu_Q(s, a_k)\\) via rejection sampling [27–30].

##### **Credit Assignment Mechanics**
* Credit is assigned at the **episode trajectory level** using the delayed user return time as an episode-ending retention reward \\(r_t = \lambda \times \text{user return time}\\) [11].
* The framework does **not** perform fractional multi-touch attribution or per-item credit decomposition across historical interaction logs.

---

#### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets & Simulator:**
  1. **KuaiSim Retention Simulator:** Simulates long-term user retention, session leave probabilities, and multi-day return-time distributions on short-video platforms [31–32, 49].
  2. **MovieLens-1M Dataset:** Modified for offline evaluation using Normalized Capped Importance Sampling (NCIS) and behavior cloning (BC) loss [31, 43–44].
* **Production Deployment:** Deployed live in production on Kuaishou's candidate-ranking pipeline serving **25 million daily active users** and **billions of daily interactions** over a **2-week online A/B test** [10].
* **Comparison Baselines:**
  * *Non-RL / Heuristic:* CEM, DIN [13-15].
  * *Standard Off-Policy RL:* DDPG, TD3, SAC [13-15].
  * *Exploration-Focused RL:* OAC, RND [13-15].
  * *Context Encoder / Meta-RL:* ESCP [13-15].
  * *Retention-Oriented RL:* RLUR, OSPIA, RL-LTV [13-15].

---

#### **(5) Key Quantitative Results with Numbers**
* **KuaiSim Retention Simulator Benchmark (at 20K Timesteps, Table 2):**
  * **Average Return Days (lower is better):** **AURO = 1.531 ± 0.058** vs. RLUR (**1.706**), ESCP (**1.705**), OSPIA (**1.726**), SAC (**1.810**), TD3 (**1.772**), CEM (**1.858**) [13].
  * **Return Rate at Day 1 (higher is better):** **AURO = 0.824 ± 0.018** vs. RLUR (**0.765**), OSPIA (**0.803**), ESCP (**0.764**), TD3 (**0.738**), DIN (**0.755**) [13].
  * **Retention Reward (higher is better):** **AURO = -0.015 ± 0.000** vs. baselines (**-0.017 to -0.019**) [13].
* **MovieLens-1M Offline Evaluation (Table 3):**
  * **Retention Reward:** **AURO+BC = 1.798 ± 0.032** vs. RLUR+BC (**1.784**), ESCP+BC (**1.755**), TD3+BC (**1.714**), BC (**1.702**) [16].
* **Live Online Production A/B Test Results (vs. RLUR Baseline over 2 Weeks, Table 4):**
  * **7-Day Retention Rate:** **+0.138‰** permillage lift [17].
  * **App Dwell Time:** **+0.263‰** permillage lift (**AURO was the only algorithm to achieve positive dwell time gains**; TD3 regressed by **-0.685‰**, ESCP by **-0.115‰**) [46–47].
  * **Click-Through Rate (CTR):** **+3.260‰** permillage lift [17].
  * **Like Rate:** **+2.821‰** permillage lift [17].
  * **Comment Rate:** **+8.392‰** permillage lift (**nearly 5× higher** than TD3's +1.715‰) [46–47].
  * **Unlike / Hate Rate (lower is better):** **-1.874%** reduction [17].

---

#### **(6) Limitations, Failure Modes, or Negative Results**
1. **Omission of Immediate Feedback Balancing:** Focuses exclusively on optimizing long-term retention rewards without explicitly formulating or balancing immediate feedback trade-offs (e.g., CTR vs. retention) within the objective function [18].
2. **Vulnerability to Unprecedented / Adversarial User Behaviors:** If users display unprecedented behavior patterns (e.g., suddenly disliking all recommended content out of boredom), the state abstraction module may fail to adapt properly [18].
3. **Suboptimal Performance on Stubborn Users:** For stubborn users who strictly refuse to interact with unfamiliar content, optimistic exploration can result in inferior retention compared to greedy recommendation strategies [18].
4. **Reliance on Post-Processing Safety Filters:** In live deployment, RL recommendation outputs depend on downstream post-processing and filtering mechanisms to prevent inappropriate content from reaching users [19].

---

#### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Cai et al. (2023) [Ref 6 / RLUR]:** *Reinforcing User Retention in a Billion Scale Short Video Recommender System* (WWW ’23) [20].
2. **Wang et al. (2022) [Ref 42 / Surrogate]:** *Surrogate for Long-Term User Experience in Recommender Systems* (KDD ’22) [21].
3. **Fujimoto, van Hoof, & Meger (2018) [Ref 17 / TD3]:** *Addressing Function Approximation Error in Actor-Critic Methods* (ICML ’18) [22].
4. **Haarnoja et al. (2018) [Ref 18 / SAC]:** *Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor* (ICML ’18) [22].
5. **Luo et al. (2022) [Ref 30 / ESCP]:** *Adapt to Environment Sudden Changes by Learning a Context Sensitive Policy* (AAAI ’22) [23].
6. **Zhao et al. (2023) [Ref 49 / KuaiSim]:** *KuaiSim: A comprehensive simulator for recommender systems* (NeurIPS ’23) [24].
7. **Sutton & Barto (1998) [Ref 38 / RL Book]:** *Reinforcement Learning: An Introduction* [25].

---

### **Part 2: Dating App Retention Attribution Project Evaluation**

#### **(A) Q1 or Q2 or Both or Neither?**
* **Neither.**
* **Explanation:**
  * **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** Published in WWW 2025 (submitted 2023), which falls outside the 2025-01 to 2026-09 window [3–4]. Furthermore, it is an RL policy optimization framework for candidate ranking, not an industry multi-touch attribution (MTA) measurement system [3, 26].
  * **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** AURO optimizes a candidate ranking policy using RL based on episode-level user return time rewards (\\(r_t = \lambda \times \text{return time}\\)), rather than attributing N7 retention or active days back to individual in-app interaction touchpoints across past user logs [11, 26].

---

#### **(B) Q2 Class**
* **Classification:** **NOT**
* **Justification:** AURO is an offline/online RL policy optimization framework (HiP-MDP with state abstraction and guarded online exploration) that generates continuous action vectors for candidate item ranking [8–9, 16, 29]. It does **not** publish or compute a per-exposure retention credit table.

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction sequence credit.**
* **Target Outcome:** **Delayed Episode-Level User Return Time** (\\(r_t = \lambda \times \text{user return time}\\)) [11].

---

#### **(D) Replacing Last-Touch N7 → Latest Swipes**
* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% of an N7 retention label to recent swipes post-hoc, ignoring earlier interaction context and environmental shifts in user behavior. AURO replaces post-hoc rule assignment with **adaptive RL policy optimization** [3, 27]. It uses a value-based state abstraction network (\\(\phi(s)\\)) to detect shifting user behavior patterns and applies guarded online exploration (\\(\nabla_a Q_{\text{UB}}\\) with rejection sampling) to explore candidate recommendations safely without causing user churn [3, 8, 28].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *State (\\(s_t\\)):* Encodes user features, candidate profile features, and historical swiping/matching/chat events using embedding layers and Transformers, combined with state abstraction \\(\phi(s_t)\\) to detect shifts in user engagement/return behavior [15, 18–19].
  2. *Action (\\(a_t\\)):* Generates a \\(k\\)-dimensional continuous action vector \\(a_t\\) that scales scoring model weights when ranking candidate profile cards [26].
  3. *Guarded Exploration:* Generates candidate action particles around optimistic \\(Q_{\text{UB}}\\) and filters them via rejection sampling (\\(\mu_Q\\)) to explore novel candidate profiles safely without giving bad recommendations that lead to app abandonment [27–30].
  4. *Retention Reward (\\(r_t\\)):* Evaluates retention using the user's return-time delay (\\(r_t = \lambda \times \text{return time}\\)) [11].

---

#### **(E) Selection-Bias & Confounding Handling**
1. **Value-Based State Abstraction Loss (\\(J(\phi)\\)):** Aligns latent state representations with state value estimates (\\(V(s)\\)) to detect non-stationarity and distribution shifts across user behavior patterns [16–17, 20].
2. **Guarded Online Exploration with Rejection Sampling:** Evaluates candidate action particles against average Q-values (\\(\mu_Q\\)) to prevent risky exploratory actions from causing user disengagement [29–30].
3. **MovieLens-1M Offline Evaluation:** Uses Normalized Capped Importance Sampling (NCIS) and behavior cloning (BC) loss to handle off-policy evaluation bias [29].

---

#### **(F) Deployed or Production Dataset Evidence**
* **Production Deployment:** Fully launched in live production on Kuaishou's candidate-ranking pipeline serving **25 million daily active users** and **billions of daily interactions** over a **2-week online A/B test** [10].
* **Datasets & Numbers Quoted from Source:**
  * **KuaiSim Simulator Benchmark (Table 2):** Average Return Days = **1.531 ± 0.058** (vs. RLUR **1.706**), Day-1 Return Rate = **0.824 ± 0.018** (vs. RLUR **0.765**), Retention Reward = **-0.015 ± 0.000** (vs. baselines **-0.017 to -0.019**) [13].
  * **MovieLens-1M Offline Evaluation (Table 3):** Retention Reward = **1.798 ± 0.032** [16].
  * **Live Production A/B Test Results (vs. RLUR Baseline over 2 Weeks, Table 4):**
    * **7-Day Retention Rate:** **+0.138‰** permillage lift [17].
    * **App Dwell Time:** **+0.263‰** permillage lift (**AURO was the only algorithm to achieve positive dwell time gains**) [46–47].
    * **Click-Through Rate (CTR):** **+3.260‰** permillage lift [17].
    * **Like Rate:** **+2.821‰** permillage lift [17].
    * **Comment Rate:** **+8.392‰** permillage lift (**nearly 5× higher** than TD3's +1.715‰) [46–47].
    * **Unlike / Hate Rate:** **-1.874%** reduction [17].

---

💡 *Would you like to explore how AURO's value-based state abstraction or guarded online exploration module could be adapted to optimize 7-day user retention for your dating app?*

---

### Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems [1]
`2026_AAAI_RevisitMTL_Save-Revisit-Retain.md`
**Source:** https://arxiv.org/pdf/2511.18013.pdf  

### **Source Evaluation: Save, Revisit, Retain (Pinterest Framework)**
*(Jiang et al., Pinterest Inc., AAAI 2026 / arXiv: `2511.18013`)* [1]

---

### **(A) Q1 or Q2 or Both or Neither?**
* **Answer:** **Both** (Q1 and Q2) [1, 8–9, 13, 35].
* **Explanation:** 
  * **Q1 (Industry/Production Attribution 2025–2026):** **Yes.** Deployed in production on Pinterest's Related Pins surface serving **500+ million users**, with a large-scale online A/B experiment conducted from **April 29, 2025 to June 26, 2025** [1-3].
  * **Q2 (Attributing Retention / Engagement / Days-Active to In-App Interactions):** **Yes.** It establishes a surrogate attribution linkage that connects item-level save actions ("repins") on candidate items to multi-day return visits ("revisitations" on personal profiles over a 0–6 day window) as a direct proxy for 28-day active user retention [1, 5, 17, 23–25].

---

### **(B) Q2 Class**
* **Classification:** **PARTIAL** [1, 5, 10, 13, 21–25].
* **Justification:** The paper creates an item-level surrogate linkage and multi-task prediction head (\\(P(\text{revisit} \mid q, \theta)\\)) connecting content exposures/saves to 0–6 day profile revisitations and active days [5, 23–25]. It explicitly acknowledges user activity and intent confounders [1, 4], but it does **not** estimate an identified causal Multi-Touch Attribution (MTA) sequence decomposition across multiple sequential touches [5, 6].

---

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Item/Candidate-level Score Integration** (not sequence-level fractional attribution percentages) [21–22, 25–26]. It predicts the probability \\(P(c_{\text{RP\&RV}} \mid q, \theta)\\) that a candidate item will be saved and revisited, multiplying this probability by a business utility weight (\\(u_{\text{RP\&RV}}\\)) to add directly into the candidate's final ranking score [22, 25–26]:
  \\[\text{score} = \sum_{i \in L} u_i \cdot P(c_i \mid q, \theta) + u_{\text{RP\&RV}} \cdot P(c_{\text{RP\&RV}} \mid q, \theta)\\]
* **Target Outcome:** **Revisitation surrogate label (\\(c_{\text{RP\&RV}}\\))**, combining three cross-surface return events over a 0–6 day window [23–25]:
  1. *Same-day Revisitation Impression (`1dRevImpre`)* [7].
  2. *Same-day Revisitation Grid-click (`1dRevGrid`)* [7].
  3. *7-day Revisitation Grid-click (`7dRevGrid`)* (zooming into saved content 0–6 days post-save) [7].
  * *Downstream Impact:* These surrogate events strongly correlate with **28-day active days** and site-wide user retention [17–18, 38].

---

### **(D) Replacing Last-Touch N7 → Latest Swipes**
* **How it Improves on Last-Touch:** Last-touch assigns 100% credit to the final swipe before Day 7, ignoring earlier high-intent actions (matches, messaging) and failing to predict whether a current interaction will generate future return behavior [4, 5]. Pinterest's approach replaces last-touch heuristics by predicting the **probability of delayed return engagement** at candidate exposure time and incorporating that long-term retention value directly into the ranking score [7, 25–26].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  * **Initial High-Intent Action (Save/Repin Analogue):** A swipe resulting in a mutual match or saved profile.
  * **Delayed Return Event (Revisitation Analogue):** The user opening the match profile or initiating/continuing a 4-way conversation within a **0–6 day window** post-match (`1dRevImpre`, `1dRevGrid`, `7dRevGrid`) [23–24].
  * **Ranker Scoring Integration:** During ranking, candidate profiles are scored not just on immediate swipe probability \\(P(\text{like})\\), but on \\(P(\text{like}) + u_{\text{retention}} \cdot P(\text{match \& 0–6d conversation})\\), ensuring the ranker prioritizes candidate profiles that spark lasting 7-day retention [22, 25–26].

---

### **(E) Selection-Bias & Confounding Handling**
* **Confounders Acknowledged:** The authors explicitly identify attribution noise caused by shifting user intent across sessions, platform notifications, content quality, and hyper-active user bias (where engaged users save and revisit disproportionately more) [1, 4, 8, 9].
* **Handling Mechanisms:**
  1. **Surrogate Causal Filtering:** Restricts attribution to exact `(User ID, Item ID)` pairs joined across a strict 0–6 day window (`timesave < timerevisit < timesave + 7 days`), filtering out unrelated cross-session browsing noise [5–6, 31].
  2. **Intent Precision Filtering:** Focuses multi-day labels on intentional grid-clicks (`7dRevGrid`) rather than passive impressions (`1dRevImpre`), as grid-clicks show significantly higher correlation with 28-day active days [10, 11].
  3. **Unique User Feature Normalization:** Constructs historical Pin performance features (`Pin perf`) tracking both total action counts and **unique user counts** over 7, 30, and 90 days to prevent single enthusiastic users from skewing retention signals [27–28].
  * *Note:* The paper does not use formal propensity score weighting (IPW) or counterfactual causal bounds, citing user activity imbalance as an ongoing limitation for future work [9].

---

### **(F) Deployment & Production Quantitative Results**

* **Deployment Status:** Fully deployed in production on Pinterest's Related Pins surface serving **500+ million monthly active users** across ~**50% of overall platform traffic** [1, 2, 12].
* **Dataset & Scale:**
  * *Offline Training Set:* 27 days (~**6.6 billion samples**) for training, 1 day for calibration, and 3 days (~**700 million samples**) for evaluation [13].
  * *Online A/B Experiment:* **24 million users** (12M control, 12M treatment) evaluated continuously over 2 months (April 29, 2025 – June 26, 2025) [3].
* **Quoted Quantitative Results:**
  * **Online A/B Testing Lifts (Table 2):**
    * **Active Users (Site-wide Retention):** **+0.10% volume** (\\(p < 0.05\\)) and **+0.08% propensity / unique users** (\\(p < 0.05\\)) [1, 14, 15].
    * **Revisitation Metrics:** `1dRevImpre` **+0.65% volume** (\\(p < 0.05\\)), **+0.93% propensity** (\\(p < 0.05\\)); `1dRevGrid` **+0.95% volume** (\\(p < 0.05\\)), **+1.17% propensity** (\\(p < 0.05\\)); `7dRevGrid` **+1.18% volume** (\\(p < 0.05\\)), **+1.42% propensity** (\\(p < 0.05\\)) [14].
    * **Platform Engagement:** **+0.94% Repin volume** (\\(p < 0.1\\)), **+0.64% Repin propensity** (\\(p < 0.01\\)), **+0.41% Long Sessions (\\(\ge 5\\) min)** (\\(p < 0.01\\)), **+0.35% Web/API Requests** (\\(p < 0.01\\)), **+0.53% Time Spent on Related Pins**, **+0.68% Time Spent on Own Profile**, and **+0.39% Total App Time Spent** [36–38].
  * **Offline Model Performance Lifts (Table 1):**
    * *Revisitation Head:* **+40.15% NDCG@3**, **+43.44% MAP@3**, **+27.62% Recip Rank@3**, **+35.40% Recall@3**, **+21.62% Pairwise Accuracy**, and **+0.65% Hits@3** over production baseline [33–34].
    * *Repin Head:* **+0.1279% NDCG@3**, **+0.0645% MAP@3**, **+0.2705% Recall@3**, and **+0.59% Hits@3** [33–34].
    * *Optimal Task Utility Weight:* \\(u_{\text{RP\&RV}} = 1.27 \times u_{\text{Repin}}\\) [13].
  * **Revisitation Behavior Decay Rates:**
    * *Daily User Revisitation Decay:* Day 0 impression rate **14.6%** \\(\rightarrow\\) Day 1 **19.5%** \\(\rightarrow\\) Day 9 **8.7%**; Day 0 grid-click rate **6.6%** \\(\rightarrow\\) Day 1 **7.7%** \\(\rightarrow\\) Day 9 **1.6%** [16].
    * *Volume Decay:* Grid-click revisitation volume starts at **4.7%** on day 0, drops by half to **2.2%** on day 1, **1.1%** on day 2, **0.5%** by day 5, and **0.3%** by day 9 [17].
    * *Label Volume relative to Daily Repins:* `1dRevImpre` = **25.8%**, `1dRevGrid` = **4.7%**, `7dRevGrid` = **9.0%** [7].

---

💡 *Would you like to explore how Pinterest's cross-surface surrogate join pipeline or MMoE revisitation utility weights (\\(u_{\text{retention}}\\)) could be implemented for your dating platform's candidate profile ranker?*

---

### Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?
`2026_CIKM_LOTUS_Meaningful-Touchpoints-Conversion-Attribution.md`
**Source:** https://arxiv.org/pdf/2608.28649.pdf  

**(A) Q1 or Q2 or both or neither?**  
**Q1 only** [1-3]. The paper (*"Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?"*, Wu et al., CIKM 2026) covers industrial production conversion attribution at Taobao & Tmall Group of Alibaba [1, 3, 4]. It does **not** cover Q2, as it focuses strictly on e-commerce purchase conversion attribution rather than user retention, engagement, or active-day attribution [2, 5, 6].

---

**(B) Q2 Class**  
**NOT** [2, 5, 6]. The paper does not publish per-touch retention or active-day credit tables; its target outcome is e-commerce product purchase conversion [2, 5, 6].

---

**(C) Does it produce per-interaction credit? For what outcome?**  
**Yes** [2, 6, 7]. It produces fractional credit weights (\\(\sum w_i = 1\\)) across selected touchpoints for **e-commerce purchase conversion events** (\\(C\\)) [6, 7]. The system operates in two stages: Stage 1 selects meaningful touchpoints (categorized as Explicit, Implicit, or Irrelevant), and Stage 2 distributes normalized credit weights across the selected touchpoints [6, 7]. It does not attribute retention or active days [5, 6].

---

**(D) How would this replace or improve last-touch N7→latest swipes?**  
Instead of using rigid last-touch rules that assign credit solely to the latest interaction, this framework uses an LLM-driven semantic selector (**LOTUS**) with pairwise prompting to inspect full behavior sequences and recover **implicitly-related touchpoints** (such as functional complementarity or scenario alignment) [3, 5-8].  
* **Mapping to Dating Context:** Applied to dating retention, an LLM-based selector would evaluate the full interaction sequence (earlier swipes, mutual matches, and 4-way messaging conversations) rather than defaulting to the most recent swipe [6, 7]. It would identify semantically meaningful interactions—such as deep messaging exchanges or matches based on shared interests—and allocate fractional credit across all contributing touchpoints rather than crediting only the latest swipe [6-8].

---

**(E) Selection-bias handling?**  
**Not specified in source** [3, 5, 9]. The paper focuses on evaluating LLM semantic reasoning and prompting protocols (pairwise vs. listwise) for touchpoint selection rather than applying propensity weighting, inverse-propensity scoring, or causal debiasing for user swiping/activity selection bias [5, 9, 10].

---

**(F) Deployed or production dataset?**  
**Yes, both a benchmark dataset and a production deployment are reported** [3, 11, 12]:
* **SILVA Benchmark Dataset:** Constructed from Taobao & Tmall (Alibaba); contains **1,000 unique conversion events** and **69,680 preceding touchpoints** collected within a **3-day lookback window** [12]. Human annotations achieved Fleiss’ \\(\kappa > 0.70\\) [13].
* **Annotated Touchpoint Distribution:** **19.09% Explicitly-related**, **14.91% Implicitly-related**, and **66.00% Irrelevant** touchpoints [12, 14].
* **LLM Selection Benchmark Performance:** Pairwise prompting achieved an average explicit F1 of **0.8979** and implicit F1 of **0.4929** (highest implicit F1: **0.5426** by GPT-5.5; highest explicit F1: **0.9095** by Gemini-3.1-Pro) [15, 16]. Pairwise prompting outperformed listwise prompting, raising overall F1 from **0.6490 to 0.6954 (+4.64 pp gain)** [10].
* **Production Deployment & CVR Model Gains:** Tested on a production CVR prediction model serving **hundreds of millions of daily active users** at Alibaba [3, 11, 12]. LOTUS achieved an absolute **+0.35 pp GAUC gain** over the production in-shop baseline (`Base`) and **+0.15 pp GAUC gain** over the heuristic rule-based competitor (`CABB`) [3, 11]. The authors note that an absolute GAUC improvement of **0.1 pp** is empirically sufficient to drive substantial growth in online sales and ad revenue [3, 17].

---

💡 *Would you like to explore how an LLM-driven pairwise selection protocol could be adapted to identify implicit high-value interactions (e.g., messaging engagement or match quality) for your dating platform's N7 retention ranker?*

---

