# AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems [1, 2]

**Source:** https://arxiv.org/pdf/2310.03984.pdf  
**Date analyzed:** 2026-09-18  
**NLM source id:** `db4edc42-fa93-4822-8a60-f0c7116ffa57`  
**Queue id:** G9  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems* [1, 2]
* **Authors:** **Zhenghai Xue**¹, **Qingpeng Cai**\*², **Bin Yang**², **Lantao Hu**², **Peng Jiang**², **Kun Gai**³, and **Bo An**¹ (*\*Corresponding author*) [1, 3]
* **Author Affiliations:**
  1. **Nanyang Technological University**, Singapore / Skywork AI [1–2]
  2. **Kuaishou Technology**, Beijing, China [1]
  3. **Unaffiliated**, Beijing, China [1]
* **Year:** **2025** (Published at WWW ’25; arXiv pre-print `arXiv:2310.03984`) [3–4]
* **Venue:** *Proceedings of the ACM Web Conference 2025 (WWW ’25)*, April 28–May 2, 2025, Sydney, NSW, Australia [3–4]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Standard Reinforcement Learning (RL) algorithms for user retention struggle with environment non-stationarity driven by shifting user behavior patterns (such as fluctuating interaction rates and user return time distributions) [2, 4]. Shifting environments cause policy performance degradation, while "implicit cold-start" scenarios force policies to continually interact with users exhibiting novel behaviors [4, 5].
* **Key Contributions:**
  1. **Value-Based State Abstraction Module:** Introduces a state abstraction module in the policy network trained with a value-based contrastive loss (\\(J(\phi)\\)) [4, 6, 7]. It aligns latent outputs with estimated state values (\\(V\\)) to detect environmental changes universally and notify the policy to adapt [2, 6, 16–17].
  2. **Guarded Online Exploration:** Implements optimistic exploration (\\(\nabla_a Q_{\text{UB}}\\)) combined with rejection sampling over candidate action particles to safely adapt to novel user behavior without causing user disengagement or churn [2, 6, 27–30].
  3. **Industrial Scale Deployment:** Fully launched on a popular short-video recommendation platform serving 25 million daily active users [4, 8, 9].

---

### **(3) Proposed Method or Architecture in Detail**

#### **MDP Formulation & Model Architecture**
* **HiP-MDP Formulation:** Models non-stationary environments using Hidden Parameter MDPs \\(\langle S, A, \Theta, T, r, \gamma, \rho_0 \rangle\\) where hidden parameters \\(\theta \sim \Theta\\) govern dynamic shifts [9–10].
  * **State Space (\\(s_t\\)):** Low-dimensional vector concatenating user features, item features, and interaction history (processed via embedding layers and Transformers) with state abstraction vector \\(\phi(s_t)\\) [15, 18–19].
  * **Action Space (\\(a_t \in \mathbb{R}^k\\)):** \\(k\\)-dimensional continuous action vector used to compute final ranking scores alongside a scoring model [8–9].
  * **Retention Reward (\\(r_t\\)):** Assigned at the final step of an episode as \\(r_t = \lambda \times \text{user return time}\\) (set to \\(0\\) for intermediate steps; discount factor \\(\gamma = 0.9\\), \\(\lambda = -0.1\\)) [10, 11].
* **Value-Based State Abstraction Loss (\\(J(\phi)\\)):**
  Ranks a batch of states by their state value function \\(V(s)\\), divides them into \\(n\\) categories (\\(n=4\\)), and minimizes [12-15]:
  \\[J(\phi) = \frac{2B}{n} \sum_{k=0}^n \sum_{i} \|\phi(s_i) - \bar{\phi}_k\|_2^2 - \frac{B^2}{n^2} \sum_{k=0}^n \sum_{m>k} \|\bar{\phi}_k - \bar{\phi}_m\|_2^2\\]
  where \\(\bar{\phi}_k\\) is the moving average abstraction vector for category \\(k\\) [23–25].
* **Guarded Online Exploration Module:**
  Generates \\(N\\) candidate action particles around base policy action \\(a_T\\) along the gradient of upper-bound Q-value \\(Q_{\text{UB}}(s, a) = \mu_Q(s, a) + \beta \sigma_Q(s, a)\\):
  \\[a_k = a_T + k \delta \frac{\nabla_a Q_{\text{UB}}(s, a)}{\|\nabla_a Q_{\text{UB}}(s, a)\|}\\]
  and selects exploration action \\(a_E = \arg\max_{a_k} \mu_Q(s, a_k)\\) via rejection sampling [27–30].

#### **Credit Assignment Mechanics**
* Credit is assigned at the **episode trajectory level** using the delayed user return time as an episode-ending retention reward \\(r_t = \lambda \times \text{user return time}\\) [10].
* The framework does **not** perform fractional multi-touch attribution or per-item credit decomposition across historical interaction logs [10].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets & Simulator:**
  1. **KuaiSim Retention Simulator:** Simulates long-term user retention, session leave probabilities, and multi-day return time distributions on short-video platforms [31–32, 49].
  2. **MovieLens-1M Dataset:** Modified for offline evaluation using Normalized Capped Importance Sampling (NCIS) and BC loss [31, 43–44].
