# Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach

- **Source index:** 112
- **Source ID:** `3b36b297-2314-43e3-84d7-b70594cead9f`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Authors:** Kazuki Sekiya, Suguru Otani, Yuki Komatsu, Sachio Ohkawa, Shunya Noda
- **Affiliations:** University of Tokyo, MiDATA, LINKBAL
- **Year / venue:** 2026 / arXiv:2602.19689
- **Direction / priority:** D8 reciprocal recommendation and congestion / Priority 3 (core)
- **URL:** https://arxiv.org/abs/2602.19689

## 1. Summary

This paper studies a live Japanese dating platform, CoupLink, whose default integrator ranks each pair by the product of proposer login, proposer like, receiver login, and receiver relike probabilities. Greedy ranking concentrates exposure on highly responsive receivers. The authors introduce “effective dates,” which discount mutual likes when a receiver has many competing dates, and Exposure-Constrained Deferred Acceptance (ECDA), which caps each receiver by expected likes or dates rather than by recommendation headcount.

Calibrated simulations favor dating-rate orderings and a loose expected-date capacity. A two-week geographic rollout (Kanto treatment; Kansai–Tokai control) applies ECDA with expected dates capped at 1.5 per receiver-day and evaluates difference-in-differences. Predicted average dates fall 0.003, while predicted effective dates rise 0.001 and receiver dating probability rises 0.004. Full-sample realized average likes rise 0.264, but realized date and messaging changes are not significantly positive. After excluding the top 0.1% receiver-days as a diagnostic, effective dates rise 0.003, proposer/receiver dating probabilities rise 0.002/0.005, and receiver likes rise 0.334; messages are unchanged.

## 2. Experiment Critique

This is unusually strong project evidence: production-grade predictions, calibrated simulation, a preregistered field study, explicit interference motivation, and both predicted and realized funnel outcomes. It also shows that raw matches can overstate welfare when attention is concentrated.

The causal design has only one treated and one pooled control geographic unit, so conventional clustered inference is unreliable; the paper itself calls significance suggestive. The top-0.1% exclusion is post hoc and should not replace the full-sample estimate. The two-week horizon is too short for retention or revenue, and the field results do not improve messaging. “Effective dates” assumes a congested receiver selects one match uniformly for deeper interaction, which is a modeling simplification.

## 3. Industry Contribution / Project Relevance

This paper is directly on the target product. It demonstrates why multiplying point predictions is not enough: the integrator changes congestion and the value of every other exposure. ECDA supplies a practical, interpretable constraint and shows loose caps that bind only at the extreme tail can rebalance opportunities.

For a unified LTV ranker, replace expected-date capacity with an expected attention/load budget and optimize a two-sided long-term value measure. Viewer retention, candidate retention, messages, successful exits, and revenue must all enter the estimand. The mixed field result is especially important: improving effective matches without improving messages means the long-term objective cannot stop at mutual likes.

## 4. Novelty

The contribution is the combination of production behavioral predictions with matching theory, a congestion-adjusted “effective date” metric, and exposure constraints expressed in expected likes/dates rather than headcount.

## 5. Dataset Availability

CoupLink data are proprietary. The study is reported as preregistered at AEA RCT Registry `AEARCTR-0015446`. Code availability is **Not specified in source**.

## 6. Community Reaction

Not specified in source; this is a February 2026 preprint.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## 8. Meta Information

- **Domain:** Online dating, 1.5M+ cumulative users
- **Funnel:** Login → like → relike/mutual date → messages
- **Design:** Calibrated simulation plus geographic DID rollout
- **Interference handling:** Geographic market separation and receiver exposure constraints
- **Long-term outcomes:** Not measured
- **Project role:** Core congestion-aware integrator and field-design reference
