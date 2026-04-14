# Paper Analysis: Multi-Touch Attribution Based Budget Allocation in Online Advertising

**Source:** https://arxiv.org/pdf/1502.06657.pdf
**Date analyzed:** 2026-04-12

---

## 1. Summary
**Title:** Multi-Touch Attribution Based Budget Allocation in Online Advertising
**Authors:** Sahin Cem Geyik, Abhishek Saxena, Ali Dasdan
**Abstract:** Budget allocation in online advertising deals with distributing campaign-level budgets to sub-campaigns with different targeting criteria and varying ROI. The authors present a complete budget allocation scheme deployed at Turn Inc. that combines MTA-based ROI calculation with adaptive budget assignment. They provide a scalable parallelized methodology on Hadoop to calculate multi-touch attribution over tens of terabytes, and provide the first empirical comparison of LTA vs MTA-based budget allocation on a real advertising system.

**Key contributions:**
- Complete budget allocation scheme distributing money from campaign to sub-campaigns according to MTA-derived ROI
- Scalable two-step parallelized MTA algorithm on Hadoop processing tens of terabytes and billions of virtual users
- First published empirical comparison of LTA vs MTA budget allocation on a live advertising platform
- Demonstrates that MTA budget allocation significantly outperforms LTA in ROI, eCPA, and eCPC

**Methodology:** Two-step probabilistic MTA adapted from Shao & Li (2011), restricted to first-order probabilities for efficiency. Step 1: calculate empirical action probability weights w(li) = N+(li) / (N+(li) + N-(li)) for each line item. Step 2: for each action sequence, fractionally attribute credit to line items based on normalized weights. Budget allocation uses greedy assignment sorted by ROI, with an adaptive spending capability estimator. Implemented as two MapReduce jobs on Hadoop scheduled by Oozie.

**Main results:** In a 12-day live A/B test (November 2013), MTA-based budget allocation achieved significantly higher ROI, lower eCPA, and lower eCPC than LTA-based allocation. MTA correctly allocated 63.5% of budget to the highest-ROI line item (ROI 31.85), while LTA misallocated 40.5% to a retargeting line item (ROI 3.01) due to last-touch bias. The system processes the two-step MTA job in ~2 hours daily in production.

---

## 2. Experiment Critique
The experiment is a single 12-day A/B test with two campaigns and four identical line items per campaign. While this demonstrates the real-world impact, the single-experiment design limits statistical generalizability. ROI values are modified by a constant factor for privacy, preventing absolute magnitude assessment. The comparison is LTA vs a specific first-order probabilistic MTA — more sophisticated baselines (Shapley, deep learning MTA) are not tested. The retargeting bias example is compelling but may not generalize to all campaign structures. The Hadoop implementation details are thorough and aid reproducibility. Second-order probability calculations were tested but discarded as not improving accuracy enough to justify processing time — a useful negative result.

---

## 3. Industry Contribution
Highly deployable as a production system — deployed at Turn Inc. at industrial scale. The key engineering contribution is showing that a relatively simple probabilistic MTA (first-order only) can drive substantial ROI improvement when used for budget allocation decisions. The Hadoop pipeline design (sharded mappers, weight-passing between jobs, Oozie scheduling, control server integration) is a practical blueprint for implementing MTA at scale. The adaptive spending capability estimator addresses the practical constraint that sub-campaigns have heterogeneous reach.

---

## 4. Novelty vs. Prior Work
1. **Shao and Li (2011)** — "Data-driven multi-touch attribution models" — foundational probabilistic model directly adapted
2. **Dalessandro et al. (2012)** — "Causally motivated attribution" — proved Shao & Li's scheme is equivalent to Shapley value under simplifying assumptions
3. **Zhang et al. (2012)** — "Joint optimization of bid and budget allocation" — closest prior budget allocation work; authors contrast their action-based (vs click-based) approach
4. **Abhishek et al. (2013)** — "Media exposure through the funnel" — HMM-based attribution model
5. **Wooff and Anderson (2013)** — "Time-weighted multi-touch attribution" — Beta distribution bathtub-shaped credit assignment
6. **Archak et al. (2010)** — "Budget optimization with carryover effects" — Markov chain user behavior model

---

## 5. Dataset Availability
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Turn Inc. Ad Platform Data | N/A | No | Proprietary; tens of TB, billions of virtual users |
| 12-day A/B Test (Nov 2013) | N/A | No | Proprietary; 2 campaigns × 4 line items |

---

## 6. Community Reaction
No significant community discussion found.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information
**Authors:** Sahin Cem Geyik, Abhishek Saxena, Ali Dasdan
**Affiliations:** Turn Inc. (Applied Science Division)
**Venue:** ADKDD 2014 (published via KDD Workshop)
**Year:** 2015 (arXiv), 2014 (workshop)
**PDF:** https://arxiv.org/pdf/1502.06657.pdf
**Relevance:** Core
**Priority:** 2

---

## Project Relevance
**(A) Does it produce per-touchpoint or per-interaction credit suitable as continuous training labels, or mainly aggregate lift?**
- Produces per-touchpoint fractional credit. The algorithm calculates empirical probability weights for each touchpoint type and then normalizes these weights across the specific sequence of touchpoints that led to an action. This outputs a specific fractional percentage (between 0 and 1) of the action attributed to each individual touchpoint in the sequence.

**(B) Applicability to non-purchase, continuous engagement / retention outcomes?**
- Not specified in source. The paper strictly models discrete conversion actions (e.g., purchasing a product, filling out a form, or visiting a page) to support cost-per-action (CPA) campaigns, and does not mention continuous accumulation metrics like user-days-active.

**(C) Handling selection bias when high-activity users get more touchpoints?**
- Not specified in source. The model relies purely on basic empirical correlations — specifically the ratio of action sequences to total sequences containing a given touchpoint type. It does not introduce causal inference techniques or address baseline activity bias for highly active users.
