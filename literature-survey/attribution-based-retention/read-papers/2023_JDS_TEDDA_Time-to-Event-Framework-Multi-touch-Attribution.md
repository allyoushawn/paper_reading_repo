# Paper Analysis: A Time To Event Framework For Multi-touch Attribution

**Source:** https://arxiv.org/pdf/2009.08432.pdf  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** A Time To Event Framework For Multi-touch Attribution  
**Authors:** Dinah Shender, Ali Nasiri Amini, Xinlong Bao, Mert Dikmen, Amy Richardson, Jing Wang (Google)  
**Abstract:**
This paper proposes TEDDA (Time to Event Data Driven Attribution), an MTA system that models user conversions as occurrences in an inhomogeneous Poisson process with time-varying ad effects. The two key requirements addressed are: (1) handling right-censored data (incomplete journeys where a user hasn't converted yet), and (2) capturing time-varying ad effects (recency decay). The attribution algorithm is backwards elimination — distributing credit from the last ad backward, assigning synergy entirely to the later ad, which is theoretically preferred for real-time bidding scenarios.

**Key contributions:**
- TEDDA: conversion modeled as inhomogeneous Poisson process with log-linear intensity λ(t) incorporating time-decaying ad effects
- Backwards elimination credit algorithm: raw credit for ad j = λ̂(t*, A(j)) − λ̂(t*, A(j−1)), propagating backwards through the journey
- Handles right-censored data naturally (unlike binary outcome models)
- Handles time-varying ad effects via mixture of exponentials, splines, or step functions
- Theoretical comparison of backwards elimination vs Shapley values for synergy handling: backwards elimination assigns all synergy to later ad (preferred for bidding); Shapley splits evenly
- Authored by Google — directly relevant to production advertising systems

**Methodology:**
log(λ(t)) = α0 + Σⱼ fⱼ(t−tⱼ), where fⱼ captures the time-decaying effect of the j-th ad. Parameters estimated via log-likelihood for inhomogeneous Poisson process (reduces to Cox proportional hazards for single-conversion users). Multiple parameterizations supported: exponential decay basis, splines, step functions. Attribution: backwards elimination starting from conversion time t*, removing ads one by one from the end, attributing credit = drop in estimated intensity at t*.

**Main results:**
Simulation studies (500 synthetic datasets × 1M users × 30 days): accurate parameter recovery across 4 scenarios. Scenario 1 (short/medium/long decay): estimates match ground truth to 3 decimal places (exp(β1)=2.000 vs GT 2.0). AICPE matches theoretical ICPE across all scenarios (e.g., 13.87% vs 13.87% in Scenario 4). Limitation identified: sparse conditions (3 ads of same type within 24hrs, ~262 users) produce poor estimates (GT 8.0, est 4.9, wide CI).

---

## 2. Experiment Critique

**Design:**
Simulation-only study (no real advertising dataset). Four synthetic scenarios covering single ad, two ad types, zero-effect ad, and variable ad counts. 500 replications per scenario with 1M users each.

**Statistical validity:**
Strong for simulation — accurate parameter recovery with tight CIs in most settings. The identified failure mode (rare multi-ad conditions) is honest and informative. No comparison against deep learning MTA baselines — the paper focuses on the statistical framework, not predictive accuracy competition.

**Online experiments (if any):**
N/A.

**Reproducibility:**
No code released. Simulation setup fully described and reproducible.

**Overall:**
A solid statistical framework paper from Google, positioned between survival analysis and MTA. The backwards elimination algorithm is principled and theoretically justified for bidding use cases. The limitation of assuming ad independence is honestly acknowledged. Main gap is lack of empirical validation on real data.

---

## 3. Industry Contribution

**Deployability:**
High. Log-linear Poisson process with time-decaying effects is a well-understood statistical model. The backwards elimination algorithm is simple and interpretable. Google authorship implies potential production deployment in AdWords/DV360.

**Problems solved:**
For dating platform attribution: TEDDA's handling of right-censored data is directly relevant — many users who receive messages or matches will not convert (retain) within the observation window. The time-varying ad effect captures the reality that a message sent 30 days ago has less influence on current retention than one sent yesterday. The backwards elimination algorithm provides a natural way to attribute retention to the most recent engagement while not ignoring earlier ones.

**Engineering cost:**
Low. Log-linear Poisson regression is simpler than LSTM-based models. The time-decay function can be as simple as a step function (3 coefficients per ad type). No GPU infrastructure required.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**
First MTA framework explicitly satisfying both right-censoring and time-varying ad effects requirements; first theoretical comparison of backwards elimination vs Shapley for synergy handling in the bidding context.

**Prior work comparison:**
Du et al. (2019): combines timestamps with deep learning + Shapley but ignores right-censoring; Zhang et al. (2014), Xu et al. (2014): Poisson process MTA but no right-censoring handling or path-level attribution; Dalessandro et al. (2012), Shao & Li (2011): sequence-only logistic regression + Shapley, no timestamps.

**Verification:**
Claims hold up for the simulation setting. The backwards elimination / Shapley comparison is mathematically rigorous. Absence of real data validation is a gap.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Synthetic Simulation | Generated by authors | Yes (described) | 500 datasets × 1M users × 30 days |

**Offline experiment reproducibility:**
Reproducible from description — no code, but simulation setup is fully specified.

---

## 6. Community Reaction

arXiv 2020 (Journal of Data Science 2023). Google authorship. ~40 citations. Niche impact — the survival analysis approach to MTA is less common than deep learning approaches, but the backwards elimination algorithm has been cited as a principled alternative to Shapley for bidding contexts.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** Dinah Shender, Ali Nasiri Amini, Xinlong Bao, Mert Dikmen, Amy Richardson, Jing Wang  
**Affiliations:** Google  
**Venue:** Journal of Data Science 2023 (arXiv 2020)  
**Year:** 2023  
**PDF:** https://arxiv.org/pdf/2009.08432.pdf  
**Relevance:** Core  
**Priority:** 3
