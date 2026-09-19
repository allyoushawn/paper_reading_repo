# Card summaries 12/12 — Summary and Evidence sections of all cards (generated)

### Incremental Recommendation via Causal Models [1]
`2026_arXiv_NA_Incremental-Recommendation-Causal-Models.md`
**Source:** https://arxiv.org/pdf/2608.26804.pdf  

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Incremental Recommendation via Causal Models* [1]
* **Authors:** **Athanasios Vlontzos**\*¹, **David Gustafsson**², **Michael O’Riordan**³, and **Ciarán M. Gilligan-Lee**⁴ (\*Work done while at Spotify) [1, 2]
* **Author Affiliations:**
  1. **Imperial College London / Hologen**, London, UK (`Hologen Imperial College London, UK`) [1]
  2. **Spotify**, Stockholm, Sweden (`davidgustafsson@spotify.com`) [1]
  3. **Spotify**, London, UK (`moriordan@spotify.com`) [1]
  4. **Spotify** (Ireland) & **University College London**, London, UK (`ciaranl@spotify.com`) [1]
* **Year:** **2026** (arXiv pre-print: `2608.26804`) [1, 3]
* **Venue:** arXiv pre-print (`arXiv:2608.26804`) / Conference pre-print [1]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Recommendation impressions are a finite resource. Delivering recommendations to users who would discover the content organically yields no incremental value and displaces other recommendations that could [1]. While platforms collect holdback data (withholding recommendations from a small randomized fraction of users), a fundamental structural obstacle prevents naive Conditional Average Treatment Effect (CATE) subtraction (\\(\hat{p}_1(\mathbf{x}) - \hat{p}_0(\mathbf{x})\\)): **Attribution Window Mismatch** [1, 5–7]. 
  * Treated users are attributed streams within a **short direct-response window** (minutes/hours) to isolate immediate exposure effects [5–6].
  * Holdback users are attributed organic streams over a **multi-day window (2-day window)** to capture slower organic discovery [4].
  * Naive subtraction (\\(\hat{p}_1 - \hat{p}_0\\)) is mathematically invalid because the two heads measure fundamentally different outcome definitions [5].
* **Key Contribution:**
  1. **Formalization of Attribution Window Mismatch:** Identifies and formalizes why direct CATE estimation fails when treated and control attribution windows differ [3, 5–7].
  2. **Deep Twin Network Extension:** Extends an existing multi-task production recommendation architecture into a Causal Deep Twin Network [6] by adding a holdback head trained on holdback data \\(\mathcal{D}_0\\) with partitioned losses [10–12].
  3. **Dual-Threshold Targeting Policy:** Introduces a policy \\(\pi(\mathbf{x}) = \mathbb{1}[\hat{p}_1(\mathbf{x}) \ge \theta_1] \cdot \mathbb{1}[\hat{p}_0(\mathbf{x}) \le \theta_0]\\) that uses both predicted probabilities as independent decision levers, targeting only users where recommendations are both effective (high \\(\hat{p}_1\\)) and necessary (low \\(\hat{p}_0\\)) [3, 13–14].
  4. **Production A/B Test Validation:** Demonstrates a **7% reduction in recommendation impressions** on millions of Spotify users with no statistically significant impact on recommended content consumption [1, 7, 8].
  5. **Generalization & Calibration Lifts:** Proves joint training with holdback supervision improves model calibration on the treated head [1, 3, 19–22].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Architectural Components**
* **Baseline Production Model:** Multi-task shared-trunk neural network mapped from (user, content) feature vector \\(\mathbf{x}\\) to shared representation \\(\mathbf{z}\\). Task heads predict engagement outcomes (streams, likes) exclusively from treated data \\(\mathcal{D}_1\\) [9–10].
* **Causal Deep Twin Network:** Retains the deep shared trunk and appends a holdback head trained on randomized holdback examples \\(\mathcal{D}_0\\) to predict organic stream probability \\(\hat{p}_0(\mathbf{x})\\) [10–11].
* **Partitioned Loss Function:**
  \\[\mathcal{L} = \frac{1}{|\mathcal{D}_1|} \sum_{i \in \mathcal{D}_1} \ell_{\text{bce}}(y_i, \hat{p}_1(\mathbf{x}_i)) + \frac{1}{|\mathcal{D}_0|} \sum_{j \in \mathcal{D}_0} \ell_{\text{bce}}(y_j, \hat{p}_0(\mathbf{x}_j))\\]
  Gradients from both treated and holdback arms flow back to shape the shared trunk \\(\mathbf{z}\\), but treated examples update *only* the treated head and holdback examples update *only* the holdback head [11–12].

