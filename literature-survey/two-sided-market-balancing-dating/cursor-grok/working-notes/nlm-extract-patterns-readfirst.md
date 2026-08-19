### **Design Patterns for Two-Sided Market Balancing in Dating-App Recommendation**

#### **1. Bilateral Preference Aggregation via Harmonic Mean**
*   **The Lever:** Fuses individual sender-to-recipient and recipient-to-sender compatibility scores using a harmonic mean to penalize extreme interest mismatch and ensure mutual preference alignment [1, 2].
*   **Strongest Source:** *"Recommending people to people: the nature of reciprocal recommenders with a case study in online dating"* (Luiz Pizzato, Tomek Rej, Joshua Akehurst, Irena Koprinska, Kalina Yacef, Judy Kay, 2013) [3].
*   **Modeling Layer:** `reciprocal scoring` [1].

#### **2. Transferable Utility (TU) Matching Framework (Choo-Siow Model)**
*   **The Lever:** Formulates mutual recommendations as a competitive market-clearing problem where implicit shadow prices (matching costs) adjust dynamically to penalize swiping requests directed at highly popular "superstars," naturally distributing exposure [4, 5].
*   **Strongest Source:** *"Fast and examination-agnostic reciprocal recommendation in matching markets"* (Yoji Tomita, Riku Togashi, Yuriko Hashizume, Naoto Ohsaka, 2023) [6].
*   **Modeling Layer:** `capacity-aware scoring` [4].

#### **3. Exposure-Constrained Deferred Acceptance (ECDA)**
*   **The Lever:** Restricts the aggregate expected likes or expected dates a receiver can experience rather than raw profile display headcounts, using a parallelizable greedy implementation to enforce the exposure constraints [7-9].
*   **Strongest Source:** *"Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach"* (Kazuki Sekiya, Suguru Otani, Yuki Komatsu, Sachio Ohkawa, Shunya Noda, 2026) [10].
*   **Modeling Layer:** `constrained re-ranking` [7, 8].

#### **4. Alternating Nash Social Welfare (NSW) Maximization**
*   **The Lever:** Guarantees individual-level exposure fairness (envy-freeness) across the platform by optimizing an objective function defined as the product of all users' expected match utilities [11-13].
*   **Strongest Source:** *"Balancing Fairness and High Match Rates in Reciprocal Recommender Systems: A Nash Social Welfare Approach"* (Yoji Tomita, Tomohiko Yokoyama, 2026) [14, 15].
*   **Modeling Layer:** `constrained re-ranking` [13].

#### **5. Strategic Peer Demand Information Disclosure**
*   **The Lever:** Injects transparency into the user messaging flow by displaying recent incoming message volumes (demand) on popular profiles, combined with textual capacity-warning cues, to deter congested likes and steer attention to under-served peers [16].
*   **Strongest Source:** *"Managing Congestion in a Matching Market via Demand Information Disclosure"* (Ni Huang, Gordon Burtch, Pei-yu Chen, Ao Huang, 2025) [17].
*   **Modeling Layer:** `market-design lever` [16].

#### **6. Curated One-Directional Interaction Sequence Design**
*   **The Lever:** Controls the sequencing of two-sided evaluations by allowing only one side of the market (e.g., women) to initiate interactions, which cuts search backlogs and enhances match efficiency [18-20].
*   **Strongest Source:** *"Platform Design in Curated Dating Markets"* (Ignacio Rios, Daniela Saban, Fanyin Zheng, 2023) [18, 21].
*   **Modeling Layer:** `market-design lever` [22].

#### **7. Effective Dates (Congestion-Adjusted Utility Metric)**
*   **The Lever:** Measures platform matching efficiency by discounting predicted matches that involve overloaded receivers, accounting for downstream message pass-through drops [7, 23, 24].
*   **Strongest Source:** *"Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach"* (Kazuki Sekiya, Suguru Otani, Yuki Komatsu, Sachio Ohkawa, Shunya Noda, 2026) [10].
*   **Modeling Layer:** `ecosystem metrics` [7].

#### **8. Off-Policy Evaluation with Intermediate First-Stage Rewards (DiPS / DPR)**
*   **The Lever:** Evaluates new matching policies offline without risky, live A/B testing by applying importance weighting to first-stage actions (likes) combined with model-based imputation for second-stage matches [25, 26].
*   **Strongest Source:** *"Off-Policy Evaluation and Learning for Matching Markets"* (Anonymous, 2025) [27, 28].
*   **Modeling Layer:** `evaluation method` [27].

---

### **Source Ranking for a Dating-App Ranking Team**

This ranking is tailored for a team solving **superstar congestion, wasted surplus likes, under-matched average users, and mutual churn**.

