# Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching [1]

**Source:** https://arxiv.org/pdf/2602.15752.pdf  
**Date analyzed:** 2026-09-18  
**NLM source id:** `da74515a-9d0d-4f88-9161-7aa430fe7686`  
**Queue id:** G6  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**

* **Title:** *Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching* [1]
* **Authors:** **Ren Kishimoto**\*¹, **Rikiya Takehi**\*², **Koichi Tanaka**³, **Masahiro Nomura**¹, **Riku Togashi**⁴, **Yoji Tomita**⁴, and **Yuta Saito**⁵ (\*Equal contribution) [1–2]
* **Author Affiliations:**
  1. **Institute of Science Tokyo**, Tokyo, Japan (`kishimoto.r.ab@m.titech.ac.jp`, `nomura@comp.isct.ac.jp`) [1]
  2. **Waseda University**, Tokyo, Japan (`rikiya.takehi@fuji.waseda.jp`) [1]
  3. **Keio University**, Tokyo, Japan (`kouichi1207@keio.jp`) [1]
  4. **CyberAgent**, Tokyo, Japan (`rtogashi@acm.org`, `tomita_yoji@cyberagent.co.jp`) [1]
  5. **Hanjuku-kaso, Co., Ltd.**, Tokyo, Japan (`saito@hanjuku-kaso.com`) [2]
* **Year:** **2026** (arXiv pre-print: `2602.15752`, submitted Feb 2026) [1]
* **Venue:** Submitted to **ICLR 2026** / arXiv pre-print [1, 3]

---

### **(2) Core Problem and Key Contribution**

* **Core Problem:** Two-sided matching platforms (e.g., online dating, recruitment) typically optimize for total matches or axiomatic fairness of exposure [2, 4]. Match maximization concentrates recommendations on popular users, causing under-matched users to receive few matches and churn [2, 5, 6]. Axiomatic exposure fairness is only an unproven heuristic proxy and does not directly optimize user retention—which is the true business objective (e.g., subscription renewals) [2, 4, 7].
* **Key Contribution:**
  1. **User Retention Problem Formulation:** Formulates the novel problem setting of directly maximizing user retention across both sides of a two-sided matching platform [2, 8, 9].
  2. **Matching for Retention (MRet) Framework:** Introduces a dynamic Learning-to-Rank (LTR) algorithm that learns personalized retention curves \\(f(x, m)\\) based on cumulative match counts \\(m\\) and user context [2, 6, 17, 26–27].
  3. **Tractable Lower-Bound Optimization:** Proves Jensen and concavity lower bounds under concave retention assumptions, converting an NP-hard two-sided optimization into an efficient \\(O(N \log N)\\) per-candidate scoring and sorting algorithm that balances retention gains for both recommendation receivers and recommended candidates [6, 18, 20–24].

---

### **(3) Proposed Method or Architecture in Detail**

* **Two-Sided Joint Retention Gain Objective:** When user \\(x \in \mathcal{X}\\) arrives at time \\(\tau\\), the platform recommends a ranked list \\(\sigma_\tau = [\sigma_{\tau,1}, \dots, \sigma_{\tau,K}]\\) from opposing user set \\(\mathcal{Y}\\) to maximize joint retention probability gains across both sides [8, 18–19]:
  \\[\sigma_\tau^* = \arg\max_{\sigma_\tau} \left\{ \underbrace{\left[ f\left(x, m_{1:\tau}(x) + \sum_{k=1}^K \alpha_k r(x, \sigma_{\tau,k})\right) - f(x, m_{1:\tau}(x)) \right]}_{\text{Gain for receiver } x} + \sum_{k=1}^K \underbrace{\left[ f\left(\sigma_{\tau,k}, m_{1:\tau}(\sigma_{\tau,k}) + \alpha_k r(\sigma_{\tau,k}, x)\right) - f(\sigma_{\tau,k}, m_{1:\tau}(\sigma_{\tau,k})) \right]}_{\text{Gain for recommended candidates}} \right\}\\]
  where \\(r(x, y)\\) is the match probability and \\(\alpha_k\\) is the rank position visibility weight [10, 11].
