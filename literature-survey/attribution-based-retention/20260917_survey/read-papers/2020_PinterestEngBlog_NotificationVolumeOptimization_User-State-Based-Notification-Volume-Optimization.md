# User state-based notification volume optimization

**Source:** https://medium.com/pinterest-engineering/user-state-based-notification-volume-optimization-7764118f73ff | **Retrieved via:** jina proxy (direct WebFetch returned 403) | **Year / venue:** 2020-04-24 (item metadata listed "2020"), Pinterest Engineering (Medium) | **Authors / team:** Arun Nedunchezhian (Pinterest) | **Analyzed:** 2026-09-17

## 1. Summary
Pinterest segments users into engagement-tier cohorts and trains separate GBDT models per cohort to allocate weekly notification-volume "budgets" — optimizing low-engagement users toward WAU conversion and high-engagement users toward DAU — instead of one uniform volume-optimization objective.

## 2. Evidence
A/B test: overall +1% WAU, driven by a mix of -3% notification volume to dormant users, +17% to resurrected users, and +7% to marginal users (volume reallocated per segment).

## 3. Limitations
None stated explicitly; authors note future work on channel preference modeling and alternative metrics (revenue, impressions, CTR).

## 4. Project Relevance
- **Answers:** Q2 (adjacent) — ties an individual channel (notifications) to an engagement/retention proxy (WAU/DAU) at the user-segment level, not per-touch.
- **Attributes retention to individual interactions?** partly — ties notification-volume decisions to DAU/WAU outcomes, but at the user-segment/channel-budget level, not to individual in-app actions, and with no explicit causal/selection-bias correction.
- **Transferable components:** engagement-tier segmentation (could map to swipe cohorts by recency/frequency); per-segment objective functions (e.g., dormant vs. engaged users weighted differently in the retention label).
- **Required changes:** needs an actual per-interaction (per-swipe) credit mechanism plus counterfactual/selection-bias correction — Pinterest's approach optimizes aggregate volume per cohort and does not attribute credit to individual actions at all.
- **On last-touch:** not discussed.
- **Transfer rating:** adaptable — the engagement-tier segmentation and per-tier objective design is a reusable framing for differentiating swipe cohorts, but it does not itself solve the fractional-credit or selection-bias problem.
