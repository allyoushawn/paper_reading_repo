# Related-notebook Q2 queries (NOT ground truth)

NotebookLM answers from related surveys. These notebooks over-classify RL/LTR
retention optimizers as TRUE attribution. **Ground truth for this run:** D3
rubric in `discovery/D3_retention_attribution.md` plus this folder's cards.
RL-for-retention (RLUR, GFN4Retention, AURO, SEC, OCARM, MRet) is not
automatically attribution; say whether the method produces per-interaction
credit for a delayed retention label.

Do not cite papers that are only in these related notebooks unless a card
exists under this run's `read-papers/`.

## unified-ltv-ranking-dating (`67046a44-7490-4fe5-b54a-3f39ef37fdd3`)

Here is a breakdown of the papers in your sources that address **user retention or long-term engagement attribution** to individual recommendations, items, notifications, or actions. 

---

### **1. GFN4Retention (Kuaishou & City University of Hong Kong, KDD 2024)**
* **Title:** *Modeling User Retention through Generative Flow Networks* [1, 2].
* **Company:** Kuaishou Technology & City University of Hong Kong [1].
* **Method:** Formulates session-based recommendation as a trajectory generation task using Generative Flow Networks (GFNs) [3]. It uses a Detailed Balance (DB) loss and an integrated reward function (\\(R = R_{\text{retention}} \cdot e^{\alpha \sum r_{\text{immediate}}}\\)) to flow-match intermediate states [3-5].
* **Credit Type:** **Per-item / per-action credit** (step-wise retention attribution) [3, 4]. A backward flow estimator back-propagates the end-of-session macro retention reward to every intermediate recommendation step in continuous action space [3, 4].
* **Deployed:** **Yes.** Deployed in the multi-stage ranking ensemble modules of Kuaishou’s short-video platform [6, 7].
* **True Multi-Touch Retention Attribution:** **Present.** It explicitly models step-wise retention attribution by back-propagating terminal session retention signals through backward probabilistic flows across intermediate item actions [3, 4, 8].

---

### **2. RevisitMTL / Save-Revisit-Retain (Pinterest, AAAI 2026)**
* **Title:** *Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems* [9].
* **Company:** Pinterest Inc. [9].
* **Method:** A multi-task learning (MTL) ranking framework that establishes a surrogate causal attribution process linking in-app "save" (repin) actions to subsequent cross-session and cross-day revisitations (0–6 day window, grid-clicks and board impressions) [9-12].
* **Credit Type:** **Per-item credit** [11, 12]. It adds a revisitation head directly to the multi-task item ranker, predicting the probability (\\(c_{\text{RP\&RV}}\\)) that a candidate Pin will be saved and revisited [11, 12].
* **Deployed:** **Yes.** Deployed on Pinterest’s Related Pins surface serving 500M+ active users [9].
* **True Multi-Touch Retention Attribution:** **Present** (in surrogate form). It explicitly establishes causal attribution linking individual saved items to subsequent cross-session revisitations within a 0–6 day window [9-11, 13].

---

### **3. Alibaba PDQ-LTV Framework (Alibaba, WWW 2026)**
* **Title:** *A Long-term Value Prediction Framework In Video Ranking* [14, 15].
* **Company:** Alibaba Group & Tsinghua University [15].
* **Method:** A ranking-stage LTV framework combining Position-aware Debias Quantile (PDQ) normalization with a learnable multi-dimensional attribution module (contextual, behavioral, content, author signals) and cross-temporal author modeling (\\(S_{\text{auth}}^{(t)}\\) over 7 days) [15-18].
* **Credit Type:** **Per-item credit** [17, 19, 20]. Decomposes subsequent session watch time (\\(S_j = \sum c_{ji} t_i\\)) back to specific exposed items using learnable multi-dimensional causal weights while zeroing out unrelated noise [19-21].
* **Deployed:** **Yes.** Deployed at billion-scale on the Taobao App production video ranker [22-24].
* **True Multi-Touch Retention Attribution:** **Present.** It incorporates explicit multi-dimensional causal attribution to credit subsequent intra-session watch time and multi-day author return visits back to individual item exposures [16, 17, 19-21].

---

