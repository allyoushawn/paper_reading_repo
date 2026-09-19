# Card summaries 10/12 — Summary and Evidence sections of all cards (generated)

### Rethinking User Retention Modeling in Recommendation [1, 2]
`2026_TOIS_IURO+_Rethinking-User-Retention-Modeling.md`
**Source:** https://dl.acm.org/doi/pdf/10.1145/3790098  

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**

* **Title:** *Rethinking User Retention Modeling in Recommendation* [1, 2]
* **Authors:** **Rui Ding**\*¹, **Ruobing Xie**\*², **Xiaobo Hao**², **Xiaochun Yang**\*¹, **Kaikai Ge**², **Xu Zhang**², **Zhanhui Kang**², **Jie Zhou**², and **Leyu Lin**² (\*Corresponding authors) [1, 2]
* **Author Affiliations:**
  1. **Northeastern University**, School of Computer Science and Engineering, Shenyang, China (`ruiding.neu@outlook.com`, `yangxc@mail.neu.edu.cn`) [1, 2]
  2. **Tencent**, Beijing, China (`{xrbsnow-ing, rolyhao, kavinge, xuonezhang, kegokang, withtomzhou, goshawklin}@tencent.com`) [1, 2]
* **Year & Venue:** Published in **March 2026** in *ACM Transactions on Information Systems (TOIS)*, Vol. 44, No. 3, Article 64 (35 pages) [2, 3]. DOI: `10.1145/3790098` [2].

---

### **(2) Core Problem and Key Contribution**

* **Core Problem:** Standard recommender systems optimize short-term metrics (clicks, impressions, dwell time) that fail to align with long-term user satisfaction and retention [1, 3, 4]. Existing retention models focus strictly on prediction accuracy without revealing the underlying rationale or discovering *why* users return, largely due to the absence of explicit supervised signals [1, 5]. Furthermore, retention modeling suffers from weak causality, high behavioral randomness, and an inevitable \\(X\\)-day temporal delay between offline training and online deployment [1, 6, 7].
* **Key Contributions:**
  1. **Empirical Discovery of Implicit Supervised Signals:** Conducts large-scale empirical analyses on real-world user logs to uncover implicit retention signals: duration on impression (\\(doi\\), filtering out cursory scrolling \\(\le 0.1\text{s}\\)), attribute-level brief-pause ratio (\\(bpr\\)), and duration on click (\\(doc\\), distinguishing quick switches from deliberate reading) [8-13].
  2. **IURO+ Framework:** Proposes **Interpretable User Retention-Oriented Optimization (IURO+)**, a lightweight, non-RL framework consisting of three core modules [1, 14, 15]:
     * **BCMIL (Behavior-wise Contrastive Multi-Instance Learning):** Jointly models clicked and impressed items to generate User-Item (UI) retention scores, applying contrastive margin loss to sharpen rare, high-impact "aha items" [1, 14-16].
     * **FSSE (Forward Supervised Signals Extractor):** Embeds implicit supervised signals (\\(doi\\), \\(bpr\\), \\(doc\\)) into a heterogeneous Graph Attention Network (GAT) over feature-part behaviors to enrich node representations [1, 10, 17-21].
     * **BSSS (Backward Supervised Signals Stabilizer):** Leverages label-part user behaviors across three levels (node alignment, subgraph preference refinement, global embedding stabilization) to retrospectively guide feature-part training and suppress randomness [1, 6, 15, 22-25].
  3. **Industrial Plug-and-Play Deployment:** Deploys IURO+ as a lightweight online plug-in at Tencent (WeChat Top Stories) across Main-Page and Red-Dot recommendations, delivering statistically significant retention gains without harming CTR or dwell time [1, 26-30].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Architectural Components**
