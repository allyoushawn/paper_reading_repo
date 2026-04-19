# Paper Analysis: To Smooth or Not? When Label Smoothing Meets Noisy Labels

**Source:** https://proceedings.mlr.press/v162/wei22b/wei22b.pdf  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** To Smooth or Not? When Label Smoothing Meets Noisy Labels  
**Authors:** Jiaheng Wei, Hangyu Liu, Tongliang Liu, Gang Niu, Masashi Sugiyama, Yang Liu  
**Abstract:** Investigates whether label smoothing (LS) helps or hurts when learning with noisy labels. Shows that positive LS degrades performance in high-noise regimes due to "over-smoothing" the posterior. Introduces Negative/Not Label Smoothing (NLS) — using negative smooth rate r < 0 — which becomes more beneficial as noise rates increase. Several existing robust loss functions (loss correction, Peer Loss, NLNL) are shown to be special cases of NLS.

**Key contributions:**
- Identifies the phase transition: positive LS is optimal for clean/low-noise data, NLS outperforms LS at high noise rates
- Generalizes LS and NLS under a unified GLS framework: y_i^{GLS,r} := (1-r)·y_i + (r/K)·1 for r ∈ (-∞, 1]
- Theoretically proves NLS is beneficial when noise rate e ≥ r*/2 where r* is the optimal smoothing rate for clean data
- Bridges NLS to existing methods: loss correction (Patrini 2017), Peer Loss (Liu & Guo 2020), Negative Learning (Kim 2019)
- Shows warm-up with CE is required before applying NLS to avoid over-confident early convergence

**Methodology:**  
GLS unifies LS (r≥0) and NLS (r<0). For NLS, the smoothed label assigns 1+|r|/K to the target class and -|r|/K to non-target classes (probabilities still sum to 1). Theoretical analysis uses a noise transition matrix setup; Theorem 3.3 characterizes the phase transition between LS and NLS optimality. Warm-up: CE for 120 epochs, then NLS for 100 epochs.

**Main results:**  
CIFAR-10 Sym-60%: NLS 77.82% vs LS 75.01% vs CE 74.04%. CIFAR-100 Sym-60%: NLS 46.58% vs LS 41.63% vs CE 38.27%. Clothing-1M: NLS 74.24% (4th among 21 methods) vs CE 68.94% vs LS 73.44%. CIFAR-10N Worst: NLS 82.99% vs CE 77.69% vs LS 82.76%. CIFAR-100N Fine: NLS 58.59% vs CE 55.50%.

---

## 2. Experiment Critique

**Design:**  
Extensive multi-dataset evaluation: synthetic 2D datasets, UCI tabular, CIFAR-10/100 (symmetric + asymmetric noise), AGNews NLP, CIFAR-N, Clothing-1M. Coverage of multiple noise types and scales is thorough. Theorems backed by empirical phase-transition visualization. Comparison against Bootstrap, FLC, BLC, SCE, APL, Peer Loss, ELR, AUM, F-div.

**Statistical validity:**  
UCI experiments use two-sample T-test (5 non-negative vs. 5 negative smooth rates) to verify overall significance. Multiple runs with ResNet34. T-test p-values reported.

**Online experiments (if any):**  
None.

**Reproducibility:**  
Code released at https://github.com/UCSC-REAL/negative-label-smoothing. Simple implementation: standard CE warm-up then change smooth rate. No additional components needed.

**Overall:**  
Important conceptual contribution revealing that negative label smoothing — previously overlooked — is a powerful and simple technique for high-noise settings. Limitation: the optimal negative smooth rate depends on the unknown noise rate. Warm-up requirement adds a training complication. NLS does not achieve absolute SOTA (ranks 4th on Clothing-1M), but the simplicity and theoretical backing make it a useful component technique.

---

## 3. Industry Contribution

**Deployability:**  
Extremely low-cost modification: replace the smooth rate parameter in standard LS with a negative value and add a CE warm-up. No architectural changes, no extra models. Negligible engineering cost.

**Problems solved:**  
In proxy-label learning: attribution scores generate noisier labels for borderline examples. High-noise training regimes (e.g., when attribution models have low fidelity) benefit from NLS. The phase-transition insight provides a practical decision rule: estimate the noise rate, and if high, switch to NLS.

**Engineering cost:**  
Minimal. One hyperparameter (negative smooth rate r). Noise rate can be estimated with standard methods (Patrini 2017, Yao 2020).

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
First to formally define and analyze Negative Label Smoothing. Prior work (Lukasik 2020) showed LS helps with noisy labels but did not explore negative rates. The theoretical unification of loss correction, Peer Loss, and NLNL under the NLS framework is a novel insight. The phase transition characterization between LS and NLS optimality is new.

**Prior work comparison:**  
Szegedy et al. 2016 (LS), Lukasik et al. 2020 (LS for noisy labels), Patrini et al. 2017 (loss correction = special NLS), Liu & Guo 2020 (Peer Loss = special NLS), Kim et al. 2019 (NLNL = NLS as r→-∞). The paper unifies all these under a single GLS framework.

**Verification:**  
UCSC + Brown + Sydney AI Centre + RIKEN AIP + UTokyo, ICML 2022. Published as PMLR v162 wei22b. The phase transition insight is now widely cited in subsequent work.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| CIFAR-10/100 (synthetic noise) | public | Yes | Multiple noise rates |
| CIFAR-10N / CIFAR-100N | public | Yes | Human annotator noise |
| Clothing-1M | public | Yes | 1M web images |
| AGNews | public | Yes | NLP text classification |
| UCI datasets (Twonorm, Waveform, etc.) | public | Yes | Tabular classification |

**Offline experiment reproducibility:**  
High. Code released; warm-up schedule and smooth rate grid search procedure documented.

---

## 6. Community Reaction

UCSC + Sydney AI Centre + RIKEN, ICML 2022. Well-received as a simple yet theoretically grounded contribution. The unification of existing robust losses under NLS is cited in subsequent papers. The insight that practitioners have been accidentally using NLS-like methods (loss correction, Peer Loss) without realizing it is considered the paper's most impactful finding.

**Relevance to proxy-label learning:** Core. The NLS warm-up strategy is directly applicable when proxy labels have varying quality levels. The theoretical phase transition provides guidance for choosing between LS and NLS based on estimated proxy label noise rate.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |
| [2023_ICML_LogitClip_Mitigating-Memorization-Noisy-Labels-Clipping.md](./2023_ICML_LogitClip_Mitigating-Memorization-Noisy-Labels-Clipping.md) | Novelty vs. Prior Work | 2018 (GCE): partially robust. Menon et al. 2020 (PHuber-CE, gradient clipping): shown not sufficient for noise robustness. LogitNorm (Wei et al. 2022a): focuses on OOD detection, not noisy labels; always normalizes to unit norm (equivalent to fixed τ=1). LogitClip differs by having an adaptive th... |

---
## Meta Information

**Authors:** Jiaheng Wei, Hangyu Liu, Tongliang Liu, Gang Niu, Masashi Sugiyama, Yang Liu  
**Affiliations:** University of California Santa Cruz; Brown University; University of Sydney; RIKEN AIP; University of Tokyo  
**Venue:** ICML 2022  
**Year:** 2022  
**PDF:** available at proceedings.mlr.press/v162/wei22b/wei22b.pdf  
**Relevance:** Core  
**Priority:** 1  
**NLM Source ID:** 719e007c-e578-4f3c-a686-c6cdc851f2f5
