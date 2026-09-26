# UniShare: A Unified Framework for Joint Video and Receiver Recommendation in Social Sharing [1]

**Source:** https://arxiv.org/pdf/2602.09618.pdf  
**Date analyzed:** 2026-09-24  
**NLM source id:** `4824001b-1aa6-4c8e-9ff8-b77d45e029b4`  
**Queue id:** G31  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *UniShare: A Unified Framework for Joint Video and Receiver Recommendation in Social Sharing* [1]
* **Authors:** **Caimeng Wang**\*, **Li Chong**\*, **Dongxu Liu**, **Xu Min**†, and **Jianhui Bu** (\*Equal contribution, †Corresponding author) [1]
* **Affiliation:** **Kuaishou Technology**, Beijing, China [1]
* **Year & Venue:** **2025/2026** (ACM Reference Format: 2025; arXiv pre-print: `arXiv:2602.09618`, February 2026) [1, 2]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Social sharing on short-video platforms involves a complex ternary interaction among the user (sharer \\(U\\)), video content (\\(I\\)), and receiver (\\(V\\)) [1-3]. Traditional industrial systems decouple this into two isolated tasks: (1) **video recommendation** (predicting share probability) and (2) **receiver recommendation** (predicting whom to share with) [1, 4-6]. This decoupled approach causes isolated modeling (lacking cross-side signals), inadequate information utilization, and severe data sparsity, failing to optimize **bilateral satisfaction** (simultaneously satisfying sharer intent and receiver interest) [1, 4, 6, 7].
* **Key Contributions:**
  1. **Joint Ternary Formalization:** Formulates social sharing recommendation as a joint prediction problem over the \\(\langle U, I, V \rangle\\) triplet [1, 8, 15–18].
  2. **UniShare Architecture:** Proposes a unified framework featuring representation enhancement (pre-trained GNN social embeddings, multi-modal features, Bilateral Interest Modeling via target attention, and LLM-powered Relationship-Content Alignment) and a joint multi-task training paradigm with Hierarchical Negative Sampling [1, 6, 8, 19–25, 28–30].
  3. **K-Share Benchmark Dataset:** Constructs and releases **K-Share**, the first large-scale real-world sharing benchmark dataset from Kuaishou logs [1, 7, 9, 31–33].
  4. **Industrial Production Validation:** Validated via offline benchmarks and a 7-day live online A/B test on Kuaishou (+1.95% shares, +0.482% receiver reply rate) [1, 7, 52–53].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Architectural Components**
* **Ternary Probabilistic Formulation:** Models conditional probability \\(P(S=1 \mid U, I, V) = g(u, i, v; \theta)\\) for both Sub-task 1 (User-Pair Video Share Probability \\(f_1(i; u, \mathcal{V}_u)\\)) and Sub-task 2 (Per-Video Candidate Receiver Probability \\(f_2(v; u, i)\\)) [17–18].
* **Bilateral Interest Modeling (BIM):** Uses target attention over user \\(u\\)'s and candidate receiver \\(v\\)'s historical behavior sequences conditioned on video \\(i\\) (\\(\tilde{\mathbf{h}}_u = \sum \alpha_j \mathbf{h}_{uj}\\)). Sum pooling aggregates candidate receiver set \\(\mathcal{V}_u\\) embeddings for the video recommendation head [19–22].
* **Multi-Modal Semantic Enhancement:** Integrates video multi-modal embeddings \\(\mathbf{e}_{mm}(i)\\) from content understanding models and user multi-modal interest embeddings \\(\mathbf{e}_{mm}(u)\\), computing continuous matching scores \\(s_{match} = \mathbf{e}_{mm}(v) \cdot \mathbf{e}_{mm}(i)\\) to handle long-tail entities [23–24].
* **Relationship-Content Alignment (RCA):** Employs Qwen-VL LLM to evaluate relationship-content compatibility \\(s_{LLM} = \text{LLM}(\text{ASR}(i), \text{cover}(i), \text{relationship}_{uv})\\) across 6 candidate relationship types ("romantic partners", "buddies", "sister-friend", "elders", "juniors", "peers") [24, 37, 67–68]. Combines this with pre-trained social Graph Neural Network (GNN) embeddings \\(\mathbf{e}_{gnn}\\) trained with contrastive loss on follow graphs [8].
* **Hierarchical Negative Sampling (HNS):** Implements a two-tier negative sampling strategy for receiver recommendation: hard negatives (historical share recipients) and easy negatives (random social connections), producing up to 20 candidate receivers per request [9, 10].
* **Parameter Sharing & Joint Loss:** Shares embedding and feature transformation layers across tasks; freezes \\(u\\)-\\(i\\) parameters during receiver backpropagation. Joint loss \\(\mathcal{L}_{total} = \mathcal{L}_{video} + \alpha \mathcal{L}_{receiver}\\) (with weight \\(\alpha=2\\)), where \\(\mathcal{L}_{video}\\) uses binary cross-entropy on all impression samples and \\(\mathcal{L}_{receiver}\\) uses cross-entropy over sharing-labeled samples and HNS negatives [29–30, 37].

