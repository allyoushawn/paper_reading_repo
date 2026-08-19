# Paper Analysis: Building a Transformer-Based Category Recommender at Thumbtack

**Source:** Andrew Morss (Senior Applied Scientist, Thumbtack), Thumbtack Engineering blog on Medium (published Jul 20, 2026), NotebookLM source_id `b1a14644-792a-4f6a-b8e8-d0db6e825fc6`
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** A look at compensating for position bias in recommender systems using negative sampling strategies (published as "Building a Transformer-Based Category Recommender at Thumbtack")
**Authors:** Andrew Morss, Senior Applied Scientist, Thumbtack
**Abstract:**
Describes Thumbtack's transformer-based recommender that chooses which of ~500 home-service job categories to surface to a user in marketing notifications, and how the team fixed severe popularity bias (naive training essentially ignored the long tail of categories) using an "adaptive mixed sampling" negative-sampling strategy.

**Key contributions:**
- A multi-token Transformer that embeds a user's search history and contextual features (location, climate, home attributes) as tokens, and a candidate category as a query, scoring via cross-attention — with individual input tokens maskable at run time so one model serves multiple marketing-campaign types (e.g., "based on recent activity" vs. "homeowners near you").
- **Adaptive mixed sampling**: for each training batch, builds a candidate pool of positive target + in-batch negatives + random negatives, scores them all in one pass, then keeps only the top-K hardest negatives for the cross-entropy loss — combining and improving on plain random and in-batch negative sampling.
- A **Balance Score** (1 − Gini coefficient across head/mid/tail hit-rate cohorts) used alongside HR@10 as a single-number summary of how evenly the recommender performs across a popularity-skewed catalog.

**Methodology:**
Search-history categories and contextual features (location, climate, home attributes) are embedded as tokens via a language-model lookup and concatenated into a user token sequence; a candidate category (embedded the same way) attends to this sequence via cross-attention (candidate = query, user tokens = keys/values) to produce a single relevance score. Trained on next-category-search prediction. Popularity bias from naive full-catalog cross-entropy is corrected via adaptive mixed sampling: assemble positive + in-batch negatives + random negatives, keep only the top-K highest-scoring ("hardest") negatives, and compute cross-entropy over positive + hard negatives only.

