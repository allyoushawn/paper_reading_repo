# NLM Phase 4-A — q3-last-touch-replacement

Scoped to this-run source_ids (G1–G25). returncode=0 elapsed=156.7s stdout_bytes=69660

### **Candidate Replacement Attribution Architectures for Dating App N7 Retention**

---

#### **1. Counterfactual Removal-Effect Attribution (ALM-MTA)**
* **Source Paper:** *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization* (Liu et al., Kuaishou Technology, ICLR 2026) [1].
* **Exact Credit Object Estimated:** The individualized counterfactual removal drop / uplift:
  \\[\Delta(\tau_j \mid X, T) = g_\theta(X, T) - g_\theta(X, T \setminus \{\tau_j\})\\]
  which measures the exact drop in predicted conversion probability when touchpoint \\(\tau_j\\) is deleted from sequence \\(T\\), identified via front-door adjustment, an adversarially learned proxy mediator \\(M\\), InfoNCE contrastive overlap control, and Inverse Propensity Weighting (IPW) [2-5].
* **Mapping onto Swipe / Match / Conversation:** Individual profile swipes, mutual match events, and sent/received messages act as sequential touchpoints \\(\tau_j\\) in a user's multi-touch journey \\(T = \langle \tau_1, \dots, \tau_L \rangle\\) [2]. The model outputs fractional uplift scores per swipe, match, or chat action [2, 4].
* **What It Does NOT Estimate:**
  * It does **not** estimate N7 retention or active days; its target outcome \\(Y \in \{0, 1\}\\) is content creation/upload in a "Consumption-Drives-Production" (CDP) setting [2, 6].
  * It does **not** rely on backdoor adjustment alone, as system-level confounding is unobserved [3, 6].

---

#### **2. Experiment-Calibrated Data-Driven Attribution (LinkedIn LiDDA)**
* **Source Paper:** *Buyer Journey Insights with Data-Driven Attribution* / *LiDDA: Data Driven Attribution at LinkedIn* (Bencina et al., LinkedIn, 2025) [7, 8].
* **Exact Credit Object Estimated:** Normalized Transformer self-attention weights \\(\alpha_j \in [7]\\) (where \\(\sum \alpha_j = 1.0\\)) from a sequence model \\(P(C \mid EM, EC, S)\\), post-calibrated against controlled marketing A/B holdout experiments and Marketing Mix Models (MMM) [4–5, 9].
* **Mapping onto Swipe / Match / Conversation:**
  * **Swipes:** Top-of-funnel discovery touchpoints (\\(p_0\\)) [7].
  * **Matches:** Mid-funnel intent touchpoints [7].
  * **Conversations:** Bottom-of-funnel conversion touchpoints [7].
  * Attention layers allocate fractional credit across the touchpoint sequence \\(S\\) preceding a retention event [9-11].
* **What It Does NOT Estimate:**
  * It does **not** estimate a causal counterfactual removal effect (\\(\Delta \text{N7}\\) if swipe \\(i\\) is removed); it estimates normalized attention shares calibrated against aggregate experiment/MMM priors [9, 12].
  * It does **not** attribute user retention directly (it attributes B2B/B2C marketing lead and sales conversions) [7, 9, 11].

---

#### **3. Progressive Feedback & Survival/Time-to-Event (Spotify Impatient Bandits & Kuaishou AURO)**
* **Source Papers:**
  1. *Impatient Bandits: Optimizing for the Long-Term Without Delay* (Zhang et al., Spotify / Imperial College London, JMLR 2026) [13].
  2. *AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems* (Xue et al., Kuaishou / NTU, WWW 2025) [14, 15].
* **Exact Credit Object Estimated:**
  * **Impatient Bandits:** Gaussian posterior expectation of an item's 60-day cumulative active days \\(\theta_a \sim \mathcal{N}(\mu_{t,a}, \Sigma_{t,a})\\), updated online as daily progressive active-day feedback vectors \\(Y_u^{(j)} \in \{0, 1\}\\) arrive over 60 days [13].
  * **AURO:** Delayed episode-level user return-time hazard/reward \\(r_t = \lambda \times \text{user return time}\\), propagated via a value-based state abstraction network \\(\phi(s_t)\\) and guarded online exploration [3, 17, 27–30].
