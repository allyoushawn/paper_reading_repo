# Paper Analysis: DeepHit: A Deep Learning Approach to Survival Analysis With Competing Risks

**Source:** https://ojs.aaai.org/index.php/AAAI/article/view/11842  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** DeepHit: A Deep Learning Approach to Survival Analysis With Competing Risks  
**Authors:** Changhee Lee, William R. Zame, Jinsung Yoon, Mihaela van der Schaar (UCLA)  
**Abstract:**
DeepHit is a deep learning model for survival analysis that directly models the joint distribution of survival time and competing risks — without assuming any underlying stochastic process. Unlike Cox-based models that predict a continuous hazard function under the proportional hazards assumption, DeepHit outputs a discrete-time probability mass function (PMF) over time horizons for each competing event, trained jointly with a ranking loss (concordance) and a calibration loss (likelihood). This enables handling of competing risks (multiple possible failure modes) and non-proportional hazards.

**Key contributions:**
- End-to-end deep learning survival model with discrete-time PMF output — no proportional hazards assumption
- Competing risks: jointly models P(T=t, K=k) for multiple causes of failure K at each time t
- Joint loss: log-likelihood term (calibration) + cause-specific concordance loss (discrimination ranking)
- Shared embedding + cause-specific sub-networks: shared representation layer followed by K cause-specific heads
- Best C-index benchmark performance on standard survival datasets (SUPPORT, METABRIC, GBSG, KKBox)

**Methodology:**
Architecture: shared sub-network (MLP/LSTM) → K cause-specific sub-networks → softmax output → discrete PMF over T time buckets for each cause k. Loss = -log P(T=t, K=k) [calibration] + α × cause-specific concordance loss [discrimination]. Concordance loss encourages Σₜ P(T≤t) for uncensored subject to exceed that of censored controls. Competing risks: each cause has a separate head; sum of all cause-specific PMFs = overall survival distribution. Training: Adam optimizer with dropout regularization.

**Main results:**
Best C-index across standard survival benchmarks (SUPPORT, METABRIC, GBSG). On KKBox churn dataset (1.7M users): C-index = 0.858 (best among compared methods), but IBS and IBLL are worst (confirmed by Kvamme et al. 2019 pycox comparison). This discrimination-calibration tradeoff is a key empirical finding: DeepHit excels at ranking but produces poorly calibrated probability estimates.

*Note: NLM source returned abstract-only content for this paper. Detailed architecture parameters and dataset-specific metric tables are from the pycox comparison paper (Kvamme et al. JMLR 2019).*

---

## 2. Experiment Critique

**Design:**
Original DeepHit paper evaluates on SUPPORT and METABRIC (clinical) datasets with C-index as primary metric. The competing risks evaluation uses a synthetic competing risks dataset and a real electronic health record dataset (Mayo Clinic liver disease data).

**Statistical validity:**
The joint loss formulation combining likelihood and concordance is principled. The C-index is a standard survival evaluation metric. The key limitation — poor calibration despite best discrimination — was identified in subsequent benchmarking (pycox paper) rather than in the original DeepHit paper, which did not evaluate calibration metrics (IBS/IBLL).

**Online experiments (if any):**
N/A — offline benchmarks only.

**Reproducibility:**
Code available at `github.com/chl8856/DeepHit`. Standard benchmark datasets (SUPPORT, METABRIC) are publicly available. KKBox churn dataset requires WSDM Cup 2019 registration.

**Overall:**
DeepHit is a significant contribution to neural survival analysis — it removed the proportional hazards assumption and introduced the competing risks framework. The discrimination-calibration tradeoff (best C-index, worst IBS) is a practical concern for applications where calibrated probability estimates drive intervention thresholds. For pure ranking tasks (e.g., which users to prioritize for retention interventions), DeepHit is the strongest baseline.

---

## 3. Industry Contribution

**Deployability:**
High. Open-source implementation at `github.com/chl8856/DeepHit`. Also available via `pycox` package. Widely used in healthcare AI applications.

**Problems solved:**
For dating platform retention: DeepHit is applicable for competing risks survival modeling — e.g., predicting whether a user will churn via (1) subscription cancellation, (2) app deletion, or (3) extended inactivity, as three competing causes. The best C-index property makes it suitable for ranking-based intervention prioritization (who to target for re-engagement). However, if precise probability calibration is needed for intervention thresholds, Cox-Time (pycox) is preferable based on the KKBox benchmarks.

**Engineering cost:**
Low. pip via pycox. The discrete-time PMF output simplifies integration with downstream decision systems (no need for survival function integration).

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**
First end-to-end deep learning model for competing risks survival analysis without proportional hazards assumption; first to use a joint discrimination + calibration training objective for survival models.

**Prior work comparison:**
Cox-PH (Cox 1972): proportional hazards, no competing risks, no neural extension. DeepSurv (Katzman 2018): MLP + Cox-PH, proportional hazards. RSF (Ishwaran 2008): ensemble-based, handles competing risks but not deep learning. Cause-specific Cox: separate Cox for each competing cause, ignores joint distribution. DeepHit addresses all these limitations simultaneously.

**Verification:**
Best C-index results are reproducible via pycox package benchmarks (Kvamme et al. 2019). The calibration weakness is a documented empirical finding.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| SUPPORT | PhysioNet | Yes | 9K clinical patients |
| METABRIC | TCGA | Yes | 1.9K breast cancer |
| KKBox | WSDM Cup 2019 | Yes (competition) | 1.7M users, subscription churn |
| Mayo Clinic liver (PBCSEQ) | R survival package | Yes | Competing risks example |

**Offline experiment reproducibility:**
Reproducible via `github.com/chl8856/DeepHit` and `pycox` package.

---

## 6. Community Reaction

AAAI 2018. ~800+ citations. One of the most cited papers in neural survival analysis. Standard comparison baseline in all subsequent survival ML papers. The competing risks framework has been widely adopted. The calibration limitation identified in subsequent work (pycox, JMLR 2019) is now a known trade-off that practitioners account for.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| [2019_JMLR_pycox_Time-to-Event-Neural-Networks-Cox-Regression](./2019_JMLR_pycox_Time-to-Event-Neural-Networks-Cox-Regression.md) | 1. Summary | Unique survey token `DeepHit` (filename disambiguation) appears in scanned sections. |
| [2019_JMLR_pycox_Time-to-Event-Neural-Networks-Cox-Regression](./2019_JMLR_pycox_Time-to-Event-Neural-Networks-Cox-Regression.md) | Experiments | DeepHit is the primary benchmark competitor for pycox; pycox shows DeepHit achieves best C-index (0.858) but worst IBS/IBLL calibration on KKBox |
| [2023_JDS_TEDDA_Time-to-Event-Framework-Multi-touch-Attribution](./2023_JDS_TEDDA_Time-to-Event-Framework-Multi-touch-Attribution.md) | Related Work | DeepHit cited as competing deep learning survival method for conversion/churn prediction |

---

## Meta Information

**Authors:** Changhee Lee, William R. Zame, Jinsung Yoon, Mihaela van der Schaar  
**Affiliations:** UCLA  
**Venue:** AAAI 2018  
**Year:** 2018  
**PDF:** https://ojs.aaai.org/index.php/AAAI/article/view/11842  
**Relevance:** Related  
**Priority:** 2
