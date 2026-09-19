# Compact card summaries — truncated Summary + Evidence from this-run cards (1/2)

### A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications [1]
`2020_KDD_RDSA_Sleeping-Recovering-Bandit-Notifications.md`
**Source:** https://research.duolingo.com/papers/yancey.kdd20.pdf  
**Q2 class:** NOT

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
  * **Recovering Difference Softmax Algorithm:** Proposes a practical
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Surrogate for Long-Term User Experience in Recommender Systems [1]
`2022_KDD_NA_Surrogate-Long-Term-User-Experience.md`
**Source:** https://dl.acm.org/doi/pdf/10.1145/3534678.3539073  
**Q2 class:** NOT

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
  1. **Behavioral Measurement Metrics:** Defines metrics capturing users' sequential medium-term consumption patterns (entropy diversity, KL-divergence diversity, repeated consumption, high-quality completion ratio, persistent
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Long-run User Value Optimization in Recommender Systems through Content Creation Modeling [1]
`2022_arXiv_NA_Long-run-User-Value-Optimization-Meta.md`
**Source:** https://arxiv.org/pdf/2204.11421.pdf  
**Q2 class:** UNSPECIFIED

**Summary.** ### **Part 1: Dating App Retention Attribution Project Evaluation**

#### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**
* **Neither** [1, 2].
* **Explanation:**
  * **Q1 (Industry/Production Attribution 2025–2026):** **No.** Published in 2022 (`arXiv:2204.11421`), which falls outside the 2025–2026 window [1].
  * **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper models content producer supply responses (how giving distribution/engagement to content creators boosts their future posting behavior), rather than attributing user retention, active days, or return visits to individual user interaction sequences [1, 2].

---

#### **(B) Q2 Class**
* **Classification:** **NOT** [1-3].
* **Justification:** The framework scores content producers using a Heterogeneous Treatment Effects (HTE) model (T-Learner / Meta-Learner using GBDTs or Neural Networks) trained on A/B experiment data [2, 3]. It does **not** generate or publish a per-exposure retention credit table or multi-touch attribution model [2, 3].

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction credit** [2, 3].
* **Target Outcome:** **Producer-level uplift score (Individual Treatment Effect / ITE)** measuring the estimated increase in future content creation / posting frequency
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Incrementality-Focused Messaging Measurement (Netflix) — stub
`2023_NetflixBlog_NA_Incrementality-Focused-Messaging-Measurement.md`
**Source:** https://medium.com/notificationsblog/incrementality-focused-messaging-measurement-all-the-time-everywhere-94ef0c229368  
**Q2 class:** PARTIAL

**Summary.** Stub card. NotebookLM could not ingest the Medium URL; jina.ai and direct WebFetch also failed (Cloudflare / timeout). Discovery notes (D3, D4) describe a Netflix production messaging system with an always-on ~2% message holdback that estimates **incremental downstream viewing** per notification/message, contrasting open/click metrics with incremental watch.

**Evidence.** Not specified in source (fetch failed). D3 records: per-message causal incrementality via randomized withholding — a touchpoint-level incrementality design for **notifications**, not per-feed-item or swipe retention credit.

### Interpretable User Retention Modeling in Recommendation [14]
`2023_RecSys_IURO_Interpretable-User-Retention-Modeling.md`
**Source:** https://dl.acm.org/doi/pdf/10.1145/3604915.3608818  
**Q2 class:** PARTIAL

**Summary.** ### **Part 1: Dating App Retention Project Evaluation**

#### **(A) Alignment: Q1 or Q2 or Both or Neither?**
* **Category:** **Q2 Only** [3, 4, 11–12].
* **Explanation:**
  * *Q1 (Industry/Production Attribution 2025–2026):* **No.** Published in September 2023 (RecSys '23), which falls outside the 2025–2026 window [1, 2].
  * *Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):* **Yes.** The paper generates item/action-level retention scores (\\(s_{ui}\\)) and instance-level attention weights over individual user interactions to explain and predict 3-day user retention [7, 11–12].

