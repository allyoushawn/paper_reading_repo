# Paper Analysis: An Attention-based Model for Conversion Rate Prediction with Delayed Feedback via Post-click Calibration

**Source:** https://www.ijcai.org/proceedings/2020/0487.pdf
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** An Attention-based Model for Conversion Rate Prediction with Delayed Feedback via Post-click Calibration
- **authors or company:** Yumin Su, Liang Zhang, Quanyu Dai, Bo Zhang, Jinyao Yan, Dan Wang, Yongjun Bao, Sulong Xu, Yang He, Weipeng Yan (JD.com; HK PolyU; Communication University of China)
- **venue:** IJCAI
- **year:** 2020
- **URL:** https://doi.org/10.24963/ijcai.2020/487
- **source type:** industry paper
- **direction:** D7
- **problem setting:** E-commerce display-ad CVR with sparse conversions and delayed feedback (seconds to weeks); static delay models ignore post-click behavior that changes conversion hazard over elapsed time \(e_i\).
- **objective and label definition:** Latent eventual conversion \(C\); observed label \(Y\); delay \(D\); elapsed time \(E\); post-click item sequence \(S_e\) within \([0, e_i]\) day slots; training week 2018-09-04 to 09-10, test 2018-09-12 on JingDong ad positions.
- **prediction or incrementality:** Predicts \(P(C=1|X,H)\) and day-slot hazard \(h(D|X,H,S_E)\)—absolute CVR, not incrementality.
- **model architecture:** Two-stage TS-DL: Stage 1 Telepath image embeddings for dense item representation; Stage 2 conversion model (GRU + self-attention + inner-attention over \(L=10\) click history) + dynamic delay model (two-layer GRU over post-click day slots, hazard \(\sigma(h_g(e))\)); joint EM with hidden \(C\), separate gradient updates for conversion and delay parameters.
- **credit assignment:** Candidate item features \(X_i\) and pre-click history \(H_i\); post-click calibration uses \(S_{e_i}\) (items clicked after candidate click through day \(e_i\)) to set time-varying hazard.
- **training data and counterfactual handling:** EM E-step assigns posterior weight \(w_i\) to censored \(Y=0\) samples using survival probabilities; M-step maximizes joint log-likelihood (Eq. 23); assumes \(P(C|X,H,E)=P(C|X,H)\).
- **offline and online evaluation:** Three JingDong datasets (WP1: 247,627 train / 33,703 test; WP2: 73,952 / 11,202; JD-MP: 415,270 / 68,415); AUC, RelaImpr vs DIN; rCVR calibration and \(\Delta\)rCVR gap; Jensen–Shannon divergence for delay distribution. No online A/B reported.
- **reported gains:** TS-DL RelaImpr vs DIN: WP1 +5.24%, WP2 +44.76%, JD-MP +8.02% AUC; ablation TS-DL/D drops 1.61–19% RelaImpr. JD-MP JS divergence vs DFM: 0.1229/0.0889 test/train (23.9% and 29.8% reduction stated). \(\Delta\)rCVR roughly 2× DFM on WP1/WP2.
- **applicability note for a two-sided dating recommender:** Post-click behavioral sequence to dynamically update hazard of eventual match/reply is analogous to using in-app activity after a profile view to calibrate delayed conversion labels.
  Single-sided product-ad CVR; no bilateral outcomes or subscription LTV.
- **unverified claims:** none

## 1. Summary

TS-DL is a two-stage deep CVR framework combining dense Telepath image embeddings (alleviating ID sparsity) with GRU/self-attention/inner-attention over click history. The delay model learns a dynamic day-slot hazard conditioned on post-click item sequences via two-layer GRU, departing from static exponential/non-parametric DFM assumptions. EM training treats unobserved conversions as latent \(C\). Experiments on three JD.com ad datasets show consistent AUC and delay-distribution gains over DFM, DIN, and ablations.

## 2. Experiment Critique

Strengths: novel use of post-click sequences for time-varying hazard; thorough ablations (TS-DL/I, /S, /D); calibration metrics beyond AUC. Weaknesses: one-week train / one-day test window; no production online eval; all rCVR < 1 (systematic underestimation remains).

## 3. Industry Contribution

JD.com industrial ad stack; Telepath embeddings reduce reliance on sparse IDs. Complexity \(O((n+k)L(sL+(n+k)N^2)(|I_0|+|I_1|))\) with \(N\) max post-click days.

## 4. Novelty vs. Prior Work

Dynamic hazard using post-click \(S_E\) vs static DFM (Chapelle 2014), non-parametric delay (Yoshikawa & Imai 2018). Attention over click history extends DIN (Zhou et al. 2018) to CVR with delay.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| WP1, WP2, JD-MP | JingDong ad platform | No | One-week train, one-day test |

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

### (1) Ranking objective: retention / LTV / revenue vs CTR
Post-click conversion probability only.

### (2) Credit assignment: user-level delayed outcome → item-level decision
Post-click browsing sequence calibrates hazard for the original clicked candidate.

### (3) Label and horizon definitions; delay, sparsity, censoring
Day-slot survival model; EM for censored negatives; \(L=10\) click history.

### (4) Short vs long-term head fusion
Joint EM over conversion and delay heads with separate parameter updates.

### (5) Prediction vs incrementality
Absolute CVR and delay distribution.

### (6) Offline and online evaluation
Offline AUC, rCVR, JS divergence only.

### (7) Reciprocity, congestion, fairness, revenue vs match quality
Not specified in source.

### (8) Migration path from CTR-like model toward unified long-term model
Pre-trained click/impression embeddings → attention CVR head + post-click-calibrated delay survival module.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Yumin Su, Liang Zhang, Quanyu Dai, Bo Zhang, Jinyao Yan, Dan Wang, Yongjun Bao, Sulong Xu, Yang He, Weipeng Yan
**Affiliations:** JD.com; Hong Kong Polytechnic University; Communication University of China
**Venue:** IJCAI 2020
**Year:** 2020
**PDF:** https://www.ijcai.org/proceedings/2020/0487.pdf
**Relevance:** Core
**Priority:** 2
