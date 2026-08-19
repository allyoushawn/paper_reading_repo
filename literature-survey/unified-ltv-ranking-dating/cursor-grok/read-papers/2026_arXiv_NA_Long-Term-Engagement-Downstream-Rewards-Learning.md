# Survey Card

| Field | Value |
|-------|-------|
| **Title** | Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning |
| **Authors** | Dingsu Wang, Filip Ryzner, Kelly He, Armando Ordorica, et al. (Pinterest) |
| **Venue** | arXiv (Pinterest) |
| **Year** | 2026 |
| **Type** | Industry |
| **Survey Phase** | D1 — Long-Term Ranking Objectives |
| **NLM Source ID** | 2856572a-f50a-4c07-8485-d9b948ea9547 |
| **PDF** | https://arxiv.org/pdf/2607.14192.pdf |
| **One-line summary** | Model-agnostic framework that screens session-level behaviors predictive of retention, derives downstream reward heads (deep sessions, negative shallow engagement, use-case adoption), and adds them to existing rankers across Pinterest surfaces. |
| **Core mechanism** | Offline screening ranks early observable session behaviors by retention correlation → engineered DR labels (P2P rabbit-hole depth, negative closeup, interest signals) → additional ranking heads with tuned utility weights; deployable on any SL/RL recommender without surface-specific reward engineering. |

**Dating applicability:** Practical migration path: keep current Pinnability-style ranker and add retention-correlated proxy heads (e.g., deep conversation threads, negative shallow swipes) before attempting a full unified LTV model.
**Dating applicability:** Session-level proxy rewards, not item-attributed 30-day retention; no reciprocity/congestion; cross-surface cannibalization observed when thresholds are not segment-tuned.

---

# Paper Reader

## 1. Problem & Motivation

Recommender systems optimized for immediate engagement can hurt long-term value via feedback loops. Direct retention optimization is hard: labels are sparse, delayed, and weakly attributable to individual recommendations. RL approaches require heavy reward engineering and do not generalize across surfaces (Homefeed, Search, Notifications).

## 2. Method

**Problem formulation:** Define ideal retention objective over user return days; derive proxy objectives from session-level downstream behaviors observable earlier and at higher volume.

**Offline screening framework:** Rank candidate session behaviors by correlation with long-term retention; select a smaller set for online experimentation.

**Downstream reward families:**
1. **Deeper session rewards** — downloads, screenshots, saves leading to deeper engagement chains.
2. **Negative rewards** — penalize shallow closeups (duration thresholds) to reduce low-quality engagement.
3. **Use-case adoption rewards** — transitions into high-value product flows (e.g., P2P rabbit hole).

**Productionization:** Reward label generation infrastructure from multi-level engagement sequences; heads added to Pinnability ranking model with HyperOPT utility weight tuning; incremental training cost within **5%** of baseline; label latency reduced from ~3 weeks to ~2 days.

## 3. Evaluation

- **Data:** Pinterest industrial engagement (billions of user activities); no public benchmark evaluation.
- **Online:** A/B tests on Homefeed (1.5% traffic, 3–4 weeks), Related Pins, Search, Notifications.
- **Metrics:** Successful Sessions (SS), Total Time Spent, WAU, DAU, hide/report rates, cross-surface engagement.

## 4. Key Results

**Homefeed — deeper session rewards (Table 3, statistically significant relative lifts):**

| Reward | SS (Core) | SS (Non-core) | Total Time (Core) | Total Time (Non-core) |
|--------|-----------|---------------|-------------------|----------------------|
| Deeper sessions | **+0.24%** | **+0.48%** | **+0.09%** | **+0.10%** |
| Negative rewards (tuned) | **+0.16%** | **+0.16%** | **+0.46%** | **+0.24%** |
| Use-case adoption | **+0.10%** | **+0.10%** | **+0.16%** | **+0.11%** |

**Deeper session A/B (downloads/screenshots heads):** SS **+0.36%** site-wide; total time **+0.10%**; screenshots **+0.7%**; downloads **+0.7%**; WAU **+0.1%**.

**Negative rewards (segment-tuned thresholds, month-long):** SS **+0.16%**; unsuccessful sessions **−0.40%**; total time **+0.35%**; positive DAU/WAU for core and non-core (vs negative trends with uniform threshold).

## 5. Limitations

- Proxy rewards are session-level, not item-level credit for delayed retention.
- Initial uniform negative-reward threshold hurt non-core users and caused cross-surface cannibalization until segment tuning.
- No public dataset evaluation; Pinterest-specific action taxonomy.
- Does not model incrementality (conditional retention vs effect of exposure).
- No reciprocity or two-sided market treatment.

## 6. Prior Work Cited

Impatient Bandit (KDD 2023); RLUR; Pinnability; feedback-loop / homogenization literature; sequential RL for recommendations.

---

# Project Relevance

**High relevance for D1 and Q8 (staged migration).** Documents a production path from short-term ranker to retention-aligned objectives via additive proxy heads — lower risk than full objective replacement. Addresses Q3 (early observable proxies vs sparse delayed retention) and Q6 (online A/B on retention-correlated metrics). Weak on Q2 (item credit), Q5 (incrementality), Q7 (two-sided).

| # | Field | Answer |
|---|-------|--------|
| 1 | Ranking objective | Retention-aligned via downstream proxy rewards added to existing ranker; short-term engagement heads retained. |
| 2 | Credit assignment | Session-level downstream behaviors; not attribution of user-level 30-day retention to one profile impression. |
| 3 | Labels / horizon | DR labels from session actions observable in hours/days; retention ground truth for offline screening; ~3-week → ~2-day label latency in production. |
| 4 | Short/long fusion | Additional reward heads with tuned utility weights in multi-objective ranker (not single unified LTV head). |
| 5 | Prediction vs incrementality | Predicts probability of downstream session behaviors correlated with retention; not causal effect of showing item B. |
| 6 | Offline / online eval | Offline screening on billions of events; online A/B on Homefeed/Search/Notifications with SS, WAU, time-spent metrics. |
| 7 | Reciprocity / fairness | Not specified in source; segment tuning (core vs non-core) for negative rewards. |
| 8 | CTR → long-term migration | Add DR heads to existing Pinnability model with HyperOPT weight search before full objective unification. |

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
| **Reader** | PDF/URL fallback — arxiv:2607.14192 (NLM RESOURCE_EXHAUSTED) |
| **Community Reaction** | No significant community discussion found. |
