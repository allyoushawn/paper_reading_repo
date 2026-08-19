# Paper Analysis: Towards a Fair Marketplace: Counterfactual Evaluation of the Trade-off between Relevance, Fairness & Satisfaction in Recommendation Systems

**Source:** NotebookLM source `069d754f-0604-4a8c-abc4-0407ceba2423` (CIKM 2018)
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** Towards a Fair Marketplace: Counterfactual Evaluation of the Trade-off between Relevance, Fairness & Satisfaction in Recommendation Systems
**Authors:** Rishabh Mehrotra, James McInerney, Hugues Bouchard, Mounia Lalmas (Spotify Research); Fernando Diaz (Microsoft Research, work done at Spotify)
**Abstract:**
In two-sided marketplaces, optimizing purely for consumer relevance creates "superstar economics" — a small group of popular suppliers absorb most exposure while the long tail struggles for visibility. The paper formalizes supplier group fairness, proposes several joint relevance/fairness recommendation policies, and — since online A/B testing every trade-off is expensive/risky — introduces a counterfactual (off-policy, IPS-based) evaluation framework to measure each policy's effect on consumer satisfaction using offline logged data.

**Key contributions:**
- A quantitative group-level supplier fairness metric based on artist popularity bins (`ψ(s) = Σ√|bin overlap|`).
- A combinatorial contextual-bandit formulation of the recommendation problem with an Inverse Propensity Score (IPS) off-policy evaluator for unbiased offline satisfaction estimates.
- A family of relevance/fairness trade-off policies: Relevance-only, Fairness-only, Interpolated, Probabilistic, Guaranteed-Relevance.
- A personalized "Adaptive" policy that learns each user's tolerance (affinity) for fair/non-popular content and routes fairness exposure accordingly.

**Methodology:**
Relevance is cosine similarity between skip-gram user/track embeddings; fairness rewards playlists spanning multiple popularity bins (diminishing-returns square-root form); satisfaction is implicit (tracks listened). Policies combine relevance and fairness scores in different ways (linear interpolation, probabilistic mixing, hard relevance floor, or per-user affinity weighting). All policies are evaluated offline via IPS re-weighting of two weeks of randomized-exploration logs (400K+ users, 5,000+ playlists, 49K+ artists), validated with arithmetic-mean/harmonic-mean propensity sanity checks.

**Main results:**
Only-Relevance satisfaction = 0.650; Only-Fairness = 0.420 (−35%). Adaptive personalized policies beat every global trade-off and even exceed the pure-relevance baseline: Adaptive-I = 0.709 (+9.0%), Adaptive-II = 0.729 (+12.1%), while keeping fairness losses low (15–17%).

---

## 2. Experiment Critique

**Design:**
Clean two-baseline design (Relevance-only, Fairness-only) plus a sweep of the interpolation parameter β from 0 to 1 for three global policy families, and a separate head-to-head for the personalized Adaptive policies. Uses genuinely randomized (uniform) exploration logs, which is the correct precondition for unbiased IPS estimation.

**Statistical validity:**
The counterfactual estimator (IPS) is provably unbiased under non-zero propensities, and the authors explicitly verify this precondition with two independent checks (arithmetic-mean test, harmonic-mean test per Li et al.). No confidence intervals are reported alongside the satisfaction/fairness/relevance percentages in Tables 1–3, which is a gap given the effect sizes being compared are sometimes single-digit percentages.

**Online experiments (if any):**
None — the whole point of the paper is to replace costly online A/B testing with offline counterfactual evaluation using logged randomized data. The authors explicitly flag validating with live A/B tests as future work.

**Reproducibility:**
Formulas for relevance, fairness, and all six policies are fully specified; the underlying Spotify interaction data and randomized exploration logs are proprietary and not released.

**Overall:**
Results support the central claims — relevance and fairness are largely in tension (few sets score high on both), fairness-only recommendations meaningfully hurt satisfaction, and personalizing the trade-off by user affinity beats any single global weighting. The authors are candid that their fairness definition is one of many possible choices and that the framework needs live validation.

---

## 3. Industry Contribution

**Deployability:**
High for the counterfactual evaluation methodology (directly reusable at any platform with randomized exploration logging); the specific policies (Interpolation, Probabilistic, Guaranteed-Relevance, Adaptive) are simple enough to implement as a re-ranking layer on top of an existing relevance-only ranker.

**Problems solved:**
Directly targets supplier-side exposure inequality ("superstar economics") in two-sided marketplaces, and the operational problem of evaluating fairness/relevance trade-offs without running many expensive, user-experience-risking A/B tests.

**Engineering cost:**
Moderate: requires infrastructure for collecting randomized (uniform-propensity) exploration data, an embedding-based relevance model, a supplier-popularity-bin fairness score, and a per-user affinity estimator for the Adaptive variant.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First to explicitly formalize and empirically quantify the relevance/supplier-fairness/consumer-satisfaction three-way trade-off in a live two-sided marketplace, evaluated via counterfactual estimation rather than costly A/B testing, and to personalize the trade-off by user-level fairness affinity.

**Prior work comparison:** Builds on "superstar economics" (Rosen 1981), fairness-of-exposure-in-rankings (Singh & Joachims 2018), multi-sided fairness (Burke 2017), two-sided market economics (Armstrong 2006), and counterfactual/IPS estimation (Horvitz & Thompson 1952; Li et al. 2015).

