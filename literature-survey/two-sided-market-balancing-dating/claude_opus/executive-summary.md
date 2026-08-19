# Executive Summary — Two-Sided Market Balancing for a Dating Recommender

**Run:** `claude_opus` · 2026-08-18 · synthesised by Codex over the complete extraction corpus.

**Coverage: 86 extraction files covering 82 distinct works** (four files duplicate another — a blog
summarising its own paper, a preprint beside its published form; both are cited, neither is counted
as independent evidence). Fit distribution: 40 high, 29 medium, 12 low.

Companion documents: `literature-review.md` (distinct-works reconciliation, citation map, taxonomy,
design-pattern matrix, read-first top 12), `read-papers/` (per-source notes), `log.md` (eight
citation corrections found by reading sources rather than metadata), `RESUME-HERE.md` (residual gaps).

---

## PROOF OF READING

- `literature-review.md:7`: “**86 extraction files**, each source read and extracted individually.”
- `q1.md:13`: “Highly-messaged users reply less often, since their inboxes are flooded.”
- `q2.md:13`: “The LP objective Σf(s,r)g(r,s)x_sr subject to receiver capacity C_R(r) and sender capacity C_S(s) is a direct, real-data-validated instance of Layer 1 (reciprocal scoring) combined with Layer 2 (capacity-aware exposure allocation) — one of the closest matches to the project's own framing found in this corpus.”
- `q3.md:20`: “LiJAR is the strongest direct methodological match found so far for the project's "capacity-aware exposure allocation" layer.”
- `q4.md:127`: “Primarily motivating/diagnostic evidence rather than a transferable mechanism.”
- `q5.md:45`: “One of the **highest-relevance sources in the survey**.”
- `q6.md:117`: “Directly addresses **Layer 3 (market-design levers)**: this is a formal welfare analysis of a "like/application limit" as a platform intervention, providing a theoretical mechanism and proof that capping outbound applications protects the capacity-constrained side (employers, analogous to highly-desirable dating-app recipients) from being overwhelmed, at limited or no cost to the sending side.”
- `q7.md:105`: “This source is one of the most directly on-target items in the survey.”
- `q8.md:47`: “This is one of the strongest direct theoretical matches found in the survey for the project's Layer 2 (capacity-aware exposure allocation).”
- `q9.md:20`: “High relevance to **layer 2 (capacity-aware exposure allocation)** — this is the closest mechanism in this batch to "cap likes/exposure to desirable users, guarantee a floor for under-shown users," expressed as a clean, model-agnostic quota re-ranking optimization with a demonstrated large effect size on a real dataset.”
- `q10.md:20`: “The TU matching mechanism functions as a genuine capacity-aware exposure redistribution scheme, though it models capacity only implicitly.”
- `q11.md:20`: “Strong fit for **Layer 2 (capacity-aware exposure allocation)**: the UAC module is essentially a deployed per-user capacity constraint and exposure-fairness re-ranking mechanism (cap matches per user at Q, remove saturated users from the eligible pool, predict who will actually be available to consume more) — directly transferable to gating who receives more likes/impressions based on remaining reply bandwidth.”
- `q12.md:18`: “Addresses Layer 4 (ecosystem metrics and experimentation under interference) directly and is one of the strongest sources in this survey for the "interference-aware A/B testing" sub-problem.”
- `q13.md:60`: “Directly relevant to layer 3 (market-design levers) and, more loosely, layer 2 (capacity-aware exposure allocation).”
- `q14.md:18`: “Directly addresses **Layer 2 (capacity-aware exposure allocation)**: MRet is essentially a redistribution mechanism — reranking by joint retention gain instead of raw match probability, functionally similar in spirit to LiJAR-style redistribution but keyed on a learned retention curve rather than exposure counts.”
- `q15.md:39`: “Strong, direct hit on Layers 1, 2, and 4.”
86 extraction files covering 82 distinct works.

## Design Patterns

1. **Reciprocal scoring.** Score a recommendation by the probability that both parties like and respond to each other: Tu et al., “Online Dating Recommendations: Matching Markets and Learning Preferences,” SocialRecSys 2014, improved success rates by 46.84% for male suitors versus one-sided recommendation.

2. **Forecast-based capacity redistribution.** Forecast incoming demand and softly penalize oversubscribed profiles while boosting underserved ones behind a relevance floor: Borisyuk et al., “LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace,” KDD 2017, shifted applications +6.5% toward underserved jobs, −8.7% away from overserved jobs, and increased entropy 12%.

3. **Expected-load caps.** Constrain expected likes or dates—not merely the number of matches—using a serving-time allocation mechanism: Sekiya et al., “Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach,” arXiv 2026, improved simulated effective dates from 0.0584 to 0.0623 over the current recommender and validated the effect with a geographic field experiment.

4. **Market-clearing redistribution.** Use equilibrium prices or unmatched probabilities to reduce visibility for congested users and increase it for underexposed users: Tomita et al., “Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets,” RecSys 2023, reduced match Gini from 0.387 to 0.102 on dating data.

