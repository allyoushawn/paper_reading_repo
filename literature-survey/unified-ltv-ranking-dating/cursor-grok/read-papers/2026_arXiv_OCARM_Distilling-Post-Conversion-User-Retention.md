# Survey Card

| Field | Value |
|-------|-------|
| **Title** | Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling |
| **Authors** | Tianbao Ma, Ruochen Yang, Chengen Li, Yuexin Shi, Jiangxia Cao, Linxun Chen, Zhaojie Liu, Yanan Niu, Han Li, Kun Gai |
| **Venue** | arXiv (Kuaishou) |
| **Year** | 2026 |
| **Type** | Industry |
| **Survey Phase** | D4 — Label Design / Long-Term Objectives |
| **NLM Source ID** | dc23ab85-0648-42fa-821c-297f4dc06534 |
| **PDF** | https://arxiv.org/pdf/2604.25839.pdf |
| **One-line summary** | Two-stage distillation (OCARM) transfers post-conversion onboarding-content signals into bidding-time retention predictions without feature leakage. |
| **Core mechanism** | Stage 1 HAE encodes onboarding content (teacher, with leakage); Stage 2 SFE + Q-Former aligns observable user sequences to teacher via distillation loss. |

**Dating applicability:** Directly relevant when post-match onboarding experience (first messages, profile views, early matches) strongly predicts retention but is unavailable at ranking/bidding time — distill those signals into pre-conversion models.

---

# Paper Reader

## 1. Problem & Motivation

RTB re-engagement systems must predict long-term revisit probability before conversion, when onboarding content (post-conversion in-app interactions) is unavailable. Using onboarding content in training causes feature leakage; querying the recommender at bid time is infeasible due to latency and preference mismatch.

## 2. Method

**Stage 1 — Onboarding Content Encoding (teacher, with leakage):**
- Hierarchical Attention Encoder (HAE): intra-day cross-attention compression + inter-day causal self-attention over multi-day onboarding sequences \(x_c\).
- Joint BCE retention loss: \(\mathcal{L}_{Stage1} = \text{BCE}(f_{retention}([x_u; e_c]), y)\).

**Stage 2 — User Representation Distillation (student):**
- Freeze HAE teacher.
- Sequence Fusion Encoder (SFE) with Q-Former compresses historical interactions + ad contexts.
- Task-specific towers per retention horizon.
- Alignment: \(\mathcal{L}_{align} = \sum_{t \in Task} \mathcal{L}_{sim}(e_u^{(t)}, \text{sg}(e_c^{(t)}))\).
- Joint: \(\mathcal{L}_{Stage2} = \text{BCE}(f_{retention}([x_u; e_u]), y) + \lambda \mathcal{L}_{align}\).

**Inference:** Teacher discarded; \(\hat{y} = f_{retention}([x_u; g_u(x_u)])\).

**Label:** Revisit frequency \(LT_d\) over next \(d\) days.

## 3. Evaluation

- **Dataset:** Kuaishou industrial growth data — millions of users, billions of interactions.
- **Tasks:** LT1 (1-day), LT7 (7-day) offline; LT30 online.
- **Baselines:** PPNet retention model (Base); Stage 1 upper bound; Stage 2 only (ablation); encoder variants (MLP → HAE → SFE).

## 4. Key Results

**Offline (AUC / GAUC):**

| Method | LT1 AUC | LT7 AUC |
|--------|---------|---------|
| Base | 0.7297 / 0.7227 | 0.6903 / 0.6909 |
| Stage 1 upper bound | 0.7468 / 0.7371 | 0.7002 / 0.7007 |
| Full OCARM | **0.7369 / 0.7311** | **0.6949 / 0.6957** |

Encoder ablation ΔAUC: Variant 1 +0.35/+0.23%; Variant 2 +0.56/+0.32%; Full +0.72/+0.46%.

**Online A/B (LT30):**

| Cohort | Re-engaged Devices | LT30 |
|--------|-------------------|------|
| Non-uninstalled | **+20.47%** | **+11.55%** |
| Uninstalled | **+34.43%** | **+22.18%** |

## 5. Limitations

- Stage 2-only (joint training without frozen teacher) collapses (LT1 AUC 0.6709).
- Gap to Stage 1 upper bound remains substantial.
- Historical interaction sequences suffer temporal staleness for re-engaged users.
- Ad contexts carry limited personalized intent.
- No item-level credit assignment to recommender exposures.

## 6. Prior Work Cited

Cai et al. (2023) retention RL; Cao et al. (2026) foresight prediction; Chang et al. (2023) PPNet; Li et al. (2023) Q-Former/BLIP-2; Liu et al. (2024) GFN retention; Wang et al. (2025) retention-aware rec.

---

# Project Relevance

**High relevance for D4 (label design / long-term objectives).** Addresses the temporal feature-leakage boundary between post-conversion experience and pre-conversion retention prediction — directly analogous to dating where early post-match engagement predicts long-term retention but is unavailable when ranking cold-start or re-engaged users. Outcome prediction (not incrementality). No reciprocity or two-sided treatment.

| # | Field | Answer |
|---|-------|--------|
| 1 | Ranking objective | User retention (revisit frequency \(LT_d\)) over CTR-like short-term signals. |
| 2 | Credit assignment | Not specified in source (user-level bidding-stage prediction). |
| 3 | Labels / horizon | \(LT_d\) revisit frequency; offline LT1/LT7; online LT30. |
| 4 | Short/long fusion | Task-specific towers per horizon; distillation alignment (not event-head fusion). |
| 5 | Prediction vs incrementality | Predicts outcome \(p(y|x_u)\); not treatment effect. |
| 6 | Offline / online eval | Offline AUC/GAUC on industrial data; online A/B in RTB system. |
| 7 | Reciprocity / fairness | Not specified in source. |
| 8 | CTR → long-term migration | Two-stage distillation: Base → Stage 1 teacher (leaked content) → Stage 2 student (leakage-free inference). |

---

# Reverse Citation Map

| This paper cites → | Notes |
|--------------------|-------|
| | |

| ← Cited by this survey | Notes |
|------------------------|-------|
| | |

---

# Meta Information

| Field | Value |
|-------|-------|
| **Card date** | 2026-08-16 |
| **Workplace** | cursor-grok |
| **Reader** | NotebookLM Q1–Q3 (source dc23ab85-0648-42fa-821c-297f4dc06534) |
| **Community Reaction** | No significant community discussion found. |
