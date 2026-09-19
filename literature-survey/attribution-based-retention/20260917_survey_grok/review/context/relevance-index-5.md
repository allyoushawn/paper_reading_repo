# Relevance index 5/10 — Project Relevance sections of all cards (generated)

### Stratified Expert Cloning for Retention-Aware Recommendation at Scale [1]
`2025_CIKM_SEC_Stratified-Expert-Cloning.md`
**Source:** https://arxiv.org/pdf/2504.05628.pdf  

### **Source Evaluation: Stratified Expert Cloning for Retention-Aware Recommendation at Scale**
*(Lin et al., Kuaishou Technology & Peking University, CIKM 2025: `arxiv:2504.05628`)* [1]

---

### **(A) Q1 or Q2 or Both or Neither?**
* **Answer:** **Neither.**
* **Explanation:**
  * *Q1 (Industry/Production Attribution 2025–2026):* **No.** While published at CIKM 2025 (November 2025) and deployed on live production platforms, the paper presents an **imitation learning / behavior cloning recommendation framework**, not an attribution measurement system [1, 2].
  * *Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):* **No.** The authors explicitly highlight that retention optimization suffers from "delayed impact and credit assignment" [3]. Rather than performing multi-touch sequence attribution over past interactions, the paper bypasses credit assignment entirely by using Behavior Cloning over high-retention expert user logs [1, 6, 16–17].

---

### **(B) Q2 Class**
* **Classification:** **NOT**
* **Justification:** As an imitation learning / policy optimization framework (**SEC**), it learns action predictors via Behavior Cloning over stratified expert state-action pairs without generating or publishing a per-exposure retention credit table [6, 19, 23–26].

---

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction credit.**
* **Mechanism:** Bypasses temporal credit assignment by casting retention optimization as supervised imitation learning over expert state-action pairs \\((s_t, a_t)\\) [16–18, 24–26]. It trains expert policy heads \\(g_{\theta_k}(f_\phi(s))\\) using Mean Squared Error (MSE) loss for continuous actions or Cross-Entropy loss for discrete actions to directly mimic expert choices [25–26].
* **Target Outcome:** **Active Days within a 7-day window** (and reduced **Return Time** in days until next app visit) [4-7].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**
* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% of an N7 retention label to the final swipe before Day 7. **SEC** replaces rule-based attribution entirely with **Behavior Cloning (imitation learning) on high-retention "expert" users** [1, 8, 9]. Instead of attempting to back-propagate an N7 label to individual swipes, SEC identifies users who achieve high 7-day retention ("experts"), stratifies them into \\(K\\) retention tiers, and trains neural policies to directly mimic the candidate selection actions taken by those expert users in any given state [6, 19, 22–24].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *State Encoder (\\(f_\phi(s_t)\\)):* Encodes the user's current context and state (demographics, recent swipe history, active matches, messaging activity) [10, 11].
  2. *Multi-Level Expert Stratification (\\(U_1^E, U_2^E, U_3^E\\)):* Segments highly retained users into \\(K\\) expert tiers based on historical active days or retention scores [22–23].
  3. *Adaptive Policy Execution (\\(k^* = \min(k^*, r_h)\\)):* Matches a swiping user's state embedding to the nearest expert cluster centroid, bounded by their historical retention floor \\(r_h\\), and uses expert policy \\(\pi_{k^*}\\) to recommend candidate profiles whose match/engagement potential aligns with successful long-term retained users [33–36].

---

### **(E) Selection-Bias & Confounding Handling**
1. **Multi-Level Expert Stratification:** Rather than using a binary expert/non-expert classification (which introduces severe selection bias by attempting to force average users to mimic unachievable top-1% behavior), SEC stratifies expert users into \\(K\\) retention hierarchies, modeling user behavior along a natural continuum [6, 21–23].
2. **Adaptive Selection with Historical Floor Constraint:** During inference, a user's selected expert level is constrained by their historical retention level (\\(k^* = \min(k^*, r_h)\\)), preventing unrealistic policy assignments and ensuring recommendation quality does not degrade [34–35].
3. **Action Entropy Regularization (AER):** Maximizes the nuclear norm of the continuous action matrix (\\(\mathcal{L}_{\text{AER}}^k = -|A_k|_*\\)) or categorical class entropy to prevent policy collapse and ensure recommendation diversity across user interests [6, 27–31].

---

### **(F) Deployment and Production Dataset Evidence**

