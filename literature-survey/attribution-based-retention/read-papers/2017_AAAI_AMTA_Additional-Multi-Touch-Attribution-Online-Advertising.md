# Paper Analysis: Additional Multi-Touch Attribution for Online Advertising

**Source:** https://ojs.aaai.org/index.php/AAAI/article/download/10737/10596  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Additional Multi-Touch Attribution for Online Advertising  
**Authors:** Feng Ji; Wenwu Wang (University of Surrey)  
**Abstract:** Models each touch as a **hazard** toward conversion with **intrinsic conversion rate** (user propensity) and channel-specific hazard; estimates parameters via EM; assigns credit by comparing path likelihood with vs without each touch.

**Key contributions:**
- AMTA: additive competing risks over ordered touches; intrinsic rate separates user baseline from ad effect.
- EM updates for parameters with closed-form E-step expectations on latent “which touch caused conversion.”
- Credit rule: marginal contribution of touch \(k\) via \(\log P(\text{path})-\log P(\text{path without }k)\) style decomposition (path likelihood ratio).

**Methodology:** Real campaign logs (Miaozhen); AUC/F1 vs last-touch, first-touch, linear, time-decay, Shapley, Zhang et al. (ICDM 2014).

**Main results:** Highest AUC on Miaozhen campaign among compared baselines; interpretable per-touch hazard parameters.

---

## 2. Experiment Critique

**Design:** Offline attribution benchmark on industry partner data; limited public release detail.

**Statistical validity:** EM convergence and identifiability depend on path diversity; no randomized incrementality test in extracted summary.

**Online experiments (if any):** Not specified in source.

**Reproducibility:** Miaozhen data not broadly public; method replicable from equations.

**Overall:** Clear **path-level** competing-risk story aligned with survival MTA lineage.

---

## 3. Industry Contribution

**Deployability:** Moderate — needs per-touch timestamps and sufficient path volume for EM.

**Problems solved:** Separates user propensity from channel hazard; improves discrimination vs decay heuristics.

**Engineering cost:** Moderate — EM loop and hazard bookkeeping.

---

## 4. Novelty vs. Prior Work

Extends Zhang et al. ICDM 2014 additive hazard MTA with intrinsic conversion rate; positions against Shapley and heuristic rules.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Miaozhen campaign logs | Partner-only | No | Used in AAAI paper |

**Offline experiment reproducibility:** Low without partner data.

---

## 6. Community Reaction

Not specified in source.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| [2018_CIKM_DARNN_Multi-touch-Conversion-Attribution-Dual-Attention](./2018_CIKM_DARNN_Multi-touch-Conversion-Attribution-Dual-Attention.md) | 1. Summary | Unique survey token `AMTA` (filename disambiguation) appears in scanned sections. |
| [2020_arXiv_DeepMTA_Interpretable-Deep-Learning-Multi-touch-Attribution](./2020_arXiv_DeepMTA_Interpretable-Deep-Learning-Multi-touch-Attribution.md) | 4. Novelty vs. Prior Work | Unique survey token `AMTA` (filename disambiguation) appears in scanned sections. |

---

## Meta Information

**Authors:** Feng Ji; Wenwu Wang  
**Affiliations:** University of Surrey  
**Venue:** AAAI 2017  
**Year:** 2017  
**PDF:** https://ojs.aaai.org/index.php/AAAI/article/download/10737/10596  
**Relevance:** Core  
**Priority:** 1

---

## Project Relevance

**(A)** Produces **per-touch** credit from path likelihood / hazard decomposition; **not specified in source** as training targets for a retention ranker.

**(B)** Conversion is binary event timing; **continuous engagement is not specified in source.**

**(C)** Intrinsic rate captures latent user heterogeneity; **explicit causal identification vs “active users get more ads” confounding is not specified in source.**
