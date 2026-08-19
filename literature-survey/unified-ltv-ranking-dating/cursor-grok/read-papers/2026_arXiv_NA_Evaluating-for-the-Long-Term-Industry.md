# Survey Card

| Field | Value |
|-------|-------|
| **Title** | Evaluating for the Long Term: Learnings from Industry |
| **Authors** | Sigerson, Cunningham, Chou, Pandey, Stray, Yuan, Bakshy, et al. (26 experts, 15 platforms, 4 universities) |
| **Venue** | arXiv industry synthesis (2026) |
| **Year** | 2026 |
| **Type** | Industry workshop paper |
| **Survey Phase** | D3 — Surrogates / Evaluation |
| **NLM Source ID** | 4e0cbb02-d402-485e-8cb7-c37581a20095 |
| **PDF** | https://arxiv.org/pdf/2608.08043.pdf |
| **One-line summary** | Consensus propositions from 15 platforms on using short-run experiments and surrogate indices to align with long-term outcomes. |
| **Core mechanism** | Workshop-synthesized best practices: autosurrogates, experiment-based vs observational surrogacy, bias correction for correlated measurement error. |

**Dating applicability:** Canonical framing is predicting 6-month DAU from 7-day engagement in ranking experiments — directly analogous to predicting 30/90-day retention or match quality from short-horizon swipe/reply metrics. Warns that content-quality and monetization changes are prime sign-reversal cases relevant to dating feed ranking.

---

# Paper Reader

## 1. Problem & Motivation

Platforms prioritize long-term outcomes (retention, DAU, LTV) but typical A/B tests run 3 days–3 months — too short to observe long-term effects directly. Teams extrapolate short-run treatment effects, risking the surrogate paradox (short-run gains that reverse long-run).

## 2. Method

Not a single algorithm; a **framework of consensus propositions** from a daylong workshop:

- **Observation-based surrogacy:** Fit long-term outcome on short-term proxies from observational data (requires unconfoundedness, transportability, full mediation — often violated).
- **Experiment-based surrogacy:** Learn/evaluate surrogates from a portfolio of long-run experiments (preferred but requires many long-run tests).
- **Univariate autosurrogate:** Short-run version of the target long-run metric; often hard to beat.
- **Six bias-correction techniques** for correlated measurement error in TE-on-TE regressions: bigger experiments, high-SNR proxies only, strongest experiments only, explicit bias adjustment, experiment splitting, backtesting decision rules.

## 3. Evaluation

No single benchmark. Evidence drawn from platform case studies:

| Platform | Evidence |
|----------|----------|
| Netflix | 200 A/B tests: 2-week vs 2-month launch agreement **95%** |
| Pandora | 21-month ad-load study: observational methods often biased, wrong sign |
| Meta/Facebook | Notification filter: short-term decline, +1 year gain; minimal integrity holdout: +0.4% impressions at 1 month, lower activity at 2 years |
| YouTube | Trashy-video downrank: −0.5% watch time at 3 weeks, recovery by 3 months |
| Pinterest | Badging: +7% DAU short-term → +2.5% long-run |
| Google | Ad-load effects continue scaling weeks/months into experiment |

## 4. Key Results

- Sign reversals are **rare** overall; concentrate in content quality, hyper-monetization, and pricing (lead-day bias).
- **Autosurrogates** are often hard to beat; elaborate surrogate indices are hard to explain to stakeholders.
- **Experiment-learned surrogates** preferred over observational; few platforms have large enough long-run experiment portfolios.
- Naive TE-on-TE regression is **asymptotically biased** from correlated measurement error.
- Decision consistency (precision/recall of launch decisions) may be a lower bar than unbiased TE estimation.

## 5. Limitations

- Confounding in observational surrogacy is expected on platforms.
- Observational surrogate CIs underestimate uncertainty (ignore residual confounding).
- Long-run experiment portfolios are selectively terminated (asymmetric, class-specific).
- Weak instruments when short-term proxy TEs are small.
- Activity bias: experimental samples oversample active users.
- Persistent treatments violate point-in-time surrogacy assumptions.
- Black-box surrogate indices erode stakeholder trust.

## 6. Prior Work Cited

Athey et al. (2026) surrogate index; Bibaut et al. (2024) weak experiments; Cunningham et al. (2025) engagement vs quality; Hohnhold et al. (2015) long-term ad load; Tripuraneni et al. (2024) proxy selection; Zhang et al. (2024) Netflix surrogate validation; Kohavi & Thomke (2017) online experiments.

---

# Project Relevance

**High relevance for D3.** This is the industry playbook for the evaluation layer our survey cares about: which short-horizon metrics to trust, when sign reversals happen, and how platforms actually validate surrogates. Directly informs dating ranking experiments where 1–2 week tests must proxy 30–90 day retention/match outcomes. Complements model-level LTV ranking papers by documenting the experiment-decision infrastructure they must plug into. Does not cover ranking architecture, credit assignment, or two-sided market mechanics.

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
| **Reader** | NotebookLM Q1–Q3 (source 4e0cbb02-d402-485e-8cb7-c37581a20095) |
| **Community Reaction** | No significant community discussion found. |
