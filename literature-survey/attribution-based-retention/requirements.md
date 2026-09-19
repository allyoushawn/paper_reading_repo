Date: 2026-04-11 (revised Run 2: 2026-04-12; Run 3 follow-up added 2026-09-17 — see § Run 3)
Topic: Multi-touch attribution and incrementality estimation for user retention

# Attribution-Based Retention - Survey Requirements

## Request

Build a literature foundation for an attribution-based incremental user retention system for a dating platform. The system treats user interactions (conversations, likes, matches) as touchpoints and user days-active as conversions — analogous to ad conversion attribution. Key methodologies sought: multi-touch attribution (Shapley value, Markov chain, data-driven / neural, probabilistic baselines), continuous-outcome and value-based attribution, marketing mix modeling (MMM) as an aggregate complement, budget allocation and bid optimization informed by attribution, and industry production attribution systems.

## Core Keywords

- multi-touch attribution (MTA)
- **continuous-outcome attribution** (required keyword for Run 2)
  - Also search: value-based attribution, revenue attribution, dose-response in ad sequences, fractional/continuous conversion modeling, non-binary outcome MTA
- incrementality estimation
- uplift modeling / heterogeneous treatment effect (HTE) — **background cluster only** (see Must Include)
- counterfactual attribution
- Shapley value attribution (including CASV, axiomatic frameworks, “Shapley Meets Uniform”)
- Markov chain attribution model (probabilistic MTA baselines)
- causal inference for marketing / retention
- conversion attribution
- user retention modeling
- data-driven / neural MTA
- marketing mix modeling (MMM)
- budget allocation and bid optimization informed by attribution
- production attribution (Meta/Facebook, Google Ads, LinkedIn, Uber, Airbnb, etc.)

## Venue priority override (Run 2)

For this survey, treat **KDD, WWW, CIKM**, and **ad-tech / product engineering blogs** (Netflix, Meta, Google, LinkedIn, DoorDash, Uber, Airbnb, Pinterest, Shopify, Stripe, and comparable company engineering publications) as **Priority 1**, **equal to NeurIPS / ICML**. The default venue prestige ranking in the literature-survey skill is overridden for this topic when judging base priority by venue.

## Target Conferences / Journals

- **Priority 1 (with override):** KDD, WWW, CIKM; NeurIPS, ICML, ICLR; major industry engineering blogs listed below
- RecSys — recommendation-flavored retention and engagement models
- SIGIR — user engagement and search-attribution related
- WSDM — web data mining, user behavior modeling
- ICDM, AAAI — data mining / causal ML methods relevant to MTA
- arXiv (causal-ML, stat.ML, cs.LG sections) — fast-moving uplift and attribution research
- ECML/PKDD — European ML venues with causal inference papers

## Target Engineering Blogs

Each query in **Engineering blog queries (Run 2)** must have its outcome logged in `queue.md` under **Engineering blog search log** (including explicit “no results” rows).

- netflixtechblog.com — retention / engagement / experimentation
- engineering.fb.com (Meta) — ads attribution
- research.google — attribution / measurement
- ai.googleblog.com — marketing measurement / attribution
- engineering.linkedin.com — engagement, LiDDA-style attribution
- doordash.engineering — incrementality testing
- eng.uber.com — causal inference / experimentation / ads
- medium.com/airbnb-engineering — experimentation and measurement
- medium.com/pinterest-engineering — attribution / ads
- shopify.engineering — incrementality / marketing science
- stripe.com/blog/engineering — attribution / modeling (if relevant posts exist)

## Search Query List

### Academic

1. `multi-touch attribution machine learning site:arxiv.org`
2. `data-driven multi-touch attribution NeurIPS OR ICML OR ICLR OR KDD OR WWW OR CIKM`
3. `Shapley value attribution marketing conversion`
4. `Markov chain attribution model digital marketing`
5. `continuous-outcome attribution OR value-based attribution OR revenue attribution multi-touch`
6. `fractional conversion OR non-binary outcome multi-touch attribution`
7. `dose-response advertising sequence causal`
8. `marketing mix modeling causal site:arxiv.org OR site:kdd.org OR site:dl.acm.org`
9. `incrementality estimation causal inference uplift modeling`
10. `counterfactual attribution user retention`
11. `causal inference conversion attribution site:arxiv.org`
12. `site:proceedings.mlr.press uplift OR attribution OR incrementality`
13. `site:proceedings.neurips.cc attribution OR uplift OR incrementality`
14. `site:openreview.net multi-touch attribution`
15. `https://api.semanticscholar.org/graph/v1/paper/search?query=multi-touch+attribution&fields=title,year,venue,citationCount,externalIds,authors`
16. `https://api.semanticscholar.org/graph/v1/paper/search?query=marketing+mix+modeling+causal&fields=title,year,venue,citationCount,externalIds,authors`
17. `https://api.semanticscholar.org/graph/v1/paper/search?query=value-based+attribution+advertising&fields=title,year,venue,citationCount,externalIds,authors`

