# Survey Card

| Field | Value |
|-------|-------|
| **Title** | Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix |
| **Authors** | Vickie Zhang, Michael Zhao, Anh Le, Maria Dimakopoulou, Nathan Kallus |
| **Venue** | arXiv (Netflix) |
| **Year** | 2023 |
| **Type** | Industry |
| **Survey Phase** | D3 — Surrogates / Evaluation |
| **NLM Source ID** | ad7e1e30-9bb9-47cb-ad2b-c14326f53adb |
| **PDF** | https://arxiv.org/pdf/2311.11922 |
| **One-line summary** | Large-scale empirical validation that 14-day linear auto-surrogate indices agree ~95% with 63-day direct measurement decisions across 1,098 Netflix personalization test arms. |
| **Core mechanism** | Linear auto-surrogate: predict 63-day average daily outcome from first \(T\) days of lagged daily observations; difference-in-means on predictions estimates long-term TE. |

**Dating applicability:** Strong evidence that 2-week experiment reads can gate ranking launches with high decision consistency vs 2-month retention windows — directly relevant when dating platforms cannot wait 60+ days per A/B. Trade-off: 35% recall gap on truly positive launches.

---

# Paper Reader

## 1. Problem & Motivation

Long-term A/B measurement is slow and limits experimentation capacity. Short-term proxies risk diverging from long-term effects (novelty, fatigue, clickbait). Surrogate-index theory exists but lacked large-scale production validation of whether surrogate-based ship decisions align with direct long-term reads.

## 2. Method

**Direct measurement (ground truth):**
\[\hat{\tau}_{a,63} = \frac{1}{63|N_a|}\sum_{i\in N_a}\sum_{t=1}^{63} Y_{it} - \frac{1}{63|N_0|}\sum_{i\in N_0}\sum_{t=1}^{63} Y_{it}\]

**Linear auto-surrogate:**
\[\mu_i = \beta_0 + \sum_{t=1}^{T}\beta_t Y_{it} + \epsilon_i, \quad \mu_i = \frac{1}{63}\sum_{t=1}^{63}Y_{it}\]
\[\hat{\tau}_{a,T} = \frac{1}{|N_a|}\sum_{i\in N_a}\hat{\mu}_{i,T} - \frac{1}{|N_0|}\sum_{i\in N_0}\hat{\mu}_{i,T}\]

**Training regimes:** (1) Pre-Test — 63 days of pre-allocation history from same users; (2) Similar Test — coefficients from another historical test in same product space.

## 3. Evaluation

- **Dataset:** 1,098 test arms from 200 personalization A/B tests at Netflix; single-shot allocations.
- **Horizons:** Short = 14 days; long = 63 days (2 months).
- **Baselines:** Direct 63-day measurement; running mean (equivalent to \(\beta_t = 1/T\)).

## 4. Key Results

| Metric | Value |
|--------|-------|
| Decision consistency (hypothesis test agreement) | **~95%** |
| Precision (launch decisions) | **79%** |
| Recall (launch decisions) | **65%** |
| False launches of statistically negative experiences | **0 cases** |
| Bias (avg surrogate − direct read) | **~0** (unbiased) |
| Theoretical capacity gain (2-week vs 2-month cycle) | **up to 300%** |

Surrogate reads more conservative: ~86.5% non-significant vs ~79% for direct 63-day reads.

## 5. Limitations

- Fat-tailed treatment-effect distributions.
- 35% recall gap — misses truly positive launches at 14 days.
- More conservative significance testing (lower power).
- Capacity argument assumes additive TEs, stable TE distribution, low marginal experiment cost, SUTVA.
- Historical retrospective evaluation only; no live surrogate deployment reported.

## 6. Prior Work Cited

Athey et al. (2019) surrogate index; Prentice (1989) surrogacy; Gupta et al. (2019); Kohavi et al. (2012); Azevedo et al. (2020) fat tails.

---

# Project Relevance

**High relevance for D3 (surrogates/evaluation).** Provides the largest published empirical validation of surrogate-index ship decisions in production personalization experiments. For dating: supports shortening experiment windows from 60-day retention to ~2-week composite reads when evaluating ranking changes, with quantified precision/recall trade-offs and zero observed dangerous false positives. Does not specify ranking objectives, credit assignment, or two-sided dynamics.

| # | Field | Answer |
|---|-------|--------|
| 1 | Ranking objective | Not specified in source (personalization algorithm tests in general). |
| 2 | Credit assignment | Not specified in source. |
| 3 | Labels / horizon | \(Y_{it}\) = daily outcome; short \(T=14\) days; long = 63 days. |
| 4 | Short/long fusion | Offline linear auto-surrogate regression on lagged daily outcomes. |
| 5 | Prediction vs incrementality | Predicts user-level \(\mu_i\); TE via difference-in-means on predictions. |
| 6 | Offline / online eval | Retrospective on 200 historical tests; no live online deployment. |
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
| **Reader** | NotebookLM Q1–Q3 (source ad7e1e30-9bb9-47cb-ad2b-c14326f53adb) |
| **Community Reaction** | No significant community discussion found. |
