### **1. Johari experimental design two-sided platforms**
*   **(1) Bibliography:** *Experimental Design in Two-Sided Platforms: An Analysis of Bias*, Ramesh Johari, Hannah Li, Inessa Liskovich, Gabriel Y. Weintraub, 2020 (published version *Management Science*, 2022/2025), Journal Article [1-3].
*   **(2) What they did (76 words):** Developed an analytical stochastic framework and its mean-field limit to study SUTVA-violating interference bias in marketplace experiments [1, 4]. They modeled a continuous-time Markov chain tracking available inventory where customers sequentially book listings for a random occupancy period [5-7]. Using this, they compared customer-side and listing-side randomization designs against a novel Two-Sided Randomization (TSR) design with customized debiasing estimators [8-10].
*   **(3) Balancing mechanism (43 words):** Shows that marketplace interference depends on market balance [8, 11]. In demand-constrained regimes, customer-side randomization (CR) is unbiased [8, 11]. In supply-constrained regimes, listing-side randomization (LR) is unbiased [8, 11]. Their TSR-Improved estimators (TSRI-1, TSRI-2) utilize strategic "cannibalization" correction terms to eliminate bias across moderately balanced markets [12-14].
*   **(4) Metrics & reported effects:** Evaluated bias relative to the true Global Treatment Effect (GTE) [15, 16]. In demand-constrained settings where relative demand \\(\lambda/\tau = 1\\), the listing-side randomization (LR) bias was tiny at 1.7% of the GTE [17]. In simulations of \\(N = 5000\\) listings, TSRI-2 successfully minimized bias but incurred a higher standard error (variance) [18-21].
*   **(5) Fit for a dating app:** **High**. Dating platforms are highly connected two-sided marketplaces where relative demand (user response times and daily active ratios) dictates whether matching experiments suffer from user-side or profile-side interference bias.
*   **(6) Confidence:** **High**. Grounded directly in the provided, fully readable paper in the notebook [1].

---

### **2. Bajari multiple randomization**
*   **(1) Bibliography:** *Multiple Randomization Designs: Estimation and Inference with Interference*, Lorenzo Masoero, Suhas Vijaykumar, Thomas S. Richardson, James McQueen, Ido Rosen, Brian Burdick, Pat Bajari, Guido Imbens, 2025, arXiv Preprint [22].
*   **(2) What they did (71 words):** Derived the exact finite-sample properties, design-based variance, conservative variance estimators, and central limit theorems for "Simple Multiple Randomization Designs" (SMRDs) [22-24]. They utilized a design-based randomization framework—holding potential outcomes as fixed—to analyze complex strategic cross-unit spillovers where treatments and outcomes are measured at the level of unit tuples (e.g., buyer-seller pairs) [23, 25, 26].
*   **(3) Balancing mechanism (43 words):** SMRDs select a random subset of buyers and sellers to expose only the joint treated pairs [23, 27]. This isolates and measures "local interference"—where a pair's outcome depends on the individual treatment and the cumulative treatment fractions of neighboring rows and columns [28-30].
*   **(4) Metrics & reported effects:** Formulated estimators for average treatment effect (\\(\tau_{ATE}\\)), buyer-spillover (\\(\tau_{spill}^B\\)), and direct effects [31-33]. Simulations on \\(I=200\\) buyers and \\(J=150\\) sellers verified that SMRDs successfully recovered the correct positive sign of platform profits where standard single-sided designs failed due to strategic spillovers [34, 35].
*   **(5) Fit for a dating app:** **High**. Ideal for evaluating how exposing a new premium communication feature to a select pair of users (e.g., sender and receiver) alters the messaging spillovers of untreated candidates across the broader network.
*   **(6) Confidence:** **High**. Grounded directly in the provided, fully readable paper in the notebook [22].

---

### **3. Holtz Airbnb cluster randomization**
*   **(1) Bibliography:** *Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization: Evidence from a Pricing Meta-experiment on Airbnb*, David Holtz, Felipe Lobel, Ruben Lobel, Inessa Liskovich, Sinan Aral, 2024 (published in *Management Science*, January 2025), Journal Article [2, 36].
*   **(2) What they did (78 words):** Documented empirical evidence of SUTVA-violating interference bias in online marketplaces and evaluated the efficacy of cluster randomization at reducing it [36]. They ran an in vivo pricing meta-experiment on Airbnb, randomly assigning listings into either an individual-level randomized meta-treatment arm (prone to spillovers) or a cluster-randomized meta-treatment arm [37-39]. Standard errors and treatment effects were analyzed to estimate the percentage of the naive treatment effect attributable to interference [40-42].
*   **(3) Balancing mechanism (46 words):** Formed listing clusters using recursive partitioning on 16-dimensional demand embeddings learned from user-level search session co-views [43-45]. This groups highly substitutable listings together into clusters, ensuring that treatment-induced demand shifts are contained within clusters, reducing the negative competitive spillovers that bias TATE estimates [46-48].
*   **(4) Metrics & reported effects:** Meta-experiment conducted on 2,602,782 Airbnb listings [49]. In the individual-level randomized arm, the platform fee increase led to an estimated loss of 0.345 bookings per listing [38, 50]. When compared with the cluster-randomized arm, 19.76% of this "naive" TATE loss was proven to be artificial interference bias and was successfully eliminated [38, 42].
*   **(5) Fit for a dating app:** **High**. Candidates on dating apps act as substitutes; clustering profiles based on swiping co-occurrence embeddings ensures that user-substitution effects are contained within clusters, preventing artificial matches-per-user drops in experiments.
*   **(6) Confidence:** **High**. Grounded directly in the provided, fully readable paper in the notebook [2].

