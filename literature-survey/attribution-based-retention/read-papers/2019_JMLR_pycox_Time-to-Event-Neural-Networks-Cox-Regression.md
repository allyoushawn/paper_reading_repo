# Paper Analysis: Time-to-Event Prediction with Neural Networks and Cox Regression

**Source:** https://jmlr.org/papers/volume20/18-424/18-424.pdf  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** Time-to-Event Prediction with Neural Networks and Cox Regression  
**Authors:** Håvard Kvamme, Ørnulf Borgan, Ida Scheel (University of Oslo)  
**Abstract:**
This JMLR paper proposes neural network extensions of the Cox proportional hazards model for time-to-event prediction (survival analysis). Three models are introduced: Cox-SGD (linear Cox trained via stochastic gradient descent with case-control sampling), Cox-MLP (nonlinear multilayer perceptron with the same CC loss), and Cox-Time (extends Cox to non-proportional hazards by including time as an explicit covariate). The paper introduces a nested case-control sampling loss that approximates the full Cox partial likelihood with just one control per event, enabling large-scale training. All models are implemented in the open-source `pycox` Python package.

**Key contributions:**
- Cox-SGD: linear Cox model trained with SGD using case-control (CC) sampling instead of full partial likelihood — makes Cox tractable on large datasets
- Cox-MLP (CC): nonlinear MLP with the same CC sampling loss — neural extension of Cox without proportionality constraints on individual covariates
- Cox-Time: Cox model with time t as an explicit input covariate — removes the proportional hazards assumption entirely; hazard ratio varies over time
- Nested case-control sampling: sample 1 control per event from risk set → approximate full partial likelihood; theoretical justification via nested case-control theory
- pycox package: `github.com/havakv/pycox` — unifies survival analysis neural network implementations
- Benchmarking: systematic comparison across 5 datasets + 6 methods using integrated Brier Score (IBS) and Integrated Binomial Log-Likelihood (IBLL) for calibration, and C-index for discrimination

**Methodology:**
Cox partial likelihood: L(β) = Π [e^η(xᵢ) / Σⱼ∈Rᵢ e^η(xⱼ)]. Full sum over risk set Rᵢ is O(n²) — intractable at scale. CC approximation: replace Rᵢ with {xᵢ} ∪ {one sampled control}, scales to O(n). Cox-Time: η(x,t) → LSTM or MLP with time input — predicts time-specific relative hazard. Four standard benchmark datasets: SUPPORT (9K clinical), METABRIC (1.9K breast cancer), Rotational/GBSG (2.2K breast cancer), FLCHAIN (7.9K serum immunoglobulin). Large-scale: KKBox music churn dataset (1.7M customers, 3M observations). Comparison baselines: DeepHit, RSF (Random Survival Forest), Cox-PH, DeepSurv, PC-Hazard.

**Main results:**
On KKBox (1.7M users): Cox-Time achieves best IBS = 0.107 and IBLL = −0.334 (best calibration). DeepHit achieves best C-index (0.858) but worst IBS and IBLL (worst calibration). On standard 4 benchmark datasets: Cox-Time generally competitive with DeepHit on C-index while maintaining superior calibration. Nested case-control with 1 control per risk set is sufficient — adding more controls does not significantly improve results on large datasets (KKBox experiment). Cox-MLP (CC) outperforms Cox-SGD (linear) across all datasets, confirming that nonlinearity helps.

---

## 2. Experiment Critique

**Design:**
Rigorous benchmarking with 5 datasets spanning clinical (SUPPORT, METABRIC, GBSG), protein (FLCHAIN), and consumer (KKBox churn) domains. Comparison across 6 methods with two complementary metrics: C-index (discrimination) and IBS/IBLL (calibration). The calibration vs discrimination tradeoff finding (DeepHit best C-index, worst IBS) is a key empirical contribution.

