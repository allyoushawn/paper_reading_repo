# Paper Analysis: Multi-Objective Ranking Optimization for Product Search Using Stochastic Label Aggregation

**Source:** NotebookLM notebook `unified-ltv-ranking-dating` (source_id `f3865b86-af82-4689-bede-d274881b5f83`), https://dl.acm.org/doi/10.1145/3366423.3380122
**Date analyzed:** 2026-08-16

## 1. Summary

**Title:** Multi-Objective Ranking Optimization for Product Search Using Stochastic Label Aggregation
**Authors:** David Carmel, Elad Haramaty, Arnon Lazerson, Liane Lewin-Eytan (Amazon, Haifa, Israel)
**Venue / Year:** WWW 2020 (The Web Conference), pages 373–383

**Abstract (paraphrased):** Product-search ranking must satisfy multiple objectives (e.g., relevance and purchase likelihood). Label aggregation reduces this to single-objective learning by combining per-instance labels into one label. The paper shows that the standard deterministic aggregation methods (linear, lexicographic) cannot reach every Pareto-optimal solution, and proposes stochastic label aggregation — randomly assigning one objective's label per training query according to a chosen probability — proving it can reach any Pareto-optimal solution that a mixture of models could achieve, unlike deterministic aggregation.

**Key contributions:**
- Stochastic label aggregation: for each training query, flip a coin with probability α to decide whether every product under that query is labeled with objective 1 or objective 2.
- A theorem proving the family of stochastic-aggregation models exactly equals the Pareto-optimal-achievable set (M_stoch = Par(M|M*)), with a companion proof that deterministic aggregation provably cannot cover this same set.
- A two-phase architecture: train single-objective models first, then train a second-phase meta-model on their scores as features, optimized against an aggregated (e.g., stochastic) label — shown empirically to beat single-phase aggregation.
- Demonstration that the stochastic method's advantage grows as label granularity shrinks (e.g., toward binary labels), which is exactly the low-granularity regime common in production purchase/no-purchase labels.

**Methodology:** All rankers use XGBoost's LambdaMART (pairwise cross-entropy) as the base learning-to-rank model, over textual-similarity, semantic-similarity (FastText), and behavioral features. Stochastic aggregation: with probability α a training query's entire product list gets objective-1 labels, with probability 1−α it gets objective-2 labels; the expected cost is provably a linear mixture of each objective's individual cost, which lets the method sweep α to trace out the achievable trade-off curve. The two-phase variant adds the single-objective models' scores as input features to a second-stage model trained on the (stochastic or linear) aggregated label.

**Main results:** Across three datasets (aggregated and raw voice-shopping search, and a public web search dataset augmented with an inverse-title-length objective), the two-phase stochastic family fully dominates the trade-off curves of deterministic linear aggregation, lexicographic aggregation, and simple model-score fusion; the dominance gap widens as label granularity decreases.

## 2. Experiment Critique

**Design:** Three datasets from two different domains (voice product search, web product search) with two different objective pairs (relevance/purchase, relevance/inverse-title-length) is a solid design for testing generality. The paper explicitly separates two research questions — aggregation method (stochastic vs. deterministic vs. fusion) and architecture (one-phase vs. two-phase) — and reports each dimension separately.

**Statistical validity:** Each reported point on a trade-off curve is the average of a bucket of ~50 independently trained models (10 buckets across α ∈ [0,1]), which is a reasonable way to smooth training variance, though no explicit significance test is reported for curve separation between families.

**Online experiments:** None. The paper explicitly states online comparison against other MORO approaches is "out of the scope of this work" and left as future work — this is a purely offline study.

**Reproducibility:** The public web dataset is genuinely public (a Figure Eight / Appen e-commerce search relevance set), and hyperparameters (tree depth, learning rate, number of trees) are given in full. The two voice-shopping datasets are proprietary Amazon traffic and cannot be released, and the raw voice dataset additionally suffers from acknowledged presentation bias (most users are shown only one or two products).

**Overall:** The theoretical result (Theorem 1) is the paper's strongest asset — a clean, provable dominance argument rather than only an empirical one — but the complete absence of online validation is a real gap for an industry paper, one the authors themselves flag.

## 3. Industry Contribution

