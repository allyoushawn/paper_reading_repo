# Incremental Recommendation via Causal Models [1]

**Source:** https://arxiv.org/pdf/2608.26804.pdf  
**Date analyzed:** 2026-09-18  
**NLM source id:** `15cdd352-b889-48d8-a3d5-4bdabefd67f8`  
**Queue id:** G18  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Incremental Recommendation via Causal Models* [1]
* **Authors:** **Athanasios Vlontzos**\*¹, **David Gustafsson**², **Michael O’Riordan**³, and **Ciarán M. Gilligan-Lee**⁴ (\*Work done while at Spotify) [1, 2]
* **Author Affiliations:**
  1. **Imperial College London / Hologen**, London, UK (`Hologen Imperial College London, UK`) [1]
  2. **Spotify**, Stockholm, Sweden (`davidgustafsson@spotify.com`) [1]
  3. **Spotify**, London, UK (`moriordan@spotify.com`) [1]
  4. **Spotify** (Ireland) & **University College London**, London, UK (`ciaranl@spotify.com`) [1]
* **Year:** **2026** (arXiv pre-print: `2608.26804`) [1, 3]
* **Venue:** arXiv pre-print (`arXiv:2608.26804`) / Conference pre-print [1]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Recommendation impressions are a finite resource. Delivering recommendations to users who would discover the content organically yields no incremental value and displaces other recommendations that could [1]. While platforms collect holdback data (withholding recommendations from a small randomized fraction of users), a fundamental structural obstacle prevents naive Conditional Average Treatment Effect (CATE) subtraction (\\(\hat{p}_1(\mathbf{x}) - \hat{p}_0(\mathbf{x})\\)): **Attribution Window Mismatch** [1, 5–7]. 
  * Treated users are attributed streams within a **short direct-response window** (minutes/hours) to isolate immediate exposure effects [5–6].
  * Holdback users are attributed organic streams over a **multi-day window (2-day window)** to capture slower organic discovery [4].
  * Naive subtraction (\\(\hat{p}_1 - \hat{p}_0\\)) is mathematically invalid because the two heads measure fundamentally different outcome definitions [5].
* **Key Contribution:**
  1. **Formalization of Attribution Window Mismatch:** Identifies and formalizes why direct CATE estimation fails when treated and control attribution windows differ [3, 5–7].
  2. **Deep Twin Network Extension:** Extends an existing multi-task production recommendation architecture into a Causal Deep Twin Network [6] by adding a holdback head trained on holdback data \\(\mathcal{D}_0\\) with partitioned losses [10–12].
  3. **Dual-Threshold Targeting Policy:** Introduces a policy \\(\pi(\mathbf{x}) = \mathbb{1}[\hat{p}_1(\mathbf{x}) \ge \theta_1] \cdot \mathbb{1}[\hat{p}_0(\mathbf{x}) \le \theta_0]\\) that uses both predicted probabilities as independent decision levers, targeting only users where recommendations are both effective (high \\(\hat{p}_1\\)) and necessary (low \\(\hat{p}_0\\)) [3, 13–14].
  4. **Production A/B Test Validation:** Demonstrates a **7% reduction in recommendation impressions** on millions of Spotify users with no statistically significant impact on recommended content consumption [1, 7, 8].
  5. **Generalization & Calibration Lifts:** Proves joint training with holdback supervision improves model calibration on the treated head [1, 3, 19–22].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Architectural Components**
