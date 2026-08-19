# Paper Analysis: A/B Testing for Recommender Systems in a Two-Sided Marketplace

**Source:** https://arxiv.org/abs/2106.00762  
**Date analyzed:** 2026-08-19

---

## 1. Summary

**Title:** A/B Testing for Recommender Systems in a Two-Sided Marketplace  
**Authors:** Preetam Nandy, Divya Venugopalan, Chun Lo, Shaunak Chatterjee  
**Abstract:** Producer-side experiments are biased when every producer's exposure depends on many consumers receiving conflicting rankings. UniCoRn unifies counterfactual control and treatment rankings without prior graph clustering, with a tunable trade-off between experimental accuracy and serving cost.

**Key contributions:**

- Defines design inaccuracy as deviation from ideal producer-specific counterfactual ranks.
- Introduces UniCoRn, a graph-agnostic rank-blending design with accuracy-cost parameter alpha.
- Proves optimality under the design metric and validates the method in simulation and LinkedIn experiments.

**Methodology:** Producers are assigned control or treatment. For each viewer session, UniCoRn obtains a control ranking, samples a fraction alpha of control producers, reserves the slots occupied by sampled control and treatment producers, scores each with its assigned model, and blends the counterfactual ranks into those slots. Alpha zero minimizes rescoring; alpha one minimizes squared rank inaccuracy.

**Main results:** UniCoRn variants outperform OASIS and low-ramp HaThucEtAl baselines in simulation. At LinkedIn, a candidate-generation experiment raises weekly active unique users 0.51% and sessions 0.57%; a viewee-retention ranker raises them 0.13% and 0.11%. All online effects have p<0.001 with no significant serving-latency increase.

## 2. Experiment Critique

**Design:** Two simulations examine rank accuracy and treatment-effect error under correlated counterfactual ranks and nonlinear response functions. Two production experiments demonstrate feasibility. The blended feed prevents a clean measurement of viewer-side outcomes.

**Statistical validity:** Simulations cover 50,000 sessions or 100 repeated 1,000-session runs. Online effects report p<0.001. Exact experiment duration and absolute sample size are not specified in source; only a 40% viewer-side traffic ramp is given.

**Online experiments:** LinkedIn connection/follow recommendation at tens-of-millions-member scale, using alpha zero and 40% viewer-side traffic.

**Reproducibility:** Algorithms are described and supplementary R/Java code is mentioned; an open repository URL is not specified in source.

**Overall:** Evidence supports producer-side experiment feasibility and significant online outcomes. Optimality is tied to rank inaccuracy, not every nonlinear downstream response; the partial traffic ramp underestimates full-launch effects.

## 3. Industry Contribution

**Deployability:** Designed for large multi-stage ranking systems and does not require a stable interaction graph.

**Problems solved:** Producer-side treatment contamination when control and treatment models imply conflicting rankings.

**Engineering cost:** Moderate: dual scoring of a sampled subset, slot-preserving rank blending, producer assignment, and treatment-specific candidate generation.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** An optimal, graph-agnostic counterfactual rank-unification design with explicit accuracy-latency control.

**Prior work comparison:** Ha-Thuc et al. (2020) uses low-ramp counterfactual seller testing; Nandy et al. (2020) proposes OASIS score blending; Pouget-Abadie et al. (2019) and Saint-Jacques et al. (2019) use graph clustering; Tu et al. (2019) and Lo et al. (2020) study producer feedback effects.

**Verification:** Source-scoped only; no external community or forward-citation search was performed.

## 5. Dataset Availability

**Datasets mentioned:**

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Synthetic rank-conflict simulations | Not specified in source | No packaged data specified | 50,000 sessions; 100 slots. |
| LinkedIn connection/follow experiments | Not public | No | 40% viewer traffic; proprietary logs. |

**Offline experiment reproducibility:** Algorithms are specified, but the production data and an explicit public code repository are unavailable.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Exact mechanism:** Assign shown users to producer-side treatments and blend each profile's counterfactual model rank into a common viewer feed. Alpha controls how many control profiles are rescored to improve experimental fidelity.

**Metrics and reported effect:** LinkedIn candidate generation increases weekly active unique users 0.51% and sessions 0.57%; a viewee-retention ranker increases them 0.13% and 0.11%, all with p<0.001.

**Capacity/congestion relevance:** Producer-side exposure interference is central, and the deployed ranker explicitly optimizes viewee return. Receiver reply capacity, oversubscription, match concentration, and reciprocal acceptance are not modeled.

**Practical mapping:** Use UniCoRn to test receiver-side capacity or retention rankers while holding each profile to one experimental model. Add match and conversation outcomes plus capacity-stratified diagnostics.

**Dating fit: High.** Producer-side exposure experimentation and viewee retention closely match the market-health problem, despite missing double opt-in outcomes.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| No verified inbound mentions within the 45-source corpus. | — | — |

## Meta Information

**Authors:** Preetam Nandy, Divya Venugopalan, Chun Lo, Shaunak Chatterjee  
**Affiliations:** LinkedIn  
**Venue:** NeurIPS  
**Year:** 2021  
**PDF:** available  
**Relevance:** Core  
**Priority:** 1

## Annotated Bibliography Fields

- **Title:** A/B Testing for Recommender Systems in a Two-Sided Marketplace
- **Authors/organization:** Preetam Nandy, Divya Venugopalan, Chun Lo, Shaunak Chatterjee; LinkedIn
- **Year:** 2021
- **Venue/type:** NeurIPS; industry recommender experimentation paper
- **Link:** https://arxiv.org/abs/2106.00762
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Assigned producers to control or treatment ranking models and developed UniCoRn to merge their conflicting counterfactual ranks into one viewer feed. A sampling parameter trades experimental fidelity against rescoring cost. Simulations compare rank and treatment-effect error; LinkedIn deployed the design for candidate-generation and viewee-retention experiments.
- **Mechanism relevant to two-sided balancing (≤50 words):** Preserve one model assignment per shown user while blending profile-specific counterfactual ranks into shared feeds. This enables producer-side measurement without a static interaction graph and supports receiver-retention or capacity-aware ranking tests.
- **Metrics and reported effect:** Candidate generation: weekly active unique users +0.51%, sessions +0.57%. Viewee-retention ranking: +0.13% and +0.11%. All p<0.001; no significant latency increase.
- **Dating-app fit:** High — producer exposure and receiver return are direct analogs, though mutual matches are not measured.
- **Confidence:** High — peer-reviewed industry work with significant live results; duration and absolute traffic are undisclosed.