* **Tractable MRet Score Derivation:** Under concave retention \\(f(x, \cdot)\\) (Lemma 1 & Lemma 2), MRet maximizes a tight lower bound by ranking candidates by an individual score in \\(O(N \log N)\\) time [20–24]:
  \\[\text{Score}(y) = \frac{1}{A} f(x, m_{1:\tau}(x) + A r(x, y)) + \frac{1}{\alpha_{\max}} \left[ f(y, m_{1:\tau}(y) + \alpha_{\max} r(x, y)) - f(y, m_{1:\tau}(y)) \right]\\]
  where \\(A = \sum_{k=1}^K \alpha_k\\) and \\(\alpha_{\max} = \max_k \alpha_k\\) [22–24].
* **Credit Assignment Mechanics:** Credit is assigned **per candidate profile \\(y\\)** at scoring time by evaluating its marginal contribution to the joint retention probability curves of both the receiver \\(x\\) and candidate \\(y\\) [11, 12]. It does **not** perform historical multi-touch sequence attribution over individual past swipes or messages; rather, it evaluates candidate match impact on long-term retention functions \\(f(x, m)\\) [2, 17–18].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets:**
  1. *Synthetic Matching Market:* \\(|X| = 1000, |Y| = 1000, K = 5\\), popularity skew parameter \\(\kappa \in [0.0, 1.0]\\), horizon \\(T = 2000\\). User retention labels sampled via Bernoulli distribution over synthetic retention functions \\(f(x, m)\\) [25–31].
  2. *Real-World Online Dating Platform Dataset:* Interaction and login logs from a large-scale Japanese online dating platform. Formed a \\(1000 \times 1000\\) user matching matrix (imputed via ALS) and trained retention function \\(\hat{f}\\) via XGBoost on 60,000 real user records partitioned into 5 k-means clusters [35–37, 74]. Evaluated next-month login retention (February 2025 logins \\(\rightarrow\\) March 2025 logins) [13, 14]. Also tested on a large-scale setup (\\(N_x = N_y = 5000\\)) [15].
* **Production Deployment:** Evaluated offline in simulation environments built directly from real-world user interaction and retention logs of a major Japanese online dating platform with millions of registered users [2, 35–37].
* **Comparison Baselines:**
  * **Max Match:** Standard greedy match probability maximization [10–11, 30].
  * **FairCo (Morik et al., 2020):** Dynamic LTR algorithm enforcing merit-proportional exposure fairness [12–14, 30].
  * **Uniform:** Random candidate ranking baseline [16].
  * **MRet (best):** Oracle upper bound with perfect access to ground-truth retention function \\(f\\) [16].
  * **Optimal:** Exact NP-hard exhaustive search over all possible rankings (evaluated on \\(N=20, K=3, T=50\\)) [17].

---

### **(5) Key Quantitative Results with Numbers**

* **Synthetic Benchmark Experiments (Figure 3 & 4):**
  * **Match Efficiency:** MRet achieved higher cumulative user retention rates than Max Match, FairCo, and Uniform across all time steps (\\(T=2000\\)), using only **~70% of the total match count** obtained by Max Match [18].
  * **Popularity Skew Robustness (\\(\kappa = 1.0\\)):** Under extreme popularity bias, Max Match retention collapsed (dropping to ~0.92 relative to Uniform), whereas MRet maintained a high retention rate (**1.08x–1.15x higher retention relative to Uniform**) [19].
  * **NP-Hard Approximation Accuracy (Figure 12):** Small-scale validation (\\(N=20, K=3, T=50\\)) showed MRet's retention curve tracks the exact NP-hard **Optimal** ranking curve almost identically [17].
* **Real-World Online Dating Benchmark Experiments (Figure 6, \\(T=3000\\)):**
  * **Extreme Data Sparsity:** Fairness-oriented methods collapsed due to matrix sparsity (FairCo and Uniform retained only **~52%–55% of users**) [20].
  * **Match Maximization:** Max Match achieved **~64% retention** [20].
  * **MRet Superiority:** **MRet achieved the highest user retention rate (~67%–68% retention)**, outperforming all baselines even when applied to non-concave real-world retention functions [20].
  * **Training Sample Scalability (Figure 13):** With \\(n=16,000\\) training records for the XGBoost retention estimator \\(\hat{f}\\), MRet matched the performance of the oracle `MRet (best)` (**~68% retention**) [21].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Pre-given Match Matrix Assumption:** Assumes match probabilities \\(r(x, y)\\) are pre-estimated offline; does not jointly optimize online exploration vs. exploitation for preference learning [22].
