# Generalized position-based model: Rethinking position weights in ranking off-policy evaluation [1]

**Source:** https://www.amazon.science/publications/generalized-position-based-model-rethinking-position-weights-in-ranking-off-policy-evaluation  
**Date analyzed:** 2026-09-24  
**NLM source id:** `9473661a-49fd-4ede-9ff0-ba2c686cf56f`  
**Queue id:** G38  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Generalized position-based model: Rethinking position weights in ranking off-policy evaluation* [1]
* **Authors:** **Norman Knyazev**, **Vito Bellini**, **Huseyin Yurtseven**, and **Ben London** [1]
* **Affiliations:** **Amazon** (**Amazon Music**) [1, 2]
* **Year:** **2026** [1]
* **Venue:** 20th ACM Conference on Recommender Systems (**RecSys 2026**) [1, 2]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Off-policy evaluation (OPE) estimates the performance of new recommendation policies using historical logged data to enable fast, safe iteration before running online A/B tests [1]. Existing ranking OPE estimators make rigid structural assumptions about user behavior, leading to trade-offs between bias and variance [1]. While the recently proposed **INTERPOL** estimator navigates these trade-offs via a window system that combines clicks across different positions, INTERPOL suffers from two key drawbacks:
  1. The window configuration must be specified *a priori*, creating hyperparameter selection friction [1].
  2. Positions within a window are weighted uniformly, ignoring relative position utility and limiting estimation accuracy [1].
* **Key Contribution:** Proposes **Generalized PBM (GPBM)**, an OPE estimator that learns position-specific weights by minimizing an approximate upper bound on the estimation error [1]. GPBM retains INTERPOL's unbiasedness guarantees while simplifying hyperparameter tuning and improving accuracy/robustness across position bias misestimation levels, logging policies, and dataset scales [1].

---

### **(3) Proposed Method or Architecture in Detail**
* **Estimation Framework:** GPBM generalizes the Position-Based Model (PBM) for ranking off-policy evaluation [1]. Rather than applying uniform weights within fixed manual windows (like INTERPOL), GPBM learns position-specific weights directly by minimizing an approximate upper bound on estimation error [1].
* **Credit Assignment Mechanics:** GPBM assigns learned position-specific weighting parameters to user click interactions occurring at different positions in ranked lists during off-policy policy evaluation [1]. It does **not** perform multi-touch sequence attribution or assign credit across historical user interaction touchpoints (e.g., swipes, matches, messages) for conversion or retention modeling [1].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets:** Not specified in source (landing page states that experiments evaluate varying data sizes, logging policies, and position bias misestimation levels, but specific dataset names are omitted from the abstract) [1].
* **Production Deployment:** Not specified in source (tagged under Amazon Music) [1, 2].
* **Comparison Baselines:** **INTERPOL** (and general existing ranking OPE estimators) [1].

---

### **(5) Key Quantitative Results with Numbers**
* **Not specified in source.** (The landing page abstract notes qualitative improvements—that GPBM provides "more accurate and robust estimates across a wide range of position bias misestimation levels, logging policies, and data sizes"—but specific numerical metrics, percentages, or tables are not included on the landing page) [1].

---

### **(6) Limitations, Failure Modes, or Negative Results**
* **Not specified in source.** (Note: The landing page explicitly states that the full PDF text was not publicly posted on the landing page) [1].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**
* **INTERPOL** (explicitly named in the abstract as the direct precursor OPE estimator) [1].
* *Other specific prior work citations are not specified in source.*

---

💡 *Would you like to discuss how position-bias correction mechanisms from Position-Based Models (PBM) apply to off-policy evaluation of your dating app's candidate profile ranker?*

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

### **Evaluation of *Generalized position-based model: Rethinking position weights in ranking off-policy evaluation* (GPBM)**  
*(Norman Knyazev, Vito Bellini, Huseyin Yurtseven, & Ben London, Amazon / Amazon Music, RecSys 2026)* [1]

---

### **(A) Q1 or Q2 or Both or Neither?**

**Neither.** [1]  
* **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** While accepted at RecSys 2026 and authored by researchers at Amazon/Amazon Music, GPBM is an **off-policy evaluation (OPE) estimator for ranking policies**, not an industry multi-touch attribution (MTA) measurement system [1].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** GPBM estimates the offline performance of new recommendation ranking policies using historical logged data by learning position-specific weights to correct for position bias, rather than attributing overall retention or active days back to individual interaction touchpoints across user logs [1].

---

### **(B) Q2 Class**

**NOT.** [1]  
* **Justification:** GPBM is an off-policy evaluation (OPE) estimator for ranking recommender systems [1]. It does **not** produce or publish a per-exposure retention credit table.

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction sequence attribution credit table.** [1]
* **Target Outcome:** **Ranking Off-Policy Evaluation (OPE) Policy Value Estimation** (offline estimation of the expected reward or click performance of a new target ranking policy \\(\pi\\) using historical logged data generated by a logging policy \\(\mu\\)) [1].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**

* **How it Improves/Informs Ranking/Evaluation:** GPBM does **not** provide a post-hoc attribution credit model to replace last-touch N7 [1]. However, it offers a crucial tool for **offline evaluation of candidate profile rankers** before running online A/B tests:
  1. *Position Bias Correction in Offline Evaluation:* When evaluating a new profile recommendation algorithm offline using logged swipe data, top-positioned profiles receive more swipes simply due to display location (position bias) [1]. Standard OPE estimators suffer from severe bias/variance trade-offs or rely on manual window setups (like INTERPOL) that weight positions uniformly [1].
  2. *Adaptive Position Weighting:* GPBM learns position-specific weights by minimizing an approximate upper bound on estimation error, providing more accurate and robust offline policy evaluation without manual hyperparameter tuning [1].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  * **Logged Swipe Data (Logging Policy \\(\mu\\)):** Historical logs of displayed profile cards, screen positions, and user swipes [1].
  * **Candidate Ranker (Target Policy \\(\pi\\)):** A new candidate profile ranking policy to be evaluated offline [1].
  * **GPBM OPE Estimator:** Applies learned position-specific weights across list positions to estimate how the new candidate ranker would perform prior to live A/B deployment [1].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Addresses Position Bias & Off-Policy Logging Shift:** Corrects for position-dependent presentation bias in logged ranking data during offline policy evaluation [1].
2. **Optimal Error Bound Minimization:** Learns position-specific weights by minimizing an approximate upper bound on estimation error, retaining the unbiasedness guarantees of INTERPOL while eliminating manual window selection [1].

---

### **(F) Deployed or Production Dataset Evidence**

* **Production Deployment:** **Not specified in source** (tagged under Amazon / Amazon Music) [1, 2].
* **Quoted Numbers from Source:** **Not specified in source** (the Amazon Science publication landing page provides a qualitative summary noting that GPBM achieves *"more accurate and robust estimates across a wide range of position bias misestimation levels, logging policies, and data sizes"*, but specific numerical tables and metrics are omitted because the full PDF was not publicly posted on the page) [1].

---

💡 *Would you like to discuss how position-bias correction mechanisms from Position-Based Models (PBM) apply to off-policy evaluation of your dating app's candidate profile ranker?*

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
**Priority:** see queue.md `G38`
