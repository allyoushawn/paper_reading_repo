# Interpretable User Retention Modeling in Recommendation [14]

**Source:** https://dl.acm.org/doi/pdf/10.1145/3604915.3608818  
**Date analyzed:** 2026-09-18  
**NLM source id:** `47cf0db1-92bc-49da-b44f-af65cea80083`  
**Queue id:** G13  
**Q2 class:** PARTIAL

---

## 1. Summary

### **Part 1: Dating App Retention Project Evaluation**

#### **(A) Alignment: Q1 or Q2 or Both or Neither?**
* **Category:** **Q2 Only** [3, 4, 11–12].
* **Explanation:**
  * *Q1 (Industry/Production Attribution 2025–2026):* **No.** Published in September 2023 (RecSys '23), which falls outside the 2025–2026 window [1, 2].
  * *Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):* **Yes.** The paper generates item/action-level retention scores (\\(s_{ui}\\)) and instance-level attention weights over individual user interactions to explain and predict 3-day user retention [7, 11–12].

---

#### **(B) Q2 Class**
* **Classification:** **PARTIAL** [7, 11–12, 14–17].
* **Justification:** IURO generates item/action-level retention scores (\\(s_{ui}\\)) via a UI Scorer and aggregates them using instance-level attention in Multi-Instance Learning (CMIL/RMIL) to predict 3-day retention [11–14]. The paper explicitly acknowledges and addresses offline-online gaps, unpredictable external factors (e.g., user mood or workload), and lack of explicit per-item retention signals [6, 14–15]. However, it does not formulate an identified causal Multi-Touch Attribution (MTA) model under formal counterfactual graph identification [7, 14–17].

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Yes.** Generates user-item retention scores \\(s_{ui} = \text{FFN}_3(\text{concat}(u_p, u_l, v_i))\\) and instance-level attention weights (\\(\text{softmax}(\text{concat}(u_p, u_l) v_i / \sqrt{d})\\)) for individual user interactions [12–13].
* **Target Outcome:** **Next-3-Day User Retention (\\(y_u\\))**, weighted by future 3-day engagement volume (\\(W_u = a \log(1 + n_c^u) + b \log(1 + n_i^u)\\)) [3]. In online serving, candidate items are scored via \\(r_{ui} = \alpha \cdot \text{CTR}_{ui} + (1-\alpha) s_{ui}\\) [4].

---

#### **(D) Improving on Last-Touch N7 → Latest Swipes**
* **How it Improves Last-Touch:** Last-touch assigns 100% credit to the final swipe before Day 7, ignoring earlier high-value interactions. IURO replaces rule-based last-touch heuristics by computing explicit user-item retention scores (\\(s_{ui}\\)) across all past interactions using Multi-Instance Learning [7, 11–12]. It applies contrastive learning to sharpen "aha items" (high-impact interactions) and uses future behavior alignment (RMIL) as pseudo-causal keys to identify which specific past interactions truly drove return visits [7, 14–17].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Interaction Sequence:* User interaction logs are represented as a sequence of past candidate profile swipes, mutual matches, and 4-way messaging conversations [11–13].
  2. *UI Scorer (\\(s_{ui}\\)):* Evaluates each swipe, match, or messaging interaction based on user demographics (\\(u_p\\)), historical behavior (\\(u_l\\)), and candidate profile features (\\(v_i\\)) [5].
  3. *Aha Item Identification:* CMIL and RMIL identify "aha interactions"—such as a high-affinity mutual match or a deep messaging conversation—that served as the primary drivers of 7-day retention [7, 14–17].
  4. *Online Candidate Ranking:* Candidate profile recommendations are scored via \\(r_{ui} = \alpha \cdot \text{CTR}_{ui} + (1-\alpha) s_{ui}\\), prioritizing profiles that align with past retention-inducing "aha" interactions [4, 6].

---

#### **(E) Selection-Bias & Confounding Handling**
1. **Future Engagement Supervised Weighting (\\(W_u\\)):** Multiplies retention targets by next-3-days cumulative activity (\\(W_u = a \log(1 + n_c^u) + b \log(1 + n_i^u)\\)) to reduce background noise from passive or accidental app opens [3].
2. **Contrastive Multi-Instance Learning (CMIL):** Uses contrastive loss \\(L_{CL} = \max(0, |y_{MIL} - y_{CMIL}^{pos}| - |y_{MIL} - y_{CMIL}^{neg}| + m)\\) to broaden the attention gap between genuine "aha items" and passive background interactions [14–15].
3. **Rationale Alignment via JS Divergence (RMIL):** Uses next-few-day clicks as external pseudo-causal keys to align the attention distribution via Jensen-Shannon divergence (\\(L_{JS}\\)), raising the overlap/consistency of selected "aha items" across initializations from **~35% to ~70%** [7, 8].