* **Production Deployment:** Deployed live in production on Kuaishou's candidate ranking pipeline serving **25 million daily active users** and **billions of daily interactions** over a **2-week online A/B test** [4, 8, 9].
* **Comparison Baselines:**
  * *Non-RL / Heuristic:* CEM, DIN [16-18].
  * *Standard Off-Policy RL:* DDPG, TD3, SAC [16-18].
  * *Exploration-Focused RL:* OAC, RND [16-18].
  * *Context Encoder / Meta-RL:* ESCP [34, 36–37, 77].
  * *Retention-Oriented RL:* RLUR, OSPIA, RL-LTV [34, 36–37, 77].

---

### **(5) Key Quantitative Results with Numbers**

* **KuaiSim Retention Simulator Benchmark (at 20K Timesteps, Table 2):**
  * **Average Return Days (lower is better):** **AURO = 1.531 ± 0.058** vs. RLUR (**1.706**), ESCP (**1.705**), OSPIA (**1.726**), SAC (**1.810**), TD3 (**1.772**), CEM (**1.858**) [16].
  * **Return Rate at Day 1 (higher is better):** **AURO = 0.824 ± 0.018** vs. RLUR (**0.765**), OSPIA (**0.803**), ESCP (**0.764**), TD3 (**0.738**), DIN (**0.755**) [16].
  * **Retention Reward (higher is better):** **AURO = -0.015 ± 0.000** vs. baselines (**-0.017 to -0.019**) [16].
* **MovieLens-1M Offline Evaluation (Table 3):**
  * **Retention Reward:** **AURO+BC = 1.798 ± 0.032** vs. RLUR+BC (**1.784**), ESCP+BC (**1.755**), TD3+BC (**1.714**), BC (**1.702**) [19].
* **Live Online Production A/B Test Results (vs. RLUR Baseline over 2 Weeks, Table 4):**
  * **7-Day Retention Rate:** **+0.138‰** permillage lift [20].
  * **App Dwell Time:** **+0.263‰** permillage lift (**AURO was the only algorithm to achieve positive dwell time gains**; TD3 regressed by **-0.685‰**, ESCP by **-0.115‰**) [46–47].
  * **Click-Through Rate (CTR):** **+3.260‰** permillage lift [20].
  * **Like Rate:** **+2.821‰** permillage lift [20].
  * **Comment Rate:** **+8.392‰** permillage lift (**nearly 5× higher** than TD3's +1.715‰) [46–47].
  * **Unlike / Hate Rate (lower is better):** **-1.874%** reduction [20, 21].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Omission of Immediate Feedback Balancing:** Focuses exclusively on optimizing long-term retention rewards without explicitly formulating or balancing immediate feedback trade-offs (e.g., CTR vs. retention) within the objective function [22].
2. **Vulnerability to Unprecedented / Adversarial User Behaviors:** If users display unprecedented behavior patterns (e.g., suddenly disliking all recommended content out of boredom), the state abstraction module may fail to adapt properly [22].
3. **Suboptimal Performance on Stubborn Users:** For stubborn users who strictly refuse to interact with unfamiliar content, optimistic exploration can result in inferior retention compared to greedy recommendation strategies [22].
4. **Reliance on Post-Processing Safety Filters:** In live deployment, RL recommendation outputs depend on downstream post-processing and filtering mechanisms to prevent inappropriate content from reaching users [23].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Cai et al. (2023) [Ref 6 / RLUR]:** *Reinforcing User Retention in a Billion Scale Short Video Recommender System* (WWW ’23) [24].
2. **Wang et al. (2022) [Ref 42 / Surrogate]:** *Surrogate for Long-Term User Experience in Recommender Systems* (KDD ’22) [25].
3. **Fujimoto, van Hoof, & Meger (2018) [Ref 17 / TD3]:** *Addressing Function Approximation Error in Actor-Critic Methods* (ICML ’18) [26].
4. **Haarnoja et al. (2018) [Ref 18 / SAC]:** *Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor* (ICML ’18) [26].
5. **Luo et al. (2022) [Ref 30 / ESCP]:** *Adapt to Environment Sudden Changes by Learning a Context Sensitive Policy* (AAAI ’22) [27].
6. **Zhao et al. (2023) [Ref 49 / KuaiSim]:** *KuaiSim: A comprehensive simulator for recommender systems* (NeurIPS ’23) [28].
7. **Sutton & Barto (1998) [Ref 38 / RL Book]:** *Reinforcement Learning: An Introduction* [29].

---

💡 *Would you like to explore how AURO's value-based state abstraction or guarded online exploration module could be adapted to optimize 7-day user retention for your dating app?*

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
**Priority:** see queue.md `G9`