### **4. Spotify Podcast RL / Maystre et al. (Spotify & Columbia, 2024)**
* **Title:** *Optimizing Audio Recommendations for the Long-Term: A Reinforcement Learning Perspective* [25].
* **Company:** Spotify & Columbia University [25].
* **Method:** Offline RL framework utilizing a content-relationship user state (\\(Z_t\\)) and structured \\(Q\\)-function decomposition that estimates item-level "stickiness" models (expected active return days to item \\(a\\) over a 60-day horizon post-discovery) [26-34].
* **Credit Type:** **Per-item credit** [29-34]. Attributes expected long-term active return days directly to individual item exposures via item-level stickiness vectors (\\(\theta_a\\)) [30-34].
* **Deployed:** **Yes.** Deployed globally at Spotify on Home banner and podcast discovery shelves [25, 35-37].
* **True Multi-Touch Retention Attribution:** **Present.** The item-decomposed \\(Q\\)-function assigns credit for changes in projected 60-day item stickiness directly to individual recommendation events [27, 30, 38, 39].

---

### **5. RLUR (Kuaishou, WWW 2023)**
* **Title:** *Reinforcing User Retention in a Billion Scale Short Video Recommender System* [40, 41].
* **Company:** Kuaishou Technology [40, 41].
* **Method:** Infinite-horizon request-based Markov Decision Process (MDP) with dual critics (Retention Critic \\(Q_T\\) estimating return-to-app time interval, Immediate Critic \\(Q_I\\) for in-session engagement), quantile reward normalization, and soft off-policy regularization [40, 42-44].
* **Credit Type:** **Policy-level RL objective** [8, 40, 45, 46]. It outputs continuous action vectors to weight ranking score ensembles per request [45]. The authors explicitly note that because retention is a macro-behavior, decomposing retention rewards directly to individual items or lists is unresolved in their formulation [8, 47].
* **Deployed:** **Yes.** Deployed at scale on Kuaishou's short-video platform [40].
* **True Multi-Touch Retention Attribution:** **Absent.** [8, 47] (Optimizes request-level MDP ranking weights over the session without decomposing item-level retention credit) [8, 40, 45].

---

### **6. AURO (Kuaishou & NTU, WWW 2025)**
* **Title:** *AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems* [48, 49].
* **Company:** Kuaishou Technology & Nanyang Technological University [48, 49].
* **Method:** Adaptive continuous-action RL framework for non-stationary environments using a value-based contrastive loss to learn state abstractions, combined with rejection sampling and optimism under uncertainty [49, 50].
* **Credit Type:** **Policy-level RL objective** [51, 52]. Generates \\(k\\)-dimensional continuous action vectors to dynamically weight scoring models at serving time [51].
* **Deployed:** **Yes.** Evaluated online and deployed at Kuaishou [49, 50].
* **True Multi-Touch Retention Attribution:** **Absent.** (Optimizes policy-level continuous action vectors targeting session-end return time) [51, 52].

---

### **7. SEC (Kuaishou Ecosystem / KuaiRand, 2025)**
* **Title:** *Stratified Expert Cloning for Retention-Aware Recommendation at Scale* [53, 54].
* **Company:** Video platforms (Kuaishou / KuaiRand ecosystem research) [53, 55, 56].
* **Method:** Imitation learning framework using multi-level expert stratification (stratifying users by retention history into expert tiers), behavior cloning per tier, adaptive expert policy selection, and action entropy regularization [54, 57, 58].
* **Credit Type:** **Policy-level imitation learning objective** [57, 58]. Learns specialized recommendation policies by cloning trajectories of high-retention expert user groups [57, 58].
* **Deployed:** **Yes.** Deployed in large-scale online A/B tests on two major video platforms [55].
* **True Multi-Touch Retention Attribution:** **Absent.** (Imitates high-retention user trajectories via behavior cloning without calculating multi-touch attribution) [54, 57].

---

