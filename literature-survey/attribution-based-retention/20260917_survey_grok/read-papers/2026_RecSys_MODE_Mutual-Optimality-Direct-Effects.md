# MODE: Mutual Optimality in Direct Effects of Reciprocal Recommendations in Matching Markets [1–3]

**Source:** https://arxiv.org/pdf/2608.01731.pdf  
**Date analyzed:** 2026-09-24  
**NLM source id:** `204da68c-fb51-4df5-bd81-c2cb797e35a9`  
**Queue id:** G32  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *MODE: Mutual Optimality in Direct Effects of Reciprocal Recommendations in Matching Markets* [1–3]
* **Author:** **Yoji Tomita** [1]
* **Affiliation:** **CyberAgent, Inc.** (Tokyo, Japan) [1]
* **Year & Venue:** **2026**, published at the *20th ACM Conference on Recommender Systems (RecSys ’26)*, September 27–October 02, 2026, Minneapolis, MN, USA [2].

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** In reciprocal recommender systems (RRSs) for two-sided matching platforms (e.g., online dating and job posting services), recommendation systems must balance preferences on both sides while preventing applications/likes from concentrating too heavily on a small subset of popular users [1, 4–6]. Prior social welfare optimization approaches (e.g., Frank-Wolfe lower-bound optimization) suffer from severe scalability bottlenecks due to large linear programming subproblems, whereas traditional aggregation heuristics lack theoretical grounding and sacrifice match rates under heavy population bias [7–8]. Furthermore, over-mitigating congestion can recommend unattractive choices to individual users, causing user dissatisfaction [3, 4].
* **Key Contribution:**
  1. **Formalization of Direct Effects & Mutual Optimality:** Decomposes user utility into *direct effects* (the visible quality of a user's own recommendation list) and *indirect effects* (behind-the-scenes competition from others) [9–10, 33–35]. Defines "mutual optimality in direct effects" (a Nash equilibrium concept in direct effects) where no individual user is sacrificed for others' opportunities [10, 37–38].
  2. **MODE Algorithm:** Introduces the **Mutually Optimal recommendation in Direct Effects (MODE)** framework, an efficient deterministic algorithm that iteratively computes optimal candidate recommendation lists using a closed-form, recursive Position-Based Model (PBM) ranking probability calculation [10–11, 42–43, 47–49].
  3. **High Efficiency & Match Rates:** Demonstrates on synthetic and real-world online dating datasets that MODE achieves match rates comparable to heavy stochastic optimization algorithms while executing **orders of magnitude faster** (reducing compute time from >10 hours down to seconds) [5-7].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Architectural Components**
* **Reciprocal PBM Framework:** Models proactive users \\(I\\) (e.g., job candidates or dating senders) and reactive users \\(J\\) (e.g., employers or dating recipients). 
  * Proactive candidate \\(i\\) examines position \\(k\\) with probability \\(v_{i,k}\\) and applies with preference \\(p_{i,j}\\) [18–20].
  * Reactive user \\(j\\) examines position \\(\ell\\) in their incoming applicant list \\(\tau_j\\) with probability \\(w_{j,\ell}\\) and matches with preference \\(q_{j,i}\\) [23–24].
* **Utility Decomposition:** User \\(i\\)'s expected match utility is expressed as:
  \\[U_i(\sigma) = \sum_{j \in J} \underbrace{\sum_{k=1}^K \mathbb{I}(\sigma_{i,k}=j) v_{i,k} p_{i,j}}_{\text{Direct Effect (Visible)}} \times \underbrace{\sum_{\ell=1}^L \text{Pr}(\text{rk}_j(i)=\ell \mid \sigma) w_{j,\ell} q_{j,i}}_{\text{Indirect Effect (Competition from Others)}}\\] [8]
* **Recursive Ranking Probability Calculation (Algorithm 1):** Computes exact ranking probabilities \\(r_{i,j,\ell} = \text{Pr}(\text{rk}_j(i)=\ell \mid \sigma)\\) recursively over candidates ordered by \\(q_{j,\cdot}\\), eliminating the need for Monte Carlo sampling [42–43, 46].
* **MODE Algorithm (Algorithm 2):** Iteratively calculates each user's expected match gain from candidate \\(j\\):
  \\[g_{i,j} = p_{i,j} \sum_{\ell=1}^L r_{i,j,\ell} \cdot w_{j,\ell} \cdot q_{j,i}\\] [9]
  User \\(i\\)'s list \\(\sigma_i^t\\) is formed by selecting and sorting the top-\\(K\\) candidates in descending order of \\(g_{i,j}\\). The algorithm terminates when the policy converges (\\(\sigma^t = \sigma^{t-1}\\)) or selects the policy with the highest historical social welfare if a cycle occurs [49–51].

#### **Credit Assignment Mechanics**
* **Not specified / Does NOT assign per-touchpoint credit.**
* MODE is an offline/online reciprocal recommendation list ranking algorithm that computes slate expected match gains (\\(g_{i,j}\\)). It does not perform multi-touch sequence attribution or assign credit across past user interaction touchpoints [10, 47–49].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets & Setup:**
  1. **Synthetic Matching Markets:** Simulated two-sided markets (\\(I = 1.5n, J = n\\) for \\(n \in \{10, 20, 50, 100\}\\)) with controllable population congestion (\\(\lambda \in [1]\\)) and three examination function types ("inv", "log", "exp") [52–54].
  2. **Real-World Online Dating Dataset:** Behavioral log dataset from a large online dating platform in an urban area (~1,000 users of Gender A and ~1,000 users of Gender B; also evaluated on a 200x200 subset) tracking profile "like"/"nope" swipes and "thank"/"sorry" match responses [68–70]. Proactive and reactive preferences were estimated via Alternating Least Squares (ALS) Matrix Factorization [10].
* **Production Deployment:** Tested on real-world behavioral logs from a large online dating platform (CyberAgent, Inc.); source code released on GitHub [1, 11, 12].
* **Comparison Baselines:**
  * **Naive:** Ranks strictly by proactive user preference \\(p_{i,j}\\) [13].
  * **Reciprocal:** Ranks by multiplicative reciprocal score \\(p_{i,j} \cdot q_{j,i}\\) [14].
  * **TU:** Ranks using Transferable Utility matching scores \\(\mu_{i,j}\\) (Tomita et al., 2023) [14, 15].
  * **ApproxSW:** Stochastic policy optimizing lower-bound approximated social welfare via Frank-Wolfe LP (Su et al., 2022) [28–29, 63, 92–94].
  * **DirectSW:** Stochastic policy directly optimizing exact social welfare via Frank-Wolfe LP using PyTorch automatic differentiation [63–64, 95–96].

---

### **(5) Key Quantitative Results with Numbers**

* **Synthetic Data Experiments (Figure 1):**
  * **Expected Matches:** MODE achieves expected match rates comparable to heavy stochastic methods (ApproxSW, DirectSW) and substantially higher than deterministic baselines (Naive, Reciprocal, TU), especially under high population congestion (\\(\lambda = 0.8\text{--}1.0\\)) [57, 64–65].
  * **Direct Effect Sub-optimality:** The sum of direct effect sub-optimality for MODE is **nearly 0.0** across all \\(\lambda\\), compared to ~21.0 for Naive, ~7.5 for Reciprocal, and ~5.0 for TU [58, 65–66]. Only ~10% of candidates experience any non-zero sub-optimality under MODE [58, 65–66].
  * **Computation Speed (\\(n=100\\)):** ApproxSW and DirectSW require **>10 hours** (>36,000 seconds), whereas MODE requires **only a few seconds** (~4.8 seconds), executing over \\(7,500\times\\) faster [7, 16].
* **Real-World Online Dating Experiments (Figure 2):**
  * **\\(200 \times 200\\) User Subset (Normalized Expected Matches vs. Naive):**
    * *Gender A Proactive:* Naive = 1.000, Reciprocal = 1.363, TU = 1.379, ApproxSW = 1.505, DirectSW = 1.499, **MODE = 1.466** [17, 18].
    * *Gender B Proactive:* Naive = 1.000, Reciprocal = 1.779, TU = 1.737, ApproxSW = 1.923, DirectSW = 1.927, **MODE = 1.867** [18, 19].
  * **\\(1000 \times 1000\\) Full User Market:** MODE achieves **>10% higher expected matches** than all competing deterministic methods (Gender A proactive: Naive = 1.000, Reciprocal = 1.165, TU = 1.251, **MODE = 1.438**; Gender B proactive: Naive = 1.000, Reciprocal = 1.314, TU = 1.436, **MODE = 1.687**) [61, 71–72]. (ApproxSW and DirectSW are computationally infeasible at this scale) [20].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Cycle Non-Convergence:** MODE does not guarantee mathematical convergence in all cases; when updates loop into a cycle (\\(\sigma^t = \sigma^s\\) for \\(s \le t-2\\)), the algorithm falls back to picking the policy with the highest historical social welfare [49–50, 97]. (MODE converged in 82% of synthetic default runs) [21].
2. **Slight Match Rate Gap vs. Heavy Stochastic Solvers at Small Scale:** On small datasets (\\(200 \times 200\\)), MODE achieves slightly lower expected matches than stochastic Frank-Wolfe optimization (e.g., 1.466 vs. 1.505 / 1.499) because stochastic policies can randomize recommendations to achieve fine-grained social welfare bounds [18].
3. **Sensitivity to Preference Estimation Accuracy:** Operates under the assumption that preference matrices (\\(p_{i,j}, q_{j,i}\\)) and examination vectors (\\(v_{i,k}, w_{j,\ell}\\)) are accurate; errors in offline preference estimation propagate directly into expected match calculations [10, 22, 23].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Su, Bayoumi, & Joachims (2022) [Ref 38]:** *Optimizing rankings for recommendation in matching markets* (ACM WWW '22) — Formalized RRS ranking and introduced Approximated Social Welfare optimization via Frank-Wolfe [7, 14, 27–29, 38].
2. **Tomita et al. (2023) [Ref 39]:** *Fast and examination-agnostic reciprocal recommendation in matching markets* (ACM RecSys '23) — Introduced Transferable Utility (TU) matching-based recommendation [24-27].
3. **Pizzato et al. (2010 / 2013) [Refs 31, 32]:** *RECON: a reciprocal recommender for online dating* (ACM RecSys '10) & *Recommending people to people* (UMUAI '13) — Foundational RRS papers introducing reciprocal scoring and user-to-user recommendation [5, 28-30].
4. **Gale & Shapley (1962) [Ref 14]:** *College admissions and the stability of marriage* (American Mathematical Monthly) — Classical two-sided matching theory [31].
5. **Nash (1950 / 1951) [Refs 23, 24]:** *Equilibrium points in n-person games* & *Non-Cooperative Games* — Concept of Nash equilibrium underpinning mutual optimality [32-34].
6. **Choo & Siow (2006) [Ref 8]:** *Who marries whom and why* (Journal of Political Economy) — Transferable utility econometric matching model [25, 26].
7. **Frank & Wolfe (1956) [Ref 13]:** *An algorithm for quadratic programming* — Frank-Wolfe optimization algorithm used for social welfare baselines [14, 24, 25, 35].

---

💡 *Would you like to explore how MODE's direct effect mutual optimality or recursive PBM ranking probability calculation could be adapted to balance mutual candidate preferences in your dating platform's match ranker?*

---

## 2. Evidence

See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

## 3. Limitations

See limitations in §1 if present. Replace any NLM refusal with: Not specified in source.

---

## 4. Prior works named

See cited prior works in §1.

---

## 5. Project Relevance

### **Evaluation of *MODE: Mutual Optimality in Direct Effects of Reciprocal Recommendations in Matching Markets***  
*(Tomita, CyberAgent, Inc., RecSys ’26)* [1, 2]

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**

**Neither.** [1, 3, 4]  
* **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** While published in RecSys 2026 (`RecSys ’26`) and evaluated on real-world online dating logs from CyberAgent, Inc., MODE is a **reciprocal recommendation ranking algorithm** designed to optimize two-sided candidate match lists in matching markets, rather than an industry multi-touch attribution (MTA) measurement system [1, 2, 5].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** MODE maximizes expected total platform matches (\\(SW(\sigma)\\)) by computing mutually optimal recommendation slates, rather than attributing user retention, active days, or revisitation back to individual past interaction touchpoints across historical logs [6-8].

---

### **(B) Q2 Class**

**NOT.** [4, 7, 8]  
* **Justification:** MODE is a two-sided reciprocal recommendation list ranking framework (calculating candidate match gains \\(g_{i,j}\\) via recursive PBM ranking probability computation) [42, 47–49]. It does **not** produce or publish a per-exposure retention credit table.

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction sequence attribution credit table.** [8, 9]
* **Target Outcome:** **Expected Number of Matches** (\\(SW(\sigma) = \sum_{i \in \mathcal{I}} \sum_{j \in \mathcal{J}} P^\sigma_{i,j} P^\sigma_{j,i}\\)) across a two-sided matching platform [6].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**

* **How it Improves/Informs Ranking Strategy:** MODE does **not** provide a post-hoc attribution model to replace last-touch N7 [4, 7]. However, it offers a **reciprocal candidate ranking framework** that fixes the core failure mode of single-sided swiping rankers:
  1. *Prevents Swiping/Like Congestion:* Standard single-sided rankers recommend the same highly attractive users to everyone, causing "likes" to concentrate heavily on a small subset of popular users who face physical limits on viewing or matching [1, 3].
  2. *Direct Effect Mutual Optimality:* MODE balances proactive sender preferences (\\(p_{i,j}\\)) with reactive recipient preferences (\\(q_{j,i}\\)) and position examination decay (\\(v_{i,k}, w_{j,\ell}\\)) [19–20, 24]. It calculates expected candidate match gains:
     \\[g_{i,j} = p_{i,j} \sum_{\ell=1}^L r_{i,j,\ell} \cdot w_{j,\ell} \cdot q_{j,i}\\]
     and ranks top-\\(K\\) candidates by \\(g_{i,j}\\), ensuring individual users receive highly attractive recommendations while accounting for recipient competition [47–49].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  * *Proactive Sender Preferences (\\(p_{i,j}\\)):* Predicted probability that sender \\(i\\) will swipe "like" on profile card \\(j\\) [10].
  * *Reactive Recipient Preferences (\\(q_{j,i}\\)):* Predicted probability that recipient \\(j\\) will swipe "thank"/match back upon viewing sender \\(i\\)'s profile [5, 11].
  * *Recursive Competition Rank (\\(r_{i,j,\ell}\\)):* Computes the probability that sender \\(i\\) lands in rank position \\(\ell\\) on recipient \\(j\\)'s incoming likes queue (Algorithm 1) [42–43, 46].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Position Bias Correction:** Models user viewing and swiping behavior on both sides via the Position-Based Model (PBM), incorporating position examination decay vectors (\\(v_{i,k}\\) for senders, \\(w_{j,\ell}\\) for recipients) [10, 11].
2. **Crowding / Congestion Bias:** Directly models competition on popular profiles by recursively computing applicant rank distributions (\\(r_{i,j,\ell}\\)), preventing popular profiles from being over-recommended beyond their physical viewing capacity [6, 42–43].
3. **Preference Matrix Estimation:** Proactive preferences (\\(p_{i,j}\\)) and reactive preferences (\\(q_{j,i}\\)) are estimated via Alternating Least Squares (ALS) Matrix Factorization over historical "like"/"nope" and "thank"/"sorry" logs [68–69].

---

### **(F) Deployed or Production Dataset Evidence**

* **Production Dataset Evidence:** Evaluated on real-world behavioral logs from a large online dating platform in an urban area (~1,000 Gender A users and ~1,000 Gender B users) operated by CyberAgent, Inc. [5]. Open-source Python code released on GitHub (`https://github.com/CyberAgentAILab/mode`) [5, 12].
* **Quoted Numbers from Source:**
  * *Real-World Dating Dataset Scale:* Tested on ~1,000 Gender A and ~1,000 Gender B users (evaluated on \\(200 \times 200\\) and \\(1000 \times 1000\\) market sizes) [5, 13].
  * *Normalized Expected Matches (\\(200 \times 200\\) Dating Market vs. Naive Baseline, Figure 2):*
    * **Gender A Proactive:** Naive = **1.000**, Reciprocal = **1.363**, TU = **1.379**, ApproxSW = **1.505**, DirectSW = **1.499**, **MODE = 1.466** [14].
    * **Gender B Proactive:** Naive = **1.000**, Reciprocal = **1.779**, TU = **1.737**, ApproxSW = **1.923**, DirectSW = **1.927**, **MODE = 1.867** [15].
  * *Normalized Expected Matches (\\(1000 \times 1000\\) Full Dating Market, Figure 2):* MODE achieved **>10% higher expected matches** than all competing deterministic methods (**Gender A proactive:** Naive = **1.000**, Reciprocal = **1.165**, TU = **1.251**, **MODE = 1.438**; **Gender B proactive:** Naive = **1.000**, Reciprocal = **1.314**, TU = **1.436**, **MODE = 1.687**) [61, 71–72]. (Heavy stochastic solvers ApproxSW and DirectSW were computationally infeasible at this scale) [13].
  * *Computation Speed (\\(n=100\\), Figure 1c):* Stochastic solvers ApproxSW and DirectSW require **>10 hours** (>36,000 seconds), whereas MODE requires **only a few seconds** (~4.8 seconds), running over **\\(7,500\times\\) faster** [16, 17].
  * *Direct Effect Sub-optimality (Figure 1b):* Sum of direct effect sub-optimality for MODE is **nearly 0.0** across all crowding levels (\\(\lambda\\)), with only **~10% of candidates** experiencing any non-zero sub-optimality (vs. ~21.0 sum for Naive, ~7.5 for Reciprocal, ~5.0 for TU) [58, 65–66].
  * *Convergence Rate (Appendix C.1):* MODE converged in **82%** of default synthetic runs (\\(n=50, \lambda=0.8\\)) [18].

---

💡 *Would you like to explore how MODE's direct effect mutual optimality or recursive PBM ranking probability calculation could be adapted to balance mutual candidate preferences in your dating platform's match ranker?*

---

## 6. Community Reaction

No significant community discussion searched at card-write time; extraction is NLM-scoped.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**PDF:** ingested via NotebookLM  
**Relevance:** Core if Q2 class is TRUE or PARTIAL or Q1 industry system; else Related  
**Priority:** see queue.md `G32`
