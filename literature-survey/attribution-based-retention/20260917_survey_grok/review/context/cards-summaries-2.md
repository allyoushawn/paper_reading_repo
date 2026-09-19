# Card summaries 2/12 — Summary and Evidence sections of all cards (generated)

### Long-run User Value Optimization in Recommender Systems through Content Creation Modeling [1]
`2022_arXiv_NA_Long-run-User-Value-Optimization-Meta.md`
**Source:** https://arxiv.org/pdf/2204.11421.pdf  

**Summary.** ### **Part 1: Dating App Retention Attribution Project Evaluation**

#### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**
* **Neither** [1, 2].
* **Explanation:**
  * **Q1 (Industry/Production Attribution 2025–2026):** **No.** Published in 2022 (`arXiv:2204.11421`), which falls outside the 2025–2026 window [1].
  * **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper models content producer supply responses (how giving distribution/engagement to content creators boosts their future posting behavior), rather than attributing user retention, active days, or return visits to individual user interaction sequences [1, 2].

---

#### **(B) Q2 Class**
* **Classification:** **NOT** [1-3].
* **Justification:** The framework scores content producers using a Heterogeneous Treatment Effects (HTE) model (T-Learner / Meta-Learner using GBDTs or Neural Networks) trained on A/B experiment data [2, 3]. It does **not** generate or publish a per-exposure retention credit table or multi-touch attribution model [2, 3].

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction credit** [2, 3].
* **Target Outcome:** **Producer-level uplift score (Individual Treatment Effect / ITE)** measuring the estimated increase in future content creation / posting frequency (\\(\hat{\tau}_i\\)) when a producer receives an engagement/distribution boost [1-3].

---

