# Phase 4 NotebookLM Query 7 — Market-Health Metrics and Evaluation

**Query:** Across all notebook sources, identify source-backed market-health metrics and interference-aware experimental designs for two-sided dating markets. Cover matches/conversations, wasted likes, distribution/coverage, capacity/congestion, two-sided retention, and causal designs. Name full source titles, reported numeric effects if any, and limitations. Do not infer; use Not specified where absent.

## Response

### **1. Matches and Conversations**

*   **Source Title:** *“Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach - arXiv”* [1]
    *   **Market-Health Metrics:** 
        *   **Average Dates:** Evaluates the expected count of mutual-like dates established on the platform [2, 3].
        *   **Average Effective Dates:** A proposer-side expected match count adjusted to discount matches with congested, overloaded receivers [3-5].
        *   **Dating Probability:** Extensive-margin probability of a user obtaining at least one date [3, 6].
    *   **Reported Numeric Effects:** 
        *   *Synthetic Simulations:* Naive *One-sided (like-sort)* yields 0.2184 average dates and 0.1859 average effective dates [7]. Sorting by *One-sided (date-sort)* increases dates to 0.3543 and effective dates to 0.2317 [7]. Utilizing *ECDA (date-sort, cap=40)* maximizes matches with 0.3372 average dates and 0.2436 average effective dates [7].
        *   *Empirical Simulations:* Optimal *ECDA (date-exposure)* with capacity 1.5 yields an average of 0.150 dates per receiver [8].
        *   *Live Rollout (excluding top 0.1% congested receiver-days):* The treatment × post difference-in-differences (DID) effect is **+0.003 average dates**, **+0.003 average effective dates**, **+0.002 proposer dating probability**, and **+0.005 receiver dating probability** [9].
    *   **Limitations:** The field experiment evaluated only two geographic clusters, meaning conventional large-cluster asymptotics are not available for standard inference [10]. Offline simulations abstract from live equilibrium responses [11].
*   **Source Title:** *“Propose with a rose? Signaling in internet dating markets”* [12]
    *   **Market-Health Metrics:** Total number of initiated dates, and the fraction of participants obtaining at least one initiated date [13].
    *   **Reported Numeric Effects:** Endowing participants with 8 roses (vs. 2 roses) increases the number of initiated dates by **44%** for men (from 0.556 to 0.800) and **86%** for women (from 0.379 to 0.705) [13]. The fraction of women obtaining at least one date increases by **50%** (from 0.218 to 0.328) [13]. Attaching a rose to a proposal increases its acceptance rate by **7.8 percentage points** [14].
    *   **Limitations:** The study cannot measure or prove long-term welfare improvements, as the precise definition of long-term match welfare remains theoretically ambiguous [15].
*   **Source Title:** *“Online Dating Recommendations: Matching Markets and Learning Preferences”* [16]
    *   **Market-Health Metrics:** Rate of successful matches (first contact replies) [16, 17].
    *   **Reported Numeric Effects:** Combining a two-sided market LP optimization with an LDA preference learning model improves successful matches by **up to 45%** (or **48%** depending on the cohort) relative to a suitor-only preference baseline [16, 17].
    *   **Limitations:** Evaluated offline by simulating a dating market using 2 million distinct pairs rather than a live A/B test on active users [17, 18].
*   **Source Title:** *“Prediction and Congestion in Two-Sided Markets: Economist versus Machine Matchmakers - UCR | Department of Economics”* [19]
    *   **Market-Health Metrics:** **Hit Rate** (the probability that at least one member from the recommended list of length N is liked) [20].
    *   **Reported Numeric Effects:** Baseline ML content filtering yields "almost zero" hit rates, while the equilibrium matching approach (CS model) yields a **~35% hit rate** with list length N = 10 [20]. In Gale-Shapley simulations, the CS model accelerates matching by **200%** [21] and matches more than 40% of men in the first round [22].
    *   **Limitations:** Content and collaborative regression coefficients are not reported [23].
*   **Source Title:** *“MODE: Mutual Optimality in Direct Effects of Reciprocal Recommendations in Matching Markets”* [24]
    *   **Market-Health Metrics:** Expected number of matches, and the sum of sub-optimality of direct effects [25, 26].
    *   **Reported Numeric Effects:** In real-world platform simulations, MODE achieves an expected number of matches **substantially larger (>10%)** than that of any other deterministic baseline [27].
    *   **Limitations:** Individual preferences are approximated from offline historical logs using Matrix Factorization rather than true preferences [28].
