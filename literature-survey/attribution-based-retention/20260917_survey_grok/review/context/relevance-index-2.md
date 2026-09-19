# Relevance index 2/10 — Project Relevance sections of all cards (generated)

### Interpretable User Retention Modeling in Recommendation [14]
`2023_RecSys_IURO_Interpretable-User-Retention-Modeling.md`
**Source:** https://dl.acm.org/doi/pdf/10.1145/3604915.3608818  

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

### User Retention-oriented Recommendation with Decision Transformer [1]
`2023_WWW_DT4Rec_User-Retention-Oriented-Decision-Transformer.md`
**Source:** https://arxiv.org/pdf/2303.06347.pdf  

### **Source Evaluation: DT4Rec (*User Retention-oriented Recommendation with Decision Transformer*)**
*(Zhao et al., City University of Hong Kong, Wuhan University, & Baidu Inc., WWW 2023: `arxiv:2303.06347`)* [1]

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**
* **Answer:** **Neither.** [1-3]
* **Explanation:**
  * *Q1 (Industry/Production Attribution 2025–01 to 2026-09):* **No.** Published at WWW 2023 (May 2023), which falls outside the 2025–2026 window [1–2]. Furthermore, it is evaluated on offline benchmark datasets rather than an industry production attribution pipeline [1, 16–17].
  * *Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):* **No.** DT4Rec formulates sequential recommendation for user retention as offline reinforcement learning via Decision Transformers (autoregressive sequence modeling) [1, 4, 5]. It does **not** perform multi-touch causal sequence attribution or publish per-exposure retention credit scores [4-6].

---

### **(B) Q2 Class**
* **Classification:** **NOT** [1, 4-6]
* **Justification:** DT4Rec is an offline RL / Decision Transformer sequence modeling framework that generates candidate recommendation lists conditioned on target retention reward prompts [4, 5, 7]. It does **not** output or publish a per-exposure retention credit table or multi-touch attribution decomposition [4, 5].

---

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction credit.** [4-6]
* **Target Outcome & Formula:** Replaces temporal value estimation with autoregressive sequence generation [4, 5]. Given a prior trajectory \\(\tau = [s_1, a_1, r_1, \dots, s_t, a_t, r_t]\\), it predicts future actions \\(a_{t+1}\\) conditioned on target retention reward prompts [5–6]. The retention outcome \\(e_t\\) is defined as user log-in frequency across \\(K\\) future timesteps [3]:
  \\[e_t = \sum_{k=1}^K \mathbb{1}[\text{log-in}_{t+k}]\text{}\\]

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**
* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% of the binary N7 retention label to recent swipes post-hoc. DT4Rec replaces post-hoc last-touch rule assignment by modeling candidate profile generation autoregressively using a Decision Transformer [4, 5]. It conditions recommendation generation on a target retention prompt \\(r\\) (e.g., active on day 7), generating candidate profiles whose sequence probability maximizes the desired return [4, 6–7].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *State (\\(s_t\\)):* Encodes historical swiping, matching, and 4-way conversation interactions using GRU action encoders and Transformer decision blocks [5, 8–11].
  2. *Action (\\(a_t\\)):* The generated candidate profile list for swiping [3, 8].
  3. *Auto-Discretized Reward Prompt (\\(r\\)):* Encodes the desired 7-day retention target (\\(e_t\\)) using meta-embedding aggregation \\(\hat{r} = \sum_{b=1}^B z_b M_b\\) to maintain partial ordering across retention levels [3, 9].
  4. *Weighted Contrastive Policy Learning:* Treats low-retention trajectories (e.g., swiping sessions resulting in churn) as weighted negative samples (\\(\mathcal{L}_{\text{CL}}\\)), steering the ranker away from generating profile lists that mirror past low-retention swiping patterns [13–15].

---