- **Deployability:** The method requires no architecture change to the base ranker (still LambdaMART); the only change is how training labels are assigned per query during data preparation, which makes it a low-risk retrofit onto an existing pairwise/listwise LTR pipeline.
- **Problems solved:** Directly solves the practical problem of *partially labeled* training data — because the stochastic and fusion families do not require every instance to carry both labels, the raw (mostly single-labeled) voice-shopping dataset could be used at all, whereas deterministic aggregation methods were mathematically excluded from that dataset entirely.
- **Engineering cost:** Very low marginal engineering cost for the single-phase stochastic variant (a per-query coin flip at label-generation time); the two-phase variant costs an extra model-training stage and doubles inference-time feature computation (two upstream model scores must be computed as inputs to the final model).
- **Ranking pipeline fit:** Fits a batch-trained, offline-refreshed LTR pipeline; the paper does not address real-time/streaming constraints the way the Alibaba or YouTube industry papers in this survey do.

## 4. Novelty vs. Prior Work

**Claimed novelty:** First proof that stochastic label aggregation can reach *any* Pareto-optimal solution reachable by a mixture of models, and the first proof that deterministic aggregation provably cannot — a theoretical result the authors position directly against Lin et al.'s PE-LTR, noting PE-LTR proves its solutions lie on the Pareto frontier but not that all frontier points are reachable.

**Prior work it builds on / compares against:**
- Momma et al., "Multi-objective Relevance Ranking" (2019) — ε-constraint / Augmented Lagrangian MORO approach for product search objectives (relevance, purchase, quality, rating, return rate).
- Svore et al., "Learning to Rank with Multiple Objective Functions" (2011) — pairwise click-based objective combination; source of the lexicographic aggregation baseline.
- Marler & Arora, survey of multi-objective optimization methods (2004) — general theoretical framing.
- Burges, "From RankNet to LambdaRank to LambdaMART" — base single-objective LTR algorithm used throughout.
- Lin et al., "A Pareto-Efficient Algorithm for Multiple Objective Optimization in E-Commerce Recommendation" (2019) — directly contrasted as a gradient-descent scalarization method that proves membership in, but not coverage of, the Pareto frontier.
- Wu et al., "Turning Clicks into Purchases: Revenue Optimization for Product Search in E-Commerce" (2018) — nested click/purchase framework comparison.

## 5. Dataset Availability

| Dataset | Type | Size | Public? |
|---|---|---|---|
| Aggregated voice dataset | Amazon voice product search, human-annotated relevance + 6-week purchase ratio | 27K queries, 54K products, both labels on every pair | Not public |
| Raw voice dataset | Amazon voice product search logs, 2 months | 360K queries, ~3.8M products; only 30% have relevance label, 70% have purchase label | Not public |
| Public web dataset | E-commerce search relevance (Figure Eight / Appen), synthetically augmented with Inverse Title Length | 1K queries, 20K products | Public |

## 6. Community Reaction

