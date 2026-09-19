# NLM Phase 4-A — q4-bias-eval

Scoped to this-run source_ids (G1–G25). returncode=0 elapsed=149.6s stdout_bytes=111628

### **Catalog of Selection-Bias & Confounding Devices**

#### **1. Front-Door Identification & Adversarial Proxy Mediation**
* **Paper / System Source:** *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization* (Kuaishou Technology, ICLR 2026) [1, 2].
* **Bias Addressed:** Resolves unobserved system-level and sequence-level confounding (e.g., latent user intent, unmeasured platform recommendation strategies, and social influences) that invalidate backdoor adjustments in observational logs [2, 3].
* **What It Does NOT Identify:** It does not identify causal effects if the latent mediator (\\(M\\)) fails path containment (i.e., if direct touchpoint-to-outcome \\(T \to Y\\) paths exist that bypass \\(M\\)) or if the adversarial proxy (\\(Y'\\)) leaks direct outcome information [2, 4, 5]. Furthermore, its target outcome is creator content upload (\\(Y\\)), *not* user retention [6, 7].
* **Yields Per-Interaction Credit?:** **YES.** Outputs individualized counterfactual removal uplift labels \\(\Delta(\tau_j \mid X, T) = g_\theta(X, T) - g_\theta(X, T \setminus \{\tau_j\})\\) for each consumed touchpoint \\(\tau_j\\) in a user sequence [180, 189–190].

---

#### **2. Experiment-Calibrated Data-Driven Attribution (DDA) & MMM Anchoring**
* **Paper / System Sources:** 
  1. *Buyer Journey Insights with Data-Driven Attribution* / *LiDDA* (LinkedIn, 2025) [3–4].
  2. *Integrated Marketing Attribution (IMA)* (Lowe's Companies, Inc., 2026) [8, 9].
* **Bias Addressed:** Over-indexing on low-funnel conversion channels (e.g., Search or Email) inherent in last-touch rules [10, 11]. Resolves missing member-level paid media impression data via probabilistic imputation [5–6]. IMA addresses campaign-level high-dimensionality and cross-campaign multicollinearity by anchoring daily campaign models to macro-level Marketing Mix Modeling (MMM) priors [9, 12].
* **What It Does NOT Identify:** It does not identify item-level counterfactual removal effects (\\(\Delta \text{Outcome}\\) if a single touchpoint is deleted) [13, 14]. LiDDA outputs normalized self-attention weights calibrated to aggregate holdout experiment/MMM ratios [13, 15], while IMA operates on aggregated daily campaign media data rather than user-level touchpoints [8, 12].
* **Yields Per-Interaction Credit?:**
  * **LiDDA:** **YES** (member-level per-touchpoint normalized attention weights) [13, 16].
  * **IMA:** **NO** (campaign-level daily sales disaggregation, no user-level touchpoint credit) [8, 12].

---

#### **3. Always-On Holdbacks & Dual-Threshold Causal Targeting (Deep Twin Network)**
* **Paper / System Source:** *Incremental Recommendation via Causal Models* (Spotify, 2026) [254–255].
* **Bias Addressed:** Selection bias toward "always-takers"—users with high organic affinity who would discover or stream content regardless of a recommendation [17, 18]. Resolves attribution window mismatches (short direct-response window for treated \\(Y(1)\\) vs. multi-day organic window for holdback \\(Y(0)\\)) [17, 19].
* **What It Does NOT Identify:** It does not estimate a valid point-wise CATE subtraction \\(p_1(\mathbf{x}) - p_0(\mathbf{x})\\) directly due to the temporal window mismatch [18, 20], nor does it produce fractional multi-touch credit across past user interaction sequences [18, 20].
* **Yields Per-Interaction Credit?:** **NO.** It produces dual propensity scores (\\(p_1(\mathbf{x})\\) for recommendation stream probability and \\(p_0(\mathbf{x})\\) for organic stream probability) to filter non-incremental impressions via a dual-threshold policy \\(\mathbb{1}[p_1(\mathbf{x}) \ge \theta_1] \cdot \mathbb{1}[p_0(\mathbf{x}) \le \theta_0]\\) at serving time [18, 20].

---

#### **4. Interleaving (Competitive Pair Team Drafting) & Online Counterfactual Evaluation**
* **Paper / System Source:** *Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking* (Airbnb, KDD 2025) [21, 22].
* **Bias Addressed:** Position bias, long observation delays, and low statistical power in standard conversion-based A/B testing (accelerating online evaluation velocity up to 100x) [21, 23, 24].
* **What It Does NOT Identify:** Interleaving breaks down when rankers perform set-level optimization (e.g., secondary objective re-ranking or diversity), as side-by-side presentation distorts user choice [25-27]. Counterfactual evaluation depends on position-decay assumptions (\\(\gamma^{-r}\\)) and does not yield historical multi-touch credit for user retention [135–136, 141].
* **Yields Per-Interaction Credit?:** **NO.** Attributes booking preferences to listing search appearances to evaluate ranking policy variants before A/B deployment; does not publish persistent per-touch sequence credit tables [28, 29].

---

#### **5. Sleeping & Recovering Bandits (IPW Relative Scoring & Recency Decay)**
* **Paper / System Source:** *A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications* (Duolingo, KDD 2020) [30, 31].
* **Bias Addressed:** Conditional eligibility bias (sleeping arms—where template availability is confounded by user activity/state) [30, 32] and user desensitization/fatigue (recovering arms—where novelty wears off) [30, 33].
* **What It Does NOT Identify:** It does not identify multi-touch sequence attribution across past user interactions [298–299], nor long-term multi-day retention directly (reward is evaluated strictly in a 2-hour post-notification window) [34].
* **Yields Per-Interaction Credit?:** **NO.** It computes arm-level relative difference scores \\(\hat{s}_a = \frac{\hat{\mu}_a^+ - \hat{\mu}_a^-}{\hat{\mu}_a^-}\\) with empirical Bayes shrinkage and recency decay penalties (\\(2^{-d_{a,t}/h}\\)) for Softmax template selection [33, 35, 36].

---

#### **6. Observational vs. RCT Gaps & Propensity-Stratified Evaluation Protocols**
* **Paper / System Sources:**
  1. *ALM-MTA* (Kuaishou, ICLR 2026) [1, 37].
  2. *Buyer Journey Insights* (LinkedIn, 2025) [13, 14].
  3. *Impatient Bandits* (Spotify, JMLR 2026) [38, 39].
  4. *AURO* (Kuaishou, WWW 2025) [40, 41].
* **Bias Addressed:** Off-policy distribution shift, spurious correlations in historical logs, and evaluation bias when true randomized controlled trial (RCT) labels are unavailable [37, 39, 42].
* **Protocol Details:** ALM-MTA introduces a non-personalized, propensity-stratified grouped AUUC protocol using Shapley value sampling across \\(K \approx 1000\\) treatment clusters [224–226]. Spotify Impatient Bandits uses Type II Maximum Likelihood prior fitting and Value of Progressive Feedback (VoPF) information bounds [39, 43, 44]. LinkedIn evaluates channel lift counterfactuals against holdout A/B tests [14].
* **What It Does NOT Identify:** Propensity stratification and off-policy estimators (NCIS, IPW) control for observed covariates \\(X\\), but fail if unobserved confounding \\(W\\) violates unconfoundedness (unless front-door mechanisms are applied) [3, 42].
* **Yields Per-Interaction Credit?:** **Varies by method.** The protocol itself is an evaluation/debiasing procedure; ALM-MTA produces per-touch credit [6, 45], whereas RL/bandit evaluation protocols do not [46, 47].

---

### **Negative Evidence: Systems That Optimize Retention Without Producing Per-Touch Credit**

The following systems from the scoped sources optimize retention, revisitation, or multi-day engagement via RL, learning-to-rank, bandits, or surrogate rewards, but **do NOT produce or publish a per-touch sequence attribution credit table**:

1. **AURO (Adaptive User Retention Optimization)** (*Kuaishou Technology / NTU, WWW 2025*): Hidden Parameter MDP (HiP-MDP) with value-based state abstraction loss \\(J(\phi)\\) and guarded online exploration [40, 46, 48]. Optimizes delayed user return time rewards (\\(r_t = \lambda \times \text{return time}\\)), outputting continuous action vectors for candidate ranking policy execution without per-touch attribution [46, 48].
2. **ItemA2C (Future Impact Decomposition)** (*Kuaishou Technology, KDD 2024*): Request-level MDP with item-decomposed advantage actor-critic [49, 50]. Decomposes list-level future value \\(V(s_{t+1})\\) into item-level targets \\(\Psi_w(s_t, i_{t,k})\\) via adversarial/reward-based weights \\(w_{t,k}\\) to update ranking policy parameters \\(\pi_\theta\\), without generating a reusable attribution credit table [50-52].
3. **GFN4Retention (Generative Flow Networks for Retention)** (*Kuaishou Technology, KDD 2024*): Probabilistic flow-matching network propagating end-of-session retention reward \\(R\\) across recommendation steps via detailed balance loss [53-55]. Generates candidate list selection policies without per-item sequence attribution labels [56, 57].
4. **Pinterest Downstream Rewards & Save-Revisit Frameworks** (*Pinterest, 2026 / AAAI 2026*): Offline screening under User-Prevalence (UP) normalization identifies session-level surrogates (P2P rabbit hole exploration, shallow closeup penalties, use-case adoption, 0–6 day save-gridclicks) [58-61]. Multi-task prediction heads are combined via HyperOPT out-of-graph weights \\(s(x) = \sum w_i p_i(x)\\) for candidate rankers; no per-interaction credit table is produced [58, 62, 63].
5. **Google / YouTube Reward Surrogates & Learned Ranking Function (LRF)** (*Google Research, KDD 2022 / RecSys 2024*): Modulates REINFORCE rewards via 2-week entropy diversity multipliers [64, 65] or computes uplift over abandonment \\(\frac{p_{\text{clk}}}{p_{\text{clk}}+p_{\text{abd}}} (R_{\text{clk}} - R_{\text{abd}})\\) to output candidate slate scores [66-68]; does not produce multi-touch sequence attribution tables [64, 67].
6. **Spotify Impatient Bandits** (*Spotify / Imperial College London, JMLR 2026*): Gaussian Bayesian filter updating 60-day active-day posterior stickiness beliefs \\(\theta_a\\) as daily progressive engagement signals arrive [38, 39, 69]. Used for Thompson Sampling podcast show recommendations without multi-touch historical sequence credit [47, 69, 70].
7. **RLUR (Reinforcing User Retention)** (*Kuaishou Technology, WWW 2023*): Infinite-horizon DDPG critic \\(Q_T(s,a)\\) minimizing cumulative return time gap between app sessions [71, 72]. Outputs ranking policy parameters without touchpoint attribution [71, 73].
8. **DT4Rec & DT4IER (Decision Transformer for Retention)** (*Baidu / Academic, WWW 2023 / 2024*): Autoregressive sequence generation prompted by discretized Return-to-Go (RTG) vectors [74-76]. Outputs recommended item sequences rather than per-touch attribution credit tables [74, 75].
9. **DCEO (Direct Causal Effect Optimization)** (*Alibaba / Taobao, 2026*): Actor model \\(f_\theta\\) predicts context-dependent fusion weights \\(w_{ur}^m\\) over upstream scores, aggregated and calibrated (\\(g_\psi\\)) to a reference impression count (\\(C=100\\)) to optimize Relative Causal Effect on 4-day GMV via critic \\(h_\phi\\) [77-79]. Produces ranking fusion weights, not a per-touch attribution table [78, 79].
10. **Matching for Retention (MRet)** (*Academic / Dating Platform Research, 2026*): Evaluates personalized retention curves \\(f(x, m_{1:\tau})\\) to maximize mutual user retention probabilities in two-sided matching, operating as a learning-to-rank allocation algorithm without fractional touchpoint credit [80-82].
