---
title: Executive Summary — Unified Retention/Revenue Ranking Model for a Dating Recommender
summary: Decision-focused synthesis of 133 references. Three ranked candidate architectures, a staged migration path, label/horizon recommendations, an evaluation plan, and an explicit account of what the literature does not answer.
topics: [literature-survey, executive-summary, unified-model, LTV, retention, revenue, reciprocal-recommendation, migration-path]
status: active
updated: 2026-08-17
---

# Executive Summary — Unified Retention/Revenue Ranking Model for a Dating Recommender

**Corpus:** 133 references. **Run:** `claude_opus`. **Full review:** [`literature-review.md`](./literature-review.md).

---

## 1. The finding that should shape the decision

**Industry has solved fusion. Industry has not solved the objective.**

Every flagship production ranker whose objective this survey could read optimizes a **short-horizon**
target:

| System | Stated training objective | Long horizon? |
|---|---|---|
| Meta, *Scaling the Instagram Explore Recommendations System*, 2023 | Fixed-weight linear "value model" over short-term engagement events | **No** — no horizon or delay handling stated anywhere |
| Kuaishou, *OneRec-V2 Technical Report*, 2025 | Same-session duration-aware watch-time quantile | **No** — 7-day return is an evaluation metric only, per the authors' own Limitations |
| Meituan, *MTGR: Industrial-Scale Generative Recommendation Framework in Meituan*, 2025 | CTR / CTCVR | **No** |
| Zhang et al., *Multi-Task Fusion via Reinforcement Learning for Long-Term User Satisfaction in Recommender Systems*, KDD 2022 | Weighted session feedback, discount 0.95 | **No** — session-scoped, not calendar |

The single documented exception is Netflix, and **it reaches a long-term objective indirectly**:
*GenRec: An LLM-Backed Recommendation Ranker at Netflix*, 2026 states the target as "expected
long-term member utility — a proxy for member satisfaction and retention", then operationalizes it by
**reweighting short-term engagement labels** with reward scores. The long-horizon signal enters
through the weights, not the labels.

**Implication.** You are not adopting a proven production pattern. You are moving a research-stage
idea into production, and should budget and communicate accordingly.

---

## 2. The gap is one dimension wide, and the starting point is named

Three literatures each hold one piece. No paper holds all three — but the nearest miss is precise.

**Kawamura et al., *Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method*,
KDD 2024 (CRRS)** already does two of the three. It estimates the **causal effect of the
recommendation itself** using a potential-outcome framework with a **bilateral treatment** — modelling
*both sides'* exposure as the treatment.

| Requirement | Status in the literature |
|---|---|
| Reciprocity / bilateral treatment inside the ranker | **Solved** — CRRS |
| Incrementality as the estimand, not a debiased prediction | **Solved** — CRRS |
| Item-level credit assignment | **Partial** — assumptions fail (see §7) |
| **A 7–30 day retention or revenue outcome as the causal target** | **Not found in any of 133 papers** |

CRRS's estimand is the effect of an exposure on **immediate match probability**. The open work is
**replacing that outcome variable with a delayed retention or revenue outcome**. That is one
well-defined extension with a named starting point — not an open-ended programme.

---

## 3. Three candidate architectures, ranked

### Architecture A — Reward-weighted short-term labels *(recommended first step)*

Keep the existing CTR/CVR heads and training cadence. Train a separate reward model that scores each
observed event by its association with a long-horizon outcome. Use those scores as **per-example
weights** in the ranking loss.

- **Objective:** unchanged short-term likelihoods, reweighted.
- **Labels and horizons:** existing like / match / conversation labels; the reward model is fitted
  against 7-day and 28-day outcomes.
- **How it absorbs today's system:** the CTR/CVR heads are untouched. The uplift blend is *not*
  replaced yet — it continues in parallel.
- **Data needed:** what you already log, plus a historical join from events to 7/28-day outcomes.
- **Precedent:** *GenRec: An LLM-Backed Recommendation Ranker at Netflix*, 2026; *GenPage: Towards
  End-to-End Generative Homepage Construction at Netflix*, 2026.
