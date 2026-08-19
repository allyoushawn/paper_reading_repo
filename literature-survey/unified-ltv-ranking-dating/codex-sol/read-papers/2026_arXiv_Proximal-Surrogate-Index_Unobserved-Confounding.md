# Paper Analysis: The Proximal Surrogate Index

**Source:** https://arxiv.org/abs/2601.17712  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** The Proximal Surrogate Index: Long-Term Treatment Effects under Unobserved Confounding  
**Authors:** Ting-Chih Hung; Yu-Chang Chen  
**Abstract:** The paper identifies long-term treatment effects by combining an experiment that has treatment and short-term surrogates but lacks the long-term outcome with an observational sample that has surrogates and the long-term outcome but lacks treatment. Proxy variables adjust unobserved confounding.  
**Methodology:** Outcome-bridge functions impute long-term outcomes into the experiment; surrogate-bridge functions reweight observational data to experimental treatment arms. Their combination yields a multiply robust cross-fitted DML estimator with an efficient influence function.  
**Main results:** In a Job Corps application, proximal estimates closely recover held-out experimental long-term benchmarks in designs where the standard surrogate index is biased; exact numerical errors are not specified in the indexed content.

## 2. Experiment Critique

**Design:** Nonparametric identification theorems, robustness/efficiency theory, cross-fitted estimation, and a semi-synthetic/empirical Job Corps benchmark against observed experimental long-term effects.  
**Statistical validity:** Provides consistency, asymptotic normality, multiply robust conditions, variance estimation, and the semiparametric efficiency bound. Validity rests on strong proxy completeness/bridge existence and no direct treatment effect outside the surrogates.  
**Online experiments:** Not applicable; uses existing randomized and observational samples.  
**Reproducibility:** Estimator theory is detailed; code/data links are not specified in the indexed source.  
**Overall:** Rigorous solution to a difficult long-term proxy problem, but demanding proxy and exclusion assumptions may be hard to defend in product systems.

## 3. Industry Contribution

**Deployability:** Enables earlier long-term effect estimation by joining short experimental outcomes to mature observational outcomes without observing treatment in the latter.  
**Problems solved:** Unobserved treatment-outcome or surrogate-outcome confounding that invalidates standard surrogate-index comparability/surrogacy.  
**Engineering cost:** Two compatible samples, outcome- and treatment-inducing proxies, nuisance bridge estimation, cross-fitting, overlap checks, and sensitivity analysis.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Proximal identification and multiply robust efficient estimation for a two-sample surrogate setting with complementary missing treatment/outcome variables.  
**Prior work comparison:** Generalizes Athey et al.'s surrogate index and adapts proximal causal inference/front-door intuition to missing-variable data combination.  
**Verification:** Indexed source only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| Job Corps evaluation | Not specified in source. | Not specified | Experimental benchmark and constructed observational/experimental samples. |

**Offline experiment reproducibility:** Not specified in source.

## 6. Community Reaction

Not specified in source.

## Survey Card Fields

**Source type:** Academic working paper  
**Direction:** D3  
**Problem setting:** Long-term causal effect estimation when experiments mature only short-term surrogates and separate observational data contain long-term outcomes but not treatment.  
**Objective and label definition:** Estimate the experimental-population ATE on long-term outcome Y; treatment A is randomized in the experiment, S are intermediate outcomes, and W/Z proxy latent confounders.  
**Prediction or incrementality:** Causal incrementality/ATE estimation.  
**Model architecture:** Outcome and surrogate bridge integral equations, multiply robust efficient influence function, and cross-fitted double/debiased machine learning nuisance estimators.  
**Credit assignment:** Attributes long-term treatment effect through short-term surrogates under no direct A-to-Y effect; proxies recover confounded S-to-Y relations.  
**Training data and counterfactual handling:** Combined randomized and observational samples; proximal proxies adjust latent confounding, with positivity, completeness, bridge, and transport assumptions.  
**Offline and online evaluation:** Theoretical proofs and Job Corps experimental-benchmark recovery; no online product experiment.  
**Reported gains:** Closer recovery of experimental benchmarks than the standard surrogate index under induced/assumed confounding; exact numeric gain not specified.  
**Unverified claims:** Practical proxy validity, exclusion/no-direct-effect, completeness, high-dimensional stability, and applicability under marketplace interference remain unverified.

## Project Relevance

**Source-stated facts:** The method can combine a short-horizon randomized experiment with a separate mature-outcome dataset and remain valid under certain unobserved confounding through proxy variables.

**Survey inference:** Dating could estimate long-run retention/revenue effects before experiments fully mature by linking early likes, matches, replies, and conversations to older cohorts' long outcomes, using redundant behavioral/profile measurements as proxies. Direct treatment effects, sample drift, privacy, and cross-user interference make identification assumptions especially fragile.

**Applicability note:** High-value causal template for validating and estimating delayed dating LTV from surrogates.  
Adopt only with explicit causal graphs, proxy tests, overlap diagnostics, and mature holdout benchmarks.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## Meta Information

**Authors:** Ting-Chih Hung; Yu-Chang Chen  
**Affiliations:** National Taiwan University  
**Venue:** arXiv  
**Year:** 2026  
**PDF:** Available  
**Relevance:** Core measurement reference  
**Priority:** 1
