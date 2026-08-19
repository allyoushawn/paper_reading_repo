# Paper Analysis: Managing Congestion in Two-Sided Platforms: The Case of Online Rentals

**Source:** https://arxiv.org/pdf/2308.14703.pdf  
**Date analyzed:** 2026-08-16  
**Workplace:** cursor-grok

## Survey Card

- **title:** Managing Congestion in Two-Sided Platforms: The Case of Online Rentals
- **authors or company:** Caterina Calsamiglia, Laura Doval, Alejandro Robinson-Cortés, Matthew Shum
- **venue:** arXiv (econ.GN)
- **year:** 2023
- **URL:** https://arxiv.org/pdf/2308.14703.pdf
- **source type:** academic
- **direction:** D8
- **problem setting:** Thick two-sided room-rental platform (Barcelona; 10% user sample, Jan 2018–Feb 2020): ranking algorithm uses shared tie-breaking randomization so listing order is invariant across renters, concentrating clicks/requests on ~20% of rooms despite one-to-one capacity constraints.
- **objective and label definition:** Estimated request utility U_is from rank-ordered logit on clicks/requests; click propensity depends on position and E[U|info]; counterfactuals vary ranking mix α∈[0,1] between full personalization and random order; outcomes = click/request concentration (Lorenz curves) and average requested-room utility; no ML ranking model or retention label.
- **prediction or incrementality:** Structural discrete-choice estimation (not ML ranker); counterfactual simulation holds search sets fixed and reorders results; assumes search volume invariant to ranking (conservative on horizontal differentiation).
- **model architecture:** Two-stage rank-ordered logit: request utility with room/user covariates and landlord-preference match; click model with position polynomial, top-position dummies, and E[u|I]×position; optional k-medoids user clusters for heterogeneity; α-weighted hybrid ranking for counterfactuals.
- **credit assignment:** Not applicable — econometric choice model, not learned recommender with delayed feedback.
- **training data and counterfactual handling:** 1,202 users, 45,462 rooms, 2,066,147 search results, 89,624 clicks, 8,542 requests; complete click/request sequences; counterfactuals reorder observed search results without re-modeling search depth.
- **offline and online evaluation:** Offline counterfactual simulation only; no platform field test of proposed algorithms; cites Chen, Hsieh, and Lin (2023) online-dating congestion experiment as related evidence.
- **reported gains:** Top position captures >15% of all clicks/requests vs ~4% at position 10; top 20% of rooms account for ~100% of requests; status-quo (utility, congestion) lies below efficiency frontier — modest α (<0.1) on random ranking matches data utility with lower congestion; full personalization (α=1) sharply increases congestion.
- **applicability note for a two-sided dating recommender:** Shared global ranking/tie-breaking is a concrete mechanism for prospect congestion when many seekers see the same profiles in the same order; per-user randomization or mixed α-ranking is a low-model alternative to full personalization.
- **applicability note for a two-sided dating recommender:** Room-rental one-to-one capacity parallels dating matches but not swipe-volume dynamics; no reciprocal scoring, session behavior, or retention outcomes — utility metric is request propensity, not message/reply/LTV.
- **unverified claims:** none