---

#### **(B) Q2 Class**
* **Classification:** **PARTIAL** [7, 11–12, 14–17].
* **Justification:** IURO generates item/action-level retention scores (\\(s_{ui}\\)) via a UI Scorer and aggregates them using instance-level attention in Multi-Instance Learning (CMIL/RMIL) to predict 3-day retention [11–14]. The paper explicitly acknowledges and addresses offline-online gaps, unpredictable external factors (e.g., user mood or workload), and lack of explicit per-item retention signals [6, 14–15]. However, it does not formulate an identified causal Multi-Touch Attribution (MTA) model under formal counterfactual graph identification [7, 14–17].

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Yes.** Generates
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### User Retention-oriented Recommendation with Decision Transformer [1]
`2023_WWW_DT4Rec_User-Retention-Oriented-Decision-Transformer.md`
**Source:** https://arxiv.org/pdf/2303.06347.pdf  
**Q2 class:** NOT

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *User Retention-oriented Recommendation with Decision Transformer* [1]
* **Authors:** **Kesen Zhao**¹, **Lixin Zou**†², **Xiangyu Zhao**†¹, **Maolin Wang**¹, and **Dawei Yin**³ (\*†Corresponding authors) [1]
* **Author Affiliations:**
  1. **City University of Hong Kong**, Hong Kong (`kesenzhao2-c@my.cityu.edu.hk`, `xianzhao@cityu.edu.hk`, `MorinWang@foxmail.com`) [1]
  2. **Wuhan University**, Wuhan, China (`zoulixin15@gmail.com`) [1]
  3. **Baidu Inc.**, Beijing, China (`yindawei@acm.org`) [1]
* **Year:** **2023** (May 1–5, 2023) [1, 2]
* **Venue:** *Proceedings of the ACM Web Conference 2023 (WWW ’23), Austin, TX, USA* [2]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Optimizing user retention in Sequential Recommender Systems (SRSs) using Reinforcement Learning (RL) faces severe offline learning challenges [1, 3]. Online trial-and-error exploration risks losing users by recommending inappropriate items [3]. Offline RL methods suffer from value estimation instability ("Deadly Triad" in value-based RL) or unbounded variance in counterfactual policy evaluation (policy-based RL) [3]. While Decision Transformers (DT) cast offline RL as autoregressive sequence modeling to avoid these issues [4, 5], applying DT directly to recommendations presents three major
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Reinforcing User Retention in a Billion Scale Short Video Recommender System [1]
`2023_WWW_RLUR_Reinforcing-User-Retention.md`
**Source:** https://arxiv.org/pdf/2302.01724.pdf  
**Q2 class:** NOT

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**

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
  1.
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### **Part 1: Dating App Retention Project Evaluation**
`2024_KDD_FID_Future-Impact-Decomposition.md`
**Source:** https://arxiv.org/pdf/2401.16108.pdf  
**Q2 class:** NOT

**Summary.** ### **Part 1: Dating App Retention Project Evaluation**

#### **(A) Alignment: Q1 or Q2 or Both or Neither?**
* **Answer:** **Neither Q1 nor Q2** [1, 6–7].
* **Explanation:** 
  * *Q1 (Industry Attribution 2025–2026):* Published in August 2024 (KDD ’24), falling outside the 2025–2026 window [6–7].
  * *Q2 (Interaction-Level Retention Attribution):* Focuses on reinforcement learning (RL) policy optimization for list-wise recommendations rather than multi-touch causal attribution over historical user journey logs [8–12, 18].

---

