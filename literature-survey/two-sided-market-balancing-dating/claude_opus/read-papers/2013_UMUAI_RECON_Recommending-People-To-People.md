# Recommending people to people: The nature of reciprocal recommenders with a case study in online dating

- **notebook source_id:** `fc3355e4`
- **extraction method:** direct PDF read (NotebookLM unavailable)

## Summary
People-to-people ("reciprocal") recommenders differ fundamentally from item recommenders because success requires mutual interest from both the subject and the object of a recommendation. The paper systematically characterizes these differences (user-model creation, user roles, success criteria) and presents RECON, a content-based reciprocal recommender for online dating, evaluated on a large real commercial dating dataset (1.4M+ messages, 90,000+ users). Headline result: incorporating reciprocity into the score roughly doubles success rate over a non-reciprocal recommender at top-10 (42.20% vs 23.00%, an 83.48% relative improvement), and both beat the unaided-search baseline (17.3%). The paper also shows reciprocal scoring spreads recommendations more evenly across popularity levels than collaborative filtering, and that modeling negative preferences further improves top-ranked success rate.

## Method
RECON's reciprocal compatibility score `s_y` for subject `x` and object `y` is the **harmonic mean** of the two one-way `Compatibility()` scores: `s_y = 2 / (Compatibility(P_x,y)^-1 + Compatibility(P_y,x)^-1)`. Harmonic mean was chosen because it stays close to the *lower* of the two one-way scores — it penalizes cases where only one side is interested, rather than averaging them away (arithmetic mean would let a very-high one-sided score compensate for the other side's disinterest). `Compatibility(P_x,y)` (Algorithm 2) is the arithmetic mean, across the subject's explicit stated-preference attributes, of the fraction of the population sharing each attribute value that object `y` has. A later extension (Pizzato et al. 2011, incorporated in §5.7) adds negative preferences: `C±(A,B) = (1 + C+(A,B) − C−(A,B)) / 2`, combining a positive compatibility (similarity to liked profiles) and negative compatibility (similarity to disliked profiles). A weighted variant (Eq. 7) introduces tunable priority weights `ω_s`, `ω_o` per side or user class, so a platform can bias the score toward one side's preferences (e.g., paying subscribers, or the employer side in a job-recommendation reuse of the same architecture).

