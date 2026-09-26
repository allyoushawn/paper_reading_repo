# Towards Reliable Social A/B Testing: Spillover-Contained Clustering with Robust Post-Experiment Analysis [1]

**Source:** https://arxiv.org/pdf/2602.08569.pdf  
**Date analyzed:** 2026-09-24  
**NLM source id:** `65d84922-448a-4dd1-950f-148e5c690bc9`  
**Queue id:** G34  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Towards Reliable Social A/B Testing: Spillover-Contained Clustering with Robust Post-Experiment Analysis* [1]
* **Authors:** **Xu Min**, **Zhaoxu Yang**, **Kaixuan Tan**, **Juan Yan**, **Xunbin Xiong**, **Zihao Zhu**, **Kaiyu Zhu**, **Fenglin Cui**, **Yang Yang**, **Sihua Yang**, and **Jianhui Bu** [1]
* **Affiliation:** **Kuaishou Technology**, Beijing, China [1]
* **Year:** **2026** (arXiv pre-print: `arXiv:2602.08569`, February 2026)
* **Venue:** arXiv pre-print (`arXiv:2602.08569v1 [cs.SI]`) [1]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Online social platforms suffer from severe **network interference (spillover effects)** where user interactions (sharing, messaging) violate the Stable Unit Treatment Value Assumption (SUTVA) by spilling treatment effects into control groups [1, 3–4]. Standard user-level randomization severely underestimates treatment effects, while conventional graph clustering algorithms produce unbalanced cluster sizes and high estimator variance in A/B testing [1-3].
* **Key Contributions:**
  1. **Two-Stage Social A/B Testing Framework:** Integrates pre-experiment spillover containment with post-experiment variance reduction [1, 4, 5].
  2. **Balanced Louvain Clustering Algorithm:** Modifies modularity optimization with a soft piecewise size penalty and a hard connectivity-based post-processing split to produce stable, size-balanced, spillover-contained clusters for Cluster-Based Randomization (CBR) [1, 19, 21–25].
  3. **Cluster-Tolerant CUPAC Variance Reduction Pipeline:** Implements a bucket-based estimation framework using Delta-method linearization and cross-fitted machine learning predictions to reduce variance and recover statistical power under cluster-level assignment [15, 30–33, 38–41].
  4. **Billion-Scale Industrial Deployment:** Validated on Kuaishou serving hundreds of millions of users, proving that spillover-contained CBR uncovers true 7-day retention (LT-7) lifts that remain masked under standard user-level designs [1, 46–48, 52–54].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Architectural Stages**
1. **Heterogeneous Multi-Behavior Graph Construction:** Aggregates five social interaction types (sharing, messaging, comments, likes, follows) into a weighted interaction graph \\(W_{ij} = \sum_{d=1}^D \omega_d s_{ij}^{(d)}\\) [29–30].
2. **Balanced Louvain Algorithm:**
   * *Soft Constraint (Size Penalty):* Modifies the node-movement score by subtracting a size penalty: \\(S_{Ci} = \Delta Q_{Ci} - \alpha \cdot P(|C|)\\), where \\(P(|C|) = \frac{k(|C| - \tau)}{\tau}\\) for clusters exceeding threshold \\(\tau = \frac{N_{\max}}{2}\\) [21–22].
   * *Hard Constraint (Connectivity-Based Split):* Iteratively splits oversized clusters (\\(|C| > N_{\max}\\)) by computing node internal connectivity \\(\text{conn}_i = \sum_{j \in C, j \neq i} w_{ij}\\) and separating peripheral low-connectivity nodes into new clusters to preserve the core community structure [23–25].
3. **Bucket-Based Randomization & Inference:** Hashes clusters into buckets assigned to treatment or control to preserve independence and account for intra-cluster correlation [31–32]. Uses first-order Delta-method transformations to construct bucket-level pseudo-outcomes \\(Z_b\\) for ratio metrics [33–34].
4. **Cross-Fitted CUPAC Adjustment:** Trains predictive ML models \\(f^{(k)}\\) exclusively on control buckets using \\(K\\)-fold cross-fitting (\\(Z_b^{\text{CUPAC}} = Z_b - \theta (\hat{Z}_b - \mathbb{E}[\hat{Z}])\\)) to prevent overfitting and Type I error inflation [38–41].