#### **(D) Replacing Last-Touch N7 → Latest Swipes**
* **How it Improves on Last-Touch:** Last-touch post-hoc rules assign 100% of an outcome to recent interactions, ignoring two-sided ecosystem dynamics and creator supply incentives [2, 4, 5]. This paper shifts the ranking paradigm from myopic short-term user satisfaction optimization (\\(R'_{it}\\)) to two-sided ecosystem long-term value optimization (\\(R''_{it}\\)) by modeling producer feedback loops [2, 4, 7–8].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Two-Sided Ecosystem Dynamic:* In a dating app (swipers/viewers vs. active profile creators/responders), showing extra profile impressions to responsive users (producers who initiate messages or update profiles) encourages them to stay active and generate conversation inventory [2, 4].
  2. *Heterogeneous Treatment Effect Modeling:* An A/B experiment boosts profile distribution for a random 2% sample of active profile creators [2, 6]. A CATE/HTE model (e.g., GBDT Meta-Learner) predicts which profile creators increase their responsiveness and messaging activity when receiving likes/swipes [2, 3].
  3. *Producer Scoring in Ranking:* The ranker boosts profiles of "high-elasticity" creators (users whose engagement encourages future activity and conversation responses), maximizing total discounted long-term user value across all users [2, 7, 8].

---

#### **(E) Selection-Bias & Confounding Handling**
1. **Randomized Producer A/B Experiment:** Randomly selects 2% of content producers to receive a distribution boost to their followers, comparing against a 2% control producer group to eliminate selection bias [2, 6, 9].
2. **Pre-Experiment Covariate Modeling (T-Learner):** Uses pre-experiment producer features \\(\mathbf{x}_i\\) (observed prior to treatment) to fit separate treatment and control outcome models (\\(m_{\text{treatment}}\\), \\(m_{\text{control}}\\)) via GBDTs or Neural Networks, calculating unconfounded Individual Treatment Effects \\(\hat{\tau}_i = m_{\text{treatment}}(\mathbf{x}_i) - m_{\text{control}}(\mathbf{x}_i)\\) [3].
3. **Continuous Holdout for Data Drift:** Maintains a small permanent producer holdout receiving average scores to retrain models periodically (e.g., weekly) and detect model degradation [2, 10].

---

#### **(F) Deployment and Production Dataset Evidence**
* **Production Deployment:** Fully deployed in live production on **Facebook App's Feed ranking system** using Meta's **FbLearner** ML infrastructure [1, 2, 11].
* **Quoted Numbers from the Source:**
  * **A/B Test Scale:** Randomly selected **2% of producers** for treatment distribution boost, compared against **2% control producers** [6].
  * **Engagement Lifts:** Treated producers received a **+26% increase in likes** and a **+9% increase in comments** [6].
  * **Producer Creation Response:** Treated producers increased their content posting frequency by **+0.19% on average** [6].
  * **Retraining Cadence:** Retrained every **1 week** on small holdout producer data [10].

---

### **Part 2: Detailed Technical Breakdown of the Source**

---

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Long-run User Value Optimization in Recommender Systems through Content Creation Modeling* [1]
* **Authors:** **Akos Lada**, **Xiaoxuan Liu**, **Jens Rischbieth**, **Yi Wang**, and **Yuwen Zhang** [1]
* **Affiliations:** **Facebook (Meta)**, Menlo Park / Seattle, USA [1]
* **Year & Venue:** Published in **2022** (submitted April 2022) as an arXiv pre-print (`arXiv:2204.11421`) / Facebook Research [1].

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Standard recommender systems optimize short-term, single-period individual user satisfaction (e.g., immediate clicks or likes) [1, 5]. This myopic focus ignores dynamic two-sided ecosystem spillovers and creator supply incentives [2, 4]. Failing to reward active content producers with engagement causes them to reduce or cease content creation, shrinking future content inventory and degrading long-term platform user value [2, 4, 12].
* **Key Contributions:**
  1. **Microeconomic Proof of Sub-Optimality:** Formalizes multi-period discounted user value maximization and proves (Theorem 1) that short-term 1-period ranking \\(R'_{it}\\) is strictly sub-optimal compared to multi-period ranking \\(R''_{it}\\) whenever inter-temporal content creation spillovers exist [3–12].
  2. **Experimental Causal Machine Learning Framework:** Combines a producer-level distribution-boosting A/B experiment with heterogeneous treatment effects (HTE) machine learning (T-Learner / Meta-Learner using GBDTs or NNs) to estimate individual creator posting elasticity [2, 13–14].
  3. **Production System Deployment:** Deployed in production on **Facebook App's Feed ranking system** via Meta's **FbLearner** pipeline, scoring creators and boosting high-value content supply [2, 16–18].

---

#### **(3) Proposed Method or Architecture in Detail**
* **Two-Step Causal Framework:**
  1. *Experimental Variation:* Runs an A/B test boosting the distribution of 2% of content producers to their followers while keeping 2% in control [2, 6, 9].
  2. *Heterogeneous Treatment Effect Estimation:* Fits separate treatment and control models (\\(m_{\text{treatment}}\\), \\(m_{\text{control}}\\)) using pre-experiment producer features \\(\mathbf{x}_i\\) (e.g., follower count, historical posting frequency) via Gradient Boosted Decision Trees (GBDTs) or Neural Networks [3]. Individual Treatment Effect is calculated as:
     \\[\hat{\tau}_i = m_{\text{treatment}}(\mathbf{x}_i) - m_{\text{control}}(\mathbf{x}_i)\\]
  3. *Production Ranking Integration:* Generates producer-level scores based on \\(\hat{\tau}_i\\) and feeds them into the Feed ranking system [2, 8, 11]. Content from producers who create more valuable content in response to engagement receives a distribution boost [2, 8].
* **Credit Assignment Mechanics:** Does **not** perform per-touchpoint multi-touch attribution [2, 3]. Instead, it assigns a **producer-level uplift score** based on the creator's estimated posting elasticity (\\(\hat{\tau}_i\\)) when receiving an engagement boost [2, 3, 8].

---

#### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets & Scale:** Production user interaction logs and content producer activity logs from the Facebook App [1, 2, 6].
* **Production Deployment:** Fully deployed in live production on **Facebook App's Feed ranking system** via Meta's **FbLearner** ML platform [1, 2, 11]. Maintains a continuous producer holdout receiving average scores for weekly model retraining [2, 10].
* **Comparison Baselines:** Short-term myopic ranking algorithms (\\(R'_{it}\\)) that optimize only 1-period user satisfaction without modeling producer feedback loops [5, 12, 13].

---

#### **(5) Key Quantitative Results with Numbers**
* **A/B Boosting Experiment (Section 4):**
  * Boosted **2% of producers at random**, compared against **2% control producers** [6].
  * Treated producers experienced a **+26% increase in likes** and a **+9% increase in comments** [6].
  * Treated producers increased their content creation/posting frequency by **+0.19% on average** [6].
* **Production Retraining Cadence:** Retrained every **1 week** on small holdout producer data to maintain model freshness and guard against data drift [10].

---

#### **(6) Limitations, Failure Modes, or Negative Results**
1. **Inefficacy in Low-Discount or Homogeneous Environments:** If the discount factor \\(\beta\\) is near zero, or if short-run top creators are identical to long-run top creators, multi-period optimization yields no improvement over myopic short-term ranking [14].
2. **Distribution Volatility & Producer Frustration Risk:** Unstable producer scores cause distribution volatility, making it difficult for creators to predict reach or justify investing effort into high-quality content [8]. To mitigate this, models must rely on stable pre-experiment features [8].
3. **Dependence on Continuous Holdout Data:** Requires maintaining a permanent producer holdout to collect control data for periodic retraining; without weekly retraining, the model degrades [10].
4. **Scope Constraint:** Evaluation was restricted to connected distribution (feed distribution to existing followers) rather than un-connected recommendation surfaces [6].

---

#### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Friedman (2001) [Ref 19]:** *Greedy Function Approximation: A Gradient Boosting Machine* (GBDTs for Meta-Learners).
2. **Kohavi et al. (2013) [Ref 20]:** *Online controlled experiments at large scale* (A/B testing methodology).
3. **Künzel et al. (2019) / Wager & Athey (2018) [Refs 20, 22]:** *Metalearners for estimating heterogeneous treatment effects using machine learning* & *Estimation and inference of heterogeneous treatment effects using random forests*.
4. **Rubin (2011) / Pearl (2009) [Refs 21, 22]:** *Causal inference using potential outcomes* & *Causality* (Potential outcomes framework).
5. **Peysakhovich & Eckles (2018) [Ref 21]:** *Learning causal effects from many randomized experiments using regularized instrumental variables*.
6. **Mas-Colell & Whinston (1995) [Ref 21]:** *Microeconomic Theory* (Microeconomic inter-temporal optimization foundation).
7. **Rumelhart, Hinton, & Williams (1986) [Ref 22]:** *Learning representations by backpropagating errors* (Neural Networks).

---

💡 *Would you like to explore how Meta's producer elasticity model (T-Learner CATE estimation) could be adapted to identify high-response active profile creators for your dating platform's ranker?*

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Incrementality-Focused Messaging Measurement (Netflix) — stub
`2023_NetflixBlog_NA_Incrementality-Focused-Messaging-Measurement.md`
**Source:** https://medium.com/notificationsblog/incrementality-focused-messaging-measurement-all-the-time-everywhere-94ef0c229368  

**Summary.** Stub card. NotebookLM could not ingest the Medium URL; jina.ai and direct WebFetch also failed (Cloudflare / timeout). Discovery notes (D3, D4) describe a Netflix production messaging system with an always-on ~2% message holdback that estimates **incremental downstream viewing** per notification/message, contrasting open/click metrics with incremental watch.

**Evidence.** Not specified in source (fetch failed). D3 records: per-message causal incrementality via randomized withholding — a touchpoint-level incrementality design for **notifications**, not per-feed-item or swipe retention credit.

### Interpretable User Retention Modeling in Recommendation [14]
`2023_RecSys_IURO_Interpretable-User-Retention-Modeling.md`
**Source:** https://dl.acm.org/doi/pdf/10.1145/3604915.3608818  

**Summary.** ### **Part 1: Dating App Retention Project Evaluation**

#### **(A) Alignment: Q1 or Q2 or Both or Neither?**
* **Category:** **Q2 Only** [3, 4, 11–12].
* **Explanation:**
  * *Q1 (Industry/Production Attribution 2025–2026):* **No.** Published in September 2023 (RecSys '23), which falls outside the 2025–2026 window [1, 2].
  * *Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):* **Yes.** The paper generates item/action-level retention scores (\\(s_{ui}\\)) and instance-level attention weights over individual user interactions to explain and predict 3-day user retention [7, 11–12].

---

#### **(B) Q2 Class**
* **Classification:** **PARTIAL** [7, 11–12, 14–17].
* **Justification:** IURO generates item/action-level retention scores (\\(s_{ui}\\)) via a UI Scorer and aggregates them using instance-level attention in Multi-Instance Learning (CMIL/RMIL) to predict 3-day retention [11–14]. The paper explicitly acknowledges and addresses offline-online gaps, unpredictable external factors (e.g., user mood or workload), and lack of explicit per-item retention signals [6, 14–15]. However, it does not formulate an identified causal Multi-Touch Attribution (MTA) model under formal counterfactual graph identification [7, 14–17].

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Yes.** Generates user-item retention scores \\(s_{ui} = \text{FFN}_3(\text{concat}(u_p, u_l, v_i))\\) and instance-level attention weights (\\(\text{softmax}(\text{concat}(u_p, u_l) v_i / \sqrt{d})\\)) for individual user interactions [12–13].
* **Target Outcome:** **Next-3-Day User Retention (\\(y_u\\))**, weighted by future 3-day engagement volume (\\(W_u = a \log(1 + n_c^u) + b \log(1 + n_i^u)\\)) [3]. In online serving, candidate items are scored via \\(r_{ui} = \alpha \cdot \text{CTR}_{ui} + (1-\alpha) s_{ui}\\) [4].

---

#### **(D) Improving on Last-Touch N7 → Latest Swipes**
* **How it Improves Last-Touch:** Last-touch assigns 100% credit to the final swipe before Day 7, ignoring earlier high-value interactions. IURO replaces rule-based last-touch heuristics by computing explicit user-item retention scores (\\(s_{ui}\\)) across all past interactions using Multi-Instance Learning [7, 11–12]. It applies contrastive learning to sharpen "aha items" (high-impact interactions) and uses future behavior alignment (RMIL) as pseudo-causal keys to identify which specific past interactions truly drove return visits [7, 14–17].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Interaction Sequence:* User interaction logs are represented as a sequence of past candidate profile swipes, mutual matches, and 4-way messaging conversations [11–13].
  2. *UI Scorer (\\(s_{ui}\\)):* Evaluates each swipe, match, or messaging interaction based on user demographics (\\(u_p\\)), historical behavior (\\(u_l\\)), and candidate profile features (\\(v_i\\)) [5].
  3. *Aha Item Identification:* CMIL and RMIL identify "aha interactions"—such as a high-affinity mutual match or a deep messaging conversation—that served as the primary drivers of 7-day retention [7, 14–17].
  4. *Online Candidate Ranking:* Candidate profile recommendations are scored via \\(r_{ui} = \alpha \cdot \text{CTR}_{ui} + (1-\alpha) s_{ui}\\), prioritizing profiles that align with past retention-inducing "aha" interactions [4, 6].

---

#### **(E) Selection-Bias & Confounding Handling**
1. **Future Engagement Supervised Weighting (\\(W_u\\)):** Multiplies retention targets by next-3-days cumulative activity (\\(W_u = a \log(1 + n_c^u) + b \log(1 + n_i^u)\\)) to reduce background noise from passive or accidental app opens [3].
2. **Contrastive Multi-Instance Learning (CMIL):** Uses contrastive loss \\(L_{CL} = \max(0, |y_{MIL} - y_{CMIL}^{pos}| - |y_{MIL} - y_{CMIL}^{neg}| + m)\\) to broaden the attention gap between genuine "aha items" and passive background interactions [14–15].
3. **Rationale Alignment via JS Divergence (RMIL):** Uses next-few-day clicks as external pseudo-causal keys to align the attention distribution via Jensen-Shannon divergence (\\(L_{JS}\\)), raising the overlap/consistency of selected "aha items" across initializations from **~35% to ~70%** [7, 8].

---

#### **(F) Deployment and Dataset Evidence**
* **Production Deployment:** Deployed live on a major industrial article recommendation feed (**Tencent WeChat**) serving over **3 million users** in an online A/B test [4].
* **Offline Datasets:** **ZhihuRec 1M** (7,963 users, 81,214 items, 1,271,751 behaviors) and an **Industrial Dataset** (~1 million users, 500,000 items, 97 million behaviors) [9].
* **Quoted Quantitative Results:**
  * **Live Online A/B Test Lifts (Table 3):** **+0.76% next-day retention** and **+0.65% next-three-day retention** [4].
  * **Hit Item Quality & Engagement:**
    * *Average CTR:* **0.129** for hit items vs. **0.082** (Exp Group) and **0.083** (Control Group) [10].
    * *Average Duration:* **98.73s** per item for hit items vs. **18.86s** (Exp Group) and **18.55s** (Control Group) [10].
    * *Filter Bubble Escape:* **34.08% of users** started following novel, surprising categories recommended by IURO in future clicks [10].
  * **Offline Retention AUC Performance (Table 2):**
    * *ZhihuRec 1M:* Base MLP (**0.7180**), IURO(AVG) (**0.5838**), IURO(MIL) (**0.8269**), IURO(MIL+MSS) (**0.8312**), IURO(CMIL+MSS) (**0.8437**), IURO(RCMIL+MSS) (**0.8445**) [11].
    * *Industrial Dataset:* Base MLP (**0.6827**), IURO(AVG) (**0.6732**), IURO(MIL) (**0.7209**), IURO(MIL+MSS) (**0.7255**), IURO(CMIL+MSS) (**0.7291**), IURO(RCMIL+MSS) (**0.7301**) [11].
  * **Explicit User Feedback Analysis (Table 1 & Section 4.1):**
    * **69% of survey participants** claim they return if items are relaxing and stress-relieving [12].
    * *Relative Retention Rates by Negative Feedback Reason:* "Not interested in items" (**35.38% next-day / 36.45% next-3-day** — lowest retention), "Low-quality content" (**90.29% / 91.78%**), "Advertising promotion" (**91.89% / 93.06%**), "Poor diversity" (**97.33% / 98.36%**), "Exaggerating titles" (**98.98% / 99.05%**), "Don't like author/content" (**102.29% / 102.03%**), "Repeated recommendation" (**113.51% / 108.07%**) [13].

---

### **Part 2: Detailed Technical Breakdown of the Source**

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Interpretable User Retention Modeling in Recommendation* [14]
* **Authors:** **Rui Ding**¹, **Ruobing Xie**\*², **Xiaobo Hao**², **Xiaochun Yang**\*¹, **Kaikai Ge**², **Xu Zhang**², **Jie Zhou**², and **Leyu Lin**² (*\*Corresponding Authors*) [14]
* **Author Affiliations:**
  1. **Northeastern University**, Shenyang, China (`ruiding.neu@outlook.com`, `yangxc@mail.neu.edu.cn`) [14]
  2. **WeChat, Tencent**, Beijing, China (`{xrbsnowing, rolyhao, kavinge, xuonezhang, withtomzhou, goshawklin}@tencent.com`) [14, 15]
* **Year & Venue:** Published in **2023** at the *Seventeenth ACM Conference on Recommender Systems (RecSys ’23), September 18–22, 2023, Singapore* [1, 2].

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Recommender systems primarily optimize for immediate accuracy metrics (e.g., CTR), which fails to capture long-term user satisfaction and retention [2, 15]. Existing retention modeling efforts focus on predictive accuracy via sequential decision-making/RL, treating retention as a black box without identifying *why* users return or *which specific behaviors* drive return visits [2, 16-18].
* **Key Contributions:**
  1. **IURO Framework:** Introduces an interpretable user retention-oriented optimization framework designed to discover and utilize explicit retention factors [6, 19].
  2. **Contrastive Multi-Instance Learning (CMIL):** Combines a UI Scorer module with instance-level attention and contrastive learning to isolate rare, high-impact "aha items" [7, 12–15].
  3. **Rationale Multi-Instance Learning (RMIL) & Distribution Alignment:** Uses future clicked items as pseudo-causal keys to supervise CMIL via Jensen-Shannon (JS) divergence loss, improving selected "aha item" consistency across initializations from **~35% to ~70%** [7, 15–17].
  4. **Explicit User Feedback Analysis:** Quantifies interpretable retention factors through user surveys and explicit negative feedback analyses across 1M daily logs [12, 19, 20].
  5. **Billion-Scale Industrial Deployment:** Validates online retention gains (+0.76% next-day retention) on Tencent WeChat article feed serving millions of users [4, 10, 21].

---

#### **(3) Proposed Method or Architecture in Detail**
* **UI Scorer Module:** A 3-layer feedforward network (\\(s_{ui} = \text{FFN}_3(\text{concat}(u_p, u_l, v_i))\\)) generating user-item retention scores, where \\(u_p\\) represents static user attributes, \\(u_l\\) represents long-term behaviors, and \\(v_i\\) represents short-term behavior (offline) or candidate item features (online) [5].
* **Multi-Instance Learning (MIL) Aggregation:**
  \\[y_{MIL}^u = \sum_{i \in sequence} \text{softmax}\left(\frac{\text{concat}(u_p, u_l) v_i}{\sqrt{d}}\right) s_{ui}\\]
  Supervised by \\(L_{MIL} = \sum_u W_u \cdot \text{MSE}(y_u, y_{MIL}^u)\\), where \\(W_u = a \log(1 + n_c^u) + b \log(1 + n_i^u)\\) incorporates future 3-day engagement volume [3, 22].
* **Contrastive Multi-Instance Learning (CMIL):** Applies contrastive loss \\(L_{CL} = \sum_u \max(0, |y_{MIL}^u - y_{CMIL,pos}^u| - |y_{MIL}^u - y_{CMIL,neg}^u| + m)\\) by masking low- and high-attention items to sharpen "aha item" selection [7, 22].
* **Rationale Multi-Instance Learning (RMIL) & Alignment:** Uses future clicked items (next few days) as external pseudo-causal keys to find historical rational behaviors (top 5 by dot product with mean future click vector) [7, 8]. Aligns CMIL and RMIL attention distributions via JS-divergence loss \\(L_{JS} = \mathbb{E}_u [\text{JS}(y_{MIL}^u \parallel y_{RMIL}^u)]\\) [8]. Total loss: \\(L = \alpha_1 L_{MIL} + \alpha_2 L_{CL} + \alpha_3 L_{RMIL} + \alpha_4 L_{JS}\\) [8].
* **Online Serving Integration:** Candidate items are reranked using \\(r_{ui} = \alpha \cdot \text{CTR}_{ui} + (1-\alpha) s_{ui}\\), bridging offline instance-level attention training with online single-item scoring [4, 6].

---

#### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets:**
  * **ZhihuRec 1M:** 7,963 users, 81,214 items, 1,271,751 behaviors over 10 days (first 7 days train, last 3 days test) [9].
  * **Industrial Dataset (Article Feed):** ~1 million users, 500,000 items, 97 million behaviors over 18 days [9].
* **Production Deployment:** Live online A/B testing on Tencent WeChat article recommendation feed serving over 3 million users [4].
* **Comparison Baselines:**
  * **Base MLP:** 3-layer MLP on static features + all behaviors (infeasible online without UI scorer) [23].
  * **IURO(AVG):** Assigns uniform impact weights across all historical items [23].
  * **IURO(MIL):** Incorporates instance-level attention without contrastive or rationale losses [23].
  * **IURO(MIL+MSS):** MIL + future cumulative feature supervised signals (\\(W_u\\)) [23].
  * **IURO(CMIL+MSS):** CMIL + \\(W_u\\) [23].
  * **IURO(RCMIL+MSS):** Full IURO framework with rationale alignment [23].

---

#### **(5) Key Quantitative Results with Numbers**
* **Offline User Retention Prediction AUC (Table 2):**
  * *ZhihuRec 1M:* Base MLP (**0.7180**), IURO(AVG) (**0.5838**), IURO(MIL) (**0.8269**), IURO(MIL+MSS) (**0.8312**), IURO(CMIL+MSS) (**0.8437**), IURO(RCMIL+MSS) (**0.8445**) [11].
  * *Industrial Dataset:* Base MLP (**0.6827**), IURO(AVG) (**0.6732**), IURO(MIL) (**0.7209**), IURO(MIL+MSS) (**0.7255**), IURO(CMIL+MSS) (**0.7291**), IURO(RCMIL+MSS) (**0.7301**) [11].
* **Live Online A/B Testing Results (>3M Users, Table 3):**
  * **Next-day retention:** **+0.76%** relative gain [4].
  * **Next-three-day retention:** **+0.65%** relative gain [4].
* **Hit Item Metrics & User Interest Expansion:**
  * *Hit Item CTR:* **0.129** (vs Exp Group **0.082** and Control Group **0.083**) [10].
  * *Hit Item Duration:* **98.73s** per item (vs Exp Group **18.86s** and Control Group **18.55s**) [10].
  * *Filter Bubble Escape:* **34.08% of hit users** started following novel, surprising categories recommended by IURO in future clicks [10].
* **Robustness across Initializations:** "Aha item" selection overlap increased from **~35%** (CMIL alone) to **~70%** (IURO with RMIL rationale supervision) [7, 8].

---

#### **(6) Limitations, Failure Modes, or Negative Results**
1. **Severe Degradation of Uniform Attribution:** `IURO(AVG)` degraded performance significantly on ZhihuRec (AUC dropped from **0.7180 down to 0.5838**), proving that uniform attribution over historical items actively harms retention modeling [11].
2. **Initialization Instability in Naive CMIL:** Without RMIL rationale supervision, CMIL selected "aha items" with only **~35% overlap** across different random parameter initializations due to parameter randomness [7].
3. **Requirement for Post-Session Behavioral Logging:** Requires future session logging (\\(W_u\\) and future clicks in RMIL) during offline training to construct supervised target weights and rationale keys [3, 7, 8].
4. **Heuristic Online Score Blending:** Online reranking relies on a linear combination parameter \\(\alpha\\) (\\(r_{ui} = \alpha \cdot \text{CTR}_{ui} + (1-\alpha) s_{ui}\\)) which must be manually tuned by online systems [4].

---

#### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Cai et al. (2023) [Ref 1]:** *Reinforcing User Retention in a Billion Scale Short Video Recommender System* (WWW '23) [24].
2. **Zhao et al. (2023) [Ref 36]:** *User Retention-oriented Recommendation with Decision Transformer* (WWW '23) [25].
3. **Wang et al. (2022) [Ref 25]:** *Surrogate for Long-Term User Experience in Recommender Systems* (SIGKDD '22) [26].
4. **Kapoor et al. (2014, 2015) [Refs 18, 19]:** *A hazard based approach to user return time prediction* (SIGKDD '14) & *Just in Time Recommendations: Modeling the Dynamics of Boredom in Activity Streams* (WSDM '15) [27, 28].
5. **Chandar et al. (2022) [Ref 4]:** *Using Survival Models to Estimate User Engagement in Online Experiments* (WWW '22) [29].
6. **Chen et al. (2018) / Yu et al. (2019, 2021) [Refs 5, 30, 31]:** *Learning to Explain: An Information-Theoretic Perspective on Model Interpretation* (ICML '18) & *Rethinking Cooperative Rationalization* (EMNLP '19 / NeurIPS '21) [29-31].
7. **Vaswani et al. (2017) [Ref 23]:** *Attention is All you Need* (NeurIPS '17) [32].

---

💡 *Would you like to explore how IURO's Contrastive Multi-Instance Learning (CMIL) or UI Scorer module (\\(s_{ui}\\)) could be adapted to score past candidate swipes, mutual matches, and conversations for your dating platform's N7 retention ranker?*

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

