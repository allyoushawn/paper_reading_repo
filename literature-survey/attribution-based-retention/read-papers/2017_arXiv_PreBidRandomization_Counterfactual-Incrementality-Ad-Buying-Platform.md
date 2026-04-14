# Paper Analysis: Counterfactual-based Incrementality Measurement in a Digital Ad-Buying Platform

**Source:** https://arxiv.org/pdf/1705.00634.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Counterfactual-based Incrementality Measurement in a Digital Ad-Buying Platform  
**Authors:** Prasad Chalasani, Ari Buchalter, Jaynth Thiagarajan (MediaMath); Ezra Winston (Carnegie Mellon University)  
**Abstract:**  
The paper develops a randomization-based methodology for causal ad lift measurement suited to DSP constraints in RTB: pre-bid test/control assignment to avoid paying for control impressions, correction for auction win bias (non-compliance), Gibbs sampling for confidence intervals on lift metrics, and Connected-ID (CID) aggregation to mitigate ID contamination and SUTVA violations.

**Key contributions:**
- Pre-bid randomization with phantom control logging so advertisers do not pay for control-group bids.
- ATT estimation under one-sided non-compliance using win-rate adjustment; Gibbs sampling (Beta–Binomial) for credible intervals on ATT / ATL / incrementality.
- CID-level analysis with optional restriction to CIDs linking multiple device identifiers to reduce cross-device/cookie contamination.

**Methodology:**  
Potential-outcomes framing; clinical-trials-style non-compliance mapping to test-win / test-loss / control populations; generative model + MCMC for posterior uncertainty; empirical evaluation on seven MediaMath campaigns over 30 days (March 2017) with large-scale bid/impression/event logs.

**Main results:**  
Reported stable positive causal lift (ATL/INC) across campaigns where naive methods often show marginal, null, or negative lift; contrasts with uncorrected win bias and ID contamination failure modes.

---

## 2. Experiment Critique

**Design:**  
Real production-style RCT-style splits with strong engineering narrative; baselines are conceptual (post-bid randomization cost, ghost ads infeasibility for DSPs) rather than shared public benchmarks.

**Statistical validity:**  
Bayesian Gibbs intervals; emphasizes identification challenges (win bias, contamination). Classical frequentist properties less central.

**Online experiments (if any):**  
Observational campaign log analyses rather than a single clean public A/B replication artifact.

**Reproducibility:**  
Proprietary MediaMath logs; methodology is detailed but not directly reproducible on public data.

**Overall:**  
Compelling industry measurement paper for DSP incrementality; not a generic MTA dataset contribution.

---

## 3. Industry Contribution

**Deployability:**  
Explicitly designed for DSP operational constraints (pre-bid hash assignment, logging semantics).

**Problems solved:**  
Credible aggregate incrementality under RTB non-compliance and identifier fragmentation.

**Engineering cost:**  
Requires CID graph quality, sustained logging of bid opportunities, and MCMC infrastructure.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
First detailed end-to-end DSP-feasible causal lift system combining pre-bid randomization, non-compliance math, Gibbs CIs, and CID fixes.

**Prior work comparison:**  
Contrasts ghost ads (walled gardens), post-bid PSA waste, observational attribution.

**Verification:**  
Widely cited in subsequent industry measurement discussions; aligns with mid-2010s DSP measurement practice.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| MediaMath DSP logs (7 campaigns, 30-day window ending 2017-03-21) | N/A | No | Proprietary |

**Offline experiment reproducibility:**  
Not reproducible without proprietary logs and CID infrastructure.

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

**Authors:** Prasad Chalasani; Ari Buchalter; Jaynth Thiagarajan; Ezra Winston  
**Affiliations:** MediaMath; Carnegie Mellon University  
**Venue:** arXiv (2017)  
**Year:** 2017  
**PDF:** https://arxiv.org/pdf/1705.00634.pdf  
**Relevance:** Core  
**Priority:** 2

---

## Project Relevance

**Low project relevance.** The method targets aggregate campaign incrementality (ATT/ATL/INC) for exposed populations, not per-interaction fractional credit suitable as supervised labels for multi-touch paths. The paper states ICE is impossible to compute directly and focuses on population averages; outcomes are framed as binary (or integer conversion counts per userID), not continuous user-days-active; single-campaign scope with future work for multi-campaign/channel interaction.

---

*[If datasets are accessible: To run experiments on these datasets, use the experiment-runner skill with the dataset URL or info above.]*
