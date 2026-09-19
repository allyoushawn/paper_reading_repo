# Card summaries 6/12 — Summary and Evidence sections of all cards (generated)

### Stratified Expert Cloning for Retention-Aware Recommendation at Scale [1]
`2025_CIKM_SEC_Stratified-Expert-Cloning.md`
**Source:** https://arxiv.org/pdf/2504.05628.pdf  

**Summary.** ### **1. Title, Authors, Affiliations, Year, Venue**
* **Title:** *Stratified Expert Cloning for Retention-Aware Recommendation at Scale* [1]
* **Authors:** **Chengzhi Lin**\*¹, **Annan Xie**\*², **Shuchang Liu**¹, **Wuhong Wang**¹, **Chuyuan Wang**¹, **Yongqi Liu**¹, and **Han Li**¹ (\*Equal contribution) [1]
* **Affiliations:** 
  1. **Kuaishou Technology**, Beijing, China (`1132559107@qq.com`, `{liushuchang, wangwuhong, wangchuyuan, liuyongqi, lihan}@kuaishou.com`) [1]
  2. **Peking University**, Beijing, China (`2301210470@stu.pku.edu.cn`) [1]
* **Year:** **2025** (Published November 2025) [2, 3]
* **Venue:** *Proceedings of the 34th ACM International Conference on Information and Knowledge Management (CIKM ’25), November 10–14, 2025, Seoul, Republic of Korea* [2, 3]

---

### **2. Core Problem and Key Contribution**
* **Core Problem:** Standard recommender systems focus on short-term engagement metrics (e.g., click-through rates), failing to model the long-term temporal dynamics of user retention [1, 4]. While Reinforcement Learning (RL) methods can optimize long-term rewards, they suffer from severe challenges in large-scale recommender systems, including delayed credit assignment, high sample complexity/inefficiency, exploration risks (frustrating users with poor recommendations), and complex evolving user preferences [1, 5, 13–16].
* **Key Contribution:** Introduces **Stratified Expert Cloning (SEC)**, a novel imitation learning framework (specifically Behavior Cloning) that leverages abundant interaction logs from high-retention "expert" users to directly learn retention-oriented policies without trial-and-error RL exploration [5-8]. Key innovations include:
  1. **Multi-level Expert Stratification:** Stratifies expert users into \\(K\\) retention-based hierarchies and trains specialized recommendation policies \\(\pi_k\\) for each tier to capture behavior continuum dynamics [6, 9-11].
  2. **Action Entropy Regularization (AER):** Incorporates entropy regularization (nuclear norm maximization for continuous action matrices, or class probability entropy for discrete actions) to maintain recommendation diversity and prevent policy collapse [6, 9, 12-14].
  3. **Adaptive Expert Selection Mechanism:** Dynamically matches users to the most appropriate expert level policy during inference based on state embedding distance to cluster centroids, constrained by the user's historical retention floor (\\(k^* = \min(k^*, r_h)\\)) [6, 19, 33–35].

---

### **3. Proposed Method or Architecture in Detail**

#### **Architectural Components**
* **State Encoder (\\(f_\phi\\)):** Shared neural network encoder that maps user context and state \\(s_t\\) (demographics, preferences, recent interactions) into a compact state embedding \\(h_t = f_\phi(s_t)\\) [15-17].
* **Action Predictors (\\(g_{\theta_k}\\)):** Specialized action predictor heads for each expert level \\(k \in \{1, \dots, K\}\\), mapping \\(h_t\\) to recommendation action \\(a_t\\) [16, 17].

#### **Training Stage**
* **Multi-Level Behavior Cloning (\\(\mathcal{L}_{\text{BC}}^k\\)):** High-retention expert users are split into \\(K\\) levels based on retention scores (e.g., active days per month) [18]. Trains level-specific policies via MSE loss for continuous actions \\(\sum \|g_{\theta_k}(f_\phi(s)) - a\|^2\\) or cross-entropy loss for discrete actions \\(\sum -\log g_{\theta_k}(a \mid f_\phi(s))\\) [16, 17].
* **Action Entropy Regularization (\\(\mathcal{L}_{\text{AER}}^k\\)):** Maximizes the nuclear norm of the continuous action matrix \\(A_k \in \mathbb{R}^{B \times d}\\) (where \\(\mathcal{L}_{\text{AER}}^k = -|A_k|_* = -\sum_{i=1}^{\min(B,d)} \sigma_i(A_k)\\)) or categorical entropy \\(\sum_{j=1}^C p_{k,j} \log p_{k,j}\\) for discrete actions [13, 19].
* **Total Training Loss:** \\(\mathcal{L} = \sum_{k=1}^K \left( \mathcal{L}_{\text{BC}}^k + \lambda \mathcal{L}_{\text{AER}}^k \right)\\) [19].

