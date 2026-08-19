# Paper Analysis: Optimizing Audio Recommendations for the Long-Term: A Reinforcement Learning Perspective

**Source:** https://arxiv.org/pdf/2302.03561.pdf  
**Date analyzed:** 2026-08-16

## Survey Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | Optimizing Audio Recommendations for the Long-Term: A Reinforcement Learning Perspective; Lucas Maystre, Daniel Russo, Yu Zhao (Spotify / Columbia); arXiv 2023 (industry-lab); https://arxiv.org/pdf/2302.03561.pdf |
| 2 | Source type | Industry-lab paper (Spotify production + academic RL framing) |
| 3 | Direction | D2 |
| 4 | Problem setting | Offline policy improvement for one recommender component (banner/shelf) within a large incumbent policy; optimize multi-month podcast listening habits vs myopic listen-probability ranking. |
| 5 | Objective and label definition | Long-term reward: total listening / engagement with recommended items over months; discovery uses 60-day fixed horizon stickiness (γ=1 over 60 days); daily periods; binary consumption r(c)=1(c>0) in prototypes; retention modeled exogenous with γ churn. Revenue/LTV not direct labels. |
| 6 | Prediction or incrementality | Predicts Q_{π0}(s,a) — long-term value of deviating from incumbent on one recommendation slot; counterfactual Q formula; not uplift vs holdout at training level though holdback validates attribution. |
| 7 | Model architecture | Structured Q-decomposition: short-term clickiness P_w(ν,u,X) × (1 + stickiness u^T θ_a); content-relationship state Z; item-level stickiness models V^{(a)}; augments existing myopic ranker. |
| 8 | Credit assignment | Item-level: Q credits recommendation via (i) change in listen probability and (ii) transition in content-relationship state affecting stickiness; surrogacy Assumption 2 mediates long-term item engagement through Z_{t+1,a}; not slate-level list pooling. |
| 9 | Training data and counterfactual handling | Offline RL on logged trajectories under incumbent π^0; partial policy improvement on one position; short-term model reused from control; stickiness vectors trained on historical discoveries pooled across surfaces. |
| 10 | Offline and online evaluation | Offline: resurfacing correlational analysis on three shows; data-efficiency study (~120,000× vs black-box Q). Online: banner A/B (12 markets, 1 week promo, 60-day follow-up); shelf A/B (9 weeks, tens of thousands of shows). |
| 11 | Reported gains | Banner (impacted users): +81% 60-day show minutes, +32% 60-day active days vs control; median minutes +80%+; shelf week-8 overall podcast minutes +1.7%, discovery consumption +6.2%, lasting discovery rate +5.4%. |
| 12 | Applicability to a two-sided dating recommender | Stickiness model for “habit forming” matches (repeat conversations) vs one-shot clickiness is analogous to try-once vs recurring connection; component-level Q improvement fits staged ranking. No reciprocity, congestion, or match-side outcomes. |
| 13 | Unverified claims | Resurfacing familiar items validated only offline (no A/B yet); 120,000× data-efficiency factor from illustrative offline comparison; substitution effects not fully modeled causally beyond aggregate A/B assurance. |

## 1. Summary

**Title:** Optimizing Audio Recommendations for the Long-Term: A Reinforcement Learning Perspective  
**Authors:** Lucas Maystre, Daniel Russo, Yu Zhao  
**Venue:** arXiv 2023 (Spotify)

**Abstract (from source):** Spotify deployed a podcast recommender optimizing multi-month listening journeys for hundreds of millions of users, departing from short-term proxy optimization. The paper formalizes offline policy improvement on one policy component using structured Q-functions based on item-level listening habits (“stickiness”), with live A/B validation and RL interpretation.

**Key contributions:**
- Content-relationship state and stickiness models for item-level long-term value.
- Q-function decomposition under surrogacy assumptions (Theorems 1, Corollary 1).
- Production discovery ranking: Q̂(s,a) = P_w × (1 + u^T θ_a).
- Large-scale A/B tests on banner and discovery shelf.

**Methodology:** Model user–app interaction as daily MDP; estimate Q_{π0}(s,a) for changing one recommendation slot; decompose into short-term listen model (existing clickiness) and stickiness dot-product; maximize Q for discovery of never-tried shows.

**Main results:** +81% 60-day minutes on banner test among impacted users; shelf experiment +1.7% week-8 overall podcast minutes and +6.2% discovery consumption; stickiness predictions calibrated in holdout analysis.

## 2. Experiment Critique

**Design:** Clean small banner test with holdback for attribution; larger persistent shelf test; multiple treatment arms (personalized, unpersonalized, sqrt stickiness).

**Statistical validity:** Average treatment effects on impacted users (63%); calibration plot for stickiness; long horizon (60 days / 9 weeks) appropriate for stated goal.

**Online experiments:** Tens of millions of users; component-only change isolates methodology.

**Reproducibility:** Proprietary Spotify data; theoretical framework and formulas detailed; resurfacing A/B left for future work.

**Overall:** Authors transparent about measurement/attribution/coordination challenges and myopic industry baseline; discovery counterfactual simplified because organic first-time listen unlikely.

## 3. Industry Contribution

**Deployability:** Now production in several Spotify surfaces; builds on existing clickiness models—additive stickiness vectors at ranking stage.

**Problems solved:** Long-horizon optimization where black-box RL fails on signal-to-noise; mismatch between items users try vs items they stick with.

**Engineering cost:** Separate stickiness vector training with pooled historical discoveries; resurfacing needs near-real-time state (higher infra); coordination across app surfaces noted as challenge.

## 4. Novelty vs. Prior Work

**Claimed novelty:** Month-scale habit formation modeling vs session-scale RL (Ie et al. SlateQ/YouTube, Zou et al., Zheng et al.); structured Q vs unstructured actor-critic.

**Prior work named in source:**
- Zou et al., long-term engagement RL (KDD 2019).
- Ie et al., SlateQ / YouTube RL (2019).
- Chen et al., YouTube REINFORCE / actor-critic (2019–2022).
- Besbes et al., clickability vs engageability (2016).
- Wu et al., bandit return models (2017).
- Wang et al., surrogate outcomes at video service (2022).
- Sutton & Barto; Howard/policy iteration CRM literature.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---------|------|---------|-------|
| Spotify logged trajectories | Production | No | Offline Q estimation |
| Banner / shelf A/B tests | Live experiments | No | Tens of millions of users |
| Resurfacing offline case study | 3 podcast shows | No | Illustrative only |

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

Flagship **Q1/Q8** case: migrates from myopic listen-probability (CTR-like) to unified long-term Q ranking while retaining short-term clickiness head (**Q4**). **Q2** explicitly decomposes long-term user outcome to item-level stickiness via content-relationship states. **Q3** uses 60-day horizon with dense/sparse binary consumption; delay handled via daily periods and fixed horizon. No **Q7** reciprocity. **Q5**: predicts Q-values, not incrementality.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| *(To be filled in during Phase 3.7)* | | |

## Meta Information

- **Authors:** Lucas Maystre, Daniel Russo, Yu Zhao
- **Affiliations:** Spotify; Columbia University (Russo)
- **Venue:** arXiv 2023
- **Year:** 2023
- **Relevance:** Core
- **Priority:** 1
- **Workplace:** cursor-grok
- **nlm:** 69ceeb8b-8273-4163-8aa6-2a347b6b6d7d
- **Note:** Card content supplemented from arXiv PDF after NLM query timeout/disconnect.