#### **Credit Assignment Mechanics**
* **Not specified in source / Does NOT assign per-touchpoint credit.**
* UniShare is a joint recommendation ranking architecture predicting binary sharing probabilities (\\(S \in \{0, 1\}\\)) on video and receiver candidates [3, 7, 11]. It does not perform multi-touch sequence attribution or assign fractional credit across past user interaction touchpoints.

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets & Scale:**
  * **K-Share Benchmark Dataset:** Constructed from a full month of real Kuaishou platform interaction logs [1, 12, 13].
  * *Scale:* **19,395 users**, **3,790,673 videos**, **11,310,319 video views**, **752,887 shares**, **1,306,752 friends**, and **186,886 receivers** (~1M share instances and ~10M video view events) [13, 14]. Stratified user sampling based on distinct receiver count (1:3:5 ratio) [15]. Evaluated using an 8:1:1 chronological train/validation/test split [16].
* **Production Deployment:**
  * Deployed live in production on the **Kuaishou** short-video platform [1, 7, 48–53].
  * *Online Serving Scheme:* Solves the \\(O(|I| \times |\mathcal{V}_u|)\\) computational complexity bottleneck during video feed browsing by utilizing an online retrieval policy that prunes candidate receiver set \\(\mathcal{V}_u\\) to the top 8 recently shared-with users (\\(\hat{\mathcal{V}}_u \le 8\\)) [48–51]. UniShare scores are merged as a key feature in a final re-ranking stage [17].
* **Comparison Baselines:**
  * *Video Recommendation Baseline:* Multi-task **PLE** (Progressive Layered Extraction) [18, 19].
  * *Receiver Recommendation Baseline:* **DCN** (Deep & Cross Network) [18, 19].
  * *Ablation Baselines:* `w/o all` (joint training only), `w/o RCA` (removes relationship-content alignment & GNN embeddings), `w/o BIM` (removes bilateral interest modeling), `w/o HNS` (removes hierarchical negative sampling) [35, 43–44].

---

### **(5) Key Quantitative Results with Numbers**

* **Offline Experiments on K-Share (Table 3):**
  * **Video Recommendation Sub-task:**
    * UniShare **AUC = 0.7588*** (+1.01% over PLE baseline **0.7512**).
    * UniShare **GAUC = 0.6976*** (+0.82% over PLE **0.6919**).
    * UniShare **Recall@10 = 0.2913*** (+1.53% over PLE **0.2869**).
    * UniShare **NDCG@10 = 0.3110** (vs. PLE **0.3099**), **MRR = 0.3934*** (vs. PLE **0.3880**).
  * **Receiver Recommendation Sub-task:**
    * UniShare **AUC = 0.9307*** (+2.01% over DCN baseline **0.9124**).
    * UniShare **GAUC = 0.9282*** (+1.55% over DCN **0.9140**).
    * UniShare **Recall@5 = 0.8532*** (+1.23% over DCN **0.8428**).
    * UniShare **NDCG@5 = 0.9093*** (vs. DCN **0.9046**), **MRR = 0.8568*** (+1.32% over DCN **0.8456**).
  * **Ablation Results (Table 3):**
    * `w/o all`: Video AUC drops to **0.7526** (-0.82%), Receiver AUC drops to **0.9213** (-1.01%).
    * `w/o RCA`: Video AUC drops to **0.7566** (-0.29%), Receiver AUC drops to **0.9282** (-0.27%).
    * `w/o BIM`: Video AUC drops to **0.7558** (-0.40%), Receiver AUC drops to **0.9273** (-0.37%).
    * `w/o HNS`: Receiver AUC drops to **0.9238** (-0.74%), showing specialized importance for receiver ranking.
  * *Offline Receiver Satisfaction:* **+3.46%** average increase in matching score between receiver interest embeddings and top 10 recommended shared videos [20].