**Main results:**
Vs. naive cross-entropy training (no negative sampling): overall HR@10 rose from 42.9% to 54.6%; Balance Score rose from 0.53 to 0.75; tail-cohort (86% of categories) HR@10 rose more than tenfold, from 2.1% to 28.4%, while head-cohort accuracy "gave up only a few points." In a live A/B test against the prior production model, the new system drove a statistically significant 5% lift in requests per user (the platform's primary conversion metric).

---

## 2. Experiment Critique

**Design:** A clean offline ablation (naive cross-entropy vs. random vs. in-batch vs. adaptive-mixed negative sampling) plus a live production A/B test — solid design by industry-blog standards, with a purpose-built fairness-style metric (Balance Score) alongside raw accuracy.

**Statistical validity:** The 5% online lift is explicitly reported as statistically significant; offline metric deltas (HR@10, Balance Score) are large enough to be directionally convincing but no confidence intervals or significance tests are given for the offline numbers themselves.

**Online experiments (if any):** One live A/B test against the prior production recommender, reporting a statistically significant 5% lift in requests per user; no duration, sample size, or randomization-unit details disclosed.

**Reproducibility:** Not reproducible — proprietary Thumbtack search/interaction logs across ~500 job categories; no dataset release. A simplified PyTorch snippet of the adaptive-sampling inner loop is included in the post, which does aid conceptual reproduction of the *method* (though not the results).

**Overall:** Credible, well-instrumented industry case study with both offline and online evidence; the core limitation is the usual one for engineering blogs — no external baseline comparison, no statistical detail on the offline numbers, and no released data.

---

## 3. Industry Contribution

**Deployability:** Already deployed in production (A/B tested against and replacing Thumbtack's prior recommender for marketing notifications).

**Problems solved:** Severe popularity bias in a small-catalog (~500 items), extremely sparse-interaction recommendation setting (users request home services far less often than they'd stream videos or shop), and support for multiple marketing-campaign framings from a single model via run-time token masking.

**Engineering cost:** Moderate — a single transformer model plus a mixed-sampling training loop (no separate two-stage retrieval/ranking pipeline needed given the small catalog); the token-masking design is a low-cost way to reuse one model across many campaign types instead of training separate models.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Practical/engineering, not a formal academic contribution; the negative-sampling framing (random vs. in-batch vs. adaptive/hard, and their combination) is presented as an application/synthesis of known ideas to Thumbtack's specific small-catalog, sparse-interaction setting.

**Prior work comparison:** No formal citations or related-work section (industry blog); random negative sampling, in-batch negatives, and hard-negative mining are all long-established recommender/IR techniques the post explicitly names and reasons about rather than treating as novel per se.

**Verification:** No novelty claims to independently verify — presented candidly as an applied engineering write-up.

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Thumbtack search/interaction logs across ~500 job categories | — | Not accessible (proprietary) | Internal telemetry only |

**Offline experiment reproducibility:** Not reproducible (no data release), though the method itself (PyTorch snippet included) is reproducible on any comparable proprietary dataset.

---

## 6. Community Reaction

Not assessed for this source (out of scope for Phase 3 batch processing).

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Andrew Morss
**Affiliations:** Thumbtack, Inc.
**Venue:** Thumbtack Engineering blog (Medium)
**Year:** 2026
**PDF:** Not fetched — analyzed via NotebookLM source; not accessed as local file
**Relevance:** Related — strong popularity-bias/exposure-redistribution technique and Gini-based balance metric, but single-sided (no reciprocal scoring) and no capacity modeling
**Priority:** 1 (per queue tier)

---

## Bibliography Fields

- **title:** A look at compensating for position bias in recommender systems using negative sampling strategies (published as "Building a Transformer-Based Category Recommender at Thumbtack")
- **authors or organization:** Andrew Morss — Thumbtack Engineering
- **year:** 2026
- **venue or type:** Thumbtack Engineering blog on Medium (industry engineering post, not peer-reviewed)
- **link:** `medium.com/thumbtack-engineering/building-a-transformer-based-category-recommender-at-thumbtack-83636da91317`
- **tier tag:** Tier 1 — Adjacent marketplace (local-services), popularity-bias correction via negative sampling
- **what they did (≤80 words):** Built a multi-token Transformer that cross-attends a candidate service category against a user's tokenized search history and context (location, climate, home attributes) to rank ~500 job categories for marketing notifications; run-time token masking lets one model serve multiple campaign types. Fixed severe popularity bias in training via "adaptive mixed sampling" — combining random, in-batch, and hard-negative sampling — and tracked a Balance Score (1 − Gini across popularity cohorts) alongside HR@10.
- **mechanism relevant to two-sided balancing (≤50 words):** Adaptive mixed sampling deliberately shows the model popular ("superstar") items as negatives more often during training, directly counteracting popularity bias; the Balance Score (1 − Gini of per-cohort hit rate) is a directly reusable ecosystem-health metric for measuring match/exposure spread across a skewed user population.
- **metrics used, and the reported effect:** HR@10 (overall 42.9%→54.6%), Balance Score (0.53→0.75), tail-cohort HR@10 (2.1%→28.4%, >10x), online A/B: statistically significant 5% lift in requests per user vs. prior production model.
- **fit for a dating app:** medium — the training-time popularity-debiasing technique and the Gini-based balance metric both transfer well to redistributing exposure away from over-subscribed profiles, but the underlying model is strictly single-sided (predicting a user's next category, not mutual/reciprocal interest) and has no notion of the recommended "item" having finite capacity, since categories are infinite-capacity digital goods.
- **confidence that the item is real and described correctly:** high (NotebookLM grounded answer with extensive direct quotes including exact numbers, a results table, and a PyTorch code snippet across all three queries; source_id validated each time; matches a real, named-author Thumbtack engineering blog post).

---

## Project Relevance

Two mechanisms transfer well here. First, **adaptive mixed sampling** — training-time negative sampling that deliberately over-samples popular items as negatives — is a training-time analogue of exposure redistribution: applied to a dating recommender, it would train the ranking model to treat over-subscribed "superstar" profiles as wrong answers more often, pushing the model to weight subtler compatibility signals over raw popularity and naturally spreading predicted relevance (and thus likely exposure) away from oversaturated profiles toward the long tail. Second, the **Balance Score** (1 − Gini coefficient across popularity-cohort hit rates) is directly reusable, nearly unmodified, as an ecosystem-health metric: tracking 1 − Gini of received likes or matches across desirability quintiles gives exactly the kind of single-number "match spread" metric the project's north star calls for. Run-time token masking is also a transferable market-design-adjacent lever for generating multiple curated recommendation batches (e.g., "active near you" vs. "niche compatible") from one model. The gap: this is a single-sided recommender (predicting which category a user wants next, not whether a category "wants" the user back), so it has no reciprocal/mutual-interest scoring, and categories are infinite-capacity digital goods, so the source has no notion of per-item reply capacity or network interference between competing viewers — both central to the project's core problem and left entirely unaddressed here.
