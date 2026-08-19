# Phase 5 NotebookLM Sanity Check

- Notebook ID: d3071ac8-16ef-4460-8991-7701679974c8
- Notebook title: two-sided-market-balancing-dating
- Source count at query time: 142
- Query: Summarize the state of the field based on all sources in this notebook, focusing on reciprocal scoring, capacity/congestion, allocation, market design, market-health metrics, and interference-aware evaluation. Name sources for claims.
- Conversation ID: 7cb33220-bcf4-4b3f-b884-6c8e5295210a

## Raw NotebookLM response

The modern literature on two-sided marketplaces represents a major paradigm shift: platforms are moving away from traditional "demand-satisfaction" search filters to operate as active, state-dependent **allocation devices** [1, 2]. By integrating machine learning with economic market design, the field is evolving to solve the unique challenges of bidirectional choice, finite human capacity, and competitive spillover effects [3, 4]. 

The state of the field across its core dimensions is synthesized below:

---

### **1. Reciprocal Scoring and Preference Modeling**
Traditional recommender systems optimize for one-sided user utility [5, 6]. In contrast, Reciprocal Recommender Systems (RRS) must satisfy the mutual, bilateral preferences of both sides to establish a match [7, 8].
*   **Architectures:** Early models like *RECON* relied on content-based attribute similarities [9-11], which were later combined with model-based *Collaborative Filtering (CF)* and Matrix Factorization to infer latent preferences from interaction histories [12-14].
*   **Sequence & Multi-Task Modeling:** Recent sequential models, such as those proposed by Zheng et al. (*“Reciprocal Sequential Recommendation”*), track temporal dynamics on both the active (initiating) and passive (responding) sides [15]. Other architectures utilize multi-task learning to simultaneously predict multiple conversion stages (e.g., clicks, applications, and recruiter replies) to manage the selection funnel [16].
*   **Causal Debiasing:** Historical interaction logs are heavily corrupted by position and exposure biases [17, 18]. Yang et al. (*“Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method”*) [19] and Kawamura et al. (*“Counterfactual Reciprocal Recommender Systems for User-to-User Matching”*) [20, 21] address this by modeling recommendations as "treatments" [22, 23], utilizing Inverse Propensity Scoring (IPS) and Self-Normalized IPS (SNIPS) [24, 25] to learn unbiased, true preferences from observational data.

---

### **2. Capacity Constraints and Marketplace Congestion**
Unlike commodity markets, matching platforms operate under strict, finite physical or cognitive capacities—such as a job seeker’s "one worker, one job" limit or a dater's daily messaging queue [8, 26].
*   **The Congestion Trap:** Naive recommender algorithms that rank profiles strictly by predicted match probability systematically concentrate attention on a tiny right-tail of highly popular "superstars" [27-29]. This herding behavior results in massive coordinate failure, inundating desirable users far beyond their reply capacities while average users suffer from a complete lack of recommended exposure [26, 29].
*   **The Screening Cost Paradox:** Arnosti et al. (*“Managing Congestion in Matching Markets”*) prove that as platforms reduce search and application costs, aggregate welfare can actually *decrease* [30]. Low search costs induce users to send too many low-conversion proposals, forcing the receiving side to spend more resources screening unavailable partners [30, 31]. 
*   **Pigouvian Solutions:** To mitigate this, He and Magnac (*“A Pigouvian Approach to Congestion in Matching Markets”*) demonstrate that introducing a low application cost acts as a Pigouvian tax, successfully discouraging marginal proposals to alleviate screening congestion without degrading final match quality [32].

---

### **3. Exposure Allocation and Reranking**
To prevent herding, platforms are utilizing matching-theoretic and optimization-based frameworks to directly govern exposure [4, 33].
*   **Exposure Controls:** In online dating, Sekiya et al. (*“Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach”*) propose *Exposure-Constrained Deferred Acceptance (ECDA)*, which caps receiver exposure in terms of expected inbound likes or expected dates [34], reallocating marginal swiping volume away from congested superstars to the rest of the market [5]. In gig-work, Sekiya et al. (*“Designing Recommendation Exposure and Favorite Lists”*) implement *Thresholded Eligibility Control (TEC)* [35], utilizing state-dependent score-capping to direct recommendations to unfilled, high-demand templates [36, 37].
*   **Centralized Matching and Pricing:** Ashlagi et al. (*“Clearing matching markets efficiently...”*) prove that under additively separable preferences, a *Communication-Efficient Deferred Acceptance (CEDA)* protocol [38] can reach stable matchings with a communication complexity scaling at only \\(O^*(\sqrt{n})\\) per agent [39, 40]. Tomita et al. (*“Fast and Examination-agnostic Reciprocal Recommendation...”*) [41, 42] integrate the Choo-Siow *Transferable Utility (TU)* model [43] to calculate endogenous "matching costs" (shadow prices) [44] that act as prices to clear the market, with Nakada et al. [45, 46] resolving the scalability bottleneck via mini-batch GPU parallelization [43].

