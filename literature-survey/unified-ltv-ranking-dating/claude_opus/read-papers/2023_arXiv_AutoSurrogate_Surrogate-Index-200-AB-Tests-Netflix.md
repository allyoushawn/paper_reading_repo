# Paper Analysis: Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix

**Source:** /Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/2311.11922.pdf
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix
**Authors:** Vickie Zhang, Michael Zhao, Anh Le, Maria Dimakopoulou, Nathan Kallus (Netflix)
**Venue:** arXiv (stat.AP), 2023 (v2 Jan 2024)

**Abstract (from source):** Surrogate index approaches have recently become a popular method of estimating longer-term impact from shorter-term outcomes. The paper leverages 1098 test arms from 200 A/B tests at Netflix to empirically investigate to what degree decisions made using a surrogate index utilizing 14 days of data would align with those made using direct measurement of day-63 treatment effects. Focusing on linear "auto-surrogate" models that use shorter-term observations of the long-term outcome itself, the authors find the statistical inferences drawn from the surrogate index are ~95% consistent with those from directly measuring the long-term treatment effect. Restricting to tests that would be "launched" (positive and statistically significant) based on the 63-day directly measured effect, relying on the surrogate index instead achieves 79% precision and 65% recall.

**Key contributions:**
1. The first large-scale empirical audit (200 real, already-run production A/B tests, 1098 test arms) of how often a surrogate-index-based ship decision agrees with the decision that direct long-term measurement would have produced.
2. Introduction and evaluation of "auto-surrogate" models — a special case of the surrogate index where the short-term predictors are earlier daily realizations of the *same* long-term outcome variable, rather than a distinct set of surrogate metrics.
3. A precision/recall framing of the surrogate-index decision problem (with the 63-day directly measured decision as ground truth), plus a throughput argument for how much extra experimentation capacity a shorter testing cycle could buy.

