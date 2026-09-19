# Relevance index 8/10 — Project Relevance sections of all cards (generated)

### Rethinking User Retention Modeling in Recommendation [1, 2]
`2026_TOIS_IURO+_Rethinking-User-Retention-Modeling.md`
**Source:** https://dl.acm.org/doi/pdf/10.1145/3790098  

### **Part 1: Dating App Retention Attribution Project Evaluation**

---

#### **(A) Q1 or Q2 or Both or Neither?**
* **Answer:** **Q2 Only** [1-5].
* **Explanation:**
  * **Q1 (Industry/Production Attribution 2025–2026):** **No.** While published in TOIS in March 2026 (Vol. 44, No. 3), this paper evaluates a lightweight retention-oriented candidate profile/item ranking system (\\(s_{ui}\\)) rather than an industry multi-touch attribution (MTA) measurement system [1-3, 6, 7].
  * **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **Yes.** The framework assigns User-Item (UI) retention scores (\\(s_{ui}\\)) and instance-level multi-instance attention weights to individual clicked and impressed in-app interactions to explain and predict 3-day user retention [3, 4, 8-10].

---

#### **(B) Q2 Class**
* **Classification:** **PARTIAL** [3, 4, 8, 9, 11, 12].
* **Justification:** IURO+ generates item/action-level retention scores (\\(s_{ui}\\)) via a 3-layer Feedforward UI Scorer and aggregates them using instance-level multi-instance attention (BCMIL) to predict next-3-day retention (\\(\hat{y}_u\\)) [4, 8-10]. The paper explicitly acknowledges and addresses offline-online serving gaps, weak causality, behavioral randomness, and the lack of explicit per-item retention labels [3, 13, 14]. However, it does not formulate an identified causal Multi-Touch Attribution (MTA) model under formal counterfactual graph identification [3, 12, 15].

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Yes.** Generates user-item retention scores \\(s_{ui} = \text{FFN}_3(\text{Concat}(h_u, h_i))\\) and instance-level attention weights (\\(\text{softmax}(h_u \cdot h_i / \sqrt{d})\\)) for individual clicked and impressed user behaviors [8-10].
* **Target Outcome:** **Next-3-Day User Retention / Return Days (\\(\hat{y}_u\\))**, weighted by label-part cumulative engagement volume (\\(W_u = a \log(1 + n^c) + b \log(1 + n^i)\\)) [9, 10]. In online serving, candidate items are re-ranked via \\(a_{ui} = \alpha \hat{c}_{ui} + (1 - \alpha) s_{ui}\\) [6, 7, 16].

---

#### **(D) Replacing Last-Touch N7 → Latest Swipes**
* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% credit to the final swipe before Day 7, ignoring earlier high-value interactions. IURO+ replaces rule-based last-touch heuristics by computing explicit user-item retention scores (\\(s_{ui}\\)) across all past interactions using BCMIL [4, 8, 9]. It uses contrastive margin loss (\\(L_{\text{CL}}\\)) to sharpen "aha items" (high-impact interactions) [4, 17, 18] and employs a Backward Supervised Signals Stabilizer (BSSS) to retrospectively guide training using label-part behaviors [11, 13, 19].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Interaction Sequence:* User swiping logs, mutual matches, and 4-way messaging conversations are mapped to short-term clicked and impressed behaviors (\\(N_{u,ck}^f, N_{u,im}^f\\)) [8-10].
  2. *UI Scorer (\\(s_{ui}\\)):* Evaluates each swipe, match, or messaging interaction based on user attributes (\\(h_u\\)) and candidate profile features (\\(h_i\\)) [8].
  3. *Aha Item Identification:* BCMIL isolates rare, high-impact "aha interactions" (e.g., a high-affinity mutual match or a deep messaging conversation) that served as primary drivers of 7-day retention [4, 17, 20, 21].
  4. *Online Candidate Ranking:* Candidate profiles are re-ranked via \\(a_{ui} = \alpha \hat{c}_{ui} + (1 - \alpha) s_{ui}\\), prioritizing profiles that align with past retention-inducing "aha" interactions [6, 7, 16].

---