- **Main risk:** **a weight is not an effect.** This improves what you optimize toward; it does not
  estimate the incremental effect of an exposure. It cannot resolve the success paradox on its own.

### Architecture B — Unified multi-task ranker with a long-horizon value head

Add a long-horizon head — retention probability and expected revenue — beside the existing event
heads, and learn the fusion rather than tuning it.

- **Objective:** multi-task, with a **ZILN** revenue head and a retention head, combined by a learned
  fusion policy.
- **Labels and horizons:** 7-day and 28-day retention; revenue over 2–4 weeks under a
  zero-inflated lognormal loss.
- **How it absorbs today's system:** existing heads become inputs to a learned fusion; the uplift
  blend is replaced by the fusion policy.
- **Precedent for each part:** fusion — Zhang et al., *Multi-Task Fusion via Reinforcement Learning
  for Long-Term User Satisfaction in Recommender Systems*, KDD 2022, and *xMTF: A Formula-Free Model
  for Reinforcement-Learning-Based Multi-Task Fusion in Recommender Systems*, 2025. Revenue loss —
  Wang, Liu and Miao, *A Deep Probabilistic Model for Customer Lifetime Value Prediction*, 2019.
  Cascade structure — Xi et al., *Modeling the Sequential Dependence among Audience Multi-step
  Conversions with Multi-task Learning in Targeted Display Advertising*, KDD 2021 (AITM), with the
  counterfactual correction of Wang et al., *ESCM2: Entire Space Counterfactual Multi-Task Model for
  Post-Click Conversion Rate Estimation*, SIGIR 2022.
- **Main risk:** **still prediction, not incrementality.** Also, no paper in this corpus demonstrates
  learned fusion over a multi-day outcome — the fusion precedents are all session-scoped.

### Architecture C — Bilateral causal ranker on a delayed outcome *(the destination)*

Extend CRRS's bilateral potential-outcome formulation so the outcome variable is a delayed retention
or revenue quantity rather than immediate match probability.

- **Objective:** estimated incremental effect of showing B to A on A's (and B's) retention/revenue.
- **How it absorbs today's system:** the uplift model is *absorbed into* the ranking objective rather
  than blended after the fact. This is the target design in the Project Context.
- **Precedent for each part:** bilateral treatment — CRRS, KDD 2024. Uplift ranking over a delayed
  monetary outcome — Tang et al., *Rankability-enhanced Revenue Uplift Modeling Framework for Online
  Marketing*, KDD 2024 (RERUM), which ranks by CATE on a 2-to-4-week revenue outcome **using a ZILN
  loss**. Making a delayed label trainable — the delayed-feedback family rooted in Chapelle,
  *Modeling Delayed Feedback in Display Advertising*, KDD 2014.
- **Main risk:** **no precedent for the combination.** RERUM ranks *customers to target with a
  coupon*, not *items to show in a slate* — the treatment differs. This is genuine research, and
  should be resourced as such.

**Ranking rationale:** A is cheap, reversible and ships value early. B is the natural consolidation.
C is where the Project Context's stated goal actually lives. Doing C without A and B first means
building a causal, reciprocal, long-horizon ranker with no intermediate validation.

---

## 4. Staged migration path, with what to measure at each stage

| Stage | Change | Measure | Gate to proceed |
|---|---|---|---|
| **0. Instrument** | Build the event → 7d/28d retention and revenue join. Nothing ships. | Coverage and latency of the join; base rates per segment | Labels reproducible and stable |
| **1. Validate a surrogate** | Fit and validate a short-horizon surrogate for your 7–30 day outcomes | Agreement between surrogate and full-horizon reads on **past** experiments | Precision/recall measured, not assumed (see §6) |
| **2. Architecture A** | Reward-weighted labels in the existing ranker | Retention and revenue at 7/28 days; watch for match-quality regression | No degradation on match quality |
| **3. Add heads** | Add ZILN revenue and retention heads; keep the uplift blend | Head calibration; incremental value over Stage 2 | Heads calibrated on held-out horizons |
| **4. Architecture B** | Replace the hand-tuned blend with learned fusion | Online A/B under a two-sided design | Fusion beats the blend on a long-horizon metric |
| **5. Architecture C** | Move incrementality inside the objective | Incremental retention/revenue per exposure | — |