* **Baseline Production Model:** Multi-task shared-trunk neural network mapped from (user, content) feature vector \\(\mathbf{x}\\) to shared representation \\(\mathbf{z}\\). Task heads predict engagement outcomes (streams, likes) exclusively from treated data \\(\mathcal{D}_1\\) [9–10].
* **Causal Deep Twin Network:** Retains the deep shared trunk and appends a holdback head trained on randomized holdback examples \\(\mathcal{D}_0\\) to predict organic stream probability \\(\hat{p}_0(\mathbf{x})\\) [10–11].
* **Partitioned Loss Function:**
  \\[\mathcal{L} = \frac{1}{|\mathcal{D}_1|} \sum_{i \in \mathcal{D}_1} \ell_{\text{bce}}(y_i, \hat{p}_1(\mathbf{x}_i)) + \frac{1}{|\mathcal{D}_0|} \sum_{j \in \mathcal{D}_0} \ell_{\text{bce}}(y_j, \hat{p}_0(\mathbf{x}_j))\\]
  Gradients from both treated and holdback arms flow back to shape the shared trunk \\(\mathbf{z}\\), but treated examples update *only* the treated head and holdback examples update *only* the holdback head [11–12].

#### **Dual-Threshold Targeting Policy**
* A recommendation is served if and only if [9]:
  \\[\pi(\mathbf{x}) = \mathbb{1}[\hat{p}_1(\mathbf{x}) \ge \theta_1] \cdot \mathbb{1}[\hat{p}_0(\mathbf{x}) \le \theta_0]\\]
  * \\(\theta_1\\): Threshold ensuring the recommendation is likely to drive a direct stream [9].
  * \\(\theta_0\\): Threshold filtering out "always-takers" who would stream organically regardless [9].

#### **Credit Assignment Mechanics**
* Credit is assigned to **individual candidate recommendation impressions** at serving time by evaluating short-window direct stream probability \\(\hat{p}_1(\mathbf{x})\\) against multi-day organic stream probability \\(\hat{p}_0(\mathbf{x})\\) [9, 10].
* It does **not** perform multi-touch sequence attribution over historical user touchpoints; rather, it uses counterfactual holdback prediction to prune non-incremental recommendations [2, 9, 11].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets & Scale:** Live production user interaction logs from Spotify, utilizing routine holdback infrastructure where recommendations are withheld from a small randomized fraction of eligible users [1–2].
* **Production Deployment:** Deployed live in production at **Spotify** on mobile and desktop recommendation surfaces, evaluated over a two-week A/B test on millions of users [1, 6, 12].
* **Comparison Baselines / Variants:**
  * **Production Baseline:** Multi-task shared-trunk model trained solely on treated examples \\(\mathcal{D}_1\\), targeting by \\(\mathbb{1}[\hat{p}_1(\mathbf{x}) \ge \theta_1]\\) [6, 10, 13].
  * **Treatment-Model:** Causal Deep Twin architecture model, but filtering using only the treated head \\(\mathbb{1}[\hat{p}_1(\mathbf{x}) \ge \theta_1]\\) (isolating the shared trunk representation effect) [6].
  * **Treatment-Causal:** Full Causal Deep Twin model with the Dual-Threshold Policy (\\(\mathbb{1}[\hat{p}_1(\mathbf{x}) \ge \theta_1] \cdot \mathbb{1}[\hat{p}_0(\mathbf{x}) \le \theta_0]\\)) [6].

---

### **(5) Key Quantitative Results with Numbers**

* **Live Production A/B Test (Treatment-Causal vs. Treatment-Model over 2 weeks, Table 1):**
  * **Recommendation Impressions per user:** **-7.1%** (`[-7.2%, -6.9%]`, 95% CI) — achieving a **7% reduction** in recommendation slot usage [8].
  * **Recommended Content Consumption Minutes:** **-0.37%** (`[-0.86%, +0.21%]`, 95% CI) — **no statistically significant reduction** in overall consumption of recommended content or user satisfaction guardrails [8].
