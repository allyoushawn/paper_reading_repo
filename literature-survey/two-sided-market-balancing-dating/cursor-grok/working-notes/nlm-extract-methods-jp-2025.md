### **1. Palomares Reciprocal RecSys Survey 2021**
*   **(1) Bibliography:** *Reciprocal Recommender Systems: Analysis of state-of-art literature, challenges and opportunities towards social recommendation*, Iván Palomares, Carlos Porcel, Luiz Pizzato, Ido Guy, Enrique Herrera-Viedma, James Neve, 2021, *Information Fusion* (Volume 69) [1, 2].
*   **(2) What they did:** Conducted a comprehensive "snapshot-style" review summarizing the state of reciprocal recommender system (RRS) research up to 2021 [3]. They formalized a general RRS conceptual model centered on preference-fusion processes [4], mapped out a two-level taxonomy of algorithms (content-based, collaborative filtering, hybrid) [5, 6], and highlighted key engineering challenges such as data sparsity, the cold-start problem, same-gender matchmaking, and popularity bias [7, 8].
*   **(3) Two-sided balancing mechanism:** Analyzed various preference-aggregation functions (e.g., harmonic mean, geometric mean, arithmetic mean, and cross-ratio uninorms) used to fuse unilateral user-to-user preferences into reciprocal compatibility scores, showing how pessimistic operators like the harmonic mean prevent popularity congestion [3, 9-12].
*   **(4) Metrics and reported effect:** Adapted classical information retrieval and machine learning metrics to reciprocal contexts, defining: Precision (P@n), Recall (R@n), Success Rate (S@n), Failure Rate (F@n), and Reciprocal Rank (RR) [13-15]. They reported that introducing a reciprocal instead of a non-reciprocal score in dating top-10 lists improves the matching success rate by 83.48% [16].
*   **(5) Dating-app fit:** **High**. Grounded heavily in online dating literature and architectures (analyzing systems like RECON, RCF, and LFRR), making it highly relevant to optimizing dating recommendation pipelines [17-19].
*   **(6) Confidence:** **High** [1].

---

### **2. Pizzato UMUAI People-to-People**
*   **(1) Bibliography:** *Recommending people to people: The nature of reciprocal recommenders with a case study in online dating*, Luiz Pizzato, Tomek Rej, Joshua Akehurst, Irena Koprinska, Kalina Yacef, Judy Kay, 2013, *User Modeling and User-Adapted Interaction* (Volume 23, Issue 5) [20].
*   **(2) What they did:** Established the first comprehensive conceptual framework for reciprocal recommenders, distinguishing them from traditional product recommenders by unique characteristics (e.g., detailed self-profiles, early user exit, and rejection cost) [20-23]. They designed and evaluated content-based and collaborative filtering approaches in online dating [21, 24].
*   **(3) Two-sided balancing mechanism:** Introduced the **RECON** algorithm, which aggregates unilateral preferences using a harmonic mean to prioritize mutual interest [25, 26]. They also developed an overall compatibility score (C±) that subtracts negative preferences (dislikes) from positive preferences (likes) to minimize the risk of rejection [27, 28].
*   **(4) Metrics and reported effect:** Evaluated S@n (Success rate), R@n (Recall), and F@n (Failure rate) [29]. RECON top-10 recommendations achieved a 42.20% success rate compared to 23.00% for a non-reciprocal baseline (an 83.48% relative improvement) [30]. Incorporating negative preferences successfully reduced the failure rate for lower values of *n* [31, 32].
*   **(5) Dating-app fit:** **High**. Grounded directly in online dating case studies and validated on a large commercial dating website dataset containing 1.4 million messages [21, 33].
*   **(6) Confidence:** **High** [20].

---

### **3. Kleinerman RecSys 2018 Balancing Receiver**
*   **(1) Bibliography:** *Optimally Balancing Receiver and Recommended Users' Importance in Reciprocal Recommender Systems*, Akiva Kleinerman, Ariel Rosenfeld, Francesco Ricci, Sarit Kraus, 2018, ACM RecSys '18 [34, 35].
*   **(2) What they did:** Developed the **Reciprocal Weighted Score (RWS)** algorithm, which estimates a user's interest using collaborative filtering and predicts the recommended user's reply likelihood using an AdaBoost classifier, balancing the two into a single score [36-38].
*   **(3) Two-sided balancing mechanism:** Personalizes the relative importance weight (\\(\alpha_x\\)) individually for each user using Brent's numerical method based on their past interaction history [39-41]. For users with no past successful interactions, a global weight of \\(\alpha = 0.3978\\) is calculated [42].
*   **(4) Metrics and reported effect:** Evaluated via an online study on the *Doovdevan* dating app with 398 users [43, 44]. RWS significantly increased successful interactions (RI rose from 1 in control to 8 in treatment; total replies I rose from 99 to 322) [45]. RWS also recommended significantly less popular users, effectively reducing information overload [46].
*   **(5) Dating-app fit:** **High**. Built, optimized, and evaluated directly in a live, operational online dating application (*Doovdevan*) with active members [34, 43].
*   **(6) Confidence:** **High** [34].

