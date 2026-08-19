# Paper Analysis: Dual Learning Algorithm for Delayed Conversions

**Source:** https://doi.org/10.1145/3397271.3401282
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** Dual Learning Algorithm for Delayed Conversions
- **authors or company:** Yuta Saito, Gota Morishita, Shota Yasui (Tokyo Institute of Technology / independent / CyberAgent)
- **venue:** SIGIR (short paper)
- **year:** 2020
- **URL:** https://doi.org/10.1145/3397271.3401282
- **source type:** academic (CyberAgent co-author)
- **direction:** D7
- **problem setting:** Display-ad CVR prediction under delayed feedback where conversions may arrive hours/days after click; combines positive-unlabeled (unconverted-so-far ≠ confirmed negative) and MNAR (decisive users observed sooner) biases without parametric delay-distribution assumption.
- **objective and label definition:** Predict true CVR γ(X)=P(Y=1|X); observed label Y_obs = O·Y where O indicates whether true conversion is observed by training time given elapsed time E since click; training periods L ∈ {0.5, 1, 2, 4} days in synthetic eval.
- **prediction or incrementality:** Prediction only—IPS/ICVR reweighting corrects label-observation bias (PU+MNAR), not causal treatment/incremental exposure effects.
- **model architecture:** Logistic regression for CVR predictor f and propensity estimator g; alternating dual training (Algorithm 1): fix g, update f via IPS-weighted CVR loss; fix f, update g via ICVR-weighted propensity loss; non-negative variant nnDLA-DF clips per-sample IPS loss at zero (Eq. 5) to reduce variance at cost of bias.
- **credit assignment:** Single click-to-conversion event level—no multi-item slate or multi-step funnel attribution.
- **training data and counterfactual handling:** Synthetic only (Algorithm 2): N=100,000 units, p=30 features, sigmoid-linear true CVR, exponential or normal delay distributions; dual IPS/ICVR estimators jointly correct PU and MNAR without assuming exponential delay (unlike DFM).
- **offline and online evaluation:** Offline synthetic only: relative log-loss vs unobservable Oracle logistic model, mean±std over 10 iterations, across delay families and training-period lengths L; no real-world or online evaluation.
- **reported gains:** Normal delay (Figure 1 right): nnDLA-DF lower relative log-loss than DFM and Naive across L=0.5–4 days, largest advantage at short L; exponential delay (Figure 1 center): DFM wins when its exponential assumption holds; nnDLA-DF competitive/stable without parametric assumption. No numeric log-loss values stated in text.
- **applicability note for a two-sided dating recommender:** MNAR insight (decisive/engaged users observed sooner) conceptually relevant to retention-label bias when active users show delayed outcomes faster—but method validated only on synthetic single-event ad data.
- **applicability note for a two-sided dating recommender:** Joint PU+MNAR framing is useful for designing delayed match/retention labels; no reciprocity, congestion, or real-world validation.
- **unverified claims:** "Stable prediction performance across a wide range of situations" inferred from four synthetic L settings and two delay families only.

## 1. Summary

**Title:** Dual Learning Algorithm for Delayed Conversions (DLA-DF)
**Authors:** Yuta Saito, Gota Morishita, Shota Yasui
**Abstract:** Proposes unbiased IPS CVR estimator and ICVR propensity estimator trained alternately to jointly address PU and MNAR delayed-feedback biases without parametric delay assumptions; evaluates on synthetic data vs Oracle, Naive, and DFM.

**Key contributions:**
- Dual learning algorithm (Algorithm 1) alternating CVR and propensity updates.
- Theoretical unbiasedness proofs for IPS and ICVR estimators.
- Non-negative variance-reduction variant nnDLA-DF.

**Methodology:** Inverse propensity weighting for CVR + inverse CVR weighting for propensity estimation; logistic models in experiments.

**Main results:** nnDLA-DF outperforms baselines under non-exponential delay and short training windows; DFM wins when exponential assumption holds.

## 2. Experiment Critique

**Design:** Clean separation of PU vs MNAR problems; compares to DFM under matched and violated assumptions.

**Statistical validity:** 10-iteration means with std on synthetic data.

**Online experiments (if any):** None.

**Reproducibility:** Synthetic generation procedure described (Algorithm 2); no released dataset file.

**Overall:** Theoretically sound short paper limited by synthetic-only evaluation.

## 3. Industry Contribution

**Deployability:** Algorithmic contribution; CyberAgent affiliation but no production deployment reported.

**Problems solved:** Joint delayed-feedback debiasing for CPA display advertising CVR.

**Engineering cost:** Lightweight logistic dual training; nnDLA-DF trades bias for variance reduction.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First method jointly solving PU and MNAR delayed conversion problems without parametric delay distribution.

**Prior work comparison:** vs Chapelle DFM (exponential delay, no MNAR), Yoshikawa non-parametric delay (no MNAR), Ktena et al. IPS (MNAR only, no PU).

**Verification:** Synthetic experiments support relative rankings; no real-log validation.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Synthetic (Algorithm 2) | N/A | Generation procedure only | N=100,000, p=30 features |

**Offline experiment reproducibility:** Procedure specified; no public data release.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** CVR point prediction for ad ranking/eCPM—not retention/LTV ranking.

**(2) Credit assignment:** Single-event click→conversion; no multi-step dating funnel.

**(3) Label and horizon definitions:** Elapsed time E since click determines observation propensity θ(X,E); training windows L up to 4 days in synthetic eval; PU treatment of Y_obs=0.

**(4) Short-term + long-term heads:** Not applicable—single CVR head with debiased loss.

**(5) Prediction vs incrementality:** Label-bias correction, not uplift.

**(6) Offline and online evaluation:** Synthetic log-loss only; no delayed retention metrics or A/B.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Not addressed.

**(8) Migration path from CTR-like model to unified long-term model:** Not specified.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Yuta Saito, Gota Morishita, Shota Yasui
**Affiliations:** Tokyo Institute of Technology; CyberAgent, Inc.
**Venue:** SIGIR 2020 (short research papers)
**Year:** 2020
**PDF:** https://doi.org/10.1145/3397271.3401282
**Relevance:** Related
**Priority:** 3