#### **Dual-Threshold Targeting Policy**
* A recommendation is served if and only if [9]:
  \\[\pi(\mathbf{x}) = \mathbb{1}[\hat{p}_1(\mathbf{x}) \ge \theta_1] \cdot \mathbb{1}[\hat{p}_0(\mathbf{x}) \le \theta_0]\\]
  * \\(\theta_1\\): Threshold ensuring the recommendation is likely to drive a direct stream [9].
  * \\(\theta_0\\): Threshold filtering out "always-takers" who would stream organically regardless [9].

#### **Credit Assignment Mechanics**
* Credit is assigned to **individual candidate recommendation impressions** at serving time by evaluating short-window direct stream probability \\(\hat{p}_1(\mathbf{x})\\) against multi-day organic stream probability \\(\hat{p}_0(\mathbf{x})\\) [9, 10].
* It does **not** perform multi-touch sequence attribution over historical user touchpoints; rather, it uses counterfactual holdback prediction to prune non-incremental recommendations [2, 9, 11].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets & Scale:** Live production user interaction logs from Spotify, utilizing routine holdback infrastructure where recommendations are withheld from a small randomized fraction of eligible users [1–2].
* **Production Deployment:** Deployed live in production at **Spotify** on mobile and desktop recommendation surfaces, evaluated over a two-week A/B test on millions of users [1, 6, 12].
* **Comparison Baselines / Variants:**
  * **Production Baseline:** Multi-task shared-trunk model trained solely on treated examples \\(\mathcal{D}_1\\), targeting by \\(\mathbb{1}[\hat{p}_1(\mathbf{x}) \ge \theta_1]\\) [6, 10, 13].
  * **Treatment-Model:** Causal Deep Twin architecture model, but filtering using only the treated head \\(\mathbb{1}[\hat{p}_1(\mathbf{x}) \ge \theta_1]\\) (isolating the shared trunk representation effect) [6].
  * **Treatment-Causal:** Full Causal Deep Twin model with the Dual-Threshold Policy (\\(\mathbb{1}[\hat{p}_1(\mathbf{x}) \ge \theta_1] \cdot \mathbb{1}[\hat{p}_0(\mathbf{x}) \le \theta_0]\\)) [6].

---

### **(5) Key Quantitative Results with Numbers**

* **Live Production A/B Test (Treatment-Causal vs. Treatment-Model over 2 weeks, Table 1):**
  * **Recommendation Impressions per user:** **-7.1%** (`[-7.2%, -6.9%]`, 95% CI) — achieving a **7% reduction** in recommendation slot usage [8].
  * **Recommended Content Consumption Minutes:** **-0.37%** (`[-0.86%, +0.21%]`, 95% CI) — **no statistically significant reduction** in overall consumption of recommended content or user satisfaction guardrails [8].
