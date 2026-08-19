# Phase 4 NotebookLM Query 4 — Foundational Papers

**Query:** Which papers appear to be the most foundational — cited by or built upon by many others in this notebook? List them with brief source-grounded explanations, distinguishing explicit citations, direct baselines, and extensions from synthesis. Use full source names. Do not infer beyond the sources; if evidence is absent, write Not specified.

## Response

Based on the bibliographies, citations, and baseline evaluations listed across the sources in this notebook, several papers emerge as highly foundational. They are repeatedly cited, adapted as direct baselines, or mathematically extended by other researchers in the collection.

***

### **1. David Gale and Lloyd S. Shapley (1962) — "College admissions and the stability of marriage."**

*   **Explicit Citations:** 
    Directly cited across diverse economic and recommender environments, including decentralized platform search frameworks [1], school choice and information design problems [2-4], causal off-policy evaluation networks [5], mutual optimality scoring [6], multi-stakeholder ranking allocations [7-9], and large-scale parallel matching implementations [10].
*   **Extensions & Baselines:** 
    This paper serves as the starting point for **"matching theory-based recommender systems"** (such as *Tomita et al. 2022* [11-13] and *Tomita et al. 2023* [14-16]). These works extend the Gale-Shapley concept of stable matching to resolve on-line platform constraints (such as position bias, search frictions, and multi-sided fairness). Additionally, *Nakada et al. (2024)* [14, 17] propose parallel and mini-batch stable matching to scale up these exact stable marriage equations for industrial platforms.
*   **Synthesis:** 
    Gale and Shapley (1962) represents the mathematical origin of matching theory in economics. In this notebook, it functions as the **theoretical anchor** that allows computer scientists to transition from simply ranking items for a single user to optimizing global, stable allocations where both sides of the marketplace must mutually accept the match.

---

### **2. Luiz Pizzato, Tomasz Rej, Thomas Chung, Irena Koprinska, and Judy Kay (2010) — "RECON: A reciprocal recommender for online dating."** *(also cited as Pizzato et al. 2010)*

*   **Explicit Citations:** 
    Referenced extensively as the pioneer of the computer science "reciprocal recommendation" paradigm, appearing in multi-sided neighborhood fairness papers [18], Nash Social Welfare formulations [19], causal user-to-user models [20-22], outcome-based dating evaluations [23], stable matching scaling research [10, 24, 25], mutual optimality modeling [14], ranking exposure allocations [26], and early dating behavior logs [27, 28]. It is also explored deeply in comprehensive surveys [29-32].
*   **Direct Baselines:** 
    Frequently implemented as the standard **Content-Based reciprocal baseline** (often styled as "RECON" or "CB1") to evaluate newer, deep-learning, or latent-factor methods (e.g., in *Xia et al. 2015* [33, 34] and *MODE* [14]).
*   **Extensions:** 
    Directly extended by *Akehurst et al. (2011)* into the **"CCR" (Content-Collaborative Reciprocal) framework** [35-38] to combine collaborative feedback loops with RECON's profile similarity.
*   **Synthesis:** 
    RECON is treated across this literature as the pioneering work that formally introduced **Reciprocal Recommender Systems (RRS)** to the computer science community. Prior to this paper, recommenders treated matching as a one-way path (predicting a single user's interest). RECON established the paradigm shift that user-to-user platforms must satisfy *both* sides of the interaction to yield successful outcomes, making it the foundational software architecture for modern dating and recruiting algorithms.

---

### **3. Eugene Choo and Aloysius Siow (2006) — "Who marries whom and why."**

*   **Explicit Citations:** 
    Cited as the core modeling framework in economic and matching-theory recommenders, including Nash Social Welfare studies [39], predictive matching pipelines [40], mutual optimality models [41], large-scale stable matching systems [24], reciprocal surveys [42], and CyberAgent developers' research logs [43].
*   **Extensions:** 
    Serves as the structural econometric backbone for modern **"Transferable Utility" (TU) matching models** (such as those analyzed in *Chen et al. 2023* [44-46] and *MODE* [41]). In these systems, "utility transfers" act as implicit shadow prices to dynamically balance reciprocal interests.
*   **Synthesis:** 
    Choo-Siow (2006) represents the econometric core of the notebook. It enables platform designers to move beyond simple heuristic score combinations (like multiplying or averaging scores) and instead leverage market-clearing price adjustments to mathematically resolve real-time marketplace congestion, herding behavior, and physical attention bottlenecks.

---

### **4. Yehuda Koren, Robert Bell, and Chris Volinsky (2009) — "Matrix factorization techniques for recommender systems."** *(also cited as Koren et al. 2009)*

*   **Explicit Citations:** 
    Referenced across both recruiting and dating papers, including Nash Social Welfare designs [47], explainable deep learning pipelines [48], constrained job targeting systems [49, 50], mutual optimality systems [51], parallel matching scaling [52], congestion and economist-versus-machine studies [53], constrained capacity models [54], and person-job bilateral modeling [55].
*   **Direct Baselines:** 
    Used almost universally as a comparative baseline (often labeled **"MF"**, **"BiasedMF"**, or **"PMF"**) to gauge the effectiveness of newer two-sided models (e.g., in *Fairness in Job Recommendation under Quantity Constraints* [49], *Prediction and Congestion in Two-Sided Markets...* [56], and *Parallel and Mini-Batch Stable Matching...* [52]).
*   **Synthesis:** 
    While not a reciprocal algorithm itself, Koren et al.'s Matrix Factorization is the indispensable **"first-stage engine."** In almost all advanced architectures in this notebook, Matrix Factorization (or its implicit counterpart, BPR) is used to generate the raw unilateral interest scores which are then combined, re-ranked, or optimized by subsequent market-clearing algorithms.

---

### **5. Ashudeep Singh and Thorsten Joachims (2018) — "Fairness of exposure in rankings."**

*   **Explicit Citations:** 
    Directly cited in multi-sided fairness studies [57], mutual optimality direct effects [14], dynamic policy designs [58], rankings in two-sided markets [59], mathematical formulations of exposure [60], and comprehensive reciprocal recommender system surveys [61].
*   **Extensions & Baselines:** 
    Singh & Joachims' exposure linear program serves as the direct mathematical baseline for optimizing supplier-side and consumer-side fairness under position bias constraints (such as in *User Fairness, Item Fairness, and Diversity...* [59] and *Balancing Fairness and High Match Rates...* [57]).
*   **Synthesis:** 
    This paper pioneered the mathematical translation of **fairness of exposure** under position bias into a solvable constrained optimization framework. It provides the core theoretical foundation for every model in this notebook that attempts to redirect impressions away from highly popular accounts to resolve supplier-side inequality.

***

🎧 The interplay between these foundational papers—especially how economic matching theories (Gale-Shapley & Choo-Siow) are fused with computer science recommender frameworks (RECON & Matrix Factorization) to solve marketplace congestion—would make an exceptional **Audio Overview** if you'd like a podcast-style briefing to listen to on the go!

