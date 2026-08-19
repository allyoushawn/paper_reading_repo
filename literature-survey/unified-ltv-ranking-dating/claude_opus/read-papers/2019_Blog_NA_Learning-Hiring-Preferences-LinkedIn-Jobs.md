# Paper Analysis: Learning Hiring Preferences: The AI Behind LinkedIn Jobs

**Source:** LinkedIn Engineering Blog, February 12, 2019. https://www.linkedin.com/blog/engineering/learning/learning-hiring-preferences-the-ai-behind-linkedin-jobs
**Date analyzed:** 2026-08-16

## 1. Summary

Benjamin McCann and Nadeem Anjum (LinkedIn) describe the "Recommended Matches" candidate-recommendation feature and the "online learning" algorithm that powers it across the entire LinkedIn Jobs platform. The core problem is threefold: a hirer's preferences for a specific opening are dynamic and highly personalized, so a static ranking model cannot keep up; passive candidates (not actively job-seeking) must be convinced via a "two-way interest" optimization, where hirers must reach out to candidates who are both qualified and likely to respond; and relevance signals were previously fragmented across separate channels (job targeting, passive sourcing via Recommended Matches, applicant review), producing an incoherent cross-channel experience. The key contribution is a globally deployed, real-time online-learning system layered onto an existing XGBoost ranking model: feedback (Message, Archive, Skip) on candidates is aggregated in real time at the hiring-project level (a hiring project links a job post, its search queries, and all candidate feedback for that specific opening), broken out by profile "term type" (skill, title, industry, etc.), sourcing channel, and feedback type. For each candidate X and term type t, a "Personalization Feature" is computed as the dot product z_{t,s,r} = w_{t,s,r}·p_t, where w_{t,s,r} is a vector of term weights derived from historical impression/feedback counts for channel s and rating r, and p_t is X's boolean profile-term vector. These personalization scores are added as a handful of the many features feeding the production XGBoost model, alongside an explicit discovery-channel indicator (interactions with an applicant are treated as fundamentally different from interactions with a recommended match) and job-seeking-intent signals (e.g., Open Candidate status) that boost passive candidates who are more likely to accept outreach. Reported results: the updated algorithm performs "nearly 20% better" than the prior production algorithm when simulating members' past hiring activity; adding the online-learning features produces a 49.61% relative lift in NDCG@1 (averaged over all search queries) versus a model without them; and online-learning features occupy 7 of the top 10 most important features in the XGBoost model.

## 2. Experiment Critique

**Design.** The only evaluation is an offline replay of historical member hiring-activity logs, simulating past hiring and rating actions; no held-out protocol, cross-validation scheme, or sample size is disclosed beyond "averaged over all search queries."

**Statistical validity.** None is demonstrated. Both headline figures ("nearly 20% better," NDCG@1 +49.61%) are single point estimates with no confidence interval, variance, or significance test reported.

**Online experiments.** None are quantitatively reported. Online tuning is described only qualitatively — "we've been actively surveying our job posters" — with no A/B test, ramp schedule, or online metric given.

**Reproducibility.** Not reproducible: no code release, no public or benchmark dataset (only internal LinkedIn hiring logs), and only the top-level personalization-feature equation is published — the underlying term-weight update rule, the full XGBoost feature set, and hyperparameters are not disclosed.

**Overall.** This is a company engineering blog post, not a peer-reviewed or independently evaluated paper. Its quantitative claims should be treated as unverified vendor-reported figures rather than experimental findings.

## 3. Industry Contribution

**Deployability.** Already deployed and proven at scale: the post describes a system running in production across LinkedIn's Jobs platform (Recommended Matches, Job Applicants, Recruiter Search), not a research prototype.

**Problems solved.** Unifies relevance signal across three previously separate sourcing channels into a single XGBoost ranker, and lets that same base model adapt per hiring project in real time without per-project retraining, via a lightweight personalization-feature dot product rather than a full model refit.

**Engineering cost.** The final scoring step (a dot product added as a handful of XGBoost features) is computationally cheap and adds little marginal serving cost, but it requires real-time feedback-aggregation infrastructure — counters keyed by hiring project, sourcing channel, feedback type, and profile term type — which is nontrivial online-learning plumbing even though the resulting feature computation itself is simple. No explicit latency numbers are given.

## 4. Novelty vs. Prior Work

**Claimed novelty.** Replacing a static, per-opening relevance model with a real-time, per-hiring-project personalization signal folded into an existing tree-based ranker, combined with an explicit "two-way interest" mechanism that boosts passive candidates by their own job-seeking-intent signals rather than ranking purely on hirer preference.

**Prior work.** None in the academic sense. As an engineering blog post, the source has no related-work section or citation list. Its only outbound references are a Wikipedia explainer for XGBoost, a Wikipedia explainer for NDCG (the evaluation metric used), and internal LinkedIn product pages (the original Recommended Matches launch post, the Open Candidate feature). No prior recommender-systems literature is cited or positioned against.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| LinkedIn member hiring-activity logs | Internal production logs (Message/Archive/Skip actions, hiring-project metadata) | No | Used to retrospectively simulate past hiring/rating behavior; size, date range, and sampling procedure not disclosed |
| Job-poster feedback surveys | Internal qualitative survey data | No | Used only for online-side monitoring; not a formal offline dataset |

