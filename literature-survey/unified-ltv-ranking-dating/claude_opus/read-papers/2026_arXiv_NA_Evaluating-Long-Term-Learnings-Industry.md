# Paper Analysis: Evaluating for the Long Term: Learnings from Industry

**Source:** NotebookLM, `nlm:4e0cbb02-d402-485e-8cb7-c37581a20095`
**Date analyzed:** 2026-08-16

## 1. Summary

Leif Sigerson (Pinterest), Tom Cunningham (METR), Winston Chou (Netflix), Sana Pandey (MIT CSAIL), Jonathan Stray (UC Berkeley CHAI), Lo-Hua Yuan (Airbnb), Eytan Bakshy (Meta), Timothy Chan (Statsig), Molly Davies (Pinterest), Maria Dimakopoulou (Uber), Simon Ejdemyr (Netflix), Kenneth Hung (Meta), Nathan Kallus (Netflix & Cornell University), Madhav Kumar (Harvard Business School), Thu Le (Lyft), A. Demetri Pananos (Datadog), Lee Richardson (Google), Brennan Schaffner (Knight-Georgetown Institute), Rose Tan, Martin Tingley, Nadia Tomova (Booking.com), Panagiotis Toulis (University of Chicago Booth School of Business), Wenjing Zheng (Roblox), Zander Arnao (Knight-Georgetown Institute), Dean Eckles (MIT), "Evaluating for the Long Term: Learnings from Industry."

**Abstract (paraphrased):** Online platforms prioritize long-term business outcomes (e.g., 6-month DAU, annual retention), but typical experiments are far too short to measure these outcomes directly. The paper collects and shares industry knowledge — codified as consensus "propositions" — on how to make launch decisions from short-term experiments that stay aligned with long-term outcomes, based on a daylong workshop with 26 experts from 15 online platforms and 4 universities.

**Key contributions:** This is not a single-method paper but a cross-industry consensus report. Its contributions are propositions, each backed (where possible) by public evidence from a named company:
- Sign reversals from short-run to long-run treatment effects are rare, and concentrate in three categories: content-quality/relevance changes, "hyper-monetization," and pricing (lead-day bias).
- A simple univariate "autosurrogate" (the short-run version of the long-run target metric itself) is hard to beat with more elaborate models.
- Experimentally-learned surrogates are preferable to observationally-learned ones because of confounding, but few platforms have a large enough portfolio of long experiments to learn one purely from experimental variation.
- Six concrete techniques mitigate the "correlated measurement error" bias that arises when regressing noisy long-run effects on noisy short-run proxy effects.
- A catalogue of open challenges: evolving/persistent treatments, activity bias, and the tension between surrogate simplicity (trusted by decision-makers) and accuracy.

**Methodology:** Structured expert elicitation. Propositions were drafted from public evidence and prior experience, debated in an 8-hour workshop, then refined with participant sign-off. Each proposition is supported, where available, with a named company's public case study.

**Main results:** See Reference Card and Section 2 below; results are a set of real-world case studies (Netflix, Meta, Pinterest, Airbnb, YouTube, Pandora, Bing, Google) rather than a single benchmark.

## 1b. Surrogate Construction, Validation, and Failure Mode (batch-specific extraction)

This paper is the survey's primary source for the practical question of acting on a long-horizon objective without waiting for the horizon, so this subsection is extracted in more depth than the standard template calls for.