#### **(B) Q2 Classification**
* **Classification:** **NOT** [15, 21–23, 31–36].
* **Justification:** The paper presents an RL actor-critic policy optimization method (**ItemA2C**) that decomposes list-level future value \\(V(s_{t+1})\\) down to individual items for policy gradient updates, rather than publishing an explicit per-exposure retention credit table or multi-touch attribution model [15–18, 35–41].

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Yes (in the form of an RL item-level advantage score)** [1-3]. 
* **Target Outcome & Formula:** Allocates cumulative session rewards and long-term state value \\(V(s_{t+1})\\) (which correlates with 7-day retention) to individual items \\(i_{t,k}\\) in list \\(a_t\\) via item target value \\(\Psi_w\\) and advantage \\(A\\):
 
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Modeling User Retention through Generative Flow Networks [1]
`2024_KDD_GFN4Retention_Modeling-User-Retention.md`
**Source:** https://arxiv.org/pdf/2406.06043.pdf  
**Q2 class:** NOT

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Modeling User Retention through Generative Flow Networks* [1]
* **Authors:** **Ziru Liu**†¹, **Shuchang Liu**†², **Bin Yang**², **Zhenghai Xue**³, **Qingpeng Cai**\*², **Xiangyu Zhao**\*¹, **Zijian Zhang**¹, **Lantao Hu**², **Han Li**², and **Peng Jiang**\*² (*†Co-first authors, \*Corresponding authors*) [1]
* **Author Affiliation:**
  1. **City University of Hong Kong**, Hong Kong, China [1]
  2. **Kuaishou Technology**, Beijing, China [1]
  3. **Nanyang Technological University**, Singapore [1]
* **Year:** **2024** (Published August 2024) [3–4]
* **Venue:** *Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD ’24), August 25–29, 2024, Barcelona, Spain* [3–4]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Standard recommender systems optimize for immediate item-level feedback (clicks, likes, watch time) [2]. However, these short-term metrics fail to capture long-term user satisfaction and retention (return-to-app behavior) [5–6]. Optimizing retention is difficult due to its between-session nature, delayed/sparse return signals, unobservable user activity between sessions, and the uncertain relationship between immediate item feedback and return time [3, 4]. Standard Reinforcement Learning (RL) approaches suffer from severe
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Learned Ranking Function: From Short-term Behavior Predictions to Long-term User Satisfaction [1]
`2024_RecSys_LRF_Learned-Ranking-Function-YouTube.md`
**Source:** https://arxiv.org/pdf/2408.06512.pdf  
**Q2 class:** NOT

**Summary.** ### **Part 1: Detailed Technical Breakdown of the Source**

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Learned Ranking Function: From Short-term Behavior Predictions to Long-term User Satisfaction* [1]
* **Authors:** **Yi Wu**\*¹, **Daryl Chang**\*¹, **Jennifer She**¹, **Zhe Zhao**¹, **Li Wei**¹, and **Lukasz Heldt**¹ (\*Equal contribution) [1]
* **Affiliations:** **Google / YouTube** (San Bruno, CA & Mountain View, CA, USA) [1, 2]
* **Year & Venue:** Published in **2024** at the *Proceedings of the 18th ACM Conference on Recommender Systems (RecSys ’24), October 14–18, 2024, Bari, Italy* [1]. (arXiv pre-print: `arXiv:2408.06512`, August 2024).

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Large-scale video recommendation systems generate multi-task predictions for short-term user behaviors (e.g., CTR, watch time after click), but combining these predictions into a single ranking score typically relies on heuristic functions or manual tuning (e.g., Bayesian optimization) [1, 3]. These heuristics struggle to scale, adapt to changing platform objectives, or directly optimize for long-term user satisfaction across the entire platform [1, 4]. Furthermore, existing slate optimization frameworks assume zero future rewards when a user abandons a slate, which is unrealistic for platforms where users navigate
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Sequential Recommendation for Optimizing Both Immediate Feedback and Long-term Retention
`2024_arXiv_NA_Sequential-Rec-Immediate-Feedback-Long-term-Retention.md`
**Source:** https://arxiv.org/html/2404.03637  
**Q2 class:** NOT

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Sequential Recommendation for Optimizing Both Immediate Feedback and Long-term Retention*
* **Authors:** Not specified in source.
* **Affiliations:** Not specified in source.
* **Year:** **2024** (April 2024, `arXiv:2404.03637v2`).
* **Venue:** arXiv pre-print (`arXiv:2404.03637v2`).

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Standard sequential recommender systems often optimize a single metric—either immediate user feedback (e.g., Click-Through Rate / CTR) or long-term retention (e.g., return frequency) [11–12]. Optimizing solely for immediate feedback leads to myopic recommendations, while focusing only on retention ignores immediate user satisfaction [11–12]. However, adapting Decision Transformers (DT) to multi-reward contexts presents major challenges:
  1. Complex dynamics among diverse user responses make reward design difficult [1].
  2. Interdependencies among multiple objectives introduce training complexity and task interference [1].
