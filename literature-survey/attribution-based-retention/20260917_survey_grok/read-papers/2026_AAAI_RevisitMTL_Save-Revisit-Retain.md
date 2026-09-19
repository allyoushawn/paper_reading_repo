# Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems [1]

**Source:** https://arxiv.org/pdf/2511.18013.pdf  
**Date analyzed:** 2026-09-18  
**NLM source id:** `6d64098b-cfd7-44cc-9e0d-14a3b30bba04`  
**Queue id:** G5  
**Q2 class:** PARTIAL

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**

* **Title:** *Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems* [1]
* **Authors:** **Weijie Jiang**, **Armando Ordorica**, **Jaewon Yang**, **Olafur Gudmundsson**, **Yucheng Tu**\*, and **Huizhong Duan** (\*Work done at Pinterest) [1, 2]
* **Affiliations:** **Pinterest Inc.** [1]
* **Year:** **2026** (submitted Nov 2025, Copyright © 2026 AAAI) [1, 2]
* **Venue:** *Proceedings of the AAAI Conference on Artificial Intelligence (AAAI '26)* / arXiv pre-print (`arXiv:2511.18013`) [1, 2]

---

### **(2) Core Problem and Key Contribution**

* **Core Problem:** Optimizing long-term user revisitation (returning to view previously saved content) to drive platform retention faces two major challenges:
  1. *Attribution Noise & Confounding:* Unclear causal links between initial candidate exposures/saves and delayed return visits due to confounding factors like changing user intent, platform notifications, or UI layout [1, 3].
  2. *Scalability Bottleneck:* Tracking cross-session revisitations occurring days or weeks later requires maintaining and joining massive activity logs across millions of users and surfaces, creating heavy computational and serving latency overhead [1, 3].
* **Key Contributions:**
  1. **Surrogate Attribution Framework:** Establishes a lightweight surrogate process linking initial item save actions ("repins") to subsequent cross-session revisitation events, isolating true return intent from incidental noise [1, 4, 5].
  2. **Cross-Surface Data Pipeline:** Implements a scalable event-aggregation pipeline that performs cross-surface joins (linking Related Pins save events with Own Profile revisit events over a 0–6 day window) [1, 7, 29–31].
  3. **Multi-Task Joint Modeling:** Integrates a dedicated revisitation prediction head into an existing Multi-Gate Mixture-of-Experts (MMoE) ranking architecture without adding serving cost or latency [1, 6-8].
  4. **Billion-Scale Industrial Deployment:** Deployed on Pinterest's Related Pins surface serving **500M+ users**, achieving a statistically significant **+0.10% increase in active users** in live A/B testing [1, 9, 10].

---

### **(3) Proposed Method or Architecture in Detail**

* **Multi-Task Learning (MTL) Architecture:**
  * **Input Features:** Query Pin features, candidate Pin features, user features, and a Transformer-based user sequence module [7].
  * **Representation & Expert Layers:** Feature cross-summarization \\(\rightarrow\\) **DCNv2** deep feature interaction layer \\(\rightarrow\\) MLP aggregation \\(\rightarrow\\) **MMoE** (Multi-Gate Mixture-of-Experts) shared experts and task gates [7].
  * **Task Prediction Heads:** Predicts probabilities for standard engagement tasks (\\(P(\text{grid-click})\\), \\(P(\text{repin})\\), \\(P(\text{click})\\), \\(P(\text{long-click})\\)) plus the new **revisitation prediction head** \\(P(c_{\text{RP\&RV}} \mid q, \theta)\\) [8, 11].
* **Credit Assignment & Touchpoint Linkage Mechanism:**
  * **Surrogate Linkage:** Connects an initial save action ("repin") on the Related Pins surface to subsequent profile revisitations over a 0–6 day temporal window [5–7, 23].
  * **Revisitation Label Construction (\\(c_{\text{RP\&RV}}\\)):** Combines three binary sub-signals into a unified revisitation target:
    1. *Same-day Revisitation Impression (1dRevImpre):* User saved a Pin and viewed it on their profile on the same day [12].
    2. *Same-day Revisitation Grid-click (1dRevGrid):* User saved a Pin and tapped to zoom into it on their profile on the same day [12].
    3. *7-day Revisitation Grid-click (7dRevGrid):* User saved a Pin and tapped/zoomed into it on their profile within days 0–6 following the save [12].
  * **Ranking Score Integration:** Assigns credit directly to candidate Pins during ranking by adding the predicted revisitation probability weighted by a utility weight \\(u_{\text{RP\&RV}}\\) into the multi-task final ranking score [22, 25–26]:
    \\[\text{score} = \sum_{i \in L} u_i \cdot p(c_i \mid q, \theta) + u_{\text{RP\&RV}} \cdot p(c_{\text{RP\&RV}} \mid q, \theta)\\]

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets & Scale:**
  * **Offline Dataset:** 27 days of training logs (~**6.6 billion samples**), 1 day for calibration, and 3 days for evaluation (~**700 million samples**) from Pinterest's Related Pins surface [13].
  * **Online A/B Experiment:** **24 million users** (12M control, 12M treatment) evaluated continuously over two months (April 29, 2025 – June 26, 2025) [9, 14].
* **Production Deployment:** Deployed live on Pinterest's Related Pins surface (serving ~50% of total platform traffic) to **500+ million monthly active users** [1, 15, 16].
* **Comparison Baselines:**
  * *Production Baseline:* Existing MMoE + DCNv2 multi-task ranking model predicting immediate engagement tasks (\\(P(\text{grid-click})\\), \\(P(\text{repin})\\), \\(P(\text{click})\\), \\(P(\text{long-click})\\)) without revisitation modeling [13, 21–22, 33].
  * *Conceptual Baselines:* Separate causal/triple-task revisitation models (Zhang et al., 2021) and Reinforcement Learning / Generative Flow Networks (Liu et al., 2024 / GFN4Retention) [6, 17, 18].

---

### **(5) Key Quantitative Results with Numbers**

* **Offline Evaluation Benchmark (Table 1):**
  * **Revisitation Task Head:** **+40.15% NDCG@3**, **+43.44% MAP@3**, **+35.40% Recall@3**, **+27.62% Recip Rank@3**, and **+21.62% Pairwise Accuracy** over baseline [19].
  * **Repin Task Head:** **+0.1279% NDCG@3**, **+0.0645% MAP@3**, and **+0.2705% Recall@3** [19].
  * **Overall Ranking Hits@3:** **+0.59% lift on Repin** and **+0.65% lift on Revisitation** [33–34].
* **Live Online Production A/B Testing (Table 2, 24M Users):**
  * **Active Users (Site-wide Retention):** **+0.10% volume** (\\(p < 0.05\\)) and **+0.08% propensity** (\\(p < 0.05\\)) [10, 20].
  * **Revisitation Metrics:**
    * *1dRevImpre:* **+0.65% volume** (\\(p < 0.05\\)), **+0.93% propensity** (\\(p < 0.05\\)) [20].
    * *1dRevGrid:* **+0.95% volume** (\\(p < 0.05\\)), **+1.17% propensity** (\\(p < 0.05\\)) [20].
    * *7dRevGrid:* **+1.18% volume** (\\(p < 0.05\\)), **+1.42% propensity** (\\(p < 0.05\\)) [20].
  * **Core Engagement:** **+0.94% Repin volume** (\\(p < 0.1\\)), **+0.41% Long Sessions (\\(\ge 5\\) min)** (\\(p < 0.01\\)), **+0.35% Web/API Requests** (\\(p < 0.01\\)), **+0.53% Time Spent on Related Pins**, **+0.68% Time Spent on Own Profile**, and **+0.39% Total App Time Spent** [36–38].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **User Activity Imbalance & Label Sparsity Bottleneck:** Highly active users repin disproportionately more than less active users, resulting in sparse revisitation label coverage for less active user cohorts [21].
2. **Intent vs. Density Trade-Off:** Impression-based revisits offer high label volume but contain incidental scroll noise, whereas grid-click revisits signal deliberate return intent but decay rapidly (grid-click revisits drop from 4.7% on day 0 to 2.2% on day 1, and 0.3% by day 9) [22, 23].
3. **Relevance vs. Diversity Tension:** Authors note that earlier attempts to optimize recommendation diversity hurt click and save engagement metrics by >1% [24].
4. **Offline Recip Rank@3 Degradation:** Offline Recip Rank@3 on the repin head exhibited a slight negative change (**-0.02666%**), though overall Hits@3 and online metrics were strictly positive [33–34].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Zhang et al. (2021) [Triple-Task Causal Retention]:** *User Retention: A Causal Approach with Triple Task Modeling* (IJCAI '21) [6, 25].
2. **Wang et al. (2022) [Surrogate Rewards for Experience]:** *Surrogate for long-term user experience in recommender systems* (KDD '22) [4, 5, 26].
3. **Liu et al. (2024) [GFN4Retention]:** *Modeling User Retention through Generative Flow Networks* (KDD '24) [17, 18, 26].
4. **Liu et al. (2017) [Pinterest Related Pins Architecture]:** *Related pins at pinterest: The evolution of a real-world recommender system* (WWW '17) [9, 14-16, 26].
5. **Ma et al. (2018) [MMoE Architecture]:** *Modeling task relationships in multi-task learning with multi-gate mixture-of-experts* (KDD '18) [7, 26].
6. **Wang et al. (2021) [DCNv2 Layer]:** *DCN v2: Improved deep & cross network and practical lessons for web-scale learning to rank systems* (WWW '21) [7, 26].
7. **Zhao et al. (2023) [DT4Rec]:** *User retention-oriented recommendation with decision transformer* (WWW '23) [18, 25].

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

### **Source Evaluation: Save, Revisit, Retain (Pinterest Framework)**
*(Jiang et al., Pinterest Inc., AAAI 2026 / arXiv: `2511.18013`)* [1]

---

### **(A) Q1 or Q2 or Both or Neither?**
* **Answer:** **Both** (Q1 and Q2) [1, 8–9, 13, 35].
* **Explanation:** 
  * **Q1 (Industry/Production Attribution 2025–2026):** **Yes.** Deployed in production on Pinterest's Related Pins surface serving **500+ million users**, with a large-scale online A/B experiment conducted from **April 29, 2025 to June 26, 2025** [1-3].
  * **Q2 (Attributing Retention / Engagement / Days-Active to In-App Interactions):** **Yes.** It establishes a surrogate attribution linkage that connects item-level save actions ("repins") on candidate items to multi-day return visits ("revisitations" on personal profiles over a 0–6 day window) as a direct proxy for 28-day active user retention [1, 5, 17, 23–25].

---

### **(B) Q2 Class**
* **Classification:** **PARTIAL** [1, 5, 10, 13, 21–25].
* **Justification:** The paper creates an item-level surrogate linkage and multi-task prediction head (\\(P(\text{revisit} \mid q, \theta)\\)) connecting content exposures/saves to 0–6 day profile revisitations and active days [5, 23–25]. It explicitly acknowledges user activity and intent confounders [1, 4], but it does **not** estimate an identified causal Multi-Touch Attribution (MTA) sequence decomposition across multiple sequential touches [5, 6].

---

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Item/Candidate-level Score Integration** (not sequence-level fractional attribution percentages) [21–22, 25–26]. It predicts the probability \\(P(c_{\text{RP\&RV}} \mid q, \theta)\\) that a candidate item will be saved and revisited, multiplying this probability by a business utility weight (\\(u_{\text{RP\&RV}}\\)) to add directly into the candidate's final ranking score [22, 25–26]:
  \\[\text{score} = \sum_{i \in L} u_i \cdot P(c_i \mid q, \theta) + u_{\text{RP\&RV}} \cdot P(c_{\text{RP\&RV}} \mid q, \theta)\\]
* **Target Outcome:** **Revisitation surrogate label (\\(c_{\text{RP\&RV}}\\))**, combining three cross-surface return events over a 0–6 day window [23–25]:
  1. *Same-day Revisitation Impression (`1dRevImpre`)* [7].
  2. *Same-day Revisitation Grid-click (`1dRevGrid`)* [7].
  3. *7-day Revisitation Grid-click (`7dRevGrid`)* (zooming into saved content 0–6 days post-save) [7].
  * *Downstream Impact:* These surrogate events strongly correlate with **28-day active days** and site-wide user retention [17–18, 38].

---

### **(D) Replacing Last-Touch N7 → Latest Swipes**
* **How it Improves on Last-Touch:** Last-touch assigns 100% credit to the final swipe before Day 7, ignoring earlier high-intent actions (matches, messaging) and failing to predict whether a current interaction will generate future return behavior [4, 5]. Pinterest's approach replaces last-touch heuristics by predicting the **probability of delayed return engagement** at candidate exposure time and incorporating that long-term retention value directly into the ranking score [7, 25–26].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  * **Initial High-Intent Action (Save/Repin Analogue):** A swipe resulting in a mutual match or saved profile.
  * **Delayed Return Event (Revisitation Analogue):** The user opening the match profile or initiating/continuing a 4-way conversation within a **0–6 day window** post-match (`1dRevImpre`, `1dRevGrid`, `7dRevGrid`) [23–24].
  * **Ranker Scoring Integration:** During ranking, candidate profiles are scored not just on immediate swipe probability \\(P(\text{like})\\), but on \\(P(\text{like}) + u_{\text{retention}} \cdot P(\text{match \& 0–6d conversation})\\), ensuring the ranker prioritizes candidate profiles that spark lasting 7-day retention [22, 25–26].

---

### **(E) Selection-Bias & Confounding Handling**
* **Confounders Acknowledged:** The authors explicitly identify attribution noise caused by shifting user intent across sessions, platform notifications, content quality, and hyper-active user bias (where engaged users save and revisit disproportionately more) [1, 4, 8, 9].
* **Handling Mechanisms:**
  1. **Surrogate Causal Filtering:** Restricts attribution to exact `(User ID, Item ID)` pairs joined across a strict 0–6 day window (`timesave < timerevisit < timesave + 7 days`), filtering out unrelated cross-session browsing noise [5–6, 31].
  2. **Intent Precision Filtering:** Focuses multi-day labels on intentional grid-clicks (`7dRevGrid`) rather than passive impressions (`1dRevImpre`), as grid-clicks show significantly higher correlation with 28-day active days [10, 11].
  3. **Unique User Feature Normalization:** Constructs historical Pin performance features (`Pin perf`) tracking both total action counts and **unique user counts** over 7, 30, and 90 days to prevent single enthusiastic users from skewing retention signals [27–28].
  * *Note:* The paper does not use formal propensity score weighting (IPW) or counterfactual causal bounds, citing user activity imbalance as an ongoing limitation for future work [9].

---

### **(F) Deployment & Production Quantitative Results**

* **Deployment Status:** Fully deployed in production on Pinterest's Related Pins surface serving **500+ million monthly active users** across ~**50% of overall platform traffic** [1, 2, 12].
* **Dataset & Scale:**
  * *Offline Training Set:* 27 days (~**6.6 billion samples**) for training, 1 day for calibration, and 3 days (~**700 million samples**) for evaluation [13].
  * *Online A/B Experiment:* **24 million users** (12M control, 12M treatment) evaluated continuously over 2 months (April 29, 2025 – June 26, 2025) [3].
* **Quoted Quantitative Results:**
  * **Online A/B Testing Lifts (Table 2):**
    * **Active Users (Site-wide Retention):** **+0.10% volume** (\\(p < 0.05\\)) and **+0.08% propensity / unique users** (\\(p < 0.05\\)) [1, 14, 15].
    * **Revisitation Metrics:** `1dRevImpre` **+0.65% volume** (\\(p < 0.05\\)), **+0.93% propensity** (\\(p < 0.05\\)); `1dRevGrid` **+0.95% volume** (\\(p < 0.05\\)), **+1.17% propensity** (\\(p < 0.05\\)); `7dRevGrid` **+1.18% volume** (\\(p < 0.05\\)), **+1.42% propensity** (\\(p < 0.05\\)) [14].
    * **Platform Engagement:** **+0.94% Repin volume** (\\(p < 0.1\\)), **+0.64% Repin propensity** (\\(p < 0.01\\)), **+0.41% Long Sessions (\\(\ge 5\\) min)** (\\(p < 0.01\\)), **+0.35% Web/API Requests** (\\(p < 0.01\\)), **+0.53% Time Spent on Related Pins**, **+0.68% Time Spent on Own Profile**, and **+0.39% Total App Time Spent** [36–38].
  * **Offline Model Performance Lifts (Table 1):**
    * *Revisitation Head:* **+40.15% NDCG@3**, **+43.44% MAP@3**, **+27.62% Recip Rank@3**, **+35.40% Recall@3**, **+21.62% Pairwise Accuracy**, and **+0.65% Hits@3** over production baseline [33–34].
    * *Repin Head:* **+0.1279% NDCG@3**, **+0.0645% MAP@3**, **+0.2705% Recall@3**, and **+0.59% Hits@3** [33–34].
    * *Optimal Task Utility Weight:* \\(u_{\text{RP\&RV}} = 1.27 \times u_{\text{Repin}}\\) [13].
  * **Revisitation Behavior Decay Rates:**
    * *Daily User Revisitation Decay:* Day 0 impression rate **14.6%** \\(\rightarrow\\) Day 1 **19.5%** \\(\rightarrow\\) Day 9 **8.7%**; Day 0 grid-click rate **6.6%** \\(\rightarrow\\) Day 1 **7.7%** \\(\rightarrow\\) Day 9 **1.6%** [16].
    * *Volume Decay:* Grid-click revisitation volume starts at **4.7%** on day 0, drops by half to **2.2%** on day 1, **1.1%** on day 2, **0.5%** by day 5, and **0.3%** by day 9 [17].
    * *Label Volume relative to Daily Repins:* `1dRevImpre` = **25.8%**, `1dRevGrid` = **4.7%**, `7dRevGrid` = **9.0%** [7].

---

💡 *Would you like to explore how Pinterest's cross-surface surrogate join pipeline or MMoE revisitation utility weights (\\(u_{\text{retention}}\\)) could be implemented for your dating platform's candidate profile ranker?*

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
**Priority:** see queue.md `G5`
