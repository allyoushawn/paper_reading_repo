# Phase 4 NotebookLM Query 2 — Datasets and Benchmarks

**Query:** What are the most common evaluation datasets and benchmarks used across these papers? Map each dataset or benchmark to the papers that use it. Use full source names. Do not infer beyond the sources; if evidence is absent, write Not specified.

## Response

### **1. MovieLens Datasets (MovieLens-100K and MovieLens-1M / ML-1M)**
*   **Description:** Publicly available benchmarks containing movie ratings, user genres, and demographic attributes (such as gender, age, and occupation) used to evaluate collaborative filtering, multi-sided exposure fairness, and user-bias mitigations [1, 2].
*   **Mapped Papers:**
    *   `"Joint Multisided Exposure Fairness for Recommendation - Microsoft"` [1]
    *   `"https://arindam.cs.illinois.edu/papers/17/rec-capacity-cikm17.pdf"` [2]
    *   `"RecSys 2025 - Accepted Contributions"` (utilized across multiple accepted works, including: *"Mitigating Latent User Biases in Pre-trained VAE Recommendation Models via On-demand Input Space Transformation"* [3], *"See the Movie, Hear the Song, Read the Book: Extending MovieLens-1M..."* [4], *"In-context Learning for Addressing User Cold-start in Sequential Movie Recommenders"* [5], and *"R⁴ec: A Reasoning, Reflection, and Refinement Framework for Recommendation Systems"* [6]).

---

### **2. Japanese Online Dating Platform Dataset (Proprietary / Tapple)**
*   **Description:** A massive, proprietary transaction dataset recording active swiping behaviors ("Like"/"Nope") and reciprocal match decisions ("Thanks"/"Sorry") from millions of opposite-sex profiles [7, 8].
*   **Mapped Papers:**
    *   `"Balancing Fairness and High Match Rates in Reciprocal Recommender Systems: A Nash Social Welfare Approach - arXiv"` [7, 9]
    *   `"MODE: Mutual Optimality in Direct Effects of Reciprocal Recommendations in Matching Markets - arXiv"` (represented as `"https://arxiv.org/pdf/2608.01731.pdf"`) [8, 10]

---

### **3. BOSS Zhipin Online Recruitment Dataset**
*   **Description:** Large-scale logs recording sequential candidate-recruiter interactions (impressions, clicks, applications, and recruiter-side accept/reject reviews) on a major Chinese online recruitment platform [11, 12].
*   **Mapped Papers:**
    *   `"Interview choice reveals your preference on the market: To improve job-resume matching through profiling memories - KAUST Repository"` [11]
    *   `"https://dl.acm.org/doi/pdf/10.1145/3580305.3599783"` [12]

---

### **4. DBLP Co-Authorship Graph (DBLP-CoAuthor)**
*   **Description:** A co-authorship database mapped into a reciprocal matching setting, where authors are modeled as nodes and mutual co-authorships are treated as successful bidirectional connections [13, 14].
*   **Mapped Papers:**
    *   `"Counterfactual Reciprocal Recommender Systems for User-to-User Matching - arXiv"` [13]
    *   `"https://arxiv.org/pdf/2508.01867.pdf"` [14]

---

### **5. Epinions Trust Network (Epinions-Trust)**
*   **Description:** A user-to-user trust network where a reciprocal match is defined as a pair of users who have mutually declared trust in one another [13, 14].
*   **Mapped Papers:**
    *   `"Counterfactual Reciprocal Recommender Systems for User-to-User Matching - arXiv"` [13]
    *   `"https://arxiv.org/pdf/2508.01867.pdf"` [14]

---

### **6. Wantedly Visit Logs**
*   **Description:** Real-world behavioral logs and live A/B testing logs detailing job seeker applications and company-side scouting or recruiting decisions [15].
*   **Mapped Papers:**
    *   `"https://arxiv.org/pdf/2507.13608.pdf"` [15, 16]
    *   `"RecSys 2025 - Accepted Contributions"` (specifically the paper: *"Off-Policy Evaluation and Learning for Matching Markets"* [17])

---

### **7. Chinese Recruitment Platform logs (Tech, Sales, and Design Segments)**
*   **Description:** Multi-industry transactional logs capturing resumes, job descriptions, and user dynamic interactions divided into tech, sales, and design datasets to evaluate sparse person-job matches [18-20].
*   **Mapped Papers:**
    *   `"https://arxiv.org/pdf/2208.08612.pdf"` [18, 19]
    *   `"https://arxiv.org/pdf/2306.14712.pdf"` [20]