## Datasets and Baselines
Large real-world commercial online dating website: six-week window, first four weeks as training data, last two weeks as test; 1.4 million messages sent by over 90,000 users (only subjects/objects active — i.e. sent/received a message — during training are evaluated). Repeated on other six-week periods with "near identical" results (not itemized). A second, smaller dataset (Akehurst et al. 2012: 8,000 users, 116,000 interactions) is used for the explicit-vs-implicit preference predictive-power analysis. Baselines/comparators:
- **Baseline** = the site's natural (unaided) EOI success rate: 17.3% for established users, 16.1% for new users.
- **Non-reciprocal recommender** = RECON using only the subject→object compatibility (object's own preferences ignored).
- **Standard user-based collaborative filtering** (non-reciprocal) — used only for the popularity-spread comparison (Fig. 6).
- **Reciprocal positive-only** vs **reciprocal combined (positive+negative)** recommender (§5.7).

## Results
- Top-10 success rate: RECON (reciprocal) 42.20% vs non-reciprocal 23.00% vs baseline 17.3% — **83.48% relative improvement** from reciprocity.
- Top-100 recall: improved from 5.90% (non-reciprocal) to 10.80% (reciprocal) — **83.05% relative improvement**.
- Cold start (new users): baseline success 16.10%; RECON top-10/top-20 reach roughly 1-in-4 (~25%) success, clearly above baseline, using pre-filtering by peer-group preferences.
- Table 6: as interactions become more costly/serious, subjects increasingly match the object's stated preferences — object matches subject 78% of EOIs / 75% of paid communications, vs only 70% of profile views; subject matches object's preferences 57% (EOIs) / 67% (paid) vs 54% (views).
- Profile completeness: users with profiles >65% complete average 30 EOIs vs 15 EOIs for those at 40% complete (p < 0.01).
- Explicit-preference mismatch: largest for *education* and *religion* (30% of EOIs sent to non-matching objects), smallest for *age*, *smoke*, *height* (10%).
- Implicit vs explicit preference power (Akehurst 2012 subset): in **62%** of successful interactions the subject's explicit preferences did **not** match the object's profile; in **42%** of unsuccessful interactions they **did** match. A probabilistic implicit-preference model achieved **89% accuracy** predicting success — explicit stated preferences are a materially worse signal than inferred (implicit) preferences.
- Proactivity/gender: population-wide balance of proactive vs reactive roles, but strongly gendered — the "Highly Reactive" class is 81.7% female, the "Highly Proactive" class is 76.3% male.
- Success-by-role cross table (Table 8): highest success rate 43.7% (Highly Reactive subject → Highly Proactive object); lowest 9.0% (Highly Proactive subject → Highly Reactive object).
- Popularity/overload effect (Fig. 5): a female user's success rate falls from 28% (at 4 EOIs received) to 11.31% (at 50+ EOIs received) — direct evidence of attention/reply-capacity saturation among popular users.
- Table 12: overall average success rate 14.4%; very-popular (VP) subjects reach 30.9% success vs 12.5–20.0% for less-popular subject classes; very-active+unpopular (VA+UP) subjects have the lowest success (9.0–11.2% range per column); best single cell is 41.8% (VP subject → very-active-unpopular object).
- Recommendation-spread comparison (Fig. 6): RECON (reciprocal) distributes recommendation frequency far more evenly across user-popularity levels than standard collaborative filtering, which concentrates heavily on already-popular objects (CF line rises steeply toward 400+ EOIs/user at high recommendation counts; RECON plateaus around 150–200).
- Negative-preference-augmented recommender (§5.7): top-1 success 37.46% (combined pos+neg) vs 31.78% (positive-only); top-5: 30.77% vs 28.09%. Improvement statistically significant at top-1–top-5 (Mann-Whitney-Wilcoxon, 95% CI) but **not** significant at higher n; failure rate is also lower for the combined recommender at low n, though it crosses above the 54.19% baseline failure rate by top-100. 72% of EOIs were sent to objects with overall compatibility score > 0.5. Mean positive compatibility 0.45±0.07, negative compatibility 0.40±0.09, overall 0.51±0.08 (all normally distributed).

## Limitations
- Only EOI-exchange outcomes are studied (Events 1–6 of the paper's own scenario); the eventual relationship outcome ("happily ever after," Event 8) is not observable in the data and explicitly excluded from the success definition.
- Acute cold-start problem specific to reciprocal domains: about a quarter of users leave the site within four weeks of signing up, so implicit-preference histories stay thin — "less common for users to have rich implicit preferences" than in traditional recommenders (their own Table 2, Row f).
- Single domain (online dating) and a single (anonymized, unnamed) commercial platform's historical data, despite its large size (1.6M interactions); applicability to other reciprocal domains (job recommendation, mentoring, flatmate search) is discussed but not empirically tested.
- Serendipity and transparency are flagged as open, unresolved problems specific to reciprocal recommenders — explaining a recommendation can require revealing the *other* party's preferences, which raises privacy concerns not present in item recommenders.
- The negative-preference improvement is not statistically significant beyond top-5.
- The weighted priority-scoring scheme (Eq. 7) is proposed conceptually but not empirically evaluated in this paper.

## Heavily Cited Prior Works
- Gale & Shapley (1962) — "College admissions and the stability of marriage," the foundational stable-matching algorithm.
- Pizzato et al. (2010b) — RECON's original RecSys conference paper; this UMUAI article consolidates and extends it.
- Diaz, Metzler & Amer-Yahia (2010) — matchmaking cast as an information-retrieval problem with two-sided relevance, online dating.
- McFee & Lanckriet (2010) — metric learning to rank, evaluated on online dating data.
- Akehurst et al. (2011, 2012) — CCR (content-collaborative reciprocal recommender); explicit vs. implicit preference analysis reused directly in this paper's §5.3.
- Cai et al. (2010, 2011) — SocialCollab, collaborative filtering for people-to-people recommendation in social networks.
- Brožovský & Petříček (2007) — one of the first online-dating recommender studies (item-to-item and user-to-user collaborative filtering).

## Bibliography Fields
- **title:** Recommending people to people: The nature of reciprocal recommenders with a case study in online dating
- **authors or organization:** Luiz Pizzato, Tomek Rej, Joshua Akehurst, Irena Koprinska, Kalina Yacef, Judy Kay (Computer Human Adapted Interaction (CHAI) lab, University of Sydney; funded by the Smart Services Cooperative Research Centre)
- **year:** 2013
- **venue or type:** User Modeling and User-Adapted Interaction (UMUAI), journal article
- **link:** https://www.dropbox.com/s/cb93kjvlolh1n7q/2012_UMUAI_Pizzato_etal_UMUAI.pdf?dl=1
- **tier tag:** Tier 2 applied-on-real-platform-data
- **what they did (≤80 words):** Defined and systematically characterized "reciprocal recommenders" (people-to-people recommenders requiring mutual interest), contrasting them with item recommenders on user modeling, user roles, and success metrics. Built and evaluated RECON, a content-based reciprocal recommender using a harmonic-mean bilateral compatibility score, on 1.6M interactions from a large commercial online dating site, then extended it with negative-preference modeling and analyzed its effect on recommendation spread across user popularity.
- **mechanism relevant to two-sided balancing (≤50 words):** Harmonic-mean reciprocal score (penalizes one-sided interest) is a direct Layer-1 (reciprocal scoring) building block. A tunable per-side priority-weight formula (Eq. 7) anticipates market-design levers. Empirically, reciprocal scoring alone spreads recommendations more evenly across popularity levels than CF — an early, informal precursor to capacity-aware exposure allocation (Layer 2).
- **metrics used, and the reported effect:** Success rate at n (S@n), recall at n (R@n), failure rate at n (F@n). RECON top-10 S@10 = 42.20% vs non-reciprocal 23.00% vs baseline 17.3% (+83.48% relative). Recall@100 5.90%→10.80% (+83.05%). Negative-preference recommender: top-1 S@1 = 37.46% vs positive-only 31.78% (significant at top-1–top-5, Mann-Whitney-Wilcoxon, 95% CI; not significant at higher n).
- **fit for a dating app:** high — a real dating-platform mechanism (reciprocal harmonic-mean scoring, popularity-aware spread, tunable side-priority weighting) validated on a large real dating dataset; it is the closest thing in this batch to a ready-made Layer-1 building block, plus empirical evidence that reciprocal scoring alone reduces (but does not solve) popular-user overload.
- **confidence that the item is real and described correctly:** high — read directly from the full 40-page PDF, including equations, tables, and numeric results; title/authors/venue match the manifest.

## Project Relevance
Directly addresses **Layer 1 (reciprocal scoring)**: the harmonic-mean formula and its rationale (penalize one-sided interest rather than average it away) is exactly the kind of like-back-probability mechanism the project's Layer 1 calls for, and the paper's own §5.7 negative-preference extension is a natural precursor to conditioning on dislike signals too.

Touches **Layer 2 (capacity-aware exposure allocation)** only informally: Fig. 6 shows RECON's reciprocal design naturally spreads recommendations more evenly across popularity levels than plain collaborative filtering — a real, measured de-concentration effect — but there is no explicit notion of a *capacity limit* or *remaining reply budget*; the system reacts to historical popularity/response-rate patterns, not to a hard constraint. Tables 8/11/12 and Fig. 5 are effectively an informal ecosystem-health analysis (success rate collapsing as popularity rises, i.e. reply-capacity saturation) but stop short of a formal fairness or Gini-style metric — a partial, retrospective echo of **Layer 4**.

Does not address **Layer 3 (market-design levers)** at all — no like limits, curated batches, or signaling are discussed. No live A/B test or interference-aware experimentation is reported; all results are computed on static historical data.

Bottom line: strong source for grounding the reciprocal-scoring mechanism and citing an early empirical link between "reciprocal design" and "reduced popularity concentration," but it stops well short of capacity-constrained allocation or market-design levers.

## Reverse Citation Map
