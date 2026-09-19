# NLM Phase 4-A — q1-mechanisms

Scoped to this-run source_ids (G1–G25). returncode=0 elapsed=51.1s stdout_bytes=15468 RETRY after timeout.

### **Systems Producing a Reusable Per-Interaction Credit Table**

#### **1. ALM-MTA**
* **Full Title:** *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization*
* **Company:** **Kuaishou Technology & The University of Auckland**
* **Unit of Credit:** Individual consumed touchpoint / media item (\\(\tau_j\\)) in a user's consumption sequence.
* **Outcome:** Creator content upload / creation behavior (\\(Y \in \{0, 1\}\\)) within the sequence horizon (*consumption-drives-production setting; not retention*).
* **Credit Type:** **Causal identification** (front-door identification criterion, adversarially learned proxy mediator \\(M\\), InfoNCE contrastive overlap control, and Inverse Propensity Weighting).
* **Output Format:** **Reusable per-interaction credit table / labels** (outputs individualized counterfactual removal uplift labels \\(\Delta(\tau_j \mid X, T) = g_\theta(X, T) - g_\theta(X, T \setminus \{\tau_j\})\\) converted into pointwise training targets).

---

#### **2. SILVA / LOTUS**
* **Full Title:** *Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?* (Introducing SILVA Benchmark & LOTUS Framework)
* **Company:** **Taobao & Tmall Group of Alibaba**
* **Unit of Credit:** Individual historical touchpoint / interaction (\\(t_i\\)) in a user behavior path.
* **Outcome:** E-commerce conversion / product purchase (\\(C\\)).
* **Credit Type:** **Heuristic MTA** (LLM-driven pairwise/listwise semantic reasoning over explicit and implicit touchpoint relationships).
* **Output Format:** **Reusable per-interaction credit table / labels** (outputs explicit and implicit touchpoint selection labels and normalized attribution weights \\(\sum w_i = 1.0\\) used as training labels for downstream CVR prediction models).

---

#### **3. Buyer Journey Insights with Data-Driven Attribution (LinkedIn DDA / LiDDA)**
* **Full Title:** *Buyer Journey Insights with Data-Driven Attribution* / *LiDDA: Data Driven Attribution at LinkedIn*
* **Company:** **LinkedIn**
* **Unit of Credit:** Member-level marketing touchpoint (\\(p_t\\)).
* **Outcome:** B2B / B2C marketing lead and sales conversions.
* **Credit Type:** **Heuristic MTA** (Transformer self-attention neural network calibrated with controlled marketing A/B holdout experiments and Marketing Mix Models).
* **Output Format:** **Reusable per-interaction credit table** (outputs normalized attention weight matrices summing to \\(1.0\\) stored with conversion and touchpoint IDs).

---

#### **4. Integrated Marketing Attribution (IMA)**
* **Full Title:** *Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM*
* **Company:** **Lowe's Companies, Inc.**
* **Unit of Credit:** Daily campaign-level media series / ad touchpoint per channel (*daily campaign level, not user-level*).
* **Outcome:** Daily campaign-level incremental sales / revenue.
* **Credit Type:** **Heuristic MTA** (Bayesian regression temporal disaggregation with adstock transformations anchored to weekly Marketing Mix Modeling priors).
* **Output Format:** **Reusable per-interaction credit table** (outputs daily campaign-level attributed incremental sales).

---

#### **5. IURO / IURO+**
* **Full Title:** *Rethinking User Retention Modeling in Recommendation* (RecSys '23) / *Interpretable User Retention-Oriented Optimization* (ACM TOIS '26)
* **Company:** **Zhihu / WeChat (Tencent) / Renmin University of China**
* **Unit of Credit:** Individual user-item interaction / click (\\(i\\)).
* **Outcome:** Next-3-days user retention (clicked and impressed item counts \\(W_u\\) and behavior retention probability).
* **Credit Type:** **Surrogate linkage** (Behavior-wise Contrastive Multi-Instance Learning [BCMIL] with attention and contrastive "aha item" masking).
* **Output Format:** **Reusable per-interaction credit table / scores** (generates explicit user-item retention scores \\(s_{ui}\\) used for interpretability analysis and online ranking).

---

### **Systems Producing a Ranking / RL Policy Only (No Per-Touch Credit Table)**

#### **6. Pinterest Downstream Rewards & Save-Revisit Frameworks**
* **Full Title:** *Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning* / *Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems*
* **Company:** **Pinterest**
* **Unit of Credit:** Individual candidate Pin / item (\\(x_{u,t}\\)).
* **Outcome:** Long-term user retention (WAU / successful session revisits), deeper Pin-to-Pin (P2P) session engagement, shallow closeup avoidance, and use-case adoption.
* **Credit Type:** **Surrogate linkage** (predicting near-term downstream session trajectories \\(\hat{\mathcal{R}}_{u,t}\\) and 0–6 day save-gridclick revisitation under User-Prevalence normalization).
* **Output Format:** **Ranking policy only** (multi-task predicted score heads combined via HyperOPT out-of-graph weights \\(s(x) = \sum w_i p_i(x)\\) for candidate rankers).

