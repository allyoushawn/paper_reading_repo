# Sequential Recommendation for Optimizing Both Immediate Feedback and Long-term Retention

**Source:** https://arxiv.org/html/2404.03637  
**Date analyzed:** 2026-09-18  
**NLM source id:** `305cd94b-33e0-46f8-961a-2228a9d46046`  
**Queue id:** G22  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Sequential Recommendation for Optimizing Both Immediate Feedback and Long-term Retention*
* **Authors:** Not specified in source.
* **Affiliations:** Not specified in source.
* **Year:** **2024** (April 2024, `arXiv:2404.03637v2`).
* **Venue:** arXiv pre-print (`arXiv:2404.03637v2`).

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Standard sequential recommender systems often optimize a single metric—either immediate user feedback (e.g., Click-Through Rate / CTR) or long-term retention (e.g., return frequency) [11–12]. Optimizing solely for immediate feedback leads to myopic recommendations, while focusing only on retention ignores immediate user satisfaction [11–12]. However, adapting Decision Transformers (DT) to multi-reward contexts presents major challenges:
  1. Complex dynamics among diverse user responses make reward design difficult [1].
  2. Interdependencies among multiple objectives introduce training complexity and task interference [1].
* **Key Contributions:**
  1. **DT4IER Framework:** Introduces Decision Transformer for Integrated Engagement and Retention, a framework engineered for long short-term multi-task sequential recommendation scenarios [5–6].
  2. **Adaptive RTG Balancing Module:** Adaptively reweights short-term (CTR) and long-term (return frequency) Return-to-Go (RTG) sequences using user-specific features to bridge immediate feedback and retention [5, 14–15].
  3. **Multi-Reward Encoder & Contrastive Loss:** Implements a high-dimensional encoder for 2D multi-task rewards along with a contrastive learning loss (\\(\mathcal{L}_{\text{contra}}\\)) to prevent predicted action embeddings for distinct rewards from converging too closely [5, 14–16].
  4. **Empirical Validation:** Demonstrates superior performance across three real-world benchmark datasets against state-of-the-art sequential recommenders and multi-task learning models [2, 3].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Problem Formulation & MDP Trajectory**
* Formulates multi-reward sequential recommendation using trajectory representations [8, 11–12]:
  \\[\tau = \left(\hat{\mathbf{R}}_1, \mathbf{s}_1, \mathbf{a}_1, \dots, \hat{\mathbf{R}}_t, \mathbf{s}_t, \mathbf{a}_t, \dots, \hat{\mathbf{R}}_T, \mathbf{s}_T\right)\\]
  * **Session \\(t\\):** Individual timestamp / day in a trajectory of length \\(T\\) [4].
  * **State \\(\mathbf{s}_t\\):** User's historical interaction information (clicked item IDs zero-padded to length \\(H=30\\)) [4].
  * **Action \\(\mathbf{a}_t\\):** Recommendation list containing item IDs of length \\(N=30\\) [4].
  * **Reward \\(\mathbf{r}_t = (r_{s,t}, r_{l,t}) \in \mathbf{R}^2\\):** Short-term indicator \\(r_{s,t}\\) is the Click-Through Rate (CTR) for recommended list \\(\mathbf{a}_t\\) at session \\(t\\); long-term indicator \\(r_{l,t}\\) is return frequency for session \\(t\\) [4].
  * **Return-to-Go (RTG) \\(\hat{\mathbf{R}}_t = [\hat{R}_{s,t}, \hat{R}_{l,t}] = [\sum_{i=t}^T r_{s,i}, \sum_{i=t}^T r_{l,i}]\\):** Un-discounted cumulative short- and long-term rewards from session \\(t\\) to \\(T\\) [4].

#### **Core Architectural Modules**
1. **Adaptive RTG Balancing Block:** Reweights the short- and long-term RTG sequence adaptively using user-specific features [14–15].
2. **State-Action & Reward Embedding Module:** Uses a GRU encoder for state and action sequences (converting discrete item ID sequences of length 30), a high-dimensional encoder for 2D rewards, and positional session encodings [14, 17, 27–29].
3. **Transformer Decision Block:** Uses a unidirectional Transformer with multi-head self-attention, skip connections, and GELU activation to generate action embeddings prompted by the balanced RTG vector [14, 27–28].
4. **Action Decoding Block:** Decodes predicted action embeddings into recommended item ID sequences using a GRU decoder [14, 28–29].
5. **Joint Loss Function:** Combines cross-entropy loss \\(\mathcal{L}_{\text{cross}}\\) (over one-hot encoded item IDs) with a contrastive learning loss \\(\mathcal{L}_{\text{contra}} = -\sum_{\hat{\mathbf{E}}^{A-} \in \Omega^-} D(\hat{\mathbf{E}}^A, \hat{\mathbf{E}}^{A-})\\), where negative samples \\(\Omega^-\\) are low-performing sessions with CTR and retention rewards below 0.6 [16–18]:
   \\[\mathcal{L} = \mathcal{L}_{\text{cross}} + \alpha \mathcal{L}_{\text{contra}}\\]
   (with contrastive loss weight \\(\alpha = 0.1\\)) [5, 6].

