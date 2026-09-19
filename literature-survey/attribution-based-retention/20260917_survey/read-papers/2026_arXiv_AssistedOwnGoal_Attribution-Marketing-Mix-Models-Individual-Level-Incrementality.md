# Media Measurement and the Assisted Own Goal: Attribution, Marketing-Mix Models, and Individual-Level Incrementality

**Source:** https://arxiv.org/pdf/2607.09608.pdf | **NLM source id:** 83299ba5-8a24-4110-9d80-1d8f2b75b107 | **Year / venue:** 2026, arXiv 2607.09608 (06/21/2026) | **Authors / affiliation:** Tobias B. Konitzer, PhD — GrowthLoop | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
The "assisted own goal" hypothesis: a demand-generating (upper-funnel) platform G can cause an incremental purchase, but if distrust drives the consumer to complete the transaction on a downstream trusted marketplace R, the conversion is invisible to G's attribution system. Measured ROAS understates true incremental ROAS by an observability factor κ(τ,φ) = 1 − τ(1−φ) < 1 (τ = distrust/diversion share, φ = off-platform signal recovery rate). ROAS-thresholding budget allocation then defunds the platform that actually generated the demand — a formal equilibrium under-investment result. The fix: (1) ambient audience-level randomization — every activated audience automatically carries its own intent-to-treat (ITT) experiment via deterministic salted hashing of user IDs, requiring no assignment bookkeeping; (2) an individual-level extension of Predicted Incrementality by Experimentation (PIE, Gordon et al. 2023) that trains CATE/heterogeneous-treatment-effect learners mapping pre-assignment features to experiment-identified ITT outcomes, nesting the campaign-level PIE estimate by aggregation.
**Unit of credit:** per-user ITT assignment (Z_i ∈ {0,1}), aggregable to campaign-level predicted incrementality. **Outcome:** channel-complete total conversions (Y_i = Y_i^G + Y_i^R, summed across every sales channel) and true incremental ROAS. **Bias handling:** contrasts computed on randomized assignment, not realized exposure, so delivery-algorithm endogeneity is avoided; channel-complete outcome aggregation makes the ITT estimator provably invariant to diversion share τ, recovery rate φ, and marketplace claim share η (Proposition 3).

## 2. Evidence
- Deployed in production at GrowthLoop (ambient audience-level hashing system).
- Controlled simulation (200,000 simulated consumer journeys/cell, τ ∈ {0,.25,.5,.75,.95}, φ ∈ {0,.3}): at τ=0.75, φ=0, last-touch attribution credited platform G with exactly 25% of conversions it caused (matches theoretical κ=0.25). As true ad effectiveness α rose from 1.0→2.6, attributed revenue for G peaked at α≈1.7 then collapsed, losing nearly half its peak despite G being >2x more effective.
- Recovery simulation (τ=0.7, φ=0.1, 200K users/arm, 2% baseline conversion, true lift=15/1000): proposed ITT model recovered 15.4±1.0 (matches ground truth); last-touch attribution reported only 5.5 (63.3% undercount, exactly κ×truth); MMM estimated 9.7±2.4, with the shortfall falsely re-credited to R's endogenous spend coefficient.
- Cites Gordon et al. (2023) PIE achieving out-of-sample R²=0.88 vs. R²=0.19 for 7-day last-click attribution (from prior literature, not this paper's own experiment).

## 3. Limitations
- Ambient ITT requires the target audience to be enumerable at activation time (addressable via IDs/hashes); broad prospecting/lookalike acquisition cannot be enumerated beforehand, diluting ITT toward zero.
- MMM fails structurally: downstream harvester spend is endogenous to upper-funnel-generated demand, producing multicollinearity/simultaneity bias rather than simple signal loss.
- Extending CATE models to un-experimented acquisition audiences relies on a strong transportability/common-support assumption.
- The theoretical model is deliberately parsimonious: single product, single generator/retailer, static one-shot allocation, reduced-form trust parameter τ; does not model multi-touch attribution windows or strategic suppression of φ by the retailer.

## 4. Prior works named
- Gordon, Moakler & Zettelmeyer (2023) — Predicted Incrementality by Experimentation (PIE), the framework this paper extends to the individual level
- Johnson, Lewis & Nubbemeyer (2017) — Ghost Ads (economics of measuring online ad effectiveness)
- Blake, Nosko & Tadelis (2015) — eBay paid-search field experiment (organic-demand harvesting)
- Gordon, Zettelmeyer, Bhargava & Chapsky (2019) — comparison of attribution/MMM/experimental lift at Facebook
- Künzel et al. (2019) meta-learners / Wager & Athey (2018) causal forests — CATE estimators used for δ(x)

## 5. Project Relevance
- **Answers:** Q1 (2026 industry-adjacent incrementality measurement) and directly addresses last-touch critique relevant to Q2 framing.
- **Attributes retention to individual interactions?** No — attributes ad-driven purchase conversions across channels, not retention/engagement to in-app interactions.
- **Transferable components:** Ambient deterministic salted-hash holdouts (stateless, no assignment bookkeeping) is directly reusable for running always-on, per-user or per-feature-variant randomized experiments; the individual-level CATE extension of PIE is a template for a persuadability/incrementality model; the channel-complete/platform-complete outcome principle — aggregate outcomes across all downstream surfaces (matches, later conversations) rather than crediting only the observed touchpoint — maps closely onto "credit later matches and conversations, not just the last swipe."
- **Required changes:** Move from binary campaign/audience ITT assignment to micro-level fractional credit across a heterogeneous swipe/match/message sequence; re-anchor outcome from purchase conversion to a recurring daily N7-active binary; would need a sequence/path model since this paper's ITT machinery gives an aggregate treatment effect, not a per-touch decomposition within a single treated unit.
- **On last-touch:** Direct, sharp critique — proves last-touch (and even multi-touch/data-driven attribution) cannot fix the "assisted own goal" because the failure is *observability*, not the crediting heuristic: "no reweighting of visible touchpoints can restore credit for this invisible conversion." Directly analogous to the dating platform's problem of ignoring later matches/conversations.
- **Transfer rating:** background — its causal-identification principle (channel-complete/platform-complete measurement invariant to where the outcome is realized) is conceptually the strongest single argument against last-touch found in this batch, but the method itself (audience-level ITT for ad spend) does not directly give a per-swipe fractional-credit mechanism.
