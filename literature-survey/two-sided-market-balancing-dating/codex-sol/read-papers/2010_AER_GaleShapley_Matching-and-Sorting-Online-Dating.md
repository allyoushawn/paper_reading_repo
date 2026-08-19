# Paper Analysis: Matching and Sorting in Online Dating

**Source:** https://people.duke.edu/~dandan/webfiles/PapersUpside/Matching%20and%20Sorting%20Dating.pdf  
**Date analyzed:** 2026-08-19

---

## 1. Summary

**Title:** Matching and Sorting in Online Dating  
**Authors:** Günter J. Hitsch, Ali Hortaçsu, and Dan Ariely  
**Abstract:**  
The paper estimates mate preferences from profile browsing and first-contact behavior on a decentralized dating site, then uses Gale-Shapley matching as an equilibrium benchmark. It finds that heterogeneous preferences can reproduce observed sorting and that decentralized matches are approximately efficient relative to the simulated stable-matching benchmark.

**Key contributions:**
- Estimates horizontal and vertical mate preferences from observed choice sets.
- Tests whether rejection costs materially change whom users contact.
- Benchmarks realized matching against Gale-Shapley stable assignments.

**Methodology:**  
Person fixed-effects logit preference models, reply-probability correction with 250 bootstrap replications, Adachi two-sided search foundations, and deferred-acceptance simulations with counterfactual preference specifications.

**Main results:**  
Male- and female-initiated first contacts convert to matches at 4.3% and 6.4%; 71% and 56% receive no reply. Rejection-cost coefficients are small and insignificant. Observed and simulated sorting are close on several attributes, though education and race are underpredicted offline.

---

## 2. Experiment Critique

**Design:**  
Rich clickstream data expose browses, contacts, replies, and estimated matches. Gale-Shapley and counterfactual preferences provide meaningful benchmarks, but the study is observational and the match proxy is exchanged contact information, not verified dates or relationships.

**Statistical validity:**  
Fixed effects, clustered/bootstrapped uncertainty, and large interaction samples are strengths. Unobserved chemistry, self-reported traits, and model identification choices materially affect the equilibrium comparison.

**Online experiments (if any):**  
Not specified in source.

**Reproducibility:**  
The structural specification is detailed, but proprietary logs and random-utility simulation inputs are unavailable. The paper reports 250 bootstrap replications.

**Overall:**  
The results support preference heterogeneity and approximate decentralized efficiency in this 2003 web setting. They do not validate modern feed allocation or receiver-capacity controls.

---

## 3. Industry Contribution

**Deployability:**  
Most useful as an offline market benchmark: estimate bilateral preferences, simulate stable matches, and compare achieved match ranks.

**Problems solved:**  
Separates preference-driven sorting from search frictions and quantifies unrequited outreach and match conversion.

**Engineering cost:**  
High: pairwise utility estimation and large-market stable-matching simulations; assumptions require careful validation.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
Links detailed online choice sets and first contacts to structural two-sided search and stable-matching outcomes.

**Prior work comparison:**  
Builds on Adachi (2003), Gale and Shapley (1962), Becker (1973), Roth and Sotomayor (1990), Choo and Siow (2006), Wong (2003), and Laumann et al. It contrasts decentralized outcomes with a centralized stable-match benchmark.

**Verification:**  
The primary source supports these links; no external novelty search was performed in this batch.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Dating-site clickstream, Boston/San Diego, 2003 | Not specified in source | No | 3,004 men; 2,783 women; 385,470 male and 172,946 female browses |
| 2000 Census IPUMS 5% sample | https://usa.ipums.org/usa/ | Restricted/registered | Offline marriage comparison |
| NSFG Cycle 6 | Not specified in source | Yes | Correlation comparison |
| NHANES 1988–1994 | https://www.cdc.gov/nchs/nhanes/ | Yes | Anthropometric benchmark |

**Offline experiment reproducibility:**  
Public comparison data are available, but the proprietary dating clickstream prevents full reproduction.

---

## 6. Community Reaction

Not specified in source.

---

## Project Relevance

**Mechanism:** Structural bilateral preference estimation plus Gale-Shapley as an ecosystem-efficiency benchmark; no production reciprocal ranker is proposed.  
**Metrics/effect:** 71% of male and 56% of female first contacts receive no reply; 4.3% and 6.4% convert to matches; median pre-match exchange is six emails.  
**Capacity/congestion:** Actual email sending is unlimited and receiver capacity is not modeled; one-partner capacity exists only in the stable-assignment simulation.  
**Dating-app fit:** **Medium** — strong empirical benchmark, dated interface and no capacity-aware exposure allocation.  
**Strict implication:** Compare current achieved-match ranks with a stable-matching simulation only as a diagnostic, and separately measure inbox congestion because this model does not represent receiver screening capacity.

## Annotated Bibliography Fields

**Citation:** Günter J. Hitsch, Ali Hortaçsu, and Dan Ariely. 2010. *Matching and Sorting in Online Dating*. American Economic Review 100(1). https://people.duke.edu/~dandan/webfiles/PapersUpside/Matching%20and%20Sorting%20Dating.pdf. **Tier 2.**  
**What they did (≤80 words):** Estimated mate preferences from a 2003 dating-site clickstream, tested strategic selectivity, simulated Gale-Shapley matches, and compared observed online sorting and reweighted offline marriage patterns with stable-matching predictions.  
**Two-sided mechanism (≤50 words):** Uses estimated preferences and deferred acceptance to benchmark platform-wide sorting and achieved partner ranks; the correction for predicted reply probability tests whether rejection risk changes proposals.  
**Metrics and reported effect:** Reply, contact-to-match conversion, match-rank distance, and attribute correlation; 71%/56% of male/female contacts are unrequited and 4.3%/6.4% become matches.  
**Dating-app fit:** **Medium** — rigorous market benchmark, not modern capacity control.  
**Confidence:** **High** for source identity and reported study results.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| [2015_ExpEcon_VirtualRose_Propose-With-A-Rose.md](./2015_ExpEcon_VirtualRose_Propose-With-A-Rose.md) | Novelty vs. Prior Work — Background | Cites Hitsch, Hortaçsu, and Ariely (2010) as online-dating preference context. |
| [2018_SciAdv_PageRank_Aspirational-Pursuit-of-Mates.md](./2018_SciAdv_PageRank_Aspirational-Pursuit-of-Mates.md) | Novelty vs. Prior Work — Background | Lists Hitsch et al. among central prior works. |
| [2024_MarketingScience_SequentialSearch_Effects-Market-Size-Competition.md](./2024_MarketingScience_SequentialSearch_Effects-Market-Size-Competition.md) | Novelty vs. Prior Work — Background | Cites Hitsch, Hortaçsu, and Ariely (2010) as static dating-preference estimates. |
| [2026_arXiv_ECDA_Predictive-Models-Two-Sided-Recommendations.md](./2026_arXiv_ECDA_Predictive-Models-Two-Sided-Recommendations.md) | Novelty vs. Prior Work — Background | Cites Hitsch, Hortaçsu, and Ariely (2010) as modeling online dating. |

---

## Meta Information

**Authors:** Günter J. Hitsch; Ali Hortaçsu; Dan Ariely  
**Affiliations:** University of Chicago; Duke University  
**Venue:** American Economic Review  
**Year:** 2010  
**PDF:** available  
**Relevance:** Core  
**Priority:** 2

---
