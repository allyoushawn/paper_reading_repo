Date: 2026-04-11
Source: https://arxiv.org/pdf/2409.19696
NLM Source ID: aa20075a-9c12-4333-a10d-dcb54c2fc610
Venue: NeurIPS 2024
Relevance: Core
Priority: 1

# Vision-Language Models are Strong Noisy Label Detectors

**Authors:** Tong Wei et al.
**Affiliation:** (Multiple institutions)
**Code:** https://github.com/HotanLee/DeFT

## Problem

Fine-tuning vision-language models (e.g., CLIP) on noisy downstream datasets is challenging. Standard small-loss filtering (GMM, Co-teaching) fails on instance-dependent noise and "hard" clean samples with large loss. Full fine-tuning (FFT) on noisy data distorts CLIP's pre-trained visual-text alignment. The question: can the rich cross-modal alignment in VLMs be leveraged to identify noisy labels before fine-tuning degrades the representations?

## Method: DeFT (Denoising Fine-Tuning)

**Key finding:** VLMs maintain robust visual-text alignment even under high noise, but only when using parameter-efficient fine-tuning (PEFT like VPT). Full fine-tuning (FFT) progressively distorts representations as noise increases. This motivates a 2-phase architecture.

### Phase 1: Noisy Label Detection (PEFT-based)
1. **Dual textual prompts per class:** Positive prompt prompt+_k and negative prompt prompt-_k
   - positive prompt: optimized to maximize similarity between image features and class text features for correctly labeled images
   - negative prompt: learned as a sample-dependent threshold ϕ_i = sim(I_i, T-_k)
2. **Clean sample selection (no fixed threshold needed):**
   ```
   D_clean = {(x_i, y_i) | sim(I_i, T+_k) > ϕ_i and y_i = k}
   ```
3. **Loss:** Negative learning objective for prompts (Ldp) + similarity loss on clean subset (Lsim = contrastive CE on clean D_clean)
4. **PEFT:** Visual prompt tuning (VPT) — only a small set of parameters updated. Preserves pre-trained alignment integrity.

### Phase 2: Model Adaptation (FFT on clean data)
- Drops PEFT modules
- Trains linear classifier + full fine-tuning using only D_clean
- Minimal epochs (10) — efficient

**Advantage over loss-based filtering:** (1) No prior knowledge of noise ratio required; (2) text modality adds orthogonal signal to loss; (3) identifies "hard noise" (instance-dependent) that small-loss criterion misses.

## Key Results

| Dataset | DeFT | Best Baseline | Delta |
|---------|------|--------------|-------|
| CIFAR-100N (real) | **79.04%** | UNICON 77.68% | +1.36pp |
| Clothing1M (real) | **72.44%** | ELR 72.14% | +0.30pp |
| WebVision (real) | **85.12%** | LongReMix 84.96% | +0.16pp |
| Stanford-Cars (IDN) | avg +4.34pp over best prior | — | — |

Also outperforms on multiple architectures on Clothing1M: ResNet-50 (70.82 vs CE 66.02), MAE-ViT-B (65.23 vs 61.31), ConvNeXt-T (71.68 vs 68.80).

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Relevance to Proxy Label Learning

**Rating: Moderate (detection method).** 

1. **Instance-dependent noise detection:** Proxy labels from attribution models exhibit instance-dependent errors — DeFT's key advantage is exactly this. The dual-prompt detection mechanism doesn't assume i.i.d. noise, making it applicable to structured proxy label errors.
2. **Applicable when pre-trained VLMs are available:** If the supervised model uses a pre-trained visual backbone, DeFT provides a principled way to identify which training samples have corrupted proxy labels before training.
3. **Limitation for non-image domains:** DeFT is entirely vision-specific (dual prompts require textual class descriptions). For tabular/interaction-level proxy labels in recommendation systems, the framework doesn't directly transfer — only the detection philosophy (use external robust pre-trained model as semantic oracle) is transferable.
4. **Separation of concerns:** The DeFT philosophy — first filter noise using a robust detector, then train on clean — is broadly applicable and more principled than training-time noise robustness methods.

## Method Tracker Update

- **DeFT**: Wei et al., NeurIPS 2024 | Baseline mentions: 0 (new) | Derived variants: 0 | Component count: 3 | Simplicity: 3 | Performance consistency: 4 | Composite: ~14
