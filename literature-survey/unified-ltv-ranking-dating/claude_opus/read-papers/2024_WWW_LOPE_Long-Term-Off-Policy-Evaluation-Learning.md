# Paper Analysis: Long-term Off-Policy Evaluation and Learning

**Source:** NotebookLM, `nlm:7fee3f6b-6faa-436e-aa21-d9477fef7739`
**Date analyzed:** 2026-08-16

## 1. Summary

Yuta Saito (Cornell University), Himan Abdollahpouri (Spotify), Jesse Anderton (Spotify), Ben Carterette (Spotify), Mounia Lalmas (Spotify), "Long-term Off-Policy Evaluation and Learning," WWW 2024 (Singapore).

**Abstract (paraphrased):** Short- and long-term outcomes of an algorithm often diverge — the classic click-bait failure mode raises short-term clicks but damages long-term engagement. Existing approaches either rely on Long-term Causal Inference (LCI), which needs the restrictive "surrogacy" assumption and produces no learning algorithm, or typical Off-Policy Evaluation (OPE, e.g., IPS/DR), which needs no surrogacy assumption but cannot use short-term rewards to control variance and is therefore very high-variance when the long-term reward is noisy. The paper proposes Long-term Off-Policy Evaluation (LOPE), which decomposes the expected long-term reward into a surrogate effect (explained by short-term rewards) and an action effect (residual), estimates the surrogate effect via importance weighting over short-term-reward distributions and the action effect via reward regression, and extends this to policy-gradient learning (LOPE-PG).

**Key contributions:** (1) A reward-function decomposition q(x,a,s) = g(x,s) + h(x,a,s) that strictly generalizes the surrogacy assumption (recovered when h=0). (2) The LOPE estimator, proven unbiased under either the surrogacy assumption OR a weaker "conditional pairwise correctness" (CPC) condition on the action-effect regression — a new doubly-robust-style guarantee. (3) A proof that the surrogate importance weight has provably lower variance than the vanilla (action-based) importance weight used by IPS/DR. (4) LOPE-PG, extending the estimator to offline policy-gradient learning, so the long-term value can be directly optimized from historical data without a long-term online experiment.