* **Backend vs. Client-Side Discrepancy:** Identified an approximate **30% discrepancy** between backend recommendation servings (holdback log events) and client-side impressions (treated log events) due to network latency and client-side rendering differences [14].
* **Model Calibration Improvement:** The causal treated head tracked the diagonal calibration line noticeably closer than the production baseline, particularly at higher predicted probabilities (Figure 4) [19–20].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Failure of Direct CATE Subtraction (\\(\hat{p}_1 - \hat{p}_0\\)):** Direct subtraction fails and provides no valid causal interpretation due to the attribution window mismatch (short direct-response window for treated vs. 2-day organic window for holdback) [5].
2. **Distributional Gap Between Backend and Client Logs:** The **~30% discrepancy** between backend recommendation servings and client-side impressions creates additional feature space divergence between \\(\mathcal{D}_1\\) and \\(\mathcal{D}_0\\) [14].
3. **Threshold Sensitivity Trade-Off:** Aggressively decreasing \\(\theta_0\\) saves more impressions but risks withholding recommendations from users who might have provided incremental streams [15].
4. **Prerequisite of Holdback Infrastructure:** Requires access to continuous randomized holdback experiment data; platforms without existing holdback infrastructures cannot train the holdback head [2].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Shalit, Johansson, & Sontag (2017) [Ref 15]:** *Estimating individual treatment effect: generalization bounds and algorithms* (TARNet / CFR) [16, 17].
2. **Shi, Blei, & Veitch (2019) / DragonNet [Ref 16]:** *Adapting Neural Networks for the Estimation of Treatment Effects* [16-18].
3. **Deep Twin Networks [Ref 17]:** *Deep Twin Networks for CATE Estimation* [16, 17, 19].
4. **Ma et al. (2018) [Ref 11 / ESSM]:** *Entire Space Multi-Task Model: An Effective Approach for Estimating Post-Click Conversion Rate* [10, 20].
5. **Schnabel et al. (2016) [Ref 14]:** *Recommendations as Treatments: Debiasing Learning and Evaluation* [11, 17].
6. **Rubin (1974) [Ref 13]:** *Estimating causal effects of treatments in randomized and nonrandomized studies* (Potential Outcomes Framework) [12, 17].
7. **Gutierrez & Gérardy (2017) [Ref 9]:** *Causal Inference and Uplift Modeling: A Review of the Literature* [16, 21].

---

💡 *Would you like to explore how Spotify's dual-threshold policy (\\(\pi(\mathbf{x})\\)) or holdback Deep Twin Network architecture could be adapted to prune non-incremental candidate profile impressions for your dating platform?*

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

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction credit.** [1, 3, 7]
* **Target Outcome:** At recommendation candidate serving time, the model outputs two separate stream probability scores for a candidate item \\(\mathbf{x}\\) [9–10, 13]:
  1. **\\(\hat{p}_1(\mathbf{x})\\) (Treated Stream Probability):** Probability of a stream occurring within a **short direct-response window (minutes to hours)** when recommended [2, 9].
  2. **\\(\hat{p}_0(\mathbf{x})\\) (Holdback Organic Stream Probability):** Probability of an organic stream occurring within a **two-day window** when withheld [10, 11].
* It does not calculate fractional credit across past multi-touch user interaction sequences [1, 3, 7].

---

### **(D) Replacing Last-Touch N7 → Latest Swipes**
* **How it Improves on Last-Touch:** Last-touch post-hoc rules assign 100% of a downstream outcome to recent interactions, ignoring organic baseline engagement and "always-takers" (users who would engage regardless) [1–2]. This paper replaces post-hoc last-touch attribution with a **counterfactual dual-threshold targeting policy** \\(\pi(\mathbf{x}) = \mathbb{1}[\hat{p}_1(\mathbf{x}) \ge \theta_1] \cdot \mathbb{1}[\hat{p}_0(\mathbf{x}) \le \theta_0]\\) at candidate recommendation time [1, 3]. It explicitly models what the user would have done organically without the recommendation [3, 12].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Candidate Profile Impression (\\(\mathbf{x}\\)):* Evaluates whether presenting a specific profile card will drive an incremental right-swipe/match [9, 13].
  2. *Treated Stream Head (\\(\hat{p}_1(\mathbf{x})\\)):* Predicts the probability of an immediate right-swipe or match within a short direct-response window (e.g., minutes/hours of profile exposure) [2, 9].
  3. *Holdback Organic Head (\\(\hat{p}_0(\mathbf{x})\\)):* Predicts the organic probability that the user would discover, match, or converse with this user organically over a multi-day window (e.g., 2 days) through organic search or browse surfaces [10, 11].
  4. *Pruning Non-Incremental Swipes (\\(\theta_0\\)):* Filters out profile recommendations where \\(\hat{p}_0(\mathbf{x}) > \theta_0\\) (users who would organically discover/match anyway), saving scarce recommendation slots for profiles where recommendations are both effective (\\(\hat{p}_1(\mathbf{x}) \ge \theta_1\\)) and necessary (\\(\hat{p}_0(\mathbf{x}) \le \theta_0\\)) [1, 13–14].

