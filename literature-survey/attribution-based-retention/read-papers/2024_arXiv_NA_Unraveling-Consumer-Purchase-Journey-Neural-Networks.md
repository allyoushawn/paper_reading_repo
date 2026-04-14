# Paper Analysis: Unraveling Consumer Purchase Journey Using Neural Network Models

**Source:** https://arxiv.org/pdf/2404.07098.pdf  
**Date analyzed:** 2026-04-14 (NLM batch 2026-04-14; three `notebook_query` calls on source `52dc09e5-3135-4632-8145-acbcbf64f56e` only)

---

## 1. Summary

**Title:** Unraveling Consumer Purchase Journey Using Neural Network Models  
**Authors:** Victor Churchill (Trinity College); H. Alice Li, Dongbin Xiu (The Ohio State University)  
**Abstract:** Models **31-dimensional** vectors of **aggregated marketing touchpoint counts** over a lookback window \(T\) to predict **binary purchase**. Uses an **ensemble of \(K=10\)** shallow feedforward nets (best config: **3 hidden layers × 10 nodes**, sigmoid activations, **551** trainable parameters) with outputs averaged then thresholded by maximizing **balanced accuracy** on validation data. On a **proprietary** multinational software-provider sample (**20,556 users**, June 2018–Sept 2021; **11.8%** buyers), the ensemble beats logistic regression, naive Bayes, kNN, bagging, random forest, AdaBoost, and gradient boosting (each ensemble-limited to 10 base models for fairness). **SHAP** implements Shapley-style explanations of the ensemble over touchpoint types. Shortening lookback from **40 months to 1 month** yields only ~**19%** relative drop in AUROC / balanced accuracy while cutting storage ~**97.5%**.

**Key contributions:**
- Demonstrates compact MLP ensemble on **tabular touch counts** without hand-built POE/AIDA buckets.
- Shapley/SHAP analysis at **touchpoint-type** level plus **within-type** impact distributions (beeswarm plots).
- Empirical robustness to **short lookback** vs classical and tree ensembles.

**Methodology:** 80/10/10 train/val/test split; Adam on **BCE** for **10,000** epochs at LR \(10^{-3}\); architecture sweep (Table 2); threshold \(\tau^*\) from balanced accuracy on validation.

**Main results (40-month window):** AUROC **0.838**, balanced accuracy **0.776**, TPR **0.782**, TNR **0.770** (best among compared models). **1-month window:** AUROC **0.675**, balanced accuracy **0.630**—still best among baselines in paper’s Table 4.

---

## 2. Experiment Critique

**Design:** Single-industry proprietary logs—strong internal validity, unclear external validity.

**Statistical validity:** Class imbalance handled via balanced accuracy / focal variants tested; primary model BCE on raw counts.

**Online experiments (if any):** Not specified in source.

**Reproducibility:** **Not reproducible** from public artifacts—dataset proprietary; method is standard deep-learning stack if features were released.

**Overall:** Solid applied ML + interpretability; **Shapley values explain the fitted predictor**, not guaranteed causal incrementality without additional identification.

---

## 3. Industry Contribution

**Deployability:** Blueprint for firms with rich touch logs: count-vectorization + compact MLP + SHAP dashboards.

**Problems solved:** Managerially legible **touchpoint-type importance** under nonlinearity vs rigid taxonomies.

**Engineering cost:** Moderate feature engineering (31 channels); 10× ensemble increases training cost linearly.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** NN + Shapley on **tabular touchpoint counts** where prior work often uses hand-staged funnels or classical GLMs; extends attribution-style discussion beyond Li & Kannan (2014) / Kireyev et al. (2016) by showing **distributions within types**.

**Prior work comparison:** Contrasts with predefined AIDA / paid-owned-earned splits and with NN successes mostly on unstructured media.

**Verification:** Empirical superiority is dataset-specific; Shapley attributions are **model-dependent**.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Proprietary B2B software touch + purchase logs | Not public | No | 31 touch types; 40-month vs 1-month lookback experiments |

**Offline experiment reproducibility:** Methodology only.

---

## 6. Community Reaction

No significant community discussion found (recent arXiv stat.AP preprint).

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|------------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Victor Churchill; H. Alice Li; Dongbin Xiu  
**Affiliations:** Trinity College; The Ohio State University  
**Venue:** arXiv (stat.AP)  
**Year:** 2024  
**PDF:** https://arxiv.org/pdf/2404.07098.pdf  
**Relevance:** Core  
**Priority:** 3  
**NLM:** `nlm:52dc09e5-3135-4632-8145-acbcbf64f56e`

---

## Project Relevance

**Phase 1 label generation:** Inputs are **type-level counts**, not a full ordered event sequence; SHAP values are **per feature (touch type)**, so they are **coarse fractional signals** (e.g., allocate type-level SHAP across events only via an **ad hoc** normalization—**not specified in source**). The head is **binary purchase**, not **user-days-active**; swapping to regression + SHAP is a **plausible engineering analog** but outside the paper’s evaluated claims. **Selection bias** (active users accumulate more touches) is **not** addressed—the model is trained for predictive accuracy, not causal debiasing.

**Transferable pieces:** Short lookback + count featurization for **compute scaling**; SHAP-on-ensemble as a **pattern** for turning a joint predictor into **importance weights**—best paired with **causal MTA** or propensity-aware methods from the rest of the survey when used as supervision.
