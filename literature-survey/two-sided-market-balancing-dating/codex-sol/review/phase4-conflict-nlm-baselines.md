# Phase 4 Conflict Follow-up — Direct Baselines

**Query:** Conflict resolution using only these seven sources: identify every case where DPGNN, transferable-utility reciprocal ranking, or RECON is used as a direct experimental comparison baseline by another included source. Distinguish table/experiment baselines from related-work citations, and name the using paper and the baseline method. Do not infer; write Not specified where absent.

## Response

Based on a rigorous review of the seven selected sources, there are exactly **four cases** where **DPGNN**, **transferable-utility reciprocal ranking (TU)**, or **RECON** is implemented as an active experimental baseline in a table or evaluation graph by another paper in this collection. 

To ensure precision, related-work citations have been explicitly separated from direct experimental comparator implementations:

---

### **1. RECON as an Experimental Baseline**
*   **Using Paper:** *“Reciprocal Recommendation System for Online Dating”* (Peng Xia, Benyuan Liu, Yizhou Sun, and Cindy Chen, 2015) [1]
*   **Baseline Method:** **RECON** (evaluated under the designation **`CB1`** or **`CB1(RECON)`**) [2-4].
*   **Experimental Role:** In Section 2, the authors cite RECON as related work [2]. However, in Section 5, they go beyond conceptual citation and directly code and run RECON as their content-based baseline to benchmark their proposed algorithms [3, 5, 6]. Figures 8, 9, 12, and 13 plot RECON (`CB1`) head-to-head against their proposed `CB2` and collaborative filtering methods across **I-Precision**, **I-Recall**, **R-Precision**, and **R-Recall** metrics [6-10].

---

### **2. DPGNN as an Experimental Baseline**
*   **Using Paper:** *“Reciprocal Sequential Recommendation”* (Bowen Zheng, Yupeng Hou, Wayne Xin Zhao, Yang Song, and Hengshu Zhu, 2023) [11]
*   **Baseline Method:** **DPGNN** [12].
*   **Experimental Role:** While DPGNN is cited conceptually under related work [13], it is explicitly integrated as a core competitive baseline representing state-of-the-art static reciprocal models [12, 14]. In **Table 2**, DPGNN's performance is compared directly against the paper's proposed sequential model (*ReSeq*) on three distinct real-world recruitment datasets (Design, Sale, and Technology) using **HR@5**, **MRR@5**, and **NDCG@5** metrics [15].

---

### **3. DPGNN as an Experimental Baseline**
*   **Using Paper:** *“Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method”* (Chen Yang, Sunhao Dai, Yupeng Hou, Wayne Xin Zhao, Jun Xu, Yang Song, and Hengshu Zhu, 2024) [16, 17]
*   **Baseline Method:** **DPGNN** [18].
*   **Experimental Role:** In **Table 3**, the authors utilize DPGNN as a direct graph-based reciprocal baseline on both the Recruitment and Dating datasets [19-21]. DPGNN is compared head-to-head with their proposed causal framework (*CRRS*) across all traditional and newly proposed metrics (including **Recall@50**, **Precision@50**, **NDCG@50**, **SRecall@50**, **SPrecision@50**, **RNDCG@50**, **CRecall@50**, **CPrecision@50**, and **True Positive Pairs**) [20, 21].

---

### **4. Transferable-Utility Reciprocal Ranking (TU) as an Experimental Baseline**
*   **Using Paper:** *“Fair Reciprocal Recommendation in Matching Markets”* (Yoji Tomita and Tomohiko Yokoyama, 2024) [22]
*   **Baseline Method:** **TU** (representing the deterministic, transferable-utility stable matching model proposed by Tomita et al., 2023) [23, 24].
*   **Experimental Role:** In **Figures 1 and 2**, the authors use the TU matching model as a direct comparison baseline in their simulation sweeps [24, 25]. They evaluate its expected number of matches and its ability to reduce envy against their proposed alternate Nash social welfare (NSW) maximization algorithm on both synthetic and real-world Japanese online dating platform data [24-28].

---

### **Other Mentions (Not Used as Experimental Baselines):**
*   *Modeling Two-Way Selection Preference for Person-Job Fit* (Chen Yang et al., 2022) cites RECON in its related work section [29], but does not utilize it as a benchmark in its experimental evaluation section [30, 31].
*   *Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets* (Yoji Tomita et al., 2023) originally designs the **TU** approach as its proposed method [32, 33], citing RECON under related work [34] without running RECON in its experimental setups [35, 36]. 
*   *Revisiting Reciprocal Recommender Systems* (Chen Yang et al., 2024) cites RECON under related work [37] but restricts its experimental comparison in Table 3 to DPGNN [18, 20, 21].

