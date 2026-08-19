# Paper Analysis: Rankability-enhanced Revenue Uplift Modeling Framework for Online Marketing

**Source:** https://xingt-tang.github.io/assets/pdf/rerum_kdd24.pdf  
**Source ID:** cfc316a0-65fd-4330-8add-d39b74011f4d  
**Date analyzed:** 2026-08-18  
**Model identifier:** codex-sol  
**Evidence mode:** NotebookLM indexed-content fallback after source-scoped query plateau.

---

## 1. Summary

**Authors:** Bowei He; Yunpeng Weng; Xing Tang; Ziqiang Cui; Zexu Sun; Liang Chen; Xiuqiang He; Chen Ma  
**Abstract:** RERUM adapts uplift backbones to zero-heavy, long-tail revenue with a ZILN response head, theoretical response-ranking bounds, and a listwise uplift-ranking loss.

**Main results:** Across Hillstrom and a 5M-person Tencent FiT dataset, RERUM generally improved AUUC/AUQC/Kendall/LIFT metrics; RERUM-DragonNet raised average LIFT@30 21.98%. Three online campaigns improved sales-revenue LIFT@2 by 9.20%, 37.24%, and 15.43% (20.61% average) and reportedly added $430M monthly AUM.

---

## 2. Experiment Critique

**Design:** Public and industrial RCT data, nine uplift baselines, five seeds, module ablations, ranking and calibration metrics, plus three online campaigns.

**Statistical validity:** Offline improvements use t-tests at p≤0.05; exact online intervals, assignment details, duration, and multiplicity correction are absent from extracted content.

**Online experiments:** Yes, on Tencent FiT; campaign-specific lifts are reported.

**Reproducibility:** Code is available at https://github.com/BokwaiHo/revenue_uplift; Hillstrom is public, product data are proprietary.

**Overall:** Strong direct evidence for ranking incremental revenue, though extreme AUM claims depend on platform accounting and campaign design.

---

## 3. Industry Contribution

**Deployability:** Designed around existing uplift backbones and deployed on a 400M-user fintech platform.

**Problems solved:** Continuous long-tail treatment response and allocation by incremental revenue rank.

**Engineering cost:** Requires randomized treatment/control data, ZILN heads, and large-batch ranking losses.

**Project relevance:** Core. This is the clearest bridge from response prediction to incremental revenue ranking; a dating product could treat exposure/promotion strategy as treatment and optimize incremental subscription/à-la-carte value rather than spend propensity.

**Most important mismatch:** It models independent individuals and binary treatment, not reciprocal pairs, candidate congestion, multi-stage matching, delayed retention, or successful-exit censoring. Interference violates standard CATE assumptions.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Joint ZILN revenue regression and explicit pairwise/listwise uplift-rank optimization.

**Prior work comparison:** Extends TAR/CFR/DragonNet-style CATE models beyond value accuracy to ranking quality under continuous revenue.

**Verification:** Source-grounded only.

---

## 5. Dataset Availability

| Dataset | Accessible | Notes |
|---------|------------|-------|
| Hillstrom Men/Women | Yes | 64K email-campaign consumers. |
| Tencent FiT product | No | >5M individuals, >1,800 features. |
| Code | Yes | Official GitHub link above. |

---

## 6. Community Reaction

No significant discussion assessed.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Affiliations:** Tencent FiT / academic collaborators  
**Venue:** KDD  
**Year:** 2024  
**Relevance:** Core  
**Priority:** 1  
**Direction:** D6 — causal uplift / incrementality
