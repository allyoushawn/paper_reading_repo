# Paper Analysis: Optimizing Airbnb Search Journey with Multi-task Learning

**Source:** https://arxiv.org/abs/2305.18431
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Optimizing Airbnb Search Journey with Multi-task Learning
- **authors or company:** Chun How Tan, Austin Chan, Malay Haldar, Jie Tang, Xin Liu, Mustafa Abdool, Huiji Gao, Liwei He, Sanjeev Katariya (Airbnb)
- **venue:** KDD
- **year:** 2023
- **URL:** https://doi.org/10.1145/3580305.3599881
- **source type:** industry paper
- **direction:** D5, D8
- **problem setting:** Airbnb stays search over multi-week guest journeys with six positive milestones (click → long click → payment page → reservation request → host acceptance → uncancelled booking) and negative milestones (rejection, cancellation), balancing guest and host preferences in a two-sided marketplace.
- **objective and label definition:** Primary: uncancelled booking per search impression (binary NDCG relevance). Auxiliary heads: six sequential positive milestones via chain-rule decomposition P(unc)=P(unc|book)P(book|req)…P(c); negative milestones (rejection, cancellation) via Twiddler + Combination modules; labels from multi-week search logs with class imbalance on negatives (<1%–10%).
- **prediction or incrementality:** Journey Ranker predicts listing scores decomposed into Base (positive funnel), Twiddler (negative milestones), and Combination (context-dependent weighting of negative risks); predicts conversion probabilities, not causal incrementality.
- **model architecture:** Four modules end-to-end: Shared Representation (MLP embeddings for listing F_L and context F_C), Base Module (six milestone logits + chain-rule loss), Twiddler Module (three negative-milestone logits), Combination Module (context embedding E_C only → coefficients blending base and twiddler outputs); +9.2% parameters vs baseline single-task unc model.
- **credit assignment:** Search-impression listwise labels; positive milestones attributed along guest journey chain; negative milestones down-weighted via context-conditioned combination; training mixes booker-only positive labels with added non-booker/clicker searches (+20% clicker searches, +50% more search data in ablations).
- **training data and counterfactual handling:** Production Airbnb stays search logs; multi-label impressions with applicable positive/negative milestones; prior MTL booking+long-click and online-fused single-task models failed on bookings or stability—no explicit IPS/counterfactual correction stated.
- **offline and online evaluation:** Offline NDCG (binary uncancelled booking relevance) with 95% CI; online A/B on stays and three other Airbnb products (p<0.01). Funnel metrics: searchers→clickers, clickers→uncancelled bookers.
- **reported gains:** Stays offline NDCG +0.48% (±0.05%) vs baseline (+9.2% params). Stays online: +0.61% uncancelled bookers, +0.14% searchers→clickers, +0.48% clickers→uncancelled bookers. Also +2.0% bookers (in-real-life experiences), +9.0% bookers (online experiences).
- **applicability note for a two-sided dating recommender:** Journey Ranker's chain-rule cascade from swipe/click through match request to retained mutual match mirrors dating funnels where intermediate milestones and negative outcomes (ghosting, unmatch) must be modeled alongside final retention.
- **applicability note for a two-sided dating recommender:** Direct two-sided marketplace precedent (guest vs host milestones); transferable modular MTL pattern, though booking economics and multi-week search horizons differ from swipe-speed dating loops.
- **unverified claims:** none

## 1. Summary

**Title:** Optimizing Airbnb Search Journey with Multi-task Learning
**Authors:** Chun How Tan et al. (Airbnb)
**Abstract:** Presents Journey Ranker, a modular multi-task architecture using positive search milestones decomposed by the chain rule and negative milestones modulated by guest context, deployed across four Airbnb search products with significant business gains.

**Key contributions:**
- Base/Twiddler/Combination module design separating positive funnel, negative risks, and context blending.
- Chain-rule formulation linking six positive guest actions to uncancelled booking.
- Production deployment with offline and online validation across multiple Airbnb products.

**Methodology:** End-to-end MTL with shared embeddings; softmax losses per milestone; Combination Module uses only context embedding to learn journey-stage-dependent negative weights.

**Main results:** +0.48% offline NDCG and +0.61% online uncancelled bookers on stays; strong cross-product generalization.

## 2. Experiment Critique

**Design:** Ablations on milestone subsets, graded vs binary relevance, data sampling (booker-only vs mixed), and module removal; interpretability analysis of Combination Module by guest state/query segment.

**Statistical validity:** 95% CI on offline NDCG; online p<0.01 across products.

**Online experiments (if any):** A/B on stays ranking plus experiences and online experiences products.

**Reproducibility:** Proprietary Airbnb logs; architecture and loss structure well specified.

**Overall:** Strong industrial MTL cascade with rare multi-product online validation; long-horizon guest journey unlike feed ranking.

## 3. Industry Contribution

**Deployability:** Production Journey Ranker replacing prior stays ranker; +9.2% parameter overhead vs single-task baseline.

**Problems solved:** Prior booking+long-click MTL moved clicks not bookings; online-fused single-task models were unstable; binary unc-only training discarded journey structure.

**Engineering cost:** Four-module MTL trained end-to-end; modular design reused across four Airbnb products.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Modular journey-aware MTL with explicit negative-milestone twiddling and context-only combination for two-sided search ranking.

**Prior work comparison:** Builds on Airbnb prior MTL ranking [8]; relates to AITM/ESMM-style sequential decomposition and HM3 hierarchical behaviors.

**Verification:** Online stays +0.61% bookers and ablation table support architectural claims.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Airbnb search logs | Proprietary | No | Multi-week guest journeys |

**Offline experiment reproducibility:** Not reproducible without Airbnb data.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** Primary uncancelled booking with intermediate milestone heads—conversion funnel, not explicit retention/LTV horizon beyond booking.

**(2) Credit assignment:** Chain-rule decomposition across six positive milestones; context-conditioned negative down-weighting; search-list listwise labels.

**(3) Label and horizon definitions:** Multi-week search journey labels; negative milestones sparse; no D1/D7 retention horizon stated.

**(4) Short-term + long-term heads:** Multiple milestone heads fused in end-to-end MTL with Combination Module—cascade pattern (D5) rather than separate LTV prediction head.

**(5) Prediction vs incrementality:** Predicts milestone probabilities along guest journey; not causal effect of a listing on long-term user retention.

**(6) Offline and online evaluation:** Offline NDCG + online A/B on bookers and funnel metrics; two-sided guest/host objectives explicitly modeled.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Two-sided guest/host milestones (acceptance, rejection); no reciprocal matching or congestion modeling stated.

**(8) Migration path from CTR-like model:** Extends single-task unc booking ranker with Base+Twiddler+Combination modules and chain-rule MTL—template for adding negative-outcome and funnel heads to a CTR/match model.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Chun How Tan, Austin Chan, Malay Haldar, Jie Tang, Xin Liu, Mustafa Abdool, Huiji Gao, Liwei He, Sanjeev Katariya
**Affiliations:** Airbnb
**Venue:** KDD 2023
**Year:** 2023
**PDF:** https://arxiv.org/pdf/2305.18431.pdf
**Relevance:** Core
**Priority:** 1
