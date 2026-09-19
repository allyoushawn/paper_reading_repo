# Compact relevance index — truncated Project Relevance from this-run cards (2/2)

### Buyer journey insights with data-driven attribution [1]
`2025_LinkedIn_LiDDA_Buyer-Journey-Data-Driven-Attribution.md`
**Source:** https://www.linkedin.com/blog/engineering/marketing/buyer-journey-insights-with-data-driven-attribution  
**Q2 class:** NOT

### **(A) Q1 or Q2 Alignment**

* **Q1 (Industry/Production Attribution 2025–2026):** **Yes.** Published on January 22, 2025 [1], this source details LinkedIn's production hybrid attribution platform deployed for internal product marketing and expanded to the LinkedIn Marketing Solutions (LMS) advertiser stack [1-3].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper models binary marketing conversion outcomes (\\(C\\)) rather than user retention or active days [4, 5].
* **Summary:** **Q1 only.**

---

### **(B) Q2 Class**

* **Classification:** **NOT**
* **Explanation:** The system generates multi-touch fractional credit for marketing conversion events (\\(C\\)), not for user retention, days-active, or return-visit outcomes [4, 5].

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **Yes.** The model passes the touchpoint sequence through self-attention Transformer layers, extracting the combined attention weight matrix and normalizing it so weights sum to 1.0 (\\(\sum w_i = 1.0\\)) [5, 6]. These normalized attention weights are directly interpreted as the percentage contribution of each individual touchpoint [5].
* **Target Outcome:** Binary conversion outcome \\(C\\) (whether a customer/member journey results in a conversion) [4, 5].

---

### **(D) Replacing Last-Touch N7 → Latest Swipes**

* **How it Improves on Last-Touch:** Last-touch assigns 100% credit to the final interaction, over-indexing on bottom-of-funnel conversion points while completely
… [truncated]

### AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems [1, 2]
`2025_WWW_AURO_Adaptive-User-Retention-Optimization.md`
**Source:** https://arxiv.org/pdf/2310.03984.pdf  
**Q2 class:** NOT

### **Part 1: Detailed Technical Breakdown of the Source**

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems* [1, 2]
* **Authors:** **Zhenghai Xue**¹, **Qingpeng Cai**\*², **Bin Yang**², **Lantao Hu**², **Peng Jiang**², **Kun Gai**³, and **Bo An**¹ (*\*Corresponding author*) [1–2]
* **Author Affiliations:**
  1. **Nanyang Technological University**, Singapore / Skywork AI [1–2]
  2. **Kuaishou Technology**, Beijing, China [1]
  3. **Unaffiliated**, Beijing, China [1]