#### **Inference Stage**
* **State Space Clustering:** K-means partitions the state space of each expert level into \\(C_k\\) clusters with centroids \\(\mu_{k,c}\\) [20].
* **Adaptive Selection:** Computes minimum distance \\(d_k = \min_c d(f_\phi(s), \mu_{k,c})\\) and assigns the user to expert level \\(k^* = \arg\min_k \{k \mid d_k \le \delta_k\}\\) [21, 22]. Applies historical constraint \\(k^* = \min(k^*, r_h)\\) to ensure recommendations match or exceed the user's historical retention pattern [22, 23].

#### **Credit Assignment Mechanics**
* **No explicit multi-touch credit assignment.** SEC bypasses temporal credit assignment entirely by formulating retention optimization as supervised imitation learning (Behavior Cloning) over expert state-action pairs \\((s_t, a_t)\\) [1, 6, 7, 11, 24]. Instead of decomposing delayed retention signals across past interactions, it trains policies to directly mimic the actions taken by high-retention expert users in given states [6, 8, 11].

---

### **4. Datasets, Production Deployment, and Comparison Baselines**
* **Datasets:**
  * **KuaiRand:** Sequential recommendation dataset with random video exposures (27,285 users, 7,551 items, 1,436,609 interactions, 0.70% density) [25]. Evaluated offline using the **KuaiSim retention simulator** [25].
* **Production Deployment:**
  * Deployed live on **Kuaishou** and **Kuaishou Lite** platforms, each serving **over 200 million Daily Active Users (DAU)** [26, 27].
  * Integrated across both 1st Ranking Stage and 2nd Ranking Stage, using multimodal video clustering for discrete action generation [28, 29]. Online A/B testing allocated 10% traffic to baseline and SEC-optimized versions over two weeks [29].
* **Comparison Baselines:**
  * *Offline Baselines:* CEM (Cross-Entropy Method), DIN (Deep Interest Network), TD3 (Twin Delayed DDPG), SAC (Soft Actor-Critic), RLUR (Reinforcing User Retention), and GFN (Generative Flow Networks) [30].
  * *Online Baselines:* Standard Behavior Cloning + Entropy Loss without multi-level expert stratification [29, 31].

---

### **5. Key Quantitative Results with Numbers**

* **Offline Benchmark (KuaiRand Dataset, Table 1):**
  * **Return Time** (average days until return, lower is better): SEC = **1.411** vs. GFN (**1.496**), RLUR (**1.786**), CEM (**1.889**), DIN (**1.947**), SAC (**2.373**), TD3 (**2.382**) — achieving a **5.7% reduction** in return time over GFN [32, 33].
  * **Click Rate:** SEC = **0.833** vs. GFN (**0.805**), SAC (**0.801**), TD3 (**0.800**), RLUR (**0.789**), DIN (**0.773**), CEM (**0.762**) — a **3.5% improvement** over GFN [32, 33].
  * **Long View Rate:** SEC = **0.825** vs. GFN (**0.794**), SAC (**0.795**), TD3 (**0.791**), RLUR (**0.778**) — a **3.9% improvement** over GFN [32, 33].
  * **Like Rate:** SEC = **0.806** vs. GFN (**0.885**), SAC (**0.857**), TD3 (**0.852**), RLUR (**0.831**) — 8.9% lower than GFN, demonstrating an explicit trade-off where optimizing for long-term retention sacrifices some immediate satisfaction metrics [32, 33].
* **Offline Ablation Study (Table 2):**
  * Removing Multi-level stratification increased Return Time to **1.423** (+0.9%) and decreased Click Rate to **0.821** (-1.2%) [32, 34].
  * Removing Action Entropy Regularization increased Return Time to **1.449** (+1.8%) and decreased Long View Rate to **0.805** (-2.4%) [32, 34].
* **Live Online Production A/B Testing Results (Table 3, Table 4, & Section 5.2.2):**
  * **Active Days (Users active within a 7-day window):**
    * *Behavior Cloning + Entropy Loss:* 1st Ranking Stage (**+0.034%** Kuaishou, **+0.037%** Kuaishou Lite); 2nd Ranking Stage (**+0.036%** Kuaishou, **+0.042%** Kuaishou Lite) [29, 31].
    * *Additional gain from Multi-Level Expert Stratification:* **+0.028%** on Kuaishou, **+0.043%** on Kuaishou Lite [29, 31].
    * *Cumulative Total Improvement:* **+0.098%** on Kuaishou, **+0.122%** on Kuaishou Lite [29, 31].
    * *DAU Business Impact:* Translates directly into **over 200,000 additional daily active users (DAU)** on each platform [5, 29, 31].
  * **User Interest Expansion (Table 4):** Valid interest clusters increased by **+1.31%** on Kuaishou and **+1.14%** on Kuaishou Lite [35].

