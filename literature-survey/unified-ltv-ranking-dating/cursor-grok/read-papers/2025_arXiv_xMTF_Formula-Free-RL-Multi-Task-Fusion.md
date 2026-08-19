# Survey Card

| Field | Value |
|-------|-------|
| **Title** | xMTF: A Formula-Free Model for Reinforcement-Learning-Based Multi-Task Fusion in Recommender Systems |
| **Authors** | Yang Cao, Changhao Zhang, Xiaoshuang Chen, Kaiqiao Zhan, Ben Wang (Kuaishou Technology) |
| **Venue** | WWW 2025 |
| **Year** | 2025 |
| **Type** | Industry |
| **Survey Phase** | D1 — Long-Term Ranking Objectives |
| **NLM Source ID** | da625059-d4d2-4065-9d44-6a9fe8a1cfba |
| **PDF** | https://arxiv.org/pdf/2504.05669.pdf |
| **One-line summary** | Replaces fixed multi-task fusion formulas with learnable monotonic fusion cells (MFCs) trained via a two-stage hybrid RL+SL strategy to maximize long-term satisfaction (daily watch time) from short-term prediction heads. |
| **Core mechanism** | Sprecher Representation Theorem → per-prediction monotonic fusion cells compose item score; outer RL stage optimizes fusion against session-level long-term reward, inner SL stage transfers supervised signal; deployed with streaming online updates. |

**Dating applicability:** Directly relevant to replacing a post-hoc CTR/CVR+uplift blend: learn how to fuse like/match/conversation heads into one score optimized for delayed retention/revenue rather than tuning fixed formula weights.
**Dating applicability:** Credit assignment stays at fusion-layer (session MDP), not attributing a 30-day retention label to showing one profile; no reciprocity or congestion modeling.

---

# Paper Reader

## 1. Problem & Motivation

Recommender systems use MTL heads (CTR, like rate, etc.) plus an MTF module to merge predictions into a ranking score. Existing RL-based MTF methods only tune coefficients inside pre-defined fusion formulas, limiting the search space and long-term satisfaction optimization.

## 2. Method

**RL formulation:** User = environment, recommender = agent; fusion parameters \(a_t\) are RL actions; reward \(r_t\) is session-level long-term feedback (daily watch time, retention).

**xMTF:** Any suitable fusion function expressed as composition of single-variable monotonic functions (Sprecher Representation Theorem). Monotonic Fusion Cells (MFCs) replace fixed formulas.

**Two-Stage Hybrid (TSH) training:**
- **Outer stage:** RL optimizes MFC parameters against long-term user satisfaction.
- **Inner stage:** Supervised transfer loss anchors fusion to immediate prediction quality.

**Serving:** Streaming training — session data sent to xMTF on session end; model converges in ~2 days from scratch, then continuously updated online.

## 3. Evaluation

- **Offline:** KuaiRand simulator; metric = total watch time (seconds) over simulated sessions.
- **Baselines:** CEM, TD3, BatchRL-MTF, TSCAC, MR-MPL (each with two fusion formulas); UNEX-RL online.
- **Online:** Short-video platform with **100M+** users; 7-day A/B vs UNEX-RL; primary metric = daily watch time.

## 4. Key Results

**Offline (KuaiRand, total watch time):**

| Method | Total Watch Time (s) |
|--------|---------------------|
| Best formula-based baseline (TSCAC-2) | 1194.7 (±12.4) |
| **xMTF** | **1279.7 (±12.9)** |
| xMTF w/o outer (no RL) | 1092.8 (±9.1) |
| xMTF w/o inner (degenerates to formula) | 1106.3 (±11.2) |

**Online vs UNEX-RL (7-day A/B):**

| Metric | Gain |
|--------|------|
| Daily watch time | **+0.833%** [−0.11%, 0.11%] |
| Play counts | **+0.583%** [−0.14%, 0.14%] |
| Comment | **+2.391%** [−1.26%, 1.26%] |
| Share | **+2.205%** [−0.81%, 0.81%] |

Paper notes 0.1% daily watch time improvement is statistically significant on their platform.

## 5. Limitations

- Long-term reward is session-level (daily watch time), not item-attributed retention.
- MFC monotonicity assumption may not hold for all fusion semantics.
- KuaiRand offline simulator may not capture full production dynamics.
- No reciprocity, congestion, or two-sided market treatment.
- Does not unify MTL label definition — only fuses existing short-term heads.

## 6. Prior Work Cited

Cai et al. (2023) RLUR retention RL; Zhang et al. (2024) BatchRL-MTF; Zhang et al. (2023) UNEX-RL multi-stage MTF; Han et al. DRRS; TSCAC two-stage constrained actor-critic.

---

# Project Relevance

**High relevance for D1 and Q4.** Production-validated pattern for making long-term satisfaction the RL reward while keeping existing short-term prediction towers — directly analogous to fusing like/match/conversation heads toward retention instead of a fixed blend. Weak on Q2 (item-level delayed credit), Q5 (incrementality), and Q7 (two-sided).

| # | Field | Answer |
|---|-------|--------|
| 1 | Ranking objective | Long-term user satisfaction via session-level daily watch time / retention as RL reward; MTL heads remain CTR-like short-term proxies. |
| 2 | Credit assignment | Session-level MDP; fusion action per request, reward at session end — not per-item attribution of delayed retention. |
| 3 | Labels / horizon | RL reward = daily watch time (long-term); MTL labels = immediate feedback types. |
| 4 | Short/long fusion | Learned formula-free MFC fusion (RL outer + SL inner), replacing fixed weighted-sum/log formulas. |
| 5 | Prediction vs incrementality | Optimizes accumulated long-term reward via RL policy over fusion weights; not CATE/uplift per exposure. |
| 6 | Offline / online eval | KuaiRand simulator + 7-day online A/B on 100M-user platform vs UNEX-RL. |
| 7 | Reciprocity / fairness | Not specified in source. |
| 8 | CTR → long-term migration | Keep MTL towers, replace fixed fusion formula with xMTF RL-trained MFCs optimized on long-term reward. |

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
| **Reader** | PDF/URL fallback — arxiv:2504.05669 (NLM RESOURCE_EXHAUSTED) |
| **Community Reaction** | No significant community discussion found. |
