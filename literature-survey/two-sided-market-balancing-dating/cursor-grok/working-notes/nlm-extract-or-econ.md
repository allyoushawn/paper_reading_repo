### **1. Rios-Saban-Zheng Assortment Dating**
*   **(1) Bibliography:** *Platform Design in Curated Dating Markets*, Anonymous (Rios, Saban, Zheng), 2023, manuscript submitted to *Manufacturing & Service Operations Management* [1-3].
*   **(2) What they did:** Studied how curated dating platforms should select and display subsets of profiles to users in each period to maximize matches under varying interaction sequences (one- vs. two-directional) and timing constraints (sequential vs. non-sequential) [1, 4, 5].
*   **(3) Two-sided balancing mechanism:** Developed the **Dating Heuristic (DH)**, which solves a mixed-integer program with a one-period lookahead to select optimal profile assortments that balance backlog size and selectivity across both sides [6-8].
*   **(4) Metrics & Effects:** Proved that DH robustly guarantees a \\(1 - 1/e\\) (approx. 63.2%) approximation of the optimal dynamic program across all designs [2, 7]. Using Houston, TX dating data (173 women, 113 men), they showed that a one-directional design with women initiating yields at least 50% of the matches of a two-directional design [8-10].
*   **(5) Dating-app fit:** **High**. The algorithm was designed and validated using empirical data from an active, major US online dating app [3, 9].
*   **(6) Confidence:** **High**.

---

### **2. Ashlagi Assortment Planning**
*   **(1) Bibliography:** *Assortment planning for two-sided sequential matching markets*, Itai Ashlagi, Anilesh K. Krishnaswamy, Rahul Makhijani, Daniela Saban, Kirankumar Shiragur, 2022, *Operations Research* [11-13].
*   **(2) What they did:** Formulated the two-sided sequential assortment problem where the platform presents recommended menus of suppliers to customers (who choose via MNL), and suppliers sequentially match with at most one applicant [11, 14, 15].
*   **(3) Two-sided balancing mechanism:** Utilizes **two-dimensional bucketing** (grouping similar suppliers) and an LP-based rounding algorithm to construct menus that bound the number of times a supplier is displayed, minimizing applicant collisions [16-18].
*   **(4) Metrics & Effects:** Proved the sequential assortment problem is strongly NP-hard [16, 19]. Developed a polynomial-time algorithm that guarantees a constant-factor approximation, consistently achieving at least 1/3 of the linear relaxation upper bound in simulated trials [16, 19-21].
*   **(5) Dating-app fit:** **High/Medium**. Although framed around general platforms (like Airbnb), its core approach of grouping and limiting candidate exposures based on desirability and outside-option scores is highly relevant to dating app queuing [11, 17, 22].
*   **(6) Confidence:** **High**.

---

### **3. Kanoria-Saban Which Side Searches**
*   **(1) Bibliography:** *Facilitating the search for partners on matching platforms: Restricting agent actions*, Yash Kanoria, Daniela Saban, 2017, Working Paper (later published in *Management Science* 2021) [23-25].
*   **(2) What they did:** Evaluated how dynamic matching platforms can mitigate wasteful, costly search and screening behavior by strategically restricting what agents can see or do [23, 26, 27].
*   **(3) Two-sided balancing mechanism:** **Directional search restrictions**. In asymmetric markets, the platform blocks the less selective (or long) side of the market from initiating proposals, forcing the pickier (short) side to propose first [26, 28, 29].
*   **(4) Metrics & Effects:** Under market imbalance (workers arriving \\(\lambda \ge 1.25\\) times faster than employers), workers propose in all unregulated equilibria, driving down their selectivity and welfare [29-31]. Blocking workers from proposing allows them to be highly selective when receiving proposals, boosting worker welfare significantly with a negligible welfare cost to employers [29, 32-34]. 
*   **(5) Dating-app fit:** **High**. Explicitly models dating dynamics and highlights how platforms like Bumble (forcing women to reach out first) reduce congestion and increase matching efficiency [35, 36].
*   **(6) Confidence:** **High**.

---

