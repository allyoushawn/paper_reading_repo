# Paper Analysis: PinnerFormer: Sequence Modeling for User Representation at Pinterest

**Source:** https://arxiv.org/pdf/2205.04507  
**Source ID:** 29080c52-b3ed-4ef6-b2ad-36e4c1da2d6e  
**Date analyzed:** 2026-08-18  
**Model identifier:** codex-sol  
**Evidence mode:** Three independent source-scoped NotebookLM queries; no conversation reuse and no fallback.

---

## 1. Summary

**Title:** PinnerFormer: Sequence Modeling for User Representation at Pinterest  
**Authors:** Not specified in source-scoped response.  
**Abstract:** PinnerFormer learns a single transferable Pinterest user representation from action sequences. Its dense all-action objective targets a window of future engagements, allowing daily batch embeddings to retain much of the value of real-time sequence inference.

### **(1) Core Problem and Key Contribution**

*   **Core Problem:** 
    *   **Limitations of Myopic "Next Action" Prediction:** Traditional sequential recommender models are optimized to predict a user's immediate next action [1, 2]. While conceptually straightforward, this myopic focus does not align well with daily-updated offline batch architectures, making them highly sensitive to short-term variations and staleness [3-5].
    *   **Extreme Infrastructure and Computational Cost:** Serving sequential models in real time is computationally expensive, requiring the system to fetch a user's entire history and perform inference on complex models after every single user action [6]. Alternatively, stateful architectures require highly complex, real-time streaming infrastructure to maintain and warm up users' hidden states in the face of potential data corruption [6, 7].
    *   **Poor Personalization Scalability:** Platforms often maintain dozens of distinct ranking and retrieval models [8]. Developing, training, and serving custom user representations for each model is computationally and operationally unscalable [8].
    *   **Storage Bottlenecks of Multi-Embedding Models:** Multi-embedding architectures (such as Pinterest's legacy model, PinnerSage) struggle to scale at the ranking stage because storing multiple high-dimensional embeddings for millions of items in billion-row datasets incurs unsustainable memory and data-loading costs [9].

*   **Key Contributions:**
    *   **PinnerFormer:** An end-to-end learned sequence model that outputs a **single, highly transferrable user representation** [1, 3, 9]. It is designed to be computed in an inexpensive, offline batch setting and has been deployed in production at Pinterest since Fall 2021 [1, 3, 10].
    *   **Dense All-Action Loss:** A novel training objective that models long-term future user actions instead of only predicting the immediate next step [1, 3].
    *   **Mitigating the Real-Time vs. Batch Gap:** The authors demonstrate that the dense all-action loss nearly **halves the performance gap** between a model computed once a day in batch and one computed in real time after every user interaction, making batch serving highly practical [4, 11].
    *   **Versatile Auxiliary Feature:** Instead of training specialized representations for each downstream surface, a single PinnerFormer user embedding acts as a robust feature that drives substantial engagement lifts across multiple independent ranking models (such as Homefeed and Ads) [8, 11, 12].

---

### **(2) Proposed Method or Architecture in Detail**

```
+--------------------+
| User Action Stream | (1 Year History, M most recent) [10]
+---------+----------+
          |
          v
+--------------------+
|  Feature Encoding  | (PinSage, action type, surface, duration, relative time) [13]
+---------+----------+
          |
          v
+--------------------+
|  Transformer Core  | (Pre-Norm layers, Causal Masking MHSA, FFN blocks) [14-17]
+---------+----------+
          |
          v
+--------------------+
|  Output MLP & L2   | (Outputs user embedding sequence E; extracts e1) [15, 17, 18]
+---------+----------+
          |
          v
+--------------------+
|Dense All-Action Lss| (Computes sampled softmax with logQ, mixed negatives, K-day window) [19-21]
+--------------------+
```

#### **1. Input and Feature Encoding**
*   The model takes a user's sequence of actions \\(A_U = \{A_1, A_2, \dots, A_S\}\\) over the past year, truncated to the \\(M\\) most recent actions [10]. It focuses on predicting positive engagement: Pin saves (Repins), close-ups lasting \\(>10\\) seconds, and link clicks lasting \\(>10\\) seconds on the Homefeed [22].
*   For each action, the input features are concatenated into a single vector \\(a_i \in \mathbb{R}^{D_{\text{in}}}\\) [14]:
    *   **PinSage Embedding:** A pre-computed 256-dimensional vector aggregating visual, text, and engagement information for the Pin [10].
    *   **Categorical Metadata:** Action type and interaction surface are mapped through small, learnable embedding tables [13].
    *   **Duration:** Encoded as a scalar value, \\(\log(\text{duration})\\) [13].
    *   **Relative Time:** The time elapsed since the user's last action, and the time gap between consecutive actions, are encoded using a logarithmic transformation and Time2vec-style sine and cosine periodic transformations [13, 23]. It utilizes \\(P_{\text{abs}} = 12\\) manually selected fixed periods (ranging from 15 minutes to 1 year) [24] and \\(P_{\text{rel}} = 32\\) evenly spaced periods on a log scale (ranging from 1 second to 4 weeks) [24].

#### **2. Model Architecture**
*   **Transformer Core:** Projected features are added to learnable positional encodings to form \\(V^{(0)} \in \mathbb{R}^{M \times H}\\) [16]. The sequence is processed through alternating multi-head self-attention (MHSA) and feedforward network (FFN) blocks [15, 16]. 
*   **Pre-Norm Connections:** Layer normalization is applied before each block (rather than after) to maximize training stability [14, 17].
*   **Causal Masking:** A temporal mask is applied within the self-attention blocks to ensure each item can only attend to past or present actions in the sequence [16, 21].
*   **Embedding Extraction:** The transformer output \\(V^{(L)}\\) is passed through a two-layer output MLP (LayerNorm, linear layer, GELU activation, linear layer) and \\(L2\\) normalized, yielding a sequence of embeddings \\(E = (e_1, e_2, \dots, e_M)^T \in \mathbb{R}^{S \times D}\\) [15, 17, 18].
*   **Final User Embedding:** The first row \\(e_1\\) (representing the most recent sequence output) is selected as the final user embedding \\(u \in \mathbb{R}^D\\) [18].
*   **Pin Embedding:** Pins are represented by passing their raw PinSage embeddings through a small MLP and applying \\(L2\\) normalization [25].

#### **3. Dense All-Action Loss**
*   **Predictive Objective:** Instead of using \\(e_1\\) to predict only the next immediate action [21, 26], the **dense all-action loss** selects random indices \\(\{s_i\}\\) from the sequence [21]. For each \\(e_{s_i}\\), the model is trained to predict a randomly selected positive action from the subsequent \\(K\\)-day future window [21].
*   **Mixed Negative Sampling:** Negatives are collected across all GPUs used in training to build a massive candidate pool [27]. It merges **in-batch negatives** (positive items from other users in the batch, with positive items for the target user masked out) [19, 28] and **random negatives** uniformly sampled from the corpus [19, 28]. In production, the model caps in-batch negatives at 5,000 and fixes random negatives to 8,192 [29].
*   **Sampled Softmax with logQ Correction:** To correct for popularity and sampling bias, the model applies a logQ correction term \\(Q_i(v)\\) (approximated online via a count-min sketch) to the logits, utilizing a learned temperature parameter \\(\tau \in [0.01, \infty)\\) [20, 30]:
    \\[ \mathcal{L}(u_i, p_i) = -\log \left( \frac{e^{s(u_i, p_i) - \log(Q_i(p_i))}}{e^{s(u_i, p_i) - \log(Q_i(p_i))} + \sum_{j=1}^N e^{s(u_i, n_j) - \log(Q_i(n_j))}} \right) \\]

#### **4. Daily Incremental Serving Workflow**
*   Running offline daily, the pipeline identifies users who have taken new actions in the past day, infers their new PinnerFormer user embeddings, merges them with the existing database, and uploads them to a low-latency online key-value feature store [31, 32].
*   Pin representations are cheap to compute and are regenerated from scratch daily [33]. The system compiles them into a **Hierarchical Navigable Small World (HNSW) graph** for fast nearest-neighbor online retrieval [33].

---

### **(3) Datasets Used for Evaluation and Comparison Baselines**

*   **Evaluation Dataset & Setup:**
    *   **Evaluation Window:** Disjoint evaluation cohorts are constructed at a fixed training end-time \\(t\\) [34]. The model generates a user representation at \\(t\\) and is evaluated on its ability to retrieve all Pins the user positively interacts with over a **14-day future window** \\((t, t+14d]\\) [34, 35].
    *   **Retrieval Index:** Candidate generation is evaluated by querying the user embedding against an index containing **1 million random Pins** [34].
    *   **Metrics:** 
        *   *Recall@10:* Measures retrieval accuracy of positive future engagements [34, 36].
        *   *Interest Entropy@50:* Measures the topic diversity of the top 50 retrieved results for an individual user across 350 unique subjects [36].
        *   *P90 Coverage@10:* Global diversity metric measuring what fraction of the 1M index accounts for 90% of the top 10 retrieved results across all users [36].

*   **Comparison Baselines:**
    *   **PinnerSage (Previous Production Champion):** A multi-embedding clustering model [13, 37]. To evaluate accuracy, it uses an oracle baseline selecting the closest of \\(c\\) user clusters (e.g., 5 or 20 clusters) to the positive pin [38, 39]. Diversity is evaluated using round-robin blending of the clusters' retrieved results [38].
    *   **SASRec:** A standard next-item sequential baseline [26]. It is adapted for fair comparison by replacing its standard binary cross-entropy loss with PinnerFormer's sampled softmax and applying equal loss weighting to \\(e_1\\) and internal sequence positions [26, 40].
    *   **Inference Frequency Baselines:** To quantify the performance degradation of batch serving, the dense all-action loss is compared against next-action prediction models across three frequencies: **Once** (using only the embedding at \\(t\\) for 14 days), **Daily** (re-computed with a 1-day delay), and **Real-time** (updated after every action) [26, 41].
    *   **Negative Sampling Variants:** Evaluates models trained on random negatives only, in-batch negatives only, or mixed negatives, with and without Sample Probability Correction (SPC) [42].
    *   **Single-Task Models:** Evaluates task-specific single-head networks trained strictly to predict close-ups, clicks, or Repins individually [43].
    *   **Feature Ablation Suites:** Assesses performance drops by removing individual input components (PinSage, Timestamp, Surface, Action Type, Duration, and Positional Encoding) [44].
    *   **Hyperparameter Ablations:** Conducts performance sweeps across varying sequence lengths (\\(1\\) to \\(256\\)) [43, 45], final embedding dimensions (\\(8\\) to \\(1024\\)) [29], and transformer layer capacities [46].

***

🎨 I can use Python in our sandbox using matplotlib to plot and compare PinnerFormer's offline Recall@10 and P90 index coverage across varying sequence lengths, reproducing the exact curves shown in the paper's hyperparameter evaluation (Figure 4).

---

## 2. Experiment Critique

### **(1) Key Quantitative Results and Improvements over Baselines**

*   **Offline Evaluation (Recall@10, Diversity, and Coverage):**
    *   **PinnerFormer vs. PinnerSage (Table 1):** The single-embedding PinnerFormer significantly outperforms the previous multi-embedding PinnerSage baseline on the 14-day engagement task [1-3]. Even when evaluating PinnerSage using an optimistic oracle selection over 5 or 20 clusters, PinnerFormer achieves a **Recall@10 of 0.229**, compared to 0.026 for PinnerSage (5 clusters) and 0.046 for PinnerSage (20 clusters) [1, 2, 4]. 
    *   In terms of diversity, PinnerFormer scores **1.97 on Interest Entropy@50** (PinnerSage with 20 clusters scores 2.10) [1, 3, 4] and **0.042 on global P90 Coverage@10** [1, 3, 4].
*   **Mitigating the Real-time vs. Daily Batch Gap (Table 2):**
    *   A sequential model trained on standard next-item prediction (SASRec) suffers a severe **13.9% performance drop in Recall@10** when moving from real-time updates to daily batch inference [2].
    *   PinnerFormer, trained with the **dense all-action objective**, experiences only an **8.3% drop in Recall@10** under daily batch serving [2], nearly halving the performance gap and making computationally inexpensive daily offline inference highly viable [5-7].
*   **Impact of the Dense All-Action Window (Table 3):**
    *   Training with the **Dense All-Action loss using a 28-day window** achieves the highest **Recall@10 of 0.229** (P90 Coverage: 0.042) [8].
    *   This outperforms the same loss trained on a 14-day window (0.223) [8], a naive All-Action 28-day model (0.224) [8], a customized SASRec Softmax baseline (0.198) [8], and a standard Next Action model (0.186) [8].
*   **Negative Sampling and Sample Probability Correction (Table 4):**
    *   Applying **Sample Probability Correction (SPC)** to a **Mixed Negative pool** (combining random and in-batch negatives) maximizes retrieval accuracy, reaching a **Recall@10 of 0.229** [9, 10].
    *   Without SPC, mixed negatives achieve a Recall@10 of 0.138 [9]. Using in-batch negatives only with SPC drops Recall@10 to 0.167 [9], while using random negatives only with SPC yields a Recall@10 of 0.139 [9].
*   **Feature Ablation (Table 6):**
    *   The model relies most heavily on the **PinSage embedding** (omitting it drops Recall@10 to 0.142 and collapses P90 Coverage to 0.0005) [11] and the **Timestamp** (omitting it drops Recall@10 to 0.210) [11].
    *   Dropping other features (Surface, Action Type, Duration, or Positional Encoding) causes minor performance decreases [11].
*   **Online A/B Experiment Lifts:**
    *   **Homefeed Ranking (Table 7):** Replacing PinnerSage with PinnerFormer drove significant platform lifts: **+1.0% Time Spent**, **+0.4% Daily Active Users (DAU)**, **+0.12% Weekly Active Users (WAU)**, **+7.5% Homefeed Repins**, **+1.0% Clickthroughs**, and **+6.0% Close-ups** [12].
    *   **Ads Ranking (Table 8):** Adding PinnerFormer to downstream ad models delivered strong clickthrough rate (CTR) and long-click (gCTR) gains across three major surfaces [13]:
        *   *Related Pins:* **+7.1% CTR** and **+6.9% gCTR** [12].
        *   *Search:* **+7.3% CTR** and **+5.2% gCTR** [12].
        *   *Homefeed:* **+10.0% CTR** and **+10.1% gCTR** [12].

---

### **(2) Limitations, Failure Modes, or Negative Results Noted by the Authors**

*   **Multi-Task Performance Trade-Off:** Although the multi-task configuration achieves the highest *overall* Recall@10 (0.23), it is a compromise [14]. It performs slightly worse on each individual task (10s Closeup, 10s Click, and Repin) compared to dedicated single-task models trained strictly on those targets [9, 14, 15].
*   **Model Collapse on Random-Only Negatives:** When trained using random negatives in isolation, the model collapses [15]. It fails to capture fine-grained user interests and over-recommends universally popular items, retrieving highly similar content for almost all users (P90 Coverage drops to 0.001) [15].
*   **SPC vs. Diversity Trade-Off:** While applying Sample Probability Correction (SPC) significantly increases Recall@10, it does so at the cost of **decreasing global result diversity** (lowering global P90 Coverage@10) [10, 16].
*   **Dimension and Sequence Length Bottlenecks:**
    *   Doubling sequence lengths beyond 32 yields **diminishing returns** [17]. The authors limit sequences to 256 because longer sequences require compromises in batch size or make parallel model tuning too slow [17, 18].
    *   Varying the embedding size beyond 128 dimensions also yields diminishing returns in Recall@10 [19]. The authors select 256 dimensions purely to remain compatible with Pinterest's legacy infrastructure [20].
*   **PinnerSage Multi-Cluster Diversity Advantage:** When utilizing a sufficiently large number of clusters (e.g., 20), the older PinnerSage representation outperforms the single-embedding PinnerFormer in retrieving a diverse range of interests for a given user [3].
*   **Objective Loss Fusion Failures:** Attempting to sum losses computed from different training objectives together failed to outperform single-objective models [16].

---

### **(3) Top 5–7 Most Heavily Cited Prior Works**

1.  **PinnerSage** (*Pal et al., 2020* [21]) [22]:
    *   *Context:* Pinterest's previous multi-embedding user representation framework, heavily cited as the primary point of comparison and the baseline replaced in online experiments [3, 18, 23-25].
2.  **SASRec** (*Kang and McAuley, 2018* [24]) [26]:
    *   *Context:* The self-attentive sequential baseline, cited extensively as the architectural starting point for causal masking, dense multi-task loss comparison, and negative sampling modifications [27-30].
3.  **PinSage** (*Ying et al., 2018* [27]) [31]:
    *   *Context:* Pinterest's web-scale graph convolutional neural network, cited as the source of the 256-dimensional Pin embeddings that act as the primary input feature for PinnerFormer [21, 32-34].
4.  **Attention is All You Need** (*Vaswani et al., 2017* [35]) [36]:
    *   *Context:* The foundational paper introducing the Transformer network and multi-head self-attention used to sequence-model historical user actions [37, 38].
5.  **Practice on Long Sequential User Behavior Modeling / MIMN** (*Pi et al., 2019* [37]) [22]:
    *   *Context:* Cited to represent stateful sequential recommenders, helping frame the streaming infrastructure challenges, memory requirements, and data corruption risks that PinnerFormer bypasses by using batch serving [39-41].
6.  **Mixed Negative Sampling** (*Yang et al., 2020* [42]) [43]:
    *   *Context:* Google's two-tower neural network retrieval paper, cited to justify and detail the strategy of combining random and in-batch negatives to prevent model collapse [35, 43].
7.  **Time2vec** (*Kazemi et al., 2019* [40]) [26]:
    *   *Context:* Cited to define the methodology for time-timestamp feature encoding, which uses fixed cosine and sine periodic transformations over a log scale [21, 44].

***

🧩 We can write a Python script in our sandbox using matplotlib to plot PinnerFormer's offline Recall@10 and global P90 Coverage against sequence lengths and embedding dimensions, reproducing the hyperparameter curves.

**Overall assessment:** The reported offline comparisons and production experiments support the paper's representation-learning claims within Pinterest. Generalization to reciprocal dating, causal retention, and revenue objectives remains untested.

---

## 3. Industry Contribution and Project Relevance

### **(1) Project Needs Addressed**

*   **Source-Stated Facts:**
    *   **Unified Long-Term Objective:** The paper directly addresses the complexity of multi-task learning by training a single user embedding to predict multiple positive future engagement types (saves, close-ups, and clicks) simultaneously, bypassing the need for separate task-specific models or post-hoc blending [1, 2].
    *   **Delayed 7–30 Day Retention or Revenue Labels:** PinnerFormer replaces myopic next-action prediction with an objective designed to predict positive user engagements over a multi-day future window (evaluating on a **14-day horizon** [3, 4], and optimizing training on up to a **28-day horizon** [5-7]).
    *   **Multi-Stage Cascade:** Addressed partially via parallel multi-task learning of different engagement types (Closeup, Click, Repin) within the same sequence [1, 2, 8], though not formulated as a sequential conditional cascade.
    *   **Reciprocal Matching, Congestion/Exposure Externalities, Subscriptions plus à la carte value, Success-Paradox Censoring, and Prediction-versus-Incrementality:** **Not specified in source.**

*   **Survey Inference:**
    *   **Dating Recommender Alignment:** Viewer A’s sequential swiping stream (skips, likes, matches, chats) can be compiled chronologically. PinnerFormer's multi-day target horizon aligns perfectly with tracking whether viewer A will establish a delayed, high-value connection (e.g., active chat or subscription) with candidate B over a 7-to-30 day window.

---

### **(2) Transferable Method Components**

*   **Source-Stated Facts:**
    *   **Dense All-Action Loss:** Instead of predicting only the immediate next action from the final sequence state [9-11], this loss selects multiple random historical indices \\(\{s_i\}\\) in the user sequence and trains each intermediate embedding \\(e_{s_i}\\) to retrieve a randomly selected positive action from the subsequent \\(K\\)-day future window [12].
    *   **Causal-Masked Transformer Core:** The model projects historical sequences through a Transformer utilizing Pre-Norm residual connections [13] and applies causal masking to the self-attention blocks so each action only attends to past or present actions [12, 14].
    *   **Daily Incremental Batch Serving:** User embeddings are inferred daily in an offline batch setting and uploaded to a low-latency key-value store [15]. This avoids the extreme computational cost and streaming infrastructure complexity required to maintain stateful, real-time sequential recommenders [16, 17].
    *   **Sampled Softmax with logQ Correction & Mixed Negatives:** The loss function pools in-batch negatives (masking out positive actions for the target user) and random negatives uniformly sampled from the corpus [18, 19]. It applies a logQ correction (approximated via a count-min sketch) to adjust for item popularity sampling bias [20, 21].

*   **Survey Inference:**
    *   **Dating Ranker Transfer:** Instead of real-time scoring, the dating recommender can compute viewer A's sequential embedding once a day offline. During live serving, candidate profiles can be ranked using the cosine similarity between the daily batch user embedding and candidate B's vector representation, drastically reducing live infrastructure latency.

---

### **(3) Evidence Supporting Transfer**

*   **Source-Stated Facts:**
    *   **Closing the Batch-to-Realtime Gap:** Moving from real-time updates to daily batch inference drops retrieval accuracy (Recall@10) by **13.9%** under standard next-item prediction models (SASRec) [22, 23]. Utilizing the **dense all-action objective (PinnerFormer)** restricts this batch-processing loss to only **8.3%** [22-24].
    *   **Offline Retrieval Accuracy:** The Dense All-Action loss trained on a 28-day window achieved a **Recall@10 of 0.229** (P90 global coverage: 0.042) [7], significantly outpacing next-action prediction (0.186) and next-item SASRec (0.198) [7].
    *   **Downstream Model Generalization:** Although multi-task training slightly underperforms single-task models on their individual targets, it achieves the best overall generalization [2, 25, 26].
    *   **Online Production Gains:** Replacing the previous PinnerSage multi-embedding baseline with a single PinnerFormer user embedding in Pinterest's Homefeed ranking model drove major sitewide engagement: **+1% Time Spent, +0.4% DAU, +0.12% WAU, +7.5% Homefeed Repins, and +6% Close-ups** [27, 28]. It also generalized to Ads ranking, delivering up to **+10.0% CTR and +10.1% long-clicks (gCTR)** [28].

*   **Survey Inference:**
    *   The massive gains delivered across highly diverse surfaces (Homefeed, Search, Ads) prove that a single, unified sequential user embedding can successfully generalize to downstream, unobserved objectives (like long-term retention and monetized transactions) without requiring separate model pipelines.

---

### **(4) Critical Mismatches, Caveats, or Missing Requirements**

*   **Source-Stated Facts:**
    *   **Unilateral Action Constraint:** The sequence model is trained strictly on a single user's unilateral historical interactions with passive items (Pins) [8, 29].
    *   **Reciprocal Matching, Pool Congestion, SUTVA Interference, and Success-Paradox Churn:** **Not specified in source.**

*   **Survey Inference:**
    *   **The Bilateral Reciprocity Mismatch:** Unlike Pins, candidate B is an active stakeholder. Recommending B to viewer A is a wasted exposure if candidate B skips or rejects viewer A. PinnerFormer's strictly unilateral sequential framework cannot capture bilateral match reciprocity or queue congestion.
    *   **The Success Paradox:** A highly successful match results in users finding partners, entering relationships, and deleting the app (positive churn). Because PinnerFormer's training objective maximizes long-term, multi-day active app engagement [9, 28], the model will actively penalize successful pairings (which lead to account deletion) and over-recommend addictive, low-compatibility profiles that drive high-volume, superficial swiping.

***

📊 We could write a Python script in our sandbox using matplotlib to simulate how varying the future label window (\\(K\\)) impacts the gradient variance of the Dense All-Action loss on sparse, simulated dating cascades.

**Deployability:** Demonstrated in production at Pinterest; adaptation requires a sequence pipeline, daily embedding refresh, and integration into downstream rankers.  
**Engineering cost:** Substantial training and feature-pipeline cost, but serving can use one cached embedding rather than online sequence inference.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** A dense all-action loss and a single transferable sequence-derived user representation designed for efficient daily batch serving.  
**Prior work comparison:** The source-scoped prior-work evidence is included in Section 2.  
**Verification:** No independent web novelty audit was performed in this NotebookLM batch; novelty is reported as claimed by the paper.

---

## 5. Dataset Availability

**Datasets mentioned:** See the datasets and baselines subsection of Section 1. Pinterest production data are proprietary unless the source explicitly states otherwise.

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Pinterest engagement and production logs | Not specified in source | No | Proprietary platform data. |

**Offline experiment reproducibility:** Limited without the proprietary action logs and production infrastructure; the source-scoped response above records the reported architecture and evaluation setup.

---

## 6. Community Reaction

No significant community discussion was assessed in this source-scoped NotebookLM batch.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** Not specified in source-scoped response  
**Affiliations:** Pinterest  
**Venue:** KDD  
**Year:** 2022  
**PDF:** Available at source URL  
**Relevance:** Related  
**Priority:** 1  
**Direction:** D4 — retention / lifetime value / long-horizon value