---

### **4. Christakopoulou Capacity Constraints CIKM 2017**
*   **(1) Bibliography:** *Recommendation with Capacity Constraints*, Konstantina Christakopoulou, Jaya Kawale, Arindam Banerjee, 2017, ACM CIKM '17 [47].
*   **(2) What they did:** Proposed a multi-objective optimization framework that balances standard recommendation accuracy with expected item usage limits [47]. They applied this to three state-of-the-art latent factor models: PMF, BPR, and GeoMF [47, 48].
*   **(3) Two-sided balancing mechanism:** Adds a capacity loss penalty to the recommendation objective function, balanced by a trade-off parameter (\\(\alpha\\)) [48, 49]. They introduced the concept of user propensity to follow recommendations to weigh expected item exposure [48, 50].
*   **(4) Metrics and reported effect:** Evaluated test RMSE, pairwise 0/1 loss, capacity loss, and Weighted Average Precision (WAP@top) [49, 51-53]. On Movielens 100K, Cap-BPR reduced capacity loss to 0.08 (vs. 4.51 for standard BPR) with only a minor rise in pairwise loss (0.14 vs. 0.12) [54]. Incorporating actual capacities also improved top-N precision (WAP@10 rose from 0.016 to 0.041 on Foursquare) [55, 56].
*   **(5) Dating-app fit:** **High/Medium**. While framed around movies and POI check-ins, its formulation of penalizing overallocation of scarce resources (modeled as item capacities and user propensities) is highly applicable to mitigating the "superstar effect" in dating apps [47, 57].
*   **(6) Confidence:** **High** [47].

---

### **5. Singh Joachims Fairness of Exposure**
*   **(1) Bibliography:** *Fairness of Exposure in Rankings*, Ashudeep Singh, Thorsten Joachims, 2018, ACM KDD '18 [58, 59].
*   **(2) What they did:** Formulated a group fairness framework for ranked lists based on exposure allocation [58]. They developed a linear programming approach to maximize user relevance utility while satisfying group-level exposure constraints, decomposing the resulting doubly stochastic matrices into deterministic rankings [58, 60].
*   **(3) Two-sided balancing mechanism:** Implements group fairness constraints (demographic parity, disparate treatment, and disparate impact) by mapping position bias to exposure allocation, ensuring that a group's average exposure is proportional to its average relevance [61-64].
*   **(4) Metrics and reported effect:** Evaluated DCG, Disparate Treatment Ratio (DTR), and Disparate Impact Ratio (DIR) [65, 66]. In a job seeker simulation, the unconstrained ranking yielded a DTR of 1.7483; the fair ranking achieved a DTR of 1.0000 with a minimal utility drop (DCG went from 3.8193 to 3.8044) [65, 67]. Similar results were shown on the Yow news dataset [68].
*   **(5) Dating-app fit:** **High**. Can be used directly to enforce exposure equity across user groups (e.g., based on demographic attributes or desirability tiers) to resolve the natural "superstar congestion" of dating platforms [58].
*   **(6) Confidence:** **High** [58].

---

