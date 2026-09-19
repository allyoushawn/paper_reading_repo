# Compact relevance index — truncated Project Relevance from this-run cards (1/2)

### A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications [1]
`2020_KDD_RDSA_Sleeping-Recovering-Bandit-Notifications.md`
**Source:** https://research.duolingo.com/papers/yancey.kdd20.pdf  
**Q2 class:** NOT

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

* **Per-Interaction Credit:** **No per-interaction sequence attribution
… [truncated]

### Surrogate for Long-Term User Experience in Recommender Systems [1]
`2022_KDD_NA_Surrogate-Long-Term-User-Experience.md`
**Source:** https://dl.acm.org/doi/pdf/10.1145/3534678.3539073  
**Q2 class:** NOT

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
* **Per-Interaction Credit:** **No
… [truncated]

### Long-run User Value Optimization in Recommender Systems through Content Creation Modeling [1]
`2022_arXiv_NA_Long-run-User-Value-Optimization-Meta.md`
**Source:** https://arxiv.org/pdf/2204.11421.pdf  
**Q2 class:** UNSPECIFIED

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
  2. **Two-Step Causal ML Framework:** Combines a producer-level distribution-boosting A/B experiment with heterogeneous treatment effects (HTE) machine learning (T-Learner / Meta-Learner using GBDTs
… [truncated]

### Incrementality-Focused Messaging Measurement (Netflix) — stub
`2023_NetflixBlog_NA_Incrementality-Focused-Messaging-Measurement.md`
**Source:** https://medium.com/notificationsblog/incrementality-focused-messaging-measurement-all-the-time-everywhere-94ef0c229368  
**Q2 class:** PARTIAL

- **Answers:** Q2 adjacent (notification incrementality), not swipe MTA.
- **Q2 class:** PARTIAL (touchpoint holdback, not in-app item).
- **Per-interaction credit:** per **message** incremental viewing, not per-swipe N7.
- **Last-touch replacement:** holdout incrementality is a calibration device for observational credit, analogous to Amazon Ads MTA's RCT calibration, not a full multi-touch retention labeler.
- **Transfer rating:** adaptable as a **notification-level** incrementality fixture, not as swipe attribution.

**Low project relevance** for swipe-level N7 labels; useful as a measurement pattern.

---

### Interpretable User Retention Modeling in Recommendation [14]
`2023_RecSys_IURO_Interpretable-User-Retention-Modeling.md`
**Source:** https://dl.acm.org/doi/pdf/10.1145/3604915.3608818  
**Q2 class:** PARTIAL

### **Part 1: Detailed Technical Breakdown of the Source**

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Interpretable User Retention Modeling in Recommendation* [1]
* **Authors:** **Rui Ding**¹, **Ruobing Xie**\*², **Xiaobo Hao**², **Xiaochun Yang**\*¹, **Kaikai Ge**², **Xu Zhang**², **Jie Zhou**², and **Leyu Lin**² (*\*Corresponding Authors*) [1, 2]
* **Author Affiliations:**
  1. **Northeastern University**, Shenyang, China (`ruiding.neu@outlook.com`, `yangxc@mail.neu.edu.cn`) [1]
  2. **WeChat, Tencent**, Beijing, China (`{xrbsnowing, rolyhao, kavinge, xuonezhang, withtomzhou, goshawklin}@tencent.com`) [1, 2]
* **Year & Venue:** Published in **2023** at the *Seventeenth ACM Conference on Recommender Systems (RecSys ’23), September 18–22, 2023, Singapore* [3, 4].

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Recommender systems primarily optimize for immediate accuracy and engagement metrics (e.g., Click-Through Rate / CTR), which fails to reflect long-term user satisfaction and retention [2, 4]. Existing retention modeling efforts (e.g., Reinforcement Learning, Decision Transformers, survival analysis) treat retention as a black box focused purely on predictive accuracy, failing to discover *why* users return or *which specific behaviors* affect retention ("interpretability") [4-7]. Major challenges include:
  1. *Offline-Online Gap:* Offline training predicts user-level return, whereas online serving requires item-level scoring [8].
  2. *Complex Causality & External Randomness:* Retention is
… [truncated]

### User Retention-oriented Recommendation with Decision Transformer [1]
`2023_WWW_DT4Rec_User-Retention-Oriented-Decision-Transformer.md`
**Source:** https://arxiv.org/pdf/2303.06347.pdf  
**Q2 class:** NOT

### **Source Evaluation: DT4Rec (*User Retention-oriented Recommendation with Decision Transformer*)**
*(Zhao et al., City University of Hong Kong, Wuhan University, & Baidu Inc., WWW 2023: `arxiv:2303.06347`)* [1]

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**
* **Answer:** **Neither.** [1-3]
* **Explanation:**
  * *Q1 (Industry/Production Attribution 2025–01 to 2026-09):* **No.** Published at WWW 2023 (May 2023), which falls outside the 2025–2026 window [1–2]. Furthermore, it is evaluated on offline benchmark datasets rather than an industry production attribution pipeline [1, 16–17].
  * *Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):* **No.** DT4Rec formulates sequential recommendation for user retention as offline reinforcement learning via Decision Transformers (autoregressive sequence modeling) [1, 4, 5]. It does **not** perform multi-touch causal sequence attribution or publish per-exposure retention credit scores [4-6].

