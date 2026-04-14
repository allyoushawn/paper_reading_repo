# Paper Analysis: A Unified Survey of Treatment Effect Heterogeneity Modelling and Uplift Modelling

**Source:** https://arxiv.org/pdf/2007.12769.pdf  
**Date analyzed:** 2026-04-12

---

This **ACM Computing Surveys** article (Zhang, Li, Liu; arXiv 2007.12769) unifies **treatment effect heterogeneity** and **uplift modelling** under the potential-outcomes framework, stressing overlap, SUTV, and unconfoundedness. It catalogs meta-learners (S/T/X/R), transformed outcomes, deep CFR-style models, causal/uplift trees and forests, SVM uplift objectives, generative CEVAE/GANITE variants, and surveys software (causalTree, grf, CausalML, etc.) plus benchmarks on synthetic data, IHDP semi-synthetic settings, Hillstrom email RCT, and the large Criteo uplift dataset. Empirical takeaways: CATE estimation is fragile (weak signals, systematic underestimation even when models are “correctly specified”); IHDP Setting B breaks all surveyed methods (MAPE >300%); Hillstrom shows train/test uplift instability; deep models scale near-constantly while tree methods are fastest. Limitations called out include SUTV violations in marketing (spillover via forwards), greedy tree instability, and deep nets’ tuning difficulty without ground-truth CATEs.

**Low project relevance for Phase 1 MTA labels:** The survey targets **scalar CATE/uplift** for a **single binary treatment**, not fractional credit along **sequences of heterogeneous touchpoints**; it does not provide MTA credit assignment mechanisms for supervised path-level labels (per NotebookLM scoped answer).

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** Weijia Zhang, Jiuyong Li, Lin Liu  
**Affiliations:** Southeast University; University of South Australia  
**Venue:** ACM Computing Surveys (arXiv version used)  
**Year:** 2021 (journal publication timing per survey metadata)  
**PDF:** https://arxiv.org/pdf/2007.12769.pdf  
**Relevance:** Related  
**Priority:** 3

---

## Project Relevance

**Low project relevance.** The survey is strictly about **CATE/uplift estimation** for binary treatments—not multi-touch fractional credit for sequential engagement events. Useful as **background** for incrementality literacy and for cross-walking to papers that *do* connect uplift to path-level attribution.
