### **Modeling Impression Discounting in Large-scale Recommender Systems**
*   **(1) Bibliography:** *Modeling Impression Discounting in Large-scale Recommender Systems*, Pei Lee, Laks V.S. Lakshmanan, Mitul Tiwari, Sam Shah, 2014, ACM KDD '14 [1, 2].
*   **(2) What they did:** Analyzed implicit "no-action" user feedback (repeatedly viewing recommendations without converting) on a massive scale across LinkedIn's "People You May Know" (PYMK) and "Endorsements" [3, 4]. They designed linear, inverse, exponential, and quadratic decay regression models to discount and re-rank ignored items [3, 5].
*   **(3) Two-sided balancing mechanism:** Operates as a post-processing plugin applying a discounting factor \\(d \le 1\\) to ranking scores (\\(T^*.R = T.R \cdot d\\)) [6, 7]. Highly exposed but unaccepted items are dynamically demoted, allowing fresh, under-exposed candidates to surface to improve user conversion and satisfaction [8, 9].
*   **(4) Metrics and reported effect:** In offline evaluations, the models yielded up to a 31% improvement in the PYMK invitation rate [5]. In online A/B testing, the models achieved up to a 13.26% (or up to 13%) improvement in the invitation rate depending on the decay function utilized [5, 10].
*   **(5) Fit for a dating app:** **High**. Dating app users experience massive repetition fatigue; automatically discounting profiles that a user repeatedly views but ignores (swipes left or ignores) ensures that they are replaced with fresher prospects.
*   **(6) Confidence:** **High** [5, 7].

---

### **LiJAR: Job Application Redistribution**
*   **(1) Bibliography:** *LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace*, Fedor Borisyuk, Liang Zhang, Krishnaram Kenthapadi, 2017, ACM KDD '17 [11-13].
*   **(2) What they did:** Formulated the job application redistribution problem to address marketplace imbalances where some postings receive too many applications and others receive too few [11]. They designed a dynamic Gamma-Poisson and Negative Binomial forecasting model to predict total applications at expiration and built real-time boosting and penalization algorithms [14-17].
*   **(3) Two-sided balancing mechanism:** Estimates application confidence intervals [17]. If the upper bound falls below minimum targets (minApps), the score is boosted by a constant factor [17, 18]. If the lower bound exceeds maximum targets (maxApps), the score is exponentially decayed based on current application counts [17, 19].
*   **(4) Metrics and reported effect:** Achieved a 6.5% user engagement increase for underserved postings (Bucket 1) and reduced over-served posting applications by 8.7% (Bucket 3) [14, 20]. Deploying the system increased the entropy of the job application distribution by 12% while keeping total applications positive (+2.3%) [20, 21].
*   **(5) Fit for a dating app:** **High**. It directly mitigates the "superstar effect" where highly attractive profiles are flooded with incoming messages they cannot meaningfully manage, while simultaneously distributing attention to under-exposed, highly compatible users.
*   **(6) Confidence:** **High** [14, 22, 23].

---

### **DPGNN: Dual-Perspective Graph Neural Network**
*   **(1) Bibliography:** *Modeling Two-Way Selection Preference for Person-Job Fit*, Chen Yang, Yupeng Hou, Yang Song, Tao Zhang, Ji-Rong Wen, Wayne Xin Zhao, 2022, ACM RecSys '22 [24-26].
*   **(2) What they did:** Explicitly modeled the bilateral, directed two-way selection preferences of both job seekers and employers in online recruitment [27, 28]. They proposed DPGNN, which utilizes dual-node representations for each user, updates representations via hybrid GCN propagation, and optimizes models using quadruple-based and contrastive losses [27, 29].
*   **(3) Two-sided balancing mechanism:** Instantiates an active selection node (\\(c^a\\)) and a passive attractiveness node (\\(c^p\\)) for each user [30]. Performs hybrid GCN propagation to balance unidirectional interactions (applications/outreach) with bidirectional matching history to ensure both users' mutual expectations are met [31-34].
*   **(4) Metrics and reported effect:** Evaluated on Tech, Sales, and Design datasets [35]. DPGNN outperformed best baselines in Recall@5, Precision@5, NDCG@5, and MRR@5, yielding relative improvements of 7.12% on Tech, 4.81% on Sales, and 7.73% on Design [36, 37].
*   **(5) Fit for a dating app:** **High**. Dating is fundamentally a two-way selection process; decoupling active swiping preferences from passive swiping attractiveness prevents recommending matches destined for unilateral rejection.
*   **(6) Confidence:** **High** [27, 29].

---

### **Fast and Examination-agnostic Reciprocal Recommendation (TU Matching)**
*   **(1) Bibliography:** *Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets*, Yoji Tomita, Riku Togashi, Yuriko Hashizume, Naoto Ohsaka, 2023, ACM RecSys '23 [38-40].
*   **(2) What they did:** Proposed a reciprocal recommendation method based on matching with transferable utility (TU matching/Choo-Siow model) to handle system congestion and popularity concentration [38, 41, 42]. They designed a scalable vector concatenation strategy that maintains dot-product structure for sublinear, real-time maximum inner product search (MIPS) [43, 44].
*   **(3) Two-sided balancing mechanism:** Leverages an Iterative Proportional Fitting Procedure (IPFP) to compute market-clearing outside-option probabilities, which are concatenated into \\((2d+2)\\)-dimensional feature maps [44-46]. This dynamically offsets popularity imbalances and balances mutual preferences across both sides of the market [47].
*   **(4) Metrics and reported effect:** Evaluated on synthetic data and real dating platform data [48, 49]. Significantly outperformed Naive and Reciprocal baselines in matches (e.g., 152.39 matches in synthetic \\(n=100\\) vs. 106.45 for Naive) [50, 51]. Successfully scaled to \\(1000\times1000\\) users where the SW baseline failed [52-54], and improved Gini equity [55].
*   **(5) Fit for a dating app:** **High**. Grounded and tested directly on a Japanese online dating platform (Tapple) to distribute matches fairly and resolve real-time scaling bottlenecks under millions of active members [49, 56].
*   **(6) Confidence:** **High** [42, 43].