* **Production Deployment:** Deployed live on **Kuaishou** and **Kuaishou Lite**, two major video platforms serving **over 200 million Daily Active Users (DAU)** each [4, 12, 13]. Evaluated in online A/B testing holding out 10% traffic for over two weeks across both 1st Ranking Stage and 2nd Ranking Stage pipelines [7, 13].
* **Offline Benchmark Dataset:** **KuaiRand** (27,285 users, 7,551 items, 1,436,609 interactions, 0.70% density) evaluated using the **KuaiSim retention simulator** [6, 14].
* **Quoted Quantitative Results:**
  * **Offline Simulator Benchmark (KuaiRand, Table 1):**
    * **Return Time (lower is better):** **1.411** days (SEC) vs. GFN (**1.496**), RLUR (**1.786**), CEM (**1.889**), DIN (**1.947**), SAC (**2.373**), TD3 (**2.382**) — achieving a **5.7% reduction in return time** over GFN [6, 15].
    * **Click Rate:** **0.833** (SEC) vs. GFN (**0.805**), SAC (**0.801**), TD3 (**0.800**), RLUR (**0.789**), DIN (**0.773**), CEM (**0.762**) — a **3.5% improvement** over GFN [6, 15].
    * **Long View Rate:** **0.825** (SEC) vs. GFN (**0.794**), SAC (**0.795**), TD3 (**0.791**), RLUR (**0.778**) — a **3.9% improvement** over GFN [6, 15].
    * **Like Rate:** **0.806** (SEC) vs. GFN (**0.885**), SAC (**0.857**), TD3 (**0.852**), RLUR (**0.831**) — **8.9% lower** than GFN, demonstrating an explicit trade-off where optimizing for long-term retention sacrifices some immediate satisfaction [15, 16].
  * **Live Online A/B Testing Results (Table 3 & Table 4):**
    * **Active Days (Users active within a 7-day window):**
      * *Behavior Cloning + Entropy Loss:* 1st Ranking (**+0.034%** Kuaishou, **+0.037%** Kuaishou Lite); 2nd Ranking (**+0.036%** Kuaishou, **+0.042%** Kuaishou Lite) [7].
      * *Additional gain from Multi-Level Expert Stratification:* **+0.028%** on Kuaishou, **+0.043%** on Kuaishou Lite [7].
      * *Cumulative Total Improvement:* **+0.098%** on Kuaishou, **+0.122%** on Kuaishou Lite [4, 7].
      * *DAU Business Impact:* Translates directly into **over 200,000 additional daily active users (DAU)** on each platform [4, 17, 18].
    * **User Interest Expansion (Table 4):** Valid interest clusters increased by **+1.31%** on Kuaishou and **+1.14%** on Kuaishou Lite [19].

---

💡 *Would you like to explore how SEC's multi-level expert stratification or action entropy regularization could be adapted to guide candidate profile selection for your dating platform's retention ranker?*

---

### Impatient Bandits: Optimizing for the Long-Term Without Delay [1]
`2025_JMLR_ImpatientBandits_Optimizing-Recommendations-Long-Term.md`
**Source:** https://arxiv.org/pdf/2501.07761.pdf  

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

### Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking [1]
`2025_KDD_NA_Interleaving-Counterfactual-Airbnb-Search.md`
**Source:** https://arxiv.org/pdf/2508.00751.pdf  

### **Source Evaluation: *Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking***
*(Zhang et al., Airbnb & Microsoft, KDD 2025: `arXiv:2508.00751`)* [1, 2]

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**

**Q1 only.** [1-3]  
* **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **Yes.** Published in August 2025 at KDD 2025 (`arXiv:2508.00751`), this paper describes a production evaluation and multi-session conversion attribution framework deployed live in production across Airbnb's search ranking infrastructure [1-3].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper focuses on evaluating candidate search rankers and attributing accommodation booking conversions across multi-session search journeys, rather than attributing user retention, active days, or return visits [1, 4, 5].

---

### **(B) Q2 Class**

**NOT.** [8, 10, 35–36]  
* **Justification:** The paper presents online experimentation and counterfactual evaluation frameworks (Interleaving and Counterfactual Evaluation) for accelerating search ranker evaluation, rather than publishing a per-exposure retention credit table or interaction-level retention attribution model [8, 10, 35–36].

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **Yes (at the search-occurrence and competitive-pair level)** [15, 26, 28, 39–41].
* **Target Outcome:** **Accommodation Booking Conversions** (and clicks) [1, 5]. Section 5.5 explicitly details that booking conversions are attributed across **all search occurrences** where a listing appeared during the experiment period, acknowledging the compound effect of repeated exposure across multi-session search journeys [5].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**

