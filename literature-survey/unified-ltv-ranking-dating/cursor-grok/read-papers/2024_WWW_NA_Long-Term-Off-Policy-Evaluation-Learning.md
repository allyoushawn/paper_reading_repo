# Survey Card

| Field | Value |
|-------|-------|
| **Title** | Long-term Off-Policy Evaluation and Learning |
| **Authors** | Yuta Saito, Himan Abdollahpouri, Jesse Anderton, Ben Carterette, Mounia Lalmas |
| **Venue** | WWW 2024 (Spotify) |
| **Year** | 2024 |
| **Type** | Academic / Industry |
| **Survey Phase** | D3 — Surrogates / Evaluation |
| **NLM Source ID** | 7fee3f6b-6faa-436e-aa21-d9477fef7739 |
| **PDF** | https://arxiv.org/pdf/2404.15691.pdf |
| **One-line summary** | LOPE estimator decomposes long-term reward into surrogate + action effects, using surrogate importance weighting to beat LCI and standard OPE. |
| **Core mechanism** | \(q(x,a,s) = g(x,s) + h(x,a,s)\); LOPE combines surrogate IW on \(g\) with regression on \(h\); extends to LOPE-PG policy learning. |

**Dating applicability:** Enables offline evaluation of a new ranking policy's long-term retention/LTV using only week-1 engagement logs and historical data — without running a multi-month A/B test. Directly relevant when click/match proxies may not fully mediate long-term outcomes (surrogacy violations common in engagement optimization).

---

# Paper Reader

## 1. Problem & Motivation

Long-term policy value (e.g., annual active users, revenue) requires year-long A/B tests — slow and risky. **LCI** uses short-term surrogates but requires strict surrogacy (\(r \perp a \mid x, s\)); violated by click-bait-like effects. **Standard OPE** (IPS/DR) avoids surrogacy but ignores less-noisy short-term rewards, suffering high variance.

## 2. Method

**Reward decomposition:**
\[q(x,a,s) = g(x,s) + h(x,a,s)\]
- \(g\): surrogate effect (predictable from short-term rewards \(s\) alone)
- \(h\): residual action effect (not captured by surrogates)

**LOPE estimator:**
\[V_{\mathrm{LOPE}}(\pi_1; D_H) = \frac{1}{n}\sum_i \left\{ \frac{\pi_1(s_i|x_i)}{\pi_0(s_i|x_i)}(r_i - \hat{h}(x_i,a_i,s_i)) + \hat{h}(x_i,\pi_1) \right\}\]

- Surrogate importance weight \(w(x,s) = \pi_1(s|x)/\pi_0(s|x)\) estimated via Bayes' rule and \(\pi_0(a|x,s)\) regression.
- **Unbiased** if surrogacy holds OR conditional pairwise correctness (CPC) on \(\hat{h}\).
- **LOPE-PG:** policy gradient extension for long-term off-policy learning.

## 3. Evaluation

**Synthetic:** 1,000 users, 10D context, |A|=30; surrogacy violation \(\lambda \in [0,1]\); noise \(\sigma_r \in [1,9]\).

**Real-world (Spotify):** 3-week A/B test, ~4M users, 3 policies; |A|>1,000 contents.
- Short-term \(s\): streams, clicks, likes, dislikes at **week 1 (day 7)**
- Long-term \(r\): streams at **week 3 (day 21)**

**Baselines:** Long-term experiment (AVG), LCI, IPS, DR, Reg-based (for OPL).

## 4. Key Results

**Synthetic:**
- Lowest MSE across data sizes; **36%** MSE reduction vs DR at \(n=200\); **71%** vs LCI at \(n=1000\).
- Robust to surrogacy violation (\(\lambda\)); LCI degrades.
- **45%** MSE reduction vs DR at \(\sigma_r=9\).
- Policy selection: **85%** correct at \(\sigma_r=9\) vs **79%** for IPS/DR.
- LOPE-PG: **~60%** improvement over DR-PG at \(n_H=500\); **~80%** at \(\sigma_r=9\).

**Real-world (Table 2, MSE ×10⁻³):**

| Policy | LCI | IPS | DR | LOPE |
|--------|-----|-----|-----|------|
| #1 | 8.316 | 8.474 | 8.051 | **6.999** |
| #2 | 9.566 | 9.735 | 9.411 | **8.615** |
| #3 | 6.476 | 6.614 | 6.343 | **5.715** |

LOPE achieves **9.2–15.0%** MSE reduction vs DR (second best).

## 5. Limitations

- No guidance on short-term reward preprocessing / representation learning.
- Comparability assumption: reward distributions static across historical and experiment data (violations from seasonality).
- Real-world eval only **3-week** horizon; year-long metrics unvalidated.
- Long-term reward regression remains hard (sparse, noisy).
- Does not address two-sided market dynamics.

## 6. Prior Work Cited

Athey et al. (2019, 2020) surrogate index/LCI; Dudík et al. (2011, 2014) DR; Rosenbaum & Rubin (1983) propensity scores; Prentice (1989) surrogacy; Saito & Joachims (2021–2023) OPE for recsys; Kallus & Mao (2020); Wang et al. (2022) recsys surrogates.

---

# Project Relevance

**High relevance for D3.** Provides the offline evaluation bridge between short-horizon ranking experiments and long-term retention/LTV policy value — with explicit handling of surrogacy violation (action effects not mediated by short-term metrics). For dating: evaluate whether a new match-ranking policy improves 30-day retention using only week-1 match/reply/return signals plus historical logs. Complements experiment-level surrogate construction (Tripuraneni, Athey) with policy-level OPE. No ranking architecture, credit assignment, or two-sided market coverage.

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
| **Reader** | NotebookLM Q1–Q3 (source 7fee3f6b-6faa-436e-aa21-d9477fef7739) |
| **Community Reaction** | No significant community discussion found. |