**Do not skip Stage 1.** Every later stage depends on being able to read a long-horizon result faster
than the horizon, and on knowing how lossy that read is.

---

## 5. Label and horizon recommendations, with evidence

- **Retention: use both 7-day and 28-day.** 28-day has the strongest industrial precedent — Pancha et
  al., *PinnerFormer: Sequence Modeling for User Representation at Pinterest*, KDD 2022 uses a 28-day
  dense all-action label. A 1-day/7-day pair is used in Pinterest's *Save, Revisit, Retain: A Scalable
  Framework for Enhancing User Retention*. A 10-day geometric cap appears in Zhao et al., *KuaiSim: A
  Comprehensive Simulator for Recommender Systems*, NeurIPS 2023.
- **Revenue: model it with a zero-inflated lognormal (ZILN) loss over a 2-to-4 week window.** Most
  users never subscribe and a few spend heavily — exactly the distribution ZILN targets (Wang, Liu and
  Miao, 2019). RERUM (KDD 2024) demonstrates ZILN inside a *ranking* objective at a 2-to-4 week
  horizon, which is the closest precedent to your need.
- **Treat "not yet converted" as censored, never as negative.** This is the founding insight of
  Chapelle, *Modeling Delayed Feedback in Display Advertising*, KDD 2014 and of Elkan and Noto,
  *Learning Classifiers from Only Positive and Unlabeled Data*, KDD 2008. A user who has not returned
  yet is not a user who will not return.
- **Model multiple valued events from one exposure**, rather than a single binary outcome — see
  *Handling Many Conversions per Click in Modeling Delayed Feedback*, Google 2021, and the negative
  binomial formulation in *Delayed Feedback Model with Negative Binomial Regression for Multiple
  Conversions*, AdKDD 2020. Your cascade produces a like, a match, a conversation and possibly a
  subscription from one impression.
- **Model negative milestones, not only positive ones.** Tan et al., *Optimizing Airbnb Search Journey
  with Multi-task Learning*, KDD 2023 devotes three of ten task heads to negative outcomes through
  uncancelled booking. This is the most direct published handle on your success paradox.

**A caution on the scale mismatch.** The delayed-feedback literature operates at **hours to days**.
Your horizons are **weeks**. The framing transfers; the exponential-delay assumptions and calibration
timescales are not validated at your scale by any paper in this corpus.

---

## 6. Evaluation plan

**Offline.** Validate a surrogate before relying on it. Athey, Chetty, Imbens and Kang, *The Surrogate
Index: Combining Short-Term Proxies to Estimate Long-Term Treatment Effects More Rapidly and
Precisely*, 2019 is the foundation. Tripuraneni et al., *Choosing a Proxy Metric from Past
Experiments*, KDD 2024 gives a selection procedure.

**Know the cost before you rely on it.** *Evaluating the Surrogate Index as a Decision-Making Tool
Using 200 A/B Tests at Netflix*, 2023 compared a 14-day surrogate against 63-day direct measurement
across 200 tests and 1,098 arms:

- **~95% overall agreement** — but this is the misleading number.
- On launch decisions: **79% precision, 65% recall.**
- **Zero** false launches on tests that were significantly negative at 63 days.

**The surrogate is safe but lossy.** It will not ship harm; it will quietly discard roughly a third of
genuine wins. Netflix estimates ~53% more experiments are needed to compensate — presented there as
illustrative, resting on untested assumptions, and it should be cited that way.

**Check segment fragility.** *PROXIMA: Proxy Metric Validation with Segment-Level Fragility Detection
for Online Controlled Experiments* detects proxies that hold in aggregate and fail for a segment.
Dating revenue behaviour differs sharply between never-paying users, one-off purchasers and
subscribers — a proxy validated on the whole population can be badly wrong for the segment that
generates the revenue.

