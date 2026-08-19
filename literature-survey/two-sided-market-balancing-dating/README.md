# Literature Survey Topic — Two-Sided Market Balancing in Dating-App Recommendation

**Created:** 2026-08-16

**Canonical brief:** `knowledge_base/projects/attribution_based_retention/survey-4-brief-two-sided-market-balancing-dating.md` (Survey 4 of the Attribution-Based Retention project). This README distills that brief's Project Context; the brief itself remains the source of truth for full wording, seed references, and rules.

**Workspace prefix for this run:** `claude_opus`. Per the brief's "Shared resources" section, `README.md`, `requirements.md`, and `queue.md` at this topic root are shared across every model/tool that runs this survey — read them, don't recreate them, and extend `queue.md` additively in later runs. This run's own outputs (`read-papers/`, `literature-review.md`, `executive-summary.md`, `method-tracker.md`, working notes) belong under `./claude_opus/`, not the shared root.

## Why surveyed

The product is a two-sided dating market where a match requires a like from both sides. Desirability is heavily skewed: a small set of highly desirable users absorb most incoming likes and cannot reply to all of them, so their surplus likes are wasted. Most other users receive few likes and few matches, and churn. Senders lose trust in the product because their likes rarely become conversations. This survey was triggered by the finding that no prior KB content or survey covered reciprocal recommendation, ecosystem health, congestion, or exposure allocation (kb-retriever check, 2026-08-15) — the modeling gap is market balancing under capacity limits with feedback loops, not single-viewer engagement prediction.

## Audience

The recommendation team at the dating app. This survey plays a research-analyst role: it finds and organizes references, mechanisms, metrics, and design patterns for the team. It does not design the model or make the modeling decision itself.

## Project Context

**The problem.** Our product is a two-sided market: a match needs a like from both sides. Each impression spends two things — the viewer's attention, and the reply capacity of the person shown. Desirability is heavily skewed: a small set of highly desirable users absorbs most likes and cannot reply to all of them, so their surplus likes are wasted. Most other users get few matches and churn. Senders lose trust because their likes never become conversations.

**The target.** Because of this, the target is not click-through rate or conversion rate for a single viewer. The target is the health of the whole market: total matches, conversations, the spread of matches across users (not concentrated on a few), and retention on both sides.

**The framing.** We treat this as market balancing under capacity limits, with feedback loops — that is, exposure allocation under capacity limits, not single-viewer CTR/CVR prediction. We want modeling ideas from teams who solved similar problems, including outside dating (job marketplaces, other two-sided platforms).

**Four modeling layers** structure the search:
1. **Reciprocal scoring** — the like-back probability conditioned on the other side's capacity, not just relevance to the viewer.
2. **Capacity-aware exposure allocation** — per-user capacity limits, LiJAR-style application/like redistribution, assortment optimization, exposure-fairness re-ranking, pacing.
3. **Market-design levers** — like limits, curated batches, signaling, which side searches.
4. **Ecosystem metrics and experimentation under interference** — Gini of matches, share of users with one or more matches, wasted likes, two-sided retention, and A/B testing that accounts for marketplace interference.

**Relation to Survey 3.** Survey 3 (a separate, earlier survey in this project) owns the ranking *objective* — unified retention/revenue objective design for a single viewer. Survey 4 (this survey) owns the *market layer* on top of that objective: reciprocal scoring, capacity-aware allocation, market-design levers, ecosystem metrics, and two-sided experimentation. The CyberAgent RecSys 2023 and RecSys 2024 papers on their dating platform appear as seed references in both surveys' briefs. If both surveys' outputs are used together, do not double-count these two papers as independent evidence — they are one shared source viewed through two different lenses.

**Deliverable.** This survey should produce:
1. An executive summary, one page maximum, listing 5 to 8 design patterns, each with one sentence and its strongest source.
2. An annotated bibliography grouped by search direction. Each item: title, authors/organization, year, venue/type, link, tier tag; what they did (≤80 words); the mechanism relevant to two-sided balancing (≤50 words); metrics used and the reported effect; fit for a dating app (high/medium/low, one reason); confidence that the item is real and described correctly.
3. A design-pattern matrix — rows: reciprocal scoring, capacity-aware scoring, constrained re-ranking, market-design lever, ecosystem metrics, evaluation method; columns: sources; cells: one-line notes.
4. Gaps and open questions, with the next 5 searches suggested.
5. A read-first list ranking the 10 items with the highest expected value for the team's design work.