---

#### **7. DCEO: Direct Causal Effect Optimization**
* **Full Title:** *DCEO: Direct Causal Effect Optimization for Long-Term User Value Modeling in E-commerce Search*
* **Company:** **Taobao & Tmall Group of Alibaba**
* **Unit of Credit:** Individual item impression (\\((r, i)\\)) within a search request.
* **Outcome:** User-level \\(n\\)-day cumulative outcome (4-day cumulative GMV or purchase count \\(Y_u\\)).
* **Credit Type:** **Causal identification** (actor-critic framework optimizing Relative Causal Effect [RCE] under a 5% relative proxy intervention).
* **Output Format:** **Ranking policy only** (actor \\(f_\theta\\) generates request-specific fusion weights \\(w_{ur}^m\\) to modulate candidate ranking scores).

---

#### **8. ItemA2C (Future Impact Decomposition)**
* **Full Title:** *Future Impact Decomposition in Request-Level Recommendations*
* **Company:** **Kuaishou Technology & USTC**
* **Unit of Credit:** Individual item (\\(i_{t,k}\\)) in a recommended list \\(a_t\\).
* **Outcome:** Cumulative user watch time / interaction depth and next-week user return frequency (retention).
* **Credit Type:** **RL advantage** (decomposes list-level TD target into item-level targets via adversarial or reward-based future-impact weights \\(w_{t,k}\\)).
* **Output Format:** **RL policy only** (decomposes advantage scores into item-level actor gradient updates \\(\mathcal{L}_{\text{actor}}(i_{t,k})\\)).

---

#### **9. GFN4Retention**
* **Full Title:** *Modeling User Retention through Generative Flow Networks*
* **Company:** **Kuaishou Technology & City University of Hong Kong**
* **Unit of Credit:** Individual recommendation step / list action (\\(a_t\\)).
* **Outcome:** Session-level user return time / retention reward \\(R\\) and immediate feedback.
* **Credit Type:** **RL flow** (Generative Flow Network detailed balance loss propagating terminal retention flow \\(F_R(s_T) = R\\)).
* **Output Format:** **RL policy only** (trains forward flow recommendation policy \\(P_F(a_t \mid s_t)\\)).

---

#### **10. Google / YouTube Reward Surrogates & Learned Ranking Function (LRF)**
* **Full Title:** *Surrogate for Long-Term User Experience in Recommender Systems* / *Learned Ranking Function: From Short-term Behavior Predictions to Long-term User Satisfaction*
* **Company:** **Google Research / Brain Team & YouTube**
* **Unit of Credit:** Individual recommended action / candidate video (\\(v\\)).
* **Outcome:** 20-week platform visiting frequency / long-term user satisfaction (watch time and return visits).
* **Credit Type:** **Surrogate linkage** (multiplicative surrogate multipliers in REINFORCE or uplift over abandonment \\(\frac{p_{\text{clk}}}{p_{\text{clk}}+p_{\text{abd}}}(R_{\text{clk}} - R_{\text{abd}})\\)).
* **Output Format:** **Ranking / RL policy only** (modulates policy gradient updates or candidate slate scores).

---

