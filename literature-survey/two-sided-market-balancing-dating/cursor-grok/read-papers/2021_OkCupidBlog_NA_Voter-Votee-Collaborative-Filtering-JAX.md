# 2021 OkCupid Tech Blog — voter vs votee CF with JAX

**Title:** Large-scale collaborative filtering to predict who on OkCupid will like you, with JAX  
**Authors:** Zachary Jablons  
**Year / venue:** 2021, OkCupid Tech Blog  
**Link:** https://tech.okcupid.com/large-scale-collaborative-filtering-to-predict-who-on-okcupid-will-like-you-with-jax-88ac8a934044  
**Tier:** 1  
**nlm:** 199f4755-e45b-4d9b-b46c-03c7e011160e (NLM body miss; cited from live page)

## Summary
OkCupid records likes/passes as votes. Interaction matrix is directed: `dot(A,B)` must not equal `dot(B,A)`. Each user has a **voter** vector and a **votee** vector. SVD-style reconstruction trained in JAX on hundreds of millions of votes/week; ~3 hours for a week of sitewide data. Explicitly the inbound-likeability model, not “who will you like.”

## Metrics
Qualitative improvement over baseline; no public A/B %.

## Project Relevance
**High** as the scoring primitive (P(they like you)). **Low** as a market balancer — no capacity or redistribution.

## Reverse Citation Map

| Mentioning Paper | Section | Summary of Mention |
|------------|------|--------------|
| [2025_TinderBlog_2T-PMatch_Elasticsearch-8-Migration.md](./2025_TinderBlog_2T-PMatch_Elasticsearch-8-Migration.md) | corpus | Directed like-back scoring with an online match-rate A/B; OkCupid only reports offline like prediction. |
