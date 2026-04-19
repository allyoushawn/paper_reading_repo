Date: 2026-04-12  
Source: https://proceedings.neurips.cc/paper/5073-learning-with-noisy-labels.pdf  
NLM Source ID: `46d54136-9971-47f0-978d-41d30a1dc0d5`  
NotebookLM notebook: `proxy-label-learning` (`6fbcf9e6-3833-4660-8b56-67b0b98bf394`)  
Venue: NeurIPS 2013  
Relevance: Core  
Priority: 2 (seminal)

# Paper Analysis: Learning with Noisy Labels

**Source:** https://proceedings.neurips.cc/paper/5073-learning-with-noisy-labels.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Learning with Noisy Labels  

**Authors:** Nagarajan Natarajan, Inderjit S. Dhillon, Pradeep Ravikumar, Ambuj Tewari  

**Abstract:**  
Binary classification under **class-conditional** random label noise (CCN): labels are flipped with class-dependent probabilities \(\rho_{+1}, \rho_{-1}\). The paper gives **two general modifications** of surrogate losses: (1) **unbiased estimators** \(\tilde{\ell}\) so that minimizing empirical risk on noisy labels tracks the clean risk; with a **symmetry** condition on \(\ell\), \(\tilde{\ell}\) stays convex (squared, logistic, Huber); hinge yields non-convex \(\tilde{\ell}\) but a **biconjugate**-based approximate convex minimization is analyzed. (2) **Label-dependent costs** / \(\alpha\)-weighted margin losses so that minimizing noisy risk ties to clean 0–1 risk; explains **biased SVM / weighted logistic** as noise-tolerant in theory.

**Key contributions:**
- First finite-sample risk bounds for **convex surrogates under CCN** without distributional separability assumptions (per paper framing).
- Practical algorithms: \(\tilde{\ell}_{\log}\) and **C-SVM** with asymmetric costs; strong empirical noise robustness.

**Methodology:**  
Lemma-based construction of \(\tilde{\ell}\); Theorems on Rademacher-style bounds; reduction to weighted classification for the second approach.

**Main results:**  
Synthetic separable: **>90%** accuracy at \(\rho_{+1}=\rho_{-1}=0.4\) with \(\tilde{\ell}_{\log}\); linearly separable demo **98.5%** at 0.4 flip rate. Banana dataset: C-SVM **90.6%** (20% noise), **88.5%** (40% noise) vs weaker RP baselines. UCI (Breast, Diabetes, Thyroid, German, Heart, Image): competitive with **RP, NHERD, PAM** across noise settings; \(\tilde{\ell}_{\log}\) often best overall.

---

## 2. Experiment Critique

**Design:**  
3 train/test splits; CV for hyperparameters; kernel width fixed from clean-tuned SVM for fair kernel comparisons.

**Statistical validity:**  
Averaging over splits and noise corruptions; tabular benchmarks modest in size.

**Online experiments (if any):**  
Not specified in source.

**Reproducibility:**  
Standard UCI preprocessing (Rätsch repository referenced in source).

**Overall:**  
Theory–practice alignment for CCN; limitations on harder noise models acknowledged.

---

## 3. Industry Contribution

**Deployability:**  
Lightweight loss / SVM-cost tweaks when flip rates are roughly stable or tunable as hyperparameters.

**Problems solved:**  
Cheap weak supervision / crowdsourcing with asymmetric confusion between classes.

**Engineering cost:**  
Low for logistic/SVM pipelines; noise-rate tuning via CV if unknown.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
General convex-surrogate theory for CCN; unification explaining practical biased SVMs.

**Prior work comparison:**  
Contrasts RCN/PAC (Angluin & Laird; Ben-David et al.) limited to 0–1 or restrictive convex cases; cites **Scott (2012)** \(\alpha\)-weighted Bayes optimality; **Stempfel & Ralaivola** RP and hinge proxies; **Liu et al. (2003)** biased SVM for PU; **Crammer & Lee** NHERD; **Khardon & Wachman** PAM survey.