#### **11. Spotify Impatient Bandits**
* **Full Title:** *Impatient Bandits: Optimizing for the Long-Term Without Delay*
* **Company:** **Spotify, Imperial College London, & Columbia University**
* **Unit of Credit:** Individual recommended content item / podcast show (\\(a\\)).
* **Outcome:** Cumulative 60-day active days / return days / listening time.
* **Credit Type:** **Surrogate linkage** (Gaussian Bayesian filter updating posterior beliefs over an item's 60-day stickiness vector \\(\theta_a\\) as daily feedback arrives).
* **Output Format:** **RL policy only** (updates posterior stickiness distributions for Thompson Sampling candidate selection).

---

#### **12. Duolingo Recovering Difference Softmax**
* **Full Title:** *A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications*
* **Company:** **Duolingo**
* **Unit of Credit:** Individual notification template / arm (\\(a\\)).
* **Outcome:** 2-hour lesson completion rate (\\(r_t \in \{0, 1\}\\)) and D1/D7 retention.
* **Credit Type:** **Surrogate linkage** (Horvitz-Thompson IPW relative difference scores \\(\hat{s}_a = \frac{\hat{\mu}_a^+ - \hat{\mu}_a^-}{\hat{\mu}_a^-}\\) with empirical Bayes shrinkage and recency decay).
* **Output Format:** **RL policy only** (selects notification templates via Softmax exploration policy).

---

#### **13. Meta Creator Modeling (Producer Elasticity)**
* **Full Title:** *Long-run User Value Optimization in Recommender Systems through Content Creation Modeling*
* **Company:** **Meta (Facebook)**
* **Unit of Credit:** Content producer / creator distribution boost.
* **Outcome:** Multi-period discounted long-term user value and creator content posting frequency.
* **Credit Type:** **Causal identification** (Heterogeneous Treatment Effects T-Learner / CATE estimation from a 2% producer distribution-boosting A/B experiment).
* **Output Format:** **Ranking policy only** (assigns producer-level uplift scores to boost responsive creators in Feed ranking).

---

#### **14. AURO (Adaptive User Retention Optimization)**
* **Full Title:** *AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems*
* **Company:** **Kuaishou Technology & Nanyang Technological University**
* **Unit of Credit:** Continuous action vector (\\(a_t\\)) for candidate item list ranking.
* **Outcome:** Delayed episode-level user return time (\\(r_t = \lambda \times \text{return time}\\)).
* **Credit Type:** **RL advantage** (Hidden Parameter MDP policy learning with value-based state abstraction loss \\(J(\phi)\\) and guarded online exploration).
* **Output Format:** **RL policy only** (continuous action vector execution for candidate ranking).

---

#### **15. RLUR (Reinforcing User Retention)**
* **Full Title:** *Reinforcing User Retention in a Billion Scale Short Video Recommender System*
* **Company:** **Kuaishou Technology**
* **Unit of Credit:** Recommended list action (\\(a_{i,t}\\)).
* **Outcome:** Cumulative returning time gap minimization (\\(r(s,a) = \text{return time}\\)).
* **Credit Type:** **RL advantage** (infinite-horizon DDPG critic \\(Q_T(s,a)\\) with RND exploration).
* **Output Format:** **RL policy only** (DDPG recommendation policy).

---

#### **16. OCARM (Onboarding Content Distillation Alignment)**
* **Full Title:** *OCARM: Onboarding Content Distillation Alignment for User Re-engagement in Real-Time Bidding*
* **Company:** **Short-Video Platform (Kuaishou)**
* **Unit of Credit:** Ad re-engagement touchpoint / user profile.
* **Outcome:** Revisit frequency (\\(LT_d\\) / D1–D7 return visits).
* **Credit Type:** **Surrogate linkage** (Hierarchical Content Encoder teacher representations distilled into Student User Encoder at bidding time).
* **Output Format:** **Ranking policy only** (retention prediction model for CVR/retention bidding).

---

#### **17. DT4Rec & DT4IER (Decision Transformer for Retention)**
* **Full Title:** *User Retention-oriented Recommendation with Decision Transformer* / *Sequential Recommendation for Optimizing Both Immediate Feedback and Long-term Retention*
* **Company:** **Baidu Inc., City University of Hong Kong, & Academic Benchmarks**
* **Unit of Credit:** Recommended item list action (\\(\mathbf{a}_t\\)).
* **Outcome:** Future log-in frequency, return frequency, and Click-Through Rate (CTR).
* **Credit Type:** **RL flow** (autoregressive sequence generation prompted by adaptive Return-to-Go vectors \\(\hat{\mathbf{R}}_t\\)).
* **Output Format:** **RL policy only** (autoregressive recommendation policy).

---

#### **18. Spotify Deep Twin Network (Incremental Recommendation via Causal Models)**
* **Full Title:** *Incremental Recommendation via Causal Models*
* **Company:** **Spotify**
* **Unit of Credit:** Recommendation impression / candidate item (\\(\mathbf{x}\\)).
* **Outcome:** 60-day active listening days / stream conversion.
* **Credit Type:** **Causal identification** (dual propensity scoring \\(p_1(\mathbf{x})\\) and \\(p_0(\mathbf{x})\\) for recommendation vs organic stream probability).
* **Output Format:** **Ranking policy only** (dual-threshold policy \\(\mathbb{1}[p_1(\mathbf{x}) \ge \theta_1] \cdot \mathbb{1}[p_0(\mathbf{x}) \le \theta_0]\\) filtering non-incremental impressions).

---

#### **19. Matching for Retention (MRet)**
* **Full Title:** *Matching for Retention: Aligning Recommendations with Business Goals in Two-Sided Platforms*
* **Company:** **Academic / Dating Platform Research**
* **Unit of Credit:** Individual match candidate recommendation.
* **Outcome:** User retention / churn probability reduction.
* **Credit Type:** **Surrogate linkage** (evaluates personalized retention curves \\(f(x, m_{1:\tau})\\) to maximize joint retention probability).
* **Output Format:** **Ranking policy only** (learning-to-rank allocation algorithm for match candidates).

---

#### **20. Stratified Expert Cloning (SEC)**
* **Full Title:** *Stratified Expert Cloning for Retention-Aware Recommendation at Scale*
* **Company:** **Kuaishou Technology**
* **Unit of Credit:** Recommended item list action.
* **Outcome:** User retention / active days and return time.
* **Credit Type:** **RL advantage** (imitates hierarchical expert trajectories with adaptive expert selection).
* **Output Format:** **RL policy only** (imitation learning recommendation policy).

---

#### **21. Airbnb Interleaving & Counterfactual Evaluation**
* **Full Title:** *Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking*
* **Company:** **Airbnb**
* **Unit of Credit:** Search impression occurrence / listing touch.
* **Outcome:** Multi-session booking conversion.
* **Credit Type:** **Causal identification** (position-aware counterfactual reward estimators \\(g_i\\) and team drafting interleaving).
* **Output Format:** **Ranking policy only** (offline ranking policy evaluation metric).
