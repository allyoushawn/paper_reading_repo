# Paper Analysis: Causally Driven Incremental Multi Touch Attribution Using a Recurrent Neural Network

**Source:** https://arxiv.org/pdf/1902.00215.pdf  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** Causally Driven Incremental Multi Touch Attribution Using a Recurrent Neural Network  
**Authors:** Ruihuan Du, Yu Zhong, Harikesh Nair, Bo Cui, Ruyang Shou (JD.com)  
**Abstract:**
This paper proposes a two-component framework for multi-touch attribution at JD.com scale: (1) a bi-directional LSTM to model conversion probability incorporating ad intensity, timing, user heterogeneity, and inter-channel competition, and (2) an incremental Shapley value algorithm that computes attribution credits via a mixed exact/Monte Carlo approach with MapReduce parallelization. The paper is notable for being deployed in production at JD.com with 75M+ users, 7B impressions, and 301 ad positions.

**Key contributions:**
- Bi-directional LSTM conversion model incorporating four key signals: ad exposure intensity, timing, user heterogeneity (baseline purchase probability), and channel competition
- Incremental Shapley value: marginal credit assigned to each touchpoint based on counterfactual removal from the conversion model, not rule-based attribution
- Mixed exact/Monte Carlo Shapley algorithm: exact computation for small coalitions (≤6), MC sampling for large coalitions, 2300% faster than pure MC with lower error
- MapReduce parallelization for production-scale deployment at JD.com
- Empirical correction of last-click bias: cart and payment page overvalued by last-click; display ads undervalued

**Methodology:**
The bi-directional LSTM processes the ad exposure sequence in both forward and backward directions, producing a conversion probability for any sub-journey (coalition). The Shapley formula requires evaluating the model on all 2^K subsets of K channels. The mixed algorithm computes exact Shapley for coalitions of size ≤6 (covers ~85% of journeys) and uses MC for the rest. MapReduce distributes coalition evaluations across workers. Attribution credits are then aggregated by ad position and channel type.

**Main results:**
Mixed algorithm: 101.24 orders/minute computation rate vs 4.2 (pure MC). Error: 0.0064 vs 0.3190 (MC). Production deployment corrected last-click results substantially: display ads' share increased from ~0% to meaningful positive attribution. Cart and payment page ads, overvalued by last-click to 60%+, were corrected downward. The framework attributed 7B impressions across 301 ad positions daily.

---

## 2. Experiment Critique

**Design:**
Real production system evaluation at JD.com. Comparison: mixed algorithm vs pure MC Shapley (error + speed). Attribution results compared against last-click baseline. No A/B test or ground truth conversion lift measurement.

**Statistical validity:**
Limited by absence of ground truth. The computational comparison (speed and error) is rigorous and reproducible. The last-click correction finding is directionally plausible but not causally validated. Production deployment is the strongest evidence of practical viability.

**Online experiments (if any):**
N/A — offline attribution system, no reported online A/B test.

**Reproducibility:**
No code released. Dataset is proprietary JD.com. The mixed algorithm is fully described mathematically and can be reimplemented.

**Overall:**
Strong industry deployment paper. The scale (7B impressions, 301 ad positions, 75M users) is impressive. The mixed exact/MC Shapley algorithm is a genuine engineering contribution. Lack of causal ground truth is a limitation shared with all MTA papers.

---

## 3. Industry Contribution

**Deployability:**
Very high. The bi-directional LSTM + incremental Shapley framework is a standard architecture. The mixed exact/MC algorithm for Shapley is a practical speedup that applies to any model-based Shapley computation. Deployed at one of the world's largest e-commerce platforms.

**Problems solved:**
For dating platform attribution: the mixed Shapley algorithm directly applies to computing incremental attribution of user interactions (messages, matches, profile views) on retention probability. The bi-directional LSTM's treatment of timing and user heterogeneity is directly relevant. The "loyal user" correction (separating single-channel from multi-channel users) mirrors the dating platform problem of distinguishing high-intent users.

**Engineering cost:**
Moderate. Bi-directional LSTM is standard. Mixed Shapley requires careful coalition enumeration. MapReduce infrastructure is needed for scale, but the algorithm works at smaller scale without it.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**
First production deployment of incremental Shapley-based MTA at e-commerce scale; first mixed exact/MC Shapley algorithm with proven error bounds; first bi-directional LSTM conversion model incorporating all four key ad signals (intensity, timing, heterogeneity, competition) jointly.

**Prior work comparison:**
Zhao et al. (2018): simplified Shapley formula but no incremental/causal framing; Shao & Li (2011): limited to 2-way interactions; DARNN (Ren et al. 2018): no Shapley attribution. JD.com paper bridges causal incrementality and deep sequence modeling, which prior work addressed separately.

**Verification:**
Production deployment at JD.com is the strongest validation. The mixed algorithm's 2300% speedup and 50× error reduction over pure MC are reproducible via the described method.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| JD.com Production Data | Not public | No | 7B impressions, 75M users, 301 ad positions |

**Offline experiment reproducibility:**
Not reproducible — proprietary JD.com data.

---

## 6. Community Reaction

arXiv 2019, JD.com industry paper. ~100 citations. The mixed Shapley algorithm has been cited by subsequent MTA papers as a practical contribution. The production deployment at JD.com scale gives it industry credibility. Limited theoretical novelty but strong engineering contribution.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| [2024_arXiv_DCRMTA_Unbiased-Causal-Representation-Multi-touch-Attribution](./2024_arXiv_DCRMTA_Unbiased-Causal-Representation-Multi-touch-Attribution.md) | Related Work | JDMTA incremental Shapley approach cited as prior Shapley-based MTA work |

---

## Meta Information

**Authors:** Ruihuan Du, Yu Zhong, Harikesh Nair, Bo Cui, Ruyang Shou  
**Affiliations:** JD.com  
**Venue:** arXiv 2019 (industry report)  
**Year:** 2019  
**PDF:** https://arxiv.org/pdf/1902.00215.pdf  
**Relevance:** Core  
**Priority:** 3