* **How it Improves on Last-Touch:** Section 5.5 explicitly rejects single-touch or last-touch rules for high-stakes multi-session user journeys, observing that decisions are influenced by every exposure across the user's journey rather than merely the final interaction [5].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Multi-Touch Journey Window:* Replaces last-touch post-hoc attribution by crediting 7-day retention across **all profile exposures, candidate swipes, and interactions** that occurred throughout the user's multi-session swiping journey during the evaluation period [5].
  2. *Counterfactual Ranker Evaluation:* Rather than waiting weeks for N7 retention signals in standard A/B testing, evaluates candidate profile rankers using counterfactual position-decay estimators (\\(\tau_g, \tau_{\text{oec}}\\)) on profile exposures, achieving **15x–100x speedups** in statistical power [9, 39–41, 55].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Competitive Pair Team Drafting:** Uses a single initial coin flip and alternating selection to eliminate position bias in interleaved result lists, ensuring each ranker has an equal 50% probability (\\(P(r=1) = P(r=2) = 0.5\\)) of occupying top positions [24–25, 29].
2. **Rank Similarity Thresholding (\\(\alpha = 2\\)):** Incorporates an equal-zone similarity threshold \\(\alpha = 2\\) in counterfactual reward estimation, setting incremental gain \\(g_i = 0\\) when position rank differences are minor (\\(|r_i(w) - r_i(1-w)| \le \alpha\\)) to eliminate noise from non-meaningful rank changes [40–41, 54].
3. **Automated Data Quality Checks:** Continuously monitors impression distribution and team first-place rates to verify unbiasedness in production [30–31, 51].

---

### **(F) Deployment & Production Dataset Evidence**

* **Production Deployment:** Fully deployed live in production on Airbnb's search ranking infrastructure and utilized to conduct over 100 search ranking experiments [3, 6, 7].
* **Validation Corpus:** Evaluated directly on a real-world production validation corpus of **29 interleaving–A/B test pairs** and **30 counterfactual–A/B test pairs** [8, 9].
* **Quoted Quantitative Results:**
  * **Interleaving Sensitivity & Speedup:** Achieved a **50x speedup** over traditional A/B testing (requiring 1/50th of the traffic to reach equal statistical power) [8, 10].
  * **Interleaving Alignment:** **82% directional alignment** with A/B test outcomes, with a point estimate correlation of **corr = 0.60** across 29 test pairs [8].
  * **Counterfactual Evaluation Speedup:** Achieved a **15x speedup** for \\(\tau_{\text{oec}}\\), **23x speedup** for \\(\tau_{\text{win-loss}}\\), and **100x speedup** for \\(\tau_g\\) compared to A/B testing [10, 11].
  * **Counterfactual Evaluation Correlations with A/B Tests (Table 2):**
    * \\(\tau_g\\) (Gain Estimator): **corr = 0.66** [12].
    * \\(\tau_{\text{oec}}\\): **corr = 0.65** [9].
    * \\(\tau_{\text{win-loss}}\\): **corr = 0.58** [12].
    * \\(\tau_{\text{diff}}\\): **corr = 0.55** [12].
    * \\(\tau_{\text{sim}}\\): **corr = -0.29** [12].
  * **Position Similarity Threshold Impact (Table 3):** Setting \\(\alpha = 2\\) yielded higher correlation (**0.66** for \\(\tau_g\\), **0.60** for \\(\tau_{\text{win-loss}}\\)) than setting \\(\alpha = 1\\) (**0.64** and **0.58**) [54–55].
  * **Unbiasedness Data Quality Verification (Table 1):**
    * Listings shown: **\\(\Delta = 0.00\%\\)** (\\(p = 0.91\\)) [13].
    * Shown first: **\\(\Delta = -0.01\%\\)** (\\(p = 0.85\\)) [13].
    * Shown reciprocal rank: **\\(\Delta = -0.02\%\\)** (\\(p = 0.85\\)) [13].
    * Listings found: **\\(\Delta = 0.00\%\\)** (\\(p = 0.95\\)) [13].

---

💡 *Would you like to explore how Airbnb's multi-session exposure attribution or counterfactual position-decay scoring (\\(\tau_g\\)) could be adapted to evaluate candidate profile rankers for your dating platform?*

---

