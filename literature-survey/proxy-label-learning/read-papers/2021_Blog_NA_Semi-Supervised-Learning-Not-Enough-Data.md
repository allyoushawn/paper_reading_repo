Date: 2026-04-12  
Source: https://lilianweng.github.io/posts/2021-12-05-semi-supervised/  
NLM Source ID: `4831ebc3-a784-4e96-87e9-f2745de32728`  
NotebookLM notebook: `proxy-label-learning` (`6fbcf9e6-3833-4660-8b56-67b0b98bf394`)  
Venue: Blog (Lilian Weng, 2021)  
Relevance: Related  
Priority: 2

# Paper Analysis: Learning with Not Enough Data Part 1: Semi-Supervised Learning

**Source:** https://lilianweng.github.io/posts/2021-12-05-semi-supervised/  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Learning with Not Enough Data Part 1: Semi-Supervised Learning

**Authors:** Lilian Weng (Lil’Log)

**Abstract:**  
A broad tutorial on SSL framed as optimizing \(L = L_s + \mu(t) L_u\), focusing on how different methods construct the **unsupervised loss** \(L_u\): consistency regularization (Π-model, temporal ensembling, Mean Teacher, VAT, UDA), pseudo-labeling / self-training (Noisy Student, Meta Pseudo Labels), and hybrids (MixMatch family, FixMatch, DivideMix sketch). It also connects SSL to pre-training + self-training tradeoffs.

**Key contributions:**
- Unified loss framing and intuitive diagrams/notes for major SSL families through ~2021.
- Practical themes: augmentation quality, confidence thresholds, confirmation bias mitigation, and pre-training interactions.

**Methodology:**  
Expository synthesis with equations and citations to primary papers (not a novel algorithm submission).

**Main results:**  
Aggregated benchmark pointers (not a single new table): e.g., **CIFAR-10** comparisons including fully supervised **WRN-28-2** error **5.4** vs **PyramidNet+ShakeDrop** **2.7** on 50k labels (no RandAugment) as reference bars for reading SSL plots; qualitative claims about **SVHN** Mean Teacher behavior, etc.

---

## 2. Experiment Critique

**Design:**  
Survey-level: mixes multiple papers’ claims; not a unified experimental protocol.

**Statistical validity:**  
Not specified in source.

**Online experiments (if any):**  
Not specified in source.

**Reproducibility:**  
Reproducibility is defined by each cited method’s original paper/code; the blog itself is not an experiment artifact.

**Overall:**  
Excellent onboarding for SSL mechanics; quantitative statements should be traced to the **original** papers (Xie et al. UDA/Noisy Student; Sohn et al. FixMatch; etc.).

---

## 3. Industry Contribution

**Deployability:**  
Emphasizes engineering realities: augmentation pipelines, teacher–student stabilization, and that **self-training can be expensive** vs fine-tuning a pretrained model.

**Problems solved:**  
Label scarcity; provides mental model for choosing among consistency, pseudo-label, and hybrid approaches.

**Engineering cost:**  
High for large-scale self-training (Noisy Student narrative); depends heavily on augmentation quality (UDA).

---

## 4. Novelty vs Prior Work

**Paper's claimed novelty:**  
Educational synthesis (not claiming new SOTA).

**Prior work comparison:**  
Summarizes Laine & Aila (Π / temporal), Tarvainen & Valpola (Mean Teacher), Miyato et al. (VAT), Xie et al. (UDA / Noisy Student), Pham et al. (Meta Pseudo Labels), Berthelot et al. (MixMatch / ReMixMatch), Sohn et al. (FixMatch), Li et al. (DivideMix sketch), Zoph et al., Chen et al. (SimCLRv2 + distillation), etc.

**Verification:**  
Not independently verified beyond NotebookLM extraction.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| SVHN | Public | Yes | Mean Teacher example |
| CIFAR-10 | Public | Yes | UDA plot / SSL comparisons |
| ImageNet / COCO | Public | Yes | Pre-training vs self-training discussion |
| Text tasks | Varies | Often public | UDA + BERT fine-tuning narrative |

**Offline experiment reproducibility:**  
Follow each cited method’s canonical implementation.

---

## 6. Community Reaction

No dedicated X/Reddit/HN scan was run for this notebook-driven batch.

---

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Meta Information

**Authors:** Lilian Weng  
**Affiliations:** Not specified in source  
**Venue:** Personal blog (Lil’Log)  
**Year:** 2021  
**PDF:** web page ingested via NotebookLM (`source_type=url`, `wait=True`)  
**Relevance:** Related  
**Priority:** 2

---

## NotebookLM Extraction Notes (Phase 3 Batch 3)

**Q1:** Summarizes SSL families and cites standard vision/text benchmarks; not a single “paper method” in the strict sense.

**Q2:** Includes aggregated quantitative pointers (CIFAR-10 supervised baselines; Zoph et al. pre-training vs self-training findings), limitations (confirmation bias; scaling of label propagation; Temporal Ensembling epoch cadence; FixMatch augmentation ablations; critique of strong distribution-alignment assumptions), and a dense list of foundational citations (Laine & Aila; Tarvainen & Valpola; Lee; Xie et al.; Berthelot et al.; Sohn et al.; Zoph & Chen studies).