* **Live Production Online A/B Test Results on Kuaishou (7-day test, Table 4):**
  * **Number of shares:** **+1.95%**
  * **Number of unique sharing users:** **+0.805%**
  * **CTR of the share button:** **+1.12%**
  * **CTR of share icon on panel:** **+1.14%**
  * **Reply rate of receivers:** **+0.482%** [52–53].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Escalating Joint Scoring Complexity:** Scoring every candidate receiver for every candidate video expands per-request complexity to \\(O(|I| \times |\mathcal{V}_u|)\\) (vs. decoupled \\(O(|I|)\\) for browsing and \\(O(|\mathcal{V}_u|)\\) for panel clicks), requiring online candidate set truncation (\\(\hat{\mathcal{V}}_u \le 8\\)) to avoid high serving latency [48–51, 55].
2. **ID Feature Sparsity in Long-Tail Entities:** Pure ID-based representations fail on rare or long-tail users and videos, necessitating external pre-trained multi-modal and GNN embeddings [23–24].
3. **Sensitivity to Receiver Retrieval Coverage:** If the candidate receiver retrieval set is empty (\\(\mathcal{V}_u = \emptyset\\)), the estimated video share probability \\(f_1(i; u, \mathcal{V}_u)\\) drops to near zero, causing multi-task rankers to suppress sharing objectives [17].
4. **Dependency on Offline LLM Inference:** Relationship-content alignment relies on offline Qwen-VL LLM inference over ASR text and cover images, which covers ~80% of \\(\langle u, v \rangle\\) pairs [37, 66–69].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Ma et al. (2018) [Ref 12 / ESMM]:** *Entire Space Multi-Task Model: An Effective Approach for Estimating Post-Click Conversion Rate* (ACM SIGIR '18).
2. **Ma et al. (2018) [Ref 11 / MMoE]:** *Modeling Task Relationships in Multi-task Learning with Multi-gate Mixture-of-Experts* (ACM SIGKDD '18).
3. **Tang et al. (2020) [Ref 15 / PLE]:** *Progressive Layered Extraction (PLE): A Novel Multi-Task Learning (MTL) Model for Personalized Recommendations* (ACM RecSys '20).
4. **Wang et al. (2021) [Ref 17 / DCN V2]:** *DCN V2: Improved Deep & Cross Network and Practical Lessons for Web-scale Learning to Rank Systems* (ACM WWW '21).
5. **Ji et al. (2021) [Ref 5 / HGSRec]:** *Who You Would Like to Share With? A Study of Share Recommendation in Social E-commerce* (AAAI '21).
6. **Zhao et al. (2025) [Ref 24 / Joint Modeling Survey]:** *Joint Modeling in Recommendations: A Survey*.
7. **Zhao et al. (2023) [Ref 25 / DynShare]:** *Time-interval Aware Share Recommendation via Bi-directional Continuous Time Dynamic Graphs* (ACM SIGIR '23).

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

### **Evaluation of *UniShare: A Unified Framework for Joint Video and Receiver Recommendation in Social Sharing***  
*(Wang et al., Kuaishou Technology, arXiv:2602.09618 / ACM '25)* [1]

---

### **(A) Q1 or Q2 or Both or Neither?**

**Neither.** [1]  
* **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** While published in February 2026 (`arXiv:2602.09618`) and deployed in live production at Kuaishou, UniShare is a **joint recommendation ranking framework** for short-video social sharing (predicting video sharing probability and candidate receiver choice simultaneously), rather than a multi-touch attribution (MTA) measurement system [1, 15–18].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** UniShare optimizes immediate sharing intent and receiver engagement (predicting sharing probabilities \\(S \in \{0, 1\}\\) for candidate videos and receivers), rather than attributing user retention, active days, or revisitation back to individual past interaction touchpoints across historical logs [15–18].

---

### **(B) Q2 Class**

**NOT.** [1, 15–18]  
* **Justification:** UniShare is a multi-task joint recommendation architecture (Bilateral Interest Modeling + Relationship-Content Alignment + Hierarchical Negative Sampling). It does **not** produce or publish a per-exposure retention credit table [1, 8, 18–25].

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction sequence attribution credit table.** [1, 2]
* **Target Outcome:** Predicts binary social sharing interaction probabilities [15–18]:
  1. *Video Share Probability (Sub-task 1):* \\(f_1(i; u, \mathcal{V}_u) = \sum_{v \in \mathcal{V}_u} P(S=1 \mid u, i, v)\\) [17–18].
  2. *Receiver Recommendation Probability (Sub-task 2):* \\(f_2(v; u, i) = P(S=1 \mid u, i, v)\\) for candidate receiver \\(v \in \mathcal{V}_u\\) [2].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**

* **How it Improves/Informs Ranking Strategy:** UniShare does **not** provide a post-hoc attribution model to replace last-touch N7 [1, 2]. However, it offers a **joint ternary recommendation paradigm** for platforms driven by two-sided or peer-to-peer social choices [1, 3, 4]:
  1. *Ternary Interaction Modeling (\\(\langle U, I, V \rangle\\)):* In a dating app, matching and messaging can be modeled as a joint ternary interaction among the active user (\\(U\\)), candidate profile (\\(I\\)), and engagement/chat prompt (\\(V\\)), replacing decoupled single-side rankers [12, 15–18].
  2. *Bilateral Interest Modeling (BIM):* Employs target attention over historical behavior sequences to dynamically evaluate whether a profile card aligns with **both** parties' mutual preferences simultaneously [19–22].
  3. *Relationship-Content Alignment (RCA):* Combines pre-trained social Graph Neural Network (GNN) follow-graph embeddings with LLM-based relationship classification (e.g., Qwen-VL categorizing interaction types into "buddies", "peers", "romantic partners") to ensure recommended candidates align with relational intent [24–25, 37, 66–68].
  4. *Hierarchical Negative Sampling (HNS):* Separates hard negative candidates (past interacted users) from easy negatives (random social connections) during candidate generation [5].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Mitigates Data Sparsity & Cold-Start Bias:** Integrates pre-trained multi-modal video/user interest embeddings (\\(\mathbf{e}_{\text{mm}}\\)) and social graph GNN embeddings (\\(\mathbf{e}_{\text{gnn}}\\)) to prevent representation collapse on sparse or long-tail entities [23–25].
2. **Hierarchical Negative Sampling (HNS):** Combines hard negatives (users who previously received shares from \\(u\\)) and easy negatives (random social connections) to mimic real-world interface constraints (up to 20 candidates per panel) [5-7].
3. **Online Candidate Truncation for Scalability:** Resolves the \\(O(|I| \times |\mathcal{V}_u|)\\) joint scoring complexity during feed browsing by truncating the online candidate set \\(\mathcal{V}_u\\) to the top 8 recently shared-with users (\\(\hat{\mathcal{V}}_u \le 8\\)) and blending scores during final re-ranking [48–51].

---

### **(F) Deployed or Production Dataset Evidence**

* **Production Deployment:** Fully deployed live in production on the **Kuaishou** short-video platform [1, 7, 48–53].
* **Quoted Dataset & Experimental Metrics:**
  * **K-Share Benchmark Dataset (Table 2):** **19,395 users**, **3,790,673 videos**, **11,310,319 video views**, **752,887 shares**, **1,306,752 friends**, and **186,886 receivers** (~1M share instances, ~10M video view events) [8, 9].
  * **Offline Benchmark Results on K-Share (Table 3):**
    * *Video Recommendation Sub-task:* UniShare **AUC = 0.7588*** (+1.01% over PLE baseline 0.7512), **GAUC = 0.6976*** (+0.82%), **Recall@10 = 0.2913*** (+1.53%), **NDCG@10 = 0.3110**, **MRR = 0.3934*** [38–39, 43–44].
    * *Receiver Recommendation Sub-task:* UniShare **AUC = 0.9307*** (+2.01% over DCN baseline 0.9124), **GAUC = 0.9282*** (+1.55%), **Recall@5 = 0.8532*** (+1.23%), **NDCG@5 = 0.9093***, **MRR = 0.8568*** [40, 43–44].
    * *Offline Receiver Satisfaction:* **+3.46%** average increase in matching score between receiver interest embeddings and top 10 recommended videos [10].
  * **Ablation Study AUC Drops (Table 3):**
    * `w/o all` (removes all enhanced representations): Video AUC drops to **0.7526** (-0.82%), Receiver AUC drops to **0.9213** (-1.01%) [11, 12].
    * `w/o RCA`: Video AUC drops to **0.7566** (-0.29%), Receiver AUC drops to **0.9282** (-0.27%) [11, 12].
    * `w/o BIM`: Video AUC drops to **0.7558** (-0.40%), Receiver AUC drops to **0.9273** (-0.37%) [11, 12].
    * `w/o HNS`: Receiver AUC drops to **0.9238** (-0.74%) [11, 12].
  * **Live Production Online A/B Test Results on Kuaishou (7-day test, Table 4):**
    * **Number of shares:** **+1.95%** [1, 7, 52–53].
    * **Number of unique sharing users:** **+0.805%** [52–53].
    * **CTR of the share button:** **+1.12%** [52–53].
    * **CTR of share icon on panel:** **+1.14%** [52–53].
    * **Receiver reply rate:** **+0.482%** [1, 7, 52–53].

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
**Priority:** see queue.md `G31`
