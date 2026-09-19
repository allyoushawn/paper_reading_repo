# Impact of Organic Ranking on Ad Click Incrementality

**Source:** https://research.google/blog/impact-of-organic-ranking-on-ad-click-incrementality/ | **NLM source id:** 077dc10e-9f00-4a5b-a018-f35d94d5691d | **Year / venue:** 2026-06, Google Research blog (post itself is dated 2012-03-27 per the retrieved page text; treated per batch metadata) | **Authors / affiliation:** David Chan (Statistician), Lizzy Van Alstine (Research Evangelist) — Google Research | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Follow-up to Google's 2011 Search Ads Pause study (which found 89% of search-ad clicks are incremental). This post asks (1) how often an ad impression co-occurs with an organic result for the same advertiser, and (2) how ad-click incrementality varies with the organic result's rank. Method: meta-analysis of 390 Search Ads Pause quasi-experiments (pausing ad campaigns and observing counterfactual organic traffic). **Unit of credit:** per ad click / aggregate campaign-level incrementality — not per-touchpoint or per-user. **Outcome:** ad click incrementality (share of ad-click visits not replaced by organic clicks when ads are paused). **Bias handling:** pause-based quasi-experiments isolate a causal counterfactual directly, rather than adjusting an observational estimate; authors also recommend geo-randomized experiments for advertiser-level causal measurement.

## 2. Evidence
Across 390 pause studies: 81% of ad impressions and 66% of ad clicks occur with no accompanying organic result on page one. Incrementality by organic rank: 50% of ad clicks incremental at organic rank #1; 82% at ranks 2–4; 96% at rank 5 or lower — compared to the 89% overall average from the original 2011 study.

## 3. Limitations
Measures clicks/traffic only, not downstream conversions, revenue, or ROAS. Reports macro averages; individual-advertiser incrementality varies with brand strength and vertical. Recommends advertiser-specific randomized geo-experiments rather than assuming the macro numbers transfer.

## 4. Prior works named
- Google Search Ads Pause study (2011) — "Studies Show Search Ads Drive 89% Incremental Clicks"
- Vaver & Koehler (2011) — Measuring Ad Effectiveness Using Geo Experiments
- Original 2011 Search Ads Pause study's value-per-click calculation framework

## 5. Project Relevance
- **Answers:** Q1
- **Attributes retention to individual interactions?** No — measures aggregate ad-click incrementality relative to organic search rank; no retention, engagement, or per-interaction credit.
- **Transferable components:** The core "organic baseline" idea — disentangling causal incremental value from activity a user would have generated anyway — is directly analogous to the dating platform's selection-bias problem (engaged users swipe/return regardless). Pause/holdout experiments as the causal-anchor mechanism also transfers conceptually.
- **Required changes:** Everything about granularity: this is aggregate search-campaign click incrementality, not micro-level per-swipe sequence attribution for a recurring N7 outcome; would need a full redesign to heterogeneous, multi-touch, daily-recurring in-app events.
- **On last-touch:** Not discussed — the post does not address multi-touch or last-touch attribution models at all, only ad-vs-organic click substitution.
- **Transfer rating:** background — useful only as a conceptual illustration of the organic-baseline/cannibalization idea, not as an attribution methodology.