### Engineering blog queries (Run 2 — log each in queue.md)

B1. `site:netflixtechblog.com attribution OR incrementality OR retention`
B2. `site:engineering.fb.com attribution OR incrementality`
B3. `site:research.google multi-touch attribution`
B4. `site:ai.googleblog.com marketing mix OR attribution OR incrementality`
B5. `site:engineering.linkedin.com attribution OR incrementality OR multi-touch`
B6. `site:doordash.engineering incrementality`
B7. `site:eng.uber.com causal inference attribution`
B8. `site:medium.com/airbnb-engineering attribution OR incrementality`
B9. `site:medium.com/pinterest-engineering attribution`
B10. `site:shopify.engineering incrementality`
B11. `site:stripe.com/blog/engineering attribution`

## Survey Scope and Constraints

### Target paper counts (Run 2)

- **Total papers:** 90–120 (net of full survey depth)
- **Already in Done:** 23 (count toward target; **do not re-process**)
- **Net new needed:** ~70–97 (expand queue via Phase 2 / citation harvest / adjacent discovery)

### Cluster targets (approximate budgets)

| Cluster | Target count | Notes |
|--------|----------------|-------|
| Core MTA + ad industry (Markov, Shapley variants, neural, probabilistic) | 60–80 | ~10 in Done at Run 2 start — **primary paper budget** |
| Continuous-outcome / value-based attribution | 10–15 | 0 in Done — expand |
| MMM | 5–10 | 0 in Done — expand |
| Industry blog posts / production systems | 5–10 | ~3 in Done — expand |
| Geo / switchback calibration | ~5 | ~4 in Done — ~1 more |
| Survival / counterfactual churn baselines | 3–5 | 2 in Done — **no further expansion** |
| Background CATE / HTE | 6 | 6 in Done — **no expansion** |

### Must include (revised — Run 2)

**Core — allocate most new paper budget here**

- Markov chain MTA (probabilistic baselines, e.g. Shao & Li 2011, Anderl et al. 2016)
- Shapley value MTA variants (CASV, axiomatic frameworks, “Shapley Meets Uniform”)
- Data-driven / neural MTA (extend beyond current Done set)
- Continuous-outcome attribution / value-based attribution / revenue attribution
- MMM (marketing mix modeling) — aggregate complement to user-level MTA (**5–10 papers**)
- Budget allocation and bid optimization informed by attribution
- Industry production attribution systems: Meta/Facebook, Google Ads, LinkedIn (e.g. LiDDA), Uber, Airbnb (and comparable write-ups)

**Background only — do not expand (papers may remain cited in synthesis; do not add budget)**

- **CATE / HTE methods** (CFR, TARNet, Causal Forest, DML, X-learner, DragonNet, R-learner, etc.): produce aggregate lift estimates, not per-interaction credit scores aligned with Phase 1 labeling.
- **Survival analysis** (DeepHit, Cox-Time, etc.): churn predictors, not attribution models; **2 papers already in Done are sufficient.**

### Exclude

- Pure click-prediction / CTR models with no causal/attribution component
- General recommender systems without retention or attribution angle
- Pure NLP papers (e.g. text attribution / saliency maps)
- Hardware or systems papers

### Hard constraints (Run 2 execution)

1. **Do not start Phase 4** synthesis until the **Done** section of `queue.md` has **≥ 60** papers.
2. **Blog logging:** For every engineering blog query in this file (B1–B11), log outcomes in `queue.md` (**Engineering blog search log**): URLs or titles found, or explicit **“no results from [blog]”** for that query.
3. **Paywalled papers:** Before marking unavailable, log free-version search attempts (arXiv, SSRN, Semantic Scholar, author homepage) in the **Skipped** section of `queue.md`.
4. **Core MTA sequencing:** Until **Core MTA** papers in **Done** are **≥ 50%** of the **total Done count**, do not process **expansion** papers (MMM, continuous-outcome cluster, extra industry blogs, etc.). Papers already in Done count toward the total but **CATE/survival Done items do not count toward the Core MTA numerator** (see `queue.md` **Core MTA accounting** for the canonical list).

### Adjacent-field expansion plan (after core threshold)

