# Paper Analysis: Shapley Value Methods for Attribution Modeling in Online Advertising

**Source:** https://arxiv.org/pdf/1804.05327.pdf  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** Shapley Value Methods for Attribution Modeling in Online Advertising  
**Authors:** Kaifeng Zhao, Seyed Hanif Mahboobi, Saeed R. Bagheri (GroupM, Singapore / New York)  
**Abstract:**
This paper re-examines the Shapley value method for online advertising attribution and makes two contributions: (1) a mathematically simplified formula that reduces computation from O(2^K · K) to approximately O(2^K), reducing analysis time from 17 hours to 2 minutes for 18 channels; (2) an ordered Shapley value method that differentiates channel credit by the sequential position (touchpoint index) of the channel in the user's conversion journey, providing a richer view of channel roles at different stages.

**Key contributions:**
- Simplified Shapley formula: φⱼ = Σ (1/|S|+1) · R(S ∪ {xⱼ}) — weighted average over coalitions containing channel xⱼ
- Ordered Shapley value: φʲᵢ decomposes total Shapley value by touchpoint position i, revealing channel effectiveness at each stage of the conversion journey
- Clarifies and corrects definitional errors in prior Shapley-based MTA methods (Shao & Li 2011, Dalessandro 2012)
- Empirical demonstration on a real 18-channel, 153k conversion advertising campaign

**Methodology:**
For the simplified Shapley formula, each coalition is evaluated at most once per channel instead of iterating over all permutations. For ordered Shapley: R(S∪{xⱼ}) is decomposed into Rᵢ(S∪{xⱼ}) by the position index i of channel xⱼ in the user's journey. This yields a (channels × touchpoints) attribution matrix showing channel contribution at each sequential step.

**Main results:**
17 hours → 2 minutes computation time for 18 channels. Campaign: Paid Search 47%, DSPs 40.43%, Publishers 12.58%. Ordered Shapley reveals: touchpoint 1 gets 91.59% of total credit, but this is largely from single-channel converters (loyal users). When filtering multi-channel users: Paid Search at touchpoint 1 drops from 43.76% to 8.25% (4.37% for 3+ channel journeys). DSPs become increasingly important at touchpoints 3–5.

---

## 2. Experiment Critique

**Design:**
Single real campaign (3 months, 18 channels, 153k conversions). Comparison against general Shapley value only — no other attribution baselines. Computational comparison is primary quantitative result.

**Statistical validity:**
Limited — single campaign, no replication, no ground truth attribution. The honest acknowledgment of the "loyal user" bias (offline channels not captured) is a strength. The ordered Shapley segmentation analysis is exploratory but revealing.

**Online experiments (if any):**
N/A.

**Reproducibility:**
No code released. Dataset is proprietary GroupM campaign data. Methods are fully described mathematically.

**Overall:**
Practical industry paper with useful methodological contributions. The simplified formula and ordered Shapley are genuine value adds for practitioners. Theoretical depth is limited; the paper is applied rather than foundational.

---

## 3. Industry Contribution

**Deployability:**
High. The simplified formula is a drop-in replacement for Shapley computation in any MTA pipeline. The ordered Shapley provides richer channel role understanding. GroupM (WPP) is one of the world's largest media agencies, giving this industry credibility.

**Problems solved:**
For dating platform attribution: the ordered Shapley value provides a natural way to understand whether a particular interaction type (e.g., first match vs subsequent messages) plays a different role at the beginning vs end of a user's "conversion journey" toward retention. The simplified formula makes Shapley computationally tractable.

**Engineering cost:**
Low. The simplified formula is a straightforward reformulation. No ML infrastructure required beyond standard attribution logging.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**
First simplification of Shapley computation for advertising attribution that is both computationally efficient and mathematically equivalent; first ordered Shapley method for sequential touchpoint attribution.

**Prior work comparison:**
Shao & Li (2011): simple probabilistic model, limited to 2-way interactions, incorrect marginal contribution definition; Dalessandro et al. (2012): full Shapley but computationally infeasible and focuses only on grand coalition users. This paper corrects both.

**Verification:**
Claims hold up mathematically. The 17-hour → 2-minute speedup is reproducible via the formula. The ordered Shapley has been adopted in industry attribution tooling.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| GroupM Campaign Data | Not public | No | 3-month real advertising campaign |

**Offline experiment reproducibility:**
Not reproducible — proprietary dataset.

---

## 6. Community Reaction

arXiv 2018, GroupM industry paper. ~200 citations. Practical impact high in industry attribution tooling. The ordered Shapley concept has been cited by subsequent MTA papers as a useful methodology for understanding channel sequencing effects.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| [2019_arXiv_JDMTA_Causally-Driven-Incremental-Multi-Touch-Attribution-RNN](./2019_arXiv_JDMTA_Causally-Driven-Incremental-Multi-Touch-Attribution-RNN.md) | Method | Shapley MTA framework is the basis for JDMTA's incremental Shapley; JDMTA extends with RNN and mixed exact/MC algorithm |
| [2020_arXiv_DeepMTA_Interpretable-Deep-Learning-Multi-touch-Attribution](./2020_arXiv_DeepMTA_Interpretable-Deep-Learning-Multi-touch-Attribution.md) | Method | Shapley regression approach in DeepMTA extends Shapley MTA with Phased-LSTM and powerset mask matrices |
| [2024_arXiv_DCRMTA_Unbiased-Causal-Representation-Multi-touch-Attribution](./2024_arXiv_DCRMTA_Unbiased-Causal-Representation-Multi-touch-Attribution.md) | Related Work | Shapley-based attribution cited as non-causal baseline; DCRMTA applies Shapley on its deconfounded model |

---

## Meta Information

**Authors:** Kaifeng Zhao, Seyed Hanif Mahboobi, Saeed R. Bagheri  
**Affiliations:** GroupM (WPP), Singapore / New York  
**Venue:** arXiv 2018 (industry report)  
**Year:** 2018  
**PDF:** https://arxiv.org/pdf/1804.05327.pdf  
**Relevance:** Core  
**Priority:** 3
