# Paper Analysis: 相互推薦における嗜好の集約をパーソナライズする試み

**Source:** https://www.wantedly.com/companies/wantedly/post_articles/1036056  
**Date analyzed:** 2026-08-19

---

## 1. Summary

**Title:** 相互推薦における嗜好の集約をパーソナライズする試み (*An Attempt to Personalize Preference Aggregation in Reciprocal Recommendation*)  
**Authors:** 市村千晃 (Chiaki Ichimura); Wantedly  
**Abstract:** Wantedly reproduces and adapts Kleinerman et al.'s personalized reciprocal-score aggregation. A user-specific harmonic-mean weight balances outbound application interest against the recipient's match interest; offline logs show broader recommendation diversity but lower logged-relevance metrics.

**Key contributions:**

- Implements per-user reciprocal preference aggregation with an explicit weighted harmonic mean.
- Optimizes each user's weight from historical successful interactions using bounded Brent search.
- Reports a useful negative result: diversity improves while logged nDCG declines under exposure-biased offline evaluation.

**Methodology:** Apply and match predictions are combined as `1 / (beta/apply_score + (1-beta)/match_score)`. For each user with prior successful interactions, bounded Brent optimization searches beta from 0.01 to 0.99 and minimizes the summed ranks of historical successes. The comparison uses a uniform fixed-weight aggregation rule.

**Main results:** Relative to fixed weights, apply nDCG@10 decreases 2.4%, matching-success nDCG@10 decreases 3.3%, and unique recommendations@10 increases 16.8%.

## 2. Experiment Critique

**Design:** A direct offline comparison on Wantedly Visit logs isolates the aggregation-rule change. Evaluation excludes users without prior successes and relies on outcomes exposed by the baseline policy.

**Statistical validity:** Exact sample size, time range, uncertainty, significance tests, and repeated runs are not specified in source.

**Online experiments:** Not performed for this implementation. The post contrasts its negative offline match metric with positive online results reported by Kleinerman et al.

**Reproducibility:** The aggregation equation, objective, beta bounds, and SciPy routine are described. Data, preprocessing, base scorers, and full code are not public.

**Overall:** The diversity effect is concrete, but exposure bias prevents the negative logged nDCG from establishing the true online match effect.

## 3. Industry Contribution

**Deployability:** Fits on top of existing bilateral scores and is substantially lighter than global market-clearing optimization.

**Problems solved:** One-size-fits-all preference aggregation and traffic concentration on popular recipients.

**Engineering cost:** Medium: maintain two directional scores, periodically fit per-user beta, and define fallback weights for cold-start users.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** A Wantedly-specific reproduction and product-log evaluation of personalized aggregation rather than a new mathematical method.

**Prior work comparison:** Kleinerman et al. (2018), *Optimally Balancing Receiver and Recommended Users' Importance in Reciprocal Recommender Systems*, supplies the optimization; Palomares et al. (2021) survey reciprocal aggregation; a prior Wantedly post describes bilateral user-company recommendation. Four additional prior works are not specified in source.

**Verification:** Limited to works explicitly named or linked by the source.

## 5. Dataset Availability

**Datasets mentioned:**

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Wantedly Visit historical interactions | Not public | No | Only users with at least one successful interaction are evaluated; size and time range absent. |

**Offline experiment reproducibility:** The optimization can be reproduced, but the reported results cannot without proprietary logs and bilateral base scores.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Exact mechanism:** Personalize the trade-off between a viewer's likelihood of liking and the recipient's likelihood of reciprocating. Heterogeneous weights disperse top-ranked recipients instead of sending every user through the same aggregate-score bottleneck.

**Metrics and reported effect:** Apply nDCG@10 is -2.4%, matching-success nDCG@10 is -3.3%, and unique recommendations@10 is +16.8% versus fixed weights.

**Capacity/interference relevance:** Recipient capacity is explicitly discussed but only indirectly addressed through exposure dispersion; it is not a hard constraint. Concentration externalities are acknowledged, but experimental interference is not modeled.

**Practical mapping:** The approach can sit between reciprocal scoring and reranking to increase coverage and reduce likes wasted on overloaded users. The source does not report total online matches, conversations, Gini, wasted-like counts, or two-sided retention, and it cannot personalize cold-start users.

**Dating fit: High.** The replicated method was built for online dating's positive-reply objective and attacks the same popular-recipient concentration problem.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| No verified inbound mentions within the 45-source corpus. | — | — |

## Meta Information

**Authors:** 市村千晃 (Chiaki Ichimura)  
**Affiliations:** Wantedly  
**Venue:** Wantedly Engineer Blog  
**Year:** 2026  
**PDF:** web source; no PDF required  
**Relevance:** Core  
**Priority:** 1

## Annotated Bibliography Fields

- **Title:** 相互推薦における嗜好の集約をパーソナライズする試み (*An Attempt to Personalize Preference Aggregation in Reciprocal Recommendation*)
- **Authors/organization:** Chiaki Ichimura; Wantedly
- **Year:** 2026
- **Venue/type:** Wantedly Engineer Blog; industry technical article
- **Link:** https://www.wantedly.com/companies/wantedly/post_articles/1036056
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Combined outbound apply and recipient match predictions with a user-specific weighted harmonic mean. For users with prior successes, bounded Brent search selects the weight that raises historical successful interactions. An offline comparison against fixed weights measures logged ranking quality and recommendation diversity.
- **Mechanism relevant to two-sided balancing (≤50 words):** Personalize the sender-versus-recipient score trade-off so users do not all rank the same popular recipients, dispersing exposure toward candidates with a better chance of reciprocating.
- **Metrics and reported effect:** Apply nDCG@10 -2.4%, matching-success nDCG@10 -3.3%, unique recommendations@10 +16.8% versus fixed weights.
- **Dating-app fit:** High — reciprocal reply scoring and popular-recipient dispersion transfer directly, though cold start remains.
- **Confidence:** High on source identity, formula, and offline results; medium on online effect because exposure bias is unresolved.
