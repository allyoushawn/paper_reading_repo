# A Best-of-Both Approach to Improve Match Predictions and Reciprocal Recommendations for Job Search

- **notebook source_id:** `e44c714b`
- **extraction method:** direct PDF read (NotebookLM unavailable)

## Summary
Reciprocal recommendation (job search, dating) requires predicting mutual match probability, but directly predicting the observed match label ("direct match prediction," DMP) suffers because true matches (both sides acting positively) are extremely sparse. The common workaround, "predict-then-aggregate" (PtA), trains two separate one-directional models (company→seeker, seeker→company) and combines them with a fixed aggregation function (product or harmonic mean), but this introduces biased error propagation since the two directions have very different label densities. The paper proposes **Best-of-Both (BoB)**: compute a **pseudo-match score** as a weighted average of the true (sparse, accurate) match label and the PtA predictions (dense, less accurate), then train a single meta-model to directly predict this pseudo-score, with the weighting parameter α optionally personalized per user/segment. On offline experiments over real production data from the Japanese job-search platform Wantedly Visit, BoB with a global α beats all baselines, and BoB with personalized (per-activity-segment) α does best of all, especially for smaller/less-active user segments.

## Method
- **Problem setup:** companies `c ∈ C` and job seekers `j ∈ J`; `p^{c→j}` = probability company c scouts seeker j, `p^{j→c}` = probability seeker j responds positively to company c; true match probability `m(c,j) = p^{c→j} · p^{j→c}`. Goal: produce optimal ranking `σ*_c = argsort_j m(c,j)` of job seekers for each company.
- **Direct Match Prediction (DMP):** learn `m̂` directly from observed binary match labels `m_i ∈ {0,1}` via a supervised loss `argmin Σ ℓ(m̂(c_i,j_i), m_i)`. Suffers from extreme label sparsity (match requires both actions to co-occur).
- **Predict-then-Aggregate (PtA):** learn `p̂^{c→j}` and `p̂^{j→c}` as two separate binary-classification models from the (denser) one-directional action labels, then combine via an aggregation function M — e.g., product `M(x,y)=x·y` or harmonic mean `M(x,y)=2xy/(x+y)`. Weakness: the two directions differ substantially in density/accuracy (the "first" interaction, e.g. scouting, is denser than the "response"), so naive aggregation propagates the noisier model's errors into the final ranking.
- **BoB — pseudo-match scores:** `s_pseudo(c,j;α) = α·m(c,j) + (1-α)·(p̂^{c→j}·p̂^{j→c})`, a weighted average of the true (sparse) match label and the PtA product prediction, α ∈ [0,1] controlling the balance (α=1 recovers pure true-label reliance, α=0 recovers pure PtA).
- **Meta-model:** train a single model `f̂ = argmin Σ ℓ(f'(c,j), s_pseudo(c,j;α))` (Gradient Boosting Decision Tree in the experiments) to directly predict the pseudo-score; final ranking `σ_c^bob = argsort_j f(c,j)`.
- **Personalized weights:** generalize α to a pair-specific (or segment-specific) `α_{c,j}`, allowing the true-label-vs-prediction balance to adapt per company/segment — e.g., more active companies with denser accurate history can rely more on predictions, less active ones benefit more from true labels.
- Algorithm 1 gives the full pseudo-code: (1) run PtA to get the two directional models, (2) compute pseudo-match scores with given weights, (3) train meta-model on pseudo-scores.

## Datasets and Baselines
- **Dataset:** production data from **Wantedly Visit** (Japanese job-search platform connecting job seekers and companies with a scouting feature), Nov 2023–Feb 2024. Match defined as company scout + positive seeker response. Features from profile info (education, job category, work history, skills for seekers; company/job-posting info for companies) and action logs.
- **Baselines:** Scout-Only (`M = p̂^{c→j}`), Reply-Only (`M = p̂^{j→c}`), Multiplication (`M = p̂^{c→j}·p̂^{j→c}`), Harmonic Mean.
- **BoB variants tested:** global α ∈ {0.0, 0.25, 0.5, 0.75, 1.0}, and personalized α by three company-activity segments (High/Middle/Low), each explored at α ∈ {0.0, 0.25, 0.5, 0.75} (1.0 excluded per prior experience showing it degrades performance).
- Meta-model: Gradient Boosting Decision Tree (GBDT), time-based train/test split, 5-fold cross-validation for hyperparameter tuning.

## Results
- **Table 1 — NDCG@10 on test data:**
  - Scout-Only: 0.0592; Reply-Only: 0.0886; Multiplication: 0.0969; **Harmonic Mean (best baseline): 0.0979**
  - BoB (global α=0.00): 0.1017; **BoB (global α=0.25, best global): 0.1021**; BoB (α=0.50): 0.0926; BoB (α=0.75): 0.0944; BoB (α=1.00): 0.0932
  - **BoB (personalized α): 0.1050** — best overall, beating the best baseline (0.0979) and the best global-α BoB (0.1021).
  - Optimal segment-specific α: High Activity = 0.0, Middle Activity = 0.75, Low Activity = 0.75 (text) — note Section 5.4.3 states "the optimal α values for the (High, Middle, Low) activity segments are 0.0, 0.75, and 0.75."
