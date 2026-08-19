# Paper Analysis: Learning Hiring Preferences: The AI Behind LinkedIn Jobs

**Source:** https://www.linkedin.com/blog/engineering/learning/learning-hiring-preferences-the-ai-behind-linkedin-jobs
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Learning Hiring Preferences: The AI Behind LinkedIn Jobs
- **authors or company:** Benjamin McCann, Nadeem Anjum (LinkedIn Corporation)
- **venue:** LinkedIn Engineering Blog
- **year:** 2019
- **URL:** https://www.linkedin.com/blog/engineering/learning/learning-hiring-preferences-the-ai-behind-linkedin-jobs
- **source type:** blog
- **direction:** D8
- **problem setting:** Two-sided ranking between job candidates and hirers on LinkedIn Jobs: dynamic per-opening preferences, two-way interest for passive candidates, unifying relevance across three sourcing channels (Recommended Matches, applicants, Recruiter Search).
- **objective and label definition:** Real-time hirer feedback labels (Message, Archive, Skip) aggregated per hiring project, sourcing channel, feedback type, and profile term type; horizon is real-time within session — no delay or censoring model.
- **prediction or incrementality:** Prediction only — ranks candidates by predicted relevance ("most likely to accept your outreach"); no causal or counterfactual framing.
- **model architecture:** Real-time personalization feature z_{t,s,r} = w_{t,s,r}·p_t (dot product of historical term-weight vector and candidate boolean profile-term vector), added as features to a production XGBoost ranking model; discovery channel explicitly represented; job-seeking-intent signals boost passive candidates.
- **credit assignment:** Pointwise aggregate-count: hirer feedback tallied by profile term, sourcing channel, and rating into term-weight vector; new candidate score is dot product with their profile terms — no IPS or counterfactual correction.
- **training data and counterfactual handling:** Real-time production feedback logs aggregated at hiring-project level; historical logs replayed for offline simulation; no IPS, doubly-robust, or other counterfactual correction described.
- **offline and online evaluation:** Offline replay of past hiring activity reporting NDCG@1 +49.61% relative lift from online-learning features (averaged over all search queries) and "nearly 20% better" than prior algorithm; online monitoring via job-poster surveys only — no quantitative A/B metric reported.
- **reported gains:** NDCG@1 +49.61% relative lift (offline simulation); ~20% better than previous production algorithm (offline simulation); online-learning features occupy 7 of top 10 most important XGBoost features.
- **applicability note for a two-sided dating recommender:** Closest industry analogue to viewer-and-candidate ranking — explicit "two-way interest" boosting passive candidates by job-seeking intent, not just hirer preference, is a deployed reciprocity precedent.
- **applicability note for a two-sided dating recommender:** No retention/revenue objective, no incrementality, only coarse aggregate-count credit assignment — evidence for reciprocity mechanism only, not unified LTV ranking design.
- **unverified claims:** "Nearly 20% better" and 49.61% NDCG@1 lift are self-reported point estimates with no confidence interval or significance test; no quantitative online A/B results despite claims of continuous improvement.

## 1. Summary

LinkedIn describes the "Recommended Matches" feature and online-learning algorithm powering LinkedIn Jobs. Hirer feedback (Message, Archive, Skip) is aggregated in real time at the hiring-project level by profile term type, sourcing channel, and feedback type. A personalization feature (dot product of term-weight vector and candidate profile-term vector) feeds a production XGBoost model alongside discovery-channel and job-seeking-intent features. System unifies relevance across three previously separate sourcing channels and adapts per opening without per-project retraining.

## Project Relevance

Speaks most directly to **Q7** (two-sided/reciprocal markets): "two-way interest" boosting passive candidates by their own job-seeking-intent signal is a deployed analogue to dating reciprocity. Touches **Q2** shallowly as a negative example: coarse non-counterfactual term-weight aggregation contrasts with principled attribution elsewhere. Does not address Q1, Q3, Q4, Q5, Q6, or Q8 — no retention/revenue objective, delayed labels, long/short head fusion, incrementality, validated online eval, or proxy-to-LTV migration path.

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | Immediate hirer engagement (Message/Archive/Skip); retention/LTV/revenue not specified. |
| **(2) Credit assignment** | Aggregate-count term-weight dot product; no counterfactual correction. |
| **(3) Label / horizon; delay / sparsity / censoring** | Real-time feedback within session; no delay model. |
| **(4) Short-term vs long-term head fusion** | Not specified in source. |
| **(5) Prediction vs incrementality** | Prediction only. |
| **(6) Offline / online eval** | Offline replay with NDCG@1; qualitative online surveys only. |
| **(7) Reciprocity / congestion / fairness / revenue vs match** | Two-way interest via job-seeking-intent boost; congestion and revenue trade-offs not specified. |
| **(8) CTR → unified long-term migration** | Not specified in source. |

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Benjamin McCann, Nadeem Anjum  
**Affiliations:** LinkedIn Corporation  
**Venue:** LinkedIn Engineering Blog  
**Year:** 2019  
**Relevance:** Core  
**Priority:** 1
