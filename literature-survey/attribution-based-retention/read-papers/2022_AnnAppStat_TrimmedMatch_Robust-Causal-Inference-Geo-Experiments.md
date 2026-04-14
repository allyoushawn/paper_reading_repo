# Paper Analysis: Robust Causal Inference for Incremental Return on Ad Spend with Randomized Paired Geo Experiments

**Source:** https://arxiv.org/pdf/1908.02922.pdf  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** Robust Causal Inference for Incremental Return on Ad Spend with Randomized Paired Geo Experiments  
**Authors:** Yixin Chen, Aiyou Chen (Google)  
**Abstract:**
This paper introduces Trimmed Match, a robust estimator for Incremental Return on Ad Spend (iROAS) from randomized geo experiments. The estimator is based on the trimmed mean of pair-level ratios εᵢ(θ) = Yᵢ − θXᵢ, where Y is revenue difference and X is spend difference for each geo pair. The key innovation is that outlier pairs (with extreme spend differences) are trimmed adaptively, addressing the heavy-tailed distribution problem inherent in geo-level data.

**Key contributions:**
- Trimmed Match estimator: adaptively trims geo pairs with extreme spending variation to reduce variance
- Confidence interval construction for iROAS via grid search on θ with trimmed mean test statistics
- Proof of asymptotic normality under trimming; coverage guarantees
- Empirical comparison across 7 real Google ad campaigns showing significant variance reduction vs. empirical mean ratio estimator

**Methodology:**
For each candidate θ, compute the pair-level residuals εᵢ(θ) = Yᵢ − θXᵢ. The trimmed match estimator finds θ̂ such that the trimmed mean of εᵢ(θ̂) = 0. Confidence intervals are inverted test intervals: all θ values for which the trimmed mean test does not reject at level α. The trim fraction δ is chosen by minimizing the estimated variance of the estimator.

**Main results:**
In simulation with Log-Normal noise (r=0.5, n=40 pairs): Trimmed Match RMSE = 1.96 vs. empirical mean ratio RMSE = 20.09. On 7 real Google geo experiments: Trimmed Match produced tighter confidence intervals in all 7 cases. Real case study A: CI [0.25, 1.74] (Trimmed Match) vs. [-1.26, 5.69] (empirical), enabling a clear positive decision.

---

## 2. Experiment Critique

**Design:**
Simulation study: Log-Normal, Laplace, and Cauchy noise distributions; varying pair count n (20–80); varying correlation r; 1000 replications. Real data: 7 Google ad campaigns with paired geo designs, pre-period covariate adjustment.

**Statistical validity:**
Asymptotic normality proof is rigorous. 1000 simulation replications is adequate. Real-data results are anecdotal (7 campaigns, no ground truth iROAS), but the CI width comparisons are directionally consistent. Honest acknowledgment of dependence on the paired design randomization.

**Online experiments (if any):**
The paper uses real geo experiments from Google's advertising infrastructure, though results are presented in aggregate/anonymized form.

**Reproducibility:**
R implementation available as the `trimmed.match` package (open-sourced by Google). Simulation specifications described in detail.

**Overall:**
Strong practical contribution. The method directly solves a critical problem in geo-based incrementality measurement. The robustness to heavy-tailed noise is the key value. Main limitation: requires paired randomized geo assignment (cannot be used with observational geo data or non-paired designs).

---

## 3. Industry Contribution

**Deployability:**
Very high. Google open-sourced the R package `trimmed.match`. The method is production-ready and directly applicable to any geo-based incrementality test (advertising or product experiments). The paired geo design is a standard experimental unit in marketing measurement.

**Problems solved:**
Directly addresses the dating platform attribution problem: when running geo holdout experiments to estimate the causal effect of a feature (e.g., a new matching algorithm), geo pairs with unusual spend/activity differences will dominate the iROAS estimate. Trimmed Match suppresses these outlier pairs, giving a valid CI.

**Engineering cost:**
Low. The R package `trimmed.match` provides the full estimator. Only requirement is a paired geo experimental design, which is standard in A/B experimentation infrastructure.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**
First formal treatment of trimming for iROAS estimation in geo experiments; extends classical trimmed mean theory to ratio estimation with randomized geo pairs.

**Prior work comparison:**
Prior work (e.g., Google's GeoX, Jin et al. 2017) used the empirical ratio Σ Yᵢ / Σ Xᵢ, which is vulnerable to outlier geo pairs. Trimmed Match is the first principled robust alternative with formal guarantees.

**Verification:**
Claims hold up. The `trimmed.match` R package is used in practice at Google. The companion paper "Trimmed Match Design" (Caramanis et al., arXiv:2105.07060) extends to the experimental design question of how to choose geo pairs — confirming adoption in the broader research program.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Synthetic simulations | Generated by authors | Yes (via R code) | Log-Normal, Laplace, Cauchy |
| 7 Google geo campaigns | Not public | No | Anonymized internal data |

**Offline experiment reproducibility:**
Simulation fully reproducible via R code. Real campaign data is not public.

---

## 6. Community Reaction

The paper has ~100 citations and is widely cited in the geo-experimentation literature. The `trimmed.match` R package is a standard tool in the causal advertising measurement community. No controversies.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| [2021_arXiv_TrimmedMatchDesign_Randomized-Paired-Geo-Experiments](./2021_arXiv_TrimmedMatchDesign_Randomized-Paired-Geo-Experiments.md) | Introduction | Trimmed Match (estimation) is the companion paper to TMD (design); TMD explicitly extends Trimmed Match by adding the design phase |
| [2022_DoorDash_Switchback_Incrementality-App-Marketplace-Search-Ads](./2022_DoorDash_Switchback_Incrementality-App-Marketplace-Search-Ads.md) | Related Work | Trimmed Match geo experiments cited as gold-standard when geo-targeting is available; DoorDash switchback fills the gap when it is not |

---

## Meta Information

**Authors:** Yixin Chen, Aiyou Chen  
**Affiliations:** Google  
**Venue:** Annals of Applied Statistics 2022  
**Year:** 2022  
**PDF:** https://arxiv.org/pdf/1908.02922.pdf  
**Relevance:** Core  
**Priority:** 1
