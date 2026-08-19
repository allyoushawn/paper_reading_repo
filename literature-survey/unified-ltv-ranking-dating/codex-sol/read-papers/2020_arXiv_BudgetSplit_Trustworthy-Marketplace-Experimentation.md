# Paper Analysis: Trustworthy Online Marketplace Experimentation with Budget-split Design

**Source:** https://arxiv.org/pdf/2012.08724  
**Source ID:** 519eb255-08ec-4750-a7f8-7321dc17fa15  
**Date analyzed:** 2026-08-18  
**Model identifier:** codex-sol  
**Evidence mode:** NotebookLM indexed-content fallback after source-scoped query plateau.

---

## 1. Summary

**Authors:** Min Liu; Jialiang Mao; Kang Kang  
**Abstract:** Budget-split experiments partition members and proportionally split every buyer/campaign budget, creating isolated treatment and control marketplaces. This blocks cannibalization interference while retaining member-side scale.

**Main results:** At the effect size where budget-split reached 80% power, campaign-level tests had only 5.2%/12% power and switchbacks 5.1%/5.2% in two marketplaces. Conventional tests overestimated effects by roughly one-to-two times; the design detected million-dollar annual harms previously missed.

---

## 2. Experiment Critique

**Design:** Formal potential-outcome derivation plus deployed comparisons of power curves and cannibalization bias across two marketplaces.

**Statistical validity:** Strong interference-aware estimand; variance estimation is explicitly future work, and exact marketplace metrics/sample sizes are confidential.

**Online experiments:** Yes, in two real marketplaces.

**Reproducibility:** Design and architecture are described, but marketplace data are unavailable.

**Overall:** Highly relevant evidence that ordinary user randomization fails under scarce two-sided resources.

---

## 3. Industry Contribution

**Deployability:** LinkedIn reports incremental infrastructure changes rather than a platform rewrite.

**Project relevance:** Core for dating congestion and reciprocal interference. Splitting exposure/contact budgets can create isolated experimental markets and yield trustworthy long-term retention/revenue estimates.

**Most important mismatch:** Dating “budgets” are attention/inventory and may be discrete, endogenous, and non-divisible; pair formation also creates network spillovers across partitions. The proportional restriction assumption needs validation.

---

## 4. Novelty vs. Prior Work

**Claimed novelty:** Practical unbiased high-power marketplace design requiring only a splittable buyer budget.

**Prior work comparison:** Improves over member/campaign Bernoulli tests, switchbacks, clustering, and model-based interference corrections.

**Verification:** Source-grounded only.

---

## 5. Dataset Availability

| Dataset | Accessible | Notes |
|---------|------------|-------|
| Marketplace 1 and 2 experiments | No | Proprietary LinkedIn marketplaces. |

---

## 6. Community Reaction

No significant discussion assessed.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Affiliations:** LinkedIn  
**Venue:** arXiv preprint  
**Year:** 2020  
**Relevance:** Core—inferred  
**Priority:** 1  
**Direction:** D6 — causal uplift / incrementality