---

#### **(F) Deployment and Dataset Evidence**
* **Production Deployment:** Deployed live on a major industrial article recommendation feed (**Tencent WeChat**) serving over **3 million users** in an online A/B test [4].
* **Offline Datasets:** **ZhihuRec 1M** (7,963 users, 81,214 items, 1,271,751 behaviors) and an **Industrial Dataset** (~1 million users, 500,000 items, 97 million behaviors) [9].
* **Quoted Quantitative Results:**
  * **Live Online A/B Test Lifts (Table 3):** **+0.76% next-day retention** and **+0.65% next-three-day retention** [4].
  * **Hit Item Quality & Engagement:**
    * *Average CTR:* **0.129** for hit items vs. **0.082** (Exp Group) and **0.083** (Control Group) [10].
    * *Average Duration:* **98.73s** per item for hit items vs. **18.86s** (Exp Group) and **18.55s** (Control Group) [10].
    * *Filter Bubble Escape:* **34.08% of users** started following novel, surprising categories recommended by IURO in future clicks [10].
  * **Offline Retention AUC Performance (Table 2):**
    * *ZhihuRec 1M:* Base MLP (**0.7180**), IURO(AVG) (**0.5838**), IURO(MIL) (**0.8269**), IURO(MIL+MSS) (**0.8312**), IURO(CMIL+MSS) (**0.8437**), IURO(RCMIL+MSS) (**0.8445**) [11].
    * *Industrial Dataset:* Base MLP (**0.6827**), IURO(AVG) (**0.6732**), IURO(MIL) (**0.7209**), IURO(MIL+MSS) (**0.7255**), IURO(CMIL+MSS) (**0.7291**), IURO(RCMIL+MSS) (**0.7301**) [11].
  * **Explicit User Feedback Analysis (Table 1 & Section 4.1):**
    * **69% of survey participants** claim they return if items are relaxing and stress-relieving [12].
    * *Relative Retention Rates by Negative Feedback Reason:* "Not interested in items" (**35.38% next-day / 36.45% next-3-day** — lowest retention), "Low-quality content" (**90.29% / 91.78%**), "Advertising promotion" (**91.89% / 93.06%**), "Poor diversity" (**97.33% / 98.36%**), "Exaggerating titles" (**98.98% / 99.05%**), "Don't like author/content" (**102.29% / 102.03%**), "Repeated recommendation" (**113.51% / 108.07%**) [13].

---

### **Part 2: Detailed Technical Breakdown of the Source**

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Interpretable User Retention Modeling in Recommendation* [14]
* **Authors:** **Rui Ding**¹, **Ruobing Xie**\*², **Xiaobo Hao**², **Xiaochun Yang**\*¹, **Kaikai Ge**², **Xu Zhang**², **Jie Zhou**², and **Leyu Lin**² (*\*Corresponding Authors*) [14]
* **Author Affiliations:**
  1. **Northeastern University**, Shenyang, China (`ruiding.neu@outlook.com`, `yangxc@mail.neu.edu.cn`) [14]
  2. **WeChat, Tencent**, Beijing, China (`{xrbsnowing, rolyhao, kavinge, xuonezhang, withtomzhou, goshawklin}@tencent.com`) [14, 15]
