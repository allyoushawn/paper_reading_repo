# Smarter promotions with causal machine learning

**Source:** https://careersatdoordash.com/blog/doordash-smarter-promotions-with-causal-machine-learning/ | **Retrieved via:** jina proxy (direct WebFetch returned 403) | **Year / venue:** 2025-12, DoorDash Engineering Blog | **Authors / team:** Kun Hu, Muxi Xu (DoorDash) | **Analyzed:** 2026-09-17

## 1. Summary
Two-stage causal ML framework using Double Machine Learning (DML) estimates each customer's incremental order probability from a promotion, separating "always-buyers" from "persuadables," then optimizes offer assignment under budget constraints to avoid crediting/discounting orders that would have happened anyway.

## 2. Evidence
Case study 1: non-restaurant targeting achieves near-equal incremental orders at roughly half the cost per incremental order versus a uniform baseline. Case study 2: personalized discount depth shows higher order-rate lift with better cost efficiency in A/B testing.

## 3. Limitations
No explicit limitations stated in the post; no discussion of generalization or confounders beyond the treatment itself.

## 4. Project Relevance
- **Answers:** Q1 — a modern (2025) industry causal-uplift approach directly analogous to the "swipes that would have happened anyway" selection-bias problem named in the project.
- **Attributes retention to individual interactions?** partly — attributes incremental purchase (not retention) to an individual treatment (promotion), at user level rather than per-touch.
- **Transferable components:** Double ML / heterogeneous treatment-effect framework to separate incremental from inevitable outcomes; continuous-treatment modeling; constrained allocation optimization.
- **Required changes:** swap outcome from binary purchase to N7 retention; move treatment unit from promotion-received to individual swipe/like/match; add temporal/sequence handling and fractional (not single-treatment) credit splitting across multiple interactions.
- **On last-touch:** not directly critiqued, but the framework's premise — that naive credit overpays for "always-buyers" — mirrors this project's critique of last-touch's selection-bias weakness.
- **Transfer rating:** adaptable — its causal framework for isolating incremental effect from users who would have converted anyway maps directly onto the project's stated selection-bias weakness, pending reframing to interaction-level, multi-touch, retention outcomes.