* **Backend vs. Client-Side Discrepancy:** Identified an approximate **30% discrepancy** between backend recommendation servings (holdback log events) and client-side impressions (treated log events) due to network latency and client-side rendering differences [14].
* **Model Calibration Improvement:** The causal treated head tracked the diagonal calibration line noticeably closer than the production baseline, particularly at higher predicted probabilities (Figure 4) [19–20].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Failure of Direct CATE Subtraction (\\(\hat{p}_1 - \hat{p}_0\\)):** Direct subtraction fails and provides no valid causal interpretation due to the attribution window mismatch (short direct-response window for treated vs. 2-day organic window for holdback) [5].
2. **Distributional Gap Between Backend and Client Logs:** The **~30% discrepancy** between backend recommendation servings and client-side impressions creates additional feature space divergence between \\(\mathcal{D}_1\\) and \\(\mathcal{D}_0\\) [14].
3. **Threshold Sensitivity Trade-Off:** Aggressively decreasing \\(\theta_0\\) saves more impressions but risks withholding recommendations from users who might have provided incremental streams [15].
4. **Prerequisite of Holdback Infrastructure:** Requires access to continuous randomized holdback experiment data; platforms without existing holdback infrastructures cannot train the holdback head [2].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Shalit, Johansson, & Sontag (2017) [Ref 15]:** *Estimating individual treatment effect: generalization bounds and algorithms* (TARNet / CFR) [16, 17].
2. **Shi, Blei, & Veitch (2019) / DragonNet [Ref 16]:** *Adapting Neural Networks for the Estimation of Treatment Effects* [16-18].
3. **Deep Twin Networks [Ref 17]:** *Deep Twin Networks for CATE Estimation* [16, 17, 19].
4. **Ma et al. (2018) [Ref 11 / ESSM]:** *Entire Space Multi-Task Model: An Effective Approach for Estimating Post-Click Conversion Rate* [10, 20].
5. **Schnabel et al. (2016) [Ref 14]:** *Recommendations as Treatments: Debiasing Learning and Evaluation* [11, 17].
6. **Rubin (1974) [Ref 13]:** *Estimating causal effects of treatments in randomized and nonrandomized studies* (Potential Outcomes Framework) [12, 17].
7. **Gutierrez & Gérardy (2017) [Ref 9]:** *Causal Inference and Uplift Modeling: A Review of the Literature* [16, 21].

---

💡 *Would you like to explore how Spotify's dual-threshold policy (\\(\pi(\mathbf{x})\\)) or holdback Deep Twin Network architecture could be adapted to prune non-incremental candidate profile impressions for your dating platform?*

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling [1]
`2026_arXiv_OCARM_Post-Conversion-Content-Retention.md`
**Source:** https://arxiv.org/pdf/2604.25839.pdf  

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**

* **Title:** *Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling* [1]
* **Authors:** **Tianbao Ma**\*¹, **Ruochen Yang**\*¹, **Chengen Li**¹, **Yuexin Shi**¹, **Jiangxia Cao**†¹, **Linxun Chen**¹, **Zhaojie Liu**¹, **Yanan Niu**¹, **Han Li**¹, and **Kun Gai**¹ (\*Equal contributions, †Corresponding author) [1, 2]
* **Affiliations:** **Kuaishou Technology**, Beijing, China (`{matianbao, yangruochen, lichengen, shiyuexin, caojiangxia, chenxi36, zhaotianxing, niuyanan, lihan08}@kuaishou.com`, `gai.kun@qq.com`) [1]
* **Year:** **2026** (arXiv pre-print: `2604.25839`) [1]
* **Venue:** arXiv pre-print (`arXiv:2604.25839`) / Conference pre-print [1]

---

### **(2) Core Problem and Key Contribution**

* **Core Problem:** In Real-Time Bidding (RTB) advertising systems for user re-engagement and growth, retention models must predict a user's future revisit probability at bidding time—before the user converts (clicks to open the app) and consumes any content [1, 3]. While post-conversion content consumption ("Onboarding Content"—videos watched, interactions performed post-conversion) carries exceptionally strong predictive signals for retention, it is strictly inaccessible during bidding [4–5]. Directly incorporating onboarding content into training causes severe feature leakage and an irreconcilable training-serving distribution gap [4].
* **Key Contributions:**
  1. **Problem Formulation:** Identifies the "temporal inaccessibility boundary" at conversion in RTB retention modeling and formulates the task of Onboarding Content Augmented Retention Modeling [3, 5].
  2. **OCARM Framework:** Proposes **OCARM**, a two-stage distillation-aligned framework:
     * *Stage 1:* Deliberately leaks post-conversion onboarding content during training to train a Hierarchical Attention Encoder (HAE) that produces high-quality teacher representations [8, 11–14].
     * *Stage 2:* Trains a user Sequence Fusion Encoder (SFE) on observable pre-conversion user features (profiles, historical behavior, ad contexts) aligned with the frozen teacher representations via distillation loss with a stop-gradient operator [8, 15–20].
  3. **Industrial Deployment & Validation:** Demonstrates significant retention gains on a billion-scale short-video platform dataset and in live RTB online A/B testing [8, 23–28].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Architectural Components**