* **Year & Venue:** Published in **2023** at the *Seventeenth ACM Conference on Recommender Systems (RecSys ’23), September 18–22, 2023, Singapore* [1, 2].

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Recommender systems primarily optimize for immediate accuracy metrics (e.g., CTR), which fails to capture long-term user satisfaction and retention [2, 15]. Existing retention modeling efforts focus on predictive accuracy via sequential decision-making/RL, treating retention as a black box without identifying *why* users return or *which specific behaviors* drive return visits [2, 16-18].
* **Key Contributions:**
  1. **IURO Framework:** Introduces an interpretable user retention-oriented optimization framework designed to discover and utilize explicit retention factors [6, 19].
  2. **Contrastive Multi-Instance Learning (CMIL):** Combines a UI Scorer module with instance-level attention and contrastive learning to isolate rare, high-impact "aha items" [7, 12–15].
  3. **Rationale Multi-Instance Learning (RMIL) & Distribution Alignment:** Uses future clicked items as pseudo-causal keys to supervise CMIL via Jensen-Shannon (JS) divergence loss, improving selected "aha item" consistency across initializations from **~35% to ~70%** [7, 15–17].
  4. **Explicit User Feedback Analysis:** Quantifies interpretable retention factors through user surveys and explicit negative feedback analyses across 1M daily logs [12, 19, 20].
  5. **Billion-Scale Industrial Deployment:** Validates online retention gains (+0.76% next-day retention) on Tencent WeChat article feed serving millions of users [4, 10, 21].

---

#### **(3) Proposed Method or Architecture in Detail**
* **UI Scorer Module:** A 3-layer feedforward network (\\(s_{ui} = \text{FFN}_3(\text{concat}(u_p, u_l, v_i))\\)) generating user-item retention scores, where \\(u_p\\) represents static user attributes, \\(u_l\\) represents long-term behaviors, and \\(v_i\\) represents short-term behavior (offline) or candidate item features (online) [5].
* **Multi-Instance Learning (MIL) Aggregation:**
  \\[y_{MIL}^u = \sum_{i \in sequence} \text{softmax}\left(\frac{\text{concat}(u_p, u_l) v_i}{\sqrt{d}}\right) s_{ui}\\]
  Supervised by \\(L_{MIL} = \sum_u W_u \cdot \text{MSE}(y_u, y_{MIL}^u)\\), where \\(W_u = a \log(1 + n_c^u) + b \log(1 + n_i^u)\\) incorporates future 3-day engagement volume [3, 22].
* **Contrastive Multi-Instance Learning (CMIL):** Applies contrastive loss \\(L_{CL} = \sum_u \max(0, |y_{MIL}^u - y_{CMIL,pos}^u| - |y_{MIL}^u - y_{CMIL,neg}^u| + m)\\) by masking low- and high-attention items to sharpen "aha item" selection [7, 22].
* **Rationale Multi-Instance Learning (RMIL) & Alignment:** Uses future clicked items (next few days) as external pseudo-causal keys to find historical rational behaviors (top 5 by dot product with mean future click vector) [7, 8]. Aligns CMIL and RMIL attention distributions via JS-divergence loss \\(L_{JS} = \mathbb{E}_u [\text{JS}(y_{MIL}^u \parallel y_{RMIL}^u)]\\) [8]. Total loss: \\(L = \alpha_1 L_{MIL} + \alpha_2 L_{CL} + \alpha_3 L_{RMIL} + \alpha_4 L_{JS}\\) [8].
* **Online Serving Integration:** Candidate items are reranked using \\(r_{ui} = \alpha \cdot \text{CTR}_{ui} + (1-\alpha) s_{ui}\\), bridging offline instance-level attention training with online single-item scoring [4, 6].

---

#### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets:**
  * **ZhihuRec 1M:** 7,963 users, 81,214 items, 1,271,751 behaviors over 10 days (first 7 days train, last 3 days test) [9].
  * **Industrial Dataset (Article Feed):** ~1 million users, 500,000 items, 97 million behaviors over 18 days [9].
* **Production Deployment:** Live online A/B testing on Tencent WeChat article recommendation feed serving over 3 million users [4].
* **Comparison Baselines:**
  * **Base MLP:** 3-layer MLP on static features + all behaviors (infeasible online without UI scorer) [23].
  * **IURO(AVG):** Assigns uniform impact weights across all historical items [23].
  * **IURO(MIL):** Incorporates instance-level attention without contrastive or rationale losses [23].
  * **IURO(MIL+MSS):** MIL + future cumulative feature supervised signals (\\(W_u\\)) [23].
  * **IURO(CMIL+MSS):** CMIL + \\(W_u\\) [23].
  * **IURO(RCMIL+MSS):** Full IURO framework with rationale alignment [23].

---