---

### **8. Stack Exchange Q&A Networks (StackOverflow and AskUbuntu)**
*   **Description:** Datasets tracking chronological user question-and-answering logs to predict mutual, sequential matches between question creators and expert answerers [20, 21].
*   **Mapped Papers:**
    *   `"https://arxiv.org/pdf/2306.14712.pdf"` [20, 21]

---

### **9. Libimseti Dating Network Dataset**
*   **Description:** A public, opposite-sex dating platform rating dataset where mutual ratings of 8 or above are modeled as a successful reciprocal match [22, 23].
*   **Mapped Papers:**
    *   `"https://arxiv.org/pdf/2408.09748.pdf"` [22-24]

---

### **10. Kaggle Speed Dating Dataset**
*   **Description:** A public database containing participant attributes, survey logs, and speed dating reciprocal selection outcomes [7, 25, 26].
*   **Mapped Papers:**
    *   `"Balancing Fairness and High Match Rates in Reciprocal Recommender Systems: A Nash Social Welfare Approach - arXiv"` [7, 25]
    *   `"https://www.ujaen.es/grupos-de-investigacion/asia/sites/investigacion_asia/files/uploads/node_evento/revistas_indexadas/1-s2.0-S1566253520304267-mainext.pdf"` [26, 27]

---

### **11. Gowalla and Foursquare POI Check-In Datasets**
*   **Description:** Public check-in records containing geographical and temporal coordinates, adapted to evaluate capacity-constrained location recommendation [2].
*   **Mapped Papers:**
    *   `"https://arindam.cs.illinois.edu/papers/17/rec-capacity-cikm17.pdf"` [2]
    *   `"RecSys 2025 - Accepted Contributions"` (specifically the paper: *"Exploring the Effect of Context-Awareness and Popularity Calibration on Popularity Bias in POI Recommendations"* [28])

---

### **12. NYC Taxi and Limousine Commission (NYC TLC) Trip Records**
*   **Description:** Millions of public origin-destination ride logs utilized to simulate spatial and temporal constraints under marketplace interference [29].
*   **Mapped Papers:**
    *   `"Reducing Marketplace Interference Bias Via Shadow Prices - arXiv"` (also represented as `"Reducing Marketplace Interference Bias Via Shadow Prices"`) [29]

---

### **13. Upwork Marketplace Contracts**
*   **Description:** A text-rich temporal graph mapping freelancer profiles, job postings, and established contracts on the Upwork freelancing marketplace [30, 31].
*   **Mapped Papers:**
    *   `"https://arxiv.org/pdf/2512.02849.pdf"` [30, 31]

---

### **14. Azar Video Chat Logs**
*   **Description:** User session records detailing real-time video matching and conversational duration matrices [32, 33].
*   **Mapped Papers:**
    *   `"https://arxiv.org/pdf/2410.18087.pdf"` [32, 34]
    *   `"https://minchankim.me/assets/pdf/cupid_paper.pdf"` [33, 35]

---

### **15. Last.fm (Lastfm-2k) Dataset**
*   **Description:** A public dataset logging user-to-artist implicit listening events, user tags, and social connections [4, 36].
*   **Mapped Papers:**
    *   `"https://arxiv.org/pdf/2110.15781.pdf"` [36]
    *   `"RecSys 2025 - Accepted Contributions"` (specifically the paper *"See the Movie, Hear the Song, Read the Book: Extending MovieLens-1M..."* [4])

---

### **16. CareerBuilder 2012 and Zhilian Datasets**
*   **Description:** Public online recruitment datasets mapping candidate resumes to job postings, released during historical recommender system challenges [37, 38].
*   **Mapped Papers:**
    *   `"A challenge-based survey of e-recruitment recommendation systems"` (represented as `"https://arxiv.org/pdf/2209.05112.pdf"`) [37, 38]

---

### **17. Houston Online Dating Platform Dataset**
*   **Description:** A heterosexual matchmaking dataset logging observable profile attributes and two-directional interactions from users based in Houston, TX [39, 40].
*   **Mapped Papers:**
    *   `"https://arxiv.org/pdf/2308.02584.pdf"` [41]
    *   `"https://iriosu.github.io/assets/pdf/dating_alf.pdf"` [39]

***

🎨 I can write a Python script in your sandbox using `matplotlib` to simulate a simplified bipartite matching market under varying capacities, plotting the Gini coefficient of exposure to show how different matching algorithms compare. Let me know if you would like to run this!

