# ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization [1]

**Source:** https://arxiv.org/pdf/2605.08881.pdf  
**Date analyzed:** 2026-09-18  
**NLM source id:** `42ed27d5-3e90-483f-b728-e5cdab72cfcd`  
**Queue id:** G12  
**Q2 class:** NOT

---

## 1. Summary

### **Part 1: Dating App Retention Project Evaluation**

#### **(A) Alignment: Q1 or Q2 or Both or Neither?**
* **Q1 (Industry/Production Attribution 2025–2026):** **Yes.** Published in May 2026 (`arXiv:2605.08881`), this paper describes a production causal Multi-Touch Attribution (MTA) system deployed at Kuaishou Technology on a recommendation engine serving **400 million Daily Active Users (DAU)** and evaluated over **30 billion training samples** [1-3].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper attributes user content consumption touchpoints to **content creation / video upload behavior (\\(Y \in \{0, 1\}\\))** (the Consumption Drives Production / CDP ecosystem), rather than user retention, active days, or return visits [1, 3, 4].
* **Summary:** **Q1 only.**

---

#### **(B) Q2 Class**
* **Classification:** **NOT** [1, 3, 4].
* **Justification:** The system computes causal multi-touch attribution credit for content creation / video upload conversion events (\\(Y\\)), not for user retention or active days.

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Yes.** It produces a per-touchpoint causal uplift credit score \\(\hat{\Delta}(\tau_j \mid X, T) = g_\theta(X, T) - g_\theta(X, T \setminus \{\tau_j\})\\), defined as the counterfactual drop in predicted upload probability when touchpoint \\(\tau_j\\) is deleted from the user's sequential consumption history [4-6].
* **Target Outcome:** Binary content creation / video upload event (\\(Y \in \{0, 1\}\\)) within the consumption sequence horizon [3, 4].

---

#### **(D) Replacing Last-Touch N7 → Latest Swipes**
* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% credit to the final interaction before conversion, ignoring earlier touchpoints and failing under system/sequence-level unobserved confounding [7]. ALM-MTA calculates the counterfactual marginal uplift of deleting a specific item from the historical sequence using front-door identification and an adversarially learned mediator (\\(\hat{M}\\)), isolating true causal contribution from unobserved confounders (e.g., system recommendation strategies or latent user intent) [5, 7-9].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  * **Sequence Representation:** \\(T = \langle \text{swipe}_1, \text{swipe}_2, \text{match}_1, \text{conversation}_1, \dots \rangle\\) representing the user's sequential in-app interaction journey [3, 4].
  * **Counterfactual Removal Uplift:** Replaces last-touch with counterfactual deletion uplift \\(\Delta(\text{swipe}_j) = P(\text{Retention} \mid \text{do}(T)) - P(\text{Retention} \mid \text{do}(T \setminus \{\text{swipe}_j\}))\\), evaluating how removing a specific swipe or early mutual match reduces the predicted 7-day retention probability [4, 13–14].
  * **Mediator & Front-Door Adjustment:** Uses an adversarial proxy mediator \\(\hat{M}\\) (e.g., intermediate interaction depth, messaging engagement velocity) to block unobserved user activity/intent confounders (\\(W\\)), ensuring that credit assigned to early candidate swipes reflects true causal incrementality rather than selection bias [15, 20, 55–56].

---