1. **Stage 1 — Onboarding Content Leakage Encoding (Teacher):**
   * Processes raw post-conversion onboarding content \\(x_c = \{v_0, v_1, \dots, v_n\}\\) across \\(D\\) calendar days [10–11].
   * *Intra-day Cross-Attention:* Queries the first \\(N\\) item embeddings of each day \\(d\\) using user profile vector \\(x_u\\) to produce compact daily representations \\(s^{(d)}\\) [11–12].
   * *Inter-day Causal Self-Attention:* Applies a causal mask over daily representations \\(\{s^{(1)}, \dots, s^{(D)}\}\\) to capture chronological engagement evolution without future-day leakage [6].
   * *Joint Training:* Teacher embedding \\(e_c = \text{MLP}(s)\\) is concatenated with retention features to train the retention model \\(f_{\text{retention}}([x_u; e_c])\\) under binary cross-entropy (BCE) loss [7, 8].
2. **Stage 2 — User Representation Distillation Alignment (Student):**
   * *Sequence Fusion Encoder (SFE):* Conditions observable historical interaction sequences \\(x_s^{(i)}\\) and ad contexts \\(x_s^{(a)}\\) on user profile \\(x_u\\) [17–18]. Uses learnable query tokens and sequence-specific Q-Former modules to compress variable-length behavior sequences into fixed-length interest representations \\(s^{(m)}\\) [9].
   * *Task Towers:* Maps \\([x_u; s^{(m)}]\\) to task-specific user representations \\(e_u^{(t)}\\) for retention horizons (e.g., \\(LT1\\), \\(LT7\\)) [18–19].
   * *Distillation Alignment Loss:* Minimizes the representation gap between student representation \\(e_u^{(t)}\\) and stop-gradient frozen teacher representation \\(\text{sg}(e_c^{(t)})\\):
     \\[L_{\text{align}} = \sum_{t \in \text{Task}} L_{\text{sim}}(e_u^{(t)}, \text{sg}(e_c^{(t)}))\\]
     Jointly optimized with retention task loss: \\(L_{\text{Stage2}} = \text{BCE}(f_{\text{retention}}([x_u; e_u]), y) + \lambda L_{\text{align}}\\) [19–20, 22].
3. **Inference Execution:**
   * Discards the onboarding content teacher encoder (HAE). Online inference uses only SFE to compute \\(g_u(x_u)\\) from pre-conversion observable features, evaluating \\(y = f_{\text{retention}}([x_u; g_u(x_u)])\\) without feature leakage [15, 22–23].

#### **Credit Assignment Mechanics**
* Credit is **not** assigned as fractional attribution scores to individual touchpoints, swipes, or ad exposures [10, 18–20].
* The model predicts multi-horizon user retention revisit frequencies (\\(LT_d\\), e.g., \\(LT1\\), \\(LT7\\), \\(LT30\\)) at bidding time by distilling latent representations of post-conversion onboarding content into the user encoder [10, 18–20].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets & Scale:** Industrial offline dataset collected from Kuaishou short-video platform containing millions of users and billions of interaction records [10].
* **Production Deployment:** Deployed live in the Real-Time Bidding (RTB) advertising system of Kuaishou Technology for user re-engagement and growth campaigns [1, 11].
* **Comparison Baselines & Variants:**
  * **Base Model:** Production PPNET (Parameter and Embedding Personalized Network) retention model [12].
  * **Variant 1:** MLP content encoder + MLP user encoder [21–22, 27].
  * **Variant 2:** HAE content encoder + MLP user encoder [13, 14].
  * **Variant 3 (Full OCARM):** HAE content encoder + SFE user encoder [21–22, 27].
  * **Stage 1 Upper Bound:** OCARM w/ Stage 1 (deliberately leaking onboarding content during evaluation) [21, 24–26].
  * **Stage 2 Alone:** Jointly training HAE and SFE without pre-trained frozen teacher representations [15, 16].

---

### **(5) Key Quantitative Results with Numbers**

