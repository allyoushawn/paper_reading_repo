# Paper Analysis: Beyond A/B Testing — Using Surrogacy and Region-Splits to Measure Long-Term Effects in Marketplaces

**Source:** Lyft Engineering blog (Medium), Amber Wang and Yoonji Kim, published 25 Mar 2026 (https://eng.lyft.com/beyond-a-b-testing-using-surrogacy-and-region-splits-to-measure-long-term-effects-in-marketplaces-9cb06d628f2d)
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** Beyond A/B Testing: Using Surrogacy and Region-Splits to Measure Long-Term Effects in Marketplaces
**Authors:** Amber Wang, Yoonji Kim (Lyft, Foundational Models team)
**Abstract:**
Lyft engineering post presenting a three-step causal framework to estimate the "market-mediated" long-term effects of resource-allocation decisions (driver incentives, rider pricing) in a two-sided marketplace, where standard A/B tests fail due to feedback loops and interference.

**Key contributions:**
- A two-step surrogacy framework: (1) residualized regression maps a policy change to shifts in short-term "negative user experiences" (wait time, surge, cancellations, driver idleness); (2) doubly robust AIPW estimation with a "surrogacy index" maps those negative-experience shifts to long-term outcomes (future rides, retention).
- A forward-selection algorithm (inspired by Forward Difference-in-Differences, Li 2024) to pick treated/control regions for region-split experiments, improving pre-intervention fit and statistical power over naive region selection.
- An end-to-end causal engine combining market-mediated and direct long-term effects into a single policy-level forecast, validated via switch-back experiments (Step 1), user-split experiments (Step 2), and region-split experiments (overall).

**Methodology:**
Observational causal inference (residualized regression + AIPW) for fast, cheap estimation, cross-validated with three complementary experiment designs (switch-back, user-split, region-split) that each isolate the marketplace from a different form of interference.

**Main results:**
No specific quantitative lifts reported — this is a methodology/framework post with simulated illustrative figures, not a report of a shipped result.

---

## 2. Experiment Critique

**Design:**
Combines observational causal inference (residualized regression, AIPW) with three types of validation experiments (switch-back, user-split, region-split), explicitly chosen because standard individual-user A/B tests suffer interference in a two-sided marketplace. The authors state plainly that "no single form of experiment can provide a perfect verification" and combine multiple imperfect signals instead.

**Statistical validity:**
Not specified in source — no confidence intervals, p-values, or effect sizes are given; the post illustrates its methodology with simulated example figures rather than reporting real production statistics.

**Online experiments (if any):**
Switch-back experiments (alternating policy settings across time blocks) validate Step 1; user-split experiments validate Step 2; region-split experiments (with forward-selection of treated/control regions) validate the combined end-to-end forecast.

**Reproducibility:**
Not reproducible — no code or data released; methodology described at a conceptual/formula level only, with simulated (not real) example data shown.

**Overall:**
A credible and directly relevant causal-inference framework for interference-heavy marketplaces; the core contribution is methodological (how to measure), not empirical (no reported lift numbers to critique).

---

## 3. Industry Contribution

**Deployability:**
Described as Lyft's actual production framework ("Foundational Models team"); relies on standard causal-inference tooling (residualized regression, AIPW) that is deployable at other marketplace companies.

**Problems solved:**
Directly solves the problem of measuring long-term, network-mediated effects of allocation policy changes when standard user-level A/B tests are confounded by marketplace interference (one user's treatment changes the environment for others).

**Engineering cost:**
Moderate-to-high — requires building residualized regression models per negative-experience metric, an AIPW causal-effect pipeline, a surrogacy-index calibration step, and infrastructure for three distinct experiment types (switch-back, user-split, region-split with forward-selection region matching).

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** The forward-selection region-matching algorithm is explicitly framed as inspired by, not identical to, Forward Difference-in-Differences (Li, 2024); the two-step surrogacy decomposition (policy → negative experience → long-term outcome) is presented as Lyft's own framing of "surrogacy in its broad sense."

**Prior work comparison:** Per NotebookLM, the post cites exactly two academic works: Chernozhukov et al. (2021) for AIPW, and Li (2024) for Forward Difference-in-Differences. No formal related-work section — this is an engineering blog post, not a peer-reviewed paper.

**Verification:** Not independently verified beyond the two named citations; no broader literature comparison in source.

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Lyft production marketplace data (rides, prices, incentives, wait times, cancellations) | N/A | No | Internal production data |
| Simulated example data (Step 1 elasticity curves, Step 3 region-split discrepancy) | N/A | N/A | Illustrative only, not real results |

**Offline experiment reproducibility:**
Not reproducible — all real data is internal; illustrative figures use simulated data only.

---

## 6. Community Reaction

No significant community discussion found (not investigated as part of this NotebookLM-based extraction).

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Amber Wang, Yoonji Kim
**Affiliations:** Lyft (Foundational Models team)
**Venue:** Lyft Engineering blog (Medium)
**Year:** 2026
**PDF:** Not available — web article, accessed via NotebookLM source
**Relevance:** Related
**Priority:** 2

---

## Bibliography Fields

- **title:** Beyond A/B Testing: Using Surrogacy and Region-Splits to Measure Long-Term Effects in Marketplaces
- **authors or organization:** Amber Wang, Yoonji Kim; Lyft
- **year:** 2026
- **venue or type:** Engineering blog post (Lyft Engineering / Medium)
- **link:** https://eng.lyft.com/beyond-a-b-testing-using-surrogacy-and-region-splits-to-measure-long-term-effects-in-marketplaces-9cb06d628f2d
- **tier tag:** Tier 1 — Adjacent marketplace (ride-hailing)

**what they did (≤80 words):** Lyft presents a three-step causal framework for measuring long-term "market-mediated" effects of resource-allocation policy (pricing, incentives) that standard A/B tests miss due to marketplace feedback loops. Step 1 maps policy changes to short-term negative user experiences via residualized regression; Step 2 maps those experiences to long-term outcomes via doubly-robust AIPW and a surrogacy index; Step 3 validates the combined forecast via region-split experiments using a novel forward-selection algorithm for treated/control region matching.

**mechanism relevant to two-sided balancing (≤50 words):** Region-split and switch-back experiment designs directly address interference from shared capacity — splitting by geography/time instead of by user avoids one side's treatment draining a shared resource pool that control users also depend on. No reciprocal-scoring or capacity-allocation algorithm is proposed; interference-aware measurement, not allocation, is the contribution.

**metrics used, and the reported effect:** No production quantitative results reported (framework/methodology post with simulated illustrative figures only). Named metrics: negative user experience (wait time, surge, cancellations, driver idleness/earnings), future rides, retention, and the derived "surrogacy index." No effect sizes given.

**fit for a dating app:** high — reason: per NotebookLM, region-split/switch-back designs are a directly transferable interference-correction technique for a capacity-constrained two-sided market, and the "negative user experience → churn" surrogacy framing maps cleanly onto "wasted likes → sender churn," though the framework itself proposes no reciprocal-matching or allocation mechanism.

**confidence that the item is real and described correctly:** high — all three NotebookLM queries returned `sources_used` matching this source_id, with detailed, internally consistent content including named authors, a verifiable Lyft Engineering URL, and specific cited works (Chernozhukov et al. 2021; Li 2024).

---

## Project Relevance

Per NotebookLM's direct answer, this source addresses the project's experimentation-under-interference layer concretely, though not its allocation or reciprocal-scoring layers. It does NOT propose bilateral/reciprocal matching, capacity-constrained allocation algorithms, or match-spread/Gini-style ecosystem metrics — Lyft's marketplace is unilateral (riders want rides, drivers want earnings), and NotebookLM is explicit that "the paper is completely silent on bilateral preferences." What it DOES offer is directly useful: (1) region-split and switch-back experiment designs as concrete alternatives to user-level A/B tests when a treated user's outcome depends on shared, depleted resources (superstar reply capacity is exactly this kind of shared, interference-prone resource); (2) a surrogacy/AIPW methodology for causally linking a short-term "negative experience" metric (directly analogous to a dating app's "wasted likes" or "no reply received") to long-term retention, which is a ready-made template for quantifying how unreciprocated likes drive sender churn. Most useful as a source for the project's Phase 4 "market-design levers" and "experimentation under interference" layers — specifically the region-split/switch-back experimental-design pattern and the surrogacy-index technique for connecting a short-term negative signal to long-term two-sided retention.