**Surrogate/proxy construction, by company:**
- **Netflix:** Univariate autosurrogates (the short-run version of the long-run metric itself) established as a strong, hard-to-beat baseline via a meta-analysis of 200 A/B tests. Netflix also supplies weak-instrument estimators for correlated measurement error (Bibaut et al., 2024) and a decision-rule backtesting/cross-validation method (Chou et al., 2025).
- **Meta/Facebook:** Uses experiments as instruments to fit a regularized predictive model mapping short-term proxies to long-term change (Day et al., 2026). Ran a 2-year "minimum integrity holdout" disabling quality filters (clickbait/adsfarm downranking) and a >1-year notification-volume holdout.
- **Pinterest:** A >1-year badging experiment used to characterize novelty-effect decay of a surrogate-driven signal (see failure mode below).
- **Airbnb:** ~4-month pricing experiments; contributes the "lead-day bias" correction (booking-delay confounding) as a platform-specific surrogate adjustment.
- **YouTube/Google:** 4-month diversification (DPP) holdout; 3-month "trashy/tabloid" downranking holdout; ad-load experiments showing treatment effects follow an exponential curve that keeps rising for weeks.
- **Pandora:** 21-month ad-load field experiment used as ground truth to benchmark a suite of observational estimators (panel data, fixed effects, instrumental variables) — the observational methods were frequently biased and sometimes had the wrong sign.
- **Bing:** Intentionally degraded search relevance to study long-run confidence/return-visit effects.
- **Microsoft, Booking.com:** Scale context only (10,000–100,000+ experiments/year); Microsoft reports never observing a sign reversal across its portfolio.

**Validation procedure:** The paper's central validation claim is that a surrogate or decision rule cannot be validated without at least a few real long-running experiments — pure observational validation is explicitly distrusted. Two concrete techniques are named: (1) Netflix's decision-rule backtesting/cross-validation over a historical experiment portfolio (does the surrogate-based decision rule reproduce the long-run-optimal decision on held-out experiments); (2) a placebo test that reshuffles treatment assignment at random — because there is no true effect by construction, any "significant" cross-experiment correlation the analyst finds is proof that the correlated-measurement-error bias, not signal, is driving the naive regression. This placebo test is the paper's diagnostic for detecting a specific validation failure mode (see below), not a way of confirming a surrogate is good.

**Stated failure modes (record even when brief):**
1. **Sign reversal** concentrates in three categories: content-quality/relevance changes, hyper-monetization, and pricing experiments with lead-day bias. Concrete cases: Facebook's minimum-integrity holdout showed +0.4% impressions at 1 month but net-negative activity at 2 years; YouTube's tabloid downranking showed −0.5% watch time at 3 weeks that recovered and turned positive by 3 months.
2. **Confounding bias in observational surrogates**: active users are more likely to both generate high short-term signal and retain long-term for unrelated latent reasons (e.g., free time) — this is the paper's own version of the project's prediction-vs-incrementality distinction.
3. **Correlated measurement error**: naively regressing noisy long-run treatment-effect estimates on noisy short-run proxy effects is asymptotically biased, and the bias is visible even in placebo (no true effect) experiments.
4. **Persistent/evolving treatments** violate the assumption that short-term outcomes fully mediate the long-term effect (a permanent algorithm change keeps acting after the "surrogate" window closes).
5. **Activity/sample bias**: short experiments oversample highly active users and can entirely miss inactive users, so the measured population differs from the true long-term target population.
6. **Asymmetric evidence**: platforms kill obviously bad treatments early, so there are systematically fewer long-running experiments with large negative effects — surrogate validation is implicitly better-calibrated for positive than negative decisions.
7. **False precision**: surrogate-index confidence intervals reflect "known unknowns" (sampling variance) but not "unknown unknowns" (residual confounding), so a surrogate can look more trustworthy than it is.

**Explicit disagreement among practitioners (high-signal):**
- **Novelty effects:** one platform discards the first several days of experiment data specifically to avoid novelty-effect contamination; other participants felt novelty effects would not typically change the launch decision either way. No consensus reached.
- **Surrogate portability ("metric gaming") vs. broad OECs:** one participant raised a "metric gaming" concern — a correlation between a short-term metric and the long-term north star found in past experiments can be exploited by deliberately moving the short-term metric in a way that breaks the historical causal structure (their example: sending notifications on the same cadence used to estimate the correlation). A different participant argued that a sufficiently broadly-defined Overall Evaluation Criterion (OEC) is more portable across experiment classes. The workshop's proposed reconciliation — treat surrogates as mechanistic treatment mediators, and only compare experiments affecting the same mechanism — is offered as a resolution, not a settled consensus.
- **Simplicity vs. accuracy:** described explicitly as a "recurring tension" rather than resolved. Participants agreed simple, interpretable surrogates build more trust with decision-makers, but acknowledged this can trade off against accuracy, with no agreed rule for where to draw the line.

