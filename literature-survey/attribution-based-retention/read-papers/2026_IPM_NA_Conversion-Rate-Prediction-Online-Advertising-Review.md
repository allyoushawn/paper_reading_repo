# Paper Analysis: Conversion Rate Prediction in Online Advertising: A Systematic Review

**Source:** https://arxiv.org/pdf/2512.01171.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Conversion Rate Prediction in Online Advertising: A Systematic Review  
**Authors:** Yifan Xue, Jingyuan Yang, Jiahao Liu, Jinghua Feng, Jiawei Chen, Bo Zheng, Weinan Zhang (Shanghai Jiao Tong University; Alibaba Group)  
**Abstract:** PRISMA-style survey of **conversion rate prediction (CVR)** in computational advertising (2015–2025), covering data characteristics, modeling, training, and evaluation. Maps how delayed feedback, sample selection bias, data sparsity, cold start, and multi-task objectives interact with modeling choices.

**Key contributions:**
- Taxonomy of CVR challenges and mitigation families (e.g., importance weighting, auxiliary tasks, entire-space modeling, causal views).
- Consolidated evaluation practice critique (delayed labels, calibration, position bias).

**Methodology:** Systematic literature search and screening; narrative synthesis across ~200+ works (per survey scope).

**Main results:** Identifies dominant architectural trends (DNN + auxiliary structures) and open gaps around unbiased learning under real auction dynamics.

---

## 2. Experiment Critique

**Design:** Survey—not primary empirical claims.

**Statistical validity:** N/A for new estimators; quality depends on screening completeness.

**Online experiments (if any):** Not specified in source.

**Reproducibility:** Bibliography-driven; readers follow cited primary papers.

**Overall:** High-value **orientation map** for where attribution-like signals enter CVR training; not a new MTA algorithm.

---

## 3. Industry Contribution

**Deployability:** Indirect—guides which CVR head can consume path or counterfactual credit features.

**Problems solved:** Consolidates fragmented CVR literature for practitioners.

**Engineering cost:** Reading time; cross-walking to your stack’s logging constraints.

---

## 4. Novelty vs. Prior Work

Positions relative to prior narrower surveys on CTR or single-issue CVR topics.

---

## 5. Dataset Availability

Not specified in source (survey aggregates public benchmarks cited in primary papers).

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

**Authors:** Yifan Xue, Jingyuan Yang, Jiahao Liu, Jinghua Feng, Jiawei Chen, Bo Zheng, Weinan Zhang  
**Affiliations:** Shanghai Jiao Tong University; Alibaba Group  
**Venue:** Information Processing & Management (2026); arXiv preprint  
**Year:** 2026  
**PDF:** https://arxiv.org/pdf/2512.01171.pdf  
**Relevance:** Core  
**Priority:** 1

---

## Project Relevance

**(a) Per-touchpoint fractional credit:** Survey notes multi-touch / delayed-feedback contexts but does not prescribe a single fractional label generator.

**(b) Continuous outcomes:** CVR is typically binary/probability; continuous engagement outcomes appear only as general ML-adjacent discussion, not specified in source.

**(c) Selection / heterogeneous paths:** Extensive coverage of sample selection bias and position bias in logged data.

**(d) Incrementality:** Causal and debiasing strands are surveyed; no single incrementality estimator endorsed.
