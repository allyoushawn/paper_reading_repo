# Survey Card

| Field | Value |
|-------|-------|
| **Title** | Impatient Bandits: Optimizing Recommendations for the Long-Term Without Delay |
| **Authors** | Thomas M. McDonald, Lucas Maystre, Mounia Lalmas, Daniel Russo, Kamil Ciosek |
| **Venue** | KDD 2023 (Spotify) |
| **Year** | 2023 |
| **Type** | Industry |
| **Survey Phase** | D3 — Surrogates / Evaluation |
| **NLM Source ID** | 5a389db3-49b0-4a99-b6da-bfa1d0e295c5 |
| **PDF** | https://arxiv.org/pdf/2307.09943.pdf |
| **One-line summary** | Bayesian-filter bandit that fuses progressively observed daily traces to predict 60-day stickiness without waiting for full delay. |
| **Core mechanism** | Progressive feedback MAB: Gaussian generative model + meta-learned priors + Thompson sampling ("impatient bandit"). |

**Dating applicability:** Models the cold-start exploration problem where you must rank/promote new profiles or content before 30–90 day retention is observable — progressively using day-1..k engagement traces to estimate long-horizon match/return probability. Analogous to promoting new users or features before LTV labels mature.

---

# Paper Reader

## 1. Problem & Motivation

Recommender systems increasingly optimize long-term engagement (stickiness, retention) but long-term rewards are delayed (60 days for podcast discovery). Waiting for full rewards slows exploration; short-term proxies (e.g., day-2 return) align imperfectly with long-term goals.

## 2. Method

**Progressive feedback bandit:** At each round, intermediate outcomes \(z_k\) are revealed with delay \(\Delta_k\); full reward \(r = \sum_k z_k\) observed at \(\Delta = 60\) days.

**Generative model:**
- \(\bar{z} \sim \mathcal{N}(\mu, \Sigma)\); sample traces \(\bar{z}_m = \bar{z} + \epsilon_m\), \(\epsilon_m \sim \mathcal{N}(0, V)\)
- Reward \(r = w^\top z\) (linear; polynomial/spline extensions in appendix)

**Bayesian filter:** Iterative Gaussian posterior updates on partially observed traces (Kalman-like).

**Meta-learning:** \(\mu, \Sigma, V\) estimated from historical shows via empirical averages across 200 training shows.

**Impatient bandit (Algorithm 2):** Thompson sampling on posterior \(p(r_a)\), updated each round with new partial traces.

## 3. Evaluation

- **Dataset:** 8.77M podcast activity traces (26M cumulative active-days), Sep 2021–May 2022; 200 train + 200 eval shows.
- **Reward:** Stickiness = days engaged in 59 days post-discovery; binary daily activity trace \(z \in \{0,1\}^{59}\).
- **Baselines (all Thompson sampling):** Delayed (wait 60 days); Day-two proxy (\(z_1\) only); Oracle (instant full trace).
- **Protocol:** Offline simulation, 180 rounds (~6 months), \(N \in \{50, 200\}\) shows, varying actions/day.

## 4. Key Results

- Stickiness predictions accurate after **~10 days** of observation (MAE decreases with days and trace count \(M\)).
- **50%** of prior variance explained by **8 days**; **95%** by one month.
- Progressive bandit **substantially outperforms** Delayed and Day-two proxy; performance closer to Oracle.
- Day-two proxy plateaus after ~30 days (misaligned proxy).
- Dynamic library (replacing one show/round): progressive still wins.

## 5. Limitations

- Linear reward assumption; non-linear targets require feature expansion.
- Surrogacy/comparability assumptions for non-linear extensions must be tested empirically.
- Gaussian noise poor fit for binary daily indicators (mitigated by CLT with many traces).
- **Non-personalized**; contextual extension sketched but not fully developed.
- High day-to-day volatility in noise covariance \(V\).
- **No online A/B test** reported; offline simulation only.
- Does not model incrementality vs control; predictive not causal uplift.

## 6. Prior Work Cited

Maystre et al. (2023) long-term audio RL; Li et al. (2010) contextual bandits; Athey et al. (2019) surrogate index; Kandasamy et al. (2018) parallel bandits; Rasmussen & Williams (2006) GP; Prentice (1989); Hohnhold et al. (2015) long-term metrics.

---

# Project Relevance

**High relevance for D3 (delayed labels / surrogate fusion).** Shows how to operationally fuse progressive short-horizon signals into a long-horizon reward estimate for sequential decisions — complementary to experiment-level surrogate indices. For dating: applicable to cold-start item/user exploration where early swipe/reply/return traces predict 30–90 day retention before labels arrive. Does not address two-sided markets, slate-level credit assignment, or CTR→LTV model migration.

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
| **Reader** | NotebookLM Q1–Q3 (source 5a389db3-49b0-4a99-b6da-bfa1d0e295c5) |
| **Community Reaction** | No significant community discussion found. |