#### **Credit Assignment Mechanics**
* **Does NOT assign per-touchpoint, per-item, or per-interaction credit.**
* It is an **experimentation design and statistical evaluation framework** for measuring cluster-level Average Treatment Effects (ATE) of social sharing features on aggregate business metrics (e.g., Share Count, 7-Day Retention), rather than a multi-touch attribution (MTA) model.

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets & Scale:**
  * *Kuaishou Platform Graph:* 370 million monthly active users partitioned into **73,340 clusters** (largest cluster: 249,319 users; average cluster size: 5,045) [6].
  * *City-Level Subgraph (\\(G_{\text{city}}\\)):* 550,000 users for clustering ablation studies [7].
  * *Synthetic Networks:* 900 simulated experiments on Watts-Strogatz small-world networks (\\(n=10,000\\), degree \\(d \in \{4, 10, 20\}\\)) [44–45, 79–81].
* **Production Deployment:** Fully deployed in live online A/B testing on a 2% traffic sample on Kuaishou's production platform [46–47, 51].
* **Comparison Baselines:**
  * *Randomization Schemes:* User-Based Randomization (UBR) vs. Cluster-Based Randomization (CBR) [47–49].
  * *Graph Clustering Baselines:* Constrained Label Propagation Algorithm (LPA), Standard Louvain (\\(\gamma = 1, 2\\)), Hard-only splitting, Soft-only penalty [53–56].
  * *Variance Reduction Baselines:* Difference-in-Means (DIM), CUPED [57–59].

---

### **(5) Key Quantitative Results with Numbers**
* **Online A/B Test Results on Kuaishou (Table 1):**
  * **Within-Group Share Ratio (WGSR - Spillover Containment):** CBR = **90.39%** vs. UBR = **49.68%** [8].
  * **Share Count (SC) Lift:** CBR = **+26.612%** (\\(p < 0.01\\)) vs. UBR = **+7.758%** (\\(p < 0.01\\)) [8].
  * **Share Penetration (SP) Lift:** CBR = **+14.774%** (\\(p < 0.01\\)) vs. UBR = **+4.968%** (\\(p < 0.01\\)) [8].
  * **Message Penetration (MP) Lift:** CBR = **+4.983%** (\\(p < 0.01\\)) vs. UBR = **+1.888%** (\\(p < 0.01\\)) [8].
  * **7-Day Retention (LT-7) Lift:** CBR detected a statistically significant positive lift of **+0.133%** (\\(p < 0.01\\)), whereas UBR was statistically weaker at **+0.049%** (\\(p < 0.05\\)). CBR revealed a **+0.088 percentage point higher retention gain** masked by network spillovers under UBR [49, 52–54].
* **Simulation Spillover Bias Reduction (Figure 3 & Table 4):**
  * Cluster-based assignment (WGSR \\(\approx 0.95\\)) reduced estimation bias by **87–89%** compared to user-level randomization (WGSR \\(\approx 0.50\\)) [9].
  * Extrapolation to WGSR = 1.0 recovered true ATE within **0.1%** [9].
* **Variance Reduction with CUPAC (Table 3 & Table 8):**
  * CUPAC achieved **92.45%** (Kuaishou LT-7) and **93.77%** (Bi LT-7) variance reduction over DIM, outperforming CUPED by **+6.50pp** and **+4.66pp** respectively [10].
  * CUPAC detected statistically significant LT-7 retention gains as early as **Day 28** (vs. statistically insignificant results for DIM at day 28) [58–59].
  * \\(K\\)-fold cross-fitting reduced Type I error inflation from **8.54%** to **5.08%** [11].
* **Engineering Scalability:** Redis star-topology architecture and stable cluster freezing reduced end-to-end distributed clustering computation time on a billion-edge graph from **72 hours to 6 hours** [82–84].

---

