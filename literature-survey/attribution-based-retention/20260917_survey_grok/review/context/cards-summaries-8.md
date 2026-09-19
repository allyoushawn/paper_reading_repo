# Card summaries 8/12 — Summary and Evidence sections of all cards (generated)

### AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems [1, 2]
`2025_WWW_AURO_Adaptive-User-Retention-Optimization.md`
**Source:** https://arxiv.org/pdf/2310.03984.pdf  

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**
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

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems [1]
`2026_AAAI_RevisitMTL_Save-Revisit-Retain.md`
**Source:** https://arxiv.org/pdf/2511.18013.pdf  

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**

* **Title:** *Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems* [1]
* **Authors:** **Weijie Jiang**, **Armando Ordorica**, **Jaewon Yang**, **Olafur Gudmundsson**, **Yucheng Tu**\*, and **Huizhong Duan** (\*Work done at Pinterest) [1, 2]
* **Affiliations:** **Pinterest Inc.** [1]
* **Year:** **2026** (submitted Nov 2025, Copyright © 2026 AAAI) [1, 2]
* **Venue:** *Proceedings of the AAAI Conference on Artificial Intelligence (AAAI '26)* / arXiv pre-print (`arXiv:2511.18013`) [1, 2]

---

### **(2) Core Problem and Key Contribution**

* **Core Problem:** Optimizing long-term user revisitation (returning to view previously saved content) to drive platform retention faces two major challenges:
  1. *Attribution Noise & Confounding:* Unclear causal links between initial candidate exposures/saves and delayed return visits due to confounding factors like changing user intent, platform notifications, or UI layout [1, 3].
  2. *Scalability Bottleneck:* Tracking cross-session revisitations occurring days or weeks later requires maintaining and joining massive activity logs across millions of users and surfaces, creating heavy computational and serving latency overhead [1, 3].
* **Key Contributions:**
  1. **Surrogate Attribution Framework:** Establishes a lightweight surrogate process linking initial item save actions ("repins") to subsequent cross-session revisitation events, isolating true return intent from incidental noise [1, 4, 5].
  2. **Cross-Surface Data Pipeline:** Implements a scalable event-aggregation pipeline that performs cross-surface joins (linking Related Pins save events with Own Profile revisit events over a 0–6 day window) [1, 7, 29–31].
  3. **Multi-Task Joint Modeling:** Integrates a dedicated revisitation prediction head into an existing Multi-Gate Mixture-of-Experts (MMoE) ranking architecture without adding serving cost or latency [1, 6-8].
  4. **Billion-Scale Industrial Deployment:** Deployed on Pinterest's Related Pins surface serving **500M+ users**, achieving a statistically significant **+0.10% increase in active users** in live A/B testing [1, 9, 10].

---

### **(3) Proposed Method or Architecture in Detail**

* **Multi-Task Learning (MTL) Architecture:**
  * **Input Features:** Query Pin features, candidate Pin features, user features, and a Transformer-based user sequence module [7].
  * **Representation & Expert Layers:** Feature cross-summarization \\(\rightarrow\\) **DCNv2** deep feature interaction layer \\(\rightarrow\\) MLP aggregation \\(\rightarrow\\) **MMoE** (Multi-Gate Mixture-of-Experts) shared experts and task gates [7].
  * **Task Prediction Heads:** Predicts probabilities for standard engagement tasks (\\(P(\text{grid-click})\\), \\(P(\text{repin})\\), \\(P(\text{click})\\), \\(P(\text{long-click})\\)) plus the new **revisitation prediction head** \\(P(c_{\text{RP\&RV}} \mid q, \theta)\\) [8, 11].
* **Credit Assignment & Touchpoint Linkage Mechanism:**
  * **Surrogate Linkage:** Connects an initial save action ("repin") on the Related Pins surface to subsequent profile revisitations over a 0–6 day temporal window [5–7, 23].
  * **Revisitation Label Construction (\\(c_{\text{RP\&RV}}\\)):** Combines three binary sub-signals into a unified revisitation target:
    1. *Same-day Revisitation Impression (1dRevImpre):* User saved a Pin and viewed it on their profile on the same day [12].
    2. *Same-day Revisitation Grid-click (1dRevGrid):* User saved a Pin and tapped to zoom into it on their profile on the same day [12].
    3. *7-day Revisitation Grid-click (7dRevGrid):* User saved a Pin and tapped/zoomed into it on their profile within days 0–6 following the save [12].
  * **Ranking Score Integration:** Assigns credit directly to candidate Pins during ranking by adding the predicted revisitation probability weighted by a utility weight \\(u_{\text{RP\&RV}}\\) into the multi-task final ranking score [22, 25–26]:
    \\[\text{score} = \sum_{i \in L} u_i \cdot p(c_i \mid q, \theta) + u_{\text{RP\&RV}} \cdot p(c_{\text{RP\&RV}} \mid q, \theta)\\]

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets & Scale:**
  * **Offline Dataset:** 27 days of training logs (~**6.6 billion samples**), 1 day for calibration, and 3 days for evaluation (~**700 million samples**) from Pinterest's Related Pins surface [13].
  * **Online A/B Experiment:** **24 million users** (12M control, 12M treatment) evaluated continuously over two months (April 29, 2025 – June 26, 2025) [9, 14].
* **Production Deployment:** Deployed live on Pinterest's Related Pins surface (serving ~50% of total platform traffic) to **500+ million monthly active users** [1, 15, 16].
* **Comparison Baselines:**
  * *Production Baseline:* Existing MMoE + DCNv2 multi-task ranking model predicting immediate engagement tasks (\\(P(\text{grid-click})\\), \\(P(\text{repin})\\), \\(P(\text{click})\\), \\(P(\text{long-click})\\)) without revisitation modeling [13, 21–22, 33].
  * *Conceptual Baselines:* Separate causal/triple-task revisitation models (Zhang et al., 2021) and Reinforcement Learning / Generative Flow Networks (Liu et al., 2024 / GFN4Retention) [6, 17, 18].

---

### **(5) Key Quantitative Results with Numbers**

* **Offline Evaluation Benchmark (Table 1):**
  * **Revisitation Task Head:** **+40.15% NDCG@3**, **+43.44% MAP@3**, **+35.40% Recall@3**, **+27.62% Recip Rank@3**, and **+21.62% Pairwise Accuracy** over baseline [19].
  * **Repin Task Head:** **+0.1279% NDCG@3**, **+0.0645% MAP@3**, and **+0.2705% Recall@3** [19].
  * **Overall Ranking Hits@3:** **+0.59% lift on Repin** and **+0.65% lift on Revisitation** [33–34].
* **Live Online Production A/B Testing (Table 2, 24M Users):**
  * **Active Users (Site-wide Retention):** **+0.10% volume** (\\(p < 0.05\\)) and **+0.08% propensity** (\\(p < 0.05\\)) [10, 20].
  * **Revisitation Metrics:**
    * *1dRevImpre:* **+0.65% volume** (\\(p < 0.05\\)), **+0.93% propensity** (\\(p < 0.05\\)) [20].
    * *1dRevGrid:* **+0.95% volume** (\\(p < 0.05\\)), **+1.17% propensity** (\\(p < 0.05\\)) [20].
    * *7dRevGrid:* **+1.18% volume** (\\(p < 0.05\\)), **+1.42% propensity** (\\(p < 0.05\\)) [20].
  * **Core Engagement:** **+0.94% Repin volume** (\\(p < 0.1\\)), **+0.41% Long Sessions (\\(\ge 5\\) min)** (\\(p < 0.01\\)), **+0.35% Web/API Requests** (\\(p < 0.01\\)), **+0.53% Time Spent on Related Pins**, **+0.68% Time Spent on Own Profile**, and **+0.39% Total App Time Spent** [36–38].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **User Activity Imbalance & Label Sparsity Bottleneck:** Highly active users repin disproportionately more than less active users, resulting in sparse revisitation label coverage for less active user cohorts [21].
2. **Intent vs. Density Trade-Off:** Impression-based revisits offer high label volume but contain incidental scroll noise, whereas grid-click revisits signal deliberate return intent but decay rapidly (grid-click revisits drop from 4.7% on day 0 to 2.2% on day 1, and 0.3% by day 9) [22, 23].
3. **Relevance vs. Diversity Tension:** Authors note that earlier attempts to optimize recommendation diversity hurt click and save engagement metrics by >1% [24].
4. **Offline Recip Rank@3 Degradation:** Offline Recip Rank@3 on the repin head exhibited a slight negative change (**-0.02666%**), though overall Hits@3 and online metrics were strictly positive [33–34].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Zhang et al. (2021) [Triple-Task Causal Retention]:** *User Retention: A Causal Approach with Triple Task Modeling* (IJCAI '21) [6, 25].
2. **Wang et al. (2022) [Surrogate Rewards for Experience]:** *Surrogate for long-term user experience in recommender systems* (KDD '22) [4, 5, 26].
3. **Liu et al. (2024) [GFN4Retention]:** *Modeling User Retention through Generative Flow Networks* (KDD '24) [17, 18, 26].
4. **Liu et al. (2017) [Pinterest Related Pins Architecture]:** *Related pins at pinterest: The evolution of a real-world recommender system* (WWW '17) [9, 14-16, 26].
5. **Ma et al. (2018) [MMoE Architecture]:** *Modeling task relationships in multi-task learning with multi-gate mixture-of-experts* (KDD '18) [7, 26].
6. **Wang et al. (2021) [DCNv2 Layer]:** *DCN v2: Improved deep & cross network and practical lessons for web-scale learning to rank systems* (WWW '21) [7, 26].
7. **Zhao et al. (2023) [DT4Rec]:** *User retention-oriented recommendation with decision transformer* (WWW '23) [18, 25].

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?
`2026_CIKM_LOTUS_Meaningful-Touchpoints-Conversion-Attribution.md`
**Source:** https://arxiv.org/pdf/2608.28649.pdf  

**Summary.** Here is the detailed breakdown for the paper **"Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?"** (from source `https://arxiv.org/pdf/2608.28649.pdf`).

---

### **(1) Title, Authors, Affiliations, Year, Venue**

* **Title:** *Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?*
* **Authors:** **Jinqi Wu**\*¹, **Sishuo Chen**\*², **Zhangming Chan**², **Yong Bai**², **Chao Yi**², **Han Zhu**², **Shuodian Yu**², **Lei Zhang**², **Sheng Chen**², **Chenghuan Hou**², **Jian Xu**†², and **Chaoyou Fu**¹ (*Co-first authors, †Corresponding author)
* **Author Affiliations:**
  1. **State Key Laboratory for Novel Software Technology, Nanjing University**, Nanjing, China & **School of Intelligence Science and Technology, Nanjing University**, Suzhou, China (`jinqiwu001@gmail.com`, `bradyfu24@gmail.com`)
  2. **Taobao & Tmall Group of Alibaba**, Beijing, China (`{chensishuo, zhangming.czm, baiyong.by, yunan.yc, zhuhan.zh, yushuodian.ysd, zl165646, chensheng.cs, jinyao, xiyu.xj}@alibaba-inc.com`)
* **Year:** 2026
* **Venue:** *Proceedings of the 35th ACM International Conference on Information and Knowledge Management (CIKM ’26), November 07–11, 2026, Rome, Italy*

---

### **(2) Core Problem and Key Contribution**

* **Core Problem:** Standard conversion attribution relies on heuristic, rule-based touchpoint selection (e.g., matching exact product taxonomies or collaborative filtering [CF] signals). These mechanical rules fail to align with human semantic intent and miss a vast space of **implicitly-related touchpoints**—interactions that are semantically relevant to the purchased item but lack explicit metadata or historical engagement overlaps (e.g., buying a camera after browsing memory cards, or buying anime merchandise across different product categories).
* **Key Contribution:**
  1. **SILVA Benchmark:** Constructs **SILVA** (*Selection In fuLl-path conVersion Attribution*), the first human-annotated benchmark for full-path touchpoint selection, revealing that implicitly-related touchpoints constitute **14.91%** of all conversion path touchpoints.
  2. **Systematic Evaluation of LLMs:** Conducts a comprehensive evaluation of flagship proprietary (e.g., GPT-5.5, Gemini 3.1 Pro, Claude Opus 4.7) and open-weight LLMs (e.g., GLM-5.1, DeepSeek V4-Pro, Qwen3.5) across listwise vs. pairwise prompting protocols and thinking modes.
  3. **LOTUS Framework:** Proposes **LOTUS** (*LLM-Oriented Touchpoint Understanding and Selection*), which uses LLM-identified implicit touchpoints as auxiliary labels to train industrial CVR models, achieving significant GAUC gains on an e-commerce platform with hundreds of millions of users.

---

### **(3) Proposed Method or Architecture in Detail**

* **Two-Stage Conversion Attribution Paradigm:**
  * **Stage 1 (Touchpoint Selection - Paper Focus):** Given a conversion event \\(C\\) and preceding touchpoint sequence \\(\{t_1, t_2, \dots, t_n\}\\) within a 3-day lookback window, the system selects relevant touchpoints and classifies them into three classes:
    * *Explicitly-Related:* Same item/shop/brand/category or CF-based similar leaf category.
    * *Implicitly-Related:* Semantic relationships missed by rules, such as **Functional Complementarity** (e.g., camera \\(\leftrightarrow\\) memory card) or **Scenario/Audience Alignment** (e.g., shared anime IP or outdoor activity theme).
    * *Irrelevant:* Weak or unrelated touchpoints.
  * **Stage 2 (Weight Allocation):** Distributes normalized credit \\(\sum w_i = 1\\) among the selected touchpoints.
* **LLM Selection Protocols:**
  * **Pairwise Reasoning:** Evaluates \\((t_i, C)\\) pairs individually alongside the user profile. Decomposes sequence noise into targeted candidate-level judgments.
  * **Listwise Reasoning:** Evaluates the entire behavior log \\(\{t_1, \dots, t_n\}\\) alongside \\(C\\) in a single prompt call.
* **Downstream CVR Enhancement (LOTUS):** LLM-selected implicit touchpoints are fed as positive training instances for an auxiliary indirect-conversion prediction task inside an internal foundation model on Taobao & Tmall.

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Benchmark Dataset (SILVA):**
  * Collected from Taobao & Tmall (Alibaba); contains **1,000 unique conversion events** and **69,680 preceding touchpoints** (3-day lookback window) annotated by human experts (Fleiss’ \\(\kappa > 0.70\\)).
  * Touchpoint Breakdown: **19.09% Explicit**, **14.91% Implicit**, **66.00% Irrelevant**.
* **Production Deployment:**
  * Evaluated on a production CVR prediction model serving hundreds of millions of daily active users at Alibaba.
* **Baselines:**
  * *Selection Baselines:* Rule-based Taxonomy Matching, Collaborative-Filtering (CF) Similarity rules.
  * *Evaluated LLMs:* GPT-5.5, Gemini-3.1-Pro, Claude-Opus-4.7, GLM-5.1, DeepSeek-V4-Pro, DeepSeek-V4-Flash, Qwen3.5-27B, Qwen3.5-30B-A3B.
  * *CVR Prediction Baselines:*
    * **Base (Chen et al., 2025):** Production in-shop attribution baseline.
    * **CABB (Zeng et al., 2026 / Meta):** Heuristic cross-shop selection based on CF rules.

---

### **(5) Key Quantitative Results with Numbers**

* **Touchpoint Selection Benchmark Performance (SILVA, Table 1):**
  * **Explicit F1:** Strong LLMs reach **0.897–0.909 F1** (Pairwise Gemini-3.1-Pro reaches 0.9095; GLM-5.1 reaches 0.9092).
  * **Implicit F1:** Significantly lower across all models, peaking at **0.5426** (GPT-5.5 Pairwise) and **0.5293** (Gemini-3.1-Pro Pairwise).
  * **Pairwise vs. Listwise Gain:** Pairwise prompting raises average Overall F1 from **0.6490 to 0.6954 (+4.64 pp)**. The gap narrows for flagship models (3.0 pp for GPT-5.5) but expands for smaller models (11.9 pp for Qwen3.5-30B-A3B).
* **Industrial CVR Model Gains (Table 3):**
  * **CABB (Explicit Rules) vs. Base:** **+0.20 pp GAUC**.
  * **LOTUS (LLM Explicit + Implicit) vs. Base:** **+0.35 pp GAUC** absolute improvement over the production baseline.
  * **LOTUS vs. CABB:** **+0.15 pp GAUC** incremental gain purely from capturing implicit semantic touchpoints (an absolute gain of 0.10 pp GAUC is considered commercially significant in large-scale e-commerce).

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Persistent Gap in Implicit Reasoning:** The best LLM implicit F1 score (0.5426) lags far behind explicit F1 (~0.91), showing that functional complementarity and scenario alignment remain difficult for current foundation models.
2. **Listwise Over-Filtering / Low Recall:** Listwise prompting suffers from lower recall because LLMs tend to over-filter touchpoints when processing long, noisy behavior logs in a single prompt.
3. **Underperformance of Smaller Models (<100B):** Open-weight models below 100B parameters (e.g., Qwen3.5-27B) lag heavily behind flagship models on implicit touchpoint detection.
4. **Marginal Impact of Chain-of-Thought / Thinking Mode:** Enabling Chain-of-Thought ("think" mode) provided minimal average F1 gains (+0.0082 in pairwise; +0.0196 in listwise), indicating that general CoT reasoning patterns are not yet tailored for nuanced touchpoint attribution judgments.

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Zeng et al. (2026) [CABB / Meta]:** *Click A, Buy B: Rethinking Conversion Attribution in E-Commerce Recommendations* (established cross-item heuristic touchpoint selection).
2. **Chen et al. (2025) [Multi-Attribution Learning]:** *See Beyond a Single View: Multi-Attribution Learning Leads to Better Conversion Rate Prediction* (CIKM '25, established CVR model training with attribution labels).
3. **Yao et al. (2022) [CausalMTA]:** *CausalMTA: Eliminating the User Confounding Bias for Causal Multi-touch Attribution* (KDD '22).
4. **Bencina et al. (2025) [LiDDA]:** *LiDDA: Data Driven Attribution at LinkedIn*.
5. **Lewis et al. (2025) [Amazon Ads MTA]:** *Amazon Ads Multi-Touch Attribution*.
6. **Wei et al. (2022) [Chain-of-Thought]:** *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* (NeurIPS '22).
7. **Liu et al. (2026) [ALM-MTA]:** *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization* (ICLR '26).

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

