# The Proximal Surrogate Index: Long-Term Treatment Effects under Unobserved Confounding

**Source:** https://arxiv.org/pdf/2601.17712.pdf | **NLM source id:** 0b33a3db-d741-43f2-802c-7f3558a3838d | **Year / venue:** 2026, arXiv 2601.17712 (January 27, 2026) | **Authors / affiliation:** Ting-Chih Hung, Yu-Chang Chen — National Taiwan University | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Standard surrogate-index methods (Athey et al. 2025b) combine an experimental sample (treatment A observed, long-term outcome Y missing) with an observational sample (Y and short-term surrogates S observed, A missing) to estimate long-term treatment effects, but they assume no unobserved confounder U jointly affecting treatment/surrogates and the long-term outcome — an assumption that fails whenever, e.g., unobserved ability affects both program participation and long-run earnings. This paper introduces the "proximal surrogate index," using two proxy variables — an outcome-aligned proxy W and a surrogate-aligned proxy Z — to identify the treatment effect nonparametrically despite unobserved confounding U, via two complementary bridge functions: an Outcome Bridge Function h₀(W,S,X) that imputes the missing long-term outcome in the experimental sample, and a Surrogate Bridge Function q_{a,0}(Z,S,X) that reweights the observational sample to match the experimental target distribution. These combine into a multiply robust estimator (valid if any of four alternative nuisance-component specifications is correct), with a cross-fitted DML-style estimation procedure and derived efficient-influence-function/semiparametric-efficiency results.
**Unit of credit:** per treated individual (binary A), not per-touch — a treatment-effect estimator, not a multi-touch attribution method. **Outcome:** long-term primary outcome Y (e.g., 4-year earnings/employment; generalizable to retention/LTV). **Bias handling:** explicitly targets *unobserved* confounding (beyond what standard surrogate-index or DML approaches can handle) via proxy variables and bridge-function identification, rather than relying on unconfoundedness/ignorability alone.

## 2. Evidence
- Job Corps (JC) program dataset — large-scale RCT of job training for disadvantaged US youth (Schochet et al. 2001, 2008). Experimental data split into a synthetic "Experimental Sample" (Y masked) and "Observational Sample" (A masked) to create a clean data-combination test with a known RCT ground truth.
- Variables: A = random assignment; Y = year-4 weekly earnings / proportion of weeks employed; S = years 2-3 earnings/employment; W (outcome-aligned proxy) = GED possession; Z (surrogate-aligned proxy) = English mother tongue; X = baseline demographics/pre-program earnings.
- Weekly earnings (4-yr effect): RCT ground truth $15.30 (se $5.49, p=.005); standard surrogate index (Naive 1) $7.05 (se $3.70, p=.057, >50% underestimate); standard surrogate index + proxies as covariates (Naive 2) $7.30; proposed Proximal Surrogate Index $16.43 (se $7.92, p=.038) — closely recovers RCT benchmark.
- Proportion of weeks employed (4-yr effect): RCT +2.87pp (se 1.14, p=.012); Naive 1 +0.80pp (n.s., p=.233); Naive 2 +0.84pp; Proposed +3.50pp (se 1.96, p=.074) — recovers RCT benchmark where standard surrogate index badly underestimates and loses significance.

## 3. Limitations
- Proximal estimator has larger standard errors than direct RCT observation ($7.92 vs $5.49 for earnings; 1.96 vs 1.14pp for employment) — the variance cost of solving the (potentially ill-posed) bridge equations.
- The proximal independence assumptions on W and Z (conditional independence, completeness conditions) are untestable empirically without jointly observing A and Y.
- Assumes no direct effect of treatment A on Y bypassing the surrogates S (exclusion restriction) — same assumption the base surrogate-index approach requires.
- Solving the bridge equations (inverting linear operators T, T*) can be ill-posed, requiring regularization or sieve methods.

## 4. Prior works named
- Athey, Chetty, Imbens & Kang (2025b) — Surrogate Index (the base framework this paper extends)
- Miao, Geng & Tchetgen Tchetgen (2018); Tchetgen Tchetgen et al. (2024) — proximal causal inference / proxy-variable bridge functions
- Chernozhukov et al. (2018) — Double/Debiased Machine Learning (cross-fitting)
- Prentice (1989) — surrogate endpoint operational criteria
- LaLonde (1986) — experimental-vs-observational benchmark evaluation methodology

## 5. Project Relevance
- **Answers:** Q2 background (methodological extension of surrogate-index literature to handle unobserved confounding — directly relevant to the "engaged users swipe more" selection-bias problem, framed as unobserved user-level confounding).
- **Attributes retention to individual interactions?** No — estimates a population-level ATE of a single binary macro treatment; not a per-touch/multi-touch attribution method.
- **Transferable components:** The core insight — that standard causal-adjustment methods (including plain surrogate indices or ordinary propensity-score methods) can still be badly biased if there's an *unobserved* confounder like "latent swiper motivation/attractiveness" driving both engagement and retention — is directly relevant motivation for the dating platform's stated selection-bias problem; the dual-proxy bridge-function framework offers a concrete technique (using pre-existing behavioral proxies as stand-ins for unobserved user quality/motivation) that could debias a per-swipe credit model beyond what observed covariates alone allow.
- **Required changes:** Reframe from single binary-treatment ATE to per-touch fractional credit across a heterogeneous swipe/match/message sequence; would need identification of suitable proxy variables (W, Z) for unobserved "swiper engagement propensity" in the dating context; outcome must shift to a recurring daily N7-active binary.
- **On last-touch:** Not discussed directly — no explicit critique of last-touch/last-click attribution; the paper's empirical contribution is showing standard surrogate methods underestimate long-term effects by >50% under unobserved confounding, which is a cautionary parallel to any single-proxy or single-touch credit scheme trusting confounded engagement signals.
- **Transfer rating:** adaptable — its diagnosis (unobserved user-level confounding badly biases naive short-term-proxy or observed-covariate adjustment) is highly relevant to the platform's exact selection-bias concern, and its proxy/bridge-function machinery is a reusable de-biasing technique, though the paper itself operates on single binary treatments, not multi-touch sequences.
