# Literature Survey Topic — Unified Retention/Revenue Ranking Model for a Dating Recommender

**Created:** 2026-08-16

**Source brief:** `knowledge_base/projects/attribution_based_retention/survey-3-brief-unified-ltv-ranking-dating.md`

---

## Shared-folder convention (read this first)

This folder is shared across several models running the same brief.

- **Shared at this root:** `README.md`, `requirements.md`, `queue.md`, `notebooklm-state.md`, `log.md`.
- **Per-model workplaces:** each model writes into its own subfolder — `claude_opus/`, `gemini/`, `chatgpt/`, `codex/`, and so on.
- Each workplace holds `read-papers/`, `literature-review.md`, `executive-summary.md`, `method-tracker.md`, and that model's working notes.
- Do not read or overwrite another model's workplace.
- Extend `queue.md` additively. Append new rows. Never delete or overwrite existing rows.

**NotebookLM notebook:** `unified-ltv-ranking-dating`, ID `67046a44-7490-4fe5-b54a-3f39ef37fdd3`.
Never call `notebook_create` for this topic. Call `notebook_get` or `notebook_query` against that ID.

---

## Why surveyed

The team ranks candidate profiles on a dating app. The current design has two parts.

1. A CTR/CVR-style model predicts short-term events: A likes B, A and B match, A and B converse.
2. An uplift model estimates the extra retention and revenue that a like, a match, or a conversation causes.

The team blends the two scores after the fact. The target design replaces that blend with **one unified
ranking model** whose training objective is retention and revenue directly.

This survey supports that migration decision. Surveys 1 and 2 in this knowledge base left three areas
uncovered: reinforcement learning for retention, long-term-value ranking objectives, and surrogate
metrics. This survey covers them.

## Audience

The machine learning team that builds the dating-app recommender, and the decision-makers who approve
the migration. The reader wants a ranked set of candidate architectures and a staged migration path,
not an academic overview.

## Project Context

### The system today

- The team ranks candidate profiles (user B) for a viewer (user A).
- A CTR/CVR-style model predicts short-term events: like, match, conversation.
- An uplift model estimates the extra retention and revenue caused by a like, a match, or a conversation.
- The team blends those scores after the fact.

### The target system

One unified model predicts the retention and revenue that follow when the system shows B to A.
Retention and revenue become the training objective. The blend disappears.

### Product constraints — each one shapes what counts as relevant

- **Reciprocity:** a match needs a like from both sides.
- **Congestion:** B's attention and likes are a shared, limited resource across many viewers.
- **Cascade:** impression → like → match → conversation → date or subscription.
- **Low base rates:** matches and conversations are rare per impression.
- **Delayed labels:** retention runs 7 to 30 days. Subscription revenue runs over weeks.
- **Revenue mix:** subscriptions plus a la carte features (boosts, super likes, "see who likes you").
- **Success paradox:** a good match can end the user's tenure. Retention and revenue can conflict with
  match quality.
- **Prediction vs. incrementality:** retention conditional on exposure is not the effect of the
  exposure. Active users retain regardless. Track this distinction for every reference.

### What "relevant" means here

A reference is relevant when it helps answer one of the eight research questions below with evidence
from a real system. Industry practice is the target. Academic work supports it.

A reference is **low relevance** when it optimizes a short-term proxy only, and says nothing about a
long-horizon objective, delayed labels, credit assignment, or a two-sided market.

### Research questions the survey must answer

- **Q1.** How do industry recommenders make retention, LTV, or revenue the training objective of the
  ranking model instead of CTR-like proxies?
- **Q2.** How do they attribute a user-level, delayed outcome to an item-level decision (one exposure
  or one slate)?
- **Q3.** Which label and horizon definitions do they use for retention and revenue? How do they
  handle delay, sparsity, and censoring?
- **Q4.** How do they combine short-term event heads with long-term heads: fixed fusion, learned
  fusion, or one value head?
- **Q5.** Where do uplift or incremental effects sit inside the ranking model itself, and what did that
  change?
- **Q6.** How do they evaluate such a model offline and online, given slow, noisy retention effects and
  two-sided interference?
- **Q7.** What is specific to two-sided or reciprocal markets: reciprocity, congestion, fairness across
  sides, revenue vs. match trade-off?
- **Q8.** Which migration paths from "CTR model + uplift blend" to a unified model are documented
  (auxiliary heads first, distillation, reward models, staged rollout)?

### Excluded areas — prior surveys already cover these

Do not re-survey these. Cite work from them only when a reference uses it **inside a ranking model**.

- Multi-touch attribution (Shapley, Markov, deep MTA).
- CATE and uplift meta-learners (X-learner, DML, DragonNet, causal forest).
- Survival and churn basics (Cox-Time, DeepHit).
- Geo and switchback experiments.
- Proxy-label and noisy-label learning.

### Per-reference card — every paper file must record these

- Title, authors or company, venue, year, URL.
- Source type: blog / industry paper / academic.
- Direction: D1 to D9 (see `requirements.md`).
- Problem setting.
- Objective and label definition, with horizon and delay handling.
- **Prediction or incrementality:** does the model predict the outcome, or the effect of the exposure?
- Model architecture.
- **Credit assignment:** how a user-level outcome maps to an item-level decision.
- Training data and counterfactual handling.
- Offline and online evaluation.
- Reported gains.
- Applicability note for a two-sided dating recommender (2 lines).
- Unverified claims, marked as such.

### Synthesis deliverables the executive summary must produce

1. A comparison table of all references, one row each, with the card columns.
2. A taxonomy of unified long-term-value ranking approaches, with the industry adopters of each.
3. Three candidate architectures for this case, ranked. For each: objective, labels and horizons, how
   it absorbs the current CTR/CVR heads and the uplift blend, data needed, main risk.
4. A staged migration path from the current CTR/CVR + uplift blend to the unified model, with what to
   measure at each stage.
5. Label and horizon recommendations for retention and revenue in a dating app, with evidence.
6. An evaluation plan: offline metrics, surrogate validation, online design under two-sided
   interference.
7. Open questions, gaps, and a top-10 reading order.

### Verification rules

- Every reference needs a working URL.
- Do not invent titles, venues, or results.
- Separate what a source states from what the survey infers.
- Mark each seed reference as `confirmed` or `not found` in the log.