#### **(E) Selection-Bias & Confounding Handling**
1. **Front-Door Causal Identification:** Leverages front-door adjustment via a latent mediator \\(M\\) (rendered observable via an adversarially trained proxy \\(Y'\\) invariant to outcome \\(Y\\)) to block unobserved system-level and sequence-level confounders \\(W\\) [5, 8-10].
2. **Inverse Propensity Weighting (IPW):** Reweights observational consumption logs using \\(w(X, T) = 1 / P_{\text{obs}}(T = t \mid X = x)\\) to eliminate backdoor confounding from observed covariates \\(X \to T\\) [17, 21–22].
3. **Contrastive Overlap Control:** Uses InfoNCE-based contrastive learning between touchpoints \\(T\\) and proxy mediator \\(Y'\\) to restrict front-door marginalization to the top-\\(K\\) high-match subset \\(\tau_{\text{high}}\\), maintaining positivity/overlap in high-cardinality treatment spaces [11, 12].

---

#### **(F) Deployed or Production Dataset Evidence**
* **Production Deployment:** Deployed in real-world production at Kuaishou Technology on a recommendation engine serving **400 million Daily Active Users (DAU)** [1, 2, 13].
* **Production Dataset:** Trained on **100 consecutive days of online logs** generating over **30 billion training instances** with a candidate treatment space reaching the **billion level** [1, 3].
* **Quoted Quantitative Results:**
  * **Production Online A/B Test Lifts:**
    * **Daily Active Users (DAU):** **+0.04%** [1, 2, 13].
    * **Daily Active Creators:** **+0.6%** [1, 2, 13].
    * **Unit Exposure Efficiency:** Increased by **670%** (production traffic efficiency **+0.504%**, uploads per user **+0.569%**) [1, 2, 13].
    * **Addressable Creator Scale:** Expanded by **+0.119%**; Producer WAU **+0.566%** [13].
    * **Attributable Upload Coverage:** Expanded by **1.5x** (upload coverage increased from 0.39 to 0.58 under threshold 0.54) [2, 13].
    * **Touchpoint Granularity:** Average attributed touchpoints per upload increased from 2.93 to 7.31 (**2.49x**) [13].
    * **Attribution Accuracy:** Precision increased from **4.32% to 21.88%**, Recall increased from **7.95% to 11.67%** (top-score bucket precision reached **54%**) [13].
  * **Offline Evaluation Metrics (Table 2):**
    * **AUC:** **0.9070** (vs SOTA causalMTA 0.8167, deepMTA 0.7598, DML 0.6498, DESCN 0.5492, LR 0.5102) — **+40% improvement over prior SOTA** [1, 2, 14].
    * **Log Loss:** **0.1384** (vs causalMTA 0.2835, deepMTA 0.4108, LR 0.7833) [14].
    * **gAUC:** **0.8210** (vs causalMTA 0.6752, deepMTA 0.6364, DML 0.5031) [14].
    * **Grouped AUUC (avg AUUC):** **0.8686** (vs causalMTA 0.8493, DESCN 0.8429, DML 0.8421, deepMTA 0.6277, LR 0.4725) — maximum gain of **+0.070** across propensity buckets [1, 2, 14].

---

### **Part 2: Detailed Technical Breakdown of the Source**

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization* [1]
* **Authors:** **Yuguang Liu**\*¹, **Luyao Xia**\*², **Hu Liu**\*¹, **Zhangxi Yan**¹, **Jian Liang**¹, **Han Li**¹, and **Kun Gai**¹ (\*Equal contribution) [1]
* **Affiliations:**
  1. **Kuaishou Technology**, Beijing, China (`{liuyuguang, yanzhangxi, liangjian03, lihan08, yuyue06}@kuaishou.com`) [1]
  2. **The University of Auckland**, Auckland, New Zealand (`luyao.xia@auckland.ac.nz`) [1]
* **Year:** **2026** (May 2026) [1]
* **Venue:** arXiv e-print (`arXiv:2605.08881`) / Conference pre-print [1]

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Multi-touch attribution (MTA) in platform-mediated creator economies (Consumption Drives Production / CDP) aims to quantify how historical user content consumption touchpoints induce creation (video uploads). However, MTA faces three major bottlenecks: (i) absence of explicit ground-truth causal labels, (ii) pervasive multi-source unobserved system- and sequence-level confounding (rendering backdoor adjustments alone insufficient), and (iii) severe non-positivity/overlap violations in billion-scale, high-cardinality treatment spaces [1–2, 15, 16].
* **Key Contributions:**
  1. **ALM-MTA Framework:** Introduces Adversarial Learning Mediator based Multi-Touch Attribution, an extensible front-door causal MTA framework that deconfounds unobserved system-level variables [1, 4–5, 17].
  2. **Adversarial Proxy Mediation:** Renders the latent "inspiration" mediator \\(M\\) observable via a proxy variable \\(Y'\\) while using adversarial gradient reversal to suppress outcome leakage (\\(Y' \to Y\\)), satisfying front-door conditional independence [1, 5, 9, 10].
  3. **Contrastive Overlap Control:** Employs an InfoNCE contrastive module between touchpoints and proxy mediator to restrict front-door marginalization to high-match treatment pairs, preserving positivity in high-cardinality treatment spaces [1, 11, 12].
  4. **Industrial Validation:** Deployed on Kuaishou serving 400M DAU, achieving significant gains in creator activation, attribution coverage, precision, and grouped AUUC [1, 2, 13, 14].

---

#### **(3) Proposed Method or Architecture in Detail**
* **Architecture Pipeline:**
  1. *IPW Reweighting:* Reweights observational consumption logs using Inverse Propensity Weighting \\(w(X, T) = 1 / P_{\text{obs}}(T = t \mid X = x)\\) to handle backdoor confounding from observed covariates \\(X \to T\\) [6, 15].
  2. *Shared Backbone Encoder:* Processes user context features \\(X\\) and chronological touchpoint sequence \\(T\\) [6, 16].
  3. *Weighted ITE Head:* Aggregates touchpoint embeddings with learned weights to output logit for \\(P(Y \mid X, T)\\). Calculates counterfactual removal uplift \\(\hat{\Delta}(\tau_j \mid X, T) = g_\theta(X, T) - g_\theta(X, T \setminus \{\tau_j\})\\) [4, 6].
  4. *Mediator Observation & Adversarial Head:* Supervised by proxy \\(Y'\\) (e.g., music/template/semantic match between consumed and uploaded content). A discriminator attempts to predict upload \\(Y\\) from mediator representation \\(\hat{M}\\); adversarial learning suppresses outcome leakage so \\(\hat{M}\\) contains only causal pathway information \\(T \to M \to Y\\) [6, 9, 10].
  5. *Contrastive Overlap Module:* Computes semantic alignment score \\(\omega(\tau, Y')\\) via InfoNCE loss; restricts front-door marginalization to top-\\(K\\) high-match touchpoints \\(\tau_{\text{high}}\\) [11, 12].
* **Credit Assignment Mechanics:** Credit is assigned **per touchpoint item \\(\tau_j\\)** in the consumption sequence \\(T\\). The credit score equals the counterfactual drop in predicted upload probability when that specific touchpoint is removed from the sequence (\\(\hat{\Delta}(\tau_j)\\)), grounded in front-door causal marginalization [4-6].

---

#### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets:**
  * *Industrial Production Dataset:* 100 consecutive days of online logs from Kuaishou Technology, yielding over **30 billion training instances** across a candidate treatment space at the **billion level** [1, 3].
  * *Public Criteo Conversion Dataset:* 30 days of display ad logs (average touchpoint sequence length 2.68, max length 880) used for external baseline comparisons under cost constraints [25, 74–76].
* **Production Deployment:** Deployed in real-world production at Kuaishou Technology on a recommendation engine serving **400 million Daily Active Users (DAU)** [1, 2, 13].
* **Comparison Baselines:**
  * *Statistical Learning:* Logistic Regression (LR) [14, 17].
  * *Deep Learning:* deepMTA, CAMTA [14, 17, 18].
  * *Causal Learning:* Double Machine Learning (DML), DESCN, causalMTA [14, 17, 18].

---

#### **(5) Key Quantitative Results with Numbers**
* **Offline Benchmark Results (Table 2):**
  * **AUC:** **0.9070** (vs causalMTA 0.8167, deepMTA 0.7598, DML 0.6498, DESCN 0.5492, LR 0.5102) — **+40% improvement over prior SOTA** [1, 2, 14].
  * **Log Loss:** **0.1384** (vs causalMTA 0.2835, deepMTA 0.4108, LR 0.7833) [14].
  * **gAUC:** **0.8210** (vs causalMTA 0.6752, deepMTA 0.6364, DML 0.5031) [14].
  * **Grouped AUUC (avg AUUC):** **0.8686** (vs causalMTA 0.8493, DESCN 0.8429, DML 0.8421, deepMTA 0.6277, LR 0.4725) — maximum gain of **+0.070** across propensity buckets [1, 2, 14].
* **Live Online A/B Test Lifts (Kuaishou 400M DAU Platform):**
  * **Platform DAU:** **+0.04%** [1, 2, 13].
  * **Daily Active Creators:** **+0.6%** [1, 2, 13].
  * **Unit Exposure Efficiency:** Increased by **670%** (production traffic efficiency **+0.504%**, uploads per user **+0.569%**) [1, 2, 13].
  * **Addressable Creator Scale:** **+0.119%**; Producer WAU **+0.566%** [13].
  * **Attributable Upload Coverage:** Expanded by **1.5x** (0.39 \\(\to\\) 0.58) [2, 13].
  * **Touchpoint Granularity:** Average attributed touchpoints per covered upload increased from 2.93 to 7.31 (**2.49x**) [13].
  * **Attribution Accuracy:** Precision increased from **4.32% to 21.88%**, Recall increased from **7.95% to 11.67%** (top-score bucket precision reached **54%**) [13].

---

#### **(6) Limitations, Failure Modes, or Negative Results**
1. **Outcome Leakage in Direct Mediator Observation:** Direct observation of proxy mediator \\(Y'\\) without adversarial learning leads to severe outcome leakage and training instability, causing large loss oscillations and failure to converge (Figure 5a) [30–32].
2. **Backdoor Adjustment Failure:** Standard backdoor methods (DML) achieve an offline AUC of only **0.6498** and UAUC of **0.50**, proving that backdoor adjustment alone cannot resolve unobserved system-level confounding [19].
3. **High Initial Training Loss:** Multi-task learning (MTL) with adversarial and contrastive heads causes higher initial loss during training compared to standard single-task baselines (Figure 5c) [31–33].
4. **Simplifying Assumptions:** Relies on linear aggregability of touchpoint uplift and touchpoint independence assumptions; future work is needed to capture higher-order touchpoint interactions (e.g., via leave-one/two-out inference or multi-head attribution) [20, 21].

---

#### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Yao et al. (2022) [causalMTA]:** *CausalMTA: Eliminating the user confounding bias for causal multi-touch attribution* (KDD '22) [7, 22].
2. **Ren et al. (2018) [Dual-Attention MTA]:** *Learning multi-touch conversion attribution with dual-attention mechanisms for online advertising* (CIKM '18) [23, 24].
3. **Chernozhukov et al. (2018) [DML]:** *Double/debiased machine learning for treatment and structural parameters* (Econometrics Journal) [17, 25].
4. **Zhong et al. (2022) [DESCN]:** *DESCN: Deep entire space cross networks for individual treatment effect estimation* (KDD '22) [17, 26].
5. **Miao, Geng, & Tchetgen Tchetgen (2018) / Tchetgen Tchetgen et al. (2024) [Proximal Causal Inference]:** *Identifying causal effects with proxy variables of an unmeasured confounder* (Biometrika) & *An introduction to proximal causal inference* (Statistical Science) [27-29].
6. **Neuberg (2003) / Pearl (2000) [Front-Door Criterion]:** *Causality: models, reasoning, and inference* & *The front-door criterion in potential outcome framework* [24, 25, 30].
7. **Diemert et al. (2017) [Criteo MTA Dataset]:** *Attribution modeling increases efficiency of bidding in display advertising* (KDD AdKDD Workshop) [25, 31].

---

💡 *Would you like to explore how ALM-MTA's front-door causal adjustment or contrastive overlap module could be adapted to evaluate counterfactual removal uplift for your dating platform's N7 retention ranker?*

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

### **Evaluation for Source: *"ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization"***
*(Liu et al., Kuaishou Technology & The University of Auckland, 2026: `arXiv:2605.08881`)* [1]

---

### **(A) Q1 or Q2 or Both or Neither?**

**Q1 only.** [1-5]
* **Q1 (Industry/Production Attribution 2025–2026):** **Yes.** Published in May 2026 (`arXiv:2605.08881`), this paper describes a production causal Multi-Touch Attribution (MTA) system deployed in real-world production at Kuaishou Technology on a recommendation engine serving **400 million Daily Active Users (DAU)** and evaluated over **30 billion training instances** [1, 4, 5].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper attributes user content consumption touchpoints to **content creation / video upload events (\\(Y \in \{0, 1\}\\))** in the "Consumption Drives Production" (CDP) ecosystem, rather than user retention, active days, or return visits [1-4].

---

### **(B) Q2 Class**

**NOT.** [1-4]
* **Justification:** The system computes causal multi-touch attribution credit for content creation / video upload conversion events (\\(Y\\)), not for user retention, active days, or revisitation [1-4].

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **Yes.** It produces a per-touchpoint causal uplift credit score [3, 6]:
  \\[\hat{\Delta}(\tau_j \mid X, T) = g_\theta(X, T) - g_\theta(X, T \setminus \{\tau_j\})\\]
  defined as the counterfactual drop in predicted upload probability when touchpoint \\(\tau_j\\) is deleted from the user's sequential consumption history [3, 6, 7].
* **Target Outcome:** **Binary content creation / video upload event (\\(Y \in \{0, 1\}\\))** within the consumption sequence horizon [3, 4].

---

### **(D) Replacing Last-Touch N7 → Latest Swipes**

* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% credit to the final interaction before conversion, ignoring earlier touchpoints and failing under system- and sequence-level unobserved confounding [2, 8, 9]. ALM-MTA calculates the counterfactual marginal uplift of deleting a specific item from the historical sequence using front-door identification and an adversarially learned mediator (\\(\hat{M}\\)), isolating true causal contribution from unobserved confounders (e.g., system recommendation strategies or latent user intent) [7, 9-11].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  * **Sequence Representation:** \\(T = \langle \text{swipe}_1, \text{swipe}_2, \text{match}_1, \text{conversation}_1, \dots \rangle\\) representing the user's sequential in-app interaction journey [3].
  * **Counterfactual Removal Uplift:** Replaces last-touch with counterfactual deletion uplift [3, 6, 7]:
    \\[\Delta(\text{swipe}_j) = P(\text{Retention} \mid \text{do}(T)) - P(\text{Retention} \mid \text{do}(T \setminus \{\text{swipe}_j\}))\\]
    evaluating how removing a specific swipe or early mutual match reduces the predicted 7-day retention probability [3, 6, 7].
  * **Mediator & Front-Door Adjustment:** Uses an adversarial proxy mediator \\(\hat{M}\\) (e.g., intermediate interaction depth, messaging engagement velocity) to block unobserved user activity/intent confounders (\\(W\\)), ensuring that credit assigned to early candidate swipes reflects true causal incrementality rather than selection bias [9-12].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Front-Door Causal Identification:** Leverages front-door adjustment via a latent mediator \\(M\\) (rendered observable via an adversarially trained proxy \\(Y'\\) invariant to outcome \\(Y\\)) to block unobserved system-level and sequence-level confounders \\(W\\) [7, 9-11].
2. **Inverse Propensity Weighting (IPW):** Reweights observational consumption logs using \\(w(X, T) = 1 / P_{\text{obs}}(T = t \mid X = x)\\) to eliminate backdoor confounding from observed covariates \\(X \to T\\) [6, 13, 14].
3. **Contrastive Overlap Control:** Uses InfoNCE-based contrastive learning between touchpoints \\(T\\) and proxy mediator \\(Y'\\) to restrict front-door marginalization to the top-\\(K\\) high-match subset \\(\tau_{\text{high}}\\), maintaining positivity/overlap in high-cardinality treatment spaces [15, 16].

---

### **(F) Deployment and Production Dataset Evidence**

* **Production Deployment:** Deployed in real-world production at Kuaishou Technology on a recommendation engine serving **400 million Daily Active Users (DAU)** [1, 5].
* **Production Dataset:** Trained on **100 consecutive days of online logs** generating over **30 billion training instances** with a candidate treatment space reaching the **billion level** [1, 4].
* **Quoted Quantitative Results:**
  * **Live Production Online A/B Test Lifts (Kuaishou Platform):**
    * **Daily Active Users (DAU):** **+0.04%** [1, 5, 17].
    * **Daily Active Creators:** **+0.6%** [1, 5, 17].
    * **Unit Exposure Efficiency:** Increased by **670%** (production traffic efficiency **+0.504%**, uploads per user **+0.569%**) [1, 5, 17].
    * **Addressable Creator Scale:** Expanded by **+0.119%**; Producer WAU **+0.566%** [5].
    * **Attributable Upload Coverage:** Expanded by **1.5x** (upload coverage increased from **0.39 to 0.58** under threshold **0.54**) [5, 17].
    * **Touchpoint Granularity:** Average attributed touchpoints per covered upload increased from **2.93 to 7.31** (**2.49x**) [5].
    * **Attribution Accuracy:** Precision increased from **4.32% to 21.88%**, Recall increased from **7.95% to 11.67%** (top-score bucket precision reached **54%**) [5].
  * **Offline Evaluation Benchmark Performance (Table 2):**
    * **Upload AUC:** **0.9070** (vs SOTA causalMTA **0.8167**, deepMTA **0.7598**, DML **0.6498**, DESCN **0.5492**, LR **0.5102**) — **+40% improvement over prior SOTA** [1, 17, 18].
    * **Log Loss:** **0.1384** (vs causalMTA **0.2835**, deepMTA **0.4108**, LR **0.7833**) [18].
    * **gAUC:** **0.8210** (vs causalMTA **0.6752**, deepMTA **0.6364**, DML **0.5031**) [18].
    * **Grouped AUUC (avg AUUC):** **0.8686** (vs causalMTA **0.8493**, DESCN **0.8429**, DML **0.8421**, deepMTA **0.6277**, LR **0.4725**) — maximum gain of **+0.070** across propensity buckets [1, 17, 18].
  * **Computational Complexity:** Per-forward complexity is **1.31B FLOPs** (0.92B FLOPs for the counterfactual attribution backbone and 0.39B FLOPs for adversarial/contrastive branches) [19].

---

💡 *Would you like to explore how ALM-MTA's front-door causal adjustment or contrastive overlap module could be adapted to evaluate counterfactual removal uplift for your dating platform's N7 retention ranker?*

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
**Priority:** see queue.md `G12`
