# Paper Analysis: LiDDA: Data Driven Attribution at LinkedIn

**Source:** https://arxiv.org/pdf/2505.09861.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** LiDDA: Data Driven Attribution at LinkedIn  
**Authors:** Bencina et al. (full author list on PDF title page)  
**Abstract:** LinkedIn’s GTM marketing and Ads platform need unified user-level attribution across owned and external channels. MMM gives macro incrementality but not journeys; classical DDA misses macro factors and suffers missing external impressions under GDPR/CCPA; last-touch biases to bottom-of-funnel. **LiDDA** is a production, large-scale **transformer-style attention** DDA system with: (i) temporal-aware encodings for irregular gaps (tAPE + day / day-of-week embeddings); (ii) **probabilistic imputation** of missing paid-media impressions from aggregates; (iii) **training-time calibration** to MMM channel shares (MSE/KL penalties) without post-hoc rescaling; (iv) **sessionization + downsampling** to balance high-frequency in-feed touches vs. sparse email; (v) member and company embeddings plus **LLM-derived campaign embeddings**. Attention weights (flattened, single-layer multi-head self-attention) normalize to sum to 1 within each path and are interpreted as **percent contribution per touchpoint**; channel-level rescaling aligns with MMM.

**Key contributions:**

- Industry-scale transformer attention DDA with explicit MMM reconciliation at training time.
- Privacy-aware probabilistic reconstruction of external impressions (Geometric for clickers, Poisson for no-click paths; convex optimization formulation).
- End-of-path bias diagnosis for LSTM+attention (DNAMTA) motivating direct self-attention on the touch sequence.
- Online validation vs. randomized email holdouts using IPW-balanced causal comparisons.

**Methodology:** Binary classifier \(P(Y \mid E_M, E_C, S)\); multi-head self-attention over embedded touch sequences with temporal encodings; imputation algorithms; joint loss \(L_{\text{total}} = L_{\text{DDA}} + \beta L_{\text{calib}}\) vs. MMM channel targets.

**Main results:** Offline ROC-AUC / PR-AUC > 0.97 with stable retraining across subsets; online lift tests — LiDDA vs. experimental lift differences about −2.23%, +0.95%, +2.41% across three tests (bootstrap CIs reported); ablations show sequence-only drops AUC ~5.1%; date removal most destabilizes channel mix (MSD 49.3).

---

## 2. Experiment Critique

**Design:** Strong mix of offline classification metrics, ablations on embeddings, attention randomization stress test, and real incremental email holdouts with IPW.

**Statistical validity:** Bootstrap CIs for online comparisons; AA tests for experiment sanity; Anderson–Darling on predicted conversion stability.

**Online experiments (if any):** Yes — randomized email holdouts; sparse email cadence noted (~weekly to selected members).

**Reproducibility:** Proprietary LinkedIn GTM + Ads data; methods detailed but external teams cannot replicate end-to-end.

**Overall:** Rare combination of production systems narrative + quantitative validation; attention→credit mapping still carries known interpretability caveats, which authors acknowledge with mitigations (single layer, permutation tests).

---

## 3. Industry Contribution

**Deployability:** Very high for organizations with both user-level paths and periodic MMM — blueprint for reconciling micro credits with macro incrementality.

**Problems solved:** Privacy gaps for external impressions, MMM/DDA inconsistency, BOFU last-touch bias, class imbalance from high-frequency channels.

**Engineering cost:** High — LLM campaign embeddings, imputation stack, calibration loop, and ops for sessionization/downsampling.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First industry-deployed large-scale transformer attention DDA integrating MMM at training time with privacy-driven imputation.

**Prior work comparison:** Contrasts with Shao & Li logistic MTA (early-touch bias), DNAMTA/LSTM+attention (end-of-path bias), CAMTA / CausalMTA as deep baselines, classical MMM literature.

**Verification:** Online lift alignment supports that attention credits track experimental incrementality on tested channels; generalization beyond email holdouts not established in excerpt.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| LinkedIn GTM + Ads proprietary journeys | Internal | No | Primary training/eval |

**Offline experiment reproducibility:** Methods reproducible on public MTA datasets; numbers will not match.

---

## 6. Community Reaction

Not assessed in this pass (very new industry preprint / product paper).

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** Bencina et al.  
**Affiliations:** LinkedIn  
**Venue:** arXiv (2025)  
**Year:** 2025  
**PDF:** https://arxiv.org/pdf/2505.09861.pdf  
**Relevance:** Core  
**Priority:** 1

---

## Project Relevance

**(A) Per-touchpoint credit vs aggregate lift:** **Strong match** — normalized attention weights are explicit **per-touchpoint fractional credits** within each path (then channel-calibrated via MMM).

**(B) Continuous engagement / retention outcomes:** The deployed objective is **binary conversion**; GTM scope mentions retention objectives at a high level, but **continuous days-active style labels** are **not specified in source** as the trained head.

**(C) Selection bias / activity imbalance:** **Strong partial match** — sessionization + downsampling mitigate high-frequency channels crowding paths; **member embeddings** capture latent traits; **IPW** used when validating against experiments for treated vs. control imbalance.

---

*[If datasets are accessible: To run experiments on these datasets, use the experiment-runner skill with the dataset URL or info above.]*