**Statistical validity:**
IBS and IBLL are proper scoring rules — theoretically correct for survival model evaluation. C-index measures discrimination only, not calibration. The paper correctly uses both. The nested case-control theory is solid (Goldstein & Langholz 1992 cited). Large-scale KKBox experiment with 1.7M users is a strong empirical validation.

**Online experiments (if any):**
N/A — all offline benchmarks on existing datasets.

**Reproducibility:**
Full open-source implementation at `github.com/havakv/pycox`. All 5 datasets are publicly accessible (KKBox via WSDM Cup 2019 competition data). Results fully reproducible.

**Overall:**
Strong methodological paper with rigorous benchmarking. The key insight — Cox-Time achieves best calibration at scale while DeepHit has best discrimination — is practically important for choosing survival models when calibrated probabilities matter (e.g., churn risk scoring for marketing interventions). The pycox package is a standard tool in the survival ML community.

---

## 3. Industry Contribution

**Deployability:**
Very high. The pycox package provides a single pip-installable library. Cox-Time is the recommended model when calibrated survival probabilities are needed (e.g., churn prediction where the probability itself drives marketing intervention thresholds, not just ranking).

**Problems solved:**
For dating platform retention: Cox-Time is directly applicable for predicting time-to-churn (time until subscription cancellation or app abandonment). The KKBox churn application (subscription music service) is structurally identical to dating platform subscription retention. Cox-Time calibration advantage means predicted churn probabilities can be used directly to threshold interventions (e.g., send retention push if predicted 30-day churn probability > 0.3).

**Engineering cost:**
Low. pip install pycox. The CC sampling loss reduces training complexity from O(n²) to O(n). KKBox results demonstrate scalability to 1.7M users.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**
First neural network extension of Cox that removes the proportional hazards assumption by including time as a covariate; first systematic calibration benchmarking of neural survival models showing the discrimination-calibration tradeoff.

**Prior work comparison:**
DeepSurv (Katzman et al. 2018): MLP + Cox-PH, proportional hazards; Cox-Time removes this constraint. DeepHit (Lee et al. AAAI 2018): discrete-time competing risks; best C-index but worst calibration on KKBox. RSF (Ishwaran et al. 2008): ensemble survival baseline. The key empirical finding (DeepHit vs Cox-Time tradeoff) motivates using Cox-Time when calibration matters.

**Verification:**
All claims reproducible via pycox package and public datasets.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| SUPPORT | PhysioNet | Yes | 9K clinical, 14 covariates |
| METABRIC | TCGA | Yes | 1.9K breast cancer, 9 covariates |
| Rotational/GBSG | pycox package | Yes | 2.2K breast cancer |
| FLCHAIN | R survival package | Yes | 7.9K serum |
| KKBox | WSDM Cup 2019 | Yes (competition) | 1.7M customers, subscription churn |

**Offline experiment reproducibility:**
Fully reproducible via `github.com/havakv/pycox`.

---

## 6. Community Reaction

JMLR 2019. ~400 citations. The `pycox` package is widely used in the survival analysis ML community. Frequently cited in healthcare AI and churn prediction work. The calibration vs discrimination benchmarking finding (DeepHit best C-index, Cox-Time best IBS) is now a standard reference point for choosing neural survival models.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| [2018_AAAI_DeepHit_Deep-Learning-Survival-Analysis-Competing-Risks](./2018_AAAI_DeepHit_Deep-Learning-Survival-Analysis-Competing-Risks.md) | 1. Summary | Unique survey token `pycox` (filename disambiguation) appears in scanned sections. |

---

## Meta Information

**Authors:** Håvard Kvamme, Ørnulf Borgan, Ida Scheel  
**Affiliations:** University of Oslo  
**Venue:** JMLR 2019  
**Year:** 2019  
**PDF:** https://jmlr.org/papers/volume20/18-424/18-424.pdf  
**Relevance:** Related  
**Priority:** 3