## 6. Community Reaction

Not assessed in NotebookLM mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Learning Hiring Preferences: The AI Behind LinkedIn Jobs," Benjamin McCann, Nadeem Anjum (LinkedIn Corporation), Blog, 2019, https://www.linkedin.com/blog/engineering/learning/learning-hiring-preferences-the-ai-behind-linkedin-jobs |
| 2 | Source type | Blog (LinkedIn Engineering Blog) |
| 3 | Direction | D8 |
| 4 | Problem setting | Two-sided ranking between job candidates and hirers/recruiters on LinkedIn Jobs: dynamic, per-opening hiring preferences; two-way interest optimization for passive candidates; unifying relevance across three sourcing channels |
| 5 | Objective and label definition | Real-time engagement labels — hirer feedback actions (Message, Archive, Skip) — aggregated per hiring project, sourcing channel, feedback type, and profile term type. Time horizon is real-time/online, feedback taken into account instantly within a session; no delay or censoring model is used or needed, since aggregation happens as feedback arrives |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. The system ranks candidates by a predicted-relevance score ("the candidates most likely to accept your outreach"), with no causal or counterfactual framing |
| 7 | Model architecture | Real-time personalization feature z_{t,s,r} = w_{t,s,r}·p_t (dot product of historical term-weight vector and candidate boolean profile-term vector), added as a subset of features to a production XGBoost ranking model; discovery channel explicitly represented as a feature |
| 8 | Credit assignment | Pointwise, aggregate-count based: hirer feedback (Message/Archive/Skip) on a candidate is tallied by profile term, sourcing channel, and rating into a term-weight vector; a new candidate's score is the dot product of that aggregate weight vector with their own profile terms. No counterfactual or IPS-style correction is applied — it is a direct historical-count aggregation |
| 9 | Training data and counterfactual handling | Real-time production feedback logs (Message/Archive/Skip) aggregated at the hiring-project level; historical hiring/rating logs are separately replayed for offline simulation. No IPS, doubly-robust, or other counterfactual correction is described |
| 10 | Offline and online evaluation | Offline: simulated past hiring activity, reporting "nearly 20% better" than the prior algorithm and NDCG@1 +49.61% relative lift from adding online-learning features (averaged over all search queries). Online: qualitative monitoring only, via job-poster feedback surveys — no quantitative online A/B metric is reported |
| 11 | Reported gains | NDCG@1 +49.61% relative lift (online-learning features vs. without, offline simulation, averaged over all search queries); ~20% better than the previous production algorithm (offline simulation of past hiring activity); online-learning features occupy 7 of the top 10 most important features in the production XGBoost model |
| 12 | Applicability to a two-sided dating recommender | Structurally the closest published analogue in this batch to viewer-and-candidate ranking on a dating app — its explicit "two-way interest" mechanism (boosting passive candidates by job-seeking intent, not just hirer preference) is a real-system precedent for reciprocity. It offers no retention/revenue objective, no incrementality, and only coarse aggregate-count credit assignment, so it is evidence for the ranking-side reciprocity mechanism only, not for the survey's core unified-objective question |
| 13 | Unverified claims | "Nearly 20% better" and "49.61% lift" are self-reported point estimates with no confidence interval, significance test, or independent verification; no quantitative online A/B results are given despite the post's claim of continuous improvement "based upon your feedback" |

## Project Relevance

This paper speaks most directly to **Q7** (what is specific to two-sided/reciprocal markets): its explicit "two-way interest" framing, where the ranking algorithm boosts passive candidates by their own job-seeking-intent signal rather than ranking purely on hirer preference, is a real, deployed-system analogue to reciprocity in a dating recommender — arguably the closest structural match among industry sources in this survey, since both sides (hirer and candidate) are actively re-ranked based on mutual interest. It touches **Q2** (credit assignment) only shallowly and as a negative example: the per-hiring-project term-weight aggregation is a coarse, non-counterfactual mapping of user-level feedback to item-level (candidate) scores, useful mainly as a contrast against more principled attribution schemes elsewhere in the survey. It does not address **Q1, Q3, Q4, Q5, Q6, or Q8**: there is no retention or revenue training objective, no delayed label or horizon, no fusion of short-term and long-term heads, no incrementality treatment, no offline/online evaluation methodology beyond an unvalidated offline replay, and no migration path from a proxy metric to a long-term objective — the entire system optimizes immediate hirer engagement (Message/Archive/Skip) with no LTV framing.

## Papers That Mention This Paper (Reverse Citation Map)

_This paper proposes no distinctively-named method, so no automated reverse-citation match was possible._

## Meta Information

- **Authors:** Benjamin McCann, Nadeem Anjum
- **Affiliations:** LinkedIn Corporation
- **Venue:** LinkedIn Engineering Blog
- **Year:** 2019
- **Relevance:** Core
- **Priority:** 1
- **nlm:0f0bb519-890d-4f88-99ee-00e98360f699**
