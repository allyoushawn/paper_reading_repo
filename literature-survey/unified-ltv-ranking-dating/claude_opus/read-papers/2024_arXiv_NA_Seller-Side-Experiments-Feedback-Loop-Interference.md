# Paper Analysis: Seller-Side Experiments under Interference Induced by Feedback Loops in Two-Sided Platforms

**Source:** `/Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/2401.15811.pdf` (arXiv:2401.15811v2)
**Date analyzed:** 2026-08-17

## 1. Summary

Zhihua Zhu, Zheng Cai, Liang Zheng (Tencent) and Nian Si (Booth School of Business, University of Chicago) study seller-side (supply-side/producer-side) A/B tests on two-sided platforms whose ranking scores are continuously adjusted by a "pacing algorithm" — a feedback controller that raises a seller's score when its cumulative consumption (ad budget spend, sales rate, exposure count) is low and lowers it when consumption is high, in order to hit a target pacing curve. The paper's core claim: this pacing feedback loop creates a *second, distinct* source of interference beyond the direct treatment/control competition that the counterfactual interleaving design (Ha-Thuc et al. 2020; Nandy et al. 2021) — the design "widely implemented... at Facebook, TikTok, and Kuaishou" per the paper — was built to fix, and counterfactual interleaving does not fix this second source.

Methodology: the authors build a continuous-time state-space model of the recommendation pipeline over the experiment window [0,H]. Each seller i has a raw estimated score ê_i(t), a state process S_i(t) (cumulative consumption), a pacing-adjusted ranking score r_i(t)=Ψ(S_i(t),ê_i(t)) with Ψ non-increasing in S (the damping effect), a selection indicator I_i(t)=𝟙{f_i(...)≥0}, and an observed metric O_i(t)=I_i(t)e_i(t). The ground-truth estimand is the Global Treatment Effect, GTE=(1/N)Σ_i∫_0^H[O_i^GT(t)−O_i^GC(t)]dt, comparing the fully-global-treatment and fully-global-control regimes. They analyze two designs — naive seller-side experiments and counterfactual interleaving — under two treatment types (item-performance treatments and ranking-algorithm treatments), first without feedback loops (Propositions 1–2: both designs unbiased, Table 1) and then with a damping pacing algorithm present (Theorems 1–3: **both designs underestimate the true GTE**, Table 2), with a monotonicity/damping argument for why. They confirm the theory with a real production case study at Tencent and propose a lightweight interference-detection heuristic.

## 2. Experiment Critique

**Design.** Purely theoretical derivation (propositions and theorems with proofs in Appendix A) plus one real-world empirical case study (Section 5) — no synthetic simulation study is included, which is a gap relative to the paper's own companion piece (Si 2023, the next paper in this batch) and to Nandy et al. (2021), both of which pair theory with simulation before going to production data.

**Statistical validity.** The theoretical results are clean sign-of-bias statements (E[ĜTE]≤GTE under damping) rather than magnitude bounds; no variance or confidence-interval theory is given for the estimator itself. The one empirical result reports 95% confidence intervals (advertising cost −23% [−34%,−12%]; views −27% [−38%,−15%]; GMV −21% [−34%,−9%]), but these CIs describe the *biased* counterfactual-interleaving estimate, not the true GTE, which is never independently measured.

**Online experiments.** One real production A/B test at Tencent's advertising-recommendation platform (10% control ads / 10% treatment ads, counterfactual interleaving design, λ-adjustment pacing mechanism). This is the paper's central piece of evidence: despite "simulations and A/A tests consistently indicating the superiority of the treatment strategy," the live counterfactual-interleaving experiment showed strongly negative effects on all three metrics — a sign flip, not just a magnitude discrepancy.

**Reproducibility.** The mathematical framework, all propositions/theorems and their proofs (Appendix A) are fully specified and reproducible. The production case study is not reproducible (internal Tencent data); the paper does not release code or data.

**Overall.** The theory is rigorous but narrow (sign-of-bias only, single damping-monotonicity assumption); the practical payoff is the production anecdote, which is compelling but singular — one platform, one feature, one time window. The authors explicitly flag that no correction method is proposed, only a detection heuristic (see Reference Card field 13).

## 3. Industry Contribution

**Deployability.** The proposed interference-detection method is cheap to deploy inside an existing counterfactual-interleaving pipeline: log and compare the average ranking score of treatment sellers vs. control sellers when *both are scored under the same algorithm* (e.g., compare {r_i^T : i∈treatment} against {r_i^T : i∈control}, and separately {r_i^C : i∈treatment} against {r_i^C : i∈control}). A systematic divergence over the course of the experiment (as shown in the paper's Figure 4, where the treatment group's average pacing multiplier λ̄^T visibly diverges from control and "other" groups toward the end of the day) signals that feedback-loop interference is corrupting the design.

