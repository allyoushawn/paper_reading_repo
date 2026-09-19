# Impatient Bandits: Optimizing for the Long-Term Without Delay [1]

**Source:** https://arxiv.org/pdf/2501.07761.pdf  
**Date analyzed:** 2026-09-18  
**NLM source id:** `c7d8e9d2-5ee2-4cbf-ab8a-15cba733edc1`  
**Queue id:** G16  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**
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

### **Source Evaluation: *Impatient Bandits: Optimizing for the Long-Term Without Delay***
*(Zhang et al., Imperial College London, University of Manchester, Spotify, Reflection AI, & Columbia University; JMLR 2026 / arXiv: `2501.07761`)* [1]

---

### **(A) Q1 or Q2 or Both or Neither?**

**Neither.** [1, 6–8]  
* **Q1 (Industry/Production Attribution 2025-01 to 2026-09):** **No.** While submitted in January 2025, published in March 2026 in JMLR (Vol. 27), and deployed live at Spotify, this paper presents a **bandit exploration algorithm** for long-term reward optimization rather than an industry multi-touch attribution measurement framework [1, 6–8].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The algorithm optimizes long-term 60-day engagement for podcast recommendations using progressive feedback, but it does **not** perform historical multi-touch sequence attribution or allocate per-swipe credit across past interaction logs [1-4].

---

### **(B) Q2 Class**

**NOT.** [8, 30–31]  
* **Justification:** Impatient Bandits is a multi-armed bandit policy framework (Impatient Thompson Sampling with an empirical Gaussian Bayesian filter) that updates posterior probability distributions over latent content stickiness vectors \\(\theta_a\\) [8, 29–31]. It does **not** generate or publish a per-exposure retention credit table.

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction credit.** [8, 30–31]
* **Target Outcome:** **60-Day Cumulative Active Days / Engagement (\\(R(Y_u) = \sum_{j=1}^{60} Y_u^{(j)}\\))** [2, 5, 6].
* **Mechanics:** Instead of attributing fractional credit across past swiping or messaging touchpoints, the algorithm updates the posterior belief over a recommended content item's latent 60-day stickiness vector \\(\theta_a\\) as daily user listening feedback (\\(Y_u^{(1)}, Y_u^{(2)}, \dots\\)) arrives progressively over time [8, 30–31].

---

### **(D) Replacing Last-Touch N7 → Latest Swipes**

* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% of an N7 retention label to recent swipes, ignoring earlier interactions and failing to optimize for long-term engagement during cold-start recommendation [3–5]. Impatient Bandits replaces post-hoc rule-based attribution by treating early engagement signals as **progressive feedback** (\\(Y_u^{(1)}, Y_u^{(2)}, \dots\\)) [2, 7, 8]. It uses a Bayesian filter trained on historical user engagement trajectories to continuously update posterior estimates of an item/candidate's 60-day stickiness vector \\(\theta_a\\), allowing the recommender to make uncertainty-aware candidate ranking decisions immediately without waiting 7 or 60 days [8, 30–31].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Candidate Profile / Strategy Stickiness (\\(\theta_a\\)):* Represents the latent long-term retention quality of a candidate profile or recommendation strategy [9, 10].
  2. *Progressive Trajectory (\\(Y_u^{(1)}, Y_u^{(2)}, \dots, Y_u^{(7)}\\)):* Tracks daily engagement trajectories following a match/recommendation (Day 1 swipe/match, Day 2 initial chat, Day 3 4-way conversation, Day 4–7 return visits) [2, 11].
  3. *Bayesian Filter & Thompson Sampling:* Instead of waiting for Day 7 to observe \\(N7\\), the system uses early intermediate signals (Day 1–2 matches/chats) to update the Gaussian posterior belief over \\(\theta_a\\) via Cholesky decomposition [31, 91–93], selecting candidate profile recommendations that maximize expected 7-day retention \\(R(\theta_a')\\) via Thompson sampling [3, 12].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Prior Fitting via Type II Maximum Likelihood:** Learns Gaussian prior parameters (\\(\mu_{1,z}, \Sigma_{1,z}, V_z\\)) across historical user interaction trajectories to anchor posterior updates [3, 10, 13].
2. **De Finetti's Exchangeability Assumption:** Assumes potential outcomes \\(Y_u(a)\\) are conditionally i.i.d. given latent item feature \\(\theta_a\\) and observed features \\(Z_a\\) [20–21, 28–29].
3. **Uncertainty-Aware Thompson Sampling:** Balances exploration and exploitation by sampling from posterior distributions \\(\mathcal{N}(\mu_{t,a}, \Sigma_{t,a})\\), preventing premature convergence to suboptimal items [8, 30–31].
4. *Note:* The paper does not apply explicit inverse propensity weighting (IPW) or causal debiasing for individual user selection bias.

---

### **(F) Deployment & Production Dataset Evidence**

* **Production Deployment:** Fully deployed in live production at **Spotify** on the mobile home page recommendation shelf ("Shows you might like" podcast discovery shelf) serving **hundreds of millions of users** [1, 6, 73, 80–84].
* **Production Dataset:** **8.77 million activity traces**, corresponding to **26 million cumulative active-days** across 60 days from Spotify [5]. The number of traces per show ranges between **2.4K and 295K**, with a **median of 5.8K** [5].
* **Quoted Quantitative Results:**
  * **Spotify Semi-Synthetic Benchmark (Figures 6 & 7, \\(|A|=200\\) shows):**
    * Cumulative regret for Impatient Bandit plateaued near **~150** at day 180 (for batch size \\(m=200\\)), whereas *Delayed* reached **~480**, and *Day-Two Proxy* exceeded **>600** (exhibiting linear non-sublinear regret) [63–64].
    * *Progressive (Isotropic)* without a learned prior reached regret **>800** at day 180 [65–66].
  * **Live Online Spotify A/B Test Results (Recently Released Shows, Table 1 & Figure 11 right):**
    * *Recommendation Volume:* Total impressions of recently released shows changed by **+2.15%** relative difference (virtually unchanged volume, **-0.02%** overall) [80–81].
    * *Discovery Rate (Discoveries per Impression):* **+29.7%** increase over Control [14].
    * *60-Day Retained Engagement per Impression:* 60-day active days per impression, 60-day minutes per impression, and 60-day return days per impression increased by **>50%** over Control [14].
  * **Overall Platform-Wide Impact (All Impressions, Figure 11 left):** 
    * 60-day active days: **+2.4%** over Control [83–84].
    * 60-day minutes: **+2.2%** over Control [83–84].
    * 60-day return days: **+2.5%** over Control [83–84].
    * Discovery rate: **+1.8%** over Control [83–84].

---

💡 *Would you like to explore how Impatient Bandits' Bayesian filter or Value of Progressive Feedback (VoPF) metric could be applied to evaluate early swiping and messaging engagement for your dating app's candidate profile ranker?*

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
**Priority:** see queue.md `G16`