#### **Credit Assignment Mechanics**
* Does **not** perform explicit multi-touch credit assignment or fractional attribution to individual items/swipes across a historical sequence.
* Instead, DT4IER models sequential recommendation autoregressively using a Decision Transformer by predicting action embeddings conditioned on a multi-reward Return-To-Go prompt \\(\hat{\mathbf{R}}_t = [\hat{R}_{s,t}, \hat{R}_{l,t}]\\) [8, 10–12].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets:**
  1. **Kuairand-Pure:** Unbiased sequential recommendation dataset featuring random video exposures [3].
  2. **MovieLens-25M (ML-25M):** Large-scale sparse sequential recommendation benchmark [3].
  3. **RetailRocket:** Real-world e-commerce recommendation dataset [3].
* **Production Deployment:** Not specified in source (evaluated offline on benchmark datasets).
* **Comparison Baselines:**
  * **Sequential Recommender Systems (SRSs):** BERT4Rec, SASRec, GRU4Rec [7, 8].
  * **Multi-Task Learning (MTL) Models:** MMoE and PLE (adapted for sequential recommendation using weighted scores) [6, 9].
  * **Decision Transformer Baselines & Ablations:** Standard DT, DT4Rec, and ablation variants (NAW: No Adaptive Weighting, NRE: No Reward Encoder, NCL: No Contrastive Loss) [8, 10, 11].

---

### **(5) Key Quantitative Results with Numbers**
* **Ablation Study Improvements (Section 4.6 & Passage 21):**
  * **Adaptive RTG Balancing (DT4IER vs. NAW):** Achieves improvements of **+1.50% in BLEU**, **+1.90% in NDCG**, and **+0.08% in SB-URS** over the no-adaptive-weighting variant.
  * **Multi-Reward High-Dimensional Embedding (DT4IER vs. NRE):** Outperforms NRE by **+1.80% in BLEU**, **+2.30% in NDCG**, and **+0.19% in SB-URS**.
  * **Contrastive Loss (DT4IER vs. NCL):** Outperforms NCL by **+1.02% in BLEU**, **+1.60% in NDCG**, and **+0.03% in SB-URS**.
* **RTG Prompting Sensitivity Analysis (Section 4.7 & Passages 22–23):**
  * Evaluated RTG prompting proportions from **0.4 to 1.0**.
  * Recommendation accuracy (BLEU and NDCG) increased consistently between **0.4 and 0.8**, reaching peak performance at an RTG proportion of **0.8** (prompting beyond 0.8 showed saturation without additional gains).
* **Model Hyperparameters (Section 4.4 & Passage 20):**
  * Trajectory length \\(T = 20\\); state/action length \\(H = N = 30\\); 2 Transformer layers; 8 heads; embedding size 128; batch size 128; balance term \\(\gamma = 0.5\\); contrastive loss weight \\(\alpha = 0.1\\).

---

