# Phase 4 NotebookLM Query 6 — Mechanisms for Wasted Likes and Congestion

**Query:** For the project problem of wasted likes and overloaded-user congestion in a dating-app matching market, which reciprocal-scoring, capacity-aware allocation, constrained reranking, and market-design mechanisms in the notebook directly reduce wasted proposals or overloaded-recipient congestion while preserving match quality? For every mechanism, name the full source title and give only quantitative evidence actually reported by that source, plus the evidence limitation. Do not infer beyond sources; write Not specified where a source provides no quantitative effect.

## Response

### **1. Exposure-Constrained Deferred Acceptance (ECDA)**
*   **Full Source Title:** *“Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach - arXiv”* [1]
*   **Mechanism Description:** ECDA maps predicted login, like, and relike probabilities into recommendations under proposer cognitive capacity constraints while capping receiver-side exposure in terms of expected likes or expected dates, rather than headcount [2, 3]. It uses "sorting by dating rates" (where both sides' rank-order lists are sorted by expected dating probability \\(\delta_{ij} = \lambda_i \alpha_{ij} \lambda_j \beta_{ij}\\)) to align preferences, admitting a fast greedy implementation [4-6]. 
*   **Dating-App Quantitative Evidence:**
    *   **Synthetic Market Simulation [7]:** Capping receiver capacity (using dating rate sorting) dramatically improves expected matches and effective matches (a congestion-adjusted metric) while reducing overall proposal volume (likes sent) [7, 8]. Naive sorting by like rates (*One-sided (like-sort)*) yields **4.182 average likes** and **0.1859 average effective dates** [7]. Moving to *One-sided (date-sort)* reduces proposals to **3.531 likes** while increasing expected dates to **0.3543** and effective dates to **0.2317** [7, 9]. Applying DA with *date-sort* and capacity \\(q_j = 40\\) yields **3.675 average likes**, **0.3372 average dates**, and **0.2436 average effective dates** [7].
    *   **Empirical Market Simulation (CoupLink Logs) [10]:** Reallocating exposure away from the congested right-tail of receivers using ECDA yields the following [10, 11]:
        *   *One-sided (like-sort):* Avg Dates = **0.0401**, Avg Effective Dates = **0.0241**, Proposer Dating Prob = **0.0288**, Receiver Dating Prob = **0.0344**, Avg Likes = **5.384** [10].
        *   *One-sided (date-sort):* Avg Dates = **0.1231**, Avg Effective Dates = **0.0579**, Proposer Dating Prob = **0.0508**, Receiver Dating Prob = **0.0857**, Avg Likes = **3.693** [10].
        *   *DA (date-sort, cap=140):* Avg Dates = **0.1033**, Avg Effective Dates = **0.0605**, Proposer Dating Prob = **0.0424**, Receiver Dating Prob = **0.0904**, Avg Likes = **3.610** [10].
        *   *ECDA (like-exposure, cap=22.0):* Avg Dates = **0.1054**, Avg Effective Dates = **0.0603**, Proposer Dating Prob = **0.0424**, Receiver Dating Prob = **0.0912**, Avg Likes = **3.308** (achieving the lowest proposal rate, reducing wasted likes) [10].
        *   *ECDA (date-exposure, cap=1.5):* Avg Dates = **0.0928**, Avg Effective Dates = **0.0623** (maximizing expected match quality), Proposer Dating Prob = **0.0401**, Receiver Dating Prob = **0.0932**, Avg Likes = **3.658** [10].
    *   **Large-Scale Regional Field Experiment [12, 13]:** Running ECDA with date exposure cap=1.5 reallocated recommendations away from the top 0.1% of congested receivers (who showed high early responsiveness but very poor pass-through to messaging, with message exchange conditional on date formation being roughly **one-third (1/3)** of that for other receivers) [14, 15]. The rollout successfully improved early-stage match formation for the remaining 99.9% of users without degrading post-engagement messaging quality [13, 16, 17].
*   **Evidence Limitation:**
    *   The offline simulations rely on estimated preferences and static, predicted behaviors, abstracting from live equilibrium responses [18].
    *   In the field experiment, the algorithm did not materially change or improve post-engagement messaging, meaning separate design interventions are required to boost substantive post-match communication [13, 17].

---

### **2. Equilibrium Matching Recommenders via Transferable Utility (TU)**
*   **Full Source Title:** *“Prediction and Congestion in Two-Sided Markets: Economist versus Machine Matchmakers - UCR | Department of Economics”* [19]
*   **Mechanism Description:** Fuses machine learning preference scoring (OLS content filtering or Matrix Factorization collaborative filtering) with an economic Transferable Utility (TU) matching model à la Choo and Siow (2006) on a localized "pseudo-market" [20, 21]. The model generates an endogenous "matching cost" (acting as a shadow price) that penalizes over-demanded "superstar" profiles to discourage users from pursuing congested partners where matching probabilities are slim [22, 23].
*   **Dating-App Quantitative Evidence:**
    *   **Hit Rate:** While standard content filtering has an almost zero hit rate, the equilibrium matching recommender achieves a **hit rate of ~35%** when recommending 10 users [24].
    *   **Congestion & Matching Speed:** In simulated Gale-Shapley iterations, the equilibrium matching recommender **reduces the number of rounds required to clear the market by 50%** relative to baseline ML recommenders [25]. It takes **~10 rounds for MF+CS** and **~15 rounds for OLS+CS** to clear 95% of the men in the market, whereas the baseline recommenders exhibit flat matching curves due to clustered recommendations [26]. Counterfactual simulations show the matching process is accelerated by **200%** [27].
*   **Evidence Limitation:** 
    *   The performance gains are evaluated through stylized Gale-Shapley simulation models and counterfactual evaluations, rather than a live online dating platform rollout [28].
    *   The model assumes an ideal competitive equilibrium with transferable utility, whereas actual online dating users do not easily exchange transfers [29].

---

### **3. Alternating Nash Social Welfare (NSW) Maximization**
*   **Full Source Title:** *“Balancing Fairness and High Match Rates in Reciprocal Recommender Systems: A Nash Social Welfare Approach - arXiv”* [30]
*   **Mechanism Description:** Adopts the economic fairness concept of envy-freeness from fair division theory [31, 32]. It employs the Frank-Wolfe and Sinkhorn-based algorithms to alternately maximize two Nash Social Welfare functions, preventing the extreme concentration of recommendation opportunities on popular users to alleviate marketplace congestion [33, 34].
*   **Dating-App Quantitative Evidence:**
    *   **Empirical Japanese Dating Dataset (Table 3, log-examination) [35]:** 
        *   *Naive:* Expected Matches = **60.08**, Men Envy = **1495**, Women Envy = **3016**, Men Gini = **0.575**, Women Gini = **0.604** [35].
        *   *Prod (Reciprocal Baseline):* Expected Matches = **106.00**, Men Envy = **765**, Women Envy = **608**, Men Gini = **0.548**, Women Gini = **0.623** [35].
        *   *SW_LP (Match-Maximizing):* Expected Matches = **111.37**, Men Envy = **434**, Women Envy = **331**, Men Gini = **0.518**, Women Gini = **0.597** [35].
        *   *NSW_LP (Proposed):* Expected Matches = **90.39** (preserving competitive match volume), while Men Envy drops to **31** and Women Envy to **14** (nearly eliminating congestion), and Gini indices fall to **0.381** (Men) and **0.477** (Women) [35, 36].
*   **Evidence Limitation:** 
    *   The empirical verification on real-world dating data is limited to a small sample of 200 men and 200 women [37, 38].
    *   The model assumes static, pre-estimated preference probabilities, abstracting from the dynamic incremental updates that occur as live user interactions unfold [39].

---

### **4. Flow-Controlled Probabilistic Two-Sided Matching (Baihe LP)**
*   **Full Source Title:** *“Online Dating Recommendations: Matching Markets and Learning Preferences”* [40]
*   **Mechanism Description:** Formulates matching as a probabilistic two-sided market LP that maximizes overall message replies subject to suitor capacity \\(CS(s)\\) (sending limits) and receiver capacity \\(CR(r)\\) (expected inbound caps) to act as a flow control mechanism that prevents popular receivers from being inundated with messages [41-44].
*   **Dating-App Quantitative Evidence:**
    *   Tested on logs of 2 million distinct pairs from Baihe [45]. Fusing the learned LDA preference model with the two-sided capacity optimization increases the rate of successful matches (first contact replies) by **up to 45%** (or **48%** depending on the cohort) relative to a suitor-preference-only baseline [40, 45].
*   **Evidence Limitation:**
    *   The results are based on an offline simulation test where the researchers eliminated half of the recorded messages in the dataset and checked if the algorithm could select the messages with higher actual reply rates [46, 47], rather than a live A/B test on active users.

---

### **5. Preference Signaling Mechanisms (“Roses” / “Flowers”)**
*   **Full Source Title:** *“Propose with a rose? Signaling in internet dating markets”* [48]
*   **Mechanism Description:** Restricts congestion and coordination failures by introducing a scarce preference signaling device (“roses” or “flowers”) that users can attach to a limited number of proposals to signal genuine, high-strength interest [49].
*   **Dating-App Quantitative Evidence:**
    *   In a randomized field experiment, attaching a rose makes a recipient **7.8 percentage points more likely to accept a proposal** [50].
    *   Providing a higher endowment of signals (8 roses vs. 2 roses) significantly increases dating outcomes without crowding out non-signaled offers [49, 51]:
        *   *For Men (Seoul cohort):* The fraction of men obtaining at least one initiated date increases by **45%** (from 0.313 to 0.452), and the total number of initiated dates increases by **48%** (from 0.556 to 0.833) [52].
        *   *For Women:* The fraction of women obtaining at least one initiated date increases by **50%** (from 0.218 to 0.328), and the total number of dates increases by **86%** (from 0.379 to 0.705) [52, 53].
*   **Evidence Limitation:**
    *   Users exhibit high strategic inefficiency: **approximately 30% of roses were wasted** on top-tier recipients who did not respond, and a substantial fraction of users failed to fully utilize their roses [49, 54].
    *   The empirical study cannot measure or prove long-term welfare improvements, as the precise definition of long-term match welfare remains theoretically ambiguous [55, 56].

---

### **6. Dynamic Like-Limit Control**
*   **Full Source Title:** *“Search, Selectivity, and Market Thickness in Two-Sided Markets”* [57]
*   **Mechanism Description:** Uses a capped proposal budget (like limit \\(\bar{L}\\)) to influence strategic user selectivity [58, 59]. When market thickness increases, users mechanically become over-selective (focusing likes on unachievable, popular partners). Doubling the like limit makes users less selective, spreading out likes and expanding matches [58, 60].
*   **Dating-App Quantitative Evidence:**
    *   In structural simulations calibrated via an information-intervention field experiment [61, 62]:
        *   *Market Expansion (Small Market):* Increasing platform size by 25% under standard limits decreases matches by **-12.2%** (Men) and **-17.7%** (Women) [63]. Doubling the like limit reverses this, causing matches to surge by **+136.3%** (Men) and **+121.6%** (Women) [63].
        *   *Market Expansion (Large Market):* Increasing platform size by 25% under standard limits yields flat matches (**+0.4%** for Men, **-5.9%** for Women) [64]. Doubling the like limit drives matches up by **+205.7%** (Men) and **+186.6%** (Women) [64].
        *   *Gender Gating (Small Market):* Restricting male entry while growing female users by 25% drops female matches by **-17.2%** [63]. Capping men but doubling the like limit for women only converts this into a **+20.1%** increase in female matches and a **+60.1%** increase in male matches [63].
*   **Evidence Limitation:**
    *   The dating app platform cannot observe when matches translate into real-world offline dates or marriages [65].
    *   The counterfactual outcomes are simulated from a game-theoretic structural search model, which may admit multiple equilibria of which the estimated path is only one possibility [66].

***

📊 I can write a Python simulation script in your sandbox to model a basic bipartite matching market and calculate how varying the like limit or introducing an ECDA-style date exposure cap dynamically alters the Gini coefficient of exposure. Let me know if you would like to run this!