### **(6) Limitations, Failure Modes, or Negative Results**
1. **Underestimation of Downstream Lifts under User-Level Randomization (UBR):** Uncontained network spillovers cause control users to be exposed to social features via treatment interactions, biasing ATE estimates downward and masking long-term retention benefits (LT-7 lift appeared negligible under UBR) [46, 52–54].
2. **Uncontrollable Cluster Sizes in Standard Louvain:** Standard Louvain modularity optimization creates massive communities (largest cluster > 109,000 nodes; variance 1.84M), causing severe traffic assignment imbalance and variance inflation [19, 53–56].
3. **Disruptive Splitting in Hard-Constraint-Only Variants:** Omitting the soft size penalty (\\(\alpha = 0\\)) forces aggressive post-processing splits on oversized clusters, leading to high cluster size variance (399K) [55–56].
4. **Type I Error Inflation without Cross-Fitting:** Applying predictive CUPAC modeling without cross-fitting led to overfitting and an elevated Type I error rate of **8.54%** [11].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Deng et al. (2013) [Ref 7]:** *Improving the sensitivity of online controlled experiments by utilizing pre-experiment data* (Introduced CUPED) [12].
2. **Eckles, Karrer, & Ugander (2017) [Ref 9]:** *Design and analysis of experiments in networks: Reducing bias from interference* [13].
3. **Blondel et al. (2008) [Ref 3]:** *Fast unfolding of communities in large networks* (Standard Louvain algorithm) [62–63].
4. **Tang et al. (2020) [Ref 32]:** *Control using predictions as covariates in switchback experiments* (CUPAC framework) [14].
5. **Aronow & Samii (2017) [Ref 1]:** *Estimating average causal effects under general interference, with application to a social network experiment* [15].
6. **Bojinov, Simchi-Levi, & Zhao (2023) [Ref 4]:** *Design and analysis of switchback experiments* [16].
7. **Ugander et al. (2013) / Ugander & Yin (2023) [Refs 35, 36]:** *Graph cluster randomization: Network exposure to multiple universes* & *Randomized graph cluster randomization* [17].

---

💡 *Would you like to explore how Kuaishou's cluster-based randomization (CBR) or CUPAC variance reduction could be applied to measure spillover-contained 7-day retention in your dating app's A/B experiments?*

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

### **Source Evaluation: *Towards Reliable Social A/B Testing: Spillover-Contained Clustering with Robust Post-Experiment Analysis***
*(Min et al., Kuaishou Technology, arXiv:2602.08569, February 2026)* [1]

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**

**Neither.** [1-4]
* **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** While published in February 2026 (`arXiv:2602.08569`) and deployed in live production at Kuaishou, it presents an **A/B testing and statistical inference framework** (Cluster-Based Randomization with Balanced Louvain + CUPAC variance reduction) for measuring social feature treatment effects under network interference, rather than a multi-touch attribution (MTA) measurement system [1, 3, 5].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper measures group-level / cluster-level Average Treatment Effects (ATE) on 7-day retention (LT-7) and social sharing metrics in online experiments, rather than attributing retention or active days back to individual user interaction touchpoints (e.g., swipes or messages) across historical logs [33, 49–50].

---

### **(B) Q2 Class**

**NOT.** [16, 31–33]
* **Justification:** It is an experimentation design and statistical inference framework (Balanced Louvain cluster-based randomization with a bucket-level CUPAC estimator) [5-7]. It does **not** produce or publish a per-exposure or per-interaction retention credit table.

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction credit table.**
* **Target Outcome:** Measures cluster-level / group-level Average Treatment Effect (ATE) on core platform social metrics and medium-term user retention [49–50]:
  1. **7-Day Retention (LT-7):** 7-day retained active users divided by cohort size, measuring medium-term user stickiness [4].
  2. **Share Count (SC):** Total number of sharing events initiated during the observation period [4].
  3. **Share Penetration (SP):** Percentage of users performing at least one sharing action [4].
  4. **Message Penetration (MP):** Proportion of users performing at least one messaging action [4].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**

* **How it Improves on Last-Touch:** Last-touch post-hoc rules assign 100% of an N7 retention label to recent swipes, ignoring network interference and failing to isolate true causal lift. This paper is *not* a post-hoc attribution model; instead, it provides a **spillover-contained experimentation framework** to verify whether product strategy changes (e.g., recommendation algorithms, match panels, or chat prompts) causally drive 7-day retention (LT-7) without treatment effects leaking into control users via social interactions [1, 46–47, 52–54].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. **Heterogeneous Interaction Graph Construction:** Aggregates multi-behavior user interaction relationships (e.g., messaging, profile sharing, mutual matching, likes, follows) into a weighted interaction graph [29–30].
  2. **Spillover-Contained Cluster-Based Randomization (CBR):** Partitions connected users into balanced clusters using Balanced Louvain (\\(\alpha = 0.3, N_{\max} = 250\text{K}\\)) to prevent social feature treatments (e.g., new match re-ranking or conversation prompts) from spilling over to control users [8-10].
  3. **Delta-Method Linearization & CUPAC Inference:** Uses bucket-level Delta-method linearization and cross-fitted CUPAC variance reduction to measure unconfounded 7-day retention (LT-7) gains caused by new features [33–34, 38–41].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Within-Group Share Ratio (WGSR) / Network Spillover Containment:** Controls for SUTVA violations and network interference bias by partitioning the social interaction graph into clusters via Balanced Louvain (combining a soft size penalty \\(\alpha \cdot P(|C|)\\) and a hard connectivity-based split), containing **90.39%** of sharing interactions within treatment arms (vs. **49.68%** under user-level randomization) [21, 23–24, 49].