* **Key Contributions:**
  1. **DT4IER Framework:** Introduces Decision Transformer for Integrated Engagement and Retention, a framework engineered for long short-term multi-task sequential recommendation scenarios [5–6].
  2. **Adaptive RTG Balancing Module:** Adaptively reweights short-term (CTR) and long-term (return
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Stratified Expert Cloning for Retention-Aware Recommendation at Scale [1]
`2025_CIKM_SEC_Stratified-Expert-Cloning.md`
**Source:** https://arxiv.org/pdf/2504.05628.pdf  
**Q2 class:** NOT

**Summary.** ### **1. Title, Authors, Affiliations, Year, Venue**
* **Title:** *Stratified Expert Cloning for Retention-Aware Recommendation at Scale* [1]
* **Authors:** **Chengzhi Lin**\*¹, **Annan Xie**\*², **Shuchang Liu**¹, **Wuhong Wang**¹, **Chuyuan Wang**¹, **Yongqi Liu**¹, and **Han Li**¹ (\*Equal contribution) [1]
* **Affiliations:** 
  1. **Kuaishou Technology**, Beijing, China (`1132559107@qq.com`, `{liushuchang, wangwuhong, wangchuyuan, liuyongqi, lihan}@kuaishou.com`) [1]
  2. **Peking University**, Beijing, China (`2301210470@stu.pku.edu.cn`) [1]
* **Year:** **2025** (Published November 2025) [2, 3]
* **Venue:** *Proceedings of the 34th ACM International Conference on Information and Knowledge Management (CIKM ’25), November 10–14, 2025, Seoul, Republic of Korea* [2, 3]

---

### **2. Core Problem and Key Contribution**
* **Core Problem:** Standard recommender systems focus on short-term engagement metrics (e.g., click-through rates), failing to model the long-term temporal dynamics of user retention [1, 4]. While Reinforcement Learning (RL) methods can optimize long-term rewards, they suffer from severe challenges in large-scale recommender systems, including delayed credit assignment, high sample complexity/inefficiency, exploration risks (frustrating users with poor recommendations), and complex evolving user preferences [1, 5, 13–16].
* **Key
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Impatient Bandits: Optimizing for the Long-Term Without Delay [1]
`2025_JMLR_ImpatientBandits_Optimizing-Recommendations-Long-Term.md`
**Source:** https://arxiv.org/pdf/2501.07761.pdf  
**Q2 class:** NOT

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Impatient Bandits: Optimizing for the Long-Term Without Delay* [1]
* **Authors & Affiliations:**
  * **Kelly W. Zhang** (`kelly.zhang@imperial.ac.uk`) — **Imperial College London** [1]
  * **Thomas Baldwin-McDonald** (`tommcdonald955@gmail.com`) — **University of Manchester** [1]
  * **Kamil Ciosek** (`kamilc@spotify.com`) — **Spotify** [1]
  * **Lucas Maystre** (`lucas@reflection.ai`) — **Reflection AI** [1]
  * **Daniel Russo** (`djr2174@gsb.columbia.edu`) — **Columbia University** [1]
* **Year:** **2026** (Submitted January 2025; Published March 2026) [1]
* **Venue:** ***Journal of Machine Learning Research* (JMLR)**, Vol. 27, pp. 1–58, 2026 [1]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Large-scale recommender systems face a severe trade-off between learning speed and long-term metric alignment [1, 2]. Waiting weeks or months (e.g., 60 days) to observe true long-term user satisfaction drastically slows learning and fails in **cold-start settings** for newly released content [1, 4–5]. Conversely, optimizing for immediate proxy metrics (like click-through rate or day-two return) leads to myopic recommendations poorly aligned with long-term retention [1-3].
* **Key Contributions:**
  1. **Bandits with Progressive Feedback Framework:** Formulates a multi-armed
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking [1]
`2025_KDD_NA_Interleaving-Counterfactual-Airbnb-Search.md`
**Source:** https://arxiv.org/pdf/2508.00751.pdf  
**Q2 class:** NOT

**Summary.** ### **Part 1: Detailed Technical Breakdown of the Source**

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking* [1]
* **Authors:** **Qing Zhang**¹, **Alex Deng**\*², **Michelle Du**¹, **Huiji Gao**¹, **Liwei He**¹, and **Sanjeev Katariya**¹ (\*Work completed while employed by Airbnb) [1]
* **Affiliations:** 
  1. **Airbnb** (San Francisco, CA & Seattle, WA, USA) [1]
  2. **Microsoft** (Seattle, WA, USA) [1]
* **Year:** **2025** (Conference dates: August 3–7, 2025) [2]
* **Venue:** *Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 (KDD ’25), August 3–7, 2025, Toronto, ON, Canada* [2–3]

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Online A/B testing on e-commerce platforms like Airbnb requires long running times to achieve statistical power for sparse conversion metrics (accommodations booking) [3]. Airbnb users travel infrequently (~twice a year), search journeys span multiple days, and effect sizes of mature ranking algorithms are small [3]. Offline evaluation metrics (e.g., NDCG) are fast but lack accuracy and disconnect from online business conversion metrics [6–7].
* **Key Contributions:**
  1. **Competitive Pair Team Drafting Interleaving:** An unbiased, computationally
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Buyer journey insights with data-driven attribution [1]
`2025_LinkedIn_LiDDA_Buyer-Journey-Data-Driven-Attribution.md`
**Source:** https://www.linkedin.com/blog/engineering/marketing/buyer-journey-insights-with-data-driven-attribution  
**Q2 class:** NOT

**Summary.** ### **1. Title, Authors, Affiliations, Year, Venue**
* **Title:** *Buyer journey insights with data-driven attribution* [1]
* **Authors:** **John Bencina**, **Erkut Aykutlug**, **Changshuai Wei**, and **Shao Tang** [1]
* **Affiliation:** **LinkedIn** [1, 2]
* **Year:** **2025** (Published January 22, 2025) [1]
* **Venue:** **LinkedIn Engineering Blog** [1, 3]

---

### **2. Core Problem and Key Contribution**
* **Core Problem:** Traditional Rule-Based Attribution (RBA)—such as last-touch or last-click—severely overvalues bottom-of-funnel channels (e.g., Search, Email) while completely ignoring upper and mid-funnel touchpoints (e.g., Video Ads, Digital Display) [4, 5]. Additionally, bottom-up Multi-Touch Attribution (MTA) misses user-level paid media impression data due to privacy restrictions and operates in isolation from top-down macro-economic factors, leading to inconsistent reporting against Marketing Mix Modeling (MMM) [6-9].
* **Key Contribution:** A unified, hybrid attribution architecture at LinkedIn that combines a **Transformer self-attention MTA sequence model** (incorporating member/company embeddings and probabilistic paid-media impression imputation) with **top-down MMM post-modeling calibration** [1, 2, 6, 7, 9, 10].

---

### **3. Proposed Method or Architecture in Detail**
* **Model Formulation:** A binary classification task \\(P(C \mid
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

