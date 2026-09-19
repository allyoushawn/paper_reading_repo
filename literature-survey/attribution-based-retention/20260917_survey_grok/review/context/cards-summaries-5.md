# Card summaries 5/12 — Summary and Evidence sections of all cards (generated)

### Learned Ranking Function: From Short-term Behavior Predictions to Long-term User Satisfaction [1]
`2024_RecSys_LRF_Learned-Ranking-Function-YouTube.md`
**Source:** https://arxiv.org/pdf/2408.06512.pdf  

**Summary.** ### **Part 1: Detailed Technical Breakdown of the Source**

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Learned Ranking Function: From Short-term Behavior Predictions to Long-term User Satisfaction* [1]
* **Authors:** **Yi Wu**\*¹, **Daryl Chang**\*¹, **Jennifer She**¹, **Zhe Zhao**¹, **Li Wei**¹, and **Lukasz Heldt**¹ (\*Equal contribution) [1]
* **Affiliations:** **Google / YouTube** (San Bruno, CA & Mountain View, CA, USA) [1, 2]
* **Year & Venue:** Published in **2024** at the *Proceedings of the 18th ACM Conference on Recommender Systems (RecSys ’24), October 14–18, 2024, Bari, Italy* [1]. (arXiv pre-print: `arXiv:2408.06512`, August 2024).

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Large-scale video recommendation systems generate multi-task predictions for short-term user behaviors (e.g., CTR, watch time after click), but combining these predictions into a single ranking score typically relies on heuristic functions or manual tuning (e.g., Bayesian optimization) [1, 3]. These heuristics struggle to scale, adapt to changing platform objectives, or directly optimize for long-term user satisfaction across the entire platform [1, 4]. Furthermore, existing slate optimization frameworks assume zero future rewards when a user abandons a slate, which is unrealistic for platforms where users navigate between recommendation surfaces or return later [5–6, 13].
* **Key Contributions:**
  1. **Learned Ranking Function (LRF):** Formulates slate ranking as a Markov Decision Process (MDP) and proves that maximizing slate-level long-term rewards under a cascade click model with abandonment can be solved via an optimal user-item ranking function [7–9, 17]:
     \\[\text{Score}(u, v) = \frac{p_{\text{clk}}(u, v)}{p_{\text{clk}}(u, v) + p_{\text{abd}}(u, v)} \cdot R_{\text{lift}}(u, v)\text{}\\]
  2. **Lift Loss Formulation (\\(R_{\text{lift}}\\)):** Explicitly models the baseline value of user abandonment (\\(R_{\text{abd}}(u)\\)) and directly estimates \\(R_{\text{lift}}(u, v) = R_{\text{clk}}(u, v) - R_{\text{abd}}(u)\\) using an uplift modeling loss to isolate the true net satisfaction gain of clicking a video versus leaving the slate [5-7].
  3. **Dynamic Linear Scalarization:** Develops a multi-objective constrained optimization algorithm with closed-form quadratic solutions to dynamically balance primary and secondary platform metrics during online inference [7, 22–24].
  4. **Full Production Launch on YouTube:** Fully launched in live production on YouTube's Watch Page, outperforming existing Bayesian-optimized ranking functions [7, 24–26].

---

#### **(3) Proposed Method or Architecture in Detail**
* **MDP Formulation & Cascade Click Model:**
  * User state \\(s = (u, V)\\), where \\(u\\) represents user state and \\(V\\) is a set of \\(n\\) candidate videos [8]. Action \\(\sigma\\) is a permutation ranking of \\(V\\) [9].
  * *Cascade Click Model with Abandonment:* For each position \\(i\\), user either clicks with probability \\(p_{\text{clk}}(u, v)\\), abandons the slate with probability \\(p_{\text{abd}}(u, v)\\), or scrolls to position \\(i+1\\) with probability \\(1 - p_{\text{clk}} - p_{\text{abd}}\\) [15–16].
* **Optimal User-Item Ranking Theorem (Theorem 2.3):**
  * Proves that maximizing cumulative long-term slate reward \\(Q^\pi(s, \sigma)\\) decomposes into ordering candidates by [10]:
    \\[\text{Score}(u, v) = \frac{p_{\text{clk}}(u, v)}{p_{\text{clk}}(u, v) + p_{\text{abd}}(u, v)} \cdot R_{\text{lift}}(u, v)\text{}\\]
  * Extended to multi-objective constrained optimization via weight vector \\(w = (1, w_2, \dots, w_m)\\) [11]:
    \\[\text{Score}(u, v) = \frac{p_{\text{clk}}(u, v)}{p_{\text{clk}}(u, v) + p_{\text{abd}}(u, v)} \cdot \langle R_{\text{lift}}(u, v; \theta), w \rangle\text{}\\]
