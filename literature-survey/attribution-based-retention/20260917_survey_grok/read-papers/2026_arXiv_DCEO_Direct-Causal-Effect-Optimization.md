# DCEO: Direct Causal Effect Optimization for Long-Term User Value Modeling in E-commerce Search [1]

**Source:** https://arxiv.org/html/2608.25635  
**Date analyzed:** 2026-09-18  
**NLM source id:** `d18bf088-6fb0-4082-952c-2a13f61ffc2e`  
**Queue id:** G24  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**
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
* **Target Outcome:** **User-Level Long-Term Objective (\\(Y_u\\))** accumulated over an \\(n\\)-day outcome window (specifically 4-day cumulative GMV or purchase count per user) [2, 4, 5, 8].
* **Mechanics:** The actor model (\\(f_\theta\\)) predicts request-specific fusion weights (\\(\mathbf{w}_{ur}\\)) over \\(M\\) selected upstream predicted scores (\\(\mathbf{v}_{uri}\\)) to calculate item proxy scores \\(p_{uri}(\theta) = \sum_{m=1}^M w_{ur}^m v_{uri}^m\\) [19–20]. These scores are aggregated into a calibrated user-level proxy metric \\(P_u(\theta)\\) and evaluated by a critic model (\\(h_\phi\\)) under a relative intervention (\\((1+\delta)P_u\\)) to optimize Relative Causal Effect (RCE) [5, 15–17, 20–21].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**

* **How it Improves on Last-Touch:** Last-touch heuristically assigns 100% of an \\(N7\\) retention label to recent swipes post-hoc, ignoring baseline activity and failing to distinguish predictive correlation from true causal impact [3–4, 12]. DCEO replaces post-hoc last-touch attribution by learning context-dependent fusion weights (\\(\mathbf{w}_{ur}\\)) at request time that directly maximize the **relative causal effect** of candidate profile scores on long-term user retention (\\(Y_u\\)) [4–5, 15–16].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Candidate Profile Request:* Triggered when a user requests a batch/deck of candidate profiles to swipe.
  2. *Upstream Predictions (\\(\mathbf{v}_{uri}\\)):* Multiple candidate profile score heads (e.g., predicted swipe-right, predicted match, predicted 10-message conversation, predicted profile duration) [5, 9, 10].
  3. *Actor Fusion (\\(f_\theta\\)):* Predicts request-specific weights (\\(\mathbf{w}_{ur}\\)) based on user features (\\(\mathbf{z}_u\\)) and request context (\\(\mathbf{z}_{ur}\\)) to construct an item-level proxy score \\(p_{uri}\\) [19–20].
  4. *Calibrated Aggregation & Causal Critic (\\(P_u \to h_\phi\\)):* Aggregates item proxy scores across a user's swiping session, calibrates them to a reference impression count (\\(C=100\\)), and uses a critic model (\\(h_\phi\\)) to evaluate the causal effect of increasing the proxy metric on \\(n\\)-day retention (\\(Y_u\\)), prioritizing profiles that causally drive retention rather than superficial swipes [5, 14–17, 20–21].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Calibrated User-Level Aggregation (\\(g_\psi\\)):** Calibrates the daily user proxy score \\(\hat{p}_u\\) to a fixed reference impression count (\\(C=100\\)), removing impression-count bias caused by ranking-induced user activity expansion [7, 11, 12].
2. **Conditional Normalized Ranking Loss (\\(\mathcal{L}_{\text{CNR}}\\)):** Uses a normalization network \\(e_\zeta(\mathbf{z}_u)\\) to predict conditional mean and variance \\((\mu_P, \mu_Y, \sigma_P, \sigma_Y)\\) based on user baseline features \\(\mathbf{z}_u\\), normalizing proxy metrics and outcome labels before applying pairwise Bradley–Terry ranking loss [17, 23–24].
3. **Relative Causal Effect Optimization (\\(\mathcal{L}_{\text{CE}}\\)):** Evaluates outcome changes under a relative intervention \\((1+\delta)P_u(\theta)\\) vs. \\(P_u(\theta)\\) (\\(\delta = 0.05\\)), isolating incremental causal lift over baseline user expectations [5, 13, 14].

---

### **(F) Deployment and Production Dataset Evidence**

* **Production Deployment:** Fully deployed in live production on Taobao/Tmall's large-scale e-commerce search engine serving hundreds of millions of users, evaluated in a **41-day online A/B test** [2, 8, 15].
* **Offline Dataset:** Industrial search logs from Taobao/Tmall. Trained on **14 consecutive days** of search logs and evaluated on the **15th day** [5].
* **Quoted Numbers from the Source:**
  * **Online A/B Test (41-day test vs. conventional GMV proxy, Table 8):**
    * **GMV Lift:** **+0.36%** relative gain over control [2, 8, 16].
    * **Click Count Lift:** **+0.36%** relative gain over control [16].
    * **Purchase Count Lift:** **+0.12%** relative gain over control [16].
  * **Offline Relative Causal Effect (RCE, Table 3 & Section 5.3):**
    * *Predictive Association Optimization:* **RCE = 0.022** [17].
    * *Causal Effect Loss (\\(\mathcal{L}_{\text{CE}}\\) alone):* **RCE = 0.031** [17].
    * *Full DCEO (\\(\mathcal{L}_{\text{actor}} = \mathcal{L}_{\text{CE}} + \alpha \mathcal{L}_{\text{CNR}}\\)):* **RCE = 0.053** (**2.41x improvement** over predictive association optimization) [17, 18].
  * **Upstream Score Set Ablations (Table 5):**
    * `impr2gmv` only: **RCE = 0.027** [31–32].
    * Basic impression-level set: **RCE = 0.039** [31–32].
    * Conversion-funnel set: **RCE = 0.040** [31–32].
    * Value-aware set: **RCE = 0.041** [31–32].
    * Full 17-score set: **RCE = 0.053** [31–32].
  * **Objective Sensitivity Mean Actor Weights (Table 6):**
    * *4-day Click Count Objective:* `impr2click` weight = **0.999** [19, 20].
    * *4-day Purchase Count Objective:* `impr2click` = **0.531**, `click2pay` = **0.101**, `click2pay10` = **0.256** [19, 20].
    * *4-day GMV Objective:* `impr2click` = **0.404**, `click2pay` = **0.032**, `click2pay10` = **0.154**, `click2pay30` = **0.079**, `click2pay100` = **0.105**, `click2pay1000` = **0.205** [19, 20].
  * **Hyperparameters:** Reference impression count \\(C = 100\\), relative intervention \\(\delta = 0.05\\), ranking loss weight \\(\alpha = 0.3\\) [5].

---

💡 *Would you like to explore how DCEO's actor-critic relative causal effect loss (\\(\mathcal{L}_{\text{CE}}\\)) or calibrated user-level aggregation could be adapted to optimize candidate profile fusion weights for your dating app?*

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
**Priority:** see queue.md `G24`