Not assessed in NotebookLM mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors or company, venue, year, URL | Multi-Objective Ranking Optimization for Product Search Using Stochastic Label Aggregation; David Carmel, Elad Haramaty, Arnon Lazerson, Liane Lewin-Eytan (Amazon); WWW 2020; https://dl.acm.org/doi/10.1145/3366423.3380122 |
| 2 | Source type | Industry paper (Amazon, peer-reviewed at WWW) |
| 3 | Direction | D1 |
| 4 | Problem setting | Product-search ranking that must jointly satisfy relevance and purchase-likelihood (or a third synthetic objective, inverse title length), addressed by reducing multi-objective ranking to single-objective learning-to-rank via label aggregation. |
| 5 | Objective and label definition | Per query-product pair, one of two labels — relevance R (human-annotated majority vote, [0,1] or 1–4 graded) or purchase P (purchase count ÷ impression count over a fixed 6-week or 2-month historical window). Stochastic aggregation assigns the *entire query's* product list to one objective's label via a per-query coin flip with probability α, rather than blending labels per-instance. No delayed-feedback or censoring model — purchase ratios are computed from a closed historical window, not from an explicit delay/censoring distribution. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. The task is explicitly framed as scoring a product to match a target ranking order induced by relevance/purchase labels, with no causal or exposure-effect language. |
| 7 | Model architecture | Any single-objective LTR algorithm can be the base learner; all experiments use XGBoost's LambdaMART (pairwise cross-entropy). Two model families: single-phase (train directly on the aggregated label) and two-phase (train independent single-objective models first, then a second-stage model on their scores as features, targeting the aggregated label). |
| 8 | Credit assignment | Coarse and query-level, not user- or session-level: the coin flip that decides which objective's label applies is made once per training query and applied to every product under that query — there is no mechanism for assigning a delayed, user-level outcome down to a specific single impression. |
| 9 | Training data and counterfactual handling | Historical query-product logs with pre-computed relevance and/or purchase-ratio labels; no propensity weighting or counterfactual correction. Stochastic and fusion families tolerate partially labeled data (only one of the two labels present); deterministic aggregation requires complete dual-labeled data, which the authors note limits it to small, human-annotation-cost-bounded, frequent-query-biased samples. |
| 10 | Offline and online evaluation | Offline only, via NDCG@5 (plus P@1, P@3, P@5, MRR@5 reported as showing similar trends) across the trade-off curve as α sweeps [0,1]. No online evaluation; the authors state comparison in a live product-search system is left to future work. |
| 11 | Reported gains | Two-phase stochastic (2phase-stoch) fully dominates the trade-off curves of 2phase-linear, 1phase-linear, 1phase-stoch, and fusion on all three datasets (aggregated voice, raw voice, public web with NDCG@5). Concretely, on the raw dataset, two-phase optimization of the purchase objective alone reached NDCG@5 = 0.493 versus 0.395 for single-phase. Deterministic linear methods "cover only a very limited part" of the trade-off curve — a dominance claim backed by the trade-off plots rather than a single summary statistic. |
| 12 | Applicability to a two-sided dating recommender | Low direct applicability: relevance and purchase are both same-side, non-delayed, non-reciprocal signals, and the paper explicitly excludes any two-sided, supplier/consumer, or platform-congestion consideration from its own scope (mentioning it only as related work by Nguyen et al.). The transferable idea is the stochastic-label mechanism itself — a way to combine a short-term proxy and a sparser target label without requiring every training instance to carry both. |
| 13 | Unverified claims | The claim that the two-phase architecture's advantage stems from "implicit relationships between objectives" learned via the intermediate score features is offered as the authors' explanation, not something the paper isolates experimentally from the architecture's added capacity — the depth-sweep experiment shows richer single-phase models close much of the gap, which the authors themselves use to partially attribute the two-phase gain to model capacity rather than purely to architecture. |

## Project Relevance

Relevant to **Q4** (fusion mechanism taxonomy): stochastic label aggregation is a third, distinct point in the fusion design space beyond "fixed weights" and "PE-LTR-style learned scalarization weights" — it fuses objectives at the *label* level via randomized query-level assignment rather than at the loss or score level, and the two-phase variant is architecturally similar to a "short-term head feeding a long-term head" pattern relevant to **Q4/Q8** migration paths (train single-objective models first, then a combiner). Also informative for **Q3**, negatively: it is a clear illustration of the "sparsity/partial-labeling" problem the dating app's low base rates and delayed labels will make far worse, and its solution (tolerate partial labels rather than requiring joint labels) is directly reusable framing.

**Low project relevance** for the survey's central retention/revenue objective: neither objective (relevance, purchase-ratio, or inverse title length) has any delay, horizon, or censoring; there is no causal/incrementality framing (Q2 unaddressed), no online evaluation at all (Q6 half-unaddressed), and no two-sided/reciprocal-market treatment (Q7 unaddressed). Its contribution here is a fusion-mechanism data point and a partial-labeling framing, not a template for the target retention/revenue model.

## Papers That Mention This Paper (Reverse Citation Map)

_This paper proposes no distinctively-named method, so no automated reverse-citation match was possible._

## Meta Information

- **Authors:** David Carmel, Elad Haramaty, Arnon Lazerson, Liane Lewin-Eytan
- **Affiliations:** Amazon, Haifa, Israel
- **Venue:** WWW 2020 (The Web Conference)
- **Year:** 2020
- **Relevance:** Core
- **Priority:** 1
- **NotebookLM source:** `nlm:f3865b86-af82-4689-bede-d274881b5f83`
