# Paper Analysis: Effects of Market Size and Competition in Two-Sided Markets: Evidence from Online Dating

**Source:** https://www.anderson.ucla.edu/sites/default/files/documents/areas/fac/marketing/Seminars/Fall%202018/SEARCH,%20SELECTIVITY,%20AND%20MARKET%20THICKNESS%20IN%20TWO%20SIDED%20MARKETS.pdf  
**Date analyzed:** 2026-08-19

---

## 1. Summary

**Title:** Effects of Market Size and Competition in Two-Sided Markets: Evidence from Online Dating  
**Authors:** Jessica Fong (the queried 2018 working version is titled *Search, Selectivity, and Market Thickness in Two-Sided Markets* and names Jessica Yu)  
**Abstract:** Larger dating markets do not mechanically produce more matches because users strategically change selectivity when they believe more candidates or more competitors are present. A randomized information experiment and a dynamic sequential-search model show that growth can reduce matches, while the platform's like limit strongly governs whether added thickness helps or hurts either side.

**Key contributions:**

- Randomizes beliefs about local candidate and competitor counts in a live dating app.
- Estimates a dynamic search model with finite like quotas and bilateral matching probability.
- Shows that market growth, gender gating, and like-limit changes have large, side-specific equilibrium effects.

**Methodology:** Treatment users saw independently randomized nearby male and female counts, scaled to 75%–125% of true local counts. Historical micro-level swipe logs estimate baseline beliefs; the experiment identifies selectivity responses. A finite-horizon structural model tracks profile quality, remaining likes, market size, competition, search cost, and mutual-match probability, then simulates growth and capacity policies.

**Main results:** A 50% increase in perceived market size lowers realized matches 2%, while a 50% increase in perceived competition raises them 3%. Growing both sides 25% reduces small-market matches 12.2% for men and 17.7% for women; doubling like limits reverses this to gains of 136.3% and 121.6%.

## 2. Experiment Critique

**Design:** A randomized belief intervention separates perceived market size from perceived competition without physically changing market composition. Structural counterfactuals compare two-sided growth, one-sided growth, and like-limit changes.

**Statistical validity:** The randomized reduced-form effects identify short-run belief responses. Counterfactual effect sizes rely on estimated equilibrium structure rather than randomized policy assignment; the paper's reported query output does not supply confidence intervals for all counterfactuals.

**Online experiments:** Conducted across 292 geographic grids. Of 225,680 assigned users, 84,589 were exposed; the final structural sample contains 26,092 women and 40,647 men.

**Reproducibility:** Model equations and estimation steps are described. Proprietary data, production serving logic, and replication code are not specified in source.

**Overall:** Strong causal evidence supports belief-driven selectivity. Exact market-growth and like-cap effects are model-dependent and assume immediate belief updating, random counterfactual serving, and no learning across sessions.

## 3. Industry Contribution

**Deployability:** Like caps, membership gating, and market-size information are direct product levers.

**Problems solved:** Strategic over-selectivity, visibility congestion, and market-growth policies that unintentionally lower bilateral outcomes.

**Engineering cost:** Moderate for cap and messaging experiments; high for structural estimation, equilibrium simulation, and interference-aware policy rollout.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Causally links market-thickness beliefs to individual selectivity and integrates those estimates into an equilibrium search model with proposal quotas.

**Prior work comparison:** Petrongolo and Pissarides (2001) survey aggregate matching functions; Halaburda, Piskorski, and Yıldırım (2018) theorize choice-versus-competition effects; Kanoria and Saban (2021) study action restrictions; Hitsch, Hortaçsu, and Ariely (2010) estimate static dating preferences; Lee and Niederle (2015) test signaling; Gale and Shapley (1962) omit decentralized search frictions; Bajari, Benkard, and Levin (2007) motivate two-step dynamic-game estimation.

**Verification:** The source supports the experiment and earlier title. Publication title, author surname, venue, and year follow the verified survey brief and queue.

## 5. Dataset Availability

**Datasets mentioned:**

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Historical mobile-dating logs | Not public | No | 50,000 women and 100,000 men over 34 days in 2015. |
| Randomized field experiment | Not public | No | 292 grids; final structural sample 26,092 women and 40,647 men. |
| Structural counterfactual markets | Not applicable | Reconstructable in principle | Small and large synthetic equilibrium populations. |

**Offline experiment reproducibility:** Public code, fitted parameters, and proprietary logs are not specified in source.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Exact mechanism:** Manipulate beliefs about candidate and competitor counts, and tune a finite 12-hour like quota. Market size raises expected future profile quality and selectivity; competition lowers expected visibility and relaxes selectivity. The like quota makes every outbound like a scarce resource.

**Metrics and reported effect:** Perceived market size +50% causes -2% matches; perceived competition +50% causes +3%. Two-sided growth in small markets causes -12.2% male and -17.7% female matches, while doubling like limits with growth causes +136.3% and +121.6%. Conversations and retention are not specified.

**Capacity/congestion relevance:** Like limits are explicit sender capacity. Competition enters through the probability a recipient sees the sender, `s-bar/competition size`. Receiver reply capacity is indirect, not a hard inbox or conversation cap.

**Practical mapping:** Use like limits as a market-state-dependent control, not a fixed monetization rule. Evaluate match, date, quality, and side-specific distribution effects before growing or gating one side.

**Dating fit: High.** The data, experiment, and model are built around sequential swiping and reciprocal matching on a large live dating app.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| No verified inbound mentions within the 45-source corpus. | — | — |

## Meta Information

**Authors:** Jessica Fong; queried working version names Jessica Yu  
**Affiliations:** Stanford Graduate School of Business in queried working version  
**Venue:** Marketing Science  
**Year:** 2024  
**PDF:** available (earlier working version)  
**Relevance:** Core  
**Priority:** 2

## Annotated Bibliography Fields

- **Title:** Effects of Market Size and Competition in Two-Sided Markets: Evidence from Online Dating
- **Authors/organization:** Jessica Fong; earlier working version names Jessica Yu, Stanford Graduate School of Business
- **Year:** 2024
- **Venue/type:** Marketing Science; randomized field experiment and structural model
- **Link:** https://www.anderson.ucla.edu/sites/default/files/documents/areas/fac/marketing/Seminars/Fall%202018/SEARCH,%20SELECTIVITY,%20AND%20MARKET%20THICKNESS%20IN%20TWO%20SIDED%20MARKETS.pdf
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Randomized displayed local male and female counts to causally estimate how perceived candidate supply and competition alter swiping selectivity. The author combines the experiment with historical swipe logs in a dynamic search model with finite like quotas, then simulates two-sided market growth, one-sided gender gating, and like-cap changes in small and large markets.
- **Mechanism relevant to two-sided balancing (≤50 words):** Treat market-size beliefs and like limits as coupled controls. A larger pool can induce over-selectivity and fewer matches; relaxing a scarce like quota can offset this, with sharply different effects by side and market size.
- **Metrics and reported effect:** Perceived market size +50%: matches -2%; perceived competition +50%: +3%. Small-market two-sided growth: -12.2% male and -17.7% female matches; with doubled caps: +136.3% and +121.6%.
- **Dating-app fit:** High — directly estimates strategic swiping and like-cap effects on a live reciprocal dating app.
- **Confidence:** High on source-scoped methods/results; medium-high on publication metadata because the linked PDF is a 2018 version with an earlier title and author surname.