* **Mapping onto Swipe / Match / Conversation:**
  * **Impatient Bandits:** A profile card / match recommendation is action \\(a\\); daily user app returns post-match form the progressive daily feedback trace \\(Y_u^{(1)}, Y_u^{(2)}, \dots, Y_u^{(60)}\\) [13].
  * **AURO:** The swiping/messaging session state is \\(s_t\\), ranking weights are action \\(a_t\\), and the time elapsed until the user's next app open is the episode-ending reward \\(r_t\\) [15, 18–19].
* **What They Do NOT Estimate:**
  * They do **not** produce a multi-touch sequence attribution table across historical swipes/matches; they estimate item/policy-level active-day yield or return-time distributions for online ranking/bandits [13].

---

#### **4. Surrogate Save-Revisit & Downstream Rewards (Pinterest Downstream Rewards & Save-Revisit)**
* **Source Papers:**
  1. *Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning* (Wang et al., Pinterest, 2026) [16, 17].
  2. *Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems* (Jiang et al., Pinterest, AAAI 2026) [18].
* **Exact Credit Object Estimated:**
  * **Downstream Rewards:** Expected downstream session trajectory rewards \\(\hat{\mathcal{R}}_{u,t} = \mathbb{E}_{\mathcal{E}}[\mathbb{E}_{\hat{\mathbf{S}}}[\mathbb{R}(\hat{\mathbf{S}})]]\\) combining deeper session engagement (P2P rabbit hole exploration), shallow closeup penalties (\\(<1\text{s}\\) duration), and use-case adoption (\\(\mathbb{R}^{\text{UCA}}\\)) [38–41].
  * **Save-Revisit:** Joint probability of a candidate item being saved (repinned) and subsequently revisited via own-profile impressions or grid-clicks within 0–6 days (\\(1\text{dRevImpre}, 1\text{dRevGrid}, 7\text{dRevGrid}\\)) [113–115].
* **Mapping onto Swipe / Match / Conversation:**
  * **Candidate Profile Card:** Source item \\(x_{u,t}\\) [19].
  * **Right-Swipe / Match:** Equivalent to a "Save" / Repin [18, 20].
  * **Deep Conversation:** Equivalent to entering a deep "P2P rabbit hole" or grid-click revisit [17, 21].
  * **Shallow Right-Swipe:** Right-swiping or viewing a profile for \\(<1\text{s}\\) without sending a message maps to the shallow closeup negative penalty [22].
* **What They Do NOT Estimate:**
  * They do **not** estimate causal removal attribution (MTA) or fractional credit decomposition of individual past swipes on N7 retention [17, 18]. They estimate predictive surrogate reward heads for multi-task rankers [19, 23].

---

#### **5. Interpretable Per-Item Retention Scores (IURO / IURO+)**
* **Source Papers:** *Interpretable User Retention-Oriented Optimization* (Ding et al., Zhihu / WeChat / Tencent, RecSys 2023 [24] & IURO+ ACM TOIS 2026 [25]).
* **Exact Credit Object Estimated:** Item-level UI retention scores \\(s_{ui}\\) generated by a UI Scorer module via Behavior-wise Contrastive Multi-Instance Learning (BCMIL) with instance-level attention \\(y_{\text{MIL}} = \sum \text{softmax}(\cdot) s_{ui}\\) and contrastive "aha item" margin loss \\(L_{\text{CL}}\\) [184–187, 194, 199–200].
* **Mapping onto Swipe / Match / Conversation:**
  * Past swipes, matches, and messaging sessions form the short-term historical interaction sequence (instance bag) [26, 27].
  * High-retention profiles that resulted in deep conversations are identified as "aha items" and assigned high retention weights \\(s_{ui}\\) [24, 28].
* **What It Does NOT Estimate:**
  * It does **not** estimate an identified causal counterfactual removal contrast (\\(\Delta \text{N7}\\) if swipe \\(i\\) is removed) [28, 29]. It uses contrastive multi-instance attention to sharpen retention-correlated "aha items" [28, 30].

---

