# Survey Card

| Field | Value |
|-------|-------|
| **Title** | PROXIMA: Proxy Metric Validation with Segment-Level Fragility Detection for Online Controlled Experiments |
| **Authors** | Avinash Amudala (Rochester Institute of Technology) |
| **Venue** | arXiv |
| **Year** | 2026 |
| **Type** | Academic / Industry |
| **Survey Phase** | D3 — Surrogates / Evaluation |
| **NLM Source ID** | 8fa3230b-b02b-4a06-be8d-cebe193d4223 |
| **PDF** | https://arxiv.org/pdf/2604.14352.pdf |
| **One-line summary** | Diagnostic framework scoring proxy-metric reliability via normalized effect correlation, directional accuracy, and segment-level fragility rate — detecting Simpson's Paradox-style ship/no-ship failures without constructing a surrogate index. |
| **Core mechanism** | Composite reliability \(R \in [0,1]\) from three components; fragility = fraction of segments where proxy effect sign contradicts global long-term effect; decision simulation compares proxy-based vs oracle launch policies. |

**Dating applicability:** Before trusting 7-day match-rate or conversation-rate proxies for 30-day retention ranking experiments, PROXIMA can flag segments (new vs power users, iOS vs Android) where the proxy would recommend the wrong launch decision.
**Dating applicability:** Audits proxy–outcome agreement in simulated/historical experiments only — does not train rankers, assign item credit, or model reciprocal congestion.

---

# Paper Reader

## 1. Problem & Motivation

Online A/B tests rely on fast proxy metrics instead of slow long-term OECs (retention, LTV). Aggregate proxy–outcome correlation can mask segment-level sign reversals (Simpson's Paradox), causing costly false launches. Existing surrogate-index methods predict long-term effects but do not audit segment-level fragility of a chosen proxy.

## 2. Method

**PROXIMA composite reliability score** (weights \(w_C + w_{DA} + w_{FR} = 1\)):
1. **Normalized effect correlation (C):** Correlation between proxy and long-term treatment effects across experiments.
2. **Directional accuracy (DA):** Fraction of experiments where proxy and long-term effects agree on sign.
3. **Segment-level fragility rate (FR):** Fraction of user segments where proxy effect sign contradicts global long-term direction.

**Fragility detection:** For each segment, compare proxy TE sign vs global long-term TE sign; aggregate fragility profile across experiments to flag risk zones.

**Decision simulation:** Compare proxy-based ship/no-ship decisions to oracle with perfect long-term knowledge; report win rate, false positive/negative rates, decision regret.

**Scope:** Proxy-agnostic — evaluates any candidate proxy (hand-picked, portfolio-optimized, or surrogate-index-derived).

## 3. Evaluation

- **Datasets:** Criteo Uplift (14M observations, advertising); KuaiRec (7K users, video recommendation).
- **Design:** 80 simulated A/B tests per domain.
- **Baselines:** Correlation-only scoring; surrogate-index literature (conceptual comparison).

## 4. Key Results

| Domain | Composite Reliability R | Directional Accuracy | Fragility | Oracle Decision Agreement |
|--------|------------------------|---------------------|-----------|--------------------------|
| Criteo (advertising) | **0.80** [0.77, 0.83] | >96% | **13%** | **98.4%** average (across both) |
| KuaiRec (recommendation) | **0.62** [0.59, 0.66] | >96% | **68%** | **98.4%** average (across both) |

- Recommendation domains show **substantially higher segment heterogeneity** (68% vs 13% fragility) despite high directional accuracy.
- Sensitivity analysis: composite outperforms correlation alone for discriminating reliable vs unreliable proxies.
- KuaiRec: moderate fragility tolerable when aggregate direction is correct; one false positive in simulation set.

## 5. Limitations

- Simulation on public datasets, not live production experiment logs at scale.
- Requires segment-level treatment effects and observed long-term outcomes for validation (retrospective).
- Does not construct optimal proxies — diagnoses existing ones.
- 80 simulated tests per domain may not capture all production edge cases.
- No ranking model, reciprocity, or two-sided interference treatment.

## 6. Prior Work Cited

Athey et al. (2019) surrogate index; Zhang et al. (2023) Netflix 200-test evaluation; Hagar et al. (2023) optimal proxy construction; Kohavi et al. (2009, 2013) OCE practice; Deng et al. (2017) proxy metrics; Simpson's Paradox literature.

---

# Project Relevance

**High relevance for D3 (surrogates/evaluation) and Q6.** Complements Netflix surrogate-index work by adding segment-fragility auditing — directly useful when dating platforms gate ranking launches on 7–14 day proxies for 30-day retention. Does not address Q1–Q2 (ranking objective / credit assignment) or Q7 (two-sided markets).

| # | Field | Answer |
|---|-------|--------|
| 1 | Ranking objective | Not specified in source (proxy validation for experiment decisions). |
| 2 | Credit assignment | Not specified in source. |
| 3 | Labels / horizon | Compares short-term proxy TE to long-term OEC TE across simulated experiments. |
| 4 | Short/long fusion | Not applicable — evaluates proxy reliability, not model head fusion. |
| 5 | Prediction vs incrementality | Audits whether proxy-based launch decisions match oracle long-term decisions (policy-level, not CATE). |
| 6 | Offline / online eval | 80 simulated A/B tests on Criteo + KuaiRec; decision simulation vs oracle; no live deployment. |
| 7 | Reciprocity / fairness | Segment-level heterogeneity analysis; no two-sided market modeling. |
| 8 | CTR → long-term migration | Diagnostic gate for choosing/validating short-term proxies during staged migration to long-term objectives. |

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
| **Reader** | PDF/URL fallback — arxiv:2604.14352 (NLM RESOURCE_EXHAUSTED) |
| **Community Reaction** | No significant community discussion found. |
