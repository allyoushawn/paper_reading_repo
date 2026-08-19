# Paper Analysis: Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization

**Source:** https://business.columbia.edu/sites/default/files-efs/citation_file_upload/holtz-et-al-2024-reducing-interference-bias-in-online-marketplace-experiments-using-cluster-randomization-evidence-from%20(2).pdf  
**Date analyzed:** 2026-08-19

---

## 1. Summary

**Title:** Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization: Evidence from a Pricing Meta-Experiment on Airbnb  
**Authors:** David Holtz, Felipe Lobel, Ruben Lobel, Inessa Liskovich, Sinan Aral  
**Abstract:** Individual listing randomization is biased when substitutable marketplace listings compete for demand. The authors cluster listings by search-session co-occurrence, randomize entire clusters, and validate the design in a 2.6-million-listing Airbnb pricing meta-experiment.

**Key contributions:**

- Proves cluster randomization reduces treatment-effect bias under uniform demand shifts.
- Builds demand-similarity clusters from listing embeddings and recursive partitioning.
- Quantifies interference bias by randomizing clusters between individual- and cluster-randomized experiment regimes.

**Methodology:** A 16-dimensional skip-gram demand embedding is trained from listing sequences viewed in search sessions. Recursive partitioning creates clusters of roughly 1,000 listings. A meta-experiment assigns 25% of clusters to individual listing randomization and 75% to cluster-level randomization; within each arm, half receive a guest-fee increase and half a decrease.

**Main results:** Individual randomization estimates -0.345 bookings per listing, while cluster randomization estimates -0.277. Their -0.068 interaction difference (standard error 0.018) implies at least 19.76% of the naive effect is interference bias. Both main effects and the interaction are significant at the 99% level.

## 2. Experiment Critique

**Design:** The experiment-over-experiments directly compares randomization regimes on the same platform, and blocking improves balance. Cluster construction uses observed demand similarity, but true interference is unobserved.

**Statistical validity:** The sample includes 2,602,782 listings and 5,960 clusters. Main estimates report standard errors and 99% significance. Subgroup differences by market balance and cluster quality are suggestive but not significant.

**Online experiments:** Five-day live Airbnb experiment, March 16–21, 2019: 647,377 listings in the individual arm and 1,955,405 in the cluster arm.

**Reproducibility:** Exact fee changes, tenure cutoffs, and unscaled outcomes cannot be disclosed; outcomes are multiplied by a random constant. The proprietary embedding data are unavailable.

**Overall:** Strong field evidence establishes economically meaningful interference bias for this pricing intervention. Power loss, proxy-cluster assumptions, short duration, and theoretical guarantees limited to uniform demand shifts constrain generalization.

## 3. Industry Contribution

**Deployability:** Applicable when competitive units can be grouped from historical co-view or substitution data and assigned consistently.

**Problems solved:** Treatment leakage between substitutes that inflates or attenuates marketplace A/B effects.

**Engineering cost:** High: embedding pipelines, cluster maintenance, cluster-aware assignment, and much larger sample requirements.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** A formal cluster-quality criterion plus a platform-scale meta-experiment directly measuring marketplace interference bias.

**Prior work comparison:** Blake and Coey (2014) and Fradkin (2015) describe marketplace test-control interference; Ugander et al. (2013), Eckles et al. (2017), and Saveski et al. (2017) develop graph-cluster and meta-experiment methods; Johari et al. (2022) analyzes two-sided bias; Bojinov et al. (2022) studies switchbacks.

**Verification:** Limited to prior works named by the source.

## 5. Dataset Availability

**Datasets mentioned:**

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Airbnb pricing meta-experiment | Not public | No | 2,602,782 listings; five days; proprietary treatment details scaled or withheld. |
| Airbnb search-session co-view data | Not public | No | Used for 16-dimensional listing embeddings and 5,960 clusters. |

**Offline experiment reproducibility:** Not reproducible without proprietary logs, cluster construction inputs, and unscaled outcomes.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Exact mechanism:** Cluster profiles that compete for the same viewers using co-view embeddings, then randomize whole clusters so substitutes share assignment and spillover leakage is reduced.

**Metrics and reported effect:** Bookings per listing. Individual randomization estimates -0.345 versus -0.277 under clusters; the -0.068 interaction (SE 0.018) attributes 19.76% of the naive estimate to interference bias.

**Capacity/congestion relevance:** The design captures substitution between profiles competing for demand, but it does not model receiver reply limits, reciprocal acceptance, or inbox congestion.

**Practical mapping:** Create dating-market clusters from overlapping viewer consideration sets or reciprocal-candidate neighborhoods. Cluster randomization may yield cleaner ecosystem estimates, but cross-cluster browsing and dense popular-user overlap can erode isolation.

**Dating fit: Medium.** Competitive exposure spillovers transfer, while Airbnb's unilateral inventory choice does not.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| No verified inbound mentions within the 45-source corpus. | — | — |

## Meta Information

**Authors:** David Holtz, Felipe Lobel, Ruben Lobel, Inessa Liskovich, Sinan Aral  
**Affiliations:** UC Berkeley; Airbnb; MIT  
**Venue:** Management Science  
**Year:** 2025  
**PDF:** available  
**Relevance:** Core  
**Priority:** 2

## Annotated Bibliography Fields

- **Title:** Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization: Evidence from a Pricing Meta-Experiment on Airbnb
- **Authors/organization:** David Holtz, Felipe Lobel, Ruben Lobel, Inessa Liskovich, Sinan Aral
- **Year:** 2025
- **Venue/type:** Management Science; marketplace field meta-experiment
- **Link:** https://business.columbia.edu/sites/default/files-efs/citation_file_upload/holtz-et-al-2024-reducing-interference-bias-in-online-marketplace-experiments-using-cluster-randomization-evidence-from%20(2).pdf
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Embedded Airbnb listings from search-session co-views, recursively clustered close substitutes, and ran an experiment over experimental designs. Clusters were assigned either to ordinary listing-level randomization or to cluster-level randomization, enabling a direct estimate of how much a guest-fee experiment's measured booking effect was distorted by competitive spillovers.
- **Mechanism relevant to two-sided balancing (≤50 words):** Put profiles competing for the same viewers in one assignment cluster so treatment does not leak through substitution across experimental cells. Compare cluster- and individual-level estimates to quantify residual interference.
- **Metrics and reported effect:** Individual versus cluster estimates were -0.345 and -0.277 bookings per listing; the -0.068 interaction (SE 0.018) implies 19.76% interference bias.
- **Dating-app fit:** Medium — co-view competition transfers, but reciprocal choice and reply capacity are unmodeled.
- **Confidence:** High — peer-reviewed, source-scoped platform meta-experiment; proprietary scaling limits replication.
