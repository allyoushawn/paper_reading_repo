# Paper Analysis: Multi-touch Attribution in Online Advertising with Survival Theory

**Source:** https://wnzhang.net/share/rtb-papers/attr-survival.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Multi-touch Attribution in Online Advertising with Survival Theory  
**Authors:** Weinan Zhang; Shuai Yuan; Jun Wang (UCL)  
**Abstract:** Treats conversion as event time in continuous time; models cumulative hazard from **exponential kernels** over past impressions with channel-specific parameters; fits via **minorization–maximization (MM)**; attributes credit by comparing model with vs without each touch.

**Key contributions:**
- ADDITIVEHAZARD / survival formulation: \(\lambda(t)=\sum_k \alpha_{c_k} e^{-\beta_{c_k}(t-t_k)}\) style additive intensity over impression history.
- MM algorithm for nonconvex likelihood with convergence guarantees in paper.
- Attribution by counterfactual removal of touch in intensity (survival decomposition).

**Methodology:** Miaozhen logs; F1 and ranking metrics vs last-touch, first-touch, uniform, Bagherjeiran et al. 2008.

**Main results:** Reported F1 ~0.035 vs weaker baselines on described campaign slice (scale depends on sparse positives).

---

## 2. Experiment Critique

**Design:** Offline evaluation on partner data; class imbalance typical for conversion.

**Statistical validity:** MM local optima; sensitivity to kernel width \(\beta\) per channel.

**Online experiments (if any):** Not specified in source.

**Reproducibility:** PDF open; raw logs proprietary.

**Overall:** Foundational **path-level survival MTA** cited by later AMTA and industry surveys.

---

## 3. Industry Contribution

**Deployability:** Moderate — continuous-time hazard fits streaming impression logs.

**Problems solved:** Time-credit beyond discrete position heuristics.

**Engineering cost:** Moderate — per-channel kernel parameters + MM training.

---

## 4. Novelty vs. Prior Work

Contrasts heuristic rules and discrete bag-of-impressions models; connects to survival analysis in marketing.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Miaozhen | N/A | No | Industry partner |

**Offline experiment reproducibility:** Low without data.

---

## 6. Community Reaction

Not specified in source.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** Weinan Zhang; Shuai Yuan; Jun Wang  
**Affiliations:** University College London  
**Venue:** ICDM 2014  
**Year:** 2014  
**PDF:** https://wnzhang.net/share/rtb-papers/attr-survival.pdf  
**Relevance:** Core  
**Priority:** 2

---

## Project Relevance

**(A)** Touch-level credit from survival intensity; **not specified in source** as supervised labels for retention modeling.

**(B)** Event-time conversion focus; **continuous engagement outcomes are not specified in source.**

**(C)** Hazard is conditional on observed impression stream; **causal interpretation under user activity endogeneity is not specified in source.**