## 2. Experiment Critique

- **Design:** Not a controlled experiment; a structured expert-elicitation and literature-synthesis exercise (26 experts, 15 platforms, 4 universities, 8-hour workshop, pre-drafted propositions refined and validated post-hoc with participants). Strength: draws on real production experiments platforms would not otherwise disclose. Weakness: propositions reflect informal consensus and "public evidence" cherry-picked by convenience, not a systematic meta-analysis; several propositions (e.g., DAU half-life of ~1 month) are asserted without confidence intervals or replication.
- **Statistical validity:** Individual cited case studies (Netflix's 200-test meta-analysis, Pandora's 21-month experiment) carry their own statistical rigor, but the paper itself does not run new statistical tests; it aggregates and interprets others' results.
- **Online experiments:** The entire paper is built from online experiments (single-feature holdouts lasting 3 months to 2+ years across at least 7 named platforms) — this is a strength specific to this source; it is the only paper in this batch built entirely from realized, multi-month-to-multi-year production A/B/holdout data rather than simulation.
- **Reproducibility:** Low. Most underlying company datasets (Facebook's minimum-integrity holdout, Pinterest's badging experiment) are internal and only summarized in secondary/blog sources; only Netflix's 200-A/B-test meta-analysis (Zhang et al., 2024, arXiv:2311.11922) and the Pandora study (Goli et al., 2025) are independently citable and reproducible-in-principle.
- **Overall:** Credible as an industry-consensus survey precisely because it is explicit about where consensus was NOT reached (see disagreements above) rather than presenting a false unanimity.

## 3. Industry Contribution

- **Deployability:** The paper is itself a deployment guide rather than a deployable artifact — it prescribes six concrete, implementable bias-mitigation techniques for building a surrogate index from a portfolio of long-running experiments (bigger experiments, high-SNR proxy filtering, L0-regularized experiment selection, IV/empirical-Bayes bias adjustment, experiment splitting, decision-rule backtesting).
- **Problems solved:** Directly solves the "we can't wait a horizon" bottleneck the project faces for retention (7–30 days) and revenue (weeks): it gives a menu of validated ways to make short-run launch decisions that track long-run retention/revenue, plus explicit guidance on when NOT to trust a short-run proxy (content-quality and monetization changes).
- **Engineering cost:** Ranges from near-zero (using the raw short-run version of the metric as an autosurrogate) to substantial (maintaining a portfolio of long-running holdout experiments, building experiment-splitting or IV-based bias-correction pipelines, joint offline+online governance to reconcile decision rules across dozens of thousands of experiments/year). No latency or online-serving implications — this is an offline experimentation/decision-governance practice, not a ranking-model architecture.

## 4. Novelty vs. Prior Work

**Claimed novelty:** The paper does not claim algorithmic novelty; its claimed contribution is codifying previously undocumented, cross-company tacit knowledge into shared propositions, several validated for the first time with public evidence contributed specifically for this workshop.

