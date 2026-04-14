# Paper Analysis: Deep Neural Net with Attention for Multi-channel Multi-touch Attribution

**Source:** https://arxiv.org/pdf/1809.02230.pdf  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** Deep Neural Net with Attention for Multi-channel Multi-touch Attribution  
**Authors:** Rohan Arava, Jing Lu, Benjamin Lipshitz, Ren Xu, Haichuan Yang, Licheng Wu, Yuan Qi (Adobe)  
**Abstract:**
This paper proposes DNAMTA (Deep Neural net Attention for Multi-Touch Attribution), an end-to-end deep learning model for multi-touch attribution. The key innovation is a hierarchical attention mechanism combining touchpoint-level attention (which channels matter) and time-decay attention (recency weighting) integrated with user-level control variables via a fusion network. Attribution credits are derived from the learned attention weights, providing channel-level attribution while accounting for the temporal structure of the conversion journey.

**Key contributions:**
- DNAMTA: two-stage attention architecture (touchpoint attention + time-decay attention) fused with user control variables
- Touchpoint attention: learns channel importance weights across the conversion journey
- Time-decay attention: corrects for recency bias in last-touch attribution by learning time-dependent weights
- Fusion network: combines sequential channel representation with user-level demographics and behavioral features
- Demonstrates display ad overvaluation under last-click (0.642→0.411 after time-decay correction)

**Methodology:**
Input: ad exposure sequence encoded via LSTM embedding → LSTM sequence encoder → touchpoint attention (soft attention over LSTM hidden states) → time-decay attention (learned exponential decay applied to touchpoint weights) → feature fusion (concatenate with user control variables) → FC classification head predicting conversion. Attribution = product of touchpoint attention and time-decay attention weights, normalized per channel type. Trained end-to-end on binary conversion objective.

**Main results:**
On Adobe internal 426k record dataset (6 average touchpoints): Fusion DNAMTA accuracy 0.819 / AUC 0.879 vs LR 0.789/0.846, LSTM 0.807/0.841, touchpoint-attention-only 0.811/0.869. Feature dimensionality: DNAMTA 64 vs LR 342. Time-decay attribution corrects display channel weight from 0.642 (without decay) to 0.411 (with decay), reducing display overvaluation vs recency channels.

---

## 2. Experiment Critique

**Design:**
Single proprietary Adobe dataset. Ablation study across 4 model variants (LR, LSTM, DNAMTA-touchpoint-only, DNAMTA-fusion). No causal ground truth. No multi-dataset validation.

**Statistical validity:**
Limited — single dataset, no external validation. The ablation structure is clean and shows the value of each component. The time-decay correction finding (display 0.642→0.411) is directionally meaningful but lacks causal validation.

**Online experiments (if any):**
N/A — offline classification evaluation only.

**Reproducibility:**
No code released. Dataset is proprietary Adobe data. Architecture is fully described and reproducible.

**Overall:**
Practical industry paper from Adobe. DNAMTA is a well-designed architecture that systematically improves over LSTM and LR baselines. Main limitation: no causal identification and single proprietary dataset. The time-decay attention is a genuine methodological improvement over pure touchpoint attention.

---

## 3. Industry Contribution

**Deployability:**
High. LSTM + dual attention + fusion is a standard architecture. Adobe's marketing analytics platform context gives this direct industry applicability.

**Problems solved:**
For dating platform attribution: DNAMTA's time-decay attention is directly relevant to downweighting very recent interactions (which may reflect survivorship bias) in favor of earlier interactions. The fusion of sequential interaction patterns with user-level control variables (e.g., user demographics, activity level) mirrors the dating platform architecture.

**Engineering cost:**
Moderate. Two-stage attention LSTM + fusion network. Standard deep learning infrastructure. No specialized causal machinery required.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**
First MTA method combining touchpoint attention and time-decay attention in a unified fusion framework with user control variables; demonstrates that dual attention corrects recency bias in ways that single-attention models miss.

**Prior work comparison:**
DARNN (Ren et al. 2018): dual attention but focuses on impression vs click signals rather than time-decay; no user control variable fusion. Shao & Li (2011), Zhang et al. (2014): no deep sequential modeling. DNAMTA is cited as a baseline in CAMTA (2020) and CausalMTA (2022).

**Verification:**
Results are directionally consistent and the ablation is clean. The display overvaluation finding is a known industry problem that DNAMTA's time-decay addresses.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Adobe Internal Dataset | Not public | No | 426k records, avg 6 touchpoints per journey |