### **6. Do Lorenz Two-Sided Fairness**
*   **(1) Bibliography:** *Two-sided fairness in rankings via Lorenz dominance*, Virginie Do, Sam Corbett-Davies, Jamal Atif, Nicolas Usunier, 2021, NeurIPS '21 [69].
*   **(2) What they did:** Formulated two-sided ranking fairness grounded in welfare economics, defining fair rankings as those with non-dominated generalized Lorenz curves [69, 70]. They designed a global optimization framework that maximizes concave social welfare functions for both users and items using the Frank-Wolfe algorithm [69, 71, 72].
*   **(3) Two-sided balancing mechanism:** Maximizes a parameterized, strictly concave social welfare function (\\(W_\theta\\)) that penalizes inequality by giving more weight to the worst-off users and items, extending this to symmetric reciprocal utilities in dating [71, 73-75].
*   **(4) Metrics and reported effect:** Measured user/item Gini indices, total user utility, and cumulative utility for the worse-off (10%, 25%, and 50% bins) [76-78]. On a Higgs Twitter reciprocal matching dataset (13k users), welfare optimization with \\(\alpha = -5\\) more than doubled the utility of the 10% worst-off users compared to \\(\alpha = 1\\), outperforming equal utility and exposure-based baselines [79, 80].
*   **(5) Dating-app fit:** **High**. Contains an explicit theoretical and experimental extension to reciprocal people-to-people matching (such as online dating) where users are both consumers and recommended items [69, 70, 74, 75].
*   **(6) Confidence:** **High** [69].

---

### **7. MODE Mutual Optimality**
*   **(1) Bibliography:** *MODE: Mutual Optimality in Direct Effects of Reciprocal Recommendations in Matching Markets*, Yoji Tomita, 2026, ACM RecSys '26 (Minneapolis, MN) [81].
*   **(2) What they did:** Defined "optimality of direct effects"—where a user's recommendation list is optimal for their own utility given recommendations shown to others—and developed **MODE** (Mutually Optimal recommendation in Direct Effects), an iterative deterministic ranking algorithm to solve it [82, 83].
*   **(3) Two-sided balancing mechanism:** Iteratively computes optimal deterministic lists for each user by modeling their expected match probabilities [83, 84]. It treats other users' lists as fixed to estimate positional ranking probabilities on the opposite side, dynamically dispersing exposure and reducing congestion [83-85].
*   **(4) Metrics and reported effect:** Evaluated expected matches (social welfare) and sub-optimality of direct effects [86]. In 1000x1000 user simulations on real-world online dating logs, MODE achieved a substantial match increase (>10%) over existing deterministic baselines (Naive, Reciprocal, and TU matching) with fast processing speeds [87-90].
*   **(5) Dating-app fit:** **High**. Developed by a lead researcher at CyberAgent specifically for matchmaking platforms and validated on large-scale real-world online dating data [81, 82, 91].
*   **(6) Confidence:** **High** [81].

---

### **8. Wantedly/Hayashi OPE Matching Markets RecSys 2025**
*   **(1) Bibliography:** *Off-Policy Evaluation and Learning for Matching Markets*, Yudai Hayashi, Shuhei Goda, Yuta Saito, 2025, ACM RecSys '25 (Prague, Czech Republic) [92-94].
*   **(2) What they did:** Formulated off-policy evaluation (OPE) and off-policy learning (OPL) for reciprocal matching markets to evaluate new recommendation policies offline, introducing two hybrid estimators: **DiPS** (Direct and Propensity Score) and **DPR** (Direct, Propensity, and doubly Robust) [92, 95-98].
*   **(3) Two-sided balancing mechanism:** Leverages the unique two-stage interaction structure of matching platforms (first-stage: initial reach-out/scout; second-stage: recipient response) to decompose reward estimation [97-99]. DiPS applies importance weighting to first-stage rewards and imputes second-stage outcomes with regression, reducing matching sparsity [97, 98, 100, 101].
*   **(4) Metrics and reported effect:** Evaluated Mean Squared Error (MSE), ErrorRate, and policy value [102-104]. In real-world experiments using A/B logs from the job platform *Wantedly Visit* (21,736 companies, 17,460 seekers, 1.2% sparsity), both DiPS and DPR achieved dramatically lower MSE and ErrorRate than standard IPS and DR estimators, successfully predicting true online A/B results [105-108].
*   **(5) Dating-app fit:** **High**. Online dating apps share the exact two-stage reciprocal interaction structure (first-stage: Swipe Right; second-stage: recipient replies "Thank" to Match), making this OPE method invaluable for offline dating algorithm tuning [99, 106, 109, 110].
*   **(6) Confidence:** **High** [92].

---

