# Paper Analysis: Your Looks and Your Inbox

**Source:** https://gwern.net/doc/psychology/okcupid/yourlooksandyourinbox.html  
**Date analyzed:** 2026-08-19

---

## 1. Summary

**Title:** Your Looks and Your Inbox  
**Authors:** Christian Rudder / OkCupid  
**Abstract:**  
This OkTrends analysis compares OkCupid photo ratings, message distributions, and reply behavior. It documents strong attention concentration on highly rated users and an inverse relationship between inbox volume and reply propensity.

**Key contributions:**
- Quantifies gender-specific rating and messaging distributions.
- Shows that popular recipients receive much more attention but reply less often.
- Supplies direct behavioral evidence of receiver-side congestion, without proposing an allocation intervention.

**Methodology:**  
Descriptive analysis of hundreds of millions of interactions from a platform with 3.5 million active members. Photo ratings use a 0–5 scale; message and reply rates are segmented by attractiveness. Spam is reportedly controlled, but the filter is not described.

**Main results:**  
Two-thirds of male messages go to the top third of women. The most attractive women receive nearly 5× the messages of a typical woman and 28× those of women at the low end; the most attractive men receive 11× the messages of the lowest-rated men. Highly attractive users reply less often.

---

## 2. Experiment Critique

**Design:**  
Large-scale observational platform-log analysis, but no experimental control, causal identification, model baseline, or adjustment for age, ethnicity, profile text, and other confounders is reported.

**Statistical validity:**  
The source gives ratios and distributional comparisons but no subgroup sample sizes, confidence intervals, standard errors, significance tests, or effect-size uncertainty. Ratings are explicitly unnormalized.

**Online experiments (if any):**  
Not specified in source.

**Reproducibility:**  
No dataset, code, query definitions, spam-filter specification, or complete aggregation procedure is released.

**Overall:**  
The logs strongly support the descriptive claim that attention is concentrated and popular recipients reply less. They do not establish that exposure redistribution would increase matches, conversations, or retention.

---

## 3. Industry Contribution

**Deployability:**  
Useful as a low-cost ecosystem diagnostic: reproduce attractiveness-decile message shares, inbox-volume curves, and reply-rate curves on current logs.

**Problems solved:**  
Identifies oversubscription and wasted sender effort that a single-viewer relevance metric would miss.

**Engineering cost:**  
Low for measurement; the source specifies no production scoring or re-ranking method.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
Quantifies how perceived looks relate to incoming attention and outgoing-message success on OkCupid.

**Prior work comparison:**  
Not specified in source; the original post cites no scientific prior work.

**Verification:**  
The quantitative claims are supported by the indexed OkTrends source, but external replication and causal verification are not provided.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| OkCupid interaction logs | Not specified in source | No | Hundreds of millions of interactions; 3.5M active-member platform scale |

**Offline experiment reproducibility:**  
Not reproducible from public artifacts; raw logs and aggregation details are unavailable.

---

## 6. Community Reaction

Not specified in source.

---

## Project Relevance

**Mechanism:** Ecosystem measurement, not a recommender: compare attractiveness strata with message concentration and reply-rate decay.  
**Metrics/effect:** Two-thirds of men's messages go to the top third of women; top women receive nearly 5× a typical woman's messages and 28× the low end; top men receive 11× the lowest-rated men.  
**Capacity/congestion:** Indirectly evidenced. Popular recipients reply less because their inboxes are fuller, but no capacity constraint or intervention is modeled.  
**Dating-app fit:** **Medium** — direct dating-market evidence of congestion, but no tested balancing mechanism.  
**Strict implication:** Monitor attention concentration and reply-rate decay by receiver-demand bucket before treating predicted attractiveness as a ranking objective. The source does not establish a specific exposure cap.

## Annotated Bibliography Fields

**Citation:** Christian Rudder / OkCupid. 2009. *Your Looks and Your Inbox*. OkTrends company blog. https://gwern.net/doc/psychology/okcupid/yourlooksandyourinbox.html. **Tier 1.**  
**What they did (≤80 words):** Analyzed OkCupid photo ratings, message volumes, and reply patterns to quantify how perceived attractiveness shapes user attention. The post compares gender-specific rating curves with actual messaging and reports inbox-volume multiples across attractiveness strata.  
**Two-sided mechanism (≤50 words):** A market-health diagnostic for demand concentration and receiver congestion: segment attention and reply propensity by recipient attractiveness to reveal where additional messages have diminishing reciprocal value.  
**Metrics and reported effect:** Message share, inbox-volume ratios, and reply rates; 66% of male messages target the top 33% of women, while heavily messaged users reply less.  
**Dating-app fit:** **Medium** — strong direct evidence, no intervention.  
**Confidence:** **High** that the item and reported figures match the indexed primary source; causal interpretation is low confidence.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| No verified inbound mentions within the 45-source corpus. | — | — |

---

## Meta Information

**Authors:** Christian Rudder  
**Affiliations:** OkCupid / Humor Rainbow, Inc.  
**Venue:** OkTrends company blog  
**Year:** 2009  
**PDF:** unavailable — web article  
**Relevance:** Core  
**Priority:** 1

---