### Buyer journey insights with data-driven attribution [1]
`2025_LinkedIn_LiDDA_Buyer-Journey-Data-Driven-Attribution.md`
**Source:** https://www.linkedin.com/blog/engineering/marketing/buyer-journey-insights-with-data-driven-attribution  

### **(A) Q1 or Q2 Alignment**

* **Q1 (Industry/Production Attribution 2025–2026):** **Yes.** Published on January 22, 2025 [1], this source details LinkedIn's production hybrid attribution platform deployed for internal product marketing and expanded to the LinkedIn Marketing Solutions (LMS) advertiser stack [1-3].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper models binary marketing conversion outcomes (\\(C\\)) rather than user retention or active days [4, 5].
* **Summary:** **Q1 only.**

---

### **(B) Q2 Class**

* **Classification:** **NOT**
* **Explanation:** The system generates multi-touch fractional credit for marketing conversion events (\\(C\\)), not for user retention, days-active, or return-visit outcomes [4, 5].

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **Yes.** The model passes the touchpoint sequence through self-attention Transformer layers, extracting the combined attention weight matrix and normalizing it so weights sum to 1.0 (\\(\sum w_i = 1.0\\)) [5, 6]. These normalized attention weights are directly interpreted as the percentage contribution of each individual touchpoint [5].
* **Target Outcome:** Binary conversion outcome \\(C\\) (whether a customer/member journey results in a conversion) [4, 5].

---

### **(D) Replacing Last-Touch N7 → Latest Swipes**

* **How it Improves on Last-Touch:** Last-touch assigns 100% credit to the final interaction, over-indexing on bottom-of-funnel conversion points while completely ignoring earlier touchpoints [7, 8]. This model encodes the entire historical interaction sequence \\(S = [p_1, p_2, \dots, p_T]\\) alongside Time Absolute Position Encodings (tAPE) and daily interval positional embeddings (\\(E_D\\)) [9-12]. Self-attention allocates fractional credit across all sequence elements based on their learned contribution to the final outcome [5, 6].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  * **Sequence Representation:** Encodes user interaction logs as sequential events \\(S = [\text{swipe}_1, \text{swipe}_2, \text{match}, \text{message}_1, \text{message}_2, \dots]\\) with tAPE encodings capturing irregular intra-day timing [9, 11, 12].
  * **Fractional Allocation:** Replaces 100% last-swipe credit with fractional self-attention weights, crediting earlier candidate profile swipes, mutual matches, and multi-way messaging conversations proportional to their impact on retention [5].
  * **Entity Controls:** Incorporates member embeddings (\\(E_M\\)) and company/candidate profile embeddings (\\(E_C\\)) passed through dense classification layers to control for baseline user swiping affinity [4, 6, 13].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Baseline Affinity Controls:** Feeds user representation vectors (\\(E_M\\)) and target entity vectors (\\(E_C\\)) through a dense layer into the binary classifier [4, 6, 13]. This controls for baseline conversion propensity (e.g., highly engaged users who convert regardless of exposure) [13].
2. **Paid Media Impression Imputation:** Solves missing non-click impression data by probabilistically imputing paid media impressions into member paths using owned-channel prior distributions [14, 15].
3. **Session-Level Downsampling:** Groups high-frequency owned-channel impressions within a single session into a single touchpoint to prevent frequent interactions from saturating fixed-length sequence paths [16].
4. **Top-Down MMM Post-Calibration:** Multiplies bottom-up MTA touchpoint credit by quarterly channel-level ratios derived from top-down Marketing Mix Modeling (MMM), calibrating local sequence weights to macroeconomic incrementality totals [17, 18].

---

### **(F) Deployment & Production Quantitative Results**

* **Deployment Status:** Deployed in production across LinkedIn's internal product marketing campaigns and integrated into the LinkedIn Marketing Solutions (LMS) measurement platform [2, 3, 8].
* **Reported Quantitative Numbers:**
  * **150x Increase in Upper/Mid-Funnel Credit:** Recognized a **150x increase in attributed conversion credit** for upper- and mid-funnel campaigns (Video Ads, Digital Display, Social Media) compared to Last-Click attribution, which delivered zero credit [19].
  * **5% Revenue Lift:** Enabled weekly in-quarter budget optimizations that delivered an estimated **5% lift in marketing-driven revenue** in FY25 [20].

---

💡 *Would you like to explore how LinkedIn's tAPE positional encodings or MMM post-calibration step could be adapted to balance your dating platform's per-swipe retention credit labels?*

---

