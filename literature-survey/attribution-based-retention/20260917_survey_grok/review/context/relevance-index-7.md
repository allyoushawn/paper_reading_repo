# Relevance index 7/10 — Project Relevance sections of all cards (generated)

### ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization [1]
`2026_ICLR_ALM-MTA_Front-Door-Causal-Multi-Touch-Attribution.md`
**Source:** https://arxiv.org/pdf/2605.08881.pdf  

### **Evaluation for Source: *"ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization"***
*(Liu et al., Kuaishou Technology & The University of Auckland, 2026: `arXiv:2605.08881`)* [1]

---

### **(A) Q1 or Q2 or Both or Neither?**

**Q1 only.** [1-5]
* **Q1 (Industry/Production Attribution 2025–2026):** **Yes.** Published in May 2026 (`arXiv:2605.08881`), this paper describes a production causal Multi-Touch Attribution (MTA) system deployed in real-world production at Kuaishou Technology on a recommendation engine serving **400 million Daily Active Users (DAU)** and evaluated over **30 billion training instances** [1, 4, 5].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper attributes user content consumption touchpoints to **content creation / video upload events (\\(Y \in \{0, 1\}\\))** in the "Consumption Drives Production" (CDP) ecosystem, rather than user retention, active days, or return visits [1-4].

---

### **(B) Q2 Class**

**NOT.** [1-4]
* **Justification:** The system computes causal multi-touch attribution credit for content creation / video upload conversion events (\\(Y\\)), not for user retention, active days, or revisitation [1-4].

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **Yes.** It produces a per-touchpoint causal uplift credit score [3, 6]:
  \\[\hat{\Delta}(\tau_j \mid X, T) = g_\theta(X, T) - g_\theta(X, T \setminus \{\tau_j\})\\]
  defined as the counterfactual drop in predicted upload probability when touchpoint \\(\tau_j\\) is deleted from the user's sequential consumption history [3, 6, 7].
* **Target Outcome:** **Binary content creation / video upload event (\\(Y \in \{0, 1\}\\))** within the consumption sequence horizon [3, 4].

---

### **(D) Replacing Last-Touch N7 → Latest Swipes**

* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% credit to the final interaction before conversion, ignoring earlier touchpoints and failing under system- and sequence-level unobserved confounding [2, 8, 9]. ALM-MTA calculates the counterfactual marginal uplift of deleting a specific item from the historical sequence using front-door identification and an adversarially learned mediator (\\(\hat{M}\\)), isolating true causal contribution from unobserved confounders (e.g., system recommendation strategies or latent user intent) [7, 9-11].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  * **Sequence Representation:** \\(T = \langle \text{swipe}_1, \text{swipe}_2, \text{match}_1, \text{conversation}_1, \dots \rangle\\) representing the user's sequential in-app interaction journey [3].
  * **Counterfactual Removal Uplift:** Replaces last-touch with counterfactual deletion uplift [3, 6, 7]:
    \\[\Delta(\text{swipe}_j) = P(\text{Retention} \mid \text{do}(T)) - P(\text{Retention} \mid \text{do}(T \setminus \{\text{swipe}_j\}))\\]
    evaluating how removing a specific swipe or early mutual match reduces the predicted 7-day retention probability [3, 6, 7].
  * **Mediator & Front-Door Adjustment:** Uses an adversarial proxy mediator \\(\hat{M}\\) (e.g., intermediate interaction depth, messaging engagement velocity) to block unobserved user activity/intent confounders (\\(W\\)), ensuring that credit assigned to early candidate swipes reflects true causal incrementality rather than selection bias [9-12].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Front-Door Causal Identification:** Leverages front-door adjustment via a latent mediator \\(M\\) (rendered observable via an adversarially trained proxy \\(Y'\\) invariant to outcome \\(Y\\)) to block unobserved system-level and sequence-level confounders \\(W\\) [7, 9-11].
2. **Inverse Propensity Weighting (IPW):** Reweights observational consumption logs using \\(w(X, T) = 1 / P_{\text{obs}}(T = t \mid X = x)\\) to eliminate backdoor confounding from observed covariates \\(X \to T\\) [6, 13, 14].
3. **Contrastive Overlap Control:** Uses InfoNCE-based contrastive learning between touchpoints \\(T\\) and proxy mediator \\(Y'\\) to restrict front-door marginalization to the top-\\(K\\) high-match subset \\(\tau_{\text{high}}\\), maintaining positivity/overlap in high-cardinality treatment spaces [15, 16].

---

### **(F) Deployment and Production Dataset Evidence**

* **Production Deployment:** Deployed in real-world production at Kuaishou Technology on a recommendation engine serving **400 million Daily Active Users (DAU)** [1, 5].
* **Production Dataset:** Trained on **100 consecutive days of online logs** generating over **30 billion training instances** with a candidate treatment space reaching the **billion level** [1, 4].
* **Quoted Quantitative Results:**
  * **Live Production Online A/B Test Lifts (Kuaishou Platform):**
    * **Daily Active Users (DAU):** **+0.04%** [1, 5, 17].
    * **Daily Active Creators:** **+0.6%** [1, 5, 17].
    * **Unit Exposure Efficiency:** Increased by **670%** (production traffic efficiency **+0.504%**, uploads per user **+0.569%**) [1, 5, 17].
    * **Addressable Creator Scale:** Expanded by **+0.119%**; Producer WAU **+0.566%** [5].
    * **Attributable Upload Coverage:** Expanded by **1.5x** (upload coverage increased from **0.39 to 0.58** under threshold **0.54**) [5, 17].
    * **Touchpoint Granularity:** Average attributed touchpoints per covered upload increased from **2.93 to 7.31** (**2.49x**) [5].
    * **Attribution Accuracy:** Precision increased from **4.32% to 21.88%**, Recall increased from **7.95% to 11.67%** (top-score bucket precision reached **54%**) [5].
  * **Offline Evaluation Benchmark Performance (Table 2):**
    * **Upload AUC:** **0.9070** (vs SOTA causalMTA **0.8167**, deepMTA **0.7598**, DML **0.6498**, DESCN **0.5492**, LR **0.5102**) — **+40% improvement over prior SOTA** [1, 17, 18].
    * **Log Loss:** **0.1384** (vs causalMTA **0.2835**, deepMTA **0.4108**, LR **0.7833**) [18].
    * **gAUC:** **0.8210** (vs causalMTA **0.6752**, deepMTA **0.6364**, DML **0.5031**) [18].
    * **Grouped AUUC (avg AUUC):** **0.8686** (vs causalMTA **0.8493**, DESCN **0.8429**, DML **0.8421**, deepMTA **0.6277**, LR **0.4725**) — maximum gain of **+0.070** across propensity buckets [1, 17, 18].
  * **Computational Complexity:** Per-forward complexity is **1.31B FLOPs** (0.92B FLOPs for the counterfactual attribution backbone and 0.39B FLOPs for adversarial/contrastive branches) [19].

---

💡 *Would you like to explore how ALM-MTA's front-door causal adjustment or contrastive overlap module could be adapted to evaluate counterfactual removal uplift for your dating platform's N7 retention ranker?*

---

### Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching [1]
`2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md`
**Source:** https://arxiv.org/pdf/2602.15752.pdf  

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

### A Human-Augmenting Agentic Workflow for Causal Inference (Netflix) — stub
`2026_NetflixBlog_oci-agent_Causal-Inference-Workflow.md`
**Source:** https://netflixtechblog.com/a-human-augmenting-agentic-workflow-for-causal-inference-4623f0a9c5af  

- **Answers:** neither Q1 MTA nor Q2 per-touch retention attribution.
- **Q2 class:** NOT — treatment-level observational CATE tooling, not credit assignment to swipes/matches.
- **Last-touch replacement:** not a substitute for per-swipe labels; at most a workflow for later incrementality tests of ranking changes.
- **Transfer rating:** low for Phase-1 labels.

**Low project relevance.**

---

