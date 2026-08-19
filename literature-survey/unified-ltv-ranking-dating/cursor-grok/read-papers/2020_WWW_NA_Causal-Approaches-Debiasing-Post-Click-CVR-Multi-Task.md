# Paper Analysis: Large-scale Causal Approaches to Debiasing Post-click Conversion Rate Estimation with Multi-task Learning

**Source:** https://doi.org/10.1145/3366423.3380037
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** Large-scale Causal Approaches to Debiasing Post-click Conversion Rate Estimation with Multi-task Learning
- **authors or company:** Wenhao Zhang, Wentian Bao, Xiao-Yang Liu, Keping Yang, Quan Lin, Hong Wen, Ramin Ramezani (UCLA / Alibaba Group / Columbia University)
- **venue:** WWW
- **year:** 2020
- **URL:** https://doi.org/10.1145/3366423.3380037
- **source type:** industry paper
- **direction:** D5, D6
- **problem setting:** Post-click CVR estimation in Mobile Taobao e-commerce where training occurs in click space O but inference serves full exposure space D (MNAR selection bias), compounded by extreme click/conversion sparsity (production CTR 5.2%, 0.6B samples vs 5.3B parameters on largest set).
- **objective and label definition:** Binary conversion label r_{u,i} ∈ {0,1} per exposure; conversion observed only if user clicked (o_{u,i}=1); sequential chain exposure→click→conversion with no longer-horizon retention label.
- **prediction or incrementality:** **Prediction debiasing only**—Multi-IPW/Multi-DR correct MNAR selection into training data via IPW/DR, estimating P(conversion|exposure) over full exposure space; does not estimate incremental causal effect of showing an item vs not showing it.
- **model architecture:** Shared embedding lookup + chained CTR, CVR, and (Multi-DR only) Imputation towers; Multi-IPW weights CVR loss by inverse predicted CTR (propensity) over full D; Multi-DR adds doubly-robust imputation correction (Eq. 9).
- **credit assignment:** Pointwise per-(user, item) exposure—no journey-level or delayed backward attribution.
- **training data and counterfactual handling:** Ali-CCP (84M exposures) + Mobile Taobao Sets A–D (1.1B–11.5B exposures, 109 features); central contribution is MNAR correction via jointly trained CTR propensities and imputation model with formal unbiasedness proofs (Theorems 3.1–3.2); authors prove ESMM is biased (Eq. 3, Figure 2 counterexample).
- **offline and online evaluation:** Offline only: CVR AUC, CTCVR AUC, GAUC on held-out data; Ali-CCP repeated 10 runs mean±std; production sets single-run point estimates; computational cost comparison (Fig. 4, 100 workers/440 CPU/25 GPU). No online A/B. Authors note truly unbiased CVR test sets are "rather unobtainable" (Section 4.4).
- **reported gains:** Ali-CCP (Table 3): Multi-DR CVR AUC 69.29±0.31 / CTCVR AUC 65.43±0.34 vs ESMM 68.56±0.37 / 65.32±0.49. Set D (11.5B exposures): Multi-DR CTCVR AUC 77.23 / GAUC 62.28 vs ESMM CTCVR AUC 76.55 / GAUC 61.76.
- **applicability note for a two-sided dating recommender:** Clean example of debiasing a *prediction* against click-space selection—not incrementality; formal ESMM bias proof is a caution for auditing any retained CTR/CVR-style funnel component (swipe→like→match).
- **applicability note for a two-sided dating recommender:** Rubin MNAR / IPW / doubly-robust framework reusable if project needs to debias retained short-term predictors; no reciprocity, congestion, or bilateral structure.
- **unverified claims:** "First paper" combining IPW/DR with MTL is an author novelty claim; assumes exposure space ≈ entire item space (each item exposed ~150 times on average).

## 1. Summary

**Title:** Large-scale Causal Approaches to Debiasing Post-click Conversion Rate Estimation with Multi-task Learning
**Authors:** Wenhao Zhang et al. (Alibaba/UCLA/Columbia)
**Abstract:** Proposes Multi-IPW and Multi-DR CVR estimators combining causal missing-data theory (IPW and doubly robust) with multi-task parameter sharing to address selection bias and data sparsity at billion-scale.

**Key contributions:**
- Formal proof that ESMM is biased despite industrial popularity.
- Multi-IPW and Multi-DR with shared embeddings and CTR-as-propensity.
- Production-scale evaluation up to 11.5B exposures.

**Methodology:** Three-task chain (CTR, CVR, Imputation for Multi-DR) with theorems proving unbiasedness under accurate propensities (Multi-IPW) or propensity-or-imputation accuracy (Multi-DR).

**Main results:** Multi-IPW and Multi-DR outperform ESMM, Naive IPW, Joint Learning DR, and other baselines on CTCVR AUC/GAUC with lower or equal training cost.

## 2. Experiment Critique

**Design:** Strong theoretical contribution with counterexample against ESMM; production and public benchmarks.

**Statistical validity:** Ali-CCP 10-run std reported; production Table 2 lacks confidence intervals.

**Online experiments (if any):** None—offline only; authors acknowledge evaluation proxy limitation.

**Reproducibility:** Ali-CCP public on Tianchi; production Sets A–D proprietary.

**Overall:** Principled industrial CVR debiasing; "causal" means selection-bias correction, not uplift.

## 3. Industry Contribution

**Deployability:** Evaluated at up to 11.5B exposures on distributed cluster; fits standard CTR→CVR pipeline slot.

**Problems solved:** Click-space training vs exposure-space serving mismatch plus CVR sparsity via MTL parameter sharing.

**Engineering cost:** Multi-IPW/Multi-DR require less or equal training time and smaller embeddings than Joint Learning DR (Figure 4).

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First IPW/DR + MTL combination for CVR; ESMM bias proof.

**Prior work comparison:** vs ESMM, Naive IPW, Schnabel et al. IPW, Wang et al. Joint Learning DR.

**Verification:** Consistent gains across four production set sizes and Ali-CCP support empirical claims.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Ali-CCP | Tianchi Alibaba Cloud | Yes | 84M exposures, 3.4M clicks, 18K conversions |
| Mobile Taobao Sets A–D | Proprietary | No | 1.1B–11.5B exposures |

**Offline experiment reproducibility:** Ali-CCP experiments reproducible; production sets not.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** CVR/CTCVR prediction for e-commerce ranking pipeline—not retention/LTV.

**(2) Credit assignment:** Per-exposure pointwise labels; no delayed multi-step funnel credit.

**(3) Label and horizon definitions:** Immediate conversion after click; MNAR from click-space observation; no multi-day retention horizon.

**(4) Short-term + long-term heads:** CTR+CVR chained MTL sharing embeddings—not separate LTV head fusion.

**(5) Prediction vs incrementality:** **Prediction debiasing**—corrects who enters training set, not causal effect of exposure; key distinction for project's uplift goals.

**(6) Offline and online evaluation:** Offline AUC/GAUC only; authors flag unobtainable unbiased CVR test sets.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Single-sided e-commerce CVR; not applicable to two-sided matching.

**(8) Migration path from CTR-like model to unified long-term model:** Not specified—slot-in replacement for ESMM-style CVR tower with debiased training.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Wenhao Zhang, Wentian Bao, Xiao-Yang Liu, Keping Yang, Quan Lin, Hong Wen, Ramin Ramezani
**Affiliations:** UCLA; Alibaba Group; Columbia University
**Venue:** WWW 2020
**Year:** 2020
**PDF:** https://doi.org/10.1145/3366423.3380037
**Relevance:** Core
**Priority:** 2
