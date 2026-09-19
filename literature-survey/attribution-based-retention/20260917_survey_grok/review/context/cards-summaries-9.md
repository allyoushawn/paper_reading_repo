# Card summaries 9/12 — Summary and Evidence sections of all cards (generated)

### ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization [1]
`2026_ICLR_ALM-MTA_Front-Door-Causal-Multi-Touch-Attribution.md`
**Source:** https://arxiv.org/pdf/2605.08881.pdf  

**Summary.** ### **Part 1: Dating App Retention Project Evaluation**

#### **(A) Alignment: Q1 or Q2 or Both or Neither?**
* **Q1 (Industry/Production Attribution 2025–2026):** **Yes.** Published in May 2026 (`arXiv:2605.08881`), this paper describes a production causal Multi-Touch Attribution (MTA) system deployed at Kuaishou Technology on a recommendation engine serving **400 million Daily Active Users (DAU)** and evaluated over **30 billion training samples** [1-3].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper attributes user content consumption touchpoints to **content creation / video upload behavior (\\(Y \in \{0, 1\}\\))** (the Consumption Drives Production / CDP ecosystem), rather than user retention, active days, or return visits [1, 3, 4].
* **Summary:** **Q1 only.**

---

#### **(B) Q2 Class**
* **Classification:** **NOT** [1, 3, 4].
* **Justification:** The system computes causal multi-touch attribution credit for content creation / video upload conversion events (\\(Y\\)), not for user retention or active days.

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Yes.** It produces a per-touchpoint causal uplift credit score \\(\hat{\Delta}(\tau_j \mid X, T) = g_\theta(X, T) - g_\theta(X, T \setminus \{\tau_j\})\\), defined as the counterfactual drop in predicted upload probability when touchpoint \\(\tau_j\\) is deleted from the user's sequential consumption history [4-6].
* **Target Outcome:** Binary content creation / video upload event (\\(Y \in \{0, 1\}\\)) within the consumption sequence horizon [3, 4].

---

#### **(D) Replacing Last-Touch N7 → Latest Swipes**
* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% credit to the final interaction before conversion, ignoring earlier touchpoints and failing under system/sequence-level unobserved confounding [7]. ALM-MTA calculates the counterfactual marginal uplift of deleting a specific item from the historical sequence using front-door identification and an adversarially learned mediator (\\(\hat{M}\\)), isolating true causal contribution from unobserved confounders (e.g., system recommendation strategies or latent user intent) [5, 7-9].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  * **Sequence Representation:** \\(T = \langle \text{swipe}_1, \text{swipe}_2, \text{match}_1, \text{conversation}_1, \dots \rangle\\) representing the user's sequential in-app interaction journey [3, 4].
  * **Counterfactual Removal Uplift:** Replaces last-touch with counterfactual deletion uplift \\(\Delta(\text{swipe}_j) = P(\text{Retention} \mid \text{do}(T)) - P(\text{Retention} \mid \text{do}(T \setminus \{\text{swipe}_j\}))\\), evaluating how removing a specific swipe or early mutual match reduces the predicted 7-day retention probability [4, 13–14].
  * **Mediator & Front-Door Adjustment:** Uses an adversarial proxy mediator \\(\hat{M}\\) (e.g., intermediate interaction depth, messaging engagement velocity) to block unobserved user activity/intent confounders (\\(W\\)), ensuring that credit assigned to early candidate swipes reflects true causal incrementality rather than selection bias [15, 20, 55–56].

---