5. **Retention-optimized allocation.** Optimize the joint retention gain of the viewer and recipient, rather than raw match probability or equal exposure: Kishimoto et al., “Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching,” ICLR 2026, achieved higher retention using approximately 70% of Max Match’s volume.

6. **Curated, capacity-constrained menus.** Select each user’s displayed assortment while accounting for both-side backlogs and collision risk: Ashlagi et al., “Assortment Planning for Two-Sided Sequential Matching Markets,” Operations Research 2022, achieved at least one-third of the LP upper bound in simulations while explicitly bounding supplier overexposure.

7. **Interference-aware experimentation.** Randomize by regions, clusters, time blocks, or both sides because a treatment changes the shared pool available to controls: Holtz et al., “Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization: Evidence from a Pricing Meta-experiment on Airbnb,” Management Science 2025, measured 19.76% bias from individual-level randomization.

These adjacent-marketplace results require caution: music, Airbnb, jobs, listings, and creator-content systems generally have unlimited or renewable supply-side capacity. Their mechanisms transfer only after replacing “item availability” with a person’s scarce reply bandwidth.

## Most Fundamental Methods

1. **Reciprocal recommendation:** Pizzato et al., “Recommending People to People: The Nature of Reciprocal Recommenders with a Case Study in Online Dating,” User Modeling and User-Adapted Interaction 2013, introduced harmonic-mean bilateral compatibility scoring.

2. **Stable matching:** Gale and Shapley, “College Admissions and the Stability of Marriage,” American Mathematical Monthly 1962, introduced deferred acceptance, the foundational matching mechanism repeatedly adapted to reciprocal recommendation.

3. **Transferable-utility matching:** Choo and Siow, “Who Marries Whom and Why,” Journal of Political Economy 2006, introduced the equilibrium framework underlying congestion pricing and market-clearing recommenders.

4. **Exposure fairness:** Singh and Joachims, “Fairness of Exposure in Rankings,” KDD 2018, established optimization over exposure allocations rather than relevance alone.

5. **Interference-aware experimentation:** Johari et al., “Experimental Design in Two-Sided Platforms: An Analysis of Bias,” Management Science 2022, formalized why single-sided experiments mismeasure marketplace interventions and introduced two-sided randomization estimators.

## Recommendations

1. **Build first: a reciprocal, expected-load capacity reranker.** Keep the existing candidate generator and add a serving-layer score combining bilateral match probability with receiver-side expected incoming likes/dates, remaining reply bandwidth, and recent backlog. Start with LiJAR-style soft boost/penalty and ECDA-style expected-load caps. This is the most practical combination of production evidence and dating-native validity. ECDA is especially compelling because it improved effective dates in a real dating platform; LiJAR supplies the safer incremental deployment pattern.

2. **Optimize and measure whole-market health.** Make the primary objective a retention-weighted marketplace outcome: two-sided retention and conversations, subject to maintaining total matches. Track total matches, conversations per match, share of users with at least one match, received-like/match Gini, wasted likes, reply latency, and churn by desirability cohort. Do not rely on CTR, swipe-right rate, or single-viewer CVR.

   Evaluate with geographic or graph-cluster randomization, switchbacks, or two-sided randomization—not ordinary user-level A/B tests. Report treatment effects separately for sender-constrained, receiver-constrained, and balanced segments. Use a short-term wasted-like metric only as a validated surrogate for long-term retention; Lyft’s region-split/surrogacy framework is a useful template.

3. **Avoid optimizing raw reciprocal relevance alone.** ReSeq, TinVec, Smart Photos, and similar unilateral or unconstrained reciprocal rankers may improve local match probability while concentrating exposure on already-desirable users. Also avoid hard global caps as the first intervention: congestion theory supports limits, but dating-native evidence warns that blunt caps can reduce match volume. Prefer soft, personalized throttling with relevance floors and explicit rollback guardrails.

## Anti-Patterns

- **Popularity/CTR optimization without receiver capacity:** reinforces rich-get-richer exposure and wastes likes.
- **Unconstrained reciprocal scoring:** mutual-interest prediction improves pair quality but can still funnel demand toward the same “superstar” users.
- **Uniform exposure equality:** may destroy total utility; Lorenz-dominance work shows equality can drive everyone’s utility toward zero.
- **Hard, platform-wide like caps:** can reduce useful search and match volume; use targeted, adaptive limits instead.
- **Static offline fairness metrics as the objective:** exposure parity is not equivalent to retention, conversations, or market health.
- **Individual-level A/B testing:** creates interference because treated users consume the same recipients’ reply capacity as controls.

## Open Questions and Next 5 Searches

1. What reply-capacity signal is most predictive: unread likes, recent reply latency, active-session time, or expected dates?
2. How should capacity decay and recover as users reply, churn, pause, or change activity?
3. What is the optimal trade-off curve between total matches, match spread, conversations, and two-sided retention?
4. Can ECDA, TU/IPFP, and MRet be combined into one scalable allocator with explicit reply caps?
5. Which cluster, geographic, or switchback design gives unbiased estimates when desirability networks cross treatment boundaries?