**Offline experiment reproducibility:**
Not reproducible — proprietary Adobe data.

---

## 6. Community Reaction

arXiv 2018, Adobe industry paper. ~150 citations. DNAMTA is a standard baseline in subsequent MTA papers (CAMTA, CausalMTA both include it). The time-decay attention innovation has been adopted in the field. No significant controversies.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| [2018_CIKM_DARNN_Multi-touch-Conversion-Attribution-Dual-Attention](./2018_CIKM_DARNN_Multi-touch-Conversion-Attribution-Dual-Attention.md) | 4. Novelty vs. Prior Work | Unique survey token `DNAMTA` (filename disambiguation) appears in scanned sections. |
| [2020_ICDM_CAMTA_Causal-Attention-Model-Multi-touch-Attribution](./2020_ICDM_CAMTA_Causal-Attention-Model-Multi-touch-Attribution.md) | 1. Summary | Unique survey token `DNAMTA` (filename disambiguation) appears in scanned sections. |
| [2020_ICDM_CAMTA_Causal-Attention-Model-Multi-touch-Attribution](./2020_ICDM_CAMTA_Causal-Attention-Model-Multi-touch-Attribution.md) | Related Work | DNAMTA cited as primary attention-based MTA baseline; CAMTA beats DNAMTA AUC 0.9591 vs 0.9119 on Criteo |
| [2020_arXiv_DeepMTA_Interpretable-Deep-Learning-Multi-touch-Attribution](./2020_arXiv_DeepMTA_Interpretable-Deep-Learning-Multi-touch-Attribution.md) | 4. Novelty vs. Prior Work | Unique survey token `DNAMTA` (filename disambiguation) appears in scanned sections. |
| [2022_KDD_CausalMTA_Eliminating-User-Confounding-Bias](./2022_KDD_CausalMTA_Eliminating-User-Confounding-Bias.md) | 4. Novelty vs. Prior Work | Unique survey token `DNAMTA` (filename disambiguation) appears in scanned sections. |
| [2022_KDD_CausalMTA_Eliminating-User-Confounding-Bias](./2022_KDD_CausalMTA_Eliminating-User-Confounding-Bias.md) | Related Work | DNAMTA cited as non-causal sequence baseline |
| [2023_arXiv_GraphicalMTA_Graphical-Point-Process-Framework-Multi-Touch-Attribution](./2023_arXiv_GraphicalMTA_Graphical-Point-Process-Framework-Multi-Touch-Attribution.md) | 1. Summary | Unique survey token `DNAMTA` (filename disambiguation) appears in scanned sections. |
| [2023_arXiv_GraphicalMTA_Graphical-Point-Process-Framework-Multi-Touch-Attribution](./2023_arXiv_GraphicalMTA_Graphical-Point-Process-Framework-Multi-Touch-Attribution.md) | Experiments | DNAMTA used as primary comparison baseline; Graphical MTA achieves KL 0.008 vs DNAMTA 0.012 |
| [2024_arXiv_DCRMTA_Unbiased-Causal-Representation-Multi-touch-Attribution](./2024_arXiv_DCRMTA_Unbiased-Causal-Representation-Multi-touch-Attribution.md) | 1. Summary | Unique survey token `DNAMTA` (filename disambiguation) appears in scanned sections. |
| [2024_arXiv_DCRMTA_Unbiased-Causal-Representation-Multi-touch-Attribution](./2024_arXiv_DCRMTA_Unbiased-Causal-Representation-Multi-touch-Attribution.md) | Related Work | DNAMTA cited as benchmark baseline; DCRMTA outperforms on synthetic and Criteo-custom |
| [2025_arXiv_LiDDA_Data-Driven-Attribution-LinkedIn](./2025_arXiv_LiDDA_Data-Driven-Attribution-LinkedIn.md) | 1. Summary | Unique survey token `DNAMTA` (filename disambiguation) appears in scanned sections. |

---

## Meta Information

**Authors:** Rohan Arava, Jing Lu, Benjamin Lipshitz, Ren Xu, Haichuan Yang, Licheng Wu, Yuan Qi  
**Affiliations:** Adobe  
**Venue:** arXiv 2018 (industry report)  
**Year:** 2018  
**PDF:** https://arxiv.org/pdf/1809.02230.pdf  
**Relevance:** Core  
**Priority:** 3