1. Citation harvest from `read-papers/` for Markov / Shapley / neural MTA, MMM, value-based attribution
2. Geo-experimentation / switchback (top-up only)
3. Industry production systems and blog-sourced write-ups
4. Bandit feedback and off-policy evaluation only when directly tied to attribution credit or calibration

## Project Context

**Project:** Attribution-based incremental user retention on a dating platform.

**Two-phase system:**

1. An attribution model (e.g., Shapley, Markov chain, data-driven MTA) assigns fractional credit for user days-active to prior interactions (conversations, likes, matches). These scores become **training labels**.
2. A supervised model is trained on those attribution-derived labels to generalize — scoring new interactions in real time without re-running attribution on full history.

**This survey covers Phase 1** — the label generation side. When evaluating papers, prioritize methods that:

- Produce **per-interaction credit scores** (not just aggregate lift estimates)
- Are applicable when “conversions” are user-days-active (not just purchases)
- Handle multi-touch windows with heterogeneous interaction types (conversations vs. likes vs. matches)
- Can account for selection bias (active users get more matches naturally)

**What “useful for this project” means in practice:**

- An attribution method is useful if its output can serve as a **continuous label** for supervised training (not just a binary treatment indicator)
- Incrementality matters more than prediction accuracy — the goal is causal credit, not best-fit correlation
- Industry papers from dating/social/engagement platforms are especially relevant even if not top-venue

**Alignment note (Run 2):** Large parts of the classical **CATE / uplift** literature are demoted to **background** because their default outputs are **not** per-touchpoint credit scores. They remain in the notebook for context and for papers that explicitly connect to MTA or calibration.

## Run 3 (2026-09-17) — Follow-up questions