### **(E) Selection-Bias & Confounding Handling**
1. **Auto-Discretized Reward Prompt Module:** Translates scalar retention rewards \\(r\\) through a neural weighting network \\(z = \phi(W \sigma(w \hat{r}) + \alpha \sigma(w \hat{r}))\\) to aggregate meta-embeddings, preserving the partial ordering between different retention values [4, 9].
2. **Weighted Contrastive Supervised Policy Learning:** Addresses out-of-distribution (OOD) generation issues (where inference conditions on maximum rewards while training encounters diverse rewards) by incorporating low-reward trajectories as weighted negative samples [4, 13–15]:
   \\[\mathcal{L}_{\text{CL}} = -\sum_{v^- \in \Upsilon} \hat{v}(\tilde{a}^-) f_s(\tilde{a}, \tilde{a}^-)\text{}\\]
   This prevents the model from ignoring low-reward data during autoregressive training [13–14, 27–28].
3. *Note:* Does not use explicit Inverse Propensity Weighting (IPW) or causal graph debiasing for user swiping selection bias [3–4].

---

### **(F) Deployment and Production Dataset Evidence**
* **Production Deployment:** **Not specified in source.** [1] (Evaluated offline on benchmark datasets; open-source code released at `https://github.com/kesenzhao/DT4Rec.git`) [1, 10].
* **Offline Datasets:** **IQiYi Dataset** (large-scale online video platform interaction dataset) and **MovieLens-1M (ML-1m)** (6,040 users, 3,900 movies, 1,000,209 ratings) [16–17].
* **Quoted Quantitative Results:**
  * **Prediction Accuracy Benchmark (Table 2):**
    * *IQiYi Dataset:* DT4Rec achieved **HR@5 = 0.2524**, **NDCG@5 = 0.1601**, **HR@10 = 0.3601**, **NDCG@10 = 0.1983** (statistically significant improvements over SASRec **0.2312 / 0.1478 / 0.3385 / 0.1821** and BERT4Rec **0.2104 / 0.1325 / 0.3150 / 0.1628**) [21–23].
    * *MovieLens-1M Dataset:* DT4Rec achieved **HR@5 = 0.4331**, **NDCG@5 = 0.4185**, **HR@10 = 0.5679**, **NDCG@10 = 0.3342** (statistically significant improvements over SASRec **0.4052 / 0.3983 / 0.5409 / 0.3123**) [11].
  * **User Retention Benchmark Performance (IQiYi Dataset, Table 3):**
    * *Model-Based User Return Score (MB-URS, higher is better):* DT4Rec = **6.05** vs. LIRD (**5.63**), TopK (**5.41**), DT4Rec-R (**5.16**) [11, 12].
    * *Similarity-Based User Return Score (SB-URS, higher is better):* DT4Rec = **72,270** vs. LIRD (**63,572**), TopK (**61,045**), DT4Rec-R (**52,131**) [11, 12].
    * *Improved User Retention (IUR, higher is better):* DT4Rec = **26.0%** relative user retention improvement vs. LIRD (**17.3%**), TopK (**12.7%**), DT4Rec-R (**7.5%**) [11, 12].
    * *No Return Count (NRC, churn rate, lower is better):* DT4Rec = **1.5%** vs. LIRD (**1.9%**), TopK (**2.0%**), DT4Rec-R (**2.6%**) [11].
  * **Ablation Study (IQiYi Dataset, Table 4):**
    * *Without Contrastive Learning (`w/o contrastive`):* SB-URS dropped to **65,175** (**-9.82%**), MB-URS dropped to **5.68** (**-6.11%**), IUR dropped to **18.3%** (**-29.6%** relative drop) [10].
    * *Without Contrastive Weighting (`w/o weight`):* SB-URS dropped to **69,316** (**-4.09%**), MB-URS dropped to **5.79** (**-4.30%**), IUR dropped to **20.6%** (**-20.8%**) [10].
    * *Without Auto-Discretized Reward Prompt (`w/o auto-dis`):* SB-URS dropped to **70,953** (**-1.82%**), MB-URS dropped to **5.96** (**-1.49%**), IUR dropped to **24.2%** (**-6.9%**) [10, 13].

---

💡 *Would you like to explore how DT4Rec's auto-discretized reward prompt or weighted contrastive loss could be adapted to condition candidate profile generation on 7-day retention goals for your dating app?*

---

