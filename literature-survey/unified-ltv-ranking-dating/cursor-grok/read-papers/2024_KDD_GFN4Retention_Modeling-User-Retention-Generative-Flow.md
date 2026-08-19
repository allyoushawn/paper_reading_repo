# Survey Card

| Field | Value |
|-------|-------|
| **Title** | Modeling User Retention through Generative Flow Networks |
| **Authors / Company** | Ziru Liu, Shuchang Liu, Bin Yang, Zhenghai Xue, Qingpeng Cai, Xiangyu Zhao, Zijian Zhang, Lantao Hu, Han Li, Peng Jiang / Kuaishou Technology, City University of Hong Kong |
| **Venue / Year** | KDD 2024 |
| **URL** | https://doi.org/10.1145/3637528.3671531 |
| **Source type** | Industry paper |
| **Direction** | D2 |
| **Problem setting** | Session-wise short-video recommendation: GFN models each request as forward flow step; terminal retention reward back-propagated via backward flow and refined Detailed Balance loss |
| **Objective + label + horizon + delay** | End-of-session **retention reward R** (user return frequency) plus per-step immediate rewards r_t (weighted clicks, watch time, likes, etc.); between-session delayed signal |
| **Prediction or incrementality** | Generative flow matching / policy learning (not pointwise CTR prediction) |
| **Architecture** | Transformer+DNN user state encoder; Gaussian forward policy in continuous action space → top-K item list; state flow F_R, backward flow P_B; multiplicative reward R(S)=R·exp(αΣr_t) with refined DB loss |
| **Credit assignment** | Backward probabilistic flow back-propagates terminal retention to each session step (“retention attribution”); immediate rewards enter per-step DB term −α·r_t |
| **Training / counterfactual** | Offline replay on KuaiSim + Kuairand-Pure / ML-1M; online A/B on Kuaishou ranker score-ensemble weights (10% test vs 20% control traffic per stage) |
| **Offline / online eval** | KuaiSim simulator (leave + return modules); live A/B on industrial video platform (billions of daily requests) |
| **Reported gains** | Authors report superiority over CEM, DIN, TD3, SAC, RLUR in offline and live experiments; **exact metric percentages: Not specified in source** (NLM Q2 failed) |
| **Dating applicability** | GFN retention attribution is the most explicit item/step-level credit assignment for delayed return among surveyed papers. Continuous action → top-K mapping matches ensemble-weight production patterns in dating rankers. |
| **Unverified claims** | Specific offline/online lift numbers not extracted from NLM Q1; arxiv https://arxiv.org/pdf/2406.06043.pdf per user hint. |

**Community Reaction:** No significant community discussion found.

---

## 1. Core Problem and Key Contribution

**Core problem:** Immediate-feedback optimization (clicks, likes) misses long-term engagement; **user retention** is between-session, sparse, delayed, and lacks clear per-item attribution. RL optimizes session cumulative reward as retention surrogate but relation to actual return frequency is unclear; RL also faces exploration instability on retention.

**Key contributions:**
- **GFN4Retention:** first GFN framework treating session recommendation as generative trajectory with retention matched at terminal state.
- Backward flow enables **retention attribution** to each recommendation step.
- Multiplicative integrated reward R(S)=R·exp(αΣr_t) with **refined Detailed Balance** objective balancing immediate and retention signals.
- Continuous action-space GFN extension for list-wise recommendation at scale.
- Deployed on Kuaishou (billions of daily requests).

## 2. Proposed Method or Architecture

**State encoding:** Transformer over interaction history + user feature DNN (e_u); parallel context DNN (ψ_u) to avoid over-weighting recent items; s_t = [e_u, ψ_u].

**Forward flow (policy):** φ_fw(s_t) → (μ, σ); sample a_t ~ N(μ,σ); deterministic top-K maps continuous vector to item list.

**Retention flows:** State flow F(s_t) with parametric retention component F_R and non-parametric immediate F_I(s_t)=exp(Σ_{j<t} r_j). Backward flow P_B(s_t|s_{t+1}) = φ_bw(s_t, a_t, s_{t+1}); sigmoid for non-negativity.

**Integrated reward:** R(S) = R · exp(α Σ_{t=1}^{T−1} r_t).

