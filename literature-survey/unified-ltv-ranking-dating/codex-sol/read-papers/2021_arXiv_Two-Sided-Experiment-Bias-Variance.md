# Interference, Bias, and Variance in Two-Sided Marketplace Experimentation: Guidance for Platforms

- **Source index:** 116
- **Source ID:** `ca9ef34f-f462-4c3e-b8c3-3bd64b0bedfc`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Authors:** Hannah Li, Ramesh Johari, Geng Zhao, Gabriel Y. Weintraub
- **Affiliation:** Stanford University
- **Year / venue:** 2021 preprint; 2022 version cited in selection
- **Direction / priority:** D8 marketplace interference / Priority 3
- **URL:** https://arxiv.org/abs/2104.12222

## 1. Summary

The paper analyzes ordinary demand-side (“customer-randomized”) and supply-side (“listing-randomized”) A/B tests in a two-sided market where customers consider listings, apply to one, and each listing accepts at most one application. Competition means treatment and control share scarce counterparts, so difference-in-means is generally biased for the global treatment effect (all treated versus all control).

Large-market theory characterizes bias and variance as functions of supply–demand balance, which side is randomized, intervention strength, and treatment allocation. The bias-optimal side depends on relative supply and demand; often choosing it has little variance cost. Treatment fraction can create a genuine bias–variance tradeoff. The paper also connects these results to staged ramp-ups: small initial allocation may help diagnose a harmful treatment in many regimes, but listing-randomized tests under very high demand can behave in the opposite direction.

## 2. Experiment Critique

The model is deliberately tractable and captures competition on both sides, producing actionable comparative statics rather than only saying “SUTVA fails.” It distinguishes design choice from analysis and considers practical ramp-up risk.

There is no empirical or field validation. The one-shot consideration–application–acceptance process, independent consideration formation, and random application/acceptance simplify ranking, repeated interactions, heterogeneous capacity, and strategic responses. Results are asymptotic; finite-market performance and model misspecification need simulation. Standard estimators remain biased even under the recommended choices.

## 3. Industry Contribution / Project Relevance

A dating A/B test randomizing viewers still contaminates control candidates’ inbound attention; randomizing candidates still changes the pool faced by viewers. The paper provides a disciplined way to choose the less-biased side using market tightness and to avoid assuming 50/50 allocation is automatically optimal.

For the project, every experiment should define the global policy estimand, track local supply–demand ratios by segment, and simulate expected bias under candidate attention caps. Where feasible, geographic/temporal clusters or two-sided randomization remain preferable. The theory evaluates experiments, not the unified LTV ranking loss.

## 4. Novelty

The contribution is a unified bias-and-variance analysis of the two simplest marketplace experiment designs, including the often-overlooked effect of treatment allocation.

## 5. Dataset Availability

The work is theoretical and uses no empirical dataset. Code is **Not specified in source**.

## 6. Community Reaction

Not specified in source.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## 8. Meta Information

- **Market model:** Consideration → one application → capacity-one acceptance
- **Estimand:** Global treatment effect
- **Designs:** Customer- versus listing-randomized A/B tests
- **Evidence:** Large-market theory
- **Main decision variables:** Randomized side and treatment fraction
- **Project role:** Marketplace A/B design and bias sensitivity