#### **(E) Selection-Bias & Confounding Handling**
1. **Front-Door Causal Identification:** Leverages front-door adjustment via a latent mediator \\(M\\) (rendered observable via an adversarially trained proxy \\(Y'\\) invariant to outcome \\(Y\\)) to block unobserved system-level and sequence-level confounders \\(W\\) [5, 8-10].
2. **Inverse Propensity Weighting (IPW):** Reweights observational consumption logs using \\(w(X, T) = 1 / P_{\text{obs}}(T = t \mid X = x)\\) to eliminate backdoor confounding from observed covariates \\(X \to T\\) [17, 21–22].
3. **Contrastive Overlap Control:** Uses InfoNCE-based contrastive learning between touchpoints \\(T\\) and proxy mediator \\(Y'\\) to restrict front-door marginalization to the top-\\(K\\) high-match subset \\(\tau_{\text{high}}\\), maintaining positivity/overlap in high-cardinality treatment spaces [11, 12].

---

#### **(F) Deployed or Production Dataset Evidence**
* **Production Deployment:** Deployed in real-world production at Kuaishou Technology on a recommendation engine serving **400 million Daily Active Users (DAU)** [1, 2, 13].
* **Production Dataset:** Trained on **100 consecutive days of online logs** generating over **30 billion training instances** with a candidate treatment space reaching the **billion level** [1, 3].
* **Quoted Quantitative Results:**
  * **Production Online A/B Test Lifts:**
    * **Daily Active Users (DAU):** **+0.04%** [1, 2, 13].
    * **Daily Active Creators:** **+0.6%** [1, 2, 13].
    * **Unit Exposure Efficiency:** Increased by **670%** (production traffic efficiency **+0.504%**, uploads per user **+0.569%**) [1, 2, 13].
    * **Addressable Creator Scale:** Expanded by **+0.119%**; Producer WAU **+0.566%** [13].
    * **Attributable Upload Coverage:** Expanded by **1.5x** (upload coverage increased from 0.39 to 0.58 under threshold 0.54) [2, 13].
    * **Touchpoint Granularity:** Average attributed touchpoints per upload increased from 2.93 to 7.31 (**2.49x**) [13].
    * **Attribution Accuracy:** Precision increased from **4.32% to 21.88%**, Recall increased from **7.95% to 11.67%** (top-score bucket precision reached **54%**) [13].
  * **Offline Evaluation Metrics (Table 2):**
    * **AUC:** **0.9070** (vs SOTA causalMTA 0.8167, deepMTA 0.7598, DML 0.6498, DESCN 0.5492, LR 0.5102) — **+40% improvement over prior SOTA** [1, 2, 14].
    * **Log Loss:** **0.1384** (vs causalMTA 0.2835, deepMTA 0.4108, LR 0.7833) [14].
    * **gAUC:** **0.8210** (vs causalMTA 0.6752, deepMTA 0.6364, DML 0.5031) [14].
    * **Grouped AUUC (avg AUUC):** **0.8686** (vs causalMTA 0.8493, DESCN 0.8429, DML 0.8421, deepMTA 0.6277, LR 0.4725) — maximum gain of **+0.070** across propensity buckets [1, 2, 14].

---

### **Part 2: Detailed Technical Breakdown of the Source**

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization* [1]
* **Authors:** **Yuguang Liu**\*¹, **Luyao Xia**\*², **Hu Liu**\*¹, **Zhangxi Yan**¹, **Jian Liang**¹, **Han Li**¹, and **Kun Gai**¹ (\*Equal contribution) [1]
* **Affiliations:**
  1. **Kuaishou Technology**, Beijing, China (`{liuyuguang, yanzhangxi, liangjian03, lihan08, yuyue06}@kuaishou.com`) [1]
  2. **The University of Auckland**, Auckland, New Zealand (`luyao.xia@auckland.ac.nz`) [1]
* **Year:** **2026** (May 2026) [1]
* **Venue:** arXiv e-print (`arXiv:2605.08881`) / Conference pre-print [1]

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Multi-touch attribution (MTA) in platform-mediated creator economies (Consumption Drives Production / CDP) aims to quantify how historical user content consumption touchpoints induce creation (video uploads). However, MTA faces three major bottlenecks: (i) absence of explicit ground-truth causal labels, (ii) pervasive multi-source unobserved system- and sequence-level confounding (rendering backdoor adjustments alone insufficient), and (iii) severe non-positivity/overlap violations in billion-scale, high-cardinality treatment spaces [1–2, 15, 16].
* **Key Contributions:**
  1. **ALM-MTA Framework:** Introduces Adversarial Learning Mediator based Multi-Touch Attribution, an extensible front-door causal MTA framework that deconfounds unobserved system-level variables [1, 4–5, 17].
  2. **Adversarial Proxy Mediation:** Renders the latent "inspiration" mediator \\(M\\) observable via a proxy variable \\(Y'\\) while using adversarial gradient reversal to suppress outcome leakage (\\(Y' \to Y\\)), satisfying front-door conditional independence [1, 5, 9, 10].
  3. **Contrastive Overlap Control:** Employs an InfoNCE contrastive module between touchpoints and proxy mediator to restrict front-door marginalization to high-match treatment pairs, preserving positivity in high-cardinality treatment spaces [1, 11, 12].
  4. **Industrial Validation:** Deployed on Kuaishou serving 400M DAU, achieving significant gains in creator activation, attribution coverage, precision, and grouped AUUC [1, 2, 13, 14].

---

#### **(3) Proposed Method or Architecture in Detail**
* **Architecture Pipeline:**
  1. *IPW Reweighting:* Reweights observational consumption logs using Inverse Propensity Weighting \\(w(X, T) = 1 / P_{\text{obs}}(T = t \mid X = x)\\) to handle backdoor confounding from observed covariates \\(X \to T\\) [6, 15].
  2. *Shared Backbone Encoder:* Processes user context features \\(X\\) and chronological touchpoint sequence \\(T\\) [6, 16].
  3. *Weighted ITE Head:* Aggregates touchpoint embeddings with learned weights to output logit for \\(P(Y \mid X, T)\\). Calculates counterfactual removal uplift \\(\hat{\Delta}(\tau_j \mid X, T) = g_\theta(X, T) - g_\theta(X, T \setminus \{\tau_j\})\\) [4, 6].
  4. *Mediator Observation & Adversarial Head:* Supervised by proxy \\(Y'\\) (e.g., music/template/semantic match between consumed and uploaded content). A discriminator attempts to predict upload \\(Y\\) from mediator representation \\(\hat{M}\\); adversarial learning suppresses outcome leakage so \\(\hat{M}\\) contains only causal pathway information \\(T \to M \to Y\\) [6, 9, 10].
  5. *Contrastive Overlap Module:* Computes semantic alignment score \\(\omega(\tau, Y')\\) via InfoNCE loss; restricts front-door marginalization to top-\\(K\\) high-match touchpoints \\(\tau_{\text{high}}\\) [11, 12].
* **Credit Assignment Mechanics:** Credit is assigned **per touchpoint item \\(\tau_j\\)** in the consumption sequence \\(T\\). The credit score equals the counterfactual drop in predicted upload probability when that specific touchpoint is removed from the sequence (\\(\hat{\Delta}(\tau_j)\\)), grounded in front-door causal marginalization [4-6].

---

#### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets:**
  * *Industrial Production Dataset:* 100 consecutive days of online logs from Kuaishou Technology, yielding over **30 billion training instances** across a candidate treatment space at the **billion level** [1, 3].
  * *Public Criteo Conversion Dataset:* 30 days of display ad logs (average touchpoint sequence length 2.68, max length 880) used for external baseline comparisons under cost constraints [25, 74–76].
* **Production Deployment:** Deployed in real-world production at Kuaishou Technology on a recommendation engine serving **400 million Daily Active Users (DAU)** [1, 2, 13].
* **Comparison Baselines:**
  * *Statistical Learning:* Logistic Regression (LR) [14, 17].
  * *Deep Learning:* deepMTA, CAMTA [14, 17, 18].
  * *Causal Learning:* Double Machine Learning (DML), DESCN, causalMTA [14, 17, 18].

---

#### **(5) Key Quantitative Results with Numbers**
* **Offline Benchmark Results (Table 2):**
  * **AUC:** **0.9070** (vs causalMTA 0.8167, deepMTA 0.7598, DML 0.6498, DESCN 0.5492, LR 0.5102) — **+40% improvement over prior SOTA** [1, 2, 14].
  * **Log Loss:** **0.1384** (vs causalMTA 0.2835, deepMTA 0.4108, LR 0.7833) [14].
  * **gAUC:** **0.8210** (vs causalMTA 0.6752, deepMTA 0.6364, DML 0.5031) [14].
  * **Grouped AUUC (avg AUUC):** **0.8686** (vs causalMTA 0.8493, DESCN 0.8429, DML 0.8421, deepMTA 0.6277, LR 0.4725) — maximum gain of **+0.070** across propensity buckets [1, 2, 14].
* **Live Online A/B Test Lifts (Kuaishou 400M DAU Platform):**
  * **Platform DAU:** **+0.04%** [1, 2, 13].
  * **Daily Active Creators:** **+0.6%** [1, 2, 13].
  * **Unit Exposure Efficiency:** Increased by **670%** (production traffic efficiency **+0.504%**, uploads per user **+0.569%**) [1, 2, 13].
  * **Addressable Creator Scale:** **+0.119%**; Producer WAU **+0.566%** [13].
  * **Attributable Upload Coverage:** Expanded by **1.5x** (0.39 \\(\to\\) 0.58) [2, 13].
  * **Touchpoint Granularity:** Average attributed touchpoints per covered upload increased from 2.93 to 7.31 (**2.49x**) [13].
  * **Attribution Accuracy:** Precision increased from **4.32% to 21.88%**, Recall increased from **7.95% to 11.67%** (top-score bucket precision reached **54%**) [13].

---

#### **(6) Limitations, Failure Modes, or Negative Results**
1. **Outcome Leakage in Direct Mediator Observation:** Direct observation of proxy mediator \\(Y'\\) without adversarial learning leads to severe outcome leakage and training instability, causing large loss oscillations and failure to converge (Figure 5a) [30–32].
2. **Backdoor Adjustment Failure:** Standard backdoor methods (DML) achieve an offline AUC of only **0.6498** and UAUC of **0.50**, proving that backdoor adjustment alone cannot resolve unobserved system-level confounding [19].
3. **High Initial Training Loss:** Multi-task learning (MTL) with adversarial and contrastive heads causes higher initial loss during training compared to standard single-task baselines (Figure 5c) [31–33].
4. **Simplifying Assumptions:** Relies on linear aggregability of touchpoint uplift and touchpoint independence assumptions; future work is needed to capture higher-order touchpoint interactions (e.g., via leave-one/two-out inference or multi-head attribution) [20, 21].

---

#### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Yao et al. (2022) [causalMTA]:** *CausalMTA: Eliminating the user confounding bias for causal multi-touch attribution* (KDD '22) [7, 22].
2. **Ren et al. (2018) [Dual-Attention MTA]:** *Learning multi-touch conversion attribution with dual-attention mechanisms for online advertising* (CIKM '18) [23, 24].
3. **Chernozhukov et al. (2018) [DML]:** *Double/debiased machine learning for treatment and structural parameters* (Econometrics Journal) [17, 25].
4. **Zhong et al. (2022) [DESCN]:** *DESCN: Deep entire space cross networks for individual treatment effect estimation* (KDD '22) [17, 26].
5. **Miao, Geng, & Tchetgen Tchetgen (2018) / Tchetgen Tchetgen et al. (2024) [Proximal Causal Inference]:** *Identifying causal effects with proxy variables of an unmeasured confounder* (Biometrika) & *An introduction to proximal causal inference* (Statistical Science) [27-29].
6. **Neuberg (2003) / Pearl (2000) [Front-Door Criterion]:** *Causality: models, reasoning, and inference* & *The front-door criterion in potential outcome framework* [24, 25, 30].
7. **Diemert et al. (2017) [Criteo MTA Dataset]:** *Attribution modeling increases efficiency of bidding in display advertising* (KDD AdKDD Workshop) [25, 31].

---

💡 *Would you like to explore how ALM-MTA's front-door causal adjustment or contrastive overlap module could be adapted to evaluate counterfactual removal uplift for your dating platform's N7 retention ranker?*

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching [1]
`2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md`
**Source:** https://arxiv.org/pdf/2602.15752.pdf  

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**

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

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### A Human-Augmenting Agentic Workflow for Causal Inference (Netflix) — stub
`2026_NetflixBlog_oci-agent_Causal-Inference-Workflow.md`
**Source:** https://netflixtechblog.com/a-human-augmenting-agentic-workflow-for-causal-inference-4623f0a9c5af  

**Summary.** Stub card. NotebookLM, jina.ai, and WebFetch all failed to retrieve the Netflix tech blog post. D4 logs it as a 2026 Netflix engineering post that open-sources `oci-agent` for observational causal inference, with a case study that includes **retention treatment-effect estimation** with overlap/trimming diagnostics.

**Evidence.** Not specified in source (fetch failed). No per-interaction credit table is claimed in the discovery log.

