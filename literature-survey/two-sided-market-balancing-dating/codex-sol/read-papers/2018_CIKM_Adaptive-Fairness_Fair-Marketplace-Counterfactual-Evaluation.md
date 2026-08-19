# Paper Analysis: Towards a Fair Marketplace: Counterfactual Evaluation of the Trade-off between Relevance, Fairness & Satisfaction in Recommendation Systems

**Source:** https://rishabhmehrotra.com/papers/CIKM2018-marketplace-mehrotra.pdf  
**Date analyzed:** 2026-08-18

---

## 1. Summary

**Title:** Towards a Fair Marketplace: Counterfactual Evaluation of the Trade-off between Relevance, Fairness & Satisfaction in Recommendation Systems  
**Authors:** Rishabh Mehrotra, James McInerney, Hugues Bouchard, Mounia Lalmas, Fernando Diaz  
**Abstract:** The paper studies how a marketplace recommender can balance consumer relevance, consumer satisfaction, and supplier exposure fairness. It defines a popularity-bin fairness score, evaluates global and personalized policies, and uses inverse-propensity scoring on randomized Spotify logs to estimate outcomes offline.

**Key contributions:**

- A supplier group-fairness metric with diminishing returns for repeated exposure within the same popularity bin.
- Interpolated, probabilistic, guaranteed-relevance, and user-adaptive relevance/fairness policies.
- Counterfactual policy evaluation with inverse-propensity scoring from randomized exposure logs.

**Methodology:** Relevance is cosine similarity in a joint user/track embedding space. Supplier fairness is computed over ten artist-popularity bins with a square-root term that rewards coverage and diminishing returns. Adaptive-I selects a relevance-only or fairness-only policy using each user's historical fairness affinity; Adaptive-II continuously interpolates the two objectives. Policy value is estimated from randomized production logs with inverse-propensity weighting.

**Main results:** On more than 400,000 Spotify users, 5,000 playlists, and 49,000 artists, relevance-only satisfaction is 0.650 and fairness-only satisfaction is 0.420. Adaptive-I reaches 0.709 (+9.0%), and Adaptive-II reaches 0.729 (+12.1%), relative to the relevance-only baseline. The paper also finds a region of the global trade-off where additional fair exposure has little satisfaction cost.

## 2. Experiment Critique

**Design:** The randomized logging policy supports counterfactual evaluation, and relevance-only and fairness-only policies are clear anchors. The paper compares multiple policy families rather than only one proposed setting.  
**Statistical validity:** It reports paired t-tests for some comparisons and statistically significant adaptive-policy satisfaction gains. Exact p-values, confidence intervals, and variance for the headline satisfaction estimates are not specified in source.  
**Online experiments (if any):** Data came from production traffic during two weeks in November 2017, but the evaluated policies were assessed counterfactually rather than in disclosed live treatment-vs-control deployments.  
**Reproducibility:** Spotify data are proprietary. Code, random seeds, exact train/validation/test splits, and several affinity thresholds are not specified in source.  
**Overall:** The randomized logs make the offline comparisons substantially stronger than ordinary observational replay. The key external-validity limit for dating is that artists are passive suppliers and have neither reciprocal choice nor reply capacity.

## 3. Industry Contribution

**Deployability:** High as a post-ranking or set-selection objective when randomized exploration logs with propensities are available.  
**Problems solved:** Exposure concentration, superstar economics, and heterogeneous consumer tolerance for supplier-side fairness.  
**Engineering cost:** Requires propensity-logged exploration, supplier popularity cohorts, satisfaction measurement, and either constrained or multi-objective candidate-set selection.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Joint counterfactual evaluation of relevance, supplier fairness, and satisfaction, including personalized adaptive policies.  
**Prior work comparison:** The paper builds on Rosen's *The Economics of Superstars*, Li et al.'s contextual-bandit evaluation, Horvitz–Thompson inverse-propensity estimation, Singh and Joachims' *Fairness of Exposure in Rankings*, Burke's *Multisided Fairness for Recommendation*, and Li et al.'s counterfactual search-metric evaluation.  
**Verification:** Source-scoped extraction supports the claimed distinctions; no independent web novelty check was performed in this batch.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Spotify randomized production logs | Not specified in source. | No | >400,000 users, 5,000 playlists, >49,000 artists; two weeks in Nov. 2017 |

**Offline experiment reproducibility:** Limited by proprietary data and missing code/seeds; the policy definitions and inverse-propensity estimator are described.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Mechanism.** The popularity-bin objective and adaptive interpolation are directly useful for spreading exposure away from superstar profiles without imposing the same diversification level on every viewer.  
**Metrics/effect.** Adaptive-I and Adaptive-II improve estimated satisfaction by 9.0% and 12.1% over relevance-only; fairness-only loses 35% satisfaction. Total matches, conversations, match spread, wasted likes, and two-sided retention are **Not specified in source.**  
**Capacity/congestion.** Exposure concentration is modeled, but reply capacity, inbox congestion, and feedback loops are **Not specified in source.**  
**Dating mapping.** Medium fit: map artist popularity bins to shown-user popularity or responsiveness cohorts and condition the fairness weight on the viewer, but combine this with reciprocal like-back probability and capacity constraints. Treat the dating mapping as an application inference, not a source claim.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| [2022_SIGIR_JME_Joint-Multisided-Exposure-Fairness.md](./2022_SIGIR_JME_Joint-Multisided-Exposure-Fairness.md) | Novelty vs. Prior Work — Extension | States the paper extends Mehrotra et al.'s fair-marketplace evaluation. |

## Meta Information

**Authors:** Rishabh Mehrotra, James McInerney, Hugues Bouchard, Mounia Lalmas, Fernando Diaz  
**Affiliations:** Spotify Research; Microsoft Research (work conducted at Spotify)  
**Venue:** CIKM 2018  
**Year:** 2018  
**PDF:** available  
**Relevance:** Core  
**Priority:** 1

## Annotated Bibliography Fields

- **Title:** Towards a Fair Marketplace: Counterfactual Evaluation of the Trade-off between Relevance, Fairness & Satisfaction in Recommendation Systems
- **Authors/organization:** Rishabh Mehrotra, James McInerney, Hugues Bouchard, Mounia Lalmas, Fernando Diaz; Spotify Research / Microsoft Research
- **Year:** 2018
- **Venue/type:** CIKM; conference paper
- **Link:** https://rishabhmehrotra.com/papers/CIKM2018-marketplace-mehrotra.pdf
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Defined a supplier popularity-bin fairness objective, proposed global and user-adaptive policies that trade relevance against fair exposure, and evaluated them offline with inverse-propensity scoring on randomized Spotify production logs.
- **Mechanism relevant to two-sided balancing (≤50 words):** Use diminishing returns across supplier-popularity bins, plus a viewer-specific fairness affinity, to redirect some impressions from superstar suppliers toward the long tail while protecting consumer satisfaction.
- **Metrics and reported effect:** Satisfaction proxy = tracks listened to. Adaptive-I: 0.709, +9.0%; Adaptive-II: 0.729, +12.1% versus relevance-only 0.650. Fairness-only: 0.420, 35% below relevance-only. Dating market-health effects not specified.
- **Dating-app fit:** Medium — strong exposure-control and offline-evaluation pattern, but no reciprocity or capacity.
- **Confidence:** High — peer-reviewed industry paper with production randomized logs; transfer to dating is inferential.
