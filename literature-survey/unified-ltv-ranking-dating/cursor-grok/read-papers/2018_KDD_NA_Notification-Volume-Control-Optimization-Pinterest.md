# Survey Card

| Field | Value |
|-------|-------|
| **Title** | Notification Volume Control and Optimization System at Pinterest |
| **Authors** | Bo Zhao, Koichiro Narita, Burkay Orten, John Egan |
| **Venue** | KDD 2018 |
| **Year** | 2018 |
| **Type** | Industry |
| **Survey Phase** | D4 — Label Design / Long-Term Objectives |
| **NLM Source ID** | 1c974611-15e5-462d-93e8-7e59a8b17982 |
| **PDF** | https://doi.org/10.1145/3219819.3219906 |
| **One-line summary** | Production system computing per-user weekly notification budgets via XGBoost models of DAU and unsubscribe risk, with decoupled volume control from CTR ranking. |
| **Core mechanism** | Unified MDP-style utility: \(p(a|u,k_u) = p(s_{unsub}) \cdot p(a_L) + (1-p(s_{unsub})) \cdot p(a|s_{sub})\); greedy budget allocation under global volume constraint. |

**Dating applicability:** Template for optimizing push/email frequency per user against long-term retention (DAU/WAU) rather than notification CTR — directly analogous to dating re-engagement notifications where over-messaging causes unsubscribes and churn.

---

# Paper Reader

## 1. Problem & Motivation

Increasing notification volume boosts short-term engagement but causes unsubscribes, spam filtering, and long-term trust loss. Prior systems (LinkedIn) used linear models, independent-send assumptions, and tightly coupled CTR models that made A/B testing new notification types impossible without volume confounds.

## 2. Method

**Architecture:** Decoupled weekly budget optimizer + separate daily CTR ranker + budget pacer.

**Three XGBoost sub-models:**
1. **Activity \(p(a|u, k_u, s_{sub})\):** DAU probability given weekly budget \(k_u\).
2. **Unsubscribe \(p(s_{unsub}|u, k_u)\):** Unsubscribe probability; trained on allocated budget (not actual sends) to avoid survivorship bias.
3. **Post-unsub activity \(p(a_L|u, s_{unsub})\):** Active days in 4th week after unsubscribe.

**Unified utility:**
\[p(a|u,k_u) = p(s_{unsub}|u,k_u) \cdot p(a_L|u,s_{unsub}) + (1-p(s_{unsub}|u,k_u)) \cdot p(a|u,k_u,s_{sub})\]

**Optimization:** Greedy budget allocation (Algorithm 1) + threshold grid search on Map-Reduce (Algorithm 2) to meet global average volume constraint \(K\).

**Training data:** Volume-randomized exploration group for unbiased labels. Three user segments: Email Only, Push Only, Email & Push.

## 3. Evaluation

- **Production:** Deployed mid-2017; 200M+ MAU.
- **Baselines:** Legacy Pinterest heuristic frequency rules; LinkedIn email volume optimization (Gupta et al. 2016/2017).
- **Online A/B:** Three segment-specific tests measuring volume, CTR, DAU, WAU.

## 4. Key Results

| Segment | Volume Δ | CTR Δ | DAU Δ |
|---------|----------|-------|-------|
| Email Only | **−24%** | **+31%** | +0% |
| Push Only | **−6%** | **+11%** | **+1%** |
| Email & Push | email −7%, push −4% | email +10%, push +21% | **+3%** |

Core users: reduced volume without DAU/WAU drop. Marginal users: increased volume with positive DAU/WAU lifts.

## 5. Limitations

- MDP simplified to one-week horizon with immediate rewards for subscribed users (no multi-week fatigue compounding).
- Must partition users by channel to avoid volume shifting from email-only to push users.
- Post-unsubscribe tracking fixed at 4-week stabilization window.
- Decoupled from item-level ranking — no slate/exposure credit assignment.

## 6. Prior Work Cited

Gupta et al. (2016, 2017) LinkedIn email volume; Agarwal et al. (2012) click shaping; Aberdeen et al. (2010) Gmail priority inbox; Chen & Guestrin (2016) XGBoost.

---

# Project Relevance

**High relevance for D4 (label design / long-term objectives).** Demonstrates how to define and optimize a long-term engagement label (DAU/WAU) with explicit negative-action cost (unsubscribe) at user level, decoupled from short-term CTR proxies. For dating: (1) per-user re-engagement notification budgets; (2) modeling unsubscribe/churn as first-class negative label; (3) separating volume control from match/content ranking for clean A/B tests. No reciprocity or two-sided market treatment.

| # | Field | Answer |
|---|-------|--------|
| 1 | Ranking objective | Long-term site engagement (DAU/WAU), not notification CTR. Extensible to revenue. |
| 2 | Credit assignment | User-level weekly budget \(k_u\); decoupled from item-level ranking. |
| 3 | Labels / horizon | Binary DAU per day; unsubscribe per week; post-unsub activity at week 4. One-week optimization horizon. |
| 4 | Short/long fusion | Fixed MDP fusion of activity + unsubscribe + long-term post-unsub heads. |
| 5 | Prediction vs incrementality | Models predict outcome probabilities; optimizer uses incremental utility \(p(a|u,k{+}1)-p(a|u,k)\). |
| 6 | Offline / online eval | Offline XGBoost accuracy vs logistic regression; online A/B on 3 segments. |
| 7 | Reciprocity / fairness | Not specified in source. |
| 8 | CTR → long-term migration | Decouples volume (long-term) from CTR ranker (short-term); explicit move away from CTR-only optimization. |

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
| **Reader** | NotebookLM Q1–Q3 (source 1c974611-15e5-462d-93e8-7e59a8b17982) |
| **Community Reaction** | No significant community discussion found. |