**Methodology:** The estimator is V_LOPE(π₁;D_H) = (1/n_H)Σᵢ{ŵ(xᵢ,sᵢ)(rᵢ − ĥ(xᵢ,aᵢ,sᵢ)) + ĥ(xᵢ,π₁)}, where ŵ(x,s)=π₁(s|x)/π₀(s|x) is the "surrogate importance weight" over the marginal short-term-reward distribution (estimated via Bayes' rule using a classifier for π₀(a|x,s), avoiding the need to model the high-dimensional s directly), and ĥ is a reward-regression model of the residual action effect. Unbiasedness holds if either the surrogacy assumption holds, or ĥ satisfies CPC (correctly preserves relative reward differences between any two actions conditional on s — a strictly weaker requirement than global accuracy). LOPE-PG applies the same decomposition to policy-gradient estimation.

**Main results:** Synthetic experiments (1,000 users, 10-d context, |A|=30, expected reward q(x,a;λ)=(1−λ)g(x,f(x,a))+λh(x,a) with λ controlling surrogacy violation) show LOPE achieves the lowest MSE among feasible estimators across nearly all settings — up to 71% MSE reduction vs. LCI at large sample size (surrogacy-violation robustness), and up to 45% MSE reduction vs. DR under high reward noise (variance reduction). LOPE-PG outperforms DR-PG by ~60% (small data) to ~80% (high noise). Real-world evaluation on a Spotify homepage recommendation A/B test (~4M users, >1,000 candidate items, week-1 engagement as surrogate for week-3 streams) shows LOPE achieves 9.2–15.0% lower MSE than the next-best method (DR) in reconstructing the actual 3-week experiment outcome for three deployed policies.

## 1b. Surrogate Construction, Validation, and Failure Mode (batch-specific extraction)

**Surrogate/proxy construction:** LOPE decomposes the expected long-term reward q(x,a,s) into a surrogate effect g(x,s) — the part explained purely by short-term rewards s (clicks, streams, likes, dislikes in the Spotify application) — and an action effect h(x,a,s), the residual not explained by short-term signals. This is a strict generalization of the classical surrogacy assumption (which is the special case h≡0). The surrogate effect is estimated not by direct regression but by importance weighting the marginal distribution of short-term rewards under the target vs. logging policy (the "surrogate importance weight" w(x,s)=π₁(s|x)/π₀(s|x)), while the residual action effect is estimated by a conventional reward regression trained on historical data. This is a materially different surrogate-construction strategy than papers 1–2 in this batch: rather than substituting a short-term metric for the long-term one, LOPE uses the short-term signal only to reweight/importance-sample, and explicitly models what the short-term signal fails to explain.

**Validation procedure:** Both theoretical and empirical, and unusually explicit about the conditions under which the surrogate is trustworthy. Theoretically, Theorem 3.1 proves LOPE is unbiased if either the surrogacy assumption holds OR the weaker CPC condition on the regression estimator ĥ holds — a doubly-robust-style guarantee that gives two independent paths to validity. Theorem 3.2 proves the surrogate importance weight has provably lower variance than the vanilla action-based importance weight, with the size of the reduction increasing exactly when the vanilla weight's variance is large — this is a direct, provable answer to "does using the short-term surrogate actually help." Empirically, the paper runs a dedicated surrogacy-violation stress test: sweeping λ from 0 (surrogacy holds exactly) to 1 (surrogacy maximally violated) and observing that LCI's MSE grows sharply while LOPE's MSE stays essentially flat — this is a direct, purpose-built validation of surrogate robustness under violation, the single most rigorous surrogate-validation design in this batch. The real-world Spotify evaluation is itself a validation exercise: using week-1 engagement as the surrogate for week-3 streams, LOPE's estimate is checked against the actual, fully-realized 3-week A/B test outcome for three already-deployed policies.

**Stated failure mode:** The paper reports an explicit negative result: under very low long-term-reward noise (σᵣ=1.0), LOPE actually underperforms plain IPS and DR, because in that regime the reward-regression estimation error in ĥ outweighs LOPE's variance-reduction benefit — the surrogate decomposition is not universally superior, only superior specifically when the long-term label is noisy (which the paper argues is the realistic industrial case). The authors also explicitly flag that LOPE (like LCI and typical OPE) assumes a "comparability assumption" — that the joint short-term/long-term reward distribution is stationary between the historical/logging period and the evaluation period — and note this is vulnerable to real non-stationarity (e.g., seasonal shifts in music preference), calling it a valuable but unaddressed direction for future work. Additionally, the paper does not address how to preprocess or represent high-dimensional short-term rewards, and the real-world validation is limited to a 3-week horizon, with the authors explicitly noting that validating longer horizons (e.g., annual metrics) remains future work.

## 2. Experiment Critique

- **Design:** Synthetic experiments systematically vary the surrogacy-violation parameter λ, reward noise σᵣ, historical data size n, and target-policy quality ε — a comprehensive sensitivity analysis directly targeting the paper's own claimed advantages (robustness to surrogacy violation, variance reduction under noise). Real-world experiment uses an actual completed 3-week, 4-million-user A/B test as ground truth, which is a strong design choice — the "ground truth" is a real experiment outcome, not a simulated one.
- **Statistical validity:** Synthetic MSE/bias/variance comparisons are run with statistical significance testing (Mann–Whitney U test, p=0.05) across repeated trials; the real-world comparison across three deployed policies is a single realized outcome per policy (no repeated-trial variance is reported for the real-world MSE numbers themselves, since ground truth is a single completed experiment).
- **Online experiments:** The real-world evaluation is offline replay against a completed online A/B test, not a live online deployment of LOPE itself; no online test of LOPE-PG-learned policies is reported.
- **Reproducibility:** Synthetic experiment code is public (https://github.com/usaito/www2024-lope); the real-world Spotify dataset is proprietary and not released.
- **Overall:** One of the more rigorous evaluations in this batch — the theory (two independent unbiasedness conditions, a provable variance-reduction bound) is directly matched to targeted synthetic stress tests and then further checked against a genuine large-scale industrial A/B test, though online deployment of the learned policy itself (LOPE-PG in production) is not demonstrated.

## 3. Industry Contribution

- **Deployability:** High — LOPE requires only a reward regression model and a classifier for the logging policy's action-given-context-and-surrogate distribution, both standard supervised-learning components; no new serving-time infrastructure is needed since it is used for offline policy evaluation/learning, not real-time inference.
- **Problems solved:** Directly solves "how do I evaluate or learn a policy that improves a long-term (weeks-out) metric using only historical data plus a short-term experiment," which is exactly the project's constraint (retention 7–30 days, revenue over weeks) — this is the closest paper in the batch to a ready-made offline evaluation/learning recipe for the migration itself.
- **Engineering cost:** Moderate — requires historical logs with both short-term and long-term rewards (D_H) and, optionally, a short-term-only experiment dataset for the new policy (D_S); requires training a reward-regression model and a propensity/logging-policy classifier; the LOPE-PG extension additionally requires a differentiable policy parameterization for gradient-based learning.

## 4. Novelty vs. Prior Work

**Claimed novelty:** The g/h reward decomposition that generalizes surrogacy; the surrogate-importance-weighting estimator with a doubly-robust-style unbiasedness guarantee under two independent conditions; the proof that surrogate importance weighting has provably lower variance than vanilla importance weighting; and the LOPE-PG extension to offline policy learning for a long-term objective.

**Prior work most heavily built on:**
- Athey, Chetty, and Imbens, "Combining Experimental and Observational Data to Estimate Treatment Effects on Long-Term Outcomes," and Athey, Chetty, Imbens, and Kang, "The Surrogate Index" — the LCI/surrogacy foundation LOPE generalizes.
- Dudík, Langford, and Li, "Doubly Robust Policy Evaluation and Learning," ICML 2011, and Dudík, Erhan, Langford, and Li, Statist. Sci. 2014 — the DR estimator LOPE is benchmarked against and structurally extends.
- Rosenbaum and Rubin, "The Central Role of the Propensity Score in Observational Studies for Causal Effects," Biometrika 1983 — foundational IPS/propensity-score theory.
- Prentice, "Surrogate Endpoints in Clinical Trials: Definition and Operational Criteria," 1989, and Fleming, Prentice, Pepe, and Glidden, 1994 — the classical biomedical surrogacy criteria the surrogacy assumption is rooted in.
- Hohnhold, O'Brien, and Tang, "Focusing on the Long-Term," KDD 2015 — industry motivation.
- Saito and Joachims, "Off-Policy Evaluation for Large Action Spaces via Embeddings," ICML 2022, and related follow-ups — the large-action-space OPE literature LOPE's reward-decomposition idea is related to.

## 5. Dataset Availability

| Dataset | Source | Size | Public? |
|---|---|---|---|
| Synthetic contextual bandit | Generated | 1,000 users, |A|=30 | Public (code: https://github.com/usaito/www2024-lope) |
| Spotify homepage recommendation A/B test | Spotify (May 2023, 3 weeks) | ~4M users, >1,000 candidate items | Proprietary, not released |

## 6. Community Reaction

Not assessed in NotebookLM mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Long-term Off-Policy Evaluation and Learning," Saito, Abdollahpouri, Anderton, Carterette, Lalmas (Cornell University / Spotify), WWW 2024 (ACM Web Conference, Singapore). URL: not provided in extracted content (code repository: https://github.com/usaito/www2024-lope). |
| 2 | Source type | Industry paper (Spotify-affiliated academic collaboration). |
| 3 | Direction | D3 |
| 4 | Problem setting | Off-policy evaluation and learning of a long-term policy value V(π) using only historical logs (with both short- and long-term rewards) and, optionally, a short-term-only experiment on the target policy — without running a long-term online experiment. |
| 5 | Objective and label definition | Long-term reward r ∈ [0, r_max] (e.g., an annual user-activeness indicator in the general framing; week-3 (day-21) total streams in the real-world application). Short-term surrogate reward s (multi-dimensional; week-1/day-7 streams, clicks, likes, dislikes in the application). No formal censoring/survival handling — the historical dataset D_H requires fully realized (x,s,r) triples, so delay is handled by dataset construction (waiting out the full horizon for the historical/training set) rather than by a statistical delay model. |
| 6 | Prediction or incrementality | Incrementality/causal-effect estimation of a policy's value. Paper's own wording: "the main goal of this work is to develop an estimator V̂ that can accurately estimate the long-term value of a new model... without running a long-term experiment," and the framework is explicitly positioned within "the literature on long-term causal effect estimation." V(π) is the expected long-term reward under a counterfactual policy π, a causal quantity (policy value), estimated via importance weighting/off-policy correction — not a raw outcome prediction. |
| 7 | Model architecture | Not architecture-specific: a reward-regression model ĥ(x,a,s) (e.g., neural network, 3 hidden layers used in policy-learning experiments) for the action effect, plus a classifier for the logging policy π₀(a|x,s) used to derive the surrogate importance weight via Bayes' rule. |
| 8 | Credit assignment | Pointwise, item-level: the long-term reward r is assigned directly to the single recommended action a (a specific playlist/album/podcast on the homepage) chosen for a given user request x. No slate-level or coordinate-based credit assignment is modeled. |
| 9 | Training data and counterfactual handling | Historical dataset D_H = {(xᵢ,sᵢ,rᵢ)} generated by an arbitrary logging policy π₀ (contains both short- and long-term rewards), optionally supplemented by a short-term-only experiment dataset D_S = {(xᵢ,sᵢ)} generated by running the new policy π₁ briefly. Counterfactual correction is via the surrogate importance weight w(x,s)=π₁(s|x)/π₀(s|x), estimated via Bayes' rule using a classifier for π₀(a|x,s) rather than requiring direct estimation of the high-dimensional marginal π₀(s|x). |
| 10 | Offline and online evaluation | Offline only, on both synthetic data (MSE/bias/variance vs. ground-truth policy value, with statistical significance testing) and real-world Spotify logs (MSE vs. the actual outcome of a completed 3-week, 4-million-user online A/B test, for three deployed policies). No live online deployment of LOPE or LOPE-PG-learned policies is reported. |
| 11 | Reported gains | Synthetic: up to 71% MSE reduction vs. LCI at large sample size (n=1,000) under moderate surrogacy violation; up to 45% MSE reduction vs. DR under high long-term-reward noise (σᵣ=9.0); LOPE-PG outperforms DR-PG by ~60% (n_H=500) to ~80% (σᵣ=9.0) in policy-gradient learning. Real-world Spotify homepage A/B test: LOPE achieves a 9.2–15.0% MSE reduction vs. DR (next-best method) in estimating the long-term value of three deployed policies, using week-1 engagement as surrogate for week-3 streams. |
| 12 | Applicability to a two-sided dating recommender | Gives a directly usable offline evaluation-and-learning recipe for optimizing a delayed retention/revenue objective from historical logs plus a short-term experiment — the closest paper in this batch to an implementable migration mechanism. It is entirely one-sided (single-user policy value) with no reciprocity, congestion, or fairness treatment. |
| 13 | Unverified claims | None major; the authors are notably self-critical, explicitly flagging the low-noise negative result, the untested comparability assumption under non-stationarity, and the unaddressed short-term-reward-representation question as open limitations rather than asserting unqualified superiority. |

## Project Relevance

Directly and centrally answers **Q1** (making a long-horizon reward the optimization target via off-policy value estimation rather than waiting for the full horizon), **Q5** (LOPE's core estimand V(π) is a policy-level causal/incremental quantity, and the g/h decomposition is explicitly a generalization of how uplift/surrogate reasoning combines with an OPE estimator), **Q6** (its offline-evaluation methodology — the surrogacy-violation stress test, the doubly-robust-style unbiasedness proof, and the real-A/B-test-grounded validation — is arguably the strongest template in this batch), and **Q8** (LOPE-PG is literally a mechanism for learning an improved policy from historical logs plus a brief short-term experiment, without a full long-run online test — directly answering how to migrate off a "wait for the full horizon" regime).

Partially informs **Q4** (the g/h decomposition is a principled alternative to a fixed or learned fusion of separate short-term/long-term heads, though the paper does not frame it that way) and **Q3** (label/horizon choice is demonstrated concretely — week-1 surrogate, week-3 target — but the paper offers no general guidance on horizon selection beyond the specific application). Does not address **Q2** (pointwise item-level credit assignment only, no slate) or **Q7** (no two-sided market, congestion, or fairness treatment).

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2024_Blog_LOPE_Estimating-Long-Term-Outcome-Algorithms.md](./2024_Blog_LOPE_Estimating-Long-Term-Outcome-Algorithms.md) | Related Work / Experiments | Names this paper's method (`LOPE`) |

_1 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `LOPE` across all 133 cards._

## Meta Information

- **Authors/Affiliations:** Yuta Saito (Cornell University); Himan Abdollahpouri, Jesse Anderton, Ben Carterette, Mounia Lalmas (Spotify).
- **Venue:** WWW 2024 (ACM Web Conference), Singapore
- **Year:** 2024
- **Relevance:** Core
- **Priority:** 1
- **NotebookLM source:** `nlm:7fee3f6b-6faa-436e-aa21-d9477fef7739`