*   **Source Title:** *“Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method”* [29]
    *   **Market-Health Metrics:** Recall@50, Precision@50, NDCG@50, SRecall@50, SPrecision@50, RNDCG@50, CRecall@50, CPrecision@50, True Positive Pairs [30, 31].
    *   **Reported Numeric Effects:** On the Libimseti dating dataset, the proposed CRRS model achieves: Recall@50 = 0.2172 (A side) / 0.1916 (B side), NDCG@50 = 0.0922 (A side) / 0.0777 (B side) [30], SRecall@50 = 0.1221, SPrecision@50 = 0.0027, RNDCG@50 = 0.0849, CRecall@50 = 0.3387, and True Positive Pairs = 1,743 [31].
    *   **Limitations:** An inherent conflict between coverage and stability exists due to different stances toward redundant recommendations, indicating that trade-offs may be required [32].
*   **Source Title:** *“Balancing Fairness and High Match Rates in Reciprocal Recommender Systems: A Nash Social Welfare Approach - arXiv”* [33]
    *   **Market-Health Metrics:** Expected matches [34, 35].
    *   **Reported Numeric Effects:** Evaluated on real online dating data (Table 3), the match-maximizing SW_LP model yields **111.373 expected matches**, whereas the fairness-aware NSW_LP model yields **90.388 expected matches** [35].
    *   **Limitations:** Evaluated on a sampled subset of 200 × 200 users; validating on large-scale datasets with millions of active users remains an important next step [36, 37].
*   **Source Title:** *“Search, Selectivity, and Market Thickness in Two-Sided Markets”* [38]
    *   **Market-Health Metrics:** Number of matches [38, 39], average match quality [38, 39], and the likelihood of finding a date [39].
    *   **Reported Numeric Effects:** In calibrated small-market (M=4,000) simulations:
        *   Increasing both men and women by 25% (market thickness) reduces the number of matches by **-12.2% for men and -17.7% for women** [40], while match quality drops by **-3.6%** for women [40]. The likelihood of finding a date decreases by **-12.0% (Men) and -17.5% (Women)** [40].
        *   Doubling the like limit under this expansion reverses this, increasing matches by **+136.3% (Men) and +121.6% (Women)** [40].
        *   Selective targeting ("gender gating") by increasing women by 25% decreases female matches by **-17.2%** [40].
    *   **Limitations:** The platform cannot observe when matches convert to real-world offline dates or marriages [41]. The model does not capture dynamic learning of quality distributions [42].

---

### **2. Wasted Likes**

*   **Source Title:** *“Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach - arXiv”* [1]
    *   **Market-Health Metrics:** Average likes [3, 43], expected likes [44], and received likes [45].
    *   **Reported Numeric Effects:** Naive *One-sided (like-sort)* yields an average of **4.182 likes** [7]. Utilizing *ECDA with like exposure* (cap=22.0) compresses this expected flow to an average of **3.308 likes per receiver**, mitigating wasted swipes at the congested right tail [8]. Utilizing *ECDA with date exposure* (cap=1.5) yields **3.658 average likes** [46]. In the field experiment (excluding top 0.1% receiver-days), the treatment significantly increases average likes on the receiver side by **+0.334** [9].
    *   **Limitations:** Same as above.
*   **Source Title:** *“Propose with a rose? Signaling in internet dating markets”* [12]
    *   **Market-Health Metrics:** Rose waste rate [47].
    *   **Reported Numeric Effects:** Senders exhibited strategic inefficiency: **approximately 30% of roses were wasted** on top-tier recipients who did not respond [47].
    *   **Limitations:** Same as above.

---

### **3. Distribution and Coverage**

*   **Source Title:** *“Counterfactual Reciprocal Recommender Systems for User-to-User Matching - arXiv”* [48, 49]
    *   **Market-Health Metrics:** Long-tail user coverage [50, 51].
    *   **Reported Numeric Effects:** CFRR-SNIPS increases long-tail user coverage by **51%** (raising it from 0.504 to 0.763 in synthetic tests) [50, 51].
    *   **Limitations:** Generalizing this effect from synthetic to real-world platforms requires careful validation on a case-by-case basis [50, 51].
