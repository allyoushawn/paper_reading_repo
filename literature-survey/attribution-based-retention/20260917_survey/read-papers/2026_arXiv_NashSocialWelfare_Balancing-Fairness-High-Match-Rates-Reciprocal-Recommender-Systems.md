# Balancing Fairness and High Match Rates in Reciprocal Recommender Systems: A Nash Social Welfare Approach

**Source:** https://arxiv.org/pdf/2601.13609.pdf | **NLM source id:** e25aceef-c31c-4d9f-8b20-cf96dc9c7c92 | **Year / venue:** 2026, arXiv 2601.13609 | **Authors / affiliation:** Yoji Tomita (CyberAgent, Inc., Japan), Tomohiko Yokoyama (School of Information Science and Technology, The University of Tokyo, Japan) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
On two-sided matching platforms (online dating, job recommendation), reciprocal recommender systems (RRSs) that maximize total matches (Social Welfare, SW) concentrate recommendation opportunities on popular users, creating severe unfairness/envy for disadvantaged users on both sides. The paper extends item-side envy-freeness (Saito & Joachims 2022) to both-side envy-freeness in RRSs and proposes a Nash Social Welfare (NSW) method: an alternating-optimization algorithm (Frank-Wolfe) that maximizes the product of user utilities on each side (log-NSW), which penalizes zero/low-utility outcomes heavily and equalizes recommendation opportunity, achieving near-envy-free allocations. An α-SW objective interpolates between pure match-maximization (α=1) and envy-free division (α→0). A Sinkhorn-algorithm-based entropic-regularization approximation makes the doubly-stochastic-matrix optimization GPU-scalable.
**Unit of credit:** per user's recommendation-list ranking matrix (position/probability of each candidate appearing at each rank) — an allocation/exposure unit, not a retention-credit unit. **Outcome:** expected matches (Social Welfare) traded off against both-side envy-freeness (Nash Social Welfare); no retention, engagement, or LTV outcome. **Bias handling:** addresses *popularity bias* (over-concentration of exposure on popular users) via envy-freeness and the log-NSW objective's equalizing effect — a fairness/exposure bias, not the "engaged users interact more" selection bias relevant to retention attribution.

## 2. Evidence
- Synthetic markets (n,m ∈ {10..300}, popularity-bias parameter λ, position-examination models "log"/"inv"): at n=75/m=50/λ=0.8, SW achieves 90.5±0.30 expected matches but Left Envy=1728.9, Right Envy=735.7; NSW achieves 79.6±0.24 matches with Left Envy=2.10 (p<.001), Right Envy=0.00 (p<.001) — >99.8% envy reduction at a match-rate cost.
- Japanese online dating platform (200×200 preference matrix from ALS on like/dislike and match/sorry logs): SW_LP achieves 111.37 expected matches but Men Envy=434/Women Envy=331; NSW_LP achieves 90.39 matches with Men Envy=31/Women Envy=14 (Gini improves from .518/.597 to .381/.477).
- Speed Dating Experiment dataset (Fisman et al. 2006, 274 male/277 female): IterLP achieves 180.47 matches with envy 983/771; NSW_Sinkhorn achieves 131.99 matches with near-zero envy 17/18.
- Sinkhorn-based methods run in ~200s for n=200-300 vs. >1,000-3,000s (or timeout) for LP-based methods.

## 3. Limitations
- Evaluated only on synthetic data and modest real-world samples (200x200, ~270x270); validation on platforms with millions of active users is an open challenge.
- Even with Sinkhorn acceleration, updating doubly stochastic matrices for millions of users still requires substantial computation.
- Assumes preference matrices are estimated offline and static; does not handle dynamic online preference updates as new interactions arrive.
- At extreme popularity concentration (λ=1.0), NSW trades off meaningful match volume (~71.3 vs ~79.5 for SW) to guarantee double envy-freeness.

## 4. Prior works named
- Saito & Joachims (2022) — Fair Ranking as Fair Division (item-side envy-freeness, extended here to both sides)
- Su, Bayoumi & Joachims (2022) — Optimizing Rankings for Recommendation in Matching Markets (baseline reciprocal ranking model)
- Tomita, Togashi, Hashizume & Ohsaka (2023) — Transferable Utility (TU) reciprocal recommendation baseline
- Caragiannis et al. (2019); Eisenberg & Gale (1959) — Maximum Nash Welfare theory
- Cuturi (2013); Sinkhorn (1967) — Sinkhorn algorithm / entropic regularization for optimal transport

## 5. Project Relevance
- **Answers:** Q2 background — a dating-platform-specific recommender-system paper, but on fairness/exposure allocation, not retention attribution.
- **Attributes retention to individual interactions?** No — optimizes static recommendation-list allocation to maximize expected matches subject to both-side envy-freeness; no retention, engagement, active-days, or LTV outcome at all.
- **Transferable components:** The position-based examination model (e(k) weighting by rank position) is a standard, reusable building block for any exposure/attribution model involving ranked candidate lists; the general insight that naive match/exposure maximization concentrates value unfairly on a subset of users is a relevant fairness consideration if a retention-credit ranking model is later used to actually decide who gets shown — but this is a downstream deployment concern, not part of the credit-assignment mechanism itself.
- **Required changes:** Would need essentially a different problem formulation entirely — this paper's objective and outcome (static match/exposure allocation and envy-freeness) have no retention or attribution dimension; only the position-examination modeling primitive is reusable.
- **On last-touch:** Not discussed — no attribution-heuristic critique of any kind; the paper's only "unfairness" critique is about popularity-driven exposure concentration under match-maximizing ranking, unrelated to last-touch credit assignment.
- **Transfer rating:** background — a well-evidenced dating-platform recommender-system paper on a genuinely different problem (fair match allocation), with only the position-examination-model primitive plausibly reusable for this project.