#### **1. "Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach"** 
*   *Why:* **Essential for the core problem.** It proves that naive scoring concentrates exposure on highly responsive "superstar" users [10, 29, 30]. It provides a concrete production-grade solution (**ECDA**) that constrains the expected likes or dates a user receives [7, 8]. It also models the exact downstream funnel (displays \\(\rightarrow\\) likes \\(\rightarrow\\) relikes) to prove that superstar users have a low pass-through rate to actual communication, meaning excess likes are completely wasted [24, 31, 32].

#### **2. "Balancing Fairness and High Match Rates in Reciprocal Recommender Systems: A Nash Social Welfare Approach"**
*   *Why:* **Directly addresses user churn.** It models recommendation opportunities as a scarce resource to be divided fairly [33]. It shows that pure match maximization leads to extreme envy among average users (who get zero exposure), driving churn [34, 35]. By implementing **Nash Social Welfare (NSW)** optimization, it shows how to minimize user envy to near zero while retaining highly competitive overall match throughput [13, 36].

#### **3. "Fast and examination-agnostic reciprocal recommendation in matching markets"**
*   *Why:* **Provides a highly scalable system architecture.** It maps economic stable matching (the Choo-Siow transferable utility model) to recommendations to penalize matches with over-demanded superstar profiles using an endogenous "matching cost" [4, 5]. Crucially, it reformulates this into a **\\((2d+2)\\)-dimensional vector space**, allowing the system to balance the marketplace in real time using fast, sublinear Maximum Inner Product Search (MIPS) [37-39].

#### **4. "Managing Congestion in a Matching Market via Demand Information Disclosure"**
*   *Why:* **Best for low-engineering, high-impact behavioral intervention.** This paper demonstrates that displaying a profile's recent incoming message volume, paired with capacity framing (e.g., warning that the user is busy), deters users from sending wasted likes to superstars [16]. It leverages the "fear of social rejection" to naturally steer swiping attention toward under-exposed, highly compatible users, boosting matching efficiency without needing complex model retraining [16].

#### **5. "Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method"**
*   *Why:* **Unlocks correct offline measurement.** It shows that traditional top-K metrics ignore bilateral recommendation redundancy (e.g., showing Bob to Alice and Alice to Bob simultaneously, which wastes slots and yields zero additional matches) [40-42]. It introduces **Coverage-adjusted Recall/Precision** and a **vacant-slots reranking strategy** to optimize the overall coverage of unique matched couples rather than duplicate exposures [42-44].

#### **6. "Platform Design in Curated Dating Markets"**
*   *Why:* **Optimizes curation and user retention.** It studies how platforms should select and display daily profile assortments (backlogs) [18, 21]. It proves that curated, one-directional sequences (where one side moves first and the other only responds to existing likes) can capture at least 50% of the matches of a two-directional design while drastically reducing same-side competition and superstar congestion [18, 20, 22].

#### **7. "Search, Selectivity, and Market Thickness in Two-Sided Markets"**
*   *Why:* **Crucial for platform size strategy.** It proves that simply growing the platform's user base counterintuitively *decreases* matches (e.g., a 25% member increase led to 12% fewer matches for men and 17% for women in small markets) because users become overly selective [45, 46]. It shows that the platform can mitigate this by adjusting and **imposing strict daily like limits** to control selectivity and restore optimal matching equilibria [47, 48].

#### **8. "Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching"**
*   *Why:* **Focuses on the ultimate business metric—retention.** It argues that raw match maximization and axiomatic fairness are incomplete goals that leave user retention to luck [49]. It introduces **MRet (Matching for Retention)**, which learns personalized user retention curves from profiles and interaction histories to dynamically prioritize recommendations where they yield the highest retention gain, preventing churn [50].

#### **9. "Your Looks and Your Inbox"**
*   *Why:* **Empirical baseline on human swiping bias.** It utilizes OkCupid's massive dataset to show the natural asymmetry in swiping: men send 2/3 of their likes to the top 1/3 of women, creating severe congestion and low response rates, while women rate 80% of men as below average [51]. This provides the quantitative baseline for understanding the organic attraction skews your algorithms must fight.

#### **10. "Recommending people to people: the nature of reciprocal recommenders with a case study in online dating"**
*   *Why:* **Foundational baseline for reciprocal preferences.** It introduces the **RECON** algorithm and explains why traditional collaborative filtering fails in reciprocal domains due to the high psychological cost of rejection [3, 52, 53]. It models negative preference vectors to filter out profiles highly likely to reject the sender, protecting users from rejection fatigue and churn [1, 53].

***

🎨 I can generate a conceptual diagram or architecture layout for the ECDA (Exposure-Constrained Deferred Acceptance) pipeline to show your engineering team how to implement the daily batch-to-online scoring layers.