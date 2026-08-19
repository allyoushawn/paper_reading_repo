# Survey Card

| Field | Value |
|-------|-------|
| **Title** | Choosing a Proxy Metric from Past Experiments |
| **Authors** | Nilesh Tripuraneni, Lee Richardson, Alexander D'Amour, Jacopo Soriano, Steve Yadlowsky |
| **Venue** | KDD 2024 (Google / DeepMind) |
| **Year** | 2024 |
| **Type** | Industry |
| **Survey Phase** | D3 — Surrogates / Evaluation |
| **NLM Source ID** | e33e4636-ba5b-4b65-a4b4-abeb9df03476 |
| **PDF** | https://arxiv.org/pdf/2309.07893.pdf |
| **One-line summary** | Learns sample-size-adaptive composite proxy metrics from a corpus of past A/B tests via portfolio optimization and hierarchical denoising. |
| **Core mechanism** | Proxy quality → Sharpe-ratio QP over base proxies; latent TE covariances from hierarchical model on historical experiments. |

**Dating applicability:** Directly relevant for choosing which short-horizon experiment metrics (e.g., 7-day engagement, match rate, reply rate) best track delayed retention/LTV north stars when running ranking A/B tests. Gives a principled way to weight multiple short-term proxies for launch decisions without waiting for full retention windows.

---

# Paper Reader

## 1. Problem & Motivation

Long-term north-star metrics in randomized experiments are slow, noisy, and often unavailable at decision time. Platforms instead rely on short-term proxy metrics, but lack a rigorous framework for selecting or combining them across a homogeneous population of past A/B tests.

## 2. Method

**Proxy quality** measures how well an observed proxy treatment effect tracks the latent population treatment effect on the long-term outcome: correlation between \(\Delta^N\) and \(\hat{\Delta}^P\), balancing alignment and signal-to-noise.

For composite proxies, optimal weights \(w\) maximize \(\mathrm{corr}(\Delta^N, w^\top \hat{\Delta}^P)\) subject to \(1^\top w = 1, w \ge 0\). This maps to **Sharpe-ratio portfolio optimization** (convex QP).

A **hierarchical Gaussian model** on a historical corpus denoises observed TEs to estimate latent covariances \(\Lambda^{NP}, \Lambda^{PP}\). Weights adapt to experiment sample size via \(\hat{\Xi}^{PP} \approx \Xi^{PP}_{\mathrm{ref}}/n\).

## 3. Evaluation

- **Dataset:** 307 historical A/B tests from an industrial recommendation engine; 1 north-star metric + 3 hand-selected auxiliary proxies.
- **Baselines:** Individual auxiliary metrics; Richardson et al. (2023) composite proxy optimizing proxy score.
- **Protocol:** Stratified 4-fold CV; metrics: proxy quality, proxy score, metric sensitivity.

## 4. Key Results

| Method | Sensitivity | Proxy Score | Proxy Quality |
|--------|-------------|-------------|---------------|
| New composite proxy | 0.181 | **0.666** | **0.302** |
| Baseline composite (Richardson et al.) | 0.182 | 0.611 | 0.279 |
| Auxiliary Metric 1 | 0.062 | 0.611 | 0.174 |
| Auxiliary Metric 2 | 0.368 | 0.222 | 0.258 |
| Auxiliary Metric 3 | 0.166 | 0.104 | 0.030 |

Optimal weights shift with sample size: smaller experiments favor lower-variance proxies; larger experiments weight noisier but better-aligned proxies more heavily.

## 5. Limitations

- Strong i.i.d. assumption on latent population TEs across experiments; fragile under non-stationarity.
- Linear composite proxies only; no nonlinear combinations.
- Homogeneous experiment population; no heterogeneous treatment effects.
- Evaluation criteria compare to noisy observed north-star TEs, not true latent effects.
- No reported live online deployment of the constructed proxy.

## 6. Prior Work Cited

Richardson et al. (2023) Pareto optimal proxy metrics; Athey et al. (2019) surrogate index; Elliott et al. (2015) surrogate paradox; Wang et al. (2022) recsys surrogates; Prentice (1989); Deng & Shi (2016); VanderWeele (2013).

---

# Project Relevance

**High relevance for D3 (surrogates/evaluation).** This paper addresses exactly how to construct experiment-level composite proxies from historical A/B portfolios — the decision layer above any ranking model. For dating, it supports: (a) selecting which short-horizon metrics to gate launches on, (b) weighting multiple proxies (matches, messages, returns) by experiment size, and (c) meta-analytic denoising when short- and long-term TEs share correlated measurement error. It does not specify ranking objectives, credit assignment, or two-sided market dynamics.

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
| **Reader** | NotebookLM Q1–Q3 (source e33e4636-ba5b-4b65-a4b4-abeb9df03476) |
| **Community Reaction** | No significant community discussion found. |
