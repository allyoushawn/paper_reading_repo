# Paper Analysis: Your Looks and Your Inbox

**Source:** OkTrends (official OkCupid blog), Christian Rudder, November 17, 2009 (mirror)
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** Your Looks and Your Inbox
**Authors:** Christian Rudder (OkCupid co-founder, OkTrends)
**Abstract:**
An empirical data-journalism post analyzing OkCupid's logged interaction data (3.5M active members, hundreds of millions of interactions) to quantify how physical attractiveness ratings relate to inbound message volume and reply rates, revealing strongly divergent rating and messaging behavior between men and women.

**Key contributions:**
- Quantifies the "attractiveness premium" in inbox volume: most-attractive men get 11x the messages of the lowest-rated men (medium-rated ~4x); most-attractive women get ~5x a typical woman's volume and 28x the lowest-rated women's volume.
- Shows men's rating curve for women is symmetric/charitable, but their messaging is highly consolidated: two-thirds of male messages go to the top third of women by rating.
- Shows women rate 80% of men as "worse-looking than medium" (highly skewed/critical), yet message more proportionally to that (harsh) curve rather than chasing only top-rated men.
- Notes attractive users reply less often because their inboxes are flooded, and documents an anomaly where top-rated men messaging low-rated women see unusually low reply rates ("self-confidence"/trust-barrier effect, controlled for spam).

**Methodology:**
Purely observational/empirical: plots unnormalized 0–5 star attractiveness rating distributions per gender, superimposes actual outbound message volume by recipient attractiveness group, and cross-tabulates sender-attractiveness x recipient-attractiveness against reply rate.

**Main results:** See Bibliography Fields below for the exact multiples; core finding is a strongly right-skewed, superstar-dominated distribution of inbound messages concentrated on a small top tier of rated users, with reply capacity inversely related to inbound volume (flooded inboxes reply less).

---

## 2. Experiment Critique

**Design:** Observational analysis of real production logs (not a controlled experiment); no held-out validation, no formal significance testing reported, though the sample size (hundreds of millions of interactions, 3.5M members) is very large.

**Statistical validity:** No confidence intervals or formal hypothesis tests reported; multiples (11x, 28x, 4x, 5x) are presented as descriptive ratios from binned "attractiveness groups," not model-fitted estimates.

**Online experiments (if any):** None — purely descriptive/observational, not an A/B test.

**Reproducibility:** Not reproducible outside OkCupid — proprietary interaction and rating logs, no data release, no code.

**Overall:** As a data-journalism piece rather than a peer-reviewed study, the analysis is transparent about caveats (attractiveness is subjective, data deliberately left unnormalized) and the author explicitly flags several unaddressed confounds (height, presentation quality, racial/body-type diversity) — some via later reader comments cited in the same source.

---

## 3. Industry Contribution

**Deployability:** N/A — this is a retrospective data analysis, not a proposed system or algorithm.

**Problems solved:** Provides an early, concrete empirical baseline for the exact phenomenon the project's "north star" describes: desirability skew causing a small top tier to absorb a disproportionate share of attention/messages while most users get comparatively little.

**Engineering cost:** N/A.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Positions itself as the first rigorous, large-N quantification (at the time, 2009) of exactly how much physical attractiveness drives online-dating message volume, distinct from folk wisdom ("beautiful people are more successful daters").

**Prior work comparison:** No academic citations; the (mirrored/annotated) source includes editorial footnotes pointing to later related industry analyses — a Hinge Q&A on "biggest challenge men face on dating apps" (2017) and a Tinder-focused quantitative study (Neyt et al. 2019, Mixmosa) — but these are editor additions, not citations by the original 2009 author.

**Verification:** N/A — descriptive statistics, not a novelty claim to verify against literature.

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| OkCupid interaction/rating logs (3.5M active members, hundreds of millions of interactions) | None | Not accessible | Proprietary; no public release |

**Offline experiment reproducibility:** Not reproducible — no public dataset or code.

---

## 6. Community Reaction

Not searched — out of scope for this literature-survey batch run (Phase 3 focuses on NotebookLM-grounded extraction, not web community-reaction search). Note: the source itself records substantial reader engagement (471 comments per the mirrored page footer), including reader-raised critiques (height not controlled for, presentation-quality confound, lack of racial/body-type diversity in the discussion).

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Christian Rudder
**Affiliations:** OkCupid (Humor Rainbow, Inc.)
**Venue:** OkTrends (company data-blog post)
**Year:** 2009
**PDF:** N/A — web page (mirror), ingested directly as a NotebookLM source
**Relevance:** Core
**Priority:** 1

---

## Bibliography Fields

- **title:** Your Looks and Your Inbox
- **authors or organization:** Christian Rudder / OkCupid (OkTrends)
- **year:** 2009
- **venue or type:** Company data-blog post (mirror)
- **link:** OkTrends — "Your Looks and Your Inbox" (Nov 17, 2009 mirror)
- **tier tag:** Tier 1 — Dating-platform primary source

**what they did (≤80 words):** Analyzed OkCupid's logged ratings and messages (3.5M members) to quantify how attractiveness ratings drive inbox volume. Found men's messages concentrate heavily on top-rated women (2/3 of messages to top 1/3 of women; up to 28x volume skew) despite a charitable/symmetric rating curve, while women rate men harshly (80% "below medium") but message more proportionally. Highly-messaged users reply less often, since their inboxes are flooded.

**mechanism relevant to two-sided balancing (≤50 words):** No mechanism proposed — this is pure measurement, not an intervention. But it is direct empirical evidence for the project's core premise: desirability skew (up to 28x inbox-volume multiple) concentrates likes/messages on a small top tier who cannot reply to all, echoing "wasted likes" and reply-capacity exhaustion.

**metrics used, and the reported effect:** Message-volume multiples by attractiveness group: men 11x (top) vs 4x (medium) relative to lowest-rated; women ~5x (top vs. typical), 28x (top vs. lowest-rated). Two-thirds of male messages go to top third of women. Reply rate inversely related to inbound message volume for highly-rated users.

**fit for a dating app:** high — it is a real dating platform's own empirical evidence of the exact desirability-skew/wasted-outreach dynamic the project targets, even though it offers no algorithmic fix.

**confidence that the item is real and described correctly:** high — all three queries returned grounded answers with `sources_used` matching this source_id; the widely-known OkTrends "Your Looks and Your Inbox" (2009) post and its statistics are consistently reproduced across both queries.

---

## Project Relevance

This is one of the strongest empirical-evidence sources in the batch for the project's problem statement, though it contains **no mechanism** — it is measurement only, not a proposed fix. It directly and quantitatively documents the "desirability is heavily skewed" premise: a small top tier of rated users (particularly women) absorbs a highly disproportionate share of inbound messages (up to 28x the lowest-rated tier), and NotebookLM confirms these highly-messaged users reply less often because their inboxes are flooded — the exact "reply capacity gets exhausted, surplus likes are wasted" dynamic in the project's framing. Per the source, the only proposed response to this inequality is individual-level advice (help "non-models" present themselves better) — NotebookLM explicitly confirms the post "does not discuss any platform-level algorithms or market-design levers (such as capacity-aware exposure throttling, message caps, or search cooling factors) to spread messages more evenly." No ecosystem-health metric (match Gini, share of users with ≥1 match) is computed, though the raw multiples reported here (2/3 of messages to top 1/3, 28x skew) are exactly the kind of raw statistic a match-Gini or wasted-likes metric in this project would formalize. Best used as motivating evidence/baseline severity numbers for the project's problem statement, not as a source of mechanism.