- **Segment analysis (Figure 2):** High Activity segment shows the largest relative NDCG@10 improvement over baseline at low α (0.0–0.25); Middle Activity segment shows no improvement over baseline at any α (slight degradation); Low Activity segment performs best at higher α (0.75), i.e., leans more on true match labels rather than predictions.
- Confidence/statistical testing: not reported as formal p-values; results are reported as point NDCG@10 comparisons across a single time-based test split with 5-fold CV for hyperparameter selection (no confidence intervals given in the read pages).
- Authors report the offline evaluation pipeline "has been validated for consistency with the online experiment results on the platform," implying real online deployment/validation exists, though the reported numeric results here are offline.

## Limitations
- The Middle Activity segment showed **no improvement over baseline** and slight degradation at some α — the authors attribute this to that segment having neither dense-and-accurate true labels (like High Activity) nor sufficiently reliable predictions, but this is a genuine limitation of the method for a meaningful sub-population.
- The paper explicitly separates match-prediction quality from **congestion** (the phenomenon where highly desirable users receive excessive attention and can't respond to all of it) and states this is out of scope, citing Su et al. and Tomita et al. as work that could be combined with BoB in future work — the paper does *not* address allocation/capacity constraints itself, only the match-probability estimation step.
- Optimal α must be tuned via cross-validation and varies substantially by segment, adding operational complexity versus a fixed aggregation rule.
- Only tested on a single job-search platform/dataset; generalization to other reciprocal-recommendation domains (e.g., dating) is stated as future work, not demonstrated.

## Heavily Cited Prior Works
- Su, Bayoumi & Joachims (2022) — "Optimizing rankings for recommendation in matching markets" (WWW) — addresses congestion, explicitly flagged as future integration target
- Tomita, Togashi, Yashizume & Ohsaka (2023) — "Fast and examination-agnostic reciprocal recommendation in matching markets" (RecSys)
- Tomita, Togashi & Moriwaki (2022) — "Matching theory-based recommender systems in online dating" (RecSys)
- Zheng, Hou, Zhao, Song & Zhu (2023) — "Reciprocal sequential recommendation" (RecSys)
- Yıldırım, Azad & Öğüdücü (2021) — "BideepFM: a multi-objective deep factorization machine for reciprocal recommendation"
- Luo, Yang, Xin, Fang, Yang, Chen, Zhang, Liu — "Rcrn: a reinforced random convolutional network based reciprocal recommendation approach for online dating" (arXiv 2020)
- Xia, Liu, Sun & Chen (2015) — "Reciprocal recommendation system for online dating" (ASONAM)

## Bibliography Fields
- **title:** A Best-of-Both Approach to Improve Match Predictions and Reciprocal Recommendations for Job Search
- **authors or organization:** Shuhei Goda, Yudai Hayashi (Wantedly, Inc., Tokyo), Yuta Saito (Cornell University)
- **year:** 2024
- **venue or type:** Not clearly stated in the read pages — arXiv preprint (cs.IR) with a CC BY 4.0 "copyright for this paper by its authors" notice, consistent with a workshop-style publication; no ACM/IEEE proceedings banner appears in the extracted pages.
- **link:** https://arxiv.org/pdf/2409.10992
- **tier tag:** Tier 2 applied-on-real-platform-data (production data from Wantedly Visit; offline evaluation explicitly stated to be validated against online experiment results)
- **what they did (≤80 words):** Proposed pseudo-match scores — a weighted blend of sparse-but-accurate true match labels and dense-but-noisier one-directional match predictions — as the training target for a single meta-model, replacing the common but error-propagation-prone "predict separately then aggregate" approach to reciprocal recommendation. Showed personalizing the blend weight by company-activity segment further improves ranking quality on real job-search production data.
- **mechanism relevant to two-sided balancing (≤50 words):** Directly implements Layer 1 (reciprocal scoring): a like-back-probability-style estimate `p^{c→j}·p^{j→c}` blended with true bidirectional match outcomes via a tunable, segment-personalizable weight, trained as a single meta-model rather than two decoupled directional models — improves ranking quality especially for less-active/sparser segments.
- **fit for a dating app:** high — the problem formulation (mutual scout+response, sparse true matches, two asymmetric directional signals) is structurally identical to dating like/like-back, and the personalized-α finding (different populations need different true-label-vs-prediction weighting) maps directly onto the project's concern that low-activity/low-desirability users need different modeling treatment than highly active ones.
- **confidence that the item is real and described correctly:** high — read the full paper (introduction through references) directly from the PDF; venue could not be confirmed from the extracted text, flagged above rather than guessed.

## Project Relevance
Directly addresses **Layer 1 (reciprocal scoring)** — this is essentially a paper about how to estimate like-back probability well under extreme label sparsity, which is exactly the modeling problem for reciprocal scoring conditioned on the other side. Its personalized-weighting result (segment-specific α, with Low Activity users benefiting most from leaning on true labels rather than noisy directional predictions) is a concrete, evidence-backed argument for why a dating app's reciprocal scorer should not use a single global aggregation rule across all users — low-activity/low-desirability users likely need different treatment than high-activity ones, which resonates with the project's concern about most users getting few matches. The paper explicitly acknowledges but does **not** address capacity/congestion (Layer 2) — it explicitly defers that to Su et al. and Tomita et al., naming it as a natural extension, so this source should be read as a Layer 1 building block, not a full solution to the exposure-allocation problem.

**Disanalogy to flag:** none major — job search (company scouts, seeker replies) is one of the closest available analogues to dating reciprocal-liking among the sources reviewed; the main structural difference is that "companies" are organizations that can plausibly scout many candidates in parallel with less personal reply-capacity scarcity than an individual dater, though the paper's own segment analysis (High/Middle/Low activity) shows this scarcity/activity heterogeneity is still present and material even on the company side.

## Reverse Citation Map