### **4. Arnosti Congestion Matching Markets**
*   **(1) Bibliography:** *Managing Congestion in Matching Markets*, Nick Arnosti, Ramesh Johari, Yash Kanoria, 2017 (working paper) [37-39].
*   **(2) What they did:** Analyzed decentralized matching markets with dynamic arrivals to show how lowering search and application costs causes severe screening congestion, leaving employers unable to identify available candidates and driving their welfare to zero [37, 40, 41].
*   **(3) Two-sided balancing mechanism:** Enforcing **application limits** (restricting applicant visibility) or raising application costs to decrease applicant search intensity and prevent the "tragedy of the commons" [42-45].
*   **(4) Metrics & Effects:** When screening costs \\(c'_s > f(r, c'_a)\\), employer welfare drops to zero [46, 47]. Enforcing a calculated application limit \\(\ell\\) can raise employer welfare back to the constrained efficient benchmark (\\(\Pi^{opt}_e\\)) and achieve Pareto improvements where both sides capture at least 3/4 of their optimal welfare [46, 48, 49].
*   **(5) Dating-app fit:** **High**. Directly applies to dating apps (e.g., OkCupid or Tinder) where unrestricted swiping generates severe congestion, making swipe caps necessary to keep profiles fresh and active [50-52].
*   **(6) Confidence:** **High**.

---

### **5. Halaburda Restricting Choice**
*   **(1) Bibliography:** *Competing by Restricting Choice: The Case of Matching Platforms*, Hanna Halaburda, Mikołaj Jan Piskorski, Pınar Yıldırım, 2017, *Management Science* [53-55].
*   **(2) What they did:** Examined how a matching platform can successfully compete against unrestricted rivals and charge higher prices by deliberately limiting the number of choices it offers to its users [53, 56].
*   **(3) Two-sided balancing mechanism:** Restricting the size of the daily choice set (\\(N\\)) shown to both sides, which mitigates the negative, same-side competition effect and increases overall acceptance rates [57-59].
*   **(4) Metrics & Effects:** Proved that as \\(N\\) grows, the negative competition effect eventually outweighs the positive choice effect, turning network effects negative [60, 61]. Shows that a restricted-choice platform (\\(M_1\\)) can coexist with an unrestricted rival (\\(M_2\\)) and charge a higher fee (\\(f_1 > f_2\\)) because it attracts impatient users with low outside options who find rejection costly [62-64].
*   **(5) Dating-app fit:** **High**. Formulated to explain the business models of online dating platforms, specifically why eHarmony can successfully charge a 25% price premium over Match.com despite offering fewer daily choices [53, 56, 57].
*   **(6) Confidence:** **High**.

---

### **6. Fong Market Thickness Dating (Jessica Yu / Fong)**
*   **(1) Bibliography:** *Search, Selectivity, and Market Thickness in Two-Sided Markets*, Jessica Yu (Fong), 2018, Working Paper/Doctoral Thesis (Stanford GSB) [65, 66].
*   **(2) What they did:** Designed and implemented a field experiment on a major mobile dating app, combined with a structural model, to causally measure how beliefs about market thickness (potential matches and competitors) shape search and selectivity [65, 67].
*   **(3) Two-sided balancing mechanism:** **Manipulating user beliefs** about localized market thickness via pop-up notifications to alter their value of continuing search, which can be combined with adjustments to the platform's daily like limit [65, 68-70].
*   **(4) Metrics & Effects:** A 50% increase in believed market size makes users 3% less likely to like low-quality and 2.8% more likely to like high-quality profiles (increased selectivity) [71]. A 50% increase in competition makes users 2.3% more likely to like low-quality and 4.5% less likely to like high-quality profiles (reduced selectivity) [71]. Counterintuitively, growing platform membership by 25% on both sides decreases matches by 12% for men and 17% for women in small markets due to excessive selectivity—an effect that can be reversed by doubling the daily like limit [72-74].
*   **(5) Dating-app fit:** **High**. Directly implemented as a randomized controlled trial and structural model on a popular, real-world mobile dating application [65, 67, 69].
*   **(6) Confidence:** **High**.

---