* **Offline Retention Benchmark Results (Table 1 & Table 2):**
  * **Base Model:** \\(LT1\\) AUC = **0.7297**, GAUC = **0.7227**; \\(LT7\\) AUC = **0.6903**, GAUC = **0.6909** [15].
  * **Stage 1 Upper Bound (With Leaked Onboarding Content):** \\(LT1\\) AUC = **0.7468** (+1.71% AUC), GAUC = **0.7371**; \\(LT7\\) AUC = **0.7002** (+0.99% AUC), GAUC = **0.7007** [15].
  * **Full OCARM (Stage 1 + Stage 2 Distillation):** \\(LT1\\) AUC = **0.7369** (+0.72% AUC absolute gain over base), GAUC = **0.7311**; \\(LT7\\) AUC = **0.6949** (+0.46% AUC absolute gain over base), GAUC = **0.6957** [21–22].
  * **Ablation Variants (\\(\Delta\\)AUC over Base, Table 2):**
    * *Variant 1 (MLP + MLP):* \\(LT1\ \Delta\text{AUC} = \mathbf{+0.35\%}\\), \\(LT7\ \Delta\text{AUC} = \mathbf{+0.23\%}\\) [13].
    * *Variant 2 (HAE + MLP):* \\(LT1\ \Delta\text{AUC} = \mathbf{+0.56\%}\\), \\(LT7\ \Delta\text{AUC} = \mathbf{+0.32\%}\\) [13].
    * *Variant 3 (HAE + SFE - Full OCARM):* \\(LT1\ \Delta\text{AUC} = \mathbf{+0.72\%}\\), \\(LT7\ \Delta\text{AUC} = \mathbf{+0.46\%}\\) [13].
* **Live Online A/B Test Lifts (Table 3, RTB User Growth Scenario):**
  * **Non-Uninstalled Users:** Re-engaged Devices = **+20.468%**, \\(LT30\\) Retention = **+11.548%** [17].
  * **Uninstalled Users:** Re-engaged Devices = **+34.430%**, \\(LT30\\) Retention = **+22.179%** [17].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Failure of Direct Joint Training (Stage 2 Alone):** Jointly training the content encoder (HAE) and user encoder (SFE) without a frozen Stage-1 teacher leads to severe performance degradation (\\(LT1\\) AUC drops from **0.7297 down to 0.6709**), causing representation collapse due to optimization instability without a fixed teacher signal [15, 16].
2. **Remaining Performance Gap to Upper Bound:** Although OCARM recovers a significant portion of the retention signal (\\(LT1\\) AUC **0.7369** vs base **0.7297**), a gap remains relative to the true upper bound (\\(LT1\\) AUC **0.7468**), showing inherent limits when approximating unobserved future interactions from historical priors [14, 15].
3. **Temporal Staleness of Historical Behavior:** Historical interaction logs of re-engaged users are far removed from bidding time, creating temporal staleness that limits their predictive power compared to actual onboarding content [18].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Cai et al. (2023) [Ref 2]:** *Reinforcing user retention in a billion scale short video recommender system* (WWW '23) [19].
2. **Chang et al. (2023) [PepNet / Ref 4]:** *Pepnet: Parameter and embedding personalized network for infusing with personalized prior information* (KDD '23) [20].
3. **Liu et al. (2024) [GFN4Retention / Ref 6]:** *Modeling user retention through generative flow networks* (KDD '24) [21].
4. **Zhao et al. (2023) [Decision Transformer / Ref 9]:** *User retention-oriented recommendation with decision transformer* (WWW '23) [22].
5. **Li et al. (2023) [BLIP-2 / Q-Former / Ref 5]:** *Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models* (ICML '23) [21].
6. **Wang et al. (2025) [Ref 8]:** *Not All Impressions Are Created Equal: Psychology-Informed Retention Optimization for Short-Form Video Recommendation* (RecSys '25) [23].
7. **Bie et al. (2026) [PushGen / Ref 1]:** *PushGen: Push Notifications Generation with LLM* (WSDM '26) [19].

---

💡 *Would you like to explore how OCARM's onboarding distillation framework or Q-Former sequence fusion architecture could be adapted to model pre-conversion retention signals for your dating platform?*

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