---

### **(E) Selection-Bias & Confounding Handling**
1. **Randomized Holdback Experiments (\\(\mathcal{D}_0\\)):** Utilizes routine holdback randomized experiments where recommendations are withheld from a small randomized fraction of eligible users, providing unconfounded samples from the counterfactual organic distribution \\(Y(0)\\) [1–2, 10–11].
2. **Partitioned Loss Function:** Trains the Deep Twin Network using partitioned binary cross-entropy loss [11–12]:
   \\[\mathcal{L} = \frac{1}{|\mathcal{D}_1|} \sum_{i \in \mathcal{D}_1} \ell_{\text{bce}}(y_i, \hat{p}_1(\mathbf{x}_i)) + \frac{1}{|\mathcal{D}_0|} \sum_{j \in \mathcal{D}_0} \ell_{\text{bce}}(y_j, \hat{p}_0(\mathbf{x}_j)) \quad \text{[14]}\\]
   where treated examples update *only* the treated head (\\(\hat{p}_1\\)) and holdback examples update *only* the holdback head (\\(\hat{p}_0\\)), while both update the deep shared trunk \\(\mathbf{z}\\) [11–12]. This prevents conflating the different temporal attribution windows (minutes/hours vs. 2 days) [7, 14].
3. **Handling Mismatch & Backend-Client Discrepancies:** Acknowledges an approximate **30% discrepancy** between backend recommendation servings (holdback log events \\(\mathcal{D}_0\\)) and client-side impressions (treated log events \\(\mathcal{D}_1\\)) due to latency and client-side rendering [15]. The dual-threshold policy avoids naive subtraction \\(\hat{p}_1(\mathbf{x}) - \hat{p}_0(\mathbf{x})\\) (which is mathematically invalid due to window mismatch and distributional differences) and instead treats the two scores as independent binary decision levers [7–8, 13].

---

### **(F) Deployment and Production Dataset Evidence**
* **Production Deployment:** Deployed live in production at **Spotify** on mobile and desktop recommendation surfaces across a 2-week A/B test on millions of users [1, 3–4, 17–18].
* **Quoted Numbers from the Source:**
  * **Recommendation Impressions Reduction:** **-7.1%** (`[-7.2%, -6.9%]`, 95% CI) reduction in recommendation impressions per user [1, 16].
  * **Recommended Content Consumption:** **-0.37%** (`[-0.86%, +0.21%]`, 95% CI) — **no statistically significant reduction** in overall consumption of recommended content or listener satisfaction guardrails [1, 16].
  * **Backend vs. Client-Side Discrepancy:** Approximately **30% discrepancy** between backend recommendation servings (holdback log events) and client-side impressions (treated log events) [15].
  * **Temporal Attribution Windows:** Treated streams are attributed within a **short direct-response window (on the order of minutes to hours)**; holdback organic streams are attributed within a **two-day window** [5–6].

---

💡 *Would you like to explore how Spotify's dual-threshold policy (\\(\pi(\mathbf{x})\\)) or holdback Deep Twin Network architecture could be adapted to prune non-incremental candidate profile impressions for your dating platform?*

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
**Priority:** see queue.md `G18`