**Prior work most heavily built on:**
- Athey, Chetty, Imbens, and Kang, "The Surrogate Index: Combining short-term proxies to estimate long-term treatment effects more rapidly and precisely," Review of Economic Studies, 2026 — the formal statistical foundation for the surrogate index concept used throughout.
- Hohnhold, O'Brien, and Tang, "Focusing on the Long-Term: It's Good for Users and Business," KDD 2015 — pioneering industrial ad-load long-term experimentation.
- Bibaut, Chou, Ejdemyr, and Kallus, "Learning the Covariance of Treatment Effects Across Many Weak Experiments," KDD 2024 — the weak-instruments framework used for correlated-measurement-error correction.
- Cunningham, Pandey, Sigerson, Stray, et al., "Ranking by Engagement and Non-Engagement Signals: Learnings from Industry," Annals of the New York Academy of Sciences, 2025 — the direct predecessor workshop-report methodology, reused here for content-quality case studies.
- Tripuraneni, Richardson, D'Amour, Soriano, and Yadlowsky, "Choosing a Proxy Metric from Past Experiments," KDD 2024 — proxy-selection guidelines.
- Kohavi, Deng, Frasca, Longbotham, Walker, and Xu, "Trustworthy Online Controlled Experiments: Five Puzzling Outcomes Explained," KDD 2012, and Kohavi and Thomke, Harvard Business Review, 2017 — canonical references on experimentation scale and pitfalls.
- Le and Deng, "The Price Is Right: Removing A/B Test Bias in a Marketplace of Expirable Goods," CIKM 2023 — lead-day bias correction, cited for Airbnb's pricing work.

## 5. Dataset Availability

| Dataset | Company | Duration | Public? |
|---|---|---|---|
| 200 A/B test meta-analysis | Netflix | 2 weeks vs. 2 months compared | Published (Zhang et al., 2024, arXiv:2311.11922) |
| Ad-load field experiment | Pandora | 21 months | Published (Goli et al., 2025) |
| Minimum integrity holdout | Facebook | 2 years | Internal (secondary citation: FBArchive, 2019) |
| Notification filtering holdout | Facebook | >1 year | Blog (Analytics at Meta, 2022) |
| DPP diversification homefeed | YouTube | 4 months | Published (Wilhelm et al., 2018, CIKM) |
| Trashy/tabloid downranking | YouTube | 3 months | Secondary citation only |
| Badging experiment | Pinterest | >1 year | Blog (Egan, 2015) |
| Pricing algorithm experiments | Airbnb | ~4 months | Published (Le and Deng, 2023, CIKM) |
| Mobile ad-load experiments | Google | Weeks to months | Published (Hohnhold et al., 2015, KDD) |

None of these are downloadable benchmark datasets in the conventional ML sense; all are internal production experiments described in the primary paper or its cited secondary sources.

## 6. Community Reaction