### **8. OCARM (Short-Video Platform, 2026)**
* **Title:** *Onboarding Content Augmented Retention Modeling* [59, 60].
* **Company:** Short-video platform / Real-Time Bidding (RTB) advertising researchers [59, 61, 62].
* **Method:** Two-stage distillation-aligned framework. Stage 1 intentionally allows feature leakage during training by encoding future onboarding content (\\(x_c\\), up to \\(D\\) days) via hierarchical attention (HAE) as a teacher signal for retention prediction (\\(LT_d\\)) [60, 61, 63, 64]. Stage 2 trains a user encoder (SFE) on observable pre-conversion features to approximate the teacher representation via distillation alignment [60, 64, 65].
* **Credit Type:** **Policy-level / user-level prediction objective** [61, 62]. Predicts overall user revisit frequency (\\(LT_d\\) over \\(d\\) days) for RTB bidding decisions [61, 62].
* **Deployed:** **Yes.** Validated on offline industrial logs and deployed in online RTB advertising systems [59, 62, 66].
* **True Multi-Touch Retention Attribution:** **Absent.** (Attributes retention to overall user/ad context for bidding rather than item-level multi-touch attribution) [61, 67].

---

### **9. Multi-Attribution Learning / MAL (Alibaba, CIKM 2025)**
* **Title:** *See Beyond a Single View: Multi-Attribution Learning Leads to Better Conversion Rate Prediction* [68-71].
* **Company:** Taobao & Tmall Group of Alibaba [68].
* **Method:** Multi-task framework (Attribution Knowledge Aggregator + Primary Target Predictor) co-training CVR under multiple attribution rules (First-Click, Last-Click, Linear, and Data-Driven MTA) using Cartesian-based Auxiliary Training (CAT) [69, 70, 72-74].
* **Credit Type:** **Per-action / per-touchpoint credit** [69, 75, 76]. Assigns conversion credit across historical ad click touchpoints using multi-touch attribution (MTA) mechanisms [69, 75, 76].
* **Deployed:** **Yes.** Deployed in Alibaba's display advertising system [70, 77-79].
* **True Multi-Touch Retention Attribution:** **Present** (for ad conversion paths across touchpoints) [69, 75, 80].

---

### **Note on FID**
* **FID Status:** **Absent in sources.** The acronym **FID** as a retention-attribution method does not appear in your notebook's source materials.

## two-sided-market-balancing-dating (`d3071ac8-16ef-4460-8991-7701679974c8`)

Based on an analysis of the papers in your notebook, here is how each relevant study models user retention or days-active, whether it assigns per-interaction credit, and its classification regarding **attribution of retention to specific individual actions, matches, or exposures**:

---

### 1. *Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching* (Kishimoto et al., ICLR 2026 / arXiv:2602.15752) [1, 2]

* **How Retention is Modeled:** This paper formally defines the problem of maximizing user retention on two-sided matching platforms (such as online dating and recruiting) [3]. It introduces **Matching for Retention (MRet)**, a dynamic learning-to-rank (LTR) algorithm that learns personalized **retention curves** for each user based on their profile and interaction history [3]. MRet dynamically adapts recommendation lists by evaluating the marginal **retention gains** (expected increase in days-active or retention probability) for both the user receiving the recommendation and the candidates being recommended [3].
* **Per-Interaction Credit:** **YES.** MRet explicitly calculates the per-candidate/per-interaction marginal retention gain for every potential match or profile exposure [3].
* **MRet Callout:** **PRESENT.** This paper is the primary work that introduces and evaluates **MRet** [3].
* **Classification:** **TRUE attribution** of retention to specific individual actions/matches/exposures [3].

---

### 2. *The Dating Heuristic: A Provably Strong Matching Algorithm for Dating Platforms* (Rios & Torrico, 2023/2025 / arXiv:2308.02584) [4, 5]

* **How Retention is Modeled:** The authors study dynamic profile display policies (e.g., the Integral Dating Heuristic, `DH-int`) [6]. They model history-dependent user behavior where past experiences—such as the number of recent matches or time on the app—alter future liking probabilities [7, 8]. Specifically, they evaluate a **Disengagement** specification (\\(\gamma(\sigma) = \gamma t\\)) where users naturally disengage/churn as time elapses, and a **Linear Match/Threshold** specification (\\(\gamma(\sigma) = \gamma |M|\\)) where accumulating too few or too many matches alters liking rates due to frustration or app fatigue [8, 9].
* **Per-Interaction Credit:** **NO.** While it models how macro-level user state (e.g., total matches or time elapsed) alters future liking and disengagement probabilities, it does **not** decompose overall retention into per-interaction credit assignment for individual profile exposures [7, 8].
* **MRet Callout:** **NOT PRESENT.**
* **Classification:** **PARTIAL attribution** (it models history-dependent disengagement/retention dynamics at the user-state level over time, but does not assign credit to individual actions) [7, 8].