#### **6. Sleeping Bandits & Recency Decay (Duolingo Recovering Difference Softmax)**
* **Source Paper:** *A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications* (Yancey & Settles, Duolingo, KDD 2020) [31].
* **Exact Credit Object Estimated:** Inverse propensity-weighted (IPW) relative difference score \\(\hat{s}_a = \frac{\hat{\mu}_a^+ - \hat{\mu}_a^-}{\hat{\mu}_a^-}\\) comparing eligible-and-sent vs. eligible-and-not-sent rounds, regularized via empirical Bayes shrinkage and penalized by an exponential recency decay \\(-\gamma \cdot 2^{-d_{a,t}/h}\\) [228–230].
* **Mapping onto Swipe / Match / Conversation:**
  * **Re-engagement Push / Match Reminder / Profile Card:** Arm \\(a\\) [31].
  * **Sleeping Arms (Eligibility):** Profiles or push templates available only under specific user conditions (e.g., active match pending) [32].
  * **2-Hour App Open / Message Sent:** Immediate binary reward \\(r_t \in \{0, 1\}\\) [33, 34].
  * **Recency Decay:** Reduces the score of recently shown profiles or notification templates to prevent fatigue [35].
* **What It Does NOT Estimate:**
  * It does **not** estimate multi-touch sequence attribution across past swipes/matches, nor long-term N7 retention directly (evaluates a short 2-hour window) [33, 34].

---

#### **7. Item-Wise Future-Impact Decomposition & Direct Causal Effect Optimization (ItemA2C & DCEO)**
* **Source Papers:**
  1. *ItemA2C: Future Impact Decomposition in Request-level Recommendations* (Wang et al., Kuaishou, KDD 2024) [36, 37].
  2. *DCEO: Direct Causal Effect Optimization for Long-Term User Value Modeling in E-commerce Search* (Zhang et al., Alibaba / Taobao, 2026) [38, 39].
* **Exact Credit Object Estimated:**
  * **ItemA2C:** Item-decomposed advantage function \\(A(s_t, i_{t,k}, w_{t,k}) = \Psi_w(s_t, i_{t,k}) - \frac{V(s_t)}{K}\\), allocating slate-level future value \\(V(s_{t+1})\\) to individual items via reward-based or model-based adversarial weights \\(w_{t,k}\\) [40-42].
  * **DCEO:** Relative Causal Effect (RCE) of an aggregated, calibrated user-level proxy metric \\(P_u(\theta)\\) on \\(n\\)-day cumulative user value \\(Y_u\\), optimized via an actor-critic model under a 5% relative proxy intervention [39, 43-45].
* **Mapping onto Swipe / Match / Conversation:**
  * **Swipe Deck:** Request slate \\(a_t\\) [46].
  * **Profile Card:** Individual item \\(i_{t,k}\\) [40].
  * **Right-Swipe / Match / Conversation:** Item-wise immediate rewards \\(r_{t,k}\\) [40].
  * **DCEO Context Weights:** Upstream predictions (\\(p\text{Swipe}, p\text{Match}, p\text{Chat}\\)) map to \\(v_{uri}^m\\), and actor context weights \\(w_{ur}^m\\) combine them into an item proxy score [44, 47].
* **What They Do NOT Estimate:**
  * They do **not** estimate post-hoc multi-touch attribution of N7 retention back to past swipes outside the live ranking policy [37, 40, 44].

---

### **Methodological Summary & Incremental Contrast Flag**

> ⚠️ **Flag regarding Incremental Removal Contrast on N7 Retention:**
> **None of the scoped papers estimate the true incremental effect of removing one swipe (or one item) on binary N7 retention.**
> 
> * **ALM-MTA** (Kuaishou 2026) is the **only** paper that estimates the exact counterfactual removal effect (\\(\Delta(\tau_j \mid X, T) = g_\theta(X, T) - g_\theta(X, T \setminus \{\tau_j\})\\)) of deleting a single touchpoint from a user sequence [2, 4]; however, its outcome is **content creation/upload (\\(Y\\))**, *not* N7 retention [2, 6].
> * **DCEO** (Alibaba 2026) estimates the causal effect of a 5% relative increase in an aggregated user-level proxy metric on \\(n\\)-day cumulative GMV/purchases, *not* a per-swipe removal contrast [39, 43, 44].
> * All other candidate frameworks estimate predictive correlation, Transformer attention shares (LiDDA) [9, 10], RL advantage decomposition (ItemA2C) [40, 42], instance-level attention sharpening (IURO) [26, 28], or surrogate reward proxies (Pinterest, Duolingo, Spotify) [13, 17, 23, 33]. None publish an identified causal removal contrast on N7 retention.