#### **(E) Selection-Bias & Confounding Handling**
1. **Implicit Supervised Signals Filtering:** Filters out cursory scrolling impressions (\\(\le 0.1\text{s}\\)) and quick-switch clicks (\\(\le 3\text{s}\\)) as negative signals, restricting positive signals to reasonable duration-on-impression (\\(doi\\)), attribute brief-pause ratio (\\(bpr \ge 0.05\\)), and reasonable click duration (\\(doc\\) between \\(3\text{s}\\) and \\(3\text{m}\\)) [22-26].
2. **Label-Part Cumulative Weighting (\\(W_u\\)):** Multiplies retention targets by label-part cumulative activity (\\(W_u = a \log(1 + n^c) + b \log(1 + n^i)\\)) to reduce background noise from passive or accidental app opens [10, 27].
3. **Backward Supervised Signals Stabilizer (BSSS):** Uses label-part behaviors to guide feature-part training across node alignment (\\(L_{\text{node}}\\)), subgraph preference refinement (\\(L_{\text{subgraph}}\\)), and global embedding stabilization (\\(L_{\text{global}}\\)), suppressing behavioral randomness [11, 13, 19, 28].
4. **Exclusion of User-Level Statistical Features:** Intentionally excludes user-level activity stats (e.g., total past clicks) from user profile embeddings to prevent hyper-active user bias from dominating item-level retention score exploration [8, 29].

---

#### **(F) Deployment and Production Dataset Evidence**
* **Production Deployment:** Fully deployed live in production at **Tencent (WeChat Top Stories)** across Main-Page Recommendation (Wow, Videos, Subscriptions) and Red-Dot Recommendation [1, 2, 5, 16, 20, 21].
* **Datasets:**
  * *WeChat Top Stories Industrial Dataset:* **5,000,000 users**, **700,000 items**, and **1,000,000,000 interactions** over 40 days [29, 30].
  * *ZhihuRec 1M Offline Benchmark:* **7,963 users**, **81,214 items**, and **1,271,751 interactions** over 10 days [29, 30].
