# Phase 4 NotebookLM Query 5 — Methods Used as Baselines

**Query:** Is any paper's method used as a direct experimental baseline by other papers in this notebook? Map method name to the full titles of papers that use it as a baseline. Distinguish direct comparator use from related-work citation or conceptual influence. Do not infer beyond the sources; if evidence is absent, write Not specified.

## Response

Yes, the method from one of the papers in this notebook is utilized as a direct, head-to-head experimental baseline by other papers present in the notebook. 

Specifically, **DPGNN** (Dual-Perspective Graph Representation Learning for Person-Job Fit), which is proposed in the paper **"Modeling Two-Way Selection Preference for Person-Job Fit"** [1-3], serves as a major baseline.

The mapping of this method to the papers that use it as a direct experimental comparator is detailed below:

---

### **1. Mapping of DPGNN to Papers Using It as a Baseline**

#### **Paper A: "Reciprocal Sequential Recommendation"**
*   **Role of DPGNN:** **Direct Comparator Baseline** [4, 5].
*   **Relationship & Evaluation:** In this paper, the authors propose a sequential recommendation method named *ReSeq*. They evaluate *ReSeq* on three online recruitment datasets (Design, Sale, and Technology) and explicitly include **DPGNN** as a state-of-the-art reciprocal baseline under the "person-job fit" category [4]. 
*   **Evidence:** In Table 2 of the paper, DPGNN's performance is compared directly against the proposed ReSeq model using metrics such as HR@5, MRR@5, and NDCG@5 [5].

#### **Paper B: "Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method"**
*   **Role of DPGNN:** **Direct Comparator Baseline** [3, 6].
*   **Relationship & Evaluation:** The authors of this work use **DPGNN** as a representative graph-based reciprocal recommendation baseline [3]. They test it alongside their proposed *CRRS* (Causal Reciprocal Recommender System) on two large real-world datasets (Recruitment and Dating) [3, 7, 8]. 
*   **Evidence:** In Table 3, DPGNN is evaluated head-to-head against CRRS across various metrics (including Recall@50, Precision@50, NDCG@50, and SRecall@50) to demonstrate the proposed method's effectiveness [6].

---

### **2. Distinction: Direct Comparator vs. Related-Work Citation**
While many other classic algorithms in these papers (such as **BPRMF**, **LightGCN**, and **LFRR**) are used as baselines, they represent standard library models or external works whose papers are not physically present in this notebook. 

In contrast, the connection with **DPGNN** represents a complete cross-paper lifecycle within this specific notebook:
*   The **origin paper** (*"Modeling Two-Way Selection Preference for Person-Job Fit"*) is fully present [1].
*   The **subsequent papers** (*"Reciprocal Sequential Recommendation"* and *"Revisiting Reciprocal Recommender Systems"*) do not merely cite DPGNN as related work; they actively train, tune, and evaluate the DPGNN model on their own datasets to serve as a direct benchmark [3-6].

***

📊 Since these papers focus heavily on optimizing reciprocal matching, I can write a Python script in your scratch space to simulate a basic bipartite matching market using simulated collaborative filtering and graph-based scores. This will let you visualize how different recommendation strategies alter the Gini index of user exposure. Let me know if you would like to run this!