---

### **(B) Q2 Class**
* **Classification:** **NOT** [1, 4-6]
* **Justification:** DT4Rec is an offline RL / Decision Transformer sequence modeling framework that generates candidate recommendation lists conditioned on target retention reward prompts [4, 5, 7]. It does **not** output or publish a per-exposure retention credit table or multi-touch attribution decomposition [4, 5].

---

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction credit.** [4-6]
* **Target Outcome & Formula:** Replaces temporal value estimation
… [truncated]

### Reinforcing User Retention in a Billion Scale Short Video Recommender System [1]
`2023_WWW_RLUR_Reinforcing-User-Retention.md`
**Source:** https://arxiv.org/pdf/2302.01724.pdf  
**Q2 class:** NOT

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
* **Per-Interaction Credit:** **No.** Credit is assigned at the **request level to a continuous 8-dimensional ensemble weight action vector (\\(a_{it}\\))**, which combines scoring model predictions (watch time, short view, long view, like,
… [truncated]

### **Part 1: Dating App Retention Project Evaluation**
`2024_KDD_FID_Future-Impact-Decomposition.md`
**Source:** https://arxiv.org/pdf/2401.16108.pdf  
**Q2 class:** NOT

### **Source Evaluation: ItemA2C (*Future Impact Decomposition in Request-level Recommendations*)**
*(Wang et al., Peking University & Kuaishou Technology, KDD 2024: `arxiv:2401.16108`)* [1, 6–7]

---

### **(A) Query Categorization: Q1 vs. Q2**
* **Answer:** **Neither Q1 nor Q2.**
* **Explanation:** 
  * *Q1 (Industry Attribution 2025–2026):* Published in August 2024 (KDD ’24), which falls outside the specified 2025–2026 timeframe [6–7].
  * *Q2 (Interaction-Level Retention Attribution):* Focuses on reinforcement learning (RL) policy optimization for list-wise recommendations rather than multi-touch causal sequence attribution over historical user journey logs [8–12, 18].

---

### **(B) Q2 Class**
* **Classification:** **NOT**
* **Justification:** The paper presents an RL actor-critic policy optimization method (**ItemA2C**) that decomposes list-level future value \\(V(s_{t+1})\\) down to individual items for policy gradient updates, rather than publishing an explicit per-exposure retention credit table or multi-touch attribution model [15–18, 35–41].

---

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Yes (in the form of an RL item-level advantage score)** [39–41].
* **Target Outcome & Formula:** Allocates cumulative session rewards \\(R(s_t, a_t) = \sum r_{t,k}\\) and long-term state value \\(V(s_{t+1})\\) (which drives user retention) to individual items \\(i_{t,k}\\) in list \\(a_t\\) via item target value \\(\Psi_w\\) and advantage \\(A\\) [1-4]:
  \\[\Psi_w(s_t, i_{t,k}) = r_{t,k} + w_{t,k} \gamma (1-d)
… [truncated]

### Modeling User Retention through Generative Flow Networks [1]
`2024_KDD_GFN4Retention_Modeling-User-Retention.md`
**Source:** https://arxiv.org/pdf/2406.06043.pdf  
**Q2 class:** NOT

### **Source Evaluation: GFN4Retention (*Modeling User Retention through Generative Flow Networks*)**
*(Liu et al., City University of Hong Kong & Kuaishou Technology, KDD 2024: `arxiv:2406.06043`)* [1, 2]

---

### **(A) Query Categorization: Q1 vs. Q2**
* **Answer:** **Neither Q1 nor Q2.**
* **Explanation:** 
  * *Q1 (Industry Attribution 2025–2026):* Published in August 2024 (KDD ’24), which falls outside the 2025–2026 timeframe [2, 3].
  * *Q2 (Interaction-Level Retention Attribution):* Focuses on generative flow policy optimization for session-wise recommendations rather than multi-touch causal sequence attribution over historical user journey logs [6–9].

---

### **(B) Q2 Class**
* **Classification:** **NOT**
* **Justification:** The paper presents a Generative Flow Network (GFN) reinforcement learning framework that optimizes session trajectory generation by back-propagating terminal retention flows via Detailed Balance loss [8–10, 20, 26]. It does **not** publish an explicit per-exposure retention credit table or multi-touch attribution model [6–8].

---

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Yes (via step-wise probabilistic flow matching / Detailed Balance loss)** [4-7].
* **Target Outcome & Formula:** Combines the delayed terminal session retention reward \\(\mathcal{R}\\) (reciprocal user return time gap between consecutive sessions) with non-discounted immediate engagement rewards \\(r_t = \sum \omega_b y_{t,b}\\) (clicks, likes, watch time) via an integrated multiplicative reward product
… [truncated]

### Learned Ranking Function: From Short-term Behavior Predictions to Long-term User Satisfaction [1]
`2024_RecSys_LRF_Learned-Ranking-Function-YouTube.md`
**Source:** https://arxiv.org/pdf/2408.06512.pdf  
**Q2 class:** NOT

### **Part 1: Dating App Retention Project Evaluation**

#### **(A) Q1 or Q2 or Both or Neither?**
* **Answer:** **Neither.** [1-3]
* **Explanation:**
  * **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** Published in October 2024 at RecSys '24 [1], which falls outside the 2025–2026 window. Furthermore, it is a slate optimization and candidate ranking framework for video recommendations, not a multi-touch attribution (MTA) measurement system [1-3].
  * **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** LRF predicts long-term user satisfaction lift (\\(R_{\text{lift}}\\)) at candidate ranking time using uplift modeling and cascade click probabilities [4-6], rather than attributing N7 retention or active days across past multi-touch user interaction sequences.

---

#### **(B) Q2 Class**
* **Classification:** **NOT** [3, 7, 8]
* **Justification:** As a slate ranking and RL policy optimization framework (**LRF**), it computes a candidate ranking score:
  \\[\text{Score}(u, v) = \frac{p_{\text{clk}}(u, v)}{p_{\text{clk}}(u, v) + p_{\text{abd}}(u, v)} \cdot R_{\text{lift}}(u, v)\\[5, 8]\\]
  to sort candidate profile slates, rather than publishing a per-exposure retention credit table or multi-touch sequence attribution model.

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction sequence attribution.**
* **Target Outcome:** At candidate ranking time, the model outputs item-level long-term reward lift:
  \\[R_{\text{lift}}(u, v) =
… [truncated]

### Sequential Recommendation for Optimizing Both Immediate Feedback and Long-term Retention
`2024_arXiv_NA_Sequential-Rec-Immediate-Feedback-Long-term-Retention.md`
**Source:** https://arxiv.org/html/2404.03637  
**Q2 class:** NOT

### **Source Evaluation: *Sequential Recommendation for Optimizing Both Immediate Feedback and Long-term Retention***
*(arXiv pre-print, April 2024: `arXiv:2404.03637v2`)*

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**

**Neither.** [1, 3, 11–12, 19]
* **Q1 (Industry/Production Attribution 2025-01 to 2026-09):** **No.** Published in April 2024 (`arXiv:2404.03637v2`), which falls outside the 2025–2026 window [1]. Furthermore, it is evaluated on offline benchmark datasets rather than an industry production attribution system [1, 2].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** DT4IER formulates long short-term multi-task sequential recommendation using an offline Reinforcement Learning / Decision Transformer framework [3, 4]. It generates candidate item sequences conditioned on multi-reward Return-to-Go (RTG) prompts rather than calculating per-touch attribution credit across historical interaction logs [3, 8, 11–12].

---

### **(B) Q2 Class**

**NOT.** [3, 8, 11–12]
* **Justification:** DT4IER is an offline RL / Decision Transformer sequence modeling framework that predicts recommended item lists conditioned on Return-to-Go (RTG) prompts [3, 8, 10–12]. It does **not** produce or publish a per-exposure retention credit table or multi-touch attribution decomposition.

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction credit table.** [8, 10–12]
* **Target Outcome & Formula:** Replaces temporal value estimation with
… [truncated]

### Stratified Expert Cloning for Retention-Aware Recommendation at Scale [1]
`2025_CIKM_SEC_Stratified-Expert-Cloning.md`
**Source:** https://arxiv.org/pdf/2504.05628.pdf  
**Q2 class:** NOT

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
* **Mechanism:** Bypasses temporal credit assignment by casting retention optimization as supervised imitation learning over expert state-action pairs
… [truncated]

### Impatient Bandits: Optimizing for the Long-Term Without Delay [1]
`2025_JMLR_ImpatientBandits_Optimizing-Recommendations-Long-Term.md`
**Source:** https://arxiv.org/pdf/2501.07761.pdf  
**Q2 class:** NOT

### **Source Evaluation: *Impatient Bandits: Optimizing for the Long-Term Without Delay***
*(Zhang et al., Imperial College London, University of Manchester, Spotify, Reflection AI, & Columbia University; JMLR 2026 / arXiv: `2501.07761`)* [1]

---

### **(A) Q1 or Q2 or Both or Neither?**

**Neither.** [1, 6–8]  
* **Q1 (Industry/Production Attribution 2025-01 to 2026-09):** **No.** While submitted in January 2025, published in March 2026 in JMLR (Vol. 27), and deployed live at Spotify, this paper presents a **bandit exploration algorithm** for long-term reward optimization rather than an industry multi-touch attribution measurement framework [1, 6–8].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The algorithm optimizes long-term 60-day engagement for podcast recommendations using progressive feedback, but it does **not** perform historical multi-touch sequence attribution or allocate per-swipe credit across past interaction logs [1-4].

---

### **(B) Q2 Class**

**NOT.** [8, 30–31]  
* **Justification:** Impatient Bandits is a multi-armed bandit policy framework (Impatient Thompson Sampling with an empirical Gaussian Bayesian filter) that updates posterior probability distributions over latent content stickiness vectors \\(\theta_a\\) [8, 29–31]. It does **not** generate or publish a per-exposure retention credit table.

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction credit.** [8, 30–31]
* **Target Outcome:** **60-Day Cumulative Active Days
… [truncated]

### Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking [1]
`2025_KDD_NA_Interleaving-Counterfactual-Airbnb-Search.md`
**Source:** https://arxiv.org/pdf/2508.00751.pdf  
**Q2 class:** NOT

### **Source Evaluation: *Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking***
*(Zhang et al., Airbnb & Microsoft, KDD 2025: `arXiv:2508.00751`)* [1, 2]

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**

**Q1 only.** [1-3]  
* **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **Yes.** Published in August 2025 at KDD 2025 (`arXiv:2508.00751`), this paper describes a production evaluation and multi-session conversion attribution framework deployed live in production across Airbnb's search ranking infrastructure [1-3].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper focuses on evaluating candidate search rankers and attributing accommodation booking conversions across multi-session search journeys, rather than attributing user retention, active days, or return visits [1, 4, 5].

---

### **(B) Q2 Class**

**NOT.** [8, 10, 35–36]  
* **Justification:** The paper presents online experimentation and counterfactual evaluation frameworks (Interleaving and Counterfactual Evaluation) for accelerating search ranker evaluation, rather than publishing a per-exposure retention credit table or interaction-level retention attribution model [8, 10, 35–36].

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **Yes (at the search-occurrence and competitive-pair level)** [15, 26, 28, 39–41].
* **Target Outcome:** **Accommodation Booking Conversions** (and clicks) [1, 5]. Section 5.5 explicitly details that
… [truncated]