Two independent runs answer the same questions. Claude-owned outputs: `./20260917_survey/`. **Grok-owned outputs (this run's owner for the Cursor Grok survey): `./20260917_survey_grok/`.** Do not merge the two folders. Project Context for the Grok run is in `./20260917_survey_grok/README.md`.

### Run 3 Grok extras (authoritative for `./20260917_survey_grok/`)

- NotebookLM: reuse the existing parent notebook `6a3b8a8e-6f2f-4efe-99eb-283983fc95d9` for queries, deep research, and new sources. Do not create a second topic notebook.
- Also query related notebooks `unified-ltv-ranking-dating` and `two-sided-market-balancing-dating` for Q2-adjacent retention work (RLUR, GFN4Retention, AURO, SEC, OCARM, MRet). These are retention-optimization papers; the Grok survey must say whether they produce per-interaction credit.
- Recommendation must beat last-touch N7 → latest swipes, with an explicit mapping to swipe / match / conversation touchpoints.

Outputs for the Claude-owned parallel run still go to `./20260917_survey/`. Project Context for that run is in `./20260917_survey/README.md`.

### Questions

- **Q1.** What is the latest attribution-based approach in the industry? Scope: industry-authored or production attribution work dated 2025-01 to 2026-09, plus the newest output from the teams and authors behind the classic papers in `read-papers/`.
- **Q2.** Has anyone in industry published attribution-based retention — attributing user retention, engagement, or days-active to individual in-app interactions? No date limit. Academic work counts when it uses a production dataset or reports a deployment.
- **Deliverable.** A recommendation that replaces the current production approach: last-touch attribution of the N7 retention label to the user's most recent swipes.

### Search strategy

1. **Author and team following (mandatory).** For every row of the follow list in `./20260917_survey/README.md`, search OpenAlex, arXiv, and the web for 2025–2026 output. Log every check, including "nothing new found".
2. **Topic queries (2025–2026).** multi-touch attribution; data-driven attribution; causal attribution; conversion attribution; incrementality measurement; attribution calibration; attention-based attribution; Shapley attribution advertising; privacy-preserving attribution.
3. **Q2 topic queries (no date limit).** retention attribution; engagement attribution; credit assignment for long-term user retention; reinforcement learning for user retention; incremental value of a recommendation or notification on retention; dating app match or like effect on retention; days-active causal effect of in-app action; survival attribution of app events.
4. **Engineering blogs and industry venues, 2025–2026.** The B1–B11 list above plus Amazon Science, Alibaba/Alimama, Snap, Spotify Research, Pinterest, Uber, Airbnb, DoorDash, Lyft, Booking, Match Group / Tinder / Hinge / Bumble tech blogs, Kuaishou, Tencent, ByteDance; venues KDD, WWW, CIKM, RecSys, WSDM, SIGIR, ADKDD 2025–2026.
5. **NotebookLM deep research** on the notebook `6a3b8a8e-6f2f-4efe-99eb-283983fc95d9` with one Q1 query and one Q2 query.

### Scope and constraints

- Target: 40–70 new items processed into `./20260917_survey/read-papers/`. Do not re-process papers already in `read-papers/` of the parent survey.
- Priority order: (a) Q2 hits from any platform; (b) 2025–2026 industry attribution systems; (c) 2025–2026 output from the follow list; (d) 2025–2026 academic MTA.
- Exclude: pure CTR/CVR prediction with no attribution or causal component; MMM-only work unless it introduces user-level credit; LLM text attribution.
- Per-paper extraction runs through NotebookLM (`notebook_query` scoped by `source_ids`), three queries per paper, as in `literature-survey-nlm`.
- Synthesis: NotebookLM cross-source queries, Codex draft, Cursor independent review. Raw reviewer outputs are kept in `./20260917_survey/review/`.

### Run 3 result summary (2026-09-17)

- **Processed:** 50 items into `./20260917_survey/read-papers/` (49 substantive cards, 1 stub) — 21 from 2026, 11 from 2025; discovery via author/topic harvest (OpenAlex + arXiv, 817 matches → 99 shortlist → 30 triage → 16 queued), two web-search agents (D3, D4), and four NotebookLM deep-research runs. NotebookLM notebook grew from 72 to ~120 sources (shared with a parallel Cursor Grok run in `../20260917_survey_grok/`).
- **Q1 answer:** the 2025–26 industry pattern is "observational attribution scores are not the objective; decisions are trained or calibrated on incremental outcomes with an experiment or identification anchor" — Amazon Ads MTA and LinkedIn LiDDA (2025) as anchors; TikTok ETDC+HCA (ADKDD 2026), LinkedIn causal targeting (2026, +7.20% LTV), Kuaishou ALM-MTA (ICLR 2026, front-door per-touch deletion credit at 400M DAU), Alibaba CanniUplift (KDD 2026), Snap HTE (2025). Last-touch survives only as a label to be corrected or as an auxiliary view.
- **Q2 answer:** yes, in part. Direct per-interaction retention credit with production evidence: WeChat/Tencent IURO (RecSys 2023), Kuaishou GFN4Retention (KDD 2024), Instagram notification uplift (Meta 2022). Partial: Pinterest Downstream Rewards (RecSys 2026), Meta Retentive Relevance (2025), Spotify Impatient Bandits (KDD 2023). Reciprocal-market retention ranking (not attribution): MRet (ICLR 2026, dating data), Wantedly (RecSys in HR 2026, online, not significant). No named dating, gaming, or Snap/LinkedIn/TikTok company publication found.
- **Recommendation:** three phases replacing last-touch — v1 predictive deletion residual with prevalence normalization, conservation, and an exposure holdout; v2 experiment-calibrated causal sequence attribution (propensity heads, survival hazard); v3 front-door / flow credit. Confirms the 2026-06-13 plan's direction; revises v1 identification claims and adds a holdout as a precondition. Details in `./20260917_survey/executive-summary.md`.
- **Outputs:** `./20260917_survey/{method-tracker.md, literature-review.md, executive-summary.md}` (Codex-drafted via `literature-survey-nlm` Phase 3.5 / 4-B / 5, Cursor-reviewed PASS WITH FIXES, lead-finalized), `queue.md`, `log.md`, `discovery/`, `review/`.

## Summary of Actual Search Results

Updated 2026-04-14: Phase 3.7 complete; **NotebookLM Phase 4-A** full-notebook **Queries 1–7** completed on retry (2026-04-14) with answers saved in `nlm-phase4-raw-responses.md`; `literature-review.md` updated from that output (per-paper `read-papers/` analyses remain the ground truth for each file).

- **Total papers (Done, survey corpus):** 62 (`queue.md`), each with a matching `read-papers/*.md` analysis file.
- **Extra markdown in `read-papers/` (not in Done):** 3 files (see Meta in `literature-review.md`).
- **Number of review categories (literature-review.md):** 9 topical clusters (core causal/neural MTA; Shapley/axiomatic; Markov/probabilistic & hazard; industry & calibration; MMM; geo/switchback; privacy & measurement; bidding/auction; survival/time-to-event; background CATE/uplift).
- **Key findings:** Path-level **causal MTA** (CAMTA → CausalMTA → DCRMTA) and **Shapley / cooperative** allocations are the closest analogues to **per-interaction fractional labels** for retention; **LiDDA**-style transformer attribution with **experiment calibration** and **Amazon causal calibration** anchor observational credits; **MMM** and most **bidding** work support budgeting and measurement context but not per-touch supervised labels; **CATE/uplift** stays background for touch-credit generation. See `literature-review.md` for citations and `phase3.7-summary.txt` for cross-paper mention graph stats.
