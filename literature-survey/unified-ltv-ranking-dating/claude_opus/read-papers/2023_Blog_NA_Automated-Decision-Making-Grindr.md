# Paper Analysis: Automated Decision Making at Grindr

**Source:** Grindr Company Blog, published April 14, 2023 (page shows an update timestamp of August 16, 2026). https://www.grindr.com/blog/automated-decision-making-and-grindr
**Date analyzed:** 2026-08-16

## 1. Summary

Shane Wiley (Grindr's Chief Privacy Officer), with quoted input from Tom Quisel (Chief Technology Officer), addresses growing user and regulatory confusion about what qualifies as Automated Decision Making (ADM) or Artificial Intelligence, in the context of proposed U.S. state privacy laws, the EU Commission's proposed AI Act (described as a 120+ page document targeting high-risk AI systems), and GDPR Article 22 (the right not to be subject to a decision "based solely on automated processing... which produces legal effects"). The post's central and load-bearing claim is a transparency statement: **Grindr does not use any recommendation or matchmaking algorithm.** In the authors' own words: "When a user searches for others nearby, Grindr displays those who were online recently and applies the searching user's filters (such as age, tribe, relationship status, etc...), sorted by distance. Sometimes a little randomness is thrown in to keep results fresh. That's it. There's no recommendation algorithm to speak of on Grindr today. Grindr gets out of the way, and lets our users drive their own experience." The only automated/AI systems Grindr acknowledges are security and trust-and-safety classifiers — detecting and removing spam accounts, and flagging non-compliant profile images — with a human-in-the-loop override: users who are mistakenly flagged (false positives) are routed to the Customer Experience team for manual correction. The post states this ADM use does not rise to producing a "legal effect" under GDPR Article 22, and that Grindr intends to build "smarter" product features in the future (better cascade results, recommended search tags) with a stated commitment to transparency and user controls if and when it does.

## 2. Experiment Critique

Not specified in source. There is no model, ranking system, or evaluation to critique, since the post explicitly states no recommendation algorithm exists. The only operational error modes discussed are for the security/moderation classifiers: **false negatives** (spam accounts or guideline violations that slip through undetected) and **false positives** (compliant users incorrectly flagged and blocked). Neither error rate is quantified. The post frames balancing the two as "difficult and complex" and states the platform "continually fine-tune[s]" the classifiers, but gives no metric, dataset, or evaluation methodology for that fine-tuning. False positives are resolved via human review by the Customer Experience team rather than any automated correction mechanism.

## 3. Industry Contribution

The contribution here is evidentiary rather than technical. Grindr — a major dating platform — explicitly disclaims any recommendation algorithm for its core discovery surface as of publication, relying instead on user-specified manual filters (age, tribe, relationship status, etc.) plus a strict distance sort with light randomization "to keep results fresh." This is directly useful to the survey as an industry baseline: it demonstrates that at least one large-scale dating platform's production "ranking" system is a non-learned heuristic, with all automation confined to trust-and-safety moderation rather than matching or ranking quality. No latency, serving, or feature-engineering discussion applies, since there is no ranking model to deploy.

## 4. Novelty vs. Prior Work

Not specified in source. As a corporate privacy blog post, there is no related-work section or academic citation list. The post's only anchoring references are regulatory and institutional: the EU Commission's proposed AI Act, GDPR Article 22, the UK Information Commissioner's Office (ICO) ADM compliance checklist, and Grindr's own Privacy Policy.

## 5. Dataset Availability

Not applicable — the source describes no model and uses no evaluation dataset.

## 6. Community Reaction

Not assessed in NotebookLM mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Automated Decision Making at Grindr," Shane Wiley (Chief Privacy Officer, Grindr), Blog, 2023, https://www.grindr.com/blog/automated-decision-making-and-grindr |
| 2 | Source type | Blog (Grindr Company Blog / policy statement) |
| 3 | Direction | D8 |
| 4 | Problem setting | Corporate transparency statement on Automated Decision Making and AI use, in response to regulatory scrutiny (US state privacy law proposals, EU AI Act, GDPR Article 22) |
| 5 | Objective and label definition | Not applicable — the source states no ranking model is used. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. (There is no predictive ranking model at all; the only automated systems are binary security/moderation classifiers, which are also not framed in predictive-vs-causal terms.) |
| 7 | Model architecture | None for ranking/recommendation. The only described automated systems are unspecified security classifiers for spam-account and non-compliant-image detection; no architecture is disclosed |
| 8 | Credit assignment | Not applicable — with no ranking or recommendation model, there is no item-level decision to which a user-level outcome could be assigned |
| 9 | Training data and counterfactual handling | Not specified in source. No training data, labels, or counterfactual handling are described for the security classifiers beyond "artificial intelligence" being used to detect spam and non-compliant images |
| 10 | Offline and online evaluation | Not specified in source. Only a qualitative description of balancing false positives and false negatives in the security pipeline, with no metric, benchmark, or evaluation methodology given |
| 11 | Reported gains | Not specified in source — no quantitative results of any kind are reported |
| 12 | Applicability to a two-sided dating recommender | Its value is as an industry baseline, not a method: it documents that a major dating platform's production discovery experience can be — and, as of publication, was — a non-learned distance sort with manual filters, rather than a learned ranking model, bounding how "ranking-sophisticated" the dating-app industry actually is in practice |
| 13 | Unverified claims | The claim that ADM use "largely doesn't impact our users" and does not reach the bar of producing a "legal effect" is a legal/policy self-assessment by the company, not an independently verified determination; no false-positive/false-negative rate is given for the security classifiers, so the "difficult and complex" balance claimed cannot be checked |

## Project Relevance

**Low project relevance.** The source explicitly states Grindr runs no recommendation or ranking algorithm for user discovery — there is no training objective, no label, no credit assignment, and no evaluation methodology to map to **Q1–Q6 or Q8**. Its narrow value is as a real-world industry data point for **Q7** (what two-sided/reciprocal dating platforms actually deploy): it documents that a major dating app's production "ranking" is a non-learned distance sort plus user filters, which is a useful contrast case for the survey's audience — it shows the industry migration path is not uniformly "state-of-the-art ranking to better ranking," but in at least one large deployed system, from no learned ranking at all. It also bears on **Q8** (migration paths) only by omission: a platform with no ML ranking has, by construction, no CTR/CVR-plus-uplift blend to migrate away from, which bounds the applicability of any staged-migration recommendation in the survey to platforms that already run a learned ranker.

## Papers That Mention This Paper (Reverse Citation Map)

_This paper proposes no distinctively-named method, so no automated reverse-citation match was possible._

## Meta Information

- **Authors:** Shane Wiley (Chief Privacy Officer), with quoted commentary from Tom Quisel (Chief Technology Officer)
- **Affiliations:** Grindr
- **Venue:** Grindr Company Blog
- **Year:** 2023
- **Relevance:** Related
- **Priority:** 1
- **nlm:d43aac97-9161-4325-b8c9-fa1f25d38136**