**Online, under two-sided interference.** Treating one viewer changes what other viewers see. See
Nandy et al., *A/B Testing for Recommender Systems in a Two-sided Marketplace*, NeurIPS 2021 and
*Interference, Bias, and Variance in Two-Sided Marketplace Experimentation: Guidance for Platforms*,
WWW 2022.

**The failure mode most likely to be found late: interference through the training data.** When a
treatment changes what the model learns from, the control group is contaminated through the shared
model. A unified retention model retrained on logged data inherits the treatment's effects. See
*Seller-Side Experiments under Interference Induced by Feedback Loops in Two-Sided Platforms*, 2024
and *Tackling Interference Induced by Data Training Loops in A/B Tests: A Weighted Training Approach*,
2023.

### ⚠ Evidence-quality rule

**Several retention-RL results in this corpus are simulator results, not online results**, and the
simulator generates retention circularly. In Zhao et al., *KuaiSim*, NeurIPS 2023, retention is a draw
from `Geometric(p_ret)` where `p_ret` rises with the immediate reward the policy optimizes — so a
policy that raises immediate reward **mechanically** raises its own simulated retention.

That builds in "immediate engagement causes retention", which is precisely what your success paradox
questions. **Label every cited result as online-A/B or simulator, and never compare the two.** Cai et
al., *Reinforcing User Retention in a Billion Scale Short Video Recommender System*, WWW 2023 carries
a genuine billion-user online result and is unaffected.

---

## 7. Most fundamental methods

From the finalized [`method-tracker.md`](./method-tracker.md) over 133 cards. **Counts are biased by
corpus composition** — the delayed-feedback direction holds 18 cards and cites its own lineage
densely — so treat cross-direction comparisons as unreliable.

1. **DFM** — Chapelle, *Modeling Delayed Feedback in Display Advertising*, KDD 2014 (composite 85).
   Root of the entire delayed-feedback literature; ten-plus descendants here. Assumes exponential
   delay at an advertising timescale.
2. **IPS and doubly-robust descendants** (composite 59). The shared correction machinery across
   uplift, off-policy evaluation and entire-space debiasing. **Note whether each use debiases a
   prediction or estimates an effect** — they are not the same.
3. **ESMM** — Ma et al., *Entire Space Multi-Task Model: An Effective Approach for Estimating
   Post-Click Conversion Rate*, SIGIR 2018 (composite 54). The structural transfer for your cascade,
   **but provably biased** — adopt ESCM2 instead.
4. **MMoE** — Ma et al., *Modeling Task Relationships in Multi-task Learning with Multi-gate
   Mixture-of-Experts*, KDD 2018 (composite 53). The multi-task backbone under most fusion work here.
5. **ZILN** — Wang, Liu and Miao, *A Deep Probabilistic Model for Customer Lifetime Value
   Prediction*, 2019 (composite 37). **The most transferable single component in the corpus.** Cited
   by six other papers, and the only component appearing in three roles — as an LTV loss, inside a
   Pareto multi-objective model, and **inside RERUM's uplift ranking objective**.

---

## 8. Open questions, gaps, and what the literature does not answer

1. **No published item-level credit assignment for a reciprocal, long-horizon outcome.** SlateQ's
   assumptions fail here: *Single Choice* (viewers like several candidates per session) and
   *Reward/Transition Dependence on Selection* (a match needs the other side to act — an external,
   delayed decision outside its single-agent MDP). *Future Impact Decomposition in Request-level
   Recommendations*, KDD 2024 is assumption-lighter but splits a **value estimate**, not a causal
   effect. Its useful negative result: decomposing the **critic's** TD-target to item level **failed**
   — the critic must stay at list level.
2. **Congestion control needs an architectural layer you do not have.** ECDA's exposure quota is
   defined on expected likes or dates per receiver and requires coordination **across viewers**. A
   per-request ranker cannot express it. This is an architecture decision, not a modelling detail.