2. **Bucket-Level Linearization & Delta-Method:** Resolves intra-cluster correlation and ratio metric estimation bias by computing bucket-level pseudo-outcomes \\(Z_b\\) using first-order Delta-method linearization [31–34].
3. **\\(K\\)-Fold Cross-Fitted CUPAC Adjustment:** Mitigates overfitting and Type I error inflation when utilizing pre-experiment behavioral covariates by training predictive models \\(f^{(k)}\\) exclusively on control buckets using \\(K\\)-fold cross-fitting (reducing Type I error rate from **8.54% to 5.08%**) [11].

---

### **(F) Deployment and Production Dataset Evidence**

* **Production Deployment:** Fully deployed live on **Kuaishou's production platform** for online A/B testing on a **2% traffic sample** of users [10, 12].
* **Quoted Numbers from the Source:**
  * **Graph & Cluster Scale:** Built an ultra-large weighted social graph of monthly active users partitioned into **73,340 distinct clusters** (largest cluster = **249,319 users**; average cluster size = **5,045**; overall modularity = **0.466**); **44.7%** of all sharing events occurred within clusters [10].
  * **Live Online A/B Test Results (CBR vs. User-Based Randomization UBR, Table 1):**
    * **WGSR (Spillover Containment):** **90.39%** for CBR vs. **49.68%** for UBR [13].
    * **Share Count (SC) Lift:** **+26.612%** (\\(p < 0.01\\)) for CBR vs. **+7.758%** (\\(p < 0.01\\)) for UBR [13].
    * **Share Penetration (SP) Lift:** **+14.774%** (\\(p < 0.01\\)) for CBR vs. **+4.968%** (\\(p < 0.01\\)) for UBR [13].
    * **Message Penetration (MP) Lift:** **+4.983%** (\\(p < 0.01\\)) for CBR vs. **+1.888%** (\\(p < 0.01\\)) for UBR [13].
    * **7-Day Retention (LT-7) Lift:** **+0.133%** (\\(p < 0.01\\)) for CBR vs. **+0.049%** (\\(p < 0.05\\)) for UBR. CBR revealed a **+0.088 percentage point** higher retention gain that was masked under UBR due to uncontained network spillovers [13, 14].
  * **Simulation Bias Reduction:** Cluster-based assignment (\\(\text{WGSR} \approx 0.95\\)) reduced estimation bias by **87–89%** compared to user-level randomization (\\(\text{WGSR} \approx 0.50\\)) [15]. Extrapolation to \\(\text{WGSR}=1.0\\) recovered true ATE within **0.1%** [15].
  * **CUPAC Variance Reduction (Table 3 & Table 8):** Achieved **92.45%** variance reduction for Kuaishou LT-7 and **93.77%** for Bi LT-7 over Difference-in-Means (DIM), outperforming CUPED by **+6.50pp** and **+4.66pp** respectively [16]. CUPAC detected statistically significant LT-7 gains as early as **Day 28** (\\(p = 0.048\\)) [17].
  * **Type I Error Rate:** \\(K\\)-fold cross-fitting reduced Type I error inflation from **8.54% to 5.08%** [11].
  * **Distributed Engineering Scalability:** Redis star-topology architecture reduced end-to-end clustering computation time on a billion-edge graph from **72 hours to 6 hours** [18].

---

💡 *Would you like to explore how Kuaishou's cluster-based randomization (CBR) or CUPAC variance reduction could be applied to measure spillover-contained 7-day retention in your dating app's A/B experiments?*

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
**Priority:** see queue.md `G34`
