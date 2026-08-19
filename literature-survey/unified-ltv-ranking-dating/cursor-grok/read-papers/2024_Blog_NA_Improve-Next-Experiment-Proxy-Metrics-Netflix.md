# Paper Analysis: Improve Your Next Experiment by Learning Better Proxy Metrics From Past Experiments

**Source:** https://netflixtechblog.com/improve-your-next-experiment-by-learning-better-proxy-metrics-from-past-experiments-64c786c2a3ac
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** Improve Your Next Experiment by Learning Better Proxy Metrics From Past Experiments
- **authors or company:** Aurélien Bibaut, Winston Chou, Simon Ejdemyr, Nathan Kallus (Netflix)
- **venue:** Netflix TechBlog
- **year:** 2024
- **URL:** https://netflixtechblog.com/improve-your-next-experiment-by-learning-better-proxy-metrics-from-past-experiments-64c786c2a3ac
- **source type:** blog
- **direction:** D3
- **problem setting:** Netflix A/B tests can measure sensitive short-term proxies (clicks, engagement) but not noisy delayed north stars (retention, long-term revenue). Independent product teams each invent secondary metrics; the company needs a linear proxy index that tracks the north star across thousands of experiments per year.
- **objective and label definition:** Proxy vector \(S\) (short-term, e.g. CTR or engagement) vs north-star \(Y\) (retention / long-term revenue). Horizon of \(Y\) is not given as a fixed day count; blog example contrasts click-through with “long-term retention.” Delay handling is statistical (experiment-level treatment-effect covariance), not per-impression censoring.
- **prediction or incrementality:** Incrementality of **policies / treatments**, not of a single exposure. Target is covariance of *true* treatment effects \(\mathrm{Cov}(\tau_S, \tau_Y)\), not user-level \(\mathrm{Corr}(S,Y)\) and not OLS on estimated effects (both are stated to be biased).
- **model architecture:** Three estimators of the proxy/north-star slope: Total Covariance (TC) under homogeneous measurement-error covariances; Jackknife Instrumental Variables (JIVE) without that assumption; LIML (efficient only if \(S\) fully mediates effects on \(Y\); authors recommend against LIML for most applications). Output is a linear structural model of treatment effects used as a composite proxy.
- **credit assignment:** Not an item-level ranker. Mapping is experiment → estimated treatment effects on \(S\) and \(Y\). No user-level delayed outcome mapped to one recommended title.
- **training data and counterfactual handling:** Historical A/B tests as data points. Subtracts scaled unit-level sampling covariance from the covariance of estimated treatment effects so correlated measurement error does not masquerade as a causal \(S\to Y\) slope. More experiments do **not** fix OLS bias; more units per experiment (or TC/JIVE) do.
- **offline and online evaluation:** Methods “actively used to develop proxy metrics at Netflix.” Blog does not report a numeric online lift. Companion KDD 2024 paper (Learning the Covariance of Treatment Effects Across Many Weak Experiments) is the formalization; a later decision-rule paper reports ~33% higher cumulative returns after adopting a new proxy/rule (that number is **not in this blog**).
- **reported gains:** Not specified in this source (process and estimator description only).
- **applicability note for a two-sided dating recommender:** Direct recipe for a launch gate: learn weights that map 14-day like/match/reply/D7 onto 30/63-day retention and 28-day revenue from historical ranking A/Bs, instead of correlating user-level CTR with retention.
  Dating A/Bs violate SUTVA via a shared candidate pool; this blog assumes experiment-level treatment effects under standard user splits and does not address two-sided interference.
- **unverified claims:** Companion-paper cumulative-return figure (~33%) is not stated in this blog.

## 1. Summary

**Title:** Improve Your Next Experiment by Learning Better Proxy Metrics From Past Experiments
**Authors:** Aurélien Bibaut, Winston Chou, Simon Ejdemyr, Nathan Kallus (Netflix)
**Venue:** Netflix TechBlog, 2024 (companion to KDD 2024)

**Abstract:** Netflix explains why user-level \(S\)–\(Y\) correlations and OLS on estimated A/B effects both fail as proxy-metric learners, then describes TC / JIVE / LIML estimators that recover the covariance of true treatment effects from many weak experiments.

**Key contributions:**
- States the clickbait trap: positive user-level CTR–retention correlation can coexist with a negative true treatment-effect slope.
- Shows OLS on estimated effects is biased by correlated measurement error; adding more experiments does not remove the bias.
- Recommends TC or JIVE for production proxy construction; LIML only under full mediation.

**Methodology:** Meta-analysis of historical A/B tests; linear models of treatment effects as the coordination device across decentralized metric owners.

**Main results:** Qualitative. Methods in active use on Netflix’s experimentation platform. Numeric lifts not specified in this blog.

## 2. Experiment Critique

**Design:** Methodology post pointing at a KDD 2024 paper; illustrative covariance-matrix figure (true slope negative, sampling covariance positive, estimated-effect OLS flat).

**Statistical validity:** Argument is theoretical plus industrial adoption; no holdout table in the blog.

**Online experiments:** Implied by “actively used”; no A/B of the proxy learner itself reported here.

**Reproducibility:** Estimators named; implementation details deferred to the paper.

**Overall:** Strong conceptual warning for any team that would validate a D7 surrogate by correlating it with D30 among users. Does not itself ship a ranking model.

## 3. Industry Contribution

**Deployability:** Explicitly designed for a company that runs thousands of experiments with independent DS teams sharing one north star.

**Problems solved:** Coordinating metric tradeoffs; stopping wasted metric innovation that is collinear with existing proxies; letting teams iterate without waiting for long-horizon Y.

**Engineering cost:** Needs a catalog of historical experiment treatment-effect estimates plus unit-level sampling covariances. Blog notes Netflix still lacks a fully flexible data architecture for this.

## 4. Novelty vs. Prior Work

**Claimed novelty:** Weak-IV-inspired estimators for treatment-effect covariance across many small digital experiments.

**Prior work named in source:** Introductory causal-inference confounding; OLS / scatterplot of estimated effects; KDD 2024 companion paper.

**Verification:** Same technical content as Tripuraneni/Bibaut et al. industry line already in this survey (Choosing a Proxy Metric; Learning the Covariance…). This card is the **engineering-blog** source the brief asked to search.

## 5. Dataset Availability

| Dataset | Accessible | Notes |
|---------|------------|-------|
| Netflix historical A/B catalog | No | Proprietary |
| Stylized covariance figure | Yes (in post) | Hypothetical, not a public dataset |

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

Eval-layer, not a ranker. Answers Q6: do **not** treat user-level like→retention correlation as evidence that ranking for likes will raise D30. Fit a surrogate from historical ranking experiments with TC/JIVE. Does **not** put incrementality inside the serving formula.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information
**Authors:** Aurélien Bibaut, Winston Chou, Simon Ejdemyr, Nathan Kallus
**Affiliations:** Netflix
**Venue:** Netflix TechBlog
**Year:** 2024
**PDF:** https://netflixtechblog.com/improve-your-next-experiment-by-learning-better-proxy-metrics-from-past-experiments-64c786c2a3ac
**Relevance:** Core
**Priority:** 1