---

### **4. Spotify fair marketplace**
*   **(1) Bibliography:** *Towards a Fair Marketplace: Trade-off between Relevance, Fairness & Satisfaction in RecSys*, Rishabh Mehrotra, James McInerney, Hugues Bouchard, Mounia Lalmas, Fernando Diaz, 2018 (updated/copyright 2026), Spotify Research Blog / Conference Publication [51-53].
*   **(2) What they did (71 words):** Addressed the problem of "superstar economics"—where a small fraction of popular suppliers receive most recommendation exposure—on a music streaming platform [54, 55]. They built a computational framework using offline counterfactual estimation (Inverse Propensity Scoring) to balance the trade-offs between consumer relevance (interest profile match), supplier group fairness (diversity across popularity bins), and long-term user satisfaction (track play counts) [56-59].
*   **(3) Balancing mechanism (42 words):** Deployed "adaptive policies" that calculate a listener's individual affinity or tolerance toward long-tail, fair content [60, 61]. The recommender dynamically routes diverse, fair sets of suppliers to high-tolerance consumers, while reserving standard relevant recommendations for users who do not prefer fair content [60, 61].
*   **(4) Metrics & reported effects:** While a global shift from relevance to fairness caused a 35% relative decline in consumer satisfaction, adaptive policies achieved the best trade-off—limiting supplier fairness losses to just 15% to 17% while generating a positive 9% to 21% gain in user satisfaction [62, 63].
*   **(5) Fit for a dating app:** **High**. Essential for combating the "superstar effect" in dating (where a small percentage of highly attractive profiles receive the vast majority of likes) by dynamically distributing long-tail profile exposure to open-minded users.
*   **(6) Confidence:** **High**. Grounded directly in the provided, fully readable blog post in the notebook [51].

---

### **5. LinkedIn fairness AI**
*   **(1) Bibliography:** *A closer look at how LinkedIn integrates fairness into its AI products*, Heloise Logan, Preetam Nandy, Kinjal Basu, Sakshi Jain, 2022, LinkedIn Engineering Blog [64].
*   **(2) What they did (69 words):** Outlined LinkedIn's progress in developing a scalable, platform-based Responsible AI framework to automatically measure and mitigate algorithmic bias [65]. The framework is designed to integrate seamlessly into LinkedIn's core ProML machine learning infrastructure, allowing AI modelers across different product verticals (e.g., Talent Search, PYMK) to easily evaluate and correct models before launching A/B experiments [65-67].
*   **(3) Balancing mechanism (40 words):** Automatically learns and appends a pluggable, post-processing score transformation layer directly on top of raw model scores [66, 68, 69]. This post-processing layer functions as a re-ranking layer that corrects for detected group-level opportunities and attributes without altering the underlying recommendation model [68-70].
*   **(4) Metrics & reported effects:** Implemented automated workflows using the open-source LinkedIn Fairness Toolkit (LiFT) [65, 71]. The blog details the architectural components (Fair Model Analyzer and Mitigation Trainer) and post-launch realized outcome metrics, but it does not report specific numeric statistical effects or percentages [71-73].
*   **(5) Fit for a dating app:** **High**. Provides a modular, model-agnostic re-ranking framework that can easily enforce demographic or gender-balance equity constraints on dating search results without needing to retrain heavy embedding models.
*   **(6) Confidence:** **High**. Grounded directly in the provided engineering blog post in the notebook [74].

---

### **6. Lyft marketplace marginal values** — **NO CONTENT**
### **7. DoorDash switchback rigor** — **NO CONTENT**
### **8. DoorDash supply-demand ML** — **NO CONTENT**
### **9. Airbnb host preferences** — **NO CONTENT**
### **10. Thumbtack instant matching** — **NO CONTENT**
### **11. Upwork market-level growth** — **NO CONTENT**

***

🎧 Since we've mapped out how these major industry platforms model and measure experimental bias, I could construct an audio briefing detailing how Airbnb, Spotify, and LinkedIn programmatically correct for competitive spillovers and algorithmic bias.