**Problems solved.** Gives platforms a documented failure mode of a design many already treat as the gold standard: counterfactual interleaving is unbiased *only* in the absence of feedback loops, and any platform running a pacing/budget-control/exposure-throttling mechanism between the ranking score and what gets served needs an additional check.

**Engineering cost.** Low for the diagnostic itself (an extra logged comparison, no serving-path change). But the paper does **not** provide a fix — only detection — so the cost of actually resolving the underlying bias (e.g., redesigning the pacing algorithm's interaction with the experiment, or accepting a directionally-known bias) is left as unaddressed future work.

## 4. Novelty vs. Prior Work

**Claimed novelty.** First formal demonstration that the counterfactual interleaving design — assumed reliable by Ha-Thuc et al. (2020) and Nandy et al. (2021) and adopted industry-wide — remains biased (and, empirically, can even flip sign) in the presence of pacing-algorithm feedback loops; the paper further supplies a mathematical model of *why* (the damping-effect assumption on Ψ) and a lightweight empirical diagnostic.

**Prior work.** Ha-Thuc, Dutta, Mao, Wood, and Liu, "A counterfactual framework for seller-side A/B testing on marketplaces," SIGIR 2020, and Nandy, Venugopalan, Lo, and Chatterjee, "A/B testing for recommender systems in a two-sided marketplace," NeurIPS 2021 (= UniCoRn, the direct companion paper in this survey's D8 batch) — the counterfactual interleaving design this paper stress-tests. Wang and Ba, "Producer-side experiments based on counterfactual interleaving designs for online recommender systems," arXiv:2310.16294 (2023) — a tie-breaking-rule enhancement to the same design. Nian Si, "Tackling interference induced by data training loops in A/B tests: A weighted training approach," arXiv:2310.17496 (2023) — the direct companion paper by the same corresponding author, addressing the sibling mechanism of interference through *ML model retraining* rather than through a *pacing algorithm's internal state* (see Project Relevance for the distinction). Holtz, Brennan, and Pouget-Abadie, "A study of 'symbiosis bias' in A/B tests of recommendation algorithms," arXiv:2309.07107 (2023) — a related feedback-loop bias concept. Liu, Mao, and Kang, "Trustworthy and powerful online marketplace experimentation with budget-split design," KDD 2021 (= this batch's paper 3) — an alternative design for budget-constrained marketplaces. Karlsson, "Feedback control in programmatic advertising," IEEE Control Systems Magazine 2020 — background on pacing algorithms. Fan, Si, and Zhang, "Calibration matters: Tackling maximization bias in large-scale advertising recommendation systems," arXiv:2205.09809 (2022) — the related overestimation-bias mechanism motivating Tencent's λ-adjustment strategy in the case study.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| Tencent advertising-recommendation production traffic | Real production A/B test (10% control ads, 10% treatment ads) | No — internal Tencent data | Used only for the Section 5 empirical case study; no summary statistics on scale (users/sellers/requests) given beyond the reported percentage lifts and CIs |

No synthetic or public dataset is used anywhere in the paper; all other results are purely theoretical (propositions/theorems).

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Seller-Side Experiments under Interference Induced by Feedback Loops in Two-Sided Platforms," Zhihua Zhu, Zheng Cai, Liang Zheng (Tencent), Nian Si (Booth School of Business, University of Chicago), arXiv, 2024 (arXiv:2401.15811v2), https://arxiv.org/abs/2401.15811 |
| 2 | Source type | Industry paper (Tencent authors + academic co-author), arXiv preprint, not confirmed peer-reviewed at a venue |
| 3 | Direction | D8 |
| 4 | Problem setting | Seller-side (supply-side) randomized A/B tests on two-sided platforms whose ranking scores are continuously adjusted by a "pacing algorithm" (a feedback controller reacting to cumulative budget spend, sales rate, or exposure count); the pacing feedback loop creates interference that biases both naive seller-side A/B tests and the counterfactual-interleaving design meant to fix cannibalization bias |
| 5 | Objective and label definition | Not applicable — experiment design, not a ranking objective. The estimand is the Global Treatment Effect, GTE=(1/N)Σ_i∫_0^H[O_i^GT(t)−O_i^GC(t)]dt, over a fixed experiment window [0,H]; there is no ML label, prediction horizon, or delay/censoring-handling mechanism |
| 6 | Prediction or incrementality | Incrementality — the entire paper concerns estimating the Global Treatment Effect (a causal contrast between global-treatment and global-control counterfactual regimes), explicitly distinguishing the "true metric" e_i(t) from the "observed metric" O_i(t)=I_i(t)e_i(t) |
| 7 | Model architecture | Not a predictive/ranking model. A continuous-time dynamical-systems model of the recommendation pipeline (ranking score r_i(t)=Ψ(S_i(t),ê_i(t)); state update dS_i(t)/dt=Γ(S_i(t),e_i(t),r_i(t),I_i(t),t); selection I_i(t)=𝟙{f_i(...)≥0}) layered analytically on top of two existing experiment designs (naive seller-side A/B and Ha-Thuc/Nandy counterfactual interleaving) |
| 8 | Credit assignment | Continuous-time, seller-level, not user-level-to-item-level: the observed metric O_i(t)=I_i(t)e_i(t) is attributed entirely to seller i at time t and integrated over the whole experiment window (∫_0^H O_i(t)dt per seller); there is no decomposition of a delayed user-level outcome onto individual impressions — the unit of both randomization and outcome accounting is the seller itself |
| 9 | Training data and counterfactual handling | No ML training — a causal-inference correction/diagnostic layer on top of production ranking scores. Randomized unit: seller (producer/candidate side), split into treatment and control (plus an "other" group under interleaving). Bias, with a damping pacing algorithm present: both the naive design and the counterfactual-interleaving design **underestimate** the true GTE (Theorems 1–3); in the real Tencent deployment the counterfactual-interleaving estimate went further and flipped sign entirely (measured −23% cost / −27% views / −21% GMV vs. a positive effect predicted by simulation and A/A tests), attributed to the treatment group's pacing multiplier λ^T diverging downward from the control group's λ^C over the course of the day (Figure 4) |
| 10 | Offline and online evaluation | Offline: none — purely theoretical (propositions/theorems, proofs in Appendix A), no synthetic simulation study. Online: one real production A/B test at Tencent's advertising platform (10% control / 10% treatment, counterfactual interleaving design), reporting point estimates and 95% CIs for advertising cost, views, and GMV |
| 11 | Reported gains | Not a "gains" paper in the ranking sense — the reported production numbers demonstrate a measured **bias**, not a genuine improvement: advertising cost −23% [95% CI −34%,−12%], views −27% [−38%,−15%], GMV −21% [−34%,−9%] (Tencent advertising platform, counterfactual-interleaving A/B test), directly contradicting simulations and A/A tests that indicated the treatment strategy was superior |
| 12 | Applicability to a two-sided dating recommender | Directly warns against trusting a candidate-side (viewee-side) A/B test on the dating app's ranking model if any pacing/throttling mechanism sits between the score and what gets shown — e.g., a daily match-cap, an exposure-balancing algorithm for popular profiles, or any congestion-control layer. The paper's cheap diagnostic (compare treatment-vs-control rankings under the same algorithm) is a pre-check the team could run before trusting any candidate-side retention A/B result |
| 13 | Unverified claims | The production case study's true GTE is never independently confirmed — no ground truth exists outside the biased experiment itself, so the causal narrative (sign-flip caused by feedback-loop damping, not by the new strategy genuinely underperforming) rests on the theoretical model plus indirect evidence (the diverging λ curves in Figure 4, and the A/A-test/simulation-vs-live discrepancy), not a direct unbiased remeasurement. The paper explicitly states no correction method is proposed — only detection — leaving the actual fix as future work |

## Project Relevance

Speaks to **Q6** (evaluating a ranking change under two-sided interference), specifically the failure mode where a *feedback-controlled serving mechanism* — not just direct treatment/control competition — corrupts a seller-/candidate-side experiment. Precision note for the survey: this paper's mechanism is **not** the "data training loop" the batch brief emphasizes for this pair — the ML model itself is never retrained in this paper's model; instead, a separate pacing algorithm's internal state S_i(t) (cumulative consumption) reacts to the experiment's own outcomes and feeds back into the ranking score. That is a distinct-but-related mechanism from this batch's paper 2 (Si, 2023, arXiv:2310.17496), which is explicitly about the ML model itself being retrained on logged experimental data (a genuine training-data loop). Both matter for the project: a unified retention model would be exposed to Si (2023)'s mechanism directly (the model retrains on logged outcomes that already reflect treatment effects), while this paper's pacing-loop mechanism would apply if the dating app has any congestion-control or exposure-throttling layer sitting between the unified model's score and what gets served to a candidate — plausible given the project's stated congestion constraint (B's attention is a shared, limited resource). The paper does not address Q1–Q5, Q7, or Q8: there is no training objective, no delayed-label handling, no reciprocity/fairness treatment, and no migration-path discussion — it is narrowly and usefully an evaluation-design warning, not a modeling paper.

## Papers That Mention This Paper (Reverse Citation Map)

_This paper proposes no distinctively-named method, so no automated reverse-citation match was possible._

## Meta Information

- **Authors:** Zhihua Zhu, Zheng Cai, Liang Zheng, Nian Si
- **Affiliations:** Tencent (Zhu, Cai, Zheng); Booth School of Business, University of Chicago (Si, corresponding author)
- **Venue:** arXiv, 2024 (arXiv:2401.15811v2, stat.ME)
- **Year:** 2024
- **Relevance:** Related
- **Priority:** 2
- **nlm:1423fb97**
