# Survey Card

| Field | Value |
|-------|-------|
| **Title** | Estimating long-term outcome of algorithms |
| **Authors** | Yuta Saito, Himan Abdollahpouri, Jesse Anderton, Ben Carterette, Mounia Lalmas (Spotify Research) |
| **Venue** | Spotify Research Blog (summarizing WWW 2024 paper) |
| **Year** | 2024 |
| **Type** | Blog |
| **Survey Phase** | D3 — Surrogates / Evaluation |
| **NLM Source ID** | f5a62abd-107f-4425-81cc-c84115c70732 |
| **URL** | https://research.atspotify.com/2024/05/estimating-long-term-outcome-of-algorithms |
| **One-line summary** | Blog introduction to LOPE: decompose long-term reward into surrogate + action effects, combining short-term rewards via importance weighting with reward regression for the residual. |
| **Core mechanism** | Long-term reward ≅ surrogate effect + action effect; LOPE estimates surrogate via importance weights on short-term rewards, action effect via regression. |

**Dating applicability:** Gives an offline evaluation recipe for estimating long-term retention/revenue of a new ranking policy from historical logs plus a short experiment — without waiting months. Particularly useful when short-term engagement proxies diverge from long-term match quality.

---

# Paper Reader

## 1. Problem & Motivation

Long-term online experiments are slow and risky. Long-term Causal Inference (LCI) requires strict surrogacy (short-term outcomes fully identify long-term). Typical OPE (IPS/DR) avoids surrogacy but cannot use short-term rewards, yielding high variance when long-term labels are sparse and noisy.

## 2. Method

**LOPE decomposition:**
\[\text{Long-term reward} \cong \text{surrogate effect} + \text{action effect}\]

- **Surrogate effect:** Portion of long-term reward explained by observable short-term rewards (clicks, likes, streams).
- **Action effect:** Residual influenced by specific actions/items that short-term surrogates miss.

**Estimation:**
- Surrogate effect via importance weights defined over short-term rewards.
- Action effect via reward regression (akin to LCI).
- Generalizes LCI (surrogacy = action effect ≡ 0).

LOPE can also produce a learning algorithm optimizing long-term outcomes from historical data.

## 3. Evaluation

- **Simulation:** Historical + short-term experiment sizes \(n \in \{200, \ldots, 1000\}\); varying noise and surrogacy violation.
- **Baselines:** Long-term experiment (skyline); LCI; IPS; DR.
- **Metrics:** MSE, squared bias, variance.
- **Spotify production:** Several real-world A/B tests (details not in blog).

## 4. Key Results

| Comparison | MSE reduction |
|------------|---------------|
| LOPE vs DR at \(n=200\) | **36%** |
| LOPE vs LCI at \(n=1000\) | **71%** |
| LOPE overall | Lowest MSE among feasible methods in all tested scenarios |

LOPE most robust under noise and surrogacy violation. Consistently more accurate on Spotify A/B tests per blog.

## 5. Limitations

Blog does not state LOPE-specific limitations. Notes failures of alternatives: LCI bias under surrogacy violation; OPE high variance without short-term signals; long-term experiments impractical.

(Full WWW 2024 paper adds: LOPE underperforms IPS/DR at very low long-term noise; comparability/stationarity assumption unaddressed.)

## 6. Prior Work Referenced

Methodological baselines only: LCI, OPE, IPS, DR. Full paper: Saito et al., "Long-term Off-Policy Evaluation and Learning," WWW 2024.

---

# Project Relevance

**High relevance for D3 (surrogates/evaluation).** Provides a policy-evaluation framework for estimating long-term ranking outcomes from historical logs + short experiment — directly applicable when dating platforms need to evaluate retention-optimized rankers offline before committing to multi-month A/B tests. Incrementality (policy value), not per-user outcome prediction. No credit assignment, reciprocity, or two-sided treatment.

| # | Field | Answer |
|---|-------|--------|
| 1 | Ranking objective | Offline evaluation of algorithm long-term outcomes; short-term surrogates (clicks, likes) vs long-term retention. |
| 2 | Credit assignment | Not specified in source. |
| 3 | Labels / horizon | Short-term surrogates (clicks, likes); long-term = retention months out. Sparsity: LOPE reduces variance when long-term reward sparse/noisy. |
| 4 | Short/long fusion | Statistical decomposition: surrogate effect + action effect (not neural multi-head fusion). |
| 5 | Prediction vs incrementality | Estimates expected long-term policy performance (OPE/incrementality framing). |
| 6 | Offline / online eval | Simulation (MSE/bias/variance) + Spotify real A/B tests. |
| 7 | Reciprocity / fairness | Not specified in source. |
| 8 | CTR → long-term migration | Not specified in source. |

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
| **Reader** | NotebookLM Q1–Q3 (source f5a62abd-107f-4425-81cc-c84115c70732) |
| **Community Reaction** | No significant community discussion found. |