---

### **4. Market Design and Information Intervention**
Beyond centralized algorithms, designers use structural constraints to guide decentralized search [47, 48].
*   **Information Disclosure:** Huang et al. (*“Managing Congestion in a Matching Market via Demand Information Disclosure”*) show that disclosing peer demand is highly effective at dispersing traffic, as daters' fear of social rejection naturally diverts them from over-demanded profiles, particularly when presented with explicit capacity-framing cues [29]. Conversely, Escobar and Montes (*“Congestion and Information Design in Matching Markets”*) find that full transparency about overall market seats is suboptimal; showing highly attractive, personalized top choices decreases search costs, whereas disclosing unattractive listings increases herding and aggregate congestion [49, 50].
*   **Restricting Actions:** Kanoria and Saban (*“Facilitating the Search for Partners on Matching Platforms”*) prove that restricting agent actions—such as implementing "one-sided search" (preventing one side from screening) or "directional search" (preventing one side from proposing)—can yield significant welfare improvements, especially in unbalanced markets [48, 51, 52].
*   **Strategic Manipulation:** Economic models must also anticipate strategic gaming of recommendations. Ionescu et al. (*“Strategic Behavior in Two-sided Matching Markets...”*) identify an *adversarial interaction attack* [53], where returning platform participants deliberately perform short-term suboptimal interactions with their matched partners to pollute future training data and manipulate downstream matching priorities [53, 54].

---

### **5. Market-Health and Two-Sided Metrics**
Because intermediate engagement metrics (such as clicks or favorites) often do not align with long-term marketplace health [1, 37], the field has established multi-sided, outcome-based KPIs:
*   **Liquidity & Volume:** Evaluated via *Expected Matches* (sum of mutual match probabilities) [55, 56] and realized *True Positive Pairs* [19, 57].
*   **Congestion-Adjusted Efficiency:** Measured via *Average Effective Dates* (which discounts dates established with highly congested, overloaded receivers) [34] and *Bilateral Stability* (SRecall/SPrecision), which penalizes redundant, low-conversion recommendations [57, 58].
*   **Equality of Exposure:** Tracked using the *Gini Coefficient of Exposure* [24, 25, 59] and *Double Envy* (the count of envious pairs under recommended lists on both sides of the market) [60-63].
*   **Long-Term Participation:** Platforms analyze viewer-side and provider-side population growth under dynamic "population effects" to optimize long-term social welfare rather than myopic engagement [64, 65].

---

### **6. Interference-Aware Experimental Evaluation**
A major challenge in two-sided platforms is that standard A/B testing (user-split RCTs) violates the *Stable Unit Treatment Value Assumption (SUTVA)* [13, 66]. When treated users increase their transaction volume, they deplete the shared pool of available supply, contaminating the control group's outcomes [66, 67]. 
*   **Geographic and Cluster Randomization:** To isolate these spillovers, platforms utilize geographically separated rollouts analyzed via Difference-in-Differences (DID) [68, 69]. Holtz et al. (*“Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization”*) conduct a large-scale meta-experiment on Airbnb, demonstrating empirically that at least **19.76%** of standard individual-level RCT estimates is attributable to marketplace interference bias and is successfully eliminated by clustering competitive search sets [70, 71].
*   **Two-Sided Randomization (TSR):** Johari et al. (*“Experimental Design in Two-Sided Platforms: An Analysis of Bias”*) study designs that independently randomize both sides of the market [72, 73]. They show that naive estimators are highly biased depending on market balance: Customer-Side Randomization (CR) is biased in supply-constrained regimes, while Listing-Side Randomization (LR) is biased in demand-constrained regimes [72, 74]. They propose interpolating estimators (TSRI-k) that leverage cross-group cannibalization patterns to reconstruct the true Global Treatment Effect (GTE) [72, 75].
*   **LP Shadow Price Estimators:** Bright et al. (*“Reducing Marketplace Interference Bias Via Shadow Prices”*) establish that because the platform centrally routes flows via linear programs, the structure of interference is accessible through LP dual variables [76, 77]. They prove that comparing each group's *average shadow price* (the marginal value of an additional unit of supply or demand) corresponds to the correct first-order Taylor approximation of the true global value function, eliminating network-induced bias [76, 78].
*   **Collaborative Randomization:** Nandy et al. propose *UniCoRn* (User-Side Collaborative Randomization), which randomizes user-side assignments while strategically smoothing and controlling producer-side exposure probabilities, eliminating the need to know the marketplace network graph *a priori* [79, 80].

***

📊 I can write a Python simulation in your scratch space to model a two-sided matching market with finite reply capacities. This will let you visualize how a standard A/B test overestimates treatment effects compared to an interference-aware shadow price estimator. Let me know if you would like me to set this up!