* **Training Stage:**
  * Uses on-policy Monte Carlo user trajectory buffers [18–19].
  * *Uplift Network Loss:* Directly estimates \\(R_{\text{lift}}\\)-value using MSE loss on clicked items [7]:
    \\[\mathbb{E}_{\tau \sim D, t} \left[ \left| R_{\text{lift}}(u_t, V_{\sigma(c_t)t}; \theta) + R_{\text{abd}}(u_t; \theta) - \text{Reward}(\tau, t) \right|^2 \;\middle|\; c_t > 0 \right]\text{}\\]
  * *Click Network Loss:* Fits \\(p_{\text{clk}}\\) and \\(p_{\text{abd}}\\) using cross-entropy loss over cascade probabilities [7].
* **Credit Assignment Mechanics:**
  * Credit is assigned at the **individual candidate item level** by multiplying conditional click propensity \\(\frac{p_{\text{clk}}}{p_{\text{clk}} + p_{\text{abd}}}\\) by the long-term reward lift \\(R_{\text{lift}}(u, v)\\) [10, 11].
  * It does **not** perform multi-touch sequence attribution over past user interaction logs; rather, it uses uplift modeling (\\(R_{\text{clk}} - R_{\text{abd}}\\)) to score candidate items based on their expected incremental contribution to long-term user satisfaction [6, 7].

---

#### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets & Scale:** Trained on on-policy user trajectory logs collected directly from live YouTube traffic [12, 13].
* **Production Deployment:** Fully launched in live production on **YouTube’s Watch Page** recommendation pipeline [2, 7, 24–25].
* **Comparison Baselines:**
  1. *Previous Production System:* Heuristic ranking function tuned using Bayesian optimization (Google Vizier) [25–26, 31].
  2. *Without Cascade Click Model:* Ranking candidates by \\(\text{CTR} \cdot R_{\text{lift}}\\) [25–26].
  3. *Without Lift Formulation (\\(R_{\text{abd}} = 0\\)):* Maximizing absolute click reward \\(R_{\text{clk}}\\) without subtracting abandonment baseline \\(R_{\text{abd}}\\) [14].
  4. *Two-Model Uplift Baseline:* Predicting \\(R_{\text{clk}}\\) and \\(R_{\text{abd}}\\) separately using two distinct models (\\(R_{\text{click}} - R_{\text{abd}}\\)) [27–28].

---

#### **(5) Key Quantitative Results with Numbers**
* **Initial Deployment vs. Production Control (Table / Section 4.2.1):**
  * LRF outperformed the production Bayesian optimization baseline by **+0.21%** (95% CI `[0.04, 0.38]`) in top-line long-term satisfaction metrics [25–26].
* **Cascade Click Model Impact (Section 4.2.2):**
  * Replacing standard CTR with cascade probability \\(\frac{p_{\text{clk}}}{p_{\text{clk}} + p_{\text{abd}}}\\) yielded a **+0.66%** lift (95% CI `[0.60, 0.72]`) in top-line metrics over control [15].
* **Importance of Lift Formulation (\\(R_{\text{abd}} = R_{\text{clk}} - R_{\text{lift}}\\), Section 4.2.4):**
  * Setting \\(R_{\text{abd}} = 0\\) (ignoring user abandonment value) regressed top-line platform metrics by **-0.46%** (95% CI `[0.43, 0.49]`) [14].
  * *(Insight)*: Although watch page local recommendations increased by **+0.20%** (95% CI `[0.14, 0.26]`), overall platform-wide metrics regressed, proving that ignoring \\(R_{\text{abd}}\\) causes greedy local recommendations that harm long-term retention [14].
* **Direct Lift Loss vs. Two-Model Uplift Baseline (Section 4.2.5):**
  * Direct \\(R_{\text{lift}}\\)-network training outperformed the separate Two-Model baseline by **+0.12%** (95% CI `[0.06, 0.18]`) in top-line metrics [27–28].

---

