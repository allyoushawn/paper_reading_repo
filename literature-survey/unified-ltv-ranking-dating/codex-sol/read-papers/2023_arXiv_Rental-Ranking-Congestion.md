# Managing Congestion in Two-Sided Platforms: The Case of Online Rentals

- **Source index:** 115
- **Source ID:** `d6cb3b6e-ec63-485d-b536-51adab347bec`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Authors:** Caterina Calsamiglia, Laura Doval, Alejandro Robinson-Cortés, Matthew Shum
- **Affiliations:** ICREA/IPEG/IZA, Columbia University, University of Exeter, California Institute of Technology
- **Year / venue:** 2023 / arXiv preprint
- **Direction / priority:** D8 two-sided congestion / Priority 3 (core)
- **URL:** https://arxiv.org/abs/2308.14703

## 1. Summary

Using logs from a large medium-term room-rental platform, the paper shows that ranking can manufacture congestion. The platform assigns a partial ordering, then breaks ties with the same random number for every user, causing many renters to view, click, and request the same rooms. The authors estimate click/request preferences and simulate rankings that vary personalization and user-specific randomization.

Full personalization raises expected utility but also substantially increases concentration because preferences are mainly vertically aligned: users agree on desirable rooms. Fully random order modestly reduces congestion. Mixtures of personalized and randomized ranking trace a utility–congestion frontier, and the status quo lies below that frontier—there are policies that reduce congestion without lowering expected match utility or increase utility without worsening congestion. Exact lift percentages are **Not specified in source text**; evidence is primarily graphical counterfactual analysis.

## 2. Experiment Critique

The paper models the actual search funnel, checks fit against click/request Lorenz curves, and studies preference heterogeneity through cluster robustness. Its key result is more nuanced than “personalize more”: the effect depends on horizontal versus vertical differentiation.

All policy conclusions are counterfactual. The simulation holds the number of searches, clicks, and requests fixed and omits equilibrium responses and unobserved utility shocks. The platform does not observe all final bookings, so “matches” are proxied by requests. There is no randomized test, and changing ranks could alter search depth or landlord behavior.

## 3. Industry Contribution / Project Relevance

Dating preferences also contain strong vertical components, so a high-capacity personalized model can make everyone chase the same candidates. The paper suggests two cheap diagnostics before complex market design: compare rankings across viewers and measure exposure/request Lorenz curves. User-specific tie-breaking or controlled randomness can recover frontier improvements when near-tied candidates exist.

For unified LTV ranking, personalization must be optimized jointly with candidate load. A congestion penalty should depend on predicted reply/conversation capacity, not only exposure count, and experiments must track both sides’ retention. Randomization can also provide causal exploration, but excessive randomization may lower match quality.

## 4. Novelty

The study empirically links common versus user-varying rankings to two-sided congestion and estimates a personalization–congestion frontier governed by preference differentiation.

## 5. Dataset Availability

The room-rental platform data are proprietary. Code or a public derived dataset is **Not specified in source**.

## 6. Community Reaction

Not specified in source.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## 8. Meta Information

- **Domain:** Medium-term room rental
- **Observed funnel:** Search → view/click → request
- **Method:** Structural preference estimation and ranking counterfactuals
- **Congestion measure:** Concentration/Lorenz curves of clicks and requests
- **Final bookings:** Incompletely observed
- **Project role:** Personalization–congestion tradeoff and randomized tie-breaking