**Refined DB loss:**
- Non-terminal: (log F_R(s_t) + log P_F − log F_R(s_{t+1}) − log P_B − α·r_t)²
- Terminal: (log F_R(s_T) − log R)²

Stabilization offsets β_F, β_B, β_r in log-space.

## 3. Datasets and Baselines

**Kuairand-Pure:** 27,285 users, 7,551 items, 1,436,609 interactions; six positive + two negative feedback signals.

**MovieLens-1M:** 6,400 users, 3,706 items; rating>3 positive.

**KuaiSim:** leave module + return module for cross-session simulation.

**Baselines:** CEM, DIN, TD3, SAC, RLUR.

**Online:** Kuaishou first- and second-stage ranker score-ensemble modules; GFN learns fusion weights vs fixed linear baseline (stage 1) and RL baseline (stage 2).

## 4. Key Quantitative Results

- Authors state GFN4Retention **outperforms** CEM, DIN, TD3, SAC, and RLUR on offline KuaiSim experiments and online A/B tests.
- Ablation and parameter analysis for α, β_F, β_B, β_r reported qualitatively in paper per NLM summary.
- **Exact offline retention/return-time numbers and online DAU/retention lift percentages:** Not specified in source (NLM Q2 unavailable).

## 5. Limitations and Failure Modes

- Plain GFN assumes no intermediate rewards; requires integrated reward design to track per-step engagement.
- RLUR cited as not designed for per-interaction retention attribution; uses cumulative immediate reward as indirect surrogate.
- RL methods face exploration–exploitation instability on retention metrics.
- Continuous-action top-K mapping is approximate vs combinatorial item space.
- Between-session user activity unobservable, adding uncertainty (acknowledged in problem framing).

## 6. Top Cited Prior Works

1. Bengio et al. — Generative Flow Networks (GFN foundation).
2. Cai et al. — **RLUR** (retention RL baseline and prior Kuaishou work).
3. Chandar et al. — survival models for engagement estimation.
4. Chen et al. — tree-structured policy gradient for large-scale interactive recommendation.
5. KuaiSim / KuaiRand — simulator and unbiased sequential dataset.
6. Haarnoja et al. — SAC (off-policy RL baseline).
7. Zhou et al. — DIN (deep CTR / interest model baseline).

---

## Project Relevance (Q3)

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | **Retention** (user return frequency / end-of-session R) combined with **CTR-like immediate proxies** (click, view time, like, comment, follow, forward). Revenue not specified. |
| **(2) Credit assignment** | **Yes — explicit:** backward flow P_B and refined DB loss **back-propagate terminal retention reward to each recommendation step** (“retention attribution”). |
| **(3) Label / horizon; delay / sparsity / censoring** | Retention observed at **end of session / next session**; immediate per-step feedback; authors describe retention as **sparse and delayed**; between-session activity **unobservable**. Censoring not specified in source. |
| **(4) Short-term vs long-term head fusion** | **Learned** integrated flow: multiplicative combination R(S)=R·exp(αΣr_t) with balance parameter α; separate parametric F_R and non-parametric immediate flow F_I — not fixed manual weights. |
| **(5) Prediction vs incrementality** | **Generative policy learning** optimizing session trajectory probability toward retention reward (not pure pointwise prediction). |
| **(6) Offline / online eval; delayed retention; two-sided interference** | Offline KuaiSim + public datasets; **online A/B** on Kuaishou with retention-focused metrics implied. **Delayed cross-session retention** central. Two-sided interference not specified in source. |
| **(7) Reciprocity, congestion, fairness, revenue vs match quality** | Not specified in source. |
| **(8) Migration path from CTR-like model to unified long-term model** | Deploy GFN in **score-ensemble weight modules** atop existing rankers; retain immediate reward terms in DB loss while adding retention flow F_R and backward attribution—incremental layer over production stack. |

---

## Reverse Citation Map

*(blank)*

---

## Meta Information

| Field | Value |
|-------|-------|
| **Date analyzed** | 2026-08-16 |
| **Workplace** | cursor-grok |
| **NLM source ID** | 3183e5a0-4ebb-4f26-bd56-5be0441fe5a5 |
| **Notebook ID** | 67046a44-7490-4fe5-b54a-3f39ef37fdd3 |