Not assessed in NotebookLM mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Evaluating for the Long Term: Learnings from Industry," Sigerson et al. (26 authors, 15 platforms + 4 universities), workshop report (venue/arXiv identifier not captured in NotebookLM extraction), 2026. URL: not provided in extracted content. |
| 2 | Source type | Industry workshop report / cross-company consensus paper (blends industry and academic authorship). |
| 3 | Direction | D3 |
| 4 | Problem setting | Platforms must make launch decisions on long-horizon business outcomes (e.g., 6-month DAU, retention, revenue) using only short-run (typically 3-day to 3-week) experiments, because running experiments to the full horizon is infeasible at the required decision cadence. |
| 5 | Objective and label definition | Not a single model. Canonical problem: predict the effect of a ranking-algorithm change on 6-month DAU using 7-day cumulative engagement metrics (clicks, likes, comments, reshares, upvotes, return visits) as proxies. Long-run windows observed across the cited case studies range from 3 months to 2+ years; short-run windows are typically 7 days. No formal statistical censoring model is used — delay is handled purely through experiment duration choice and post hoc bias-correction techniques (see field 9), not through survival/hazard modeling. |
| 6 | Prediction or incrementality | Incrementality/causal-effect estimation, explicitly. Paper's own words: "we describe what is known in industry about methods to estimate the long-run treatment effect of a permanent change to digital services," and a surrogate index is defined as providing "an estimate of the treatment effect on the long-run outcome as a function of treatment effects on short-run proxies." |
| 7 | Model architecture | None — this is a methodological/decision-governance survey, not a model paper. It compares two estimation paradigms (observation-based surrogacy vs. experiment-based surrogacy) rather than proposing an architecture. |
| 8 | Credit assignment | Not addressed. All measurement is at the user/experiment-arm level (aggregate treatment effect on a cohort in an A/B test); the paper does not discuss mapping a delayed outcome to a single impression, item, or slate decision. |
| 9 | Training data and counterfactual handling | Two families: (a) observational surrogacy — fit a model of the long-term outcome from short-term proxies and covariates on historical logs, valid only under an unconfoundedness assumption the paper says is frequently implausible; (b) experiment-based surrogacy — regress long-run treatment effects on short-run proxy treatment effects across a portfolio of past experiments, which is unbiased only after correcting for correlated measurement error via one or more of: bigger experiments, high-SNR proxy filtering, L0-regularized selection of the strongest experiments, IV/empirical-Bayes bias adjustment, experiment splitting, or decision-rule backtesting. |
| 10 | Offline and online evaluation | Offline: decision-consistency backtesting against historical experiment portfolios (Netflix); placebo/reshuffled-treatment diagnostics to detect correlated measurement error. Online: the entire evidence base — single-feature holdouts and long-running A/B tests lasting 3 months to 2+ years across at least 7 named platforms. |
| 11 | Reported gains | Netflix: 95% agreement between launch decisions made at 2 weeks vs. 2 months across 200 A/B tests. Pinterest badging: DAU lift decayed from 7% (short-term) to a stable 2.5% (long-term), still net positive. Pandora ad-load: 1-year effect more than double the 2-month effect. Facebook minimum-integrity holdout: +0.4% impressions at 1 month, net-negative overall activity at 2 years. YouTube tabloid downranking: −0.5% watch time at 3 weeks, recovered to net positive by 3 months. |
| 12 | Applicability to a two-sided dating recommender | Gives directly transferable, validated guidance on constructing and stress-testing a retention/revenue surrogate under the project's exact "can't wait the full horizon" constraint. It does not address reciprocity, congestion, or fairness across two sides at all — those must come from elsewhere in the survey. |
| 13 | Unverified claims | Several company-level numeric claims (e.g., the ~1-month DAU "half-life" for content-ranking changes, the specific novelty-decay trajectory) are reported as expert consensus/public evidence rather than independently re-verified by the workshop authors; Microsoft's claim of never observing a single sign-reversed experiment is self-reported and not independently audited in this source. |

## Project Relevance

Directly answers **Q1** (industry practice for making retention/revenue the training objective without a full-horizon wait — this paper's central subject), **Q3** (label/horizon definitions and delay handling, via the short-run/long-run effect taxonomy and the six measurement-error-correction techniques), and **Q6** (offline evaluation and surrogate-validation methodology, via decision-consistency backtesting and the placebo diagnostic). Partially informs **Q8** (staged migration) insofar as it describes how a proxy-based launch decision process can be validated and progressively trusted, though it does not describe a model-architecture migration path.

Does not address **Q2** (item-level credit assignment), **Q4** (fusion of short-term/long-term heads inside a ranking model), **Q5** (where uplift sits inside the ranking model itself), or **Q7** (two-sided/reciprocal-market specifics — reciprocity, congestion, fairness across sides are entirely absent from this source).

## Papers That Mention This Paper (Reverse Citation Map)

_This paper proposes no distinctively-named method, so no automated reverse-citation match was possible._

## Meta Information

- **Authors/Affiliations:** 26 authors across Pinterest, METR, Netflix, MIT, UC Berkeley, Airbnb, Meta, Statsig, Uber, Harvard Business School, Lyft, Datadog, Google, Knight-Georgetown Institute, Booking.com, University of Chicago Booth School of Business, Roblox, Cornell University.
- **Venue:** Cross-industry/academic workshop report (specific venue/preprint identifier not captured in extraction).
- **Year:** 2026
- **Relevance:** Core
- **Priority:** 1
- **NotebookLM source:** `nlm:4e0cbb02-d402-485e-8cb7-c37581a20095`
