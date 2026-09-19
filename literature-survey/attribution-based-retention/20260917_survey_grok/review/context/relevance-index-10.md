# Relevance index 10/10 — Project Relevance sections of all cards (generated)

### Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling [1]
`2026_arXiv_OCARM_Post-Conversion-Content-Retention.md`
**Source:** https://arxiv.org/pdf/2604.25839.pdf  

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