---

### **6. Limitations, Failure Modes, or Negative Results**
1. **Dependence on Expert User Availability:** Effectiveness is fundamentally contingent on having a sufficiently large and diverse set of high-retention "expert" users; it may perform poorly on nascent platforms or in niche domains lacking rich expert logs [36].
2. **Cold-Start Bottleneck:** Adaptive expert selection relies on high-quality user state embeddings \\(f_\phi(s)\\), which are sparse or unreliable for new users [36].
3. **Trade-Off with Immediate Satisfaction:** Offline Like Rate was **8.9% lower** than GFN (0.806 vs. 0.885), showing that optimizing strictly for long-term retention can slightly degrade immediate user feedback signals [33].
4. **Unproven Cross-Domain Generalizability:** Evaluated primarily on short-video platforms; applicability to e-commerce or news recommendation remains unverified due to differing definitions of expert behavior and retention metrics [36].

---

### **7. Top 5–7 Most Heavily Cited Prior Works**
1. **Cai et al. (2023) [RLUR / Retention RL]:** *Reinforcing User Retention in a Billion Scale Short Video Recommender System* (WWW '23) [37, 38].
2. **Liu et al. (2024) [GFN4Retention]:** *Modeling User Retention through Generative Flow Networks* (KDD '24) [39].
3. **Zhao et al. (2023) [DT4Rec]:** *User retention-oriented recommendation with decision transformer* (WWW '23) [40].
4. **Zhao et al. (2023) [KuaiSim Simulator]:** *KuaiSim: A comprehensive simulator for recommender systems* (NeurIPS '23) [40].
5. **Pomerleau (1991) / Ross et al. (2011) [Behavior Cloning Foundations]:** *Efficient training of artificial neural networks for autonomous navigation* & *A reduction of imitation learning and structured prediction to no-regret online learning* [41, 42].
6. **Ho & Ermon (2016) [GAIL] / Ng & Russell (2000) [IRL]:** *Generative adversarial imitation learning* & *Algorithms for inverse reinforcement learning* [43, 44].
7. **Ding et al. (2023) [IURO]:** *Interpretable User Retention Modeling in Recommendation* (RecSys '23) [45].

---

💡 *Would you like to explore how SEC's multi-level expert stratification or action entropy regularization could be adapted to guide candidate profile selection for your dating app's retention ranker?*

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Impatient Bandits: Optimizing for the Long-Term Without Delay [1]
`2025_JMLR_ImpatientBandits_Optimizing-Recommendations-Long-Term.md`
**Source:** https://arxiv.org/pdf/2501.07761.pdf  

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Impatient Bandits: Optimizing for the Long-Term Without Delay* [1]
* **Authors & Affiliations:**
  * **Kelly W. Zhang** (`kelly.zhang@imperial.ac.uk`) — **Imperial College London** [1]
  * **Thomas Baldwin-McDonald** (`tommcdonald955@gmail.com`) — **University of Manchester** [1]
  * **Kamil Ciosek** (`kamilc@spotify.com`) — **Spotify** [1]
  * **Lucas Maystre** (`lucas@reflection.ai`) — **Reflection AI** [1]
  * **Daniel Russo** (`djr2174@gsb.columbia.edu`) — **Columbia University** [1]
* **Year:** **2026** (Submitted January 2025; Published March 2026) [1]
* **Venue:** ***Journal of Machine Learning Research* (JMLR)**, Vol. 27, pp. 1–58, 2026 [1]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Large-scale recommender systems face a severe trade-off between learning speed and long-term metric alignment [1, 2]. Waiting weeks or months (e.g., 60 days) to observe true long-term user satisfaction drastically slows learning and fails in **cold-start settings** for newly released content [1, 4–5]. Conversely, optimizing for immediate proxy metrics (like click-through rate or day-two return) leads to myopic recommendations poorly aligned with long-term retention [1-3].
* **Key Contributions:**
  1. **Bandits with Progressive Feedback Framework:** Formulates a multi-armed bandit framework where rewards are observed with significant delays but become incrementally predictable as intermediate daily user engagement signals arrive [1, 4].
  2. **Impatient Bandit Algorithm:** Combines **Thompson Sampling** for active content exploration with an **empirical Gaussian Bayesian filter** that synthesizes continuous intermediate feedback signals while maintaining proper residual uncertainty estimates [1, 5].
  3. **Value of Progressive Feedback (VoPF):** Proves theoretical regret bounds governed by an information-theoretic metric (\\(\text{VoPF}(t)\\)) that quantifies how early observations reduce uncertainty about distal long-term outcomes [1, 6, 7].
  4. **Large-Scale Industrial Validation:** Deployed live in production at **Spotify** powering audio recommendations for hundreds of millions of users [1, 8].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Problem Setup & Trajectory Representation**
* **Cohort & Action Setup:** Users \\(u \in U_t\\) arrive in daily batches of size \\(m = |U_t|\\) [9]. Actions \\(a \in A\\) represent candidate items (e.g., podcast shows) [9, 10].
* **Progressive Engagement Vector (\\(Y_u(a)\\)):** Over \\(J = 60\\) days post-discovery, daily user activity is recorded as \\(Y_u(a) = (Y_u^{(1)}(a), Y_u^{(2)}(a), \dots, Y_u^{(60)}(a))\\), where \\(Y_u^{(j)} \in \{0, 1\}\\) indicates active listening on day \\(j\\) [11, 12]. Each outcome is revealed after delay \\(d_j = j-1\\) [11].
* **Target Reward (\\(R(Y_u)\\)):** Defined as cumulative 60-day active days \\(R(Y_u) = \sum_{j=1}^{60} Y_u^{(j)}\\) [12].

#### **Core Architectural Modules**
1. **Gaussian Bayesian Filter & Cholesky Updating:** Models potential outcomes as a Gaussian process \\(\theta_a \sim \mathcal{N}(\mu_{1,z}, \Sigma_{1,z})\\) and \\(Y_u(a) \mid \theta_a \sim \mathcal{N}(\theta_a, V_z)\\) [13, 14]. Uses Cholesky decomposition of noise covariance \\(V_z = L_z L_z^\top\\) (\\(L_z^{-1} Y_u\\)) to compute closed-form posterior updates \\((\mu_{t+1,a}, \Sigma_{t+1,a})\\) as censored intermediate daily feedback arrives [34, 94–96].
2. **Thompson Sampling Action Selection:** Draws posterior samples \\(\theta_a' \sim \mathcal{N}(\mu_{t,a}, \Sigma_{t,a})\\) and recommends items maximizing expected long-term return \\(A_u = \arg\max_{a \in A} R(\theta_a')\\) [15, 16]. A lower-variance variant applies probability rounding (\\(\pi_{\text{TS-rnd}}\\)) [33, 36–38].
3. **Contextual Extension:** Incorporates user context features \\(X_u\\) where expected outcomes are linear combinations over context embeddings (\\(\phi(X_u, \ell_z^{(j)})\\)) [32, 98–101].

#### **Credit Assignment Mechanics**
* The framework does **not** perform explicit multi-touch credit assignment across past user interaction logs.
* Instead, credit is assigned at the **item/action level** (\\(\theta_a\\)) by continually updating the Gaussian posterior probability distribution of an item's 60-day retention trajectory as daily engagement signals (\\(Y_u^{(1)}, Y_u^{(2)}, \dots\\)) are observed progressively [5, 15, 17].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets & Scale:**
  1. **Spotify Production Dataset:** **8.77 million activity traces**, corresponding to **26 million cumulative active-days** across 60 days of podcast show discoveries [12]. Traces per show range between **2.4K and 295K** (median **5.8K**) [12].
  2. **Synthetic Gaussian Environments:** Generated under Low (\\(\alpha=0.1\\)), Mid (\\(\alpha=0.4\\)), and High (\\(\alpha=0.8\\)) progressive feedback information regimes [18].
* **Production Deployment:** Fully deployed in live production at **Spotify** on the mobile home page recommendation shelf ("Shows you might like" podcast discovery shelf) serving **hundreds of millions of users** [1, 8, 17, 19].
* **Comparison Baselines:**
  * **Delayed Thompson Sampling:** Waits the full 60 days to observe complete engagement rewards, ignoring intermediate feedback [20, 21].
  * **Day-Two Proxy:** Optimizes for a short-term proxy (\\(Y_u^{(2)}\\), returning the day after discovery) and discards subsequent feedback [3].
  * **Progressive (Isotropic / Uninformative Prior):** Runs the Impatient Bandit algorithm using an uninformative prior (\\(\mu_1 = 0, \Sigma_1 = 100I, V = I\\)) instead of the learned prior [22].
  * **Oracle:** Assumes zero delay (\\(d_j = 0\\) for all \\(j\\)), providing an upper-bound benchmark [23].
  * **Sequential Elimination (SE):** Best-arm identification baseline evaluated with 1% and 4% elimination thresholds [24].

---

### **(5) Key Quantitative Results with Numbers**

* **Spotify Semi-Synthetic Benchmark (\\(|A|=200\\) shows, Figure 6):**
  * **Cumulative Regret:** Impatient Bandit cumulative regret plateaued near **~150** (at \\(m=200\\)), whereas *Delayed* reached **~480**, and *Day-two proxy* exceeded **>600** (exhibiting non-sublinear linear regret) [65–66].
  * **Uninformative Prior Regression:** *Progressive (Isotropic)* without a fitted prior accumulated regret **>800** at day 180, performing worse than Delayed [67–68].
* **Live Production Spotify A/B Test Results (Table 1 & Figure 11):**
  * **Recently Released Shows (Cold-Start Scale):**
    * *Recommendation Impression Volume:* Relative difference was **+2.15%** (virtually unchanged volume, **-0.02%** across all shows) [25, 26].
    * *Discovery Rate (Discoveries / Impression):* **+29.7% increase** over Control [27].
    * *60-Day Retained Engagement per Impression:* 60-day active days, 60-day minutes, and 60-day return days per impression increased by **>50%** over Control [27].
  * **Platform-Wide Impact (All Impressions):**
    * *60-day active days per impression:* **+2.4%** increase over Control [28].
    * *60-day minutes per impression:* **+2.2%** increase over Control [28].
    * *60-day return days per impression:* **+2.5%** increase over Control [28].
    * *Discovery rate per impression:* **+1.8%** increase over Control [28].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Dependency on Type II Maximum Likelihood Prior Fitting:** Algorithm performance is strictly driven by the quality of the learned prior \\((\mu_{1,z}, \Sigma_{1,z})\\) and noise covariance \\(V_z\\) [14, 29, 30]. Using an uninformative prior caused cumulative regret to jump from **~200 to >800**, rendering the algorithm ineffective [67–68].
2. **Linear Non-Sublinear Regret of Short-Term Proxies:** Optimizing solely for short-term surrogates (*Day-two proxy*) accumulated linear regret over time, proving that single short-term engagement proxies fail to reflect 60-day retention [3, 31].
3. **Restriction to Affine / Gaussian Likelihood Functions:** Bayesian update rules rely on linear Gaussian assumptions, requiring kernel approximations or linear feature spaces to extend to non-linear neural network architectures [13, 32, 33].
4. **Computational Covariance Overhead:** Maintaining and updating \\(60 \times 60\\) Gaussian covariance matrices via Cholesky decomposition (\\(L_z^{-1}\\)) for large candidate pools requires structured approximations in high-dimensional feature spaces [94–96].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Thompson (1933) [Ref / Thompson Sampling]:** *On the likelihood that one unknown probability exceeds another in view of the evidence of two samples* (Biometrika) [5, 34].
2. **Maystre, Russo, & Zhao (2023) / McDonald et al. (2023) [Refs / Spotify RL & Impatient Bandits]:** *Optimizing audio recommendations for the long-term: A reinforcement learning perspective* & *Impatient bandits: Optimizing recommendations for the long-term without delay* (KDD '23) [35-37].
3. **Athey et al. (2016) / Yang et al. (2024) [Refs / Surrogate Index]:** *Estimating treatment effects using multiple surrogates: The role of the surrogate score and the surrogate index* & *Targeting for long-term outcomes* (Management Science) [38-41].
4. **Wang et al. (2022) [Ref / Google Surrogate]:** *Surrogate for long-term user experience in recommender systems* (KDD '22) [35, 42, 43].
5. **Wu & Wager (2022) [Ref / Survival Thompson Sampling]:** *Partial likelihood Thompson sampling* (UAI '22) [43-45].
6. **Qin & Russo (2023) [Ref / Adaptive Experimentation]:** *Adaptive experimentation in the presence of exogenous nonstationary variation* [46-48].
7. **Russo & Van Roy (2016) / Russo et al. (2020) [Refs / Information Bounds & Tutorial]:** *An information-theoretic analysis of Thompson sampling* & *A tutorial on Thompson sampling* [15, 49].

---

💡 *Would you like to explore how Spotify's Gaussian Bayesian filter or Value of Progressive Feedback (VoPF) metric could be adapted to evaluate early swiping and messaging trajectories for your dating app's candidate ranker?*

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