* **Year:** **2025** (Published at WWW ’25; arXiv pre-print `arXiv:2310.03984`) [3–4]
* **Venue:** *Proceedings of the ACM Web Conference 2025 (WWW ’25)*, April 28–May 2, 2025, Sydney, NSW, Australia [3–4]

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Reinforcement Learning (RL) algorithms for user retention struggle with environment non-stationarity driven by shifting user behavior patterns (such as fluctuating interaction rates and user return-time distributions) [2-5]. Shifting environments cause policy performance degradation, while "implicit cold-start" scenarios force policies to continually interact with users exhibiting novel behaviors [3, 6].
* **Key Contributions:**
  1. **AURO Framework:** Formulates user retention under environment non-stationarity using Hidden Parameter MDPs (HiP-MDP) [3, 7].
  2. **Value-Based State Abstraction Module:** Introduces a state abstraction network trained with a value-based contrastive loss (\\(J(\phi)\\)) [2,
… [truncated]

### Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems [1]
`2026_AAAI_RevisitMTL_Save-Revisit-Retain.md`
**Source:** https://arxiv.org/pdf/2511.18013.pdf  
**Q2 class:** PARTIAL

### **Source Evaluation: Save, Revisit, Retain (Pinterest Framework)**
*(Jiang et al., Pinterest Inc., AAAI 2026 / arXiv: `2511.18013`)* [1]

---

### **(A) Q1 or Q2 or Both or Neither?**
* **Answer:** **Both** (Q1 and Q2) [1, 8–9, 13, 35].
* **Explanation:** 
  * **Q1 (Industry/Production Attribution 2025–2026):** **Yes.** Deployed in production on Pinterest's Related Pins surface serving **500+ million users**, with a large-scale online A/B experiment conducted from **April 29, 2025 to June 26, 2025** [1-3].
  * **Q2 (Attributing Retention / Engagement / Days-Active to In-App Interactions):** **Yes.** It establishes a surrogate attribution linkage that connects item-level save actions ("repins") on candidate items to multi-day return visits ("revisitations" on personal profiles over a 0–6 day window) as a direct proxy for 28-day active user retention [1, 5, 17, 23–25].

---

### **(B) Q2 Class**
* **Classification:** **PARTIAL** [1, 5, 10, 13, 21–25].
* **Justification:** The paper creates an item-level surrogate linkage and multi-task prediction head (\\(P(\text{revisit} \mid q, \theta)\\)) connecting content exposures/saves to 0–6 day profile revisitations and active days [5, 23–25]. It explicitly acknowledges user activity and intent confounders [1, 4], but it does **not** estimate an identified causal Multi-Touch Attribution (MTA) sequence decomposition across multiple sequential touches [5, 6].

---

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Item/Candidate-level Score Integration** (not sequence-level
… [truncated]

### Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?
`2026_CIKM_LOTUS_Meaningful-Touchpoints-Conversion-Attribution.md`
**Source:** https://arxiv.org/pdf/2608.28649.pdf  
**Q2 class:** NOT

**(A) Q1 or Q2 or both or neither?**  
**Q1 only** [1-3]. The paper (*"Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?"*, Wu et al., CIKM 2026) covers industrial production conversion attribution at Taobao & Tmall Group of Alibaba [1, 3, 4]. It does **not** cover Q2, as it focuses strictly on e-commerce purchase conversion attribution rather than user retention, engagement, or active-day attribution [2, 5, 6].

---

**(B) Q2 Class**  
**NOT** [2, 5, 6]. The paper does not publish per-touch retention or active-day credit tables; its target outcome is e-commerce product purchase conversion [2, 5, 6].

---

**(C) Does it produce per-interaction credit? For what outcome?**  
**Yes** [2, 6, 7]. It produces fractional credit weights (\\(\sum w_i = 1\\)) across selected touchpoints for **e-commerce purchase conversion events** (\\(C\\)) [6, 7]. The system operates in two stages: Stage 1 selects meaningful touchpoints (categorized as Explicit, Implicit, or Irrelevant), and Stage 2 distributes normalized credit weights across the selected touchpoints [6, 7]. It does not attribute retention or active days [5, 6].

---

**(D) How would this replace or improve last-touch N7→latest swipes?**  
Instead of using rigid last-touch rules that assign credit solely to the latest interaction, this framework uses an LLM-driven semantic selector (**LOTUS**) with pairwise prompting to inspect full behavior sequences and recover **implicitly-related touchpoints** (such as functional complementarity or scenario alignment) [3, 5-8].  
*
… [truncated]

### ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization [1]
`2026_ICLR_ALM-MTA_Front-Door-Causal-Multi-Touch-Attribution.md`
**Source:** https://arxiv.org/pdf/2605.08881.pdf  
**Q2 class:** NOT

### **Evaluation for Source: *"ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization"***
*(Liu et al., Kuaishou Technology & The University of Auckland, 2026: `arXiv:2605.08881`)* [1]

---

### **(A) Q1 or Q2 or Both or Neither?**

**Q1 only.** [1-5]
* **Q1 (Industry/Production Attribution 2025–2026):** **Yes.** Published in May 2026 (`arXiv:2605.08881`), this paper describes a production causal Multi-Touch Attribution (MTA) system deployed in real-world production at Kuaishou Technology on a recommendation engine serving **400 million Daily Active Users (DAU)** and evaluated over **30 billion training instances** [1, 4, 5].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper attributes user content consumption touchpoints to **content creation / video upload events (\\(Y \in \{0, 1\}\\))** in the "Consumption Drives Production" (CDP) ecosystem, rather than user retention, active days, or return visits [1-4].

---

### **(B) Q2 Class**

**NOT.** [1-4]
* **Justification:** The system computes causal multi-touch attribution credit for content creation / video upload conversion events (\\(Y\\)), not for user retention, active days, or revisitation [1-4].

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **Yes.** It produces a per-touchpoint causal uplift credit score [3, 6]:
  \\[\hat{\Delta}(\tau_j \mid X, T) = g_\theta(X, T) - g_\theta(X, T \setminus \{\tau_j\})\\]
  defined as the counterfactual drop in predicted upload
… [truncated]

### Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching [1]
`2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md`
**Source:** https://arxiv.org/pdf/2602.15752.pdf  
**Q2 class:** NOT

### **Evaluation for Source: *"Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching"***
*(Kishimoto et al., ICLR 2026 / arXiv: `2602.15752`)* [1–2]

---

### **(A) Q1 or Q2 or Both or Neither?**

**Neither.** [1-4]  
* **Q1 (Industry/Production Attribution 2025–2026):** **No.** While submitted in February 2026, this source is a dynamic Learning-to-Rank (LTR) matching algorithm paper evaluated in simulation, rather than an industry multi-touch attribution measurement system [1-3].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper directly optimizes real-time recommendation candidate ranking using learned retention curves \\(f(x, m)\\), but it does **not** perform historical multi-touch sequence attribution over individual user interaction logs [2, 6, 17–18].

---

### **(B) Q2 Class**

**NOT.** [2, 6, 17–18, 24]  
* **Justification:** The paper presents an LTR algorithm (**MRet**) that evaluates candidate profile matches against personalized concave retention curves \\(f(x, m)\\) during online recommendation, without publishing a per-exposure retention credit table or multi-touch attribution model [1, 2, 5, 6].

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction credit.** [1, 2, 5, 6]  
  It evaluates candidates at recommendation time using an individual lower-bound candidate score \\(\text{Score}(y)\\) derived from Jensen and concavity inequalities [18, 22–24]:
  \\[\text{Score}(y) = \frac{1}{A} f(x, m_{1:\tau}(x) +
… [truncated]

### A Human-Augmenting Agentic Workflow for Causal Inference (Netflix) — stub
`2026_NetflixBlog_oci-agent_Causal-Inference-Workflow.md`
**Source:** https://netflixtechblog.com/a-human-augmenting-agentic-workflow-for-causal-inference-4623f0a9c5af  
**Q2 class:** NOT

- **Answers:** neither Q1 MTA nor Q2 per-touch retention attribution.
- **Q2 class:** NOT — treatment-level observational CATE tooling, not credit assignment to swipes/matches.
- **Last-touch replacement:** not a substitute for per-swipe labels; at most a workflow for later incrementality tests of ranking changes.
- **Transfer rating:** low for Phase-1 labels.

**Low project relevance.**

---

### Rethinking User Retention Modeling in Recommendation [1, 2]
`2026_TOIS_IURO+_Rethinking-User-Retention-Modeling.md`
**Source:** https://dl.acm.org/doi/pdf/10.1145/3790098  
**Q2 class:** PARTIAL

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
* **Per-Interaction Credit:**
… [truncated]

### DCEO: Direct Causal Effect Optimization for Long-Term User Value Modeling in E-commerce Search [1]
`2026_arXiv_DCEO_Direct-Causal-Effect-Optimization.md`
**Source:** https://arxiv.org/html/2608.25635  
**Q2 class:** NOT

### **Source Evaluation: *DCEO: Direct Causal Effect Optimization for Long-Term User Value Modeling in E-commerce Search***
*(Zhang et al., Taobao & Tmall Group of Alibaba, arXiv:2608.25635, Aug 2026)* [1]

---

### **(A) Q1 or Q2 or Both or Neither?**

**Neither.** [2, 4, 7–8]  
* **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** While published on August 26, 2026 (`arXiv:2608.25635`) and deployed in live production at Alibaba (Taobao/Tmall), DCEO is a data-driven actor-critic framework for item-level proxy score learning in multi-objective search ranking, rather than an industry multi-touch attribution (MTA) measurement system [1–2, 5–6].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper optimizes a user-level \\(n\\)-day cumulative outcome (\\(4\\)-day cumulative GMV or purchase count) for e-commerce search, rather than attributing user retention, active days, or return visits across multi-touch interaction logs [2-5].

---

### **(B) Q2 Class**

**NOT.** [2, 5–8]  
* **Justification:** DCEO is an actor-critic multi-objective fusion framework that dynamically generates context-dependent weighting parameters (\\(\mathbf{w}_{ur}\\)) over upstream predicted scores to produce item-level proxy scores [2, 5, 19–20]. It does **not** publish or output a per-exposure retention credit table or causal multi-touch attribution model [5, 7–8].

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction sequence credit.** [3, 6, 7]
* **Target
… [truncated]

### Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning [1, 2]
`2026_arXiv_DownstreamRewards_Long-Term-Engagement-Optimization.md`
**Source:** https://arxiv.org/html/2607.14192  
**Q2 class:** NOT

### **Source Evaluation: *Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning***  
*(Wang et al., Pinterest, arXiv pre-print: `2607.14192v3`, August 21, 2026) [1]*

---

### **(A) Q1 or Q2 or Both or Neither?**
* **Neither** [3–4, 10, 21, 32–33].
* **Explanation:**
  * **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** While published in August 2026 (`arXiv:2607.14192v3`) and deployed live across multiple surfaces at Pinterest, it presents a **model-agnostic downstream reward framework** (surrogate reward learning) for candidate recommendation models rather than an industry multi-touch attribution (MTA) measurement system [2–4, 21].
  * **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** It predicts expected near-term downstream session trajectory rewards (Pin-to-Pin rabbit hole exploration, shallow closeups, new use-case adoption) at candidate ranking time [4, 7–9], rather than attributing overall retention or active days across historical user interaction logs to individual actions [10, 32–33].

---

### **(B) Q2 Class**
* **Classification:** **NOT** [2-5].
* **Justification:** It is a surrogate reward and policy optimization framework that models expected near-term downstream trajectory rewards (\\(\hat{\mathcal{R}}_{u,t}\\)) and tunes serving weights out-of-graph via HyperOPT [7–8, 21]. It does **not** generate or publish a per-exposure retention credit table [3, 5].

---

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:**
… [truncated]

### Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM [1]
`2026_arXiv_IMA_Integrated-Marketing-Attribution.md`
**Source:** https://arxiv.org/pdf/2606.16878.pdf  
**Q2 class:** NOT

### **Source Evaluation: Integrated Marketing Attribution (IMA) Framework**
*(Bhat et al., Lowe’s Companies, Inc., arXiv 2026: `2606.16878`)* [1]

---

### **(A) Query Categorization: Q1 vs. Q2**
* **Category:** **Q1 Only** (Industry/Production Attribution 2025-01 to 2026-09) [1].
* **Explanation:** Published in 2026, this paper presents an enterprise-scale production attribution architecture deployed at Lowe's Companies, Inc., built on 3 years of real-world retail marketing data [1-3]. It addresses aggregate, campaign-level marketing attribution rather than user-level retention sequence modeling.

---

### **(B) Q2 Class**
* **Classification:** **NOT**
* **Justification:** The paper explicitly rejects user-level multi-touch tracking due to privacy restrictions and third-party cookie deprecation [4, 5]. It operates entirely on aggregated, daily campaign-level media series and produces no per-interaction or per-exposure retention credit tables [6, 7].

---

### **(C) Credit Granularity and Target Outcome**
* **Per-Interaction Credit:** **No.** Credit is assigned at the **daily campaign level** (e.g., adstocked spend, impressions, or clicks for a specific campaign within a channel), not to individual user interactions or swiping events [6, 7].
* **Target Outcome:** **Daily channel-level incremental sales contribution (in dollars)** [6, 7]. This daily target is temporally disaggregated from a weekly Marketing Mix Model (MMM) that measures macro incremental sales lift [11–12].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch
… [truncated]

### Incremental Recommendation via Causal Models [1]
`2026_arXiv_NA_Incremental-Recommendation-Causal-Models.md`
**Source:** https://arxiv.org/pdf/2608.26804.pdf  
**Q2 class:** NOT

### **Source Evaluation: *Incremental Recommendation via Causal Models***
*(Vlontzos et al., Spotify & Imperial College London, 2026: `arXiv:2608.26804`)* [1]

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**
* **Neither.** [1-4]
* **Explanation:**
  * *Q1 (Industry/Production Attribution 2025-01 to 2026-09):* **No.** While published in August 2026 and evaluated in live production at Spotify on millions of users [1, 5, 6], it is an incremental recommendation targeting framework (uplift modeling) designed to prune non-incremental impressions, rather than a multi-touch attribution (MTA) measurement system [1-4].
  * *Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):* **No.** The paper predicts short direct-response stream probability \\(\hat{p}_1(\mathbf{x})\\) vs. 2-day organic stream probability \\(\hat{p}_0(\mathbf{x})\\) at recommendation serving time [5–6, 9–10], rather than attributing overall user retention, active days, or return visits to past interaction sequences [1, 3, 4].

---

### **(B) Q2 Class**
* **Classification:** **NOT** [1, 3, 4, 7]
* **Justification:** As an uplift modeling / policy optimization framework, it presents a Causal Deep Twin Network and a dual-threshold targeting policy \\(\pi(\mathbf{x}) = \mathbb{1}[\hat{p}_1(\mathbf{x}) \ge \theta_1] \cdot \mathbb{1}[\hat{p}_0(\mathbf{x}) \le \theta_0]\\) to filter out "always-takers" at serving time [3, 8], without producing a per-exposure retention credit table or causal multi-touch attribution model [1, 3, 4, 7].

---

### **(C)
… [truncated]

### Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling [1]
`2026_arXiv_OCARM_Post-Conversion-Content-Retention.md`
**Source:** https://arxiv.org/pdf/2604.25839.pdf  
**Q2 class:** NOT

### **Source Evaluation: OCARM (*Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling*)**
*(Ma et al., Kuaishou Technology, 2026: `arXiv:2604.25839`)* [1]

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**

* **Neither.** [1, 2]
* **Explanation:**
  * **Q1 (Industry/Production Attribution 2025–2026):** **No.** While published on arXiv in April 2026 (`arXiv:2604.25839`) and deployed in a live Real-Time Bidding (RTB) ad system [1, 3], OCARM is a predictive representation distillation framework for bidding decisions [1, 4], not a multi-touch attribution (MTA) measurement system.
  * **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** It forecasts future user revisit frequency (\\(LT_d\\), e.g., \\(LT1\\), \\(LT7\\)) prior to app conversion [2, 5], rather than performing historical multi-touch sequence attribution over individual past swiping or messaging interactions [4, 5].

---

### **(B) Q2 Class**

* **Classification:** **NOT** [8, 15–20]
* **Justification:** OCARM is a predictive representation model that trains a student user encoder (Sequence Fusion Encoder, SFE) to align with a frozen teacher content encoder (Hierarchical Attention Encoder, HAE) via representation distillation (\\(L_{\text{align}}\\)) [8, 18–20]. It does **not** publish a per-exposure or per-swipe retention credit table or multi-touch attribution model [4, 5].

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction credit.**
… [truncated]

