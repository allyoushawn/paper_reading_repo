# Paper Analysis: Summary Reports Optimization in the Privacy Sandbox Attribution Reporting API

**Source:** https://arxiv.org/pdf/2311.13586.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Summary Reports Optimization in the Privacy Sandbox Attribution Reporting API  
**Authors:** Hidayet Aksu, Badih Ghazi, Pritish Kamath, Ravi Kumar, Pasin Manurangsi, Adam Sealfon, Avinash V Varadarajan  
**Abstract:**  
Chrome’s Attribution Reporting API enforces contribution bounding and discrete Laplace noise for $\varepsilon$-DP summary reports. The paper defines a utility objective (thresholded RMS relative error, $\mathrm{RMSRE}_\tau$), fits count limits, per-query clipping, and budget fractions using historical (pre-DP) data, and shows large error reductions vs equal-budget baselines on real and synthetic conversion data, with a generalization bound (Theorem 6.1).

**Key contributions:**
- Formal optimization model for ARA summary-report parameters under API constraints.
- Argument for $\mathrm{RMSRE}_\tau$ as the operational metric vs alternatives.
- Algorithms (e.g., scipy-based enumeration/convex subproblems) and empirical gains across $\varepsilon \in \{1,\dots,64\}$; $\ell_1$ variant helps on some real-estate/travel slices.

**Methodology:**  
Bias–variance decomposition of per-slice error; train on historical slices, evaluate on held-out time or synthetic draws; compare to baselines with equal $\alpha_\ell$.

**Main results:**  
Figure 5 (paper): optimization dominates baselines across privacy budgets on three real and three synthetic datasets; Theorem 6.1 links historical threshold choice to population optimal clipping.

---

## 2. Experiment Critique

**Design:**  
Real: Criteo sponsored-search conversion log; two ad-tech proprietary slices (real estate, travel). Synthetic: three generative models with parameters in Table 3. Timestamp train/test split for real data; $C=1$ for real data due to available granularity.

**Statistical validity:**  
$\mathrm{RMSRE}_\tau$ with $\tau_\ell$ tied to training medians; generalization theory in simplified setting; non-convexity in joint $(C_\ell,\alpha_\ell)$ noted.

**Online or field experiments if any:**  
Claims API deployed at scale (Chrome); no controlled A/B described in reviewed excerpts.

**Reproducibility:**  
Criteo traceability via cited IEEE BigData paper; synthetic parameters in Table 3; explicit public code URL not specified in source.

**Overall:**  
Strong engineering-measurement contribution for DP aggregates; not a user-journey attribution learner.

---

## 3. Industry Contribution

**Deployability:**  
Targets analysts/ad-tech tuning ARA queries post–third-party cookie deprecation.

**Problems solved:**  
Reduces noise-induced error in **aggregate** attributed conversion reports via budget allocation.

**Engineering cost:**  
Requires historical unbounded data and optimization tooling per campaign topology.

---

## 4. Novelty vs Prior Work

**Paper's claimed novelty:**  
First detailed optimization study for ARA summary reports under DP, with generalization analysis.

**Prior work comparison:**  
Not specified in source (NotebookLM batch; no independent novelty web search).

**Verification:**  
Not specified in source.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Criteo SSCL | Via Tallis & Yadav IEEE BigData 2018 (cited) | Partial | Public lineage through cited work |
| Ad-tech real estate / travel | Not specified in source | Unknown | Proprietary samples |
| Synthetic (3) | Table 3 parameters | Yes | Regenerable from paper pipeline |

**Offline experiment reproducibility:**  
Synthetic side reproducible; full proprietary paths unclear.

---

## 6. Community Reaction

Not searched in this batch (NotebookLM-only ingestion).

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** Hidayet Aksu; Badih Ghazi; Pritish Kamath; Ravi Kumar; Pasin Manurangsi; Adam Sealfon; Avinash V Varadarajan  
**Affiliations:** Google (multiple offices, per author block)  
**Venue:** arXiv  
**Year:** 2023  
**PDF:** downloaded (arXiv)  
**Relevance:** Related  
**Priority:** 2

---

## NotebookLM — Project alignment (requirements.md §Project Context)

1. **Per-touchpoint fractional credit:** No — optimizes **aggregate** noisy summary reports; source notes separate per-conversion contribution computation, not joint fractional path labels for training.  
2. **Continuous outcomes as supervised training labels:** Not specified in source (conversion values as measurement targets, not discussed as ML supervision for per-interaction scoring).  
3. **Heterogeneous touch types / self-selection:** Not specified in source.