### **9. CyberAgent Japanese Blogs on Reciprocal Matching**
*   **(1) Bibliography:** *Analyzing Matches on Matching Apps* & *Aiming for a Matching Platform Where Everyone is Happy*, CyberAgent Developers Blog, 2022, Industry Technical Blog Posts [111-114].
*   **(2) What they did:** Documented CyberAgent's ongoing engineering efforts to optimize the Japanese online dating app **Tapple** (7+ million users) [115]. They analyzed Tapple's collaborative-filtering reciprocal recommenders, identified the severe inequality of profile exposures, and explored matching theory to balance opportunity distribution [113, 115-117].
*   **(3) Two-sided balancing mechanism:** Adopted economic matching theory, specifically Choo and Siow's (2006) **Transferable Utility (TU) matching model**, to incorporate user capacity constraints [113, 117, 118]. To make this computationally feasible for hundreds of thousands of users, they implemented a fast approximation of the equilibrium matching equations [119].
*   **(4) Metrics and reported effect:** Reported that Tapple's matching platform suffers from extreme exposure concentration, with a Gini index of ~0.75 for profile recommendations (similar to other international apps) [116]. Their approximated TU matching system successfully improved exposure equality (coverage rate) and user match distribution [117, 120].
*   **(5) Dating-app fit:** **High**. Written by core Tapple data scientists and engineers specifically detailing the live production architecture, user behavioral characteristics, and matching algorithms of Tapple [115, 117, 119].
*   **(6) Confidence:** **High** [112, 114].

---

### **10. Retention-Optimized Two-Sided Matching arXiv 2602.15752**
*   **(1) Bibliography:** *Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching*, Ren Kishimoto, Rikiya Takehi, Koichi Tanaka, Masahiro Nomura, Riku Togashi, Yoji Tomita, Yuta Saito, 2026, ICLR '26 / arXiv Preprint (arXiv:2602.15752) [121, 122].
*   **(2) What they did:** Addressed a critical limitation in reciprocal recommender systems—where pure match maximization causes popular users to be over-matched while other users churn—by formally defining and optimizing the objective of **maximizing long-term user retention** [123, 124]. They proposed **MRet** (Matching for Retention), a dynamic learning-to-rank algorithm [124].
*   **(3) Two-sided balancing mechanism:** Learns personalized retention curves for each user using their interaction history and profile features [124]. MRet then dynamically adjusts recommendations by evaluating and allocating scarce matches to where they yield the highest net retention gains for both sides of the market [124].
*   **(4) Metrics and reported effect:** Evaluated user retention, match totals, and fairness metrics on synthetic and real-world online dating datasets [124]. Empirically demonstrated that MRet achieves significantly higher long-term user retention compared to traditional match-maximizing or exposure-fairness baselines [124].
*   **(5) Dating-app fit:** **High**. Grounded and validated using a massive, real-world online dating dataset from a major subscription-reliant dating platform where user retention is the primary business driver [123, 124].
*   **(6) Confidence:** **High** [121].

---

### **11. OkCupid JAX Collaborative Filtering**
*   **OkCupid JAX Collaborative Filtering — NO CONTENT** *(Note: This source is not active or present in the provided notebook context).*

---

### **12. RecSys 2022 Matching Theory Tapple Talk**
*   **(1) Bibliography:** *Matching Theory-based Recommender Systems in Online Dating*, Yoji Tomita, Riku Togashi, Daisuke Moriwaki, 2022, ACM RecSys '22 (Seattle, WA) [125, 126].
*   **(2) What they did:** Formulated a scalable, matching-theory-based recommender system (MTRS) for online dating by utilizing economic matching models to replace traditional, capacity-blind preference aggregation functions [127-129].
*   **(3) Two-sided balancing mechanism:** Implements **Choo and Siow's (2006) Transferable Utility (TU) matching model** [129]. It uses the **Iterative Proportional Fitting Procedure (IPFP)**, accelerated via locality-sensitive hashing (LSH) and approximate nearest neighbor search (ANNS), to compute equilibrium matching scores (\\(\mu_{x,y}\\)) that balance user capacities [129-131].
*   **(4) Metrics and reported effect:** Notes that typical online dating platforms suffer from severe sparsity [131, 132]. While standard IPFP is computationally prohibitive at scale, their LSH/ANNS-approximated equilibrium solver reduces computational complexity to \\(O(|X||Y|)\\) per step, enabling personalized recommendations for Tapple's **7 million users** [129, 131, 132].
*   **(5) Dating-app fit:** **High**. Grounded entirely in the deployment of an industrial-grade matching-theory-based recommender on Tapple, one of Japan's most prominent online dating platforms [129, 132].
*   **(6) Confidence:** **High** [125].

***

🎨 I can write a detailed technical brief showing how we can implement the **MODE** algorithm or the **Choo-Siow IPFP solver** in Python using NumPy and SciPy to run high-throughput reciprocal recommendations on your own user preferences dataset.