* **BCMIL Module (UI Scorer & Contrastive Learning):**
  * Computes UI retention scores \\(s_{ui} = \text{FFN}_3([h_u; h_i])\\) using a 3-layer Feedforward Network [31].
  * Integrates clicked behaviors (\\(N_{u,ck}^f\\)) and impressed behaviors (\\(N_{u,im}^f\\)) separately via instance-level attention [32, 33]:
    \\[\hat{y}_u = w \sum_{i \in N_{u,ck}^f} \text{softmax}\left(\frac{h_u \cdot h_i}{\sqrt{d}}\right) s_{ui} + (1 - w) \sum_{i \in N_{u,im}^f} \text{softmax}\left(\frac{h_u \cdot h_i}{\sqrt{d}}\right) s_{ui}\\]
  * Applies contrastive margin loss \\(\mathcal{L}_{\text{CL}} = \max(0, |\hat{y}_u - \hat{y}_u^{\text{high}}| - |\hat{y}_u - \hat{y}_u^{\text{low}}| + m)\\) to widen the score gap between high-attention "aha items" and low-attention items [16, 34].
* **FSSE Module (Forward Heterogeneous Graph Extractor):**
  * Constructs a heterogeneous graph \\(G^f = (V^f, E^f)\\) with node types \\(\mathcal{A} = \{\text{user}, \text{item}, \text{category}\}\\) and edge types \\(\mathcal{R} = \{\text{UI click}, \text{UI impression}, \text{item-category}\}\\) [35, 36].
  * Decomposes \\(G^f\\) into three relation subgraphs and applies GAT attention layers injected with normalized implicit supervised signals [18-21, 37, 38]:
    * *Normalized Impression Duration (\\(doi_{u,i}\\)):* Magnifies edges for impressions paused between \\(0.1\text{s}\\) and \\(3.0\text{s}\\) [11, 19, 39].
    * *Brief-Pause Ratio (\\(bpr_{u,i}\\)):* Attribute-level pause frequency \\(bpr_{u,i} = \sum \mathbb{I}(doi > 0.1) / |N_{u,c_i}^{f,im}|\\), penalizing accidental pauses [12, 20, 40].
    * *Normalized Click Duration (\\(doc_{u,i}\\)):* Filters out cursory switch clicks (\\(\le\\) title reading time) [13, 21, 41].
* **BSSS Module (Backward Label-Part Stabilizer):**
  * Constructs a parallel heterogeneous graph \\(G^l = (V^l, E^l)\\) over label-part behaviors (the \\(X\\)-day future return window) [22, 42].
  * Guides feature-part representation learning across three loss levels [22-25]:
    1. *Node-level Feature Alignment (\\(\mathcal{L}_{\text{node}}\\)):* Aligns \\(h_v^f\\) and \\(h_v^l\\) using distance-weighted MSE and contrastive hard-negative sampling over 2-hop same-type neighbors [23, 43, 44].
    2. *Subgraph Preference Refinement (\\(\mathcal{L}_{\text{subgraph}}\\)):* Uses type-aware pooling over 2-hop neighborhoods to align structural preference shifts across user-item-category subgraphs [24, 45, 46].
    3. *Global Embedding Stabilization (\\(\mathcal{L}_{\text{global}}\\)):* Uses a Siamese network to align global type-specific average embeddings, preserving macro behavioral trends [25, 47].
* **Joint Offline Loss Function:**
  \\[\arg\min_\Theta \mathcal{L} = \mathcal{L}_{\text{BCMIL}} + \alpha_{\text{node}} \mathcal{L}_{\text{node}} + \alpha_{\text{sub}} \mathcal{L}_{\text{subgraph}} + \alpha_{\text{global}} \mathcal{L}_{\text{global}} \quad \text{[27, 48]}\\]

#### **Credit Assignment Mechanics**
* BCMIL assigns fractional credit to individual candidate items by generating User-Item retention scores (\\(s_{ui}\\)) via instance-level multi-instance attention [14, 31, 32].
* During online serving, candidate items are re-ranked by combining the UI retention score with the online model's CTR score: \\(a_{ui} = \alpha \hat{c}_{ui} + (1 - \alpha) s_{ui}\\) [28, 49].
* It does **not** publish an identified causal multi-touch attribution sequence model or per-touch credit table; rather, it scores candidate items based on their individual capacity to induce return visits ("aha items") [14, 28, 31].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets:**
  1. *ZhihuRec (1M subset):* 7,963 users, 81,214 items, 1,271,751 interactions over 10 days (first 7 days train, last 3 days test) [50, 51].
  2. *WeChat Top Stories Dataset:* 5,000,000 users, 700,000 items, and 1,000,000,000 interactions over 40 days (first 37 days train, last 3 days test) [50, 51].
