# Paper Analysis: Learning to Reweight Examples for Robust Deep Learning

**Source:** https://arxiv.org/pdf/1803.09050  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Learning to Reweight Examples for Robust Deep Learning  
**Authors:** Mengye Ren, Wenyuan Zeng, Bin Yang, Raquel Urtasun  
**Abstract:** Many training pipelines use hand-designed example weighting or mining rules that implicitly conflict across regimes (e.g., small-loss preference for noisy labels vs large-loss preference for hard examples under imbalance). The paper proposes learning per-example weights by a short meta-gradient step that aligns mini-batch training gradients with gradients on a small clean validation set, then rectifies and normalizes weights for stable optimization.

**Key contributions:**
- A clean meta-learning formulation: choose weights to minimize validation loss after a one-step proxy update, approximated online per iteration.
- A derivation showing the meta-gradient relates to inner products between training and validation gradient directions (layerwise decomposition for CNN/MLP cases).
- Strong empirical results on synthetic imbalance (MNIST 4 vs 9) and CIFAR-10/100 with uniform and background flip noise, using small clean validation sets.

**Methodology:**  
Automatic differentiation through an unrolled training batch (“backward-on-backward”) to obtain \(\nabla_\varepsilon \ell_{\text{val}}\) wrt. per-example perturbations \(\varepsilon_i\), map to nonnegative weights, batch-normalize, then train with weighted loss.

**Main results:**  
NLM-cited highlights: under 40% uniform flip on CIFAR-10 (WideResNet-28-10), method reaches ~86.92% test accuracy with 1000 clean images vs MentorNet ~76.6% in excerpted table; under extreme imbalance ratios, error increases ~2% vs catastrophic baselines; under increasing noise up to 50%, reported degradation is far smaller than baseline collapse in excerpted figure descriptions.

---

## 2. Experiment Critique

**Design:**  
Carefully separates regimes (imbalance vs noise) and includes ablations on validation size. Comparisons include MentorNet, S-model, bootstrapping variants, and oracle reweighting in background-flip settings.

**Statistical validity:**  
Multiple runs reported for several settings (means ± std in tables).

**Online experiments (if any):**  
Not specified in source.

**Reproducibility:**  
Public code link appears in paper text (`uber-research/learning-to-reweight-examples` per NLM excerpt).

**Overall:**  
Influential baseline for “small clean meta-set guides training under corruption”; compute overhead is the main practical drawback.

---

## 3. Industry Contribution

**Deployability:**  
Useful when a small trusted holdout exists (QA-reviewed subset, gold labels, or a carefully curated validation shard). Less attractive when no trusted validation exists or when second-order passes are too expensive at LLM scale.

**Problems solved:**  
Robust learning under biased sampling and label noise—common when using weak supervision or proxy-labeled corpora with a small clean anchor set.

**Engineering cost:**  
Roughly ~3× training-time overhead vs standard backprop (per paper discussion summarized by NLM).

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
Replaces heuristic loss-based mining with a principled meta-objective tied to validation alignment; avoids extra hyperparameter grids typical of many reweighting schedules.

**Prior work comparison:**  
Contrasts with MentorNet (sequence model on losses), bootstrapping noise layers, and classical hard negative mining / self-paced ideas.

**Verification:**  
ICML 2018 (PMLR proceedings); arXiv:1803.09050.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| MNIST | public | Yes | class imbalance synthetic setup |
| CIFAR-10 / CIFAR-100 | public | Yes | synthetic uniform/background noise |

**Offline experiment reproducibility:**  
High (classic vision benchmarks + released code reference).

---

## 6. Community Reaction

No significant community discussion found in this NotebookLM-derived pass.

**Relevance to proxy label learning:** Core. The clean validation set acts as a trusted target distribution for correcting proxy-labeled training data effects.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |
| [2025_arXiv_FBR_Revisiting-Meta-Learning-Noisy-Labels-Reweighting-Dynamics.md](./2025_arXiv_FBR_Revisiting-Meta-Learning-Noisy-Labels-Reweighting-Dynamics.md) | Novelty vs. Prior Work | noise; FBR as a theory-guided drop-in replacement for expensive bilevel schemes. Prior work comparison: Positions explicitly against Ren et al. (2018) and Shu et al. (Meta-Weight-Net) as the canonical meta reweighting line; uses Zhai et al. to motivate limitations of “generic reweighting ≈ ERM” a... |

---

## Meta Information

**Authors:** Mengye Ren, Wenyuan Zeng, Bin Yang, Raquel Urtasun  
**Affiliations:** Uber ATG; University of Toronto (per PDF header in source)  
**Venue:** ICML 2018  
**Year:** 2018  
**PDF:** available at https://arxiv.org/pdf/1803.09050  
**Relevance:** Core  
**Priority:** 1  
**NLM Source ID:** 7a10d83f-062f-4eea-bafc-cf83813f9140

---

*[If datasets are accessible: To run experiments on these datasets, use the experiment-runner skill with the dataset URL or info above.]*