2. **Symmetric Group Weighting:** Treats male and female retention gains equally, whereas real-world platform business models often prioritize paying users (e.g., male subscribers in dating apps) or job seekers in recruitment [22].
3. **Sensitivity to Small Training Sizes:** When retention training data is constrained (\\(n=2000\\)), MRet's retention performance drops closer to Max Match (~64% retention) [21].
4. **Immediate Feedback Simplification:** Assumes binary match outcomes are observed immediately after recommendation, setting aside real-world asynchronous communication delays [23].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Morik et al. (2020) [FairCo / Dynamic LTR]:** *Controlling fairness and bias in dynamic learning-to-rank* (SIGIR '20) [24-27].
2. **Singh & Joachims (2018) [Fairness of Exposure]:** *Fairness of exposure in rankings* (KDD '18) [4, 24, 26, 28].
3. **Pizzato et al. (2010a,b,c) [RECON / Reciprocal Recommendation]:** *RECON: a reciprocal recommender for online dating* (RecSys '10) [3, 9, 39, 52–53].
4. **Tomita & Yokoyama (2024) [Fair Reciprocal Recommendation]:** *Fair reciprocal recommendation in matching markets* [4, 6, 16, 26, 29].
5. **Su, Bayoumi, & Joachims (2022) [Optimizing Rankings in Matching Markets]:** *Optimizing rankings for recommendation in matching markets* (WWW '22) [29-31].
6. **Hu, Koren, & Volinsky (2008) [ALS Implicit Collaborative Filtering]:** *Collaborative filtering for implicit feedback datasets* (ICDM '08) [13, 32].
7. **Chen & Guestrin (2016) [XGBoost]:** *XGBoost: A scalable tree boosting system* (KDD '16) [16, 33].

---

💡 *Would you like to explore how MRet's dynamic retention scoring formula \\(\text{Score}(y)\\) or XGBoost retention curve estimator \\(\hat{f}(x, m)\\) could be integrated into your dating platform's candidate profile ranker?*

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

### **Evaluation for Source: *"Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching"***
*(Kishimoto et al., ICLR 2026 / arXiv: `2602.15752`)* [1–2]

---

### **(A) Q1 or Q2 or Both or Neither?**

**Neither.** [1-4]  
* **Q1 (Industry/Production Attribution 2025–2026):** **No.** While submitted in February 2026, this source is a dynamic Learning-to-Rank (LTR) matching algorithm paper evaluated in simulation, rather than an industry multi-touch attribution measurement system [1-3].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper directly optimizes real-time recommendation candidate ranking using learned retention curves \\(f(x, m)\\), but it does **not** perform historical multi-touch sequence attribution over individual user interaction logs [2, 6, 17–18].

---

### **(B) Q2 Class**

**NOT.** [2, 6, 17–18, 24]  
* **Justification:** The paper presents an LTR algorithm (**MRet**) that evaluates candidate profile matches against personalized concave retention curves \\(f(x, m)\\) during online recommendation, without publishing a per-exposure retention credit table or multi-touch attribution model [1, 2, 5, 6].

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction credit.** [1, 2, 5, 6]  
  It evaluates candidates at recommendation time using an individual lower-bound candidate score \\(\text{Score}(y)\\) derived from Jensen and concavity inequalities [18, 22–24]:
  \\[\text{Score}(y) = \frac{1}{A} f(x, m_{1:\tau}(x) + A r(x, y)) + \frac{1}{\alpha_{\max}} \left[ f(y, m_{1:\tau}(y) + \alpha_{\max} r(x, y)) - f(y, m_{1:\tau}(y)) \right]\\]
* **Target Outcome:** **User Retention Probability / Login Continuation Rate** (e.g., next-month login probability \\(f(x, m_{1:\tau}(x))\\) based on cumulative matches \\(m\\)) [1, 5, 7].

---

### **(D) Replacing Last-Touch N7 → Latest Swipes**

* **How it Improves on Last-Touch:** Last-touch heuristics assign 100% of an N7 retention label to the final swipes, ignoring earlier value creation and failing to account for diminishing returns. **MRet** replaces rule-based attribution by learning personalized, concave retention curves \\(f(x, m)\\) where user retention levels off after reaching a satisfactory match count \\(b_x\\) [11, 20–21, 27]. During candidate scoring, MRet calculates the **joint marginal retention gain** across both the swiper and the candidate, naturally redirecting scarce matching opportunities away from popular users whose retention curves have already saturated to under-matched users who need matches to prevent churn [2, 6, 18–21, 33–34].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  * **Match Likelihood (\\(r(x, y)\\)):** Takes estimated match probabilities between swiper \\(x\\) and candidate \\(y\\) as inputs [9, 25–26].
  * **Cumulative Match History (\\(m_{1:\tau}\\)):** Tracks historical cumulative matches for both users [5, 7, 8].
  * **Candidate Rank Scoring:** Rather than crediting recent swipes post-hoc, candidate profiles are ranked by how much an additional match from this swipe will increase the long-term retention probability \\(f(x, m)\\) for both parties [18, 22–24].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Concave Retention Curves & Diminishing Returns:** Incorporates cumulative match history \\(m_{1:\tau}\\) directly into concave user retention functions \\(f(x, m)\\), explicitly modeling that early matches provide significantly higher incremental retention gains than subsequent matches [11, 20–22, 27].
2. **Two-Sided Joint Gain Optimization:** Balances candidate retention gains against receiver retention gains, preventing highly active or popular users from monopolizing matches [6, 18–20, 33].
3. *Note:* The authors explicitly note in Appendix A (Limitations) that the model takes match probabilities \\(r(x, y)\\) as given and does not apply inverse propensity weighting (IPW) or causal debiasing for individual user swiping activity [9, 10].

---

### **(F) Deployment & Production Dataset Evidence**

* **Deployment Status:** Evaluated offline in simulation environments constructed directly from interaction and retention logs of a major Japanese online dating platform [2, 35–37].
* **Quoted Quantitative Results:**
  * **Real-World Online Dating Dataset:** Built from **1,000 male users** and **1,000 female users** forming a \\(1000 \times 1000\\) match matrix (imputed via ALS) [7]. The retention function \\(f\\) was trained via XGBoost on **60,000 real user records** partitioned into 5 k-means clusters [36–37, 74]. Evaluated next-month login retention (February 2025 logins \\(\rightarrow\\) March 2025 logins) over \\(T = 3000\\) timesteps [7, 11, 12]. Also tested on a large-scale setup with **5,000 male and 5,000 female users** (\\(N_x = N_y = 5000\\)) [13].
  * **Real-World Dating Retention Lifts (Figure 6, \\(T=3000\\)):**
    * *Fairness-based Baselines (FairCo / Uniform):* Collapsed to **~52%–55% retention** due to high matrix data sparsity [11].
    * *Max Match Baseline:* Achieved **~64% retention** [11].
    * *MRet (Proposed):* Achieved the highest retention at **~67%–68% retention** [11].
  * **Match Efficiency (Synthetic, Figure 3):** MRet achieved higher cumulative retention than Max Match, FairCo, and Uniform while using only **~70% of the total matches** required by Max Match [14].
  * **Training Sample Scalability (Real Data, Figure 13):** Trained on \\(n = 16,000\\) records, MRet reached **~68% retention**, matching the performance of the oracle upper bound `MRet (best)` [15].
  * **NP-Hard Approximation Accuracy (Small-Scale Synthetic, Figure 12):** Small-scale validation (\\(|X|=|Y|=20, K=3, T=50\\)) proved MRet's retention curve tracks the exact NP-hard **Optimal** ranking curve almost identically while running in **\\(O(N \log N)\\)** time [6, 16].

---

💡 *Would you like to explore how MRet's candidate scoring formula \\(\text{Score}(y)\\) or XGBoost retention curve estimator \\(f(x, m)\\) could be integrated into your dating platform's candidate profile ranker?*

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
**Priority:** see queue.md `G6`