### **(6) Limitations, Failure Modes, or Negative Results**
1. **Performance Collapse without High-Dimensional Reward Encoding (NRE Variant):** Naive 2D reward encoding without the dedicated high-dimensional module performed worst across all metrics (BLEU dropped by **1.80%**, NDCG by **2.30%**, SB-URS by **0.19%**), showing that simple scalar/vector reward representations fail to capture task interplay [11].
2. **Action Embedding Convergence without Contrastive Loss (NCL Variant):** Omitting contrastive loss (\\(\mathcal{L}_{\text{contra}}\\)) caused predicted action embeddings for distinct reward prompts to converge too closely, reducing recommendation accuracy (NDCG dropped by **1.60%**) [11].
3. **Saturation Point in RTG Prompting:** Prompting the Decision Transformer with maximum RTG values (1.0) did not yield optimal results; performance saturated at an RTG proportion of **0.8**, indicating that over-prompting does not translate into further performance gains [22–23].
4. **Offline Evaluation Scope:** Evaluated purely offline on benchmark datasets (Kuairand-Pure, ML-25M, RetailRocket) without live online production A/B testing reported in the text [3].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Chen et al. (2021a) [Ref 9]:** *Decision Transformer: Reinforcement Learning via Sequence Modeling* (NeurIPS '21) [10, 12, 13].
2. **Sun et al. (2019) [Ref 51]:** *BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer* (CIKM '19) [7, 8, 14].
3. **Kang & McAuley (2018) [Ref 27]:** *Self-Attentive Sequential Recommendation* (ICDM '18 / SASRec) [7, 8, 15].
4. **Vaswani et al. (2017) [Ref 58]:** *Attention is All You Need* (NeurIPS '17) [7, 12, 14].
5. **Zhao et al. (2023b) [Ref 73]:** *User Retention-oriented Recommendation with Decision Transformer* (WWW '23 / DT4Rec) [8, 10, 16].
6. **Ma et al. (2018b) / Tang et al. (2020) [Refs 38, 57]:** *MMoE* (KDD '18) & *PLE* (RecSys '20) (Multi-Task Learning baselines) [26, 37–38].
7. **Sutton & Barto (2018) / Ie et al. (2019a) [Refs 53, 24]:** *Reinforcement Learning: An Introduction* & *SlateQ* (IJCAI '19) [14, 15, 17].

---

💡 *Would you like to explore how DT4IER's adaptive RTG balancing module or contrastive loss could be adapted to condition candidate profile generation on both immediate match feedback and 7-day retention for your dating app?*

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

### **Source Evaluation: *Sequential Recommendation for Optimizing Both Immediate Feedback and Long-term Retention***
*(arXiv pre-print, April 2024: `arXiv:2404.03637v2`)*

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**

**Neither.** [1, 3, 11–12, 19]
* **Q1 (Industry/Production Attribution 2025-01 to 2026-09):** **No.** Published in April 2024 (`arXiv:2404.03637v2`), which falls outside the 2025–2026 window [1]. Furthermore, it is evaluated on offline benchmark datasets rather than an industry production attribution system [1, 2].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** DT4IER formulates long short-term multi-task sequential recommendation using an offline Reinforcement Learning / Decision Transformer framework [3, 4]. It generates candidate item sequences conditioned on multi-reward Return-to-Go (RTG) prompts rather than calculating per-touch attribution credit across historical interaction logs [3, 8, 11–12].

---

### **(B) Q2 Class**

**NOT.** [3, 8, 11–12]
* **Justification:** DT4IER is an offline RL / Decision Transformer sequence modeling framework that predicts recommended item lists conditioned on Return-to-Go (RTG) prompts [3, 8, 10–12]. It does **not** produce or publish a per-exposure retention credit table or multi-touch attribution decomposition.

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction credit table.** [8, 10–12]
* **Target Outcome & Formula:** Replaces temporal value estimation with autoregressive sequence generation. Given an input trajectory:
  \\[\tau = \left(\hat{\mathbf{R}}_1, \mathbf{s}_1, \mathbf{a}_1, \dots, \hat{\mathbf{R}}_t, \mathbf{s}_t, \mathbf{a}_t, \dots, \hat{\mathbf{R}}_T, \mathbf{s}_T\right)\\]
  it predicts future action sequence embeddings \\(\hat{\mathbf{E}}^A\\) conditioned on a 2D Return-to-Go prompt \\(\hat{\mathbf{R}}_t = [\hat{R}_{s,t}, \hat{R}_{l,t}] = [\sum_{i=t}^T r_{s,i}, \sum_{i=t}^T r_{l,i}]\\) [5, 6].
  * **Short-term indicator (\\(r_{s,t}\\)):** Click-Through Rate (CTR) for recommended list \\(\mathbf{a}_t\\) at session \\(t\\) [6].
  * **Long-term indicator (\\(r_{l,t}\\)):** Return frequency for session \\(t\\) measuring user retention [6].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**

* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% of the binary N7 retention label to recent swipes post-hoc, ignoring earlier swiping patterns and short- vs. long-term trade-offs. DT4IER replaces post-hoc last-touch rule assignment by modeling candidate profile generation autoregressively using a Decision Transformer [3, 10–11]. It conditions recommendation generation on an adaptively balanced multi-reward Return-to-Go prompt \\(\hat{\mathbf{R}}_t\\) (balancing immediate match/click rates and long-term 7-day retention/return frequency based on user features) [5, 11–15].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *State (\\(\mathbf{s}_t\\)):* Encodes historical swiping, matching, and 4-way conversation interactions (user-clicked/engaged profile IDs zero-padded to length \\(H=30\\)) using a GRU state-action encoder [6, 7].
  2. *Action (\\(\mathbf{a}_t\\)):* Generated candidate profile card recommendation list of length \\(N=30\\) [6].
  3. *Adaptive RTG Balancing:* Reweights short-term RTG (immediate right-swipe / match rate) and long-term RTG (7-day retention / return frequency) using user-specific attributes to resolve trade-off conflicts [14–15].
  4. *Contrastive Learning (\\(\mathcal{L}_{\text{contra}}\\)):* Treats low-performing swiping sessions (where both match rate \\(r_{s,t}\\) and retention reward \\(r_{l,t}\\) fall below **0.6**) as negative samples \\(\Omega^-\\), preventing action embeddings for distinct reward prompts from converging too closely and steering the ranker away from low-retention swiping patterns [8].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Adaptive RTG Balancing Module:** Reweights short-term (CTR) and long-term (return frequency) RTG sequences using user-specific attributes to balance immediate feedback with long-term retention [14–15].
2. **Contrastive Learning Objective (\\(\mathcal{L}_{\text{contra}}\\)):** Defines negative samples \\(\Omega^-\\) as session data points where short- and long-term rewards are consistently below **0.6** (falling below average in both click rate and retention metrics) [8]. The contrastive loss \\(\mathcal{L}_{\text{contra}} = -\sum_{\hat{\mathbf{E}}^{A-} \in \Omega^-} D(\hat{\mathbf{E}}^A, \hat{\mathbf{E}}^{A-})\\) ensures action embeddings for distinct reward prompts do not converge too closely [8].
3. **Cross-Entropy Loss over One-Hot Discrete Actions:** Converts discrete action space elements (item IDs of length **30**) into one-hot encoded labels and optimizes via cross-entropy loss \\(\mathcal{L}_{\text{cross}} = -\sum_{z=1}^Z y_{o,z} \log(p_{o,z})\\) combined with \\(\alpha \mathcal{L}_{\text{contra}}\\) (\\(\alpha = \mathbf{0.1}\\)) [17–18].
4. *Note:* Does not use explicit Inverse Propensity Weighting (IPW) or formal causal graph identification for user swiping selection bias.

---

### **(F) Deployment and Production Dataset Evidence**

* **Production Deployment:** **Not specified in source** (evaluated offline on benchmark datasets) [2].
* **Offline Datasets:**
  * **Kuairand-Pure:** Unbiased sequential recommendation dataset featuring random video exposures [2].
  * **MovieLens-25M (ML-25M):** Large-scale sparse benchmark for sequential recommender systems [2].
  * **RetailRocket:** Real-world e-commerce recommendation dataset [2].
* **Quoted Quantitative Results:**
  * **Ablation Study Improvements (Section 4.6 & Passage 21):**
    * *Adaptive RTG Balancing (DT4IER vs. NAW):* **+1.50% in BLEU**, **+1.90% in NDCG**, **+0.08% in SB-URS**.
    * *Multi-Reward Encoder (DT4IER vs. NRE):* **+1.80% in BLEU**, **+2.30% in NDCG**, **+0.19% in SB-URS**.
    * *Contrastive Loss (DT4IER vs. NCL):* **+1.02% in BLEU**, **+1.60% in NDCG**, **+0.03% in SB-URS**.
  * **RTG Prompting Saturation Analysis (Section 4.7 & Passages 22–23):** Performance (BLEU and NDCG) increases consistently as RTG prompt proportion increases from **0.4 to 0.8**, achieving peak accuracy at **0.8** (prompting beyond 0.8 shows saturation without additional gains).
  * **Model Hyperparameters (Section 4.4 & Passage 20):** Trajectory length \\(T = \mathbf{20}\\); maximum state/action sequence length \\(H = N = \mathbf{30}\\); **2** Transformer layers; **8** heads; embedding size **128**; Adam optimizer batch size **128**; learning rate **0.005** (Kuairand-Pure) and **0.02** (ML-25M, RetailRocket); contrastive loss negative threshold **0.6**; contrastive loss weight \\(\alpha = \mathbf{0.1}\\); balancing term \\(\gamma = \mathbf{0.5}\\).

---

💡 *Would you like to explore how DT4IER's adaptive RTG balancing block or contrastive loss could be adapted to condition candidate profile generation on both immediate match feedback and 7-day retention for your dating app?*

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
**Priority:** see queue.md `G22`
