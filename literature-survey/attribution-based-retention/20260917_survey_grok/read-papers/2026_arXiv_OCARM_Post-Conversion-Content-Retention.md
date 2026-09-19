# Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling [1]

**Source:** https://arxiv.org/pdf/2604.25839.pdf  
**Date analyzed:** 2026-09-18  
**NLM source id:** `7f131324-1d54-4dd2-8a1c-98f5f0ce8dfd`  
**Queue id:** G11  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**

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

### **Source Evaluation: OCARM (*Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling*)**
*(Ma et al., Kuaishou Technology, 2026: `arXiv:2604.25839`)* [1]

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**

* **Neither.** [1, 2]
* **Explanation:**
  * **Q1 (Industry/Production Attribution 2025–2026):** **No.** While published on arXiv in April 2026 (`arXiv:2604.25839`) and deployed in a live Real-Time Bidding (RTB) ad system [1, 3], OCARM is a predictive representation distillation framework for bidding decisions [1, 4], not a multi-touch attribution (MTA) measurement system.
  * **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** It forecasts future user revisit frequency (\\(LT_d\\), e.g., \\(LT1\\), \\(LT7\\)) prior to app conversion [2, 5], rather than performing historical multi-touch sequence attribution over individual past swiping or messaging interactions [4, 5].

---

### **(B) Q2 Class**

* **Classification:** **NOT** [8, 15–20]
* **Justification:** OCARM is a predictive representation model that trains a student user encoder (Sequence Fusion Encoder, SFE) to align with a frozen teacher content encoder (Hierarchical Attention Encoder, HAE) via representation distillation (\\(L_{\text{align}}\\)) [8, 18–20]. It does **not** publish a per-exposure or per-swipe retention credit table or multi-touch attribution model [4, 5].

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction credit.** [10, 18–20]
* **Target Outcome:** **User revisit frequency over the next \\(d\\) days (\\(LT_d\\), e.g., \\(LT1\\), \\(LT7\\), \\(LT30\\))** [5-7].
* **Mechanics:** The model produces unified, task-specific user representation vectors \\(e_u\\) at bidding time [18–19] without calculating fractional credit or attribution scores for individual touchpoints, swipes, or ad impressions.

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**

* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% of the binary N7 retention label to recent swipes post-hoc. OCARM replaces post-hoc last-touch rule assignment by predicting long-term retention probability \\(LT_d\\) prior to user interaction [4, 8, 10, 22–23]. It overcomes the "temporal inaccessibility boundary" by training a teacher model on post-conversion "onboarding content" (e.g., matches, 4-way conversations, profile views after returning) [4, 8, 11–14] and distilling those future engagement signals into a student encoder that uses only pre-conversion observable user features [8, 15–20].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Pre-Conversion Observable Features (\\(x_u, x_s\\)):* Static user profiles, historical swiping/matching logs, and ad context features fed into the Sequence Fusion Encoder (SFE) via Q-Former query tokens [10, 17–18].
  2. *Post-Conversion Onboarding Content (\\(x_c\\)):* The rich sequence of interactions a user experiences upon returning—such as early candidate swipes, mutual matches, and deep 4-way messaging conversations across days 1–7 [4, 10, 11–13].
  3. *Teacher Encoder (HAE):* Uses intra-day cross-attention and inter-day causal self-attention to encode post-conversion onboarding engagement patterns into retention-predictive embeddings \\(e_c\\) [11–14].
  4. *Distillation Alignment (\\(L_{\text{align}}\\)):* Teaches the student user encoder \\(e_u\\) to anticipate whether a user's pre-conversion profile and history will lead to high-value post-conversion conversations and 7-day retention (\\(LT7\\)) [15, 19–20].

---

### **(E) Selection-Bias & Confounding Handling**

* **Not specified in source.**
* The paper focuses on resolving the temporal inaccessibility boundary and training-serving distribution gap via representation distillation [1, 4, 8, 19–20], rather than applying propensity score weighting (IPW), counterfactual estimation, or explicit selection-bias debiasing.

---

### **(F) Deployment and Production Dataset Evidence**

* **Production Deployment:** Deployed live in the Real-Time Bidding (RTB) advertising system of Kuaishou Technology for user re-engagement and growth campaigns [3].
* **Dataset:** Industrial dataset collected from Kuaishou short-video platform containing **millions of users and billions of interaction records** [8].
* **Quoted Quantitative Results:**
  * **Offline Retention Benchmark Performance (Table 1):**
    * *Base Model (PPNET):* \\(LT1\\) AUC = **0.7297**, GAUC = **0.7227**; \\(LT7\\) AUC = **0.6903**, GAUC = **0.6909** [9].
    * *Stage 1 Upper Bound (Deliberately Leaking Onboarding Content):* \\(LT1\\) AUC = **0.7468** (+1.71% AUC gain), GAUC = **0.7371**; \\(LT7\\) AUC = **0.7002** (+0.99% AUC gain), GAUC = **0.7007** [9].
    * *Stage 2 Alone (Without Frozen Teacher):* Severely degraded to \\(LT1\\) AUC = **0.6709**, GAUC = **0.6719**; \\(LT7\\) AUC = **0.6430**, GAUC = **0.6435** [9, 10].
    * *Full OCARM (Stage 1 + Stage 2 Distillation):* \\(LT1\\) AUC = **0.7369** (+0.72% AUC absolute gain over base), GAUC = **0.7311**; \\(LT7\\) AUC = **0.6949** (+0.46% AUC absolute gain over base), GAUC = **0.6957** [9].
  * **Encoder Architecture Ablations (\\(\Delta\text{AUC}\\) over Base, Table 2):**
    * *Variant 1 (MLP Content + MLP User):* \\(LT1\ \Delta\text{AUC} = \mathbf{+0.35\%}\\), \\(LT7\ \Delta\text{AUC} = \mathbf{+0.23\%}\\) [11].
    * *Variant 2 (HAE Content + MLP User):* \\(LT1\ \Delta\text{AUC} = \mathbf{+0.56\%}\\), \\(LT7\ \Delta\text{AUC} = \mathbf{+0.32\%}\\) [11].
    * *Variant 3 (Full OCARM: HAE Content + SFE User):* \\(LT1\ \Delta\text{AUC} = \mathbf{+0.72\%}\\), \\(LT7\ \Delta\text{AUC} = \mathbf{+0.46\%}\\) [11].
  * **Live Online RTB A/B Test Results (Table 3):**
    * *Non-Uninstalled Users:* Re-engaged Devices = **+20.468%**, \\(LT30\\) Retention = **+11.548%** [7].
    * *Uninstalled Users:* Re-engaged Devices = **+34.430%**, \\(LT30\\) Retention = **+22.179%** [7].

---

💡 *Would you like to explore how OCARM's onboarding distillation framework or Q-Former sequence fusion architecture could be adapted to model pre-conversion retention signals for your dating platform?*

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
**Priority:** see queue.md `G11`
