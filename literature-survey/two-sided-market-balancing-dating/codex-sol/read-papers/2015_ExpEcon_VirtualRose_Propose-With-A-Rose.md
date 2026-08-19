# Paper Analysis: Propose with a Rose? Signaling in Internet Dating Markets

**Source:** https://web.stanford.edu/~niederle/Lee.Niederle.Rose.ExpEcon.2015.pdf  
**Date analyzed:** 2026-08-19

---

## 1. Summary

**Title:** Propose with a Rose? Signaling in Internet Dating Markets  
**Authors:** Soohyung Lee, Muriel Niederle  
**Abstract:** A scarce, nonbinding preference signal can help recipients distinguish serious proposals in a congested dating market. A randomized field experiment on a South Korean dating platform shows that attaching a virtual rose raises acceptance and increases the total number of matches rather than merely reallocating acceptances.

**Key contributions:**

- Provides causal evidence that scarce preference signals raise proposal acceptance.
- Uses randomized rose endowments as an instrument for actual signal use.
- Measures heterogeneity by recipient desirability and documents substantial non-strategic use.

**Methodology:** In two live dating events, users could send at most ten proposals and attach at most one rose per proposal; recipients could accept up to ten. Eighty percent of users received two roses and 20% received eight. Recipient-fixed-effect regressions and an instrumental-variable design estimate the causal effect of signaling.

**Main results:** A rose raises acceptance by 3.3 percentage points, about 20% relative; the instrumental-variable estimate is 4.1 points. Eight versus two roses raises total initiated dates by 48% for fully verified Seoul men and 86% for women. Middle-tier recipients with at least one rose accepted 0.259 more proposals, a 37% increase.

## 2. Experiment Critique

**Design:** A randomized field experiment with recipient fixed effects and random rose endowment addresses selection into signaling. Baseline proposals without roses and two-rose users are explicit comparators.

**Statistical validity:** The source reports statistically significant treatment effects and uses the randomized endowment as an instrument. The bottom-tier sample is small, male assignment has observable imbalance, and the study cannot define or estimate aggregate welfare.

**Online experiments:** Two sessions in July and August 2008 involved 613 unique users, 1,921 proposals, and 295 accepted proposals/dates. Encouragement banners had no statistical effect.

**Reproducibility:** Experimental design and regressions are described; proprietary logs and replication code are not specified in source.

**Overall:** The experiment supports a causal match-formation effect and a no-crowding-out claim for a restricted subgroup, but it does not measure conversations, completed offline dates, relationships, or retention.

## 3. Industry Contribution

**Deployability:** Scarce Super-Like-style signals are simple to add to an existing proposal flow.

**Problems solved:** Recipient evaluation congestion and uncertainty about a sender's likelihood of reciprocating.

**Engineering cost:** Low for the feature; moderate for endowment policy, abuse prevention, segment-level calibration, and monitoring concentration.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First clean field-experimental evidence that a limited preference signal directly increases success and total matches in online dating.

**Prior work comparison:** Avery, Fairbanks, and Zeckhauser (2003) and Avery and Levin (2010) study early admission as a signal; Coles et al. (2010) evaluate economist-job-market signaling with observational limitations; Coles, Kushnir, and Niederle (2013) provide the central theory; Roth and Xing (1997) analyze decentralized bottlenecks; Hitsch, Hortaçsu, and Ariely (2010) establish online-dating preference context.

**Verification:** Claims are supported by the source-scoped experiment. No external community or forward-citation search was performed in this batch.

## 5. Dataset Availability

**Datasets mentioned:**

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| South Korean dating-platform field experiment | Not public | No | 613 users, 1,921 proposals, 295 accepted proposals. |
| Historical regular-member platform data | Not public | No | Used to construct and validate desirability scores. |

**Offline experiment reproducibility:** The design can be replicated, but the proprietary logs and desirability model inputs are unavailable.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Exact mechanism:** Give users a scarce allotment of virtual roses that can accompany a like. Scarcity makes the signal credible and helps recipients allocate attention to attainable, serious senders.

**Metrics and reported effect:** Acceptance +3.3 points (20% relative), IV estimate +4.1 points. Eight-rose users obtain 48% more initiated dates among fully verified Seoul men and 86% more among women. For low-volume middle-tier recipients, a rose increases accepted proposals by 0.259, or 37%.

**Capacity/congestion relevance:** Senders and recipients each face ten-proposal limits. Signaling prioritizes attention but does not change profile exposure. Thirty-two percent of men and 69% of women left roses unused, and about 30% of roses were wasted on top-tier recipients who did not respond.

**Practical mapping:** Roses map directly to Super Likes or priority likes. A production system could vary allotments or surface signals prominently, while guarding against over-signaling to already congested profiles.

**Dating fit: High.** This is a randomized experiment on a reciprocal dating platform with explicit proposal and acceptance limits.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| [2024_MarketingScience_SequentialSearch_Effects-Market-Size-Competition.md](./2024_MarketingScience_SequentialSearch_Effects-Market-Size-Competition.md) | Novelty vs. Prior Work — Background | Cites Lee and Niederle (2015) as a signaling test. |

## Meta Information

**Authors:** Soohyung Lee, Muriel Niederle  
**Affiliations:** University of Maryland; Stanford University  
**Venue:** Experimental Economics  
**Year:** 2015  
**PDF:** available  
**Relevance:** Core  
**Priority:** 2

## Annotated Bibliography Fields

- **Title:** Propose with a Rose? Signaling in Internet Dating Markets
- **Authors/organization:** Soohyung Lee, Muriel Niederle
- **Year:** 2015
- **Venue/type:** Experimental Economics; randomized dating-platform field experiment
- **Link:** https://web.stanford.edu/~niederle/Lee.Niederle.Rose.ExpEcon.2015.pdf
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Randomized 613 users on a South Korean dating platform to receive two or eight scarce virtual roses. Users attached roses to proposals, and recipients saw the signal before accepting. Recipient-fixed-effect and instrumental-variable analyses estimate causal acceptance effects, while treatment-level outcomes test whether signaling expands matches or merely reallocates them.
- **Mechanism relevant to two-sided balancing (≤50 words):** A scarce priority signal communicates serious interest and attainability, helping capacity-limited recipients allocate evaluation effort. It coordinates decentralized proposals without centrally changing exposure.
- **Metrics and reported effect:** Rose acceptance +3.3 percentage points (20% relative; IV +4.1). Eight versus two roses raised total initiated dates 48% for verified Seoul men and 86% for women. Conversations and retention were not measured.
- **Dating-app fit:** High — the intervention and outcome funnel directly match limited likes, mutual acceptance, and Super-Like-style signaling.
- **Confidence:** High — source-scoped randomized field evidence and bibliographic metadata are explicit.
