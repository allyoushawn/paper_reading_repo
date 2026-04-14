# Paper Analysis: Interpretable Deep Learning Model for Online Multi-touch Attribution

**Source:** https://arxiv.org/pdf/2004.00384.pdf  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** Interpretable Deep Learning Model for Online Multi-touch Attribution  
**Authors:** Dongdong Yang (USC), Kevin Dyer (eBay), Senzhang Wang (Nanjing University of Aeronautics and Astronautics)  
**Abstract:**
This paper proposes DeepMTA, described as the first interpretable deep learning model for multi-touch attribution. The key innovation is combining Phased-LSTMs (which handle variable time intervals between touchpoints via a time gate) with an additive feature explanation model based on Shapley regression values. Attribution credits are computed from the frozen LSTM via a mask-matrix powerset approach, solving the interpretability gap in prior deep learning MTA methods.

**Key contributions:**
- Phased-LSTM conversion model: handles time-decay and variable timestamp intervals via an oscillation-based time gate (parameters τ, ron, s)
- Shapley regression attribution: generates powerset mask matrix over clicking events, feeds masked journeys to frozen LSTM, runs linear regression on accuracy changes to assign feature importance
- First model to simultaneously consider: event sequence order, event frequency, and time-decay effect
- Empirical validation on eBay production data with 100k conversion journeys

**Methodology:**
Stage 1: Phased-LSTM trained on binary conversion prediction. The time gate kt controls cell state update based on timestamp intervals rather than just sequence position, allowing explicit modeling of recency effects. Stage 2: Frozen LSTM + Shapley regression. Generate all 2^n masked journeys (or sample for long journeys via Shapley sampling values), feed each through the frozen LSTM, compute accuracy drop per event mask, run linear regression Xmask·W = Yacc to obtain weights. Negative weights are clipped to 0 before normalization. AUC 0.91 on eBay test set.

**Main results:**
Conversion prediction AUC 0.91 on 10k held-out eBay journeys. GMV attribution: Natural Search 32.1%, Paid Search 20.5%, Affiliate 14.3%, Partner Integration 7.1%, Paid Social 3.4%, Social Media 1.8%, Display 1.7% (vs last-click's 100% to final channel). Compared against last-click baseline only.

---

## 2. Experiment Critique

**Design:**
Single eBay dataset (April 2018, 100k conversion journeys, 820k+ clicking events). Evaluation: (1) AUC on conversion prediction, (2) GMV allocation vs last-click. No multi-dataset evaluation. No comparison against other deep learning MTA methods.

**Statistical validity:**
Limited — no comparison against DARNN, DNAMTA, or Shapley baselines. The dataset excludes non-conversion journeys entirely (conversion rate <1%), introducing survivorship bias. Negative weight clipping is a non-trivial heuristic that could distort attribution in long journeys. The event independence assumption in the Shapley regression is explicitly acknowledged as a limitation.

**Online experiments (if any):**
N/A — offline classification evaluation only.

**Reproducibility:**
Code stated as publicly available. Dataset is proprietary eBay data. Architecture and hyperparameters fully specified (hidden units 1024, dropout 0.5, seq length 32, 300 epochs).

**Overall:**
Technically sound for its scope. The Phased-LSTM + Shapley combination is clean. The main weaknesses are the limited baselines and single proprietary dataset. Subsequent papers (CAMTA, CausalMTA) do not cite DeepMTA prominently, suggesting limited adoption as a standard baseline.

---

## 3. Industry Contribution

**Deployability:**
High. The two-stage approach (train LSTM, freeze, then apply Shapley regression) is a practical pattern for any black-box model interpretation. eBay production data gives it direct industry credibility.

**Problems solved:**
For dating platform attribution: the Phased-LSTM time gate is directly useful for handling variable time intervals between user interactions (e.g., days between a profile view and a message). The Shapley regression attribution can be applied to any trained sequential model without retraining, making it a low-cost interpretability add-on.

**Engineering cost:**
Low-moderate. Phased-LSTM adds one time gate parameter per LSTM cell — minimal overhead. The Shapley regression requires 2^n forward passes for short journeys (exponential in journey length), mitigated by sampling for long paths.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**
First to combine deep learning with cooperative game theory for MTA interpretability; first to simultaneously handle all three key journey features (sequence, frequency, time-decay) in a single end-to-end model.

**Prior work comparison:**
Ren et al. DARNN (2018): attention-based but not interpretable; Ji & Wang AMTA (2017): hazard rates for time decay but no deep learning; Dalessandro et al. (2012): Shapley but not sequential. DeepMTA bridges these approaches.

**Verification:**
Claims are reasonable for 2020 arXiv. Limited citation count suggests limited uptake as a benchmark. The Phased-LSTM for time-decay attribution is a valid contribution but similar to DNAMTA's time-decay attention.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| eBay Warehouse Dataset | Not public | No | 100k conversion journeys, April 2018 |

**Offline experiment reproducibility:**
Not reproducible — proprietary eBay data.

---

## 6. Community Reaction

arXiv 2020. ~80 citations. Limited adoption as standard benchmark. The two-stage Phased-LSTM + Shapley regression pattern is a practical contribution. Not included in major MTA benchmark comparisons (CAMTA, CausalMTA evaluate other baselines).

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| [2023_arXiv_GraphicalMTA_Graphical-Point-Process-Framework-Multi-Touch-Attribution](./2023_arXiv_GraphicalMTA_Graphical-Point-Process-Framework-Multi-Touch-Attribution.md) | Related Work | DeepMTA cited as prior interpretable deep MTA baseline; GraphicalMTA compares against it in point process framework |

---

## Meta Information

**Authors:** Dongdong Yang, Kevin Dyer, Senzhang Wang  
**Affiliations:** University of Southern California, eBay, Nanjing University of Aeronautics and Astronautics  
**Venue:** arXiv 2020  
**Year:** 2020  
**PDF:** https://arxiv.org/pdf/2004.00384.pdf  
**Relevance:** Core  
**Priority:** 3