### **7. Lee-Niederle Rose Signaling**
*   **(1) Bibliography:** *Propose with a rose? Signaling in internet dating markets*, Soohyung Lee, Muriel Niederle, 2015, *Experimental Economics* [75, 76].
*   **(2) What they did:** Conducted a randomized field experiment in online dating to evaluate the behavior and matching success rates of users endowed with scarce "virtual roses" to signal special interest when requesting a date [77, 78].
*   **(3) Two-sided balancing mechanism:** **Preference signaling**. Proposers are given a strictly limited supply of non-binding virtual signals (roses) to attach to offers, allowing recipients to verify attainability and interest in a cluttered market [77, 79, 80].
*   **(4) Metrics & Effects:** Attaching a rose increased the likelihood of a proposal being accepted by 3.3 percentage points (a 20% relative increase), equivalent to three-quarters of the benefit of moving up a desirability tier [81, 82]. Endowing users with 8 roses instead of 2 increased total initiated dates by 44–48% for men and 86% for women without sacrificing date quality or crowding out non-rose offers [83-85]. However, users behaved non-strategically, wasting 30% of roses on the most selective "top" group who ignored them [86-88].
*   **(5) Dating-app fit:** **High**. Conducted as a live, randomized field experiment on a major online dating platform [77, 80, 89].
*   **(6) Confidence:** **High**.

---

### **8. Hitsch Matching and Sorting**
*   **(1) Bibliography:** *Matching and Sorting in Online Dating*, Günter J. Hitsch, Ali Hortaçsu, Dan Ariely, 2010, *American Economic Review* [90, 91].
*   **(2) What they did:** Estimated a rich structural model of mate preferences from first-contact choices on an online dating website and applied the Gale-Shapley stable matching algorithm to analyze sorting patterns and market efficiency [90, 92, 93].
*   **(3) Two-sided balancing mechanism:** Modeled dating app selections using a threshold-crossing rule and a fixed-effects binary logit estimator to evaluate the efficiency of frictionless, decentralized matching [93-95].
*   **(4) Metrics & Effects:** Documented strong sorting correlations in actual matches: age (\\(0.70\\)), looks (\\(0.31\\)), height (\\(0.15\\)), BMI (\\(0.13\\)), income (\\(0.15\\)), and education (\\(0.12\\)) [96, 97]. The Gale-Shapley model, using only first-contact preference estimates, successfully predicted these sorting patterns [98, 99]. The decentralized app matched users within 3.8–4.6% of their theoretical first choice under a centralized planner, demonstrating near-perfect market efficiency [100, 101].
*   **(5) Dating-app fit:** **High**. Grounded directly in complete, rich user profiles and interaction data from a major online dating service [90, 92].
*   **(6) Confidence:** **High**.

---

### **9. Bruch-Newman Aspirational Pursuit**
*   **(1) Bibliography:** *Aspirational pursuit of mates in online dating markets*, Elizabeth E. Bruch, M. E. J. Newman, 2018, *Sociological/Scientific Publication* [102].
*   **(2) What they did:** Analyzed heterosexual dating hierarchies and messaging behavior across four large US cities (New York, Boston, Chicago, Seattle) using empirical communication networks from a popular free online dating site [102, 103].
*   **(3) Two-sided balancing mechanism:** Analyzed the natural structural boundaries of dating markets, calculating desirability rankings using **PageRank** on directed initial-contact message networks [103-105].
*   **(4) Metrics & Effects:** Found that both men and women consistently engage in aspirational pursuit, targeting partners who are on average **25% more desirable** than themselves [102, 106]. Messaging effort is highly calibrated: users write messages up to 2x longer to more desirable partners [107]. Crucially, as the desirability gap of the recipient increases, the probability of receiving a reply drops markedly [102, 108].
*   **(5) Dating-app fit:** **High**. Directly analyzes large-scale, population-level messaging and interaction data from a prominent online dating platform [102, 103].
*   **(6) Confidence:** **High**.

***

🎧 This rich collection of papers would make an exceptional audio overview if you want a deep dive into the mathematical mechanisms that dating platforms—like Tinder, Hinge, and Bumble—use to solve same-side competition and superstar congestion.