* **Production Deployment:**
  * Fully deployed in live production at **Tencent (WeChat Top Stories)** across two core channels [52, 53]:
    * *Main-Page Recommendation:* Wow, Videos, and Subscriptions channels (~7,000,000 users over a 20-day A/B test) [49, 52, 53]. Candidate items re-ranked via \\(a_{ui} = \alpha \hat{c}_{ui} + (1 - \alpha) s_{ui}\\) [49].
    * *Red-Dot Recommendation:* Front-facing notification entry point where high-scoring "aha items" are highlighted to attract inactive users back to the app [52, 54].
* **Comparison Baselines:**
  * *Base MLP:* Standard multi-layer perceptron [55].
  * *IURO (AVG):* Average-pooling multi-instance baseline [55, 56].
  * *IURO (Ding et al., RecSys '23):* Earlier retention modeling baseline without graph extractor or BSSS [55-57].
  * *IURO' & IURO+ Variants:* Systematic ablations (\\(\text{IURO+}_{\text{BMIL}}\\), \\(\text{IURO+}_G\\), \\(\text{IURO+}_{G \& \text{FSSE}}\\), \\(\text{IURO+}_{\text{FSSE} \& \text{BSSS}}\\)) [55, 58, 59].
  * *Note on RL Baselines:* The authors explicitly state they **did not compare with online RL methods**, citing RL's severe deployment/maintenance overhead, lack of interpretability, and risk of damaging production CTR/revenue [60, 61].

---

### **(5) Key Quantitative Results with Numbers**

* **Offline Retention Prediction AUC (Table 3):**
  * *ZhihuRec Dataset:* Base MLP = **0.7198**, IURO (AVG) = **0.8368**, IURO (RecSys '23) = **0.8433**, Full IURO+\\(_{\text{FSSE} \& \text{BSSS}}\\) = **0.8541** (highest AUC) [55].
  * *WeChat Top Stories Dataset:* Base MLP = **0.6816**, IURO (AVG) = **0.7268**, IURO (RecSys '23) = **0.7299**, Full IURO+\\(_{\text{FSSE} \& \text{BSSS}}\\) = **0.7502** (highest AUC) [55].
* **Online Production A/B Testing Results (Main-Page Recommendation, Tables 5–7):**
  * *Retention Lifts (\\(p \le 0.05\\)):* Next-Day Retention (NDR) **+0.781%** (vs RecSys '23 baseline +0.492%), Next-Three-Day Retention (NTDR) **+0.674%** (vs +0.339%), Next-Seven-Day Retention (NSDR) **+0.625%** (vs +0.215%) [62].
  * *DAU Lifts (\\(p \le 0.05\\)):* **+0.406%** in Wow, **+0.318%** in Videos, **+1.572%** in Subscriptions [62].
  * *User-Level Metrics:* Impression Unique Visitors (IUV) **+0.49%**, Click Unique Visitors (CUV) **+0.52%**, Unique CTR (UCTR) **+0.02%**, User Duration (UD) **+0.75%** [63].
  * *Item-Level CTR & Dwell Time:* Hit items selected by the UI Scorer achieved a CTR of **0.132** (vs 0.082 Exp / 0.083 Control) and an average item duration of **98.93s** (vs 18.89s Exp / 18.55s Control) [30, 64].
* **Online Production A/B Testing Results (Red-Dot Recommendation, Tables 8–9):**
  * *Retention & DAU Lifts (\\(p \le 0.05\\)):* NDR **+0.657%**, NTDR **+0.627%**, NSDR **+0.316%**, DAU **+0.549%** [30, 54].
  * *Aha Item Entry Metrics:*
    * Interested channel: R-IUV **+0.095%**, R-CUV **+1.044%**, R-UCTR **+1.020%** [65, 66].
    * Followed channel: R-IUV **+0.267%**, R-CUV **+4.865%**, R-UCTR **+4.612%** [65, 66].
    * Hot Issue channel: R-IUV **+0.506%**, R-CUV **+8.550%**, R-UCTR **+8.037%** [65, 66].
* **User Behavioral Analysis Numbers (Sections 3 & 4):**
  * *Short vs. Long-Term Metric Correlations:* \\(\text{CORR}(\text{clicks}, \text{dwell}) = \mathbf{0.72}\\), \\(\text{CORR}(\text{clicks}, \text{impressions}) = \mathbf{0.65}\\), \\(\text{CORR}(\text{impressions}, \text{dwell}) = \mathbf{0.47}\\) [67, 68].
  * *Weak Correlation with Retention:* \\(\text{CORR}(\text{returned days}, \text{clicks}) = \mathbf{0.35}\\), \\(\text{CORR}(\text{returned days}, \text{dwell}) = \mathbf{0.267}\\) [4].
  * *Impression Pause Signal:* Cursory scrolling impressions (\\(\le 0.1\text{s}\\)) have near-zero return probability for ~60% of users; \\(P(I_+, S^l) > P(I_-, S^l)\\) holds for **84.2%** of users [69, 70].
  * *Click Duration Signal:* Cursory switch clicks have near-zero return probability for ~80% of users; \\(P(C_+, S^l) > P(C_-, S^l)\\) holds for **96.07%** of users [41].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Inherent Randomness and Weak Causality:** Despite filtering with \\(doi\\) and \\(bpr\\), user retention carries inherent behavioral randomness that cannot be fully eliminated (e.g., users pausing due to external mobile pop-ups, phone calls, or restroom breaks) [9, 12, 70, 71].
2. **Dependence on Domain-Specific Heuristic Thresholds:** Requires setting heuristic duration and pause thresholds (\\(0.1\text{s} \le doi \le 3.0\text{s}\\), \\(bpr \ge 0.05\\)), which must be re-calibrated when transferring between different media formats (e.g., news articles vs. short videos) [11, 12].
3. **Absence of Direct Online RL Baselines:** The authors explicitly chose not to deploy online RL baselines, acknowledging that RL's extreme resource requirements and black-box nature make direct online comparison impractical in top-tier industrial systems [60, 61].
4. **Uncertainty on Single-Impression Attributes:** Attributes with only a single impression and a reasonable pause duration yield \\(bpr = 1.0\\), creating temporary noise in supervised signal confidence [71].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Cai et al. (2023) [Ref 1 / RLUR]:** *Reinforcing user retention in a billion scale short video recommender system* (WWW '23) [72].
2. **Ding et al. (2023) [Ref 11 / IURO]:** *Interpretable user retention modeling in recommender systems* (RecSys '23) [57].
3. **Wang et al. (2022) [Ref 33 / Surrogate]:** *Surrogate for long-term user experience in recommender systems* (KDD '22) [73].
4. **Wu et al. (2017) [Ref 36]:** *Returning is believing: Optimizing long-term user engagement in recommender systems* (CIKM '17) [74].
5. **Velickovic et al. (2018) [Ref 29 / GAT]:** *Graph attention networks* (ICLR '18) [75].
6. **Guo et al. (2017) [Ref 17 / DeepFM]:** *DeepFM: A factorization-machine based neural network for CTR prediction* (IJCAI '17) [76].
7. **Zhao et al. (2023) [Ref 48 / Decision Transformer]:** *User retention-oriented recommendation with decision transformer* (WWW '23) [77].

---

💡 *Would you like to explore how IURO+'s brief-pause ratio (\\(bpr\\)) or BCMIL contrastive margin loss could be adapted to identify high-retention "aha candidate profiles" for your dating app's ranker?*

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### DCEO: Direct Causal Effect Optimization for Long-Term User Value Modeling in E-commerce Search [1]
`2026_arXiv_DCEO_Direct-Causal-Effect-Optimization.md`
**Source:** https://arxiv.org/html/2608.25635  

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *DCEO: Direct Causal Effect Optimization for Long-Term User Value Modeling in E-commerce Search* [1]
* **Authors:** Junzhao Zhang, Tao Zhang, Liren Yu, Feiyi Dong, Zhixuan Zhang, Dan Ou, and Haihong Tang [1]
* **Author Affiliations:** **Taobao & Tmall Group of Alibaba**, Hangzhou & Beijing, Zhejiang, China [1]
* **Year:** **2026** (Published August 26, 2026) [1]
* **Venue:** arXiv pre-print (`arXiv:2608.25635v1 [cs.LG]`) [1]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Industrial e-commerce search engines face a fundamental **cross-granularity gap** between user-level long-term objectives (such as \\(n\\)-day cumulative purchases or Gross Merchandise Value [GMV] per user) and item-level ranking scores computed for each search request [2, 3]. Conventional search systems bridge this gap using hand-crafted multi-objective fusion formulas with globally shared, manually tuned weights over item-level predictions (click, cart, purchase, transaction value) [2, 4]. These heuristic schemes provide limited personalization, require costly repeated online A/B testing, and optimize predictive association rather than the true causal effect of item-level proxy scores on long-term user value [2, 4, 5].
* **Key Contributions:**
  1. **Cross-Granularity Causal Formulation:** Formulates item-level proxy score learning from user-level long-term objectives as a cross-granularity optimization problem, evaluating alignment using the relative causal effect (RCE) of an aggregated user-level proxy metric [2, 6, 7].
  2. **DCEO Actor-Critic Architecture:** Proposes **Direct Causal Effect Optimization (DCEO)**, an end-to-end framework where an actor model (\\(f_\theta\\)) dynamically generates context-dependent fusion weights over upstream predicted scores, calibrated user-level aggregation (\\(g_\psi\\)) connects item-level scores with user-level supervision, and a critic model (\\(h_\phi\\)) estimates ultimate outcomes to optimize RCE via a Causal Effect Loss (\\(\mathcal{L}_{\text{CE}}\\)) and Conditional Normalized Ranking Loss (\\(\mathcal{L}_{\text{CNR}}\\)) [2, 7-10].
  3. **Billion-Scale Industrial Impact:** Deployed live on Taobao/Tmall's e-commerce search engine, outperforming the conventional GMV proxy by **+0.36% in GMV** in a 41-day online A/B test [2, 6, 11].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Architectural Components**
* **Training Sample & Inputs:** Each training sample contains all impressions of user \\(u\\) on a reference day (\\(\mathcal{I}_u\\)), storing user profile/history features \\(\mathbf{z}_u\\), request-level query/context features \\(\mathbf{z}_{ur}\\), \\(M=17\\) selected upstream predicted scores \\(\mathbf{v}_{uri}\\), and long-term user outcome labels \\(Y_u\\) (\\(n\\)-day cumulative GMV or purchase count) [7, 12-15].
* **Actor (\\(f_\theta\\)):** Inputs user features \\(\mathbf{z}_u\\) and request features \\(\mathbf{z}_{ur}\\) to generate request-specific softmax weights \\(\mathbf{w}_{ur} = f_\theta(\mathbf{z}_u, \mathbf{z}_{ur})\\) (where \\(w_{ur}^m \ge 0, \sum_{m=1}^M w_{ur}^m = 1\\)) [14, 16]. The weights combine with selected upstream predicted scores \\(\mathbf{v}_{uri}\\) to yield item-level proxy scores:
  \\[p_{uri}(\theta) = \sum_{m=1}^M w_{ur}^m v_{uri}^m\\] [16].
* **Calibrated User-Level Aggregation (\\(g_\psi\\)):** Aggregates daily item proxy scores \\(\hat{p}_u = \frac{1}{N_u} \sum p_{uri}(\theta)\\) and calibrates them to a fixed reference impression count (\\(C=100\\)) via calibration model \\(g_\psi(\hat{p}_u, N_u)\\), producing an unconfounded user-level proxy metric \\(P_u(\theta)\\) [7, 15-17].
* **Critic (\\(h_\phi\\)) & Causal Effect Loss (\\(\mathcal{L}_{\text{CE}}\\)):** Critic \\(h_\phi(\mathbf{z}_u, P_u)\\) estimates ultimate long-term outcome \\(Y_u\\) [9]. The actor is updated by minimizing the negative estimated outcome difference under a relative intervention \\(\delta = 0.05\\) (5% relative increase):
  \\[\mathcal{L}_{\text{CE}} = -\mathbb{E}_u \left[ h_{\text{sg}(\phi)}(\mathbf{z}_u, (1+\delta)P_u(\theta)) - h_{\text{sg}(\phi)}(\mathbf{z}_u, P_u(\theta)) \right]\\] [9, 10, 15].
* **Conditional Normalized Ranking Loss (\\(\mathcal{L}_{\text{CNR}}\\)):** Normalization model \\(e_\zeta(\mathbf{z}_u)\\) predicts conditional mean and variance \\((\mu_P, \mu_Y, \log\sigma_P, \log\sigma_Y)\\) to produce normalized metrics \\(\widetilde{P}_u(\theta)\\) and \\(\widetilde{Y}_u\\), optimizing Bradley–Terry pairwise ranking loss to align proxy metric orderings with long-term outcomes [9, 18, 19].
* **Joint Actor Loss:** \\(\mathcal{L}_{\text{actor}} = \mathcal{L}_{\text{CE}} + \alpha \mathcal{L}_{\text{CNR}}\\) (with weight \\(\alpha = 0.3\\)) [9, 15].
* **Online Serving:** Deploy only the lightweight actor \\(f_\theta\\). Computes \\(\mathbf{w}_{ur}\\), item proxy score \\(p_{uri}\\), and incorporates it directly into the multi-objective fusion score:
  \\[s_{uri} \leftarrow s_{uri} + \lambda \log(\max\{p_{uri}, \epsilon\})\\] [13, 17, 20, 21].

#### **Credit Assignment Mechanics**
* Credit is assigned at the **individual item impression level** within each request by generating context-dependent, personalized fusion weights \\(\mathbf{w}_{ur}\\) over upstream predicted scores [13, 14, 16].
* It does **not** publish an identified multi-touch sequence attribution table across past interactions; rather, it uses calibrated user-level aggregation (\\(P_u\\)) and a critic (\\(h_\phi\\)) to map user-level \\(n\\)-day outcomes back to item-level proxy scoring weights [7, 8, 16].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets & Scale:** Industrial search logs from Taobao/Tmall's e-commerce search engine [15]. Models are trained on 14 consecutive days of user logs and evaluated on the 15th day [15]. Evaluates 17 selected upstream predicted scores (e.g., `impr2click`, `click2pay`, `click2pay10`, `click2pay30`, `click2pay100`, `click2pay1000`) mapped to \\([1]\\) [15]. The ultimate objective is 4-day cumulative GMV starting from the reference day [15].
* **Production Deployment:** Live production deployment on Taobao/Tmall's e-commerce search engine serving hundreds of millions of users, evaluated via a **41-day online A/B test** [2, 6, 22].
* **Comparison Baselines:**
  * *Conventional GMV Proxy (Online Control):* \\(p_{\text{GMV}} = \text{pCTR} \times \text{pCVR} \times \mathbb{E}[\text{transaction value} \mid \text{purchase}=1]\\) [22].
  * *Predictive-Association Optimization Loss:* \\(-h_{\text{sg}(\phi)}(\mathbf{z}_u, P_u(\theta))\\) (optimizing predictive association/correlation instead of relative causal effect) [23].
  * *Causal Effect Loss alone (\\(\mathcal{L}_{\text{CE}}\\) without \\(\mathcal{L}_{\text{CNR}}\\))* [23].
  * *Upstream Score Set Ablations:* `impr2gmv` only, Basic impression-level set, Value-aware set, Conversion-funnel set [24, 25].

---

### **(5) Key Quantitative Results with Numbers**
* **Live Online A/B Test Results (41-day test vs. Conventional GMV Proxy, Table 8 & Section 5.7):**
  * **GMV Lift:** **+0.36%** relative gain over control [2, 6, 11].
  * **Click Count Lift:** **+0.36%** relative gain over control [11].
  * **Purchase Count Lift:** **+0.12%** relative gain over control [11].
* **Offline Relative Causal Effect (RCE, Table 3 & Section 5.3):**
  * *Predictive Association Optimization:* **RCE = 0.022** [23].
  * *Causal Effect Loss (\\(\mathcal{L}_{\text{CE}}\\) alone):* **RCE = 0.031** [23].
  * *Full DCEO (\\(\mathcal{L}_{\text{actor}} = \mathcal{L}_{\text{CE}} + \alpha \mathcal{L}_{\text{CNR}}\\)):* **RCE = 0.053** (**2.41x improvement** over predictive association) [23, 26].
* **Upstream Score Set Impact (Table 5 & Section 5.5):**
  * `impr2gmv` only: **RCE = 0.027** [24, 25].
  * Basic impression-level set: **RCE = 0.039** [24, 25].
  * Value-aware set: **RCE = 0.041** [24, 25].
  * Conversion-funnel set: **RCE = 0.040** [24, 25].
  * Full 17-score set: **RCE = 0.053** [24, 25].
* **Objective Sensitivity Mean Actor Weights (Table 6 & Section 5.6.1):**
  * *4-day Click Count Objective:* `impr2click` weight = **0.999** [25, 27].
  * *4-day Purchase Count Objective:* `impr2click` = **0.531**, `click2pay` = **0.101**, `click2pay10` = **0.256** [25, 27].
  * *4-day GMV Objective:* `impr2click` = **0.404**, `click2pay` = **0.032**, `click2pay10` = **0.154**, `click2pay30` = **0.079**, `click2pay100` = **0.105**, `click2pay1000` = **0.205** [25, 27].
* **Hyperparameters:** Reference impression count \\(C = 100\\), relative intervention \\(\delta = 0.05\\), ranking loss weight \\(\alpha = 0.3\\) [15].

---

### **(6) Limitations, Failure Modes, or Negative Results**
1. **Convex Combination Expressiveness Trade-Off:** The actor is restricted to predicting context-dependent weights for a convex combination of selected upstream predicted scores rather than mapping raw impression-level features directly to a proxy score [28]. While this improves training stability and online serving speed, the actor cannot recover signals absent from upstream models and inherits their coverage limits [28].
2. **Exclusion of User Activity Expansion Offline:** Calibrating proxy metrics to a fixed impression count (\\(C=100\\)) deliberately excludes changes in the ultimate objective that arise through ranking-induced changes in user activity and impression count [29]. Offline RCE is an alignment metric at fixed impression count, not an exact estimate of total deployment effect [29].
3. **Poorer Alignment of Single Un-decomposed GMV Proxy (`impr2gmv`):** Using only `impr2gmv` yielded a low RCE of **0.027** (vs **0.053** for full score set), proving that a single un-decomposed GMV proxy fails to capture multi-stage conversion dynamics [24, 25].
4. **Failure of Predictive Association:** Optimizing predictive association directly achieved an RCE of only **0.022** (less than half of DCEO's **0.053**), demonstrating that predictive correlation fails to translate into causal long-term value improvements under ranking interventions [23].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Zhao et al. (2019) [Ref 19 / Multitask Video RecSys]:** *Recommending what video to watch next: a multitask ranking system* (RecSys '19) [4, 30].
2. **Wang et al. (2022) [Ref 2 / Surrogate]:** *Surrogate for long-term user experience in recommender systems* (KDD '22) [31, 32].
3. **Ding et al. (2023) [Ref 11 / IURO]:** *Interpretable user retention modeling in recommendation* (RecSys '23) [33].
4. **Zhang et al. (2022) [Ref 8 / BatchRL-MTF]:** *Multi-task fusion via reinforcement learning for long-term user satisfaction in recommender systems* (KDD '22) [30, 34].
5. **Pei et al. (2019) [Ref 1 / Value-Aware Rec]:** *Value-aware recommendation based on reinforcement learning* (WWW '19) [34].
6. **Wang et al. (2024) [Ref 14 / Future Impact Decomposition]:** *Future impact decomposition in request-level recommendations* (KDD '24) [31, 32].
7. **VanderWeele (2013) [Ref 20 / Causal Surrogates]:** *Surrogate measures and consistent surrogates* (Biometrics '13) [5, 32].

---

💡 *Would you like to explore how DCEO's actor-critic relative causal effect loss (\\(\mathcal{L}_{\text{CE}}\\)) or calibrated user-level aggregation could be adapted to optimize candidate profile fusion weights for your dating app?*

---

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