---

### **Revisiting Reciprocal Recommender Systems (CRRS)**
*   **(1) Bibliography:** *Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method*, Chen Yang, Sunhao Dai, Yupeng Hou, Wayne Xin Zhao, Jun Xu, Yang Song, Hengshu Zhu, 2024, ACM KDD '24 [57-59].
*   **(2) What they did:** Addressed the issue of redundant mutual recommendations by proposing five holistic evaluation metrics (covering overall coverage, bilateral stability, and balanced ranking) [60-62]. They introduced the CRRS framework under a causal potential outcome framework to model recommendation effects as bilateral treatments [63, 64].
*   **(3) Two-sided balancing mechanism:** Models recommendations as bilateral treatments (\\(T_A, T_B \in \{10, 11, 01, 00\}\\)) [65]. It employs a vacant-slots reranking strategy that dynamically computes expected matching payoffs to optimize overall matching coverage while selectively filtering out redundant dual-sided recommendations [66, 67].
*   **(4) Metrics and reported effect:** Proposed CRecall, CPrecision, SRecall, SPrecision, and RNDCG [68-70]. CRRS (LightGCN) achieved significant gains: CRecall@50 rose to 0.4670 (vs. 0.4555 for DPGNN) on Recruitment and to 0.3387 (vs. 0.3007) on Dating [71, 72]. True positive matches increased to 10,490 and 1,743 [71, 72].
*   **(5) Fit for a dating app:** **High**. Dating platform success depends on maximizing distinct matched couples (coverage) rather than wasting recommendation slots showing Bob to Alice when Bob already liked Alice.
*   **(6) Confidence:** **High** [63, 73].

---

### **Fair Reciprocal Recommendation in Matching Markets (NSW)**
*   **(1) Bibliography:** *Fair Reciprocal Recommendation in Matching Markets*, Yoji Tomita, Tomohiko Yokoyama, 2024, ACM RecSys '24 [74, 75].
*   **(2) What they did:** Investigated fairness of opportunity (exposure) in reciprocal recommender systems using fair division theory, formalizing the concept of "envy-freeness" [76-78]. They proposed an alternating Nash Social Welfare (NSW) maximization algorithm via Frank-Wolfe to balance the trade-off between maximizing overall matches and guaranteeing envy-free exposure opportunities [77, 79].
*   **(3) Two-sided balancing mechanism:** Alternately maximizes Left-side and Right-side log-NSW style functions (which calculate the product of expected utilities) [80, 81]. This dynamically scales back exposure for overly popular users, ensuring more balanced exposure distribution and envy-freeness up to \\(O(\epsilon)\\) [82, 83].
*   **(4) Metrics and reported effect:** Simulated on synthetic and real online dating data [84]. NSW achieved near *zero* instances of envy (e.g., male envy dropped to 31 vs. 736 for TU) while retaining highly competitive match totals (90.39 matches in log-v vs. 102.69 for TU) [85-87].
*   **(5) Fit for a dating app:** **High**. Solves user churn driven by the "envy" average users experience when popular profiles monopolize exposure, by ensuring fairer, more balanced profile visibility.
*   **(6) Confidence:** **High** [77, 78].

---

### **BOSS: A Bilateral Occupational-Suitability-Aware Recommender System**
*   **(1) Bibliography:** *BOSS: A Bilateral Occupational-Suitability-Aware Recommender System for Online Recruitment*, Xiao Hu, Yuan Cheng, Zhi Zheng, Yue Wang, Xinxin Chi, Hengshu Zhu, 2023, ACM KDD '23 [88-90].
*   **(2) What they did:** Formulated BOSS, a multi-task recommender system mapping the progressive, multi-stage sequential action flow (Click \\(\rightarrow\\) Apply \\(\rightarrow\\) Review \\(\rightarrow\\) Accept) of online recruitment [91-94]. They utilized a multi-group Mixture-of-Experts (MoE) structure to learn independent preferences and handle bilateral, reciprocal, and sequential characteristics [91, 92, 95].
*   **(3) Two-sided balancing mechanism:** Models sequential actions progressively via chained conditional probabilities [96]. Features of job seekers and recruiters are separately processed in dedicated expert groups to learn directional preference probabilities, yielding reciprocal recommendations based on their probability product (\\(p(accept)\\)) [95-97].
*   **(4) Metrics and effects:** Evaluated across 5 large recruitment datasets [98]. Passed t-test significance (Technology AUC reached 0.8918 vs. 0.8782 for single-class models) [99, 100]. Online A/B testing on BOSS Zhipin showed a 6.15% average acceptance rate gain [101].
*   **(5) Fit for a dating app:** **Medium-High**. Highly applicable to dating's sequential progression (Swipe \\(\rightarrow\\) Match \\(\rightarrow\\) Chat \\(\rightarrow\\) Meet), capturing how the proactive side's swipe gates the reactive side's review and accept steps.
*   **(6) Confidence:** **High** [95, 96, 100].

***

🎧 This comprehensive set of two-sided balancing papers would make a highly engaging audio overview if you'd like to hear a podcast-style deep dive on how these platforms solve marketplace congestion.