*   **Source Title:** *“Balancing Fairness and High Match Rates in Reciprocal Recommender Systems: A Nash Social Welfare Approach - arXiv”* [33]
    *   **Market-Health Metrics:** Gini index of expected matches, number of envious pairs (Left Envy / Right Envy) [34, 35, 52].
    *   **Reported Numeric Effects:** In real dating platform evaluations (Table 3):
        *   *Naive:* Gini (Men) = **0.5748**, Gini (Women) = **0.6044**, Envy (Men) = **1495**, Envy (Women) = **3016** [35].
        *   *Prod (Reciprocal Baseline):* Gini (Men) = **0.5480**, Gini (Women) = **0.6231**, Envy (Men) = **765**, Envy (Women) = **608** [35].
        *   *SW_LP (Match Maximizing):* Gini (Men) = **0.5177**, Gini (Women) = **0.5974**, Envy (Men) = **434**, Envy (Women) = **331** [35].
        *   *NSW_LP (Fairness-Aware):* Gini (Men) = **0.3807**, Gini (Women) = **0.4770**, Envy (Men) = **31**, Envy (Women) = **14** [35].
    *   **Limitations:** LP-based and Sinkhorn-based optimization methods face severe computational scalability bottlenecks on large instances [37].
*   **Source Title:** *“Prediction and Congestion in Two-Sided Markets: Economist versus Machine Matchmakers - UCR | Department of Economics”* [19]
    *   **Market-Health Metrics:** Coverage rate of recommendation (ratio of distinct recommended women to total recommendations) [53].
    *   **Reported Numeric Effects:** `Not specified`. (Fusing the CS model with OLS or MF collaborative filtering is shown to increase coverage rate, but exact numeric effects are `Not specified` in the text).
    *   **Limitations:** Same as above.

---

### **4. Capacity and Congestion**

*   **Source Title:** *“Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach - arXiv”* [1]
    *   **Market-Health Metrics:** Average effective dates [3, 4] and receiver-side congestion [44, 54].
    *   **Reported Numeric Effects:**
        *   *Synthetic Market:* Naive *One-sided (like-sort)* yields 0.1859 average effective dates [7]. Introducing *ECDA (date-sort, cap=40)* raises this to **0.2436** by capping receiver exposure to expected dates [7, 55].
        *   *Real Rollout:* Trimming the top **0.1%** of receiver-day observations (which concentrate early-stage likes but exhibit exceptionally poor pass-through to messages—roughly **one-third (1/3)** the message-to-date conversion rate of other users [54, 56]) shows a statistically significant treatment DID effect of **+0.003 average effective dates** for the remaining 99.9% of users [9].
    *   **Limitations:** Same as above.
*   **Source Title:** *“A Pigouvian Approach to Congestion in Matching Markets | IZA@LISER Network”* [57]
    *   **Market-Health Metrics:** Costly screening congestion, application costs as a Pigouvian tax [57].
    *   **Reported Numeric Effects:** `Not specified` (Low application cost effectively reduces congestion without harming match quality, but exact numeric effects are `Not specified in source`).
    *   **Limitations:** `Not specified in source`.
*   **Source Title:** *“Managing Congestion in a Matching Market via Demand Information Disclosure”* [58]
    *   **Market-Health Metrics:** Peer demand disclosure, textual message-framing cues [59].
    *   **Reported Numeric Effects:** `Not specified`. (Information disclosure presented with textual framing is reported to improve matching efficiency by shifting users away from over-demanded popular peers, but exact numeric effects are `Not specified in source`).
    *   **Limitations:** `Not specified in source`.

---

### **5. Two-Sided Retention**

*   **Source Title:** *“Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach - arXiv”* [1]
    *   **Market-Health Metrics:** Extensive-margin dating probability as a key driver of user satisfaction and retention [6].
    *   **Reported Numeric Effects:** `Not specified` in numbers (reported as a qualitative KPI where receiving at least one date dramatically reduces churn, but exact numeric effects on user retention are `Not specified in source`).
    *   **Limitations:** Same as above.
*   **Source Title:** *“[2602.15752] Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching - arXiv”* [60]
    *   **Market-Health Metrics:** Retention-optimized matching [Title].
    *   **Reported Numeric Effects:** `Not specified in source`.
    *   **Limitations:** `Not specified in source`.

---

### **6. Causal / Experimental Designs (Interference-Aware)**