3. **The dating industry publishes essentially nothing.** Match Group, Bumble, Coffee Meets Bagel,
   Tantan and Soul returned null results. Only Tinder's 2019 pressroom post and a Momo InfoQ article
   exist — and **Grindr publicly states it runs no recommendation algorithm at all**. Evidence must
   transfer from LinkedIn Jobs, Airbnb and online recruitment.
4. **Reciprocal work has no calendar-time objective**, in three distinct forms: static snapshots (the
   majority), one 2-week calendar window (ECDA), and one round-count horizon (*Online Reciprocal
   Recommendation with Theoretical Performance Guarantees*, NeurIPS 2018). Note that a **real-time
   architecture is not a long horizon** — CUPID is session-based and real-time, but its label is the
   chat duration of the current call.
5. **Two references that could change these conclusions were not retrieved.** *Reward Innovation for
   Long-Term Member Satisfaction* (Netflix, RecSys 2023) is the keystone of the Architecture A pattern
   and is blocked at ACM DL with no fetchable mirror. **If you have ACM access, read it first.**
   *Learning Robust, Long-run Surrogate Metrics with Modeling and Instrumental Variables* (Meta, KDD
   2026) is likewise confirmed but unreachable.
6. **Two harvest candidates remain unread and bear directly on the central finding:** *User Retention:
   A Causal Approach with Triple Task Modeling* (IJCAI 2021) — causal reasoning applied to retention,
   the exact dimension CRRS lacks — and *Surrogate for Long-Term User Experience in Recommender
   Systems* (Google, KDD 2022).
7. **Your revenue mix has no precedent in this literature.** The Project Context describes revenue
   from **subscriptions and a la carte purchases** — boosts, super likes, "see who likes you". **No
   paper among the 133 models a mixed revenue stream of that kind.** ZILN handles a zero-inflated,
   heavy-tailed *single* monetary outcome, and the lifetime-value literature assumes one revenue
   process throughout.

   Treating a recurring subscription and impulse micro-purchases as one quantity assumes they share a
   distribution and respond to the same ranking signals. That is plausible and entirely unevidenced
   here. A subscription is a considered, infrequent decision; a boost purchase is impulsive and
   repeatable. If they diverge, a single revenue head will average two different behaviours and may
   optimize for neither.

   **Recommendation:** model them as **two heads**, at least until you have measured whether they move
   together. This is the one design question in this summary where the survey offers no evidence
   either way, and where the cost of guessing wrong is a revenue objective that silently mis-weights
   your highest-value users.

---

## 9. Top-10 reading order

1. Kawamura et al., *Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method*, KDD 2024 — the nearest miss; your starting point.
2. Tang et al., *Rankability-enhanced Revenue Uplift Modeling Framework for Online Marketing*, KDD 2024 — uplift ranking over delayed revenue with ZILN.
3. *GenRec: An LLM-Backed Recommendation Ranker at Netflix*, 2026 — the reward-weighting pattern; Architecture A.
4. Zhang et al., *Multi-Task Fusion via Reinforcement Learning for Long-Term User Satisfaction in Recommender Systems*, KDD 2022 — learned fusion, and its session-horizon limit.
5. Wang, Liu and Miao, *A Deep Probabilistic Model for Customer Lifetime Value Prediction*, 2019 — the revenue loss to adopt.
6. *Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix*, 2023 — what surrogates actually cost you.
7. *Future Impact Decomposition in Request-level Recommendations*, KDD 2024 — credit assignment, including what failed.
8. Tan et al., *Optimizing Airbnb Search Journey with Multi-task Learning*, KDD 2023 — two-sided funnel with negative milestones.
9. Wang et al., *ESCM2: Entire Space Counterfactual Multi-Task Model for Post-Click Conversion Rate Estimation*, SIGIR 2022 — the cascade variant to use.
10. Nandy et al., *A/B Testing for Recommender Systems in a Two-sided Marketplace*, NeurIPS 2021 — how to measure any of it.

**And if you can access it:** *Reward Innovation for Long-Term Member Satisfaction* (Netflix, RecSys
2023), which this survey could not retrieve.