#### **(6) Limitations, Failure Modes, or Negative Results**
1. **Severe Metric Regression when Ignoring Abandonment (\\(R_{\text{abd}} = 0\\)):** Setting \\(R_{\text{abd}} = 0\\) regressed top-line platform metrics by **-0.46%**, proving that optimizing local item rewards without accounting for user abandonment baseline values harms platform-level retention [14].
2. **Sub-optimality of Separate Two-Model Uplift:** Predicting \\(R_{\text{clk}}\\) and \\(R_{\text{abd}}\\) separately (two-model approach) was inferior to directly predicting \\(R_{\text{lift}}\\) via uplift modeling loss (losing **0.12%** in top-line metrics) [27–28].
3. **Cascade Click Model Assumptions:** Relies on a single-pass cascade click model assumption (users inspect items sequentially from top to bottom and either click, scroll, or abandon), which may not fully hold for non-linear grid layouts or multi-click sessions [15–16].
4. **On-Policy Data Dependency:** Relies on an on-policy Monte Carlo data buffer; off-policy Q-learning and Temporal Difference (TD) learning are noted as future work [18–19, 28–29].

---

#### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Ie et al. (2019) [Ref 13 / SlateQ]:** *SlateQ: A tractable LLM/RL approach to slate recommendation* (IJCAI '19 / NeurIPS '19) [4, 16].
2. **Craswell et al. (2008) [Ref 9 / Cascade Click Model]:** *An experimental comparison of click position-bias models* (WSDM '08) [9, 17, 18].
3. **Covington, Adams, & Sargin (2016) [Ref 8 / YouTube DNN]:** *Deep Neural Networks for YouTube Recommendations* (RecSys '16) [3, 8, 19].
4. **Sutton & Barto (2018) [Ref 16 / RL Book]:** *Reinforcement learning: An introduction* (MIT Press) [20-23].
5. **Golovin et al. (2017) [Ref 11 / Vizier]:** *Google Vizier: A Service for Black-Box Optimization* (KDD '17) [24].
6. **Gutierrez & Gérardy (2017) [Ref 12 / Uplift Modeling]:** *Causal inference and uplift modelling: A review* (Data Science and Pattern Recognition) [7, 25].
7. **Wilhelm et al. (2018) [Ref 18 / DPP Diversity]:** *Practical diversified recommendations on YouTube with determinantal point processes* (CIKM '18) [3, 20, 22, 26].

---

### **Part 2: Dating App Retention Attribution Project Evaluation**

#### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**
* **Neither.**
* **Explanation:**
  * *Q1 (Industry/Production Attribution 2025–2026):* **No.** Published in RecSys 2024 (October 2024), falling outside the 2025–2026 window [1]. Furthermore, it is a slate optimization / candidate ranking framework for video recommendations, not a multi-touch attribution (MTA) measurement system [2, 5–8].
  * *Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):* **No.** LRF predicts long-term user satisfaction lift (\\(R_{\text{lift}}\\)) at candidate ranking time using uplift modeling and cascade click probabilities, rather than attributing N7 retention across past multi-touch user interaction sequences [5-7, 10].

---

#### **(B) Q2 Class**
* **NOT**
* **Justification:** As a slate ranking / RL policy optimization framework (**LRF**), it computes a candidate ranking score \\(\text{Score}(u, v) = \frac{p_{\text{clk}}}{p_{\text{clk}} + p_{\text{abd}}} \cdot R_{\text{lift}}(u, v)\\) to sort candidate profile slates [10, 11], rather than publishing a per-exposure retention credit table or multi-touch sequence attribution model.

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction sequence attribution.**
* **Target Outcome:** At candidate ranking time, the model outputs item-level long-term reward lift \\(R_{\text{lift}}(u, v) = R_{\text{clk}}(u, v) - R_{\text{abd}}(u)\\) [6, 7, 10], representing expected long-term user satisfaction (e.g., total platform watch time / return visits) generated if user \\(u\\) clicks video \\(v\\) versus abandoning the slate [6, 7].

---

#### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**
* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% of an N7 retention label to recent interactions post-hoc, ignoring the baseline value of user abandonment and non-incremental activity. LRF replaces post-hoc last-touch attribution by scoring candidate profiles at ranking time using **uplift modeling against abandonment** [6, 7, 10]:
  \\[\text{Score}(u, v) = \frac{p_{\text{clk}}(u, v)}{p_{\text{clk}}(u, v) + p_{\text{abd}}(u, v)} \cdot \big(R_{\text{clk}}(u, v) - R_{\text{abd}}(u)\big)\text{}\\]
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Candidate Profile Ranking:* Evaluates candidate profile cards \\(v\\) for user \\(u\\) during a swiping session [8, 10].
  2. *Click/Match & Abandonment Propensities:* Predicts right-swipe/match probability \\(p_{\text{clk}}(u, v)\\) and session abandonment probability \\(p_{\text{abd}}(u, v)\\) (the user closing the app / leaving the swipe deck) [15–17].
  3. *Long-Term Retention Lift (\\(R_{\text{lift}}\\)):* Models \\(R_{\text{clk}}(u, v) - R_{\text{abd}}(u)\\), isolating the net 7-day retention gain from a mutual match/conversation resulting from card \\(v\\) relative to the baseline retention \\(R_{\text{abd}}(u)\\) if the user abandons the swiping session [6, 7, 10].

---

#### **(E) Selection-Bias & Confounding Handling**
1. **Cascade Click Model with Abandonment:** Explicitly models position bias and inspection probabilities in candidate slates, decomposing click probability into \\(P_i^{\text{cascade}} = \left(\prod_{j=1}^{i-1} (1 - p_{\text{clk}} - p_{\text{abd}})\right) \cdot p_{\text{clk}}\\) [15–16, 20].
2. **Uplift Loss Formulation:** Uses an uplift loss \\(\mathbb{E}\left[\left|R_{\text{lift}}(u_t, v_t) + R_{\text{abd}}(u_t) - \text{Reward}(\tau, t)\right|^2 \;\middle|\; c_t > 0\right]\\) to directly estimate net differential reward \\(R_{\text{clk}} - R_{\text{abd}}\\), debiasing item scores against user baseline retention [7].

---

#### **(F) Deployment and Production Dataset Evidence**
* **Production Deployment:** Fully launched in live production on **YouTube’s Watch Page** recommendation pipeline [2, 7, 24–25].
* **Quoted Quantitative Results:**
  * Initial LRF deployment vs. Bayesian Optimization production control: **+0.21%** lift (95% CI `[0.04, 0.38]`) in top-line metrics [25–26].
  * Adding Cascade Click Model (\\(\frac{p_{\text{clk}}}{p_{\text{clk}} + p_{\text{abd}}}\\)): **+0.66%** lift (95% CI `[0.60, 0.72]`) in top-line metrics [15].
  * Setting \\(R_{\text{abd}} = 0\\) (ignoring abandonment): **-0.46%** regression (95% CI `[0.43, 0.49]`) in top-line platform metrics [14].
  * Direct \\(R_{\text{lift}}\\)-loss vs. Two-Model Uplift Baseline: **+0.12%** lift (95% CI `[0.06, 0.18]`) in top-line metrics [27–28].

---

💡 *Would you like to explore how YouTube's uplift formulation (\\(R_{\text{clk}} - R_{\text{abd}}\\)) or dynamic linear scalarization could be adapted to balance candidate profile matches against session abandonment risk for your dating platform?*

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Sequential Recommendation for Optimizing Both Immediate Feedback and Long-term Retention
`2024_arXiv_NA_Sequential-Rec-Immediate-Feedback-Long-term-Retention.md`
**Source:** https://arxiv.org/html/2404.03637  

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Sequential Recommendation for Optimizing Both Immediate Feedback and Long-term Retention*
* **Authors:** Not specified in source.
* **Affiliations:** Not specified in source.
* **Year:** **2024** (April 2024, `arXiv:2404.03637v2`).
* **Venue:** arXiv pre-print (`arXiv:2404.03637v2`).

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Standard sequential recommender systems often optimize a single metric—either immediate user feedback (e.g., Click-Through Rate / CTR) or long-term retention (e.g., return frequency) [11–12]. Optimizing solely for immediate feedback leads to myopic recommendations, while focusing only on retention ignores immediate user satisfaction [11–12]. However, adapting Decision Transformers (DT) to multi-reward contexts presents major challenges:
  1. Complex dynamics among diverse user responses make reward design difficult [1].
  2. Interdependencies among multiple objectives introduce training complexity and task interference [1].
* **Key Contributions:**
  1. **DT4IER Framework:** Introduces Decision Transformer for Integrated Engagement and Retention, a framework engineered for long short-term multi-task sequential recommendation scenarios [5–6].
  2. **Adaptive RTG Balancing Module:** Adaptively reweights short-term (CTR) and long-term (return frequency) Return-to-Go (RTG) sequences using user-specific features to bridge immediate feedback and retention [5, 14–15].
  3. **Multi-Reward Encoder & Contrastive Loss:** Implements a high-dimensional encoder for 2D multi-task rewards along with a contrastive learning loss (\\(\mathcal{L}_{\text{contra}}\\)) to prevent predicted action embeddings for distinct rewards from converging too closely [5, 14–16].
  4. **Empirical Validation:** Demonstrates superior performance across three real-world benchmark datasets against state-of-the-art sequential recommenders and multi-task learning models [2, 3].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Problem Formulation & MDP Trajectory**
* Formulates multi-reward sequential recommendation using trajectory representations [8, 11–12]:
  \\[\tau = \left(\hat{\mathbf{R}}_1, \mathbf{s}_1, \mathbf{a}_1, \dots, \hat{\mathbf{R}}_t, \mathbf{s}_t, \mathbf{a}_t, \dots, \hat{\mathbf{R}}_T, \mathbf{s}_T\right)\\]
  * **Session \\(t\\):** Individual timestamp / day in a trajectory of length \\(T\\) [4].
  * **State \\(\mathbf{s}_t\\):** User's historical interaction information (clicked item IDs zero-padded to length \\(H=30\\)) [4].
  * **Action \\(\mathbf{a}_t\\):** Recommendation list containing item IDs of length \\(N=30\\) [4].
  * **Reward \\(\mathbf{r}_t = (r_{s,t}, r_{l,t}) \in \mathbf{R}^2\\):** Short-term indicator \\(r_{s,t}\\) is the Click-Through Rate (CTR) for recommended list \\(\mathbf{a}_t\\) at session \\(t\\); long-term indicator \\(r_{l,t}\\) is return frequency for session \\(t\\) [4].
  * **Return-to-Go (RTG) \\(\hat{\mathbf{R}}_t = [\hat{R}_{s,t}, \hat{R}_{l,t}] = [\sum_{i=t}^T r_{s,i}, \sum_{i=t}^T r_{l,i}]\\):** Un-discounted cumulative short- and long-term rewards from session \\(t\\) to \\(T\\) [4].

#### **Core Architectural Modules**
1. **Adaptive RTG Balancing Block:** Reweights the short- and long-term RTG sequence adaptively using user-specific features [14–15].
2. **State-Action & Reward Embedding Module:** Uses a GRU encoder for state and action sequences (converting discrete item ID sequences of length 30), a high-dimensional encoder for 2D rewards, and positional session encodings [14, 17, 27–29].
3. **Transformer Decision Block:** Uses a unidirectional Transformer with multi-head self-attention, skip connections, and GELU activation to generate action embeddings prompted by the balanced RTG vector [14, 27–28].
4. **Action Decoding Block:** Decodes predicted action embeddings into recommended item ID sequences using a GRU decoder [14, 28–29].
5. **Joint Loss Function:** Combines cross-entropy loss \\(\mathcal{L}_{\text{cross}}\\) (over one-hot encoded item IDs) with a contrastive learning loss \\(\mathcal{L}_{\text{contra}} = -\sum_{\hat{\mathbf{E}}^{A-} \in \Omega^-} D(\hat{\mathbf{E}}^A, \hat{\mathbf{E}}^{A-})\\), where negative samples \\(\Omega^-\\) are low-performing sessions with CTR and retention rewards below 0.6 [16–18]:
   \\[\mathcal{L} = \mathcal{L}_{\text{cross}} + \alpha \mathcal{L}_{\text{contra}}\\]
   (with contrastive loss weight \\(\alpha = 0.1\\)) [5, 6].

#### **Credit Assignment Mechanics**
* Does **not** perform explicit multi-touch credit assignment or fractional attribution to individual items/swipes across a historical sequence.
* Instead, DT4IER models sequential recommendation autoregressively using a Decision Transformer by predicting action embeddings conditioned on a multi-reward Return-To-Go prompt \\(\hat{\mathbf{R}}_t = [\hat{R}_{s,t}, \hat{R}_{l,t}]\\) [8, 10–12].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets:**
  1. **Kuairand-Pure:** Unbiased sequential recommendation dataset featuring random video exposures [3].
  2. **MovieLens-25M (ML-25M):** Large-scale sparse sequential recommendation benchmark [3].
  3. **RetailRocket:** Real-world e-commerce recommendation dataset [3].
* **Production Deployment:** Not specified in source (evaluated offline on benchmark datasets).
* **Comparison Baselines:**
  * **Sequential Recommender Systems (SRSs):** BERT4Rec, SASRec, GRU4Rec [7, 8].
  * **Multi-Task Learning (MTL) Models:** MMoE and PLE (adapted for sequential recommendation using weighted scores) [6, 9].
  * **Decision Transformer Baselines & Ablations:** Standard DT, DT4Rec, and ablation variants (NAW: No Adaptive Weighting, NRE: No Reward Encoder, NCL: No Contrastive Loss) [8, 10, 11].

---

### **(5) Key Quantitative Results with Numbers**
* **Ablation Study Improvements (Section 4.6 & Passage 21):**
  * **Adaptive RTG Balancing (DT4IER vs. NAW):** Achieves improvements of **+1.50% in BLEU**, **+1.90% in NDCG**, and **+0.08% in SB-URS** over the no-adaptive-weighting variant.
  * **Multi-Reward High-Dimensional Embedding (DT4IER vs. NRE):** Outperforms NRE by **+1.80% in BLEU**, **+2.30% in NDCG**, and **+0.19% in SB-URS**.
  * **Contrastive Loss (DT4IER vs. NCL):** Outperforms NCL by **+1.02% in BLEU**, **+1.60% in NDCG**, and **+0.03% in SB-URS**.
* **RTG Prompting Sensitivity Analysis (Section 4.7 & Passages 22–23):**
  * Evaluated RTG prompting proportions from **0.4 to 1.0**.
  * Recommendation accuracy (BLEU and NDCG) increased consistently between **0.4 and 0.8**, reaching peak performance at an RTG proportion of **0.8** (prompting beyond 0.8 showed saturation without additional gains).
* **Model Hyperparameters (Section 4.4 & Passage 20):**
  * Trajectory length \\(T = 20\\); state/action length \\(H = N = 30\\); 2 Transformer layers; 8 heads; embedding size 128; batch size 128; balance term \\(\gamma = 0.5\\); contrastive loss weight \\(\alpha = 0.1\\).

---

### **(6) Limitations, Failure Modes, or Negative Results**
1. **Performance Collapse without High-Dimensional Reward Encoding (NRE Variant):** Naive 2D reward encoding without the dedicated high-dimensional module performed worst across all metrics (BLEU dropped by **1.80%**, NDCG by **2.30%**, SB-URS by **0.19%**), showing that simple scalar/vector reward representations fail to capture task interplay [11].
2. **Action Embedding Convergence without Contrastive Loss (NCL Variant):** Omitting contrastive loss (\\(\mathcal{L}_{\text{contra}}\\)) caused predicted action embeddings for distinct reward prompts to converge too closely, reducing recommendation accuracy (NDCG dropped by **1.60%**) [11].
3. **Saturation Point in RTG Prompting:** Prompting the Decision Transformer with maximum RTG values (1.0) did not yield optimal results; performance saturated at an RTG proportion of **0.8**, indicating that over-prompting does not translate into further performance gains [22–23].
4. **Offline Evaluation Scope:** Evaluated purely offline on benchmark datasets (Kuairand-Pure, ML-25M, RetailRocket) without live online production A/B testing reported in the text [3].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Chen et al. (2021a) [Ref 9]:** *Decision Transformer: Reinforcement Learning via Sequence Modeling* (NeurIPS '21) [10, 12, 13].
2. **Sun et al. (2019) [Ref 51]:** *BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer* (CIKM '19) [7, 8, 14].
3. **Kang & McAuley (2018) [Ref 27]:** *Self-Attentive Sequential Recommendation* (ICDM '18 / SASRec) [7, 8, 15].
4. **Vaswani et al. (2017) [Ref 58]:** *Attention is All You Need* (NeurIPS '17) [7, 12, 14].
5. **Zhao et al. (2023b) [Ref 73]:** *User Retention-oriented Recommendation with Decision Transformer* (WWW '23 / DT4Rec) [8, 10, 16].
6. **Ma et al. (2018b) / Tang et al. (2020) [Refs 38, 57]:** *MMoE* (KDD '18) & *PLE* (RecSys '20) (Multi-Task Learning baselines) [26, 37–38].
7. **Sutton & Barto (2018) / Ie et al. (2019a) [Refs 53, 24]:** *Reinforcement Learning: An Introduction* & *SlateQ* (IJCAI '19) [14, 15, 17].

---

💡 *Would you like to explore how DT4IER's adaptive RTG balancing module or contrastive loss could be adapted to condition candidate profile generation on both immediate match feedback and 7-day retention for your dating app?*

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

