# Paper Analysis: Understanding Self-Distillation in the Presence of Label Noise

**Source:** https://arxiv.org/pdf/2301.13304  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** Understanding Self-Distillation in the Presence of Label Noise  
**Authors:** Rudrajit Das, Sujay Sanghavi  
**Abstract:** Provides a theoretical analysis of self-distillation (SD) under label noise for both squared loss and cross-entropy loss. SD trains a student using: ξ·ℓ(teacher's predictions, student's predictions) + (1-ξ)·ℓ(given labels, student's predictions). Key finding: in high noise regimes, the optimal ξ is surprisingly greater than 1 (anti-learning the noisy labels). Also proves conditions under which optimal SD beats optimal ℓ₂ regularization.

**Key contributions:**
- Bias-variance tradeoff: increasing ξ reduces variance but increases bias in estimating ground truth parameters — optimal ξ>1 at high noise rates
- ξ>1 anti-learning: setting ξ>1 makes the coefficient on observed labels (1-ξ) negative, actively discounting noisy labels
- Empirical validation: on Caltech-256, StanfordCars, Flowers-102, CIFAR-100, Food-101 with linear probing on ResNet-34/VGG-16; ξ=1.5 achieves +10.04% on Caltech-256 (50% random noise)
- Binary cross-entropy: quantifies range of label corruption where student outperforms teacher — first result of this kind for CE
- SD vs. regularization: Theorem 2 gives conditions when optimal SD beats optimal ℓ₂ regularization

**Methodology:**  
Linear probing setup: frozen ImageNet-pretrained ResNet-34/VGG-16 feature extractor; only softmax layer trained. Three corruption types: random, hierarchical (CIFAR-100 super-classes), adversarial (hard classes from teacher). ξ grid from 0.2 to 6.0. No data augmentation.

**Main results:**  
Caltech-256 50% random (ResNet-34): ξ=1.5 → +10.04% over teacher (67.65% vs 57.61%). StanfordCars 30% random: ξ=1.2 → +3.53%. CIFAR-100 50% random: ξ=3.5 → +5.86%. Food-101 0% noise: ξ=1 → -0.37% (SD hurts on clean data). Utility monotonically increases with noise level across all corruption types.

---

## 2. Experiment Critique

**Design:**  
Linear probing setup is a deliberate simplification for theoretical tractability — trades real-world applicability for clean theoretical validation. Three corruption types (random, hierarchical, adversarial) provide diverse noise structures. Wide ξ grid (0.2 to 6.0) confirms optimal ξ>1 consistently at high noise.

**Statistical validity:**  
Multiple runs, mean ± std reported. Controlled setup (same backbone, only softmax layer varies). Results across 5 datasets with 3 corruption types provide good coverage.

**Online experiments (if any):**  
None.

**Reproducibility:**  
Experimental setup fully specified (architectures, datasets, corruption procedures). No code repository mentioned explicitly.

**Overall:**  
Strong theoretical contribution. The practical recommendation (use ξ>1 at high noise) is actionable. Key limitations: (1) theoretical proofs strictly for linear regression + logistic regression, not deep networks in general; (2) linear probing setup may not transfer to full fine-tuning; (3) no validation on standard noisy label benchmarks (CIFAR-N, Clothing1M, WebVision).

---

## 3. Industry Contribution

**Deployability:**  
Moderate. The practical insight is clear: when noise is high (>30%), train students with ξ>1 in the distillation objective. This is a trivial code change. The limitation is that ξ requires tuning and the optimal value varies (1.5 for Caltech-256, 3.5 for CIFAR-100).

**Problems solved:**  
In proxy-label learning: knowledge distillation from a teacher trained on proxy labels to a student is a common technique. This paper provides the first theoretical justification for why ξ>1 may be optimal when proxy labels are noisy — the student should actively discount the teacher's training labels while trusting the teacher's soft predictions.

**Engineering cost:**  
Negligible. Single scalar hyperparameter ξ in the KD loss. Grid search over ~10 values.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
First theoretical characterization of SD's bias-variance tradeoff under label noise for cross-entropy loss. First result showing optimal ξ>1. First proof of when optimal SD beats optimal ℓ₂ regularization. Prior theoretical work (Mobahi et al. 2020, Dong et al. 2019) restricted to squared loss and ξ∈[0,1].

**Prior work comparison:**  
Mobahi et al. 2020 (SD amplifies regularization): squared loss, Hilbert space, ξ=1 only — no noisy labels analysis, no ξ>1 result. Dong et al. 2019 (SD mimics early stopping): dynamically updated soft labels, noisy labels empirically — no formal quantification of when student beats teacher. Li et al. 2017 (SD ameliorates noisy labels): empirical only. This paper: formal bounds for both losses.

**Verification:**  
UT Austin, ICML 2023.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Caltech-256 | public | Yes | 256 classes, random splits |
| StanfordCars | public | Yes | 196 classes |
| Flowers-102 | public | Yes | 102 classes |
| CIFAR-100 | public | Yes | Hierarchical + random corruption |
| Food-101 | public | Yes | Random + adversarial corruption |

**Offline experiment reproducibility:**  
High for the experimental setup described. No code repository cited, but setup is simple (linear probing, standard datasets).

---

## 6. Community Reaction

UT Austin, ICML 2023. Appreciated as a foundational theoretical contribution to the KD/SD literature. The practical insight (ξ>1 for high noise) attracted practitioners' attention. Noted limitation: restricted to linear probing — community questions whether results transfer to full fine-tuning.

**Relevance to proxy-label learning:** Related. When using knowledge distillation with proxy labels, the finding that ξ>1 is optimal under high noise is directly applicable. Provides theoretical grounding for "anti-learning" the original labels.

---

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Meta Information

**Authors:** Rudrajit Das, Sujay Sanghavi  
**Affiliations:** The University of Texas at Austin  
**Venue:** ICML 2023  
**Year:** 2023  
**PDF:** available at arxiv.org/pdf/2301.13304  
**Relevance:** Related  
**Priority:** 1  
**NLM Source ID:** bfa8528d-9158-4a98-bce8-c26272fa7196