* **Quoted Quantitative Results:**
  * **Main-Page Online A/B Test Lifts (>7M users, 20 days, Tables 5–7):**
    * *Retention Rates (\\(p \le 0.05\\)):* Next-Day Retention (NDR) **+0.781%** (vs RecSys '23 baseline **+0.492%**), Next-Three-Day Retention (NTDR) **+0.674%** (vs **+0.339%**), Next-Seven-Day Retention (NSDR) **+0.625%** (vs **+0.215%**) [31, 32].
    * *DAU Lifts (\\(p \le 0.05\\)):* Wow **+0.406%**, Videos **+0.318%**, Subscriptions **+1.572%** [32].
    * *User-Level Metrics:* Impression Unique Visitors (IUV) **0.49%**, Click Unique Visitors (CUV) **+0.52%**, Unique CTR (UCTR) **+0.02%**, User Duration (UD) **+0.75%** [32, 33].
    * *Item-Level Metrics:* Hit item CTR **0.132** (vs Exp **0.082** / Con **0.083**); hit item duration **98.93s** (vs Exp **18.89s** / Con **18.55s**) [34].
  * **Red-Dot Online A/B Test Lifts (Tables 8–9):**
    * *Retention & DAU (\\(p \le 0.05\\)):* NDR **+0.657%**, NTDR **+0.627%**, NSDR **+0.316%**, DAU **+0.549%** [35, 36].
    * *Entry Category Lifts:* Interested (R-IUV **+0.095%**, R-CUV **+1.044%**, R-UCTR **+1.020%**); Followed (R-IUV **+0.267%**, R-CUV **+4.865%**, R-UCTR **+4.612%**); Hot Issue (R-IUV **+0.506%**, R-CUV **+8.550%**, R-UCTR **+8.037%**) [37, 38].
  * **Filter Bubble Escape:** **32.13% of users** started following novel, surprising categories recommended by IURO+ in their label-part behaviors [38].
  * **Offline Prediction AUC (Table 3):**
    * *ZhihuRec 1M:* Base MLP (**0.7198**), IURO AVG (**0.5841**), IURO RecSys '23 (**0.8368**), IURO' (**0.8433**), \\(\text{IURO+}_{\text{BMIL}}\\) (**0.8406**), \\(\text{IURO+}_{\text{BCMIL}}\\) (**0.8428**), \\(\text{IURO+}_{\text{FSSE}}\\) (**0.8539**), \\(\text{IURO+}_{\text{BSSS}}\\) (**0.8541**) [39].
    * *WeChat Top Stories:* Base MLP (**0.6816**), IURO AVG (**0.6732**), IURO RecSys '23 (**0.7268**), IURO' (**0.7299**), \\(\text{IURO+}_{\text{BMIL}}\\) (**0.7280**), \\(\text{IURO+}_{\text{BCMIL}}\\) (**0.7389**), \\(\text{IURO+}_{\text{FSSE}}\\) (**0.7465**), \\(\text{IURO+}_{\text{BSSS}}\\) (**0.7502**) [39].
  * **Short vs. Long-Term Metric Correlations (Section 3):** \\(\text{CORR}(\text{clicks}, \text{dwell}) = \mathbf{0.72}\\), \\(\text{CORR}(\text{clicks}, \text{impressions}) = \mathbf{0.65}\\), \\(\text{CORR}(\text{impressions}, \text{dwell}) = \mathbf{0.47}\\) [40, 41]. Weak retention correlation: \\(\text{CORR}(\text{returned days}, \text{clicks}) = \mathbf{0.35}\\), \\(\text{CORR}(\text{returned days}, \text{dwell}) = \mathbf{0.267}\\) [40]. **75% of users** return fewer than 3 days within 2 weeks [42].
  * **Implicit Signal Validation:** Probability that \\(P(l_+, S_l) > P(l_-, S_l)\\) is **84.2%** (and **89.6%** when filtered with \\(bpr \ge 0.05\\)) [43, 44]; probability that \\(P(c_+, S_l) > P(c_-, S_l)\\) is **96.07%** (**80% of users** have \\(P(c_-, S_l) \approx 0\\)) [45].
  * **Explicit User Survey:** **69% of survey participants** claim they return to the system if recommended items are relaxing and stress-relieving [46]. Relative retention rates for negative feedback reasons: "Not interested in items" (**35.38% NDR / 36.45% NTDR** — lowest retention), "Low-quality content" (**90.29% / 91.78%**), "Advertising promotion" (**91.89% / 93.06%**), "Poor diversity" (**97.33% / 98.36%**), "Exaggerating titles" (**98.98% / 99.05%**), "Don't like author/content" (**102.29% / 102.03%**), "Repeated recommendation" (**113.51% / 108.07%**) [47].

---

### **Part 2: Detailed Technical Breakdown of the Source**

---

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Rethinking User Retention Modeling in Recommendation* [1, 2]
* **Authors:** **Rui Ding**\*¹, **Ruobing Xie**\*², **Xiaobo Hao**², **Xiaochun Yang**\*¹, **Kaikai Ge**², **Xu Zhang**², **Zhanhui Kang**², **Jie Zhou**², and **Leyu Lin**² (\*Corresponding authors) [1, 2]
* **Author Affiliations:**
  1. **Northeastern University**, School of Computer Science and Engineering, Shenyang, China (`ruiding.neu@outlook.com`, `yangxc@mail.neu.edu.cn`) [1, 2]
  2. **Tencent**, Beijing, China (`{xrbsnow-ing, rolyhao, kavinge, xuonezhang, kegokang, withtomzhou, goshawklin}@tencent.com`) [1, 2]
* **Year & Venue:** Published in **March 2026** in *ACM Transactions on Information Systems (TOIS)*, Vol. 44, No. 3, Article 64 (35 pages). DOI: `10.1145/3790098` [2, 48].

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Standard recommender systems optimize short-term metrics (clicks, views, dwell time) that fail to capture long-term user satisfaction and retention [1, 48-50]. Retention modeling suffers from three major challenges: (i) an offline-online serving gap where online serving requires item-level scoring while offline training has only user-level return labels [3], (ii) severe signal sparsity (one return label vs. hundreds of daily interactions) [3], and (iii) weak causality and behavioral randomness without explicit supervised signals [3].
* **Key Contributions:**
  1. **Empirical Discovery of Implicit Supervised Signals:** Discovers and validates implicit retention signals: duration on impression (\\(doi\\), filtering out cursory scrolling \\(\le 0.1\text{s}\\)), attribute-level brief-pause ratio (\\(bpr \ge 0.05\\)), and duration on click (\\(doc\\), distinguishing quick switches \\(\le 3\text{s}\\) from deliberate reading) [22-26].
  2. **IURO+ Framework:** Introduces a non-RL framework consisting of three core modules:
     * **BCMIL (Behavior-wise Contrastive Multi-Instance Learning):** Jointly models clicks and impressions via multi-instance attention and contrastive margin loss (\\(L_{\text{CL}}\\)) to sharpen rare "aha items" [4, 8, 9, 17, 18, 51].
     * **FSSE (Forward Supervised Signals Extractor):** Embeds implicit supervised signals (\\(doi\\), \\(bpr\\), \\(doc\\)) into a heterogeneous Graph Attention Network (GAT) over feature-part behaviors [4, 14, 24, 51-54].
     * **BSSS (Backward Supervised Signals Stabilizer):** Uses label-part behaviors across three levels (node alignment \\(L_{\text{node}}\\), subgraph preference refinement \\(L_{\text{subgraph}}\\), global embedding stabilization \\(L_{\text{global}}\\)) to retrospectively guide training and suppress randomness [11, 13, 19, 28, 51].
  3. **Industrial Plug-and-Play Deployment:** Deploys IURO+ as a lightweight online plug-in at Tencent (WeChat Top Stories) across Main-Page and Red-Dot recommendations, delivering significant retention gains without harming CTR or dwell time [5, 6, 20, 31, 35, 55, 56].

---

#### **(3) Proposed Method or Architecture in Detail**
* **BCMIL Module (UI Scorer & Contrastive Learning):**
  * Computes UI retention scores \\(s_{ui} = \text{FFN}_3([h_u; h_i])\\) using a 3-layer Feedforward Network [8].
  * Integrates clicked behaviors (\\(N_{u,ck}^f\\)) and impressed behaviors (\\(N_{u,im}^f\\)) separately via instance-level attention [9, 10]:
    \\[\hat{y}_u = W \sum_{i \in N_{u,ck}^f} \text{softmax}\left(\frac{h_u \cdot h_i}{\sqrt{d}}\right) s_{ui} + (1 - W) \sum_{i \in N_{u,im}^f} \text{softmax}\left(\frac{h_u \cdot h_i}{\sqrt{d}}\right) s_{ui} \quad \text{[10]}\\]
  * Applies contrastive margin loss \\(L_{\text{CL}} = \max(0, |\hat{y}_u - \hat{y}_u^{\text{high}}| - |\hat{y}_u - \hat{y}_u^{\text{low}}| + m)\\) to widen the score gap between high-attention "aha items" and low-attention items [17, 18].
* **FSSE Module (Forward Heterogeneous Graph Extractor):**
  * Constructs a heterogeneous graph \\(G^f = (V^f, E^f)\\) with node types \\(\mathcal{A} = \{\text{user}, \text{item}, \text{category}\}\\) and edge types \\(\mathcal{R} = \{\text{UI click}, \text{UI impression}, \text{item-category}\}\\) [14, 52].
  * Decomposes \\(G^f\\) into three relation subgraphs and applies GAT attention layers injected with normalized implicit supervised signals [14, 52-54, 57]:
    * *Normalized Impression Duration (\\(doi_{u,i}\\)):* Magnifies edges for impressions paused between \\(0.1\text{s}\\) and \\(3.0\text{s}\\) [52, 58, 59].
    * *Brief-Pause Ratio (\\(bpr_{u,i}\\)):* Attribute-level pause frequency \\(bpr_{u,i} = \sum \mathbb{I}(doi > 0.1) / |N_{u,c_i}^{f,im}|\\), penalizing accidental pauses [53, 60, 61].
    * *Normalized Click Duration (\\(doc_{u,i}\\)):* Filters out cursory switch clicks (\\(\le 3\text{s}\\)) [19, 54].
* **BSSS Module (Backward Label-Part Stabilizer):**
  * Constructs a parallel heterogeneous graph \\(G^l = (V^l, E^l)\\) over label-part behaviors [19, 62].
  * Guides feature-part representation learning across three loss levels [11, 19, 28]:
    1. *Node-level Feature Alignment (\\(L_{\text{node}}\\)):* Aligns \\(h_v^f\\) and \\(h_v^l\\) using distance-weighted MSE [11].
    2. *Subgraph Preference Refinement (\\(L_{\text{subgraph}}\\)):* Uses type-aware pooling over 2-hop neighborhoods to align structural preference shifts across user-item-category subgraphs [28].
    3. *Global Embedding Stabilization (\\(L_{\text{global}}\\)):* Uses a Siamese network to align global type-specific average embeddings [28].
* **Joint Offline Loss Function:**
  \\[\arg\min_\Theta L = L_{\text{BCMIL}} + \alpha_{\text{node}} L_{\text{node}} + \alpha_{\text{sub}} L_{\text{subgraph}} + \alpha_{\text{global}} L_{\text{global}} \quad \text{[28, 56]}\\]

---

#### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets:**
  1. *ZhihuRec (1M subset):* 7,963 users, 81,214 items, 1,271,751 interactions over 10 days [29, 30].
  2. *WeChat Top Stories Dataset:* 5,000,000 users, 700,000 items, 1,000,000,000 interactions over 40 days [29, 30].
* **Production Deployment:**
  * Fully deployed in live production at **Tencent (WeChat Top Stories)** across two core channels [1, 2, 5, 16, 20, 21]:
    * *Main-Page Recommendation:* Wow, Videos, and Subscriptions channels (~7,000,000 users over a 20-day A/B test) [5, 16, 20]. Candidate items re-ranked via \\(a_{ui} = \alpha \hat{c}_{ui} + (1 - \alpha) s_{ui}\\) [6, 7, 16].
    * *Red-Dot Recommendation:* Front-facing notification entry point where high-scoring "aha items" are highlighted to attract inactive users back to the app [20, 21].
* **Comparison Baselines:**
  * *Base MLP:* Standard multi-layer perceptron [63].
  * *IURO (AVG):* Average-pooling multi-instance baseline [63].
  * *IURO (Ding et al., RecSys '23):* Earlier retention modeling baseline without graph extractor or BSSS [63].
  * *IURO' & IURO+ Variants:* Systematic ablations (\\(\text{IURO+}_{\text{BMIL}}\\), \\(\text{IURO+}_{\text{BCMIL}}\\), \\(\text{IURO+}_{\text{FSSE}}\\), \\(\text{IURO+}_{\text{BSSS}}\\)) [63-65].
  * *Note on RL Baselines:* The authors explicitly state they **did not compare with online RL methods**, citing RL's severe deployment/maintenance overhead, lack of interpretability, and risk of damaging production CTR/revenue [12, 15].

---

#### **(5) Key Quantitative Results with Numbers**
* **Offline Retention Prediction AUC (Table 3):**
  * *ZhihuRec Dataset:* Base MLP = **0.7198**, IURO (AVG) = **0.5841**, IURO (RecSys '23) = **0.8368**, IURO' = **0.8433**, \\(\text{IURO+}_{\text{BSSS}}\\) = **0.8541** (highest AUC) [39].
  * *WeChat Top Stories Dataset:* Base MLP = **0.6816**, IURO (AVG) = **0.6732**, IURO (RecSys '23) = **0.7268**, IURO' = **0.7299**, \\(\text{IURO+}_{\text{BSSS}}\\) = **0.7502** (highest AUC) [39].
* **Online Production A/B Testing Results (Main-Page Recommendation, Tables 5–7):**
  * *Retention Lifts (\\(p \le 0.05\\)):* Next-Day Retention (NDR) **+0.781%** (vs RecSys '23 baseline **+0.492%**), Next-Three-Day Retention (NTDR) **+0.674%** (vs **+0.339%**), Next-Seven-Day Retention (NSDR) **+0.625%** (vs **+0.215%**) [31, 32].
  * *DAU Lifts (\\(p \le 0.05\\)):* **+0.406%** in Wow, **+0.318%** in Videos, **+1.572%** in Subscriptions [32].
  * *User-Level Metrics:* Impression Unique Visitors (IUV) **0.49%**, Click Unique Visitors (CUV) **+0.52%**, Unique CTR (UCTR) **+0.02%**, User Duration (UD) **+0.75%** [32, 33].
  * *Item-Level CTR & Dwell Time:* Hit items selected by the UI Scorer achieved a CTR of **0.132** (vs **0.082** Exp / **0.083** Control) and an average item duration of **98.93s** (vs **18.89s** Exp / **18.55s** Control) [34].
* **Online Production A/B Testing Results (Red-Dot Recommendation, Tables 8–9):**
  * *Retention & DAU Lifts (\\(p \le 0.05\\)):* NDR **+0.657%**, NTDR **+0.627%**, NSDR **+0.316%**, DAU **+0.549%** [35, 36].
  * *Entry Channel Lifts:* Interested (R-IUV **+0.095%**, R-CUV **+1.044%**, R-UCTR **+1.020%**); Followed (R-IUV **+0.267%**, R-CUV **+4.865%**, R-UCTR **+4.612%**); Hot Issue (R-IUV **+0.506%**, R-CUV **+8.550%**, R-UCTR **+8.037%**) [37, 38].
* **User Behavioral Analysis Numbers (Sections 3 & 4):**
  * *Short vs. Long-Term Metric Correlations:* \\(\text{CORR}(\text{clicks}, \text{dwell}) = \mathbf{0.72}\\), \\(\text{CORR}(\text{clicks}, \text{impressions}) = \mathbf{0.65}\\), \\(\text{CORR}(\text{impressions}, \text{dwell}) = \mathbf{0.47}\\) [40, 41].
  * *Weak Retention Correlations:* \\(\text{CORR}(\text{returned days}, \text{clicks}) = \mathbf{0.35}\\), \\(\text{CORR}(\text{returned days}, \text{dwell}) = \mathbf{0.267}\\) [40].
  * *Impression Pause Signal:* Cursory scrolling impressions (\\(\le 0.1\text{s}\\)) have near-zero return probability for ~60% of users; \\(P(l_+, S_l) > P(l_-, S_l)\\) holds for **84.2%** of users (and **89.6%** with \\(bpr \ge 0.05\\) filter) [43, 44, 66].
  * *Click Duration Signal:* Quick-switch clicks (\\(\le 3\text{s}\\)) have near-zero return probability for ~80% of users; \\(P(c_+, S_l) > P(c_-, S_l)\\) holds for **96.07%** of users [45].

---

#### **(6) Limitations, Failure Modes, or Negative Results**
1. **Inherent Randomness and Weak Causality:** Despite filtering with \\(doi\\) and \\(bpr\\), user retention carries inherent behavioral randomness that cannot be fully eliminated (e.g., users pausing due to external mobile pop-ups, phone calls, or restroom breaks) [23, 43, 67, 68].
2. **Dependence on Domain-Specific Heuristic Thresholds:** Requires setting heuristic duration and pause thresholds (\\(0.1\text{s} \le doi \le 3.0\text{s}\\), \\(bpr \ge 0.05\\), \\(3\text{s} \le doc \le 3\text{m}\\)), which must be re-calibrated when transferring between different media formats (e.g., news articles vs. short videos) [23, 25, 26].
3. **Absence of Direct Online RL Baselines:** The authors explicitly chose not to deploy online RL baselines, acknowledging that RL's extreme resource requirements, long warm-up periods, and black-box nature make direct online comparison impractical in top-tier industrial systems [12, 15].
4. **Uncertainty on Single-Impression Attributes:** Attributes with only a single impression and a reasonable pause duration yield \\(bpr = 1.0\\), creating temporary noise in supervised signal confidence [67].

---

#### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Cai et al. (2023) [Ref 1 / RLUR]:** *Reinforcing user retention in a billion scale short video recommender system* (WWW '23) [69].
2. **Ding et al. (2023) [Ref 11 / IURO]:** *Interpretable user retention modeling in recommender systems* (RecSys '23) [70].
3. **Wang et al. (2022) [Ref 33 / Surrogate]:** *Surrogate for long-term user experience in recommender systems* (KDD '22) [71].
4. **Wu et al. (2017) [Ref 36]:** *Returning is believing: Optimizing long-term user engagement in recommender systems* (CIKM '17) [72].
5. **Velickovic et al. (2018) [Ref 29 / GAT]:** *Graph attention networks* (ICLR '18) [73].
6. **Guo et al. (2017) [Ref 17 / DeepFM]:** *DeepFM: A factorization-machine based neural network for CTR prediction* (IJCAI '17) [74].
7. **Zhao et al. (2023) [Ref 48 / Decision Transformer]:** *User retention-oriented recommendation with decision transformer* (WWW '23) [75].

---

💡 *Would you like to explore how IURO+'s brief-pause ratio (\\(bpr\\)) or BCMIL contrastive margin loss could be adapted to identify high-retention "aha candidate profiles" for your dating app's ranker?*

---