**Verification:**  
Theoretical claims are standard NeurIPS-level; empirical gains strongest on synthetic + small UCI.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Synthetic 2D | N/A | Easy to reproduce | Separable / banana |
| UCI (6 sets) | Public | Yes | Via Rätsch preprocessing |

**Offline experiment reproducibility:**  
Fully reproducible on public data.

---

## 6. Community Reaction

No dedicated community scan for this batch.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |
| [2017_CVPR_NA_Loss-Correction-Label-Noise.md](./2017_CVPR_NA_Loss-Correction-Label-Noise.md) | Novelty vs. Prior Work | correction for modern deep nets. Prior work comparison: Builds on Natarajan et al. (2013) backward correction theory; Sukhbaatar et al. (2015) architecture augmentation inspiring forward view; Menon et al. (2015); Liu & Tao (2016) estimators; He et al. (2016) ResNet; Xiao et al. (2015) Clothing1M... |
| [2021_arXiv_NA_Instance-dependent-Label-noise-Learning-under.md](./2021_arXiv_NA_Instance-dependent-Label-noise-Learning-under.md) | Main note body | *Learning with noisy labels*:** Cited as a foundational work attempting to make the transition matrix identifiable by relying on the restrictive "instance-independent" assumption [15, 23, 26]. * **Patrini et al. (2017) - *Making deep neural networks robust to label noise: A loss correction approa... |
| [2021_arXiv_UnderstandingInstanceLev_Understanding-Instance-Level-Label-Noise-Disparate.md](./2021_arXiv_UnderstandingInstanceLev_Understanding-Instance-Level-Label-Noise-Disparate.md) | Main note body | 21-24]. 2. Natarajan et al. (2013): Cited extensively as the classic foundational work introducing the loss correction approach and the standard requirement of explicit noise transition matrices [4, 25-28]. 3. Liu & Guo (2020): Cited heavily for introducing "peer loss." The author mathematically ... |
| [2021_ICML_NA_Understanding-Instance-Level-Label-Noise-Disparate-Impacts.md](./2021_ICML_NA_Understanding-Instance-Level-Label-Noise-Disparate-Impacts.md) | NotebookLM Q2 / priors | **Natarajan et al. (2013); Patrini et al. (2017)** — loss correction baselines engaged in instance-level theory vs memorization. |

---
## Meta Information

**Authors:** Nagarajan Natarajan, Inderjit S. Dhillon, Pradeep Ravikumar, Ambuj Tewari  
**Affiliations:** UT Austin; University of Michigan  
**Venue:** NeurIPS 2013  
**Year:** 2013  
**PDF:** downloaded (NeurIPS proceedings)  
**Relevance:** Core  
**Priority:** 2

---

## NotebookLM Q1/Q2 digest (source-scoped)

**Q1 — Problem / method / data:** CCN label noise; two approaches: **unbiased surrogate** \(\tilde{\ell}\) (Lemma 1) with convexity when loss obeys symmetry (logistic, squared, Huber; hinge → biconjugate minimization); **\(\alpha\)-weighted** margin / cost-sensitive reduction tying noisy risk to clean 0-1 risk. Data: 2D linear synthetic, **banana**, six **UCI** sets. Baselines: **RP**, **NHERD** (project/exact), **PAM**.

**Q2 — Quantitative / limits / priors:** Linear synthetic **98.5%** @ \(\rho=0.4\); banana **90.6%** @ 0.2 noise, **88.5%** @ 0.4 (C-SVM) vs RP \(\sim\)84% @ 0.3. UCI: \(\tilde{\ell}_{\log}\) competitive all six; C-SVM best four of six. Limits: \(\tilde{\ell}\) non-convexity for hinge; C-SVM weaker on **Diabetes**/**Heart**; CCN-only theory; known rates in proofs, CV in practice. Priors: **Scott 2012/2013**, **Stempfel & Ralaivola 2007/2009**, **Liu et al. 2003**, **Crammer & Lee 2010** / PA family, **Angluin & Laird 1988**, **Khardon & Wachman 2007**, **Cesa-Bianchi et al. 2011**.