*   **Source Title:** *“Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach - arXiv”* [1]
    *   **Design:** **Geographic rollout** combined with a difference-in-differences (DID) design [61]. Standard user-split randomization violates SUTVA because changes in recommendations alter local search pools and like flows, contaminating the control group's matches [62]. The Kanto region was treated with ECDA (date exposure limit of 1.5), and the Kansai-Tokai region was the control [61, 63].
    *   **Reported Numeric Effects:** The expected outcome measures move significantly as designed [64]. For the 99.9% non-congested cohort, the treatment × post effect is **+0.003 average effective dates** and **+0.334 average likes** [9].
    *   **Limitations:** Because only two geographic clusters were randomized, conventional large-cluster asymptotics are not available; standard errors primarily serve as suggestive [10].
*   **Source Title:** *“Designing Recommendation Exposure and Favorite Lists: A Field Experiment in a Spot-Work Platform”* [65] *(Note: Although focused on spot-work, the source explicitly maps its design and spillovers directly to online dating platforms [66-68]).*
    *   **Design:** **Prefecture-level randomized rollout** analyzed with difference-in-differences (DID) style regressions [69]. Prefecture-level rollout was chosen instead of user-level randomization to limit within-market contamination, as treated users redirect favorites and applications, changing the stock of opportunities available to control users [68]. Aomori served as the treatment prefecture (under Thresholded Eligibility Control - TEC), and Iwate served as the geographically proximate control region [69].
    *   **Reported Numeric Effects:** Rolling out TEC does not statistically change overall favorites (treatment × post DID coefficient is -40.458) [70], but yields a statistically significant increase of **+9.045 matches per prefecture-day** [70].
    *   **Limitations:** Baseline match counts are omitted due to corporate confidentiality [70]. Also, prefecture-level rollout reduces but does not completely eliminate cross-prefecture spillovers [68].
*   **Source Title:** *“Reducing Marketplace Interference Bias Via Shadow Prices”* [71]
    *   **Design:** Standard RCT analyzed with a **Shadow Price (SP) Estimator** [72]. Rather than measuring total value accrued, it compares the average shadow price (dual variables associated with constraints in the matching linear program) between treatment and control groups to evaluate treatment effects [72].
    *   **Reported Numeric Effects:** In simulated supply chain and NYC ride-hailing environments, standard RCT estimators systematically **overestimate the treatment effect by more than a factor of two** under high contention [73], whereas the SP estimator successfully eliminates nearly all network-induced interference bias [73].
    *   **Limitations:** Explicitly restricted to centralized "generalized matching platforms" where the platform centrally routes supply to demand via a network flow LP [72, 74] and cannot easily be applied to decentralized customer-choice platforms like online dating apps [75].
*   **Source Title:** *“Experimental Design in Two-Sided Platforms: An Analysis of Bias”* [76]
    *   **Design:** **Two-Sided Randomization (TSR)** where both customers and listings are randomized independently, and treatment is only active when a treated customer views a treated listing [77, 78]. CR is unbiased in demand-constrained markets, and LR is unbiased in supply-constrained markets [77].
    *   **Reported Numeric Effects:** `Not specified` (evaluates mathematical bias equations and qualitative balance sweeps).
    *   **Limitations:** Dynamic mean-field limit model assumes short-lived customers and long-lived listings, abstracting from complex network structures [79, 80].
*   **Source Title:** *“Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization: Evidence from a Pricing Meta-experiment on Airbnb”* [81]
    *   **Design:** **Cluster Randomization** Meta-experiment [82]. 25% of clusters were assigned to individual-level randomization (naive), and 75% were cluster-randomized [83].
    *   **Reported Numeric Effects:** Individual randomization suggests a loss of 0.345 bookings per listing [83]. **At least 20%** (specifically **19.76%** [83]) of this individual-level estimate is attributable to interference bias and is eliminated through cluster randomization [82, 83]. In supply-constrained geographies, **12.05%** of the bias is eliminated, whereas in demand-constrained geographies, **28.65%** is eliminated [84].
    *   **Limitations:** Cluster randomization substantially reduces statistical power [85]; theoretical guarantees only hold for treatments that uniformly shift demand [85].

***

📊 Since these matching-market and causal design frameworks rely heavily on balancing supply and demand under SUTVA constraints, I can write a Python script in your sandbox to simulate a basic two-sided market under varying capacities. This will let you visualize how a standard A/B test overestimates treatment effects compared to an interference-aware shadow price estimator. Let me know if you would like me to set this up!

