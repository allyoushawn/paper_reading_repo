Date: 2026-04-12  
Source: Local PDF `/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/03_Ranking/Distill/2024 (Google) Self-Auxiliary Distillation for Sample Efficient Learning in Google-Scale Recommenders.pdf` (awesome-repo mirror; **not** `https://arxiv.org/pdf/2408.01386`, which is an unrelated arXiv id). DOI: `https://doi.org/10.1145/3640457.3688041`.  
NLM Source ID: `1d077bac-dc32-4853-85b2-11b66d8a2c2b`  
NotebookLM notebook: `proxy-label-learning` (`6fbcf9e6-3833-4660-8b56-67b0b98bf394`)  
Venue: RecSys 2024 (3-page short paper)  
Relevance: Core  
Priority: 1

# Paper Analysis: Self-Auxiliary Distillation for Sample Efficient Learning in Google-Scale Recommenders

**Source:** Local PDF (path above)  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Self-Auxiliary Distillation for Sample Efficient Learning in Google-Scale Recommenders  

**Authors:** Yin Zhang, Ruoxi Wang, Xiang Li, Tiansheng Yao, Andrew Evdokimov, Jonathan Valverde, Yuan Gao, Jerry Zhang, Evan Ettinger, Ed H. Chi, Derek Zhiyuan Cheng (Google / Google DeepMind)  

**Abstract:**  
Industrial recommenders train on billions of noisy, uneven-quality user feedback signals (clicks, installs, conversions). The paper proposes **Self-auxiliary Distillation (SEAD)**: a **main head** trains on ground-truth labels (preserving **calibration** for serving) while an **auxiliary head** (dropped at serve time) mixes **hard labels** and **teacher soft labels** via a **bilateral-branch** design and selector \(P(O,\vec{O})\)—emphasizing **positives on originals** and **distilling negatives** from the main head’s logits. A variant with **teacher/student towers** targets **iOS ATT signal loss** (biased sparse positives, false negatives), using unbiased traffic in the teacher main head and SKAdNetwork for calibration.

**Key contributions:**
- SEAD: pseudo-label auxiliary task + bilateral branch (distillation vs scratch) + shared bottom; **no extra serving cost**.
- Production evidence on **three Google surfaces** (apps, commerce, video) plus **signal-loss** scenario with large offline/online lifts.
- Ablations (OGL, DTL, SGA, LR, selector variants) isolating what drives gains.

**Methodology:**  
Shared tower; main = teacher logits; auxiliary = selector-combined targets; optional curriculum / adaptors in selector; iOS variant: separate towers + SKAdNetwork.

**Main results:**  
Table 1 (offline AUC deltas vs baselines): pCTR Model1 **+0.35%**; pCTR Model2 **+0.20%**; pCVR **+0.26%** (authors treat **+0.1%** as meaningful at Google traffic). Signal-loss table: **+17%** event AUC, **+3%** SKAdNetwork AUC, **+2%** simulation AUC, positive online outcome. Online A/B: significant business metrics across three product areas.

---

## 2. Experiment Critique

**Design:**  
Short paper; metrics are internal production streams. Ablations compare OGL (auxiliary on hard labels only), DTL (soft only), doubled LR, stop-gradient on shared trunk, and selector inversion.

**Statistical validity:**  
Large-sample AUC shifts; significance framed against **+0.1%** operational threshold. Detailed variance not specified in source.

**Online experiments (if any):**  
Yes — online A/B tests reported as supporting deployment claims.

**Reproducibility:**  
No public code or datasets; 3-page format limits architectural and hyperparameter disclosure.

**Overall:**  
Strong industry-facing evidence; academic reproducibility is intentionally limited.

---

## 3. Industry Contribution

**Deployability:**  
Auxiliary head removed at inference; shared-bottom training keeps overhead small relative to full two-tower serving.

**Problems solved:**  
**Label quality heterogeneity** (weak negatives in CTR), **calibration** constraints, and **ATT-induced label bias** / conversion signal loss.

**Engineering cost:**  
Extra head + selector logic + tuning; still framed as negligible vs full alternative stacks.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
Self-distillation structured so **serving calibration** is preserved while an auxiliary head mines richer pseudo-labels; bilateral branch + selector; ATT-focused variant.

**Prior work comparison:**  
Cites **bilateral-branch networks (Zhou et al., 2020)**, **curriculum learning (Bengio et al., 2009)**, **self-distillation / soft-label smoothing (Zhang & Sabuncu, 2020; Zhou et al., 2021)**, **CDN adaptors (Zhang et al., 2023)**, and privacy / ATT literature.

**Verification:**  
Positioning is consistent with concurrent KD and pseudo-label literature; empirical claims rest on internal evaluation.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Google production logs (Apps / Commerce / Video) | N/A | No | Streaming training |
| iOS ATT / SKAdNetwork scenario | N/A | No | Signal-loss evaluation |

**Offline experiment reproducibility:**  
Not reproducible outside Google.

---

## 6. Community Reaction

No dedicated community scan for this batch.

---

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Meta Information

**Authors:** Yin Zhang, Ruoxi Wang, Xiang Li, Tiansheng Yao, Andrew Evdokimov, Jonathan Valverde, Yuan Gao, Jerry Zhang, Evan Ettinger, Ed H. Chi, Derek Zhiyuan Cheng  
**Affiliations:** Google; Google DeepMind (as in PDF)  
**Venue:** RecSys 2024  
**Year:** 2024  
**PDF:** downloaded (local awesome-repo PDF)  
**Relevance:** Core  
**Priority:** 1

---

## NotebookLM Q1/Q2 digest (source-scoped)

**Q1 — Problem / method / data:** Problem: unequal informativeness of feedback labels; calibration; iOS ATT false negatives. Method: SEAD with shared bottom, main head on hard labels + teacher soft outputs, auxiliary bilateral branch (distillation + scratch), selector \(P(O,\vec{O})\), curriculum/adaptor options; ATT variant with teacher/student towers and SKAdNetwork calibration. Data/baselines: three production models (two pCTR, one pCVR) with streaming training; ablations OGL, DTL, SGA, LR, inverted selector.

**Q2 — Quantitative / limits / priors:** Quant: **+0.35% / +0.20% / +0.26%** offline AUC; signal-loss **+17% / +3% / +2%** table; online A/B positive across three products. Limits: OGL unstable (blow-ups), DTL neutral, positive-only auxiliary inferior, 2×LR unstable, SGA neutral (shared updates matter). Priors: **Zhou et al. BBN (2020)**; **Zhang & Sabuncu (2020)**; **Zhou et al. (2021)** soft labels; **Bengio et al. curriculum (2009)**; **Zhang et al. CDN adaptors (2023)**; ATT / privacy refs (Johnson et al., Kollnig et al., Thomas, etc., as listed in PDF).
