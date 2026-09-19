# How Airbnb Measures Future Value to Standardize Tradeoffs

**Source:** https://medium.com/airbnb-engineering/how-airbnb-measures-future-value-to-standardize-tradeoffs-3aa99a941ba5 | **Retrieved via:** jina proxy (direct WebFetch returned 403) | **Year / venue:** 2021-07-13 (item metadata listed "n.d."), Airbnb Engineering (Medium) | **Authors / team:** Mitra Akhtari, Jenny Chen, Amelia Lemionet, Dan Nguyen, Hassan Obeid, Yunshan Zhu | **Analyzed:** 2026-09-17

## 1. Summary
Introduces "Future Incremental Value" (FIV): propensity score matching (PSM) estimates the long-term (30 days to 2 years, typically ~1 year) causal incremental value of 150+ discrete platform actions (e.g., a booking, adding an amenity) when randomized experiments are infeasible, enabling standardized cross-team comparison of action value in a common currency (revenue, bookings, cost).

## 2. Evidence
~1,000 control features across guests/listings; 150+ FIV actions computed across teams; validated against experimental benchmarks as a "gut check"; dashboards report bootstrapped confidence intervals. No specific lift numbers disclosed in the post.

## 3. Limitations
True incremental impact "is never revealed" — FIV cannot be definitively validated post-hoc; high propensity-classifier AUC signals poor matching quality; requires common-support overlap between matched groups; two-sided-marketplace cannibalization/double-counting on the supply side needs separate adjustment; host-level FIV underdeveloped (small samples); unreliable with limited observational data or small groups.

## 4. Project Relevance
- **Answers:** Q2 (adjacent) — closest published analogue found to "attributing a long-horizon outcome to individual actions" via observational causal inference, though the outcome is revenue/bookings, not N7 retention or days-active.
- **Attributes retention to individual interactions?** partly — attributes long-term incremental value to discrete platform actions, not specifically to in-app swipe-level interactions or to retention/days-active.
- **Transferable components:** the propensity-score-matching pipeline that builds a counterfactual "would-have-happened-anyway" comparison group directly targets the project's selection-bias weakness; common-support trimming; two-stage match-then-compare architecture.
- **Required changes:** swap the outcome metric to N7 active-or-not; move the unit from discrete named actions to individual swipe/like/match events; add fractional splitting across multiple interactions in a user history (FIV credits one action type at a time, not a sequence); handle two-sided cannibalization analogous to match/conversation effects on both users.
- **On last-touch:** not explicitly named, but PSM is implicitly a rebuttal to naive/last-touch-style crediting — it exists precisely to strip out the "users who did X selected into doing so" bias that a last-touch label would import wholesale.
- **Transfer rating:** adaptable — the PSM counterfactual-matching methodology directly targets the same "swipes that would have happened anyway" selection-bias problem the project's baseline suffers from, though it must be re-scoped from discrete actions to per-swipe fractional credit.