**Methodology:** For 200 A/B tests run at least 63 days, the 63-day treatment effect τ̂_a,63 is computed via an unbiased difference-in-means over daily-averaged outcomes. The surrogate index (an "auto-surrogate" model) is a linear regression of the observed 63-day average outcome µ_i on a user's own daily outcome values for the first T ≤ 63 days: µ_i = β0 + Σ_{t=1}^T βt·Y_it + ε_i. The long-term treatment effect is then re-estimated as the difference-in-means of the model's predicted values. Two training regimes are compared: "Pre-Test" (model trained on the same users' 63 days of pre-allocation history) and "Similar Test" (model trained on data from a different, related A/B test in the same product space).

**Main results:** Across 200 personalization-algorithm A/B tests, the statistical conclusion (significant positive / not significant / significant negative) drawn from a 14-day auto-surrogate index agreed with the conclusion from the direct 63-day measurement ~95% of the time (Figure 4 confusion matrices, both training regimes). Restricted to launch decisions (statistically significant positive at 63 days), the surrogate index achieved 79% precision and 65% recall relative to the 63-day-based decision, with zero observed cases of the surrogate recommending "launch" on a test whose 63-day effect was statistically significant *negative*.

## 2. Experiment Critique

**Design.** A retrospective, empirical stress test rather than a proposed estimator: 1098 test arms from 200 already-completed Netflix personalization-algorithm A/B tests, using "single shot" randomized allocation. The 63-day directly measured effect is treated as ground truth against which the 14-day (and other T) surrogate-index decisions are scored.

**Statistical validity.** Relies on standard difference-in-means / SUTVA assumptions for the ground-truth 63-day estimate. The paper explicitly reports that both the directly measured and surrogate-index-estimated treatment-effect distributions are fat-tailed relative to Normal (consistent with prior literature on A/B testing with fat tails), a caveat for any inference relying on normal-approximation confidence intervals. No held-out ground truth beyond the 63-day read itself exists — the entire analysis is an internal consistency check, not a comparison against a truly independent long-run outcome.

**Online experiments.** This paper *is* effectively a large-scale online/production evaluation — its evidence base is 200 real fielded A/B tests, not simulation.

**Reproducibility.** The auto-surrogate regression and difference-in-means estimators are fully specified with equations. The underlying 200 A/B tests and the exact identity of the outcome metric(s) used ("outcome metrics that average a per-day observation" in the personalization-algorithms space) are Netflix production data and are not named or released — the empirical numbers cannot be independently reproduced.

**Overall.** A short (5-page), narrowly scoped empirical paper. Its strength is the scale and realism of its evidence (real production decisions); its weakness is that it reports a single dataset's agreement rate without stress-testing the result across product areas outside "personalization algorithms," or providing a theoretical account of why 65% recall (rather than higher) was obtained.

## 3. Industry Contribution

**Deployability.** Very high: the method is a linear regression on already-logged daily metric values, requiring no new online serving infrastructure. It is directly usable to compress a personalization-algorithm test cycle from 63 days to as few as 14.

**Problems solved.** Shortens the long-term-outcome A/B test read-out cycle, freeing testing capacity; the paper estimates a maximum theoretical 300% increase in experimentation throughput from moving to a 2-week cycle (with ~53% more 2-week tests needed to match the "true positive" yield of 2-month tests, given 65% recall).

**Engineering cost.** Minimal computationally (a per-metric linear regression); the real cost is organizational — deciding what level of false-negative risk (missed good ideas) and residual false-positive risk is acceptable for faster iteration.

**Framed in recommender-engineering terms.** This is entirely an experimentation-pipeline / launch-decision tool operating above the ranking model, not a ranking architecture, feature-engineering technique, or serving-latency concern.

## 4. Novelty vs. Prior Work

**Claimed novelty.** The first large-scale empirical audit of surrogate-index decision agreement against 200 real fielded A/B tests (rather than simulation or a handful of case studies), and the introduction of the "auto-surrogate" specialization of the surrogate index (short-term proxy = earlier realization of the same outcome variable).

**Prior work cited (5-7 most relevant):**
- Athey, Chetty, Imbens, Kang, "The surrogate index: Combining short-term proxies to estimate long-term treatment effects more rapidly and precisely," NBER, 2019 — the foundational surrogate-index method this paper empirically tests.
- Kohavi, Deng, Frasca, Longbotham, Walker, Xu, "Trustworthy online controlled experiments: Five puzzling outcomes explained," KDD 2012 — motivates why short- and long-term effects can diverge (novelty effects, user fatigue, "clickbaitness").
- Gupta et al., "Top challenges from the first practical online controlled experiments summit," SIGKDD Explorations 2019 — cited on the role of A/B testing in product development.
- Azevedo, Deng, Montiel Olea, Rao, Weyl, "A/B testing with fat tails," Journal of Political Economy, 2020 — explains the fat-tailed treatment-effect distributions the paper observes.
- Coey and Cunningham, "Improving treatment effect estimators through experiment splitting," WWW 2019.
- Peysakhovich and Eckles, "Learning causal effects from many randomized experiments using regularized instrumental variables," WWW 2018.
- Prentice, "Surrogate endpoints in clinical trials: definition and operational criteria," Statistics in Medicine, 1989 — origin of the surrogacy assumption.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| 1098 test arms / 200 A/B tests, Netflix personalization-algorithms space | Industrial, proprietary | No | Not released; exact outcome metric(s) not named in source, described only as "outcome metrics that average a per-day observation" |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix; Vickie Zhang, Michael Zhao, Anh Le, Maria Dimakopoulou, Nathan Kallus (Netflix); arXiv (stat.AP), 2023 (v2 Jan 2024); https://arxiv.org/abs/2311.11922 |
| 2 | Source type | Industry paper |
| 3 | Direction | D3 |
| 4 | Problem setting | Whether a surrogate-index estimate built from only 14 days of data leads to the same ship/no-ship decision as directly measuring the 63-day (2-month) treatment effect, tested across 200 real Netflix personalization-algorithm A/B tests (1098 test arms). |
| 5 | Objective and label definition | Long-term outcome µ_i = average of a per-day outcome metric over the first 63 days post-allocation (exact metric identity not specified in source). The surrogate ("auto-surrogate") is a linear regression of µ_i on the same metric's daily values for the first T days (T tested up to 63; headline result uses T=14). No formal censoring correction — all included tests ran the full 63 days; "delay" is handled purely by predicting the later average from an earlier trajectory of the identical metric, not by a missing-data or censoring model. |
| 6 | Prediction or incrementality | Incrementality. Both the direct 63-day estimate and the surrogate-index estimate are treatment-effect estimates (τ̂ = difference-in-means between treatment and control arms), not predictions of an individual user's outcome. The paper states the surrogate estimators "unbiasedly recover the directly measured treatment effect ... assuming SUTVA." |
| 7 | Model architecture | Not a neural or ranking architecture. A linear regression ("auto-surrogate" model) predicting the long-term daily-average outcome from T ≤ 63 days of the same metric's daily values, trained either (a) "Pre-Test": on the same users' own 63 days of pre-allocation history, or (b) "Similar Test": on data from a different, related A/B test in the same product space. |
| 8 | Credit assignment | **Not applicable at the item level — this paper operates entirely at the experiment-arm level.** The unit of analysis is a full A/B test arm (a population-level average treatment effect), never an individual impression, item, or user-level decision. |
| 9 | Training data and counterfactual handling | Randomized "single shot allocation" A/B test arms provide the counterfactual directly (control arm = counterfactual for treatment arm); no observational/counterfactual correction is needed. The auto-surrogate regression is trained on either the same users' pre-experiment history or a separate, similar experiment — never on the test being evaluated itself. |
| 10 | Offline and online evaluation | The entire paper is a retrospective evaluation of the surrogate-index decision against direct 63-day measurement across 200 already-run, live production A/B tests — there is no separate offline/online split; it is analysis of real online experiment outcomes. |
| 11 | Reported gains | Across 200 A/B tests / 1098 test arms in Netflix's personalization-algorithms space: statistical conclusions from the 14-day auto-surrogate index agreed with the 63-day direct measurement ~95% of the time (Figure 4 confusion matrices). Restricted to launch decisions (statistically significant positive at 63 days), the surrogate index achieved 79% precision and 65% recall. Zero observed cases of the surrogate concluding "launch" on a test that was statistically significant negative at 63 days. |
| 12 | Applicability to a two-sided dating recommender | Directly reusable at the experimentation layer above the eventual unified model — the auto-surrogate approach could compress retention/revenue A/B read-out from 30+ days to ~1-2 weeks using early daily retention/revenue trajectories. It validates test-level ship decisions, not per-impression ranking scores, and offers no mechanism for reciprocity or congestion. |
| 13 | Unverified claims | The throughput-gain argument ("shorter cycle outweighs increased reliability of direct measurement") explicitly rests on stated but untested assumptions: the true treatment-effect distribution doesn't change with the number of experiments run, treatment effects across different experiments are additive, and there is no/very low marginal cost to running additional experiments. The "65% recall implies ~53% more experiments needed" calculation is presented as an illustrative estimate, not a validated operational result. |

## Project Relevance

Speaks directly to **Q3** (label/horizon definition and delay handling — a concrete, empirically validated way to shorten a 30-63 day retention/revenue read to ~2 weeks) and **Q6** (offline/online evaluation methodology under slow, noisy long-term effects — precisely a "surrogate validation" case study the executive summary's evaluation-plan deliverable needs). This is the most decision-relevant reference in the batch because it reports an empirical agreement rate — not a simulated or theoretical one — at real production scale (200 tests), directly bearing on whether the project can trust a surrogate-based fast-iteration loop for its own retention/revenue experiments. It says nothing about item-level ranking, credit assignment, or two-sided/reciprocal markets (**not relevant to Q2, Q4, Q5, Q7**) — the entire analysis sits at the experiment-decision level, a mismatch the survey should carry forward explicitly (see field 8). **Warning worth carrying prominently:** 65% recall means roughly one in three genuinely good ideas would be missed (a false negative / lost opportunity) under a 14-day surrogate cutoff. The false-positive risk of shipping a genuinely harmful change was empirically zero in this specific sample, but the paper explicitly notes rare (<1%) opposite-direction mistakes were observed in other, unreported analyses — so "zero harm" should not be read as a guarantee for a different product surface such as a dating app.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `AutoSurrogate`._

## Meta Information

- **Authors:** Vickie Zhang, Michael Zhao, Anh Le, Maria Dimakopoulou, Nathan Kallus
- **Affiliations:** Netflix
- **Venue:** arXiv (stat.AP)
- **Year:** 2023 (v2 Jan 2024)
- **Relevance:** Core
- **Priority:** 1
- **nlm:ad7e1e30**