#### **(5) Key Quantitative Results with Numbers**
* **Offline User Retention Prediction AUC (Table 2):**
  * *ZhihuRec 1M:* Base MLP (**0.7180**), IURO(AVG) (**0.5838**), IURO(MIL) (**0.8269**), IURO(MIL+MSS) (**0.8312**), IURO(CMIL+MSS) (**0.8437**), IURO(RCMIL+MSS) (**0.8445**) [11].
  * *Industrial Dataset:* Base MLP (**0.6827**), IURO(AVG) (**0.6732**), IURO(MIL) (**0.7209**), IURO(MIL+MSS) (**0.7255**), IURO(CMIL+MSS) (**0.7291**), IURO(RCMIL+MSS) (**0.7301**) [11].
* **Live Online A/B Testing Results (>3M Users, Table 3):**
  * **Next-day retention:** **+0.76%** relative gain [4].
  * **Next-three-day retention:** **+0.65%** relative gain [4].
* **Hit Item Metrics & User Interest Expansion:**
  * *Hit Item CTR:* **0.129** (vs Exp Group **0.082** and Control Group **0.083**) [10].
  * *Hit Item Duration:* **98.73s** per item (vs Exp Group **18.86s** and Control Group **18.55s**) [10].
  * *Filter Bubble Escape:* **34.08% of hit users** started following novel, surprising categories recommended by IURO in future clicks [10].
* **Robustness across Initializations:** "Aha item" selection overlap increased from **~35%** (CMIL alone) to **~70%** (IURO with RMIL rationale supervision) [7, 8].

---

#### **(6) Limitations, Failure Modes, or Negative Results**
1. **Severe Degradation of Uniform Attribution:** `IURO(AVG)` degraded performance significantly on ZhihuRec (AUC dropped from **0.7180 down to 0.5838**), proving that uniform attribution over historical items actively harms retention modeling [11].
2. **Initialization Instability in Naive CMIL:** Without RMIL rationale supervision, CMIL selected "aha items" with only **~35% overlap** across different random parameter initializations due to parameter randomness [7].
3. **Requirement for Post-Session Behavioral Logging:** Requires future session logging (\\(W_u\\) and future clicks in RMIL) during offline training to construct supervised target weights and rationale keys [3, 7, 8].
4. **Heuristic Online Score Blending:** Online reranking relies on a linear combination parameter \\(\alpha\\) (\\(r_{ui} = \alpha \cdot \text{CTR}_{ui} + (1-\alpha) s_{ui}\\)) which must be manually tuned by online systems [4].

---

#### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Cai et al. (2023) [Ref 1]:** *Reinforcing User Retention in a Billion Scale Short Video Recommender System* (WWW '23) [24].
2. **Zhao et al. (2023) [Ref 36]:** *User Retention-oriented Recommendation with Decision Transformer* (WWW '23) [25].
3. **Wang et al. (2022) [Ref 25]:** *Surrogate for Long-Term User Experience in Recommender Systems* (SIGKDD '22) [26].
4. **Kapoor et al. (2014, 2015) [Refs 18, 19]:** *A hazard based approach to user return time prediction* (SIGKDD '14) & *Just in Time Recommendations: Modeling the Dynamics of Boredom in Activity Streams* (WSDM '15) [27, 28].
5. **Chandar et al. (2022) [Ref 4]:** *Using Survival Models to Estimate User Engagement in Online Experiments* (WWW '22) [29].
6. **Chen et al. (2018) / Yu et al. (2019, 2021) [Refs 5, 30, 31]:** *Learning to Explain: An Information-Theoretic Perspective on Model Interpretation* (ICML '18) & *Rethinking Cooperative Rationalization* (EMNLP '19 / NeurIPS '21) [29-31].
7. **Vaswani et al. (2017) [Ref 23]:** *Attention is All you Need* (NeurIPS '17) [32].

---

💡 *Would you like to explore how IURO's Contrastive Multi-Instance Learning (CMIL) or UI Scorer module (\\(s_{ui}\\)) could be adapted to score past candidate swipes, mutual matches, and conversations for your dating platform's N7 retention ranker?*

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

### **Part 1: Detailed Technical Breakdown of the Source**

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Interpretable User Retention Modeling in Recommendation* [1]
* **Authors:** **Rui Ding**¹, **Ruobing Xie**\*², **Xiaobo Hao**², **Xiaochun Yang**\*¹, **Kaikai Ge**², **Xu Zhang**², **Jie Zhou**², and **Leyu Lin**² (*\*Corresponding Authors*) [1, 2]
* **Author Affiliations:**
  1. **Northeastern University**, Shenyang, China (`ruiding.neu@outlook.com`, `yangxc@mail.neu.edu.cn`) [1]
  2. **WeChat, Tencent**, Beijing, China (`{xrbsnowing, rolyhao, kavinge, xuonezhang, withtomzhou, goshawklin}@tencent.com`) [1, 2]
* **Year & Venue:** Published in **2023** at the *Seventeenth ACM Conference on Recommender Systems (RecSys ’23), September 18–22, 2023, Singapore* [3, 4].

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Recommender systems primarily optimize for immediate accuracy and engagement metrics (e.g., Click-Through Rate / CTR), which fails to reflect long-term user satisfaction and retention [2, 4]. Existing retention modeling efforts (e.g., Reinforcement Learning, Decision Transformers, survival analysis) treat retention as a black box focused purely on predictive accuracy, failing to discover *why* users return or *which specific behaviors* affect retention ("interpretability") [4-7]. Major challenges include:
  1. *Offline-Online Gap:* Offline training predicts user-level return, whereas online serving requires item-level scoring [8].
  2. *Complex Causality & External Randomness:* Retention is affected by unobservable external factors (e.g., user mood or workload) [8].
  3. *Extreme Label Sparsity:* Users generate hundreds of clicks per day but only one retention label (return or not) [8].
* **Key Contributions:**
  1. **IURO Framework:** Introduces an interpretable user retention-oriented optimization framework designed to discover and utilize explicit retention factors [2, 9, 10].
  2. **Contrastive Multi-Instance Learning (CMIL):** Combines a UI Scorer module with instance-level attention and contrastive learning to isolate rare, high-impact "aha items" [7, 11–15].
  3. **Rationale Multi-Instance Learning (RMIL) & Distribution Alignment:** Uses future clicked items as pseudo-causal keys to supervise CMIL via Jensen-Shannon (JS) divergence loss, improving selected "aha item" consistency across initializations from **~35% to ~70%** [9, 11, 12].
  4. **Explicit User Feedback Analysis:** Quantifies interpretable retention factors through user surveys and explicit negative feedback analyses across 1M daily logs [2, 13-15].
  5. **Billion-Scale Industrial Deployment:** Validates online retention gains (**+0.76% next-day retention**) on Tencent WeChat article feed serving millions of users [2, 13, 16, 17].

---

#### **(3) Proposed Method or Architecture in Detail**
* **UI Scorer Module:** A 3-layer feedforward neural network generating user-item retention scores [18]:
  \\[s_{ui} = \text{FFN}_3(\text{concat}(u_p, u_l, v_i))\\]
  where \\(u_p\\) represents static user attributes, \\(u_l\\) represents long-term behaviors, and \\(v_i\\) represents short-term behavior features (offline) or candidate item features (online) [18].
* **Multi-Instance Learning (MIL) Aggregation:**
  \\[y_{MIL}^u = \sum_{i \in sequence} \text{softmax}\left(\frac{\text{concat}(u_p, u_l) v_i}{\sqrt{d}}\right) s_{ui}\\]
  Supervised by \\(L_{MIL} = \sum_u W_u \cdot \text{MSE}(y_u, y_{MIL}^u)\\), where \\(W_u = a \log(1 + n_c^u) + b \log(1 + n_i^u)\\) incorporates future 3-day engagement volume [19, 20].
* **Contrastive Multi-Instance Learning (CMIL):** Applies contrastive loss [11]:
  \\[L_{CL} = \sum_{u \in U} \max\left(0, |y_{MIL}^u - y_{CMIL,pos}^u| - |y_{MIL}^u - y_{CMIL,neg}^u| + m\right)\\]
  by masking low- and high-attention items to sharpen "aha item" selection [11, 20].
* **Rationale Multi-Instance Learning (RMIL) & Alignment:** Uses future clicked items (next few days) as external pseudo-causal keys to find historical rational behaviors (top 5 by dot product with mean future click vector) [12]. Aligns CMIL and RMIL attention distributions via JS-divergence loss \\(L_{JS} = \mathbb{E}_u [\text{JS}(y_{MIL}^u \parallel y_{RMIL}^u)]\\) [12]. Total loss: \\(L = \alpha_1 L_{MIL} + \alpha_2 L_{CL} + \alpha_3 L_{RMIL} + \alpha_4 L_{JS}\\) [12].
* **Online Serving Integration:** Candidate items are reranked using \\(r_{ui} = \alpha \cdot \text{CTR}_{ui} + (1-\alpha) s_{ui}\\), bridging offline instance-level attention training with online single-item scoring [10, 16].
* **Credit Assignment Mechanics:** Produces item/action-level retention scores (\\(s_{ui}\\)) and instance-level attention weights over past short-term behaviors to identify "aha items" that drive return visits [9, 10, 18].

---

#### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets:**
  * **ZhihuRec 1M:** 7,963 users, 81,214 items, 1,271,751 behaviors across 10 days (first 7 days train, last 3 days test) [21].
  * **Industrial Dataset (Article Feed):** ~1 million users, 500,000 items, 97 million behaviors over 18 days [21].
* **Production Deployment:** Live online A/B testing on Tencent WeChat article recommendation feed serving over **3 million users** [2, 16].
* **Comparison Baselines:**
  * **Base MLP:** 3-layer MLP on static features + all behaviors (infeasible online without UI scorer) [22].
  * **IURO(AVG):** Assigns uniform impact weights across all historical items [22].
  * **IURO(MIL):** Incorporates instance-level attention without contrastive or rationale losses [22].
  * **IURO(MIL+MSS):** MIL + future cumulative feature supervised signals (\\(W_u\\)) [22].
  * **IURO(CMIL+MSS):** CMIL + \\(W_u\\) [22].
  * **IURO(RCMIL+MSS):** Full IURO framework with rationale alignment [22].

---

#### **(5) Key Quantitative Results with Numbers**
* **Offline User Retention Prediction AUC (Table 2):**
  * *ZhihuRec 1M:* Base MLP (**0.7180**), IURO(AVG) (**0.5838**), IURO(MIL) (**0.8269**), IURO(MIL+MSS) (**0.8312**), IURO(CMIL+MSS) (**0.8437**), IURO(RCMIL+MSS) (**0.8445**) [23].
  * *Industrial Dataset:* Base MLP (**0.6827**), IURO(AVG) (**0.6732**), IURO(MIL) (**0.7209**), IURO(MIL+MSS) (**0.7255**), IURO(CMIL+MSS) (**0.7291**), IURO(RCMIL+MSS) (**0.7301**) [23].
* **Live Online A/B Testing Results (>3M Users, Table 3):**
  * **Next-day retention:** **+0.76%** relative gain [16, 24].
  * **Next-three-day retention:** **+0.65%** relative gain [16, 24].
* **Hit Item Metrics & User Interest Expansion:**
  * *Hit Item CTR:* **0.129** (vs Exp Group **0.082** and Control Group **0.083**) [17].
  * *Hit Item Duration:* **98.73s** per item (vs Exp Group **18.86s** and Control Group **18.55s**) [17].
  * *Filter Bubble Escape:* **34.08% of hit users** started following novel, surprising categories recommended by IURO in future clicks [17].
* **Explicit Negative Feedback Retention Rates (Table 1):**
  * *"Not interested in items":* **35.38% next-day / 36.45% next-3-day** retention (lowest among all reasons) [15, 25].
  * *"Low-quality content":* **90.29% / 91.78%** [25].
  * *"Advertising promotion":* **91.89% / 93.06%** [25].
  * *"Poor diversity":* **97.33% / 98.36%** [25].
  * *"Exaggerating titles":* **98.98% / 99.05%** [25].
  * *"Don't like author/content":* **102.29% / 102.03%** [25].
  * *"Repeated recommendation":* **113.51% / 108.07%** [25].
* **User Survey Findings:** **69% of survey participants** claim they return if recommended items are relaxing and stress-relieving [14].

---

#### **(6) Limitations, Failure Modes, or Negative Results**
1. **Severe Degradation of Uniform Attribution:** `IURO(AVG)` degraded performance significantly on ZhihuRec (AUC dropped from **0.7180 down to 0.5838**), proving that uniform attribution over historical items actively harms retention modeling [22, 23].
2. **Initialization Instability in Naive CMIL:** Without RMIL rationale supervision, CMIL selected "aha items" with only **~35% overlap** across different random parameter initializations due to parameter randomness [11].
3. **Requirement for Post-Session Behavioral Logging:** Requires future session logging (\\(W_u\\) and future clicks in RMIL) during offline training to construct supervised target weights and rationale keys [12, 19].
4. **Heuristic Online Score Blending:** Online reranking relies on a linear combination parameter \\(\alpha\\) (\\(r_{ui} = \alpha \cdot \text{CTR}_{ui} + (1-\alpha) s_{ui}\\)) which must be manually tuned by online systems [16].

---

#### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Cai et al. (2023) [Ref 1]:** *Reinforcing User Retention in a Billion Scale Short Video Recommender System* (WWW '23) [26].
2. **Zhao et al. (2023) [Ref 36]:** *User Retention-oriented Recommendation with Decision Transformer* (WWW '23) [27].
3. **Wang et al. (2022) [Ref 25]:** *Surrogate for Long-Term User Experience in Recommender Systems* (SIGKDD '22) [28].
4. **Kapoor et al. (2014, 2015) [Refs 18, 19]:** *A hazard based approach to user return time prediction* (SIGKDD '14) & *Just in Time Recommendations: Modeling the Dynamics of Boredom in Activity Streams* (WSDM '15) [29, 30].
5. **Chandar et al. (2022) [Ref 4]:** *Using Survival Models to Estimate User Engagement in Online Experiments* (WWW '22) [31].
6. **Chen et al. (2018) / Yu et al. (2019, 2021) [Refs 5, 30, 31]:** *Learning to Explain: An Information-Theoretic Perspective on Model Interpretation* (ICML '18) & *Rethinking Cooperative Rationalization* (EMNLP '19 / NeurIPS '21) [31, 32].
7. **Vaswani et al. (2017) [Ref 23]:** *Attention is All you Need* (NeurIPS '17) [33].

---

### **Part 2: Dating App Retention Project Evaluation**

#### **(A) Alignment: Q1 or Q2 or Both or Neither?**
* **Category:** **Q2 Only** [3, 4, 10, 18].
* **Explanation:**
  * *Q1 (Industry/Production Attribution 2025–2026):* **No.** Published in September 2023 (RecSys '23), falling outside the 2025–2026 window [3, 4].
  * *Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):* **Yes.** The paper generates item/action-level retention scores (\\(s_{ui}\\)) and instance-level attention weights over individual user interactions to explain and predict 3-day user retention [9, 10, 18].

---

#### **(B) Q2 Class**
* **Classification:** **PARTIAL** [7, 11, 12, 14–17].
* **Justification:** IURO generates item/action-level retention scores (\\(s_{ui}\\)) via a UI Scorer and aggregates them using instance-level attention in Multi-Instance Learning (CMIL/RMIL) to predict 3-day retention [11–14]. The paper explicitly acknowledges and addresses offline-online gaps, unpredictable external factors (e.g., user mood or workload), and lack of explicit per-item retention signals [8, 11, 20]. However, it does not formulate an identified causal Multi-Touch Attribution (MTA) model under formal counterfactual graph identification [7, 14–17].

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Yes.** Generates user-item retention scores \\(s_{ui} = \text{FFN}_3(\text{concat}(u_p, u_l, v_i))\\) and instance-level attention weights (\\(\text{softmax}(\text{concat}(u_p, u_l) v_i / \sqrt{d})\\)) for individual user interactions [18, 19].
* **Target Outcome:** **Next-3-Day User Retention (\\(y_u\\))**, weighted by future 3-day engagement volume (\\(W_u = a \log(1 + n_c^u) + b \log(1 + n_i^u)\\)) [19, 20]. In online serving, candidate items are scored via \\(r_{ui} = \alpha \cdot \text{CTR}_{ui} + (1-\alpha) s_{ui}\\) [16].

---

#### **(D) Improving on Last-Touch N7 → Latest Swipes**
* **How it Improves Last-Touch:** Last-touch assigns 100% credit to the final swipe before Day 7, ignoring earlier high-value interactions [6-8]. IURO replaces rule-based last-touch heuristics by computing explicit user-item retention scores (\\(s_{ui}\\)) across all past interactions using Multi-Instance Learning [9, 10, 18]. It applies contrastive learning to sharpen "aha items" (high-impact interactions) and uses future behavior alignment (RMIL) as pseudo-causal keys to identify which specific past interactions truly drove return visits [7, 14–17].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Interaction Sequence:* User interaction logs are represented as a sequence of past candidate profile swipes, mutual matches, and 4-way messaging conversations [11–13].
  2. *UI Scorer (\\(s_{ui}\\)):* Evaluates each swipe, match, or messaging interaction based on user demographics (\\(u_p\\)), historical behavior (\\(u_l\\)), and candidate profile features (\\(v_i\\)) [18].
  3. *Aha Item Identification:* CMIL and RMIL identify "aha interactions"—such as a high-affinity mutual match or a deep messaging conversation—that served as the primary drivers of 7-day retention [7, 14–17].
  4. *Online Candidate Ranking:* Candidate profile recommendations are scored via \\(r_{ui} = \alpha \cdot \text{CTR}_{ui} + (1-\alpha) s_{ui}\\), prioritizing profiles that align with past retention-inducing "aha" interactions [16].

---

#### **(E) Selection-Bias & Confounding Handling**
1. **Future Engagement Supervised Weighting (\\(W_u\\)):** Multiplies retention targets by next-3-days cumulative activity (\\(W_u = a \log(1 + n_c^u) + b \log(1 + n_i^u)\\)) to reduce background noise from passive or accidental app opens [19, 20].
2. **Contrastive Multi-Instance Learning (CMIL):** Uses contrastive loss \\(L_{CL} = \max(0, |y_{MIL} - y_{CMIL}^{pos}| - |y_{MIL} - y_{CMIL}^{neg}| + m)\\) to broaden the attention gap between genuine "aha items" and passive background interactions [11, 20].
3. **Rationale Alignment via JS Divergence (RMIL):** Uses next-few-day clicks as external pseudo-causal keys to align the attention distribution via Jensen-Shannon divergence (\\(L_{JS}\\)), raising the overlap/consistency of selected "aha items" across initializations from **~35% to ~70%** [11, 12].

---

#### **(F) Deployed or Production Dataset Evidence**
* **Production Deployment:** Deployed live on a major industrial article recommendation feed (**Tencent WeChat**) serving over **3 million users** in an online A/B test [2, 16].
* **Offline Datasets:** **ZhihuRec 1M** (7,963 users, 81,214 items, 1,271,751 behaviors) and an **Industrial Dataset** (~1 million users, 500,000 items, 97 million behaviors) [21].
* **Quoted Quantitative Results:**
  * **Live Online A/B Test Lifts (Table 3):** **+0.76% next-day retention** and **+0.65% next-three-day retention** [16, 24].
  * **Hit Item Quality & Engagement:**
    * *Average CTR:* **0.129** for hit items vs. **0.082** (Exp Group) and **0.083** (Control Group) [17].
    * *Average Duration:* **98.73s** per item for hit items vs. **18.86s** (Exp Group) and **18.55s** (Control Group) [17].
    * *Filter Bubble Escape:* **34.08% of users** started following novel, surprising categories recommended by IURO in future clicks [17].
  * **Offline Retention AUC Performance (Table 2):**
    * *ZhihuRec 1M:* Base MLP (**0.7180**), IURO(AVG) (**0.5838**), IURO(MIL) (**0.8269**), IURO(MIL+MSS) (**0.8312**), IURO(CMIL+MSS) (**0.8437**), IURO(RCMIL+MSS) (**0.8445**) [23].
    * *Industrial Dataset:* Base MLP (**0.6827**), IURO(AVG) (**0.6732**), IURO(MIL) (**0.7209**), IURO(MIL+MSS) (**0.7255**), IURO(CMIL+MSS) (**0.7291**), IURO(RCMIL+MSS) (**0.7301**) [23].
  * **Explicit User Feedback Analysis (Table 1 & Section 4.1):**
    * **69% of survey participants** claim they return if items are relaxing and stress-relieving [14].
    * *Relative Retention Rates by Negative Feedback Reason:* "Not interested in items" (**35.38% next-day / 36.45% next-3-day** — lowest retention), "Low-quality content" (**90.29% / 91.78%**), "Advertising promotion" (**91.89% / 93.06%**), "Poor diversity" (**97.33% / 98.36%**), "Exaggerating titles" (**98.98% / 99.05%**), "Don't like author/content" (**102.29% / 102.03%**), "Repeated recommendation" (**113.51% / 108.07%**) [15, 25].

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
**Priority:** see queue.md `G13`