---

### 3. *Creator-Side Recommender System: Challenges, Designs, and Applications* (DualRec, 2025 / arXiv:2502.20497) [10]

* **How Retention is Modeled:** Designed for two-sided short-video platforms (e.g., Kuaishou), DualRec optimizes creator-side retention measured as **Daily Active Creators (DAC)** [11]. Because DAC changes slowly over time, the system uses a surrogate metric called **ExpoReach-E** (the number of new items reaching \\(E\\) exposures, e.g., 1K/10K) [11]. It shows empirically that a \\(1\%\\) increase in ExpoReach corresponds to a \\(0.13\%\\) increase in DAC [12].
* **Per-Interaction Credit:** **NO.** User daily activity state (\\(a_u \in \{0, 1\}\\)) is predicted at the daily level via XGBoost, and aggregate exposure thresholds are linked to long-term DAC, but individual interactions/exposures are not assigned per-interaction retention credit [12, 13].
* **MRet Callout:** **NOT PRESENT.**
* **Classification:** **PARTIAL attribution** (correlates aggregate exposure thresholds to creator retention/DAC via proxy metrics, but does not perform per-interaction credit assignment) [11, 12].

---

### 4. *Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach* (Sekiya et al., 2026 / arXiv:2602.11331) [14]

* **How Retention is Modeled:** In evaluating Exposure-Constrained Deferred Acceptance (ECDA) on the Japanese dating platform *CoupLink*, the authors identify **Dating Probability** (the probability a user gets at least one date) as a critical platform KPI because securing at least one date strongly influences user satisfaction and platform retention [15].
* **Per-Interaction Credit:** **NO.** Dating probability is used as an intermediate welfare proxy for retention; retention itself is not decomposed into per-action credit assignment [15].
* **MRet Callout:** **NOT PRESENT.**
* **Classification:** **NOT attribution** (uses dating probability as a static proxy metric for retention rather than attributing retention directly to individual actions) [15].

---

### 5. *Policy Design for Two-sided Platforms with Participation Dynamics* (2023 / Mladenov et al., 2020) [16, 17]

* **How Retention is Modeled:** Models macro population dynamics on two-sided platforms where viewers/providers depart or churn if their received utility or exposure falls below specific thresholds [17].
* **Per-Interaction Credit:** **NO.** Uses differential/difference equations for macro population shifts rather than per-interaction action attribution [17, 18].
* **MRet Callout:** **NOT PRESENT.**
* **Classification:** **NOT attribution** (models aggregate population departure thresholds rather than individual interaction-level retention attribution) [17, 18].

---

### Summary Matrix

| Paper | Model / Method | Per-Interaction Credit? | MRet Present? | Classification |
| :--- | :--- | :--- | :--- | :--- |
| **Kishimoto et al. (ICLR 2026)** [1, 2] | **MRet** (Matching for Retention) [3] | **YES** [3] | **YES** [3] | **TRUE Attribution** [3] |
| **Rios & Torrico (2023/2025)** [4, 5] | `DH-int` / History-dependent disengagement [6, 8] | **NO** [8] | **NO** | **PARTIAL Attribution** [8] |
| **DualRec (2025)** [10] | DualRec / ExpoReach to DAC proxy [11] | **NO** [11] | **NO** | **PARTIAL Attribution** [11] |
| **Sekiya et al. (2026)** [14] | ECDA / Dating Probability proxy [15, 19] | **NO** [15] | **NO** | **NOT Attribution** [15] |
| **Policy Design Dynamics (2023)** [16] | Macro population departure thresholds [17] | **NO** [17] | **NO** | **NOT Attribution** [17] |

***

💡 *Would you like to explore the mathematical formulation of MRet's personalized retention curves and how its objective function differs from traditional Nash Social Welfare (NSW) or Transferable Utility (TU) matching?*