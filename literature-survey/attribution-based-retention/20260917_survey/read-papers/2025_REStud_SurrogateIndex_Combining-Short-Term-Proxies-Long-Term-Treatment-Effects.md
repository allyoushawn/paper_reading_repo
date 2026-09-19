# The Surrogate Index: Combining Short-Term Proxies to Estimate Long-Term Treatment Effects More Rapidly and Precisely

**Source:** https://arxiv.org/pdf/1603.09326.pdf | **NLM source id:** fa0d650a-9370-4fff-bba9-f0fb2529d026 | **Year / venue:** REStud 2025 (arXiv 1603.09326, updated Aug 2024) | **Authors / affiliation:** Susan Athey (Stanford GSB & Economics, NBER), Raj Chetty (Harvard Economics, NBER), Guido W. Imbens (Stanford, NBER), Hyunseung Kang (University of Wisconsin-Madison, Statistics) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Long-term outcomes of interest (e.g., 9-year employment/earnings) are observed only after long delays, forcing a choice between waiting or relying on a single ad hoc short-term proxy (which invites "clickbait" proxy-goal misalignment). The paper's "surrogate index" systematically combines multiple, qualitatively distinct short-term intermediate outcomes S_i into a scalar predictor μ(S_i, X_i) = E[Y_i | S_i, X_i] of the long-term primary outcome Y_i, by pooling an experimental sample E (has treatment W_i and surrogates S_i but not Y_i) with an observational sample O (has S_i and Y_i but not W_i). Under three assumptions — unconfounded treatment assignment, Prentice surrogacy (W_i ⊥ Y_i | S_i, X_i, sample=E), and comparability (P_i ⊥ Y_i | S_i, X_i) — the ATE on the surrogate index equals the ATE on the true long-term outcome. Four efficient estimators are derived (surrogate index/regression, surrogate score/weighting, influence-function/doubly-robust, double matching), with formal semiparametric efficiency bounds and bias characterizations for surrogacy/comparability violations.
**Unit of credit:** per treated unit/individual (binary W_i), not per-touch — this is a treatment-effect estimation framework, not a multi-touch attribution method. **Outcome:** long-term primary outcome Y_i (employment rate, earnings; generalizable to retention/LTV). **Bias handling:** unconfounded-assignment assumption for identification of W_i's effect; multi-surrogate combination protects against single-proxy gaming (e.g., a treatment that boosts one proxy — clicks — without boosting the true outcome); doubly robust influence-function estimator remains unbiased if either the outcome-regression or the propensity/sampling-score model is correctly specified.

## 2. Evidence
- California GAIN 9-year (36-quarter) randomized job-training experiment, N=18,130: experimental sample (Riverside, N=4,405 treated / 1,040 control); observational sample (Alameda, LA, San Diego, N=13,725).
- True 36-quarter benchmark: employment +6.4pp (s.e. 0.012), earnings +$249 (s.e. $83).
- Naive short-term estimator overestimates badly early on (+11.7pp at quarter 6 vs. true +6.4pp) and needs 25+ quarters to converge to truth.
- Surrogate Index at t=6 quarters: employment +6.1pp (s.e. 0.006); Influence Function estimator: +6.4pp (s.e. 0.006) — matches the 36-quarter benchmark almost exactly, using only 6 quarters of data.
- Earnings at t=6: Surrogate Index +$238.85 (s.e. $31.52), Influence Function +$270.10 (s.e. $32.88) vs. true +$249.05 (s.e. $49.96).
- Standard errors drop ~35-50% (roughly 75% variance reduction) using 6-quarter surrogates vs. waiting for the full 36-quarter outcome.

## 3. Limitations
- Prentice surrogacy cannot be tested within the experimental sample alone when the long-term outcome is unobserved there.
- An incomplete surrogate set fails if treatment has effects that bypass the observed surrogates entirely (the "clickbait" failure mode: a proxy that moves without moving the true outcome).
- When surrogacy/comparability fail outright, nonparametric partial-identification bounds become very wide and uninformative (e.g., [-18.6pp, +12.4pp] for Q6 employment) — the method needs approximate surrogacy to be useful.
- Comparability can break under structural site-level policy differences (e.g., Riverside's "jobs first" vs. other sites' "human capital" emphasis) if covariates X_i don't fully span those differences.

## 4. Prior works named
- Prentice (1989) — Prentice criterion for surrogate endpoints
- Baron & Kenny (1986) — causal mediation analysis
- Rosenbaum & Rubin (1983) — unconfoundedness and propensity scores
- LaLonde (1986) — experimental-vs-observational benchmark evaluation methodology
- Hahn (1998); Newey (1990, 1994) — semiparametric efficiency bounds and influence functions

## 5. Project Relevance
- **Answers:** Q2 background (foundational surrogate/proxy-outcome methodology relevant to modeling delayed retention).
- **Attributes retention to individual interactions?** No — estimates the population-level average treatment effect of a binary macro intervention using short-term proxies; not a multi-touch or per-interaction attribution method.
- **Transferable components:** The core idea — combine several early post-swipe signals (day 1-6 activity, matches, message replies) into a single surrogate index that predicts N7 retention without waiting the full 7 days — is directly reusable for early/fast retention-label construction; the multi-surrogate "anti-gaming" property (combining swipes with downstream matches/conversations) is conceptually the same fix needed against "credits swipes that would have happened anyway" if one surrogate alone (e.g., swipe count) were used; the doubly robust influence-function estimator is a reusable bias-robust estimation pattern.
- **Required changes:** This is a population ATE estimator for a single binary treatment, not a per-touch fractional-credit mechanism — would need to be reframed around a sequence of many candidate-profile "treatments" (each swipe) rather than one program assignment; the outcome must become the recurring daily N7-active binary, and the surrogate vocabulary must expand to heterogeneous event types (swipe/match/message) with time-gap structure.
- **On last-touch:** Not discussed directly — but the paper's core empirical point (a single short-term proxy like clicks alone is exploitable/misleading, i.e., "clickbait") is structurally the same critique the dating platform would level against giving 100% credit to the single last swipe.
- **Transfer rating:** adaptable — the surrogate-index construction and multi-signal anti-gaming logic transfer well conceptually to fast/robust retention labeling, even though the underlying estimand (single binary-treatment ATE) is not itself a multi-touch attribution mechanism.