**Verification:** Claims are consistent with the broader fairness-in-ranking literature the paper cites; the personalized-affinity angle appears to be the paper's most distinctive addition relative to prior group-fairness re-ranking work.

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Spotify randomized exploration logs (Nov 2017, 2 weeks) | proprietary | No | 400K+ users, 5,000+ playlists, 49K+ artists |

**Offline experiment reproducibility:** Not reproducible outside Spotify — no public dataset or code release mentioned.

---

## 6. Community Reaction

Not checked — out of scope for this NotebookLM-sourced batch pass (no web search performed).

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Rishabh Mehrotra, James McInerney, Hugues Bouchard, Mounia Lalmas, Fernando Diaz
**Affiliations:** Spotify Research; Microsoft Research
**Venue:** CIKM 2018
**Year:** 2018
**PDF:** Not fetched directly — analyzed via NotebookLM source extraction
**Relevance:** Core
**Priority:** 1

---

## Bibliography Fields

- **title:** Towards a Fair Marketplace: Counterfactual Evaluation of the Trade-off between Relevance, Fairness & Satisfaction in Recommendation Systems
- **authors or organization:** Rishabh Mehrotra, James McInerney, Hugues Bouchard, Mounia Lalmas (Spotify Research); Fernando Diaz (Microsoft Research)
- **year:** 2018
- **venue or type:** CIKM 2018 (industry paper)
- **link:** N/A (accessed via NotebookLM notebook source; not separately fetched)
- **tier tag:** Tier 1 — Adjacent marketplaces (job / ride / home / creator)

**What they did (80 words max):** Formalized supplier-side group fairness in a two-sided marketplace (Spotify), proposed six recommendation policies trading off consumer relevance against supplier exposure fairness (including a personalized, per-user-affinity variant), and built an Inverse-Propensity-Score counterfactual evaluation framework to measure each policy's effect on user satisfaction offline, avoiding costly live A/B tests. Validated on ~400K users and 49K artists from randomized exploration logs.

**Mechanism relevant to two-sided balancing (50 words max):** Directly relevant: multi-objective re-ranking that interpolates relevance against a supplier-fairness score, plus a personalized policy routing exposure-diversity content to users tolerant of it. Transfers as a template for weighting a receiver-capacity term against viewer relevance, and its IPS off-policy evaluation methodology transfers wholesale for offline interference-safe evaluation.

**Metrics used, and the reported effect:** User satisfaction (tracks listened, IPS-estimated): Relevance-only 0.650, Fairness-only 0.420 (−35%), Adaptive-I 0.709 (+9.0%), Adaptive-II 0.729 (+12.1%) vs. relevance-only baseline, with fairness losses of only 15–17% for the adaptive policies. Guaranteed-Relevance at β=0.9 gave +22.1% satisfaction but a 63.9% fairness loss.

**Fit for a dating app:** high — the relevance/fairness interpolation framework and its IPS-based offline evaluation are close analogues of what a dating platform needs to trade off viewer relevance against supply-side exposure spread, though the paper's supply side (artists) has effectively infinite capacity, unlike human reply capacity in dating.

**Confidence that the item is real and described correctly:** high — all three NotebookLM queries were grounded (`sources_used` matched the scoped source_id), and the reported figures (Tables 1–3, exact formulas, dataset scale) are specific, internally consistent, and match the known CIKM 2018 Mehrotra et al. paper.

---

## Project Relevance

Directly relevant, but with a critical structural mismatch the paper itself does not address: Spotify's suppliers (artists) have **infinite serving capacity** — any number of listeners can stream a song simultaneously — whereas a dating profile has **finite reply capacity**. This means the paper's fairness objective (diversify exposure across popularity bins) captures spread of exposure but not the deeper dating-specific cost: showing a viewer an over-congested "superstar" profile doesn't just under-expose the long tail, it also **wastes the viewer's own limited attention/likes budget** on someone who structurally cannot reply. The paper's fairness metric has no way to represent this because streaming has no analogous concept of a supplier's reply queue.

What transfers well: (1) the general multi-objective re-ranking template (`(1-β)·relevance + β·fairness`, or a hard relevance floor with fairness maximized subject to it) is a direct architectural fit for combining a base compatibility score with a receiver-capacity discount; (2) the personalized Adaptive-affinity policy — learning which users tolerate lower-relevance-but-fairer content — maps to identifying "flexible" swipers who can be routed toward under-exposed, less-popular profiles without hurting their satisfaction; (3) the IPS-based counterfactual evaluation framework is close to fully transferable and is exactly the kind of interference-safe offline evaluation methodology the project's ecosystem-metrics layer needs, since live A/B testing of exposure-redistribution policies in a dating market carries the same experimentation-under-interference risk the paper is designed to avoid.

What does not transfer: the satisfaction metric (listen count) and the fairness metric (artist popularity-bin diversity within a single session) are both single-sided constructs with no reciprocal-interest or capacity-depletion semantics; a dating adaptation would need a genuinely new fairness/spread metric (e.g., Gini of received likes, share of users with ≥1 match) and a genuinely new receiver-side "satisfaction" cost for over-congested users (chat/inbox burnout), neither of which the paper's formulas represent.
