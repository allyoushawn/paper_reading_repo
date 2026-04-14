# Paper Analysis: Predicted Incrementality by Experimentation (PIE) for Ad Measurement

**Source:** https://arxiv.org/pdf/2304.06828.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Predicted Incrementality by Experimentation (PIE) for Ad Measurement  
**Authors:** Brett R. Gordon (Northwestern / NBER); Robert Moakler (Meta Ads Research); Florian Zettelmeyer (Northwestern / NBER)  
**Abstract:**  
PIE treats ad incrementality as a campaign-level supervised prediction problem: train on thousands of Meta “Conversion Lift” RCTs to map pre- and post-determined campaign features to incremental conversions per dollar (ICPD), including post-determined variables (test outcomes, exposure, last-click conversions) that would be invalid as controls in a causal model but carry predictive signal once RCTs identify treatment effects.

**Key contributions:**
- Formalization of why post-determined aggregates can predict heterogeneous RCT effects across campaigns.
- Random forest implementation with cost-weighted out-of-sample R² and ablations vs raw LCC-7D.
- Extensive extrapolation/stability diagnostics (new advertisers, vertical held-outs, simulation regimes).

**Methodology:**  
Campaign-level dataset construction from 2,226 Meta RCTs (Nov 2019–Mar 2020); ICPD target; random forest with 10-fold CV; comparisons to raw last-click metrics and ablated PIE variants.

**Main results:**  
Reported out-of-sample R² ≈ 0.88 (full PIE) vs ≈ 0.19 for raw 7-day last-click per dollar; lower decision disagreement vs RCT benchmarks than last-click in a stylized go/no-go exercise.

---

## 2. Experiment Critique

**Design:**  
Very large real RCT corpus; strong internal validity for Meta display-like settings; generalization caveats documented.

**Statistical validity:**  
Heavy emphasis on cross-campaign prediction metrics; acknowledges failure modes (negative correlation between baseline and effect collapses signal).

**Online experiments (if any):**  
Observational meta-analysis of historical RCTs rather than a new field experiment in the paper’s core tables.

**Reproducibility:**  
Data proprietary; simulation code paths referenced in appendix style materials.

**Overall:**  
High-quality industrial measurement science; not a touchpoint credit allocator by itself.

---

## 3. Industry Contribution

**Deployability:**  
Described as related to Meta Incremental Attribution practice and analogous Amazon calibration of ML MTA models.

**Problems solved:**  
Scales *prediction* of incrementality where running RCTs everywhere is costly.

**Engineering cost:**  
Requires continuous “shadow” RCT donor pool maintenance and monitoring feature drift.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
Reframing measurement as prediction-with-RCT-labels; legitimizing post-determined inputs as predictors.

**Prior work comparison:**  
Builds on Gordon et al. Facebook experiments, Lewis et al. digital ad measurement, Imbens & Rubin potential outcomes, ghost ads literature.

**Verification:**  
Closely related subsequent industry adoption notes (Amazon MTA calibration) cited in-text.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Meta Conversion Lift RCT sample (2,226 RCTs) | N/A | No | Proprietary |

**Offline experiment reproducibility:**  
Simulations partially characterizable; core empirical tables not reproducible externally.

---

## 6. Community Reaction

No significant community discussion found.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| [2025_arXiv_CausalCalibration_Amazon-Ads-Multi-Touch-Attribution](./2025_arXiv_CausalCalibration_Amazon-Ads-Multi-Touch-Attribution.md) | 4. Novelty vs. Prior Work | Unique survey token `PIE` (filename disambiguation) appears in scanned sections. |

---

## Meta Information

**Authors:** Brett R. Gordon; Robert Moakler; Florian Zettelmeyer  
**Affiliations:** Northwestern University / NBER; Meta Platforms  
**Venue:** arXiv  
**Year:** 2023  
**PDF:** https://arxiv.org/pdf/2304.06828.pdf  
**Relevance:** Core  
**Priority:** 1

---

## Project Relevance

**Low project relevance.** PIE’s native output is campaign-level ICPD (and related aggregates), not per-interaction fractional credit for supervised labeling of touchpoint sequences. The empirical application emphasizes discrete funnel conversion events; continuous outcomes like user-days-active are not specified. Sequences are collapsed to campaign aggregates (exposure, LCC counts), not heterogeneous per-event channels. The paper does discuss endogenous activity (clicks/exposure as proxies for latent user traits) as predictive signal, which is conceptually adjacent to “active users get more touches,” but it does not produce the per-touch credit targets your Phase 1 pipeline requires.

---

*[If datasets are accessible: To run experiments on these datasets, use the experiment-runner skill with the dataset URL or info above.]*
