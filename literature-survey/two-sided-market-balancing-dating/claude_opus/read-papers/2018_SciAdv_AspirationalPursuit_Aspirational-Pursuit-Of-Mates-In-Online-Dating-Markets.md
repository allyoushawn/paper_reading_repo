# Aspirational pursuit of mates in online dating markets

- **notebook source_id:** `6fd7c401`
- **extraction method:** direct PDF read (NotebookLM unavailable)

## Summary
Bruch and Newman quantify the "desirability hierarchy" of a real online dating market using a PageRank-style score computed on the network of first messages between users in four large US cities. Both men and women overwhelmingly send first messages "up" the hierarchy — to partners roughly 25% more desirable than themselves on average — while the probability of receiving a reply falls sharply as the sender-receiver desirability gap grows. The paper is purely descriptive/measurement (no algorithm or intervention proposed): it establishes an empirical, population-scale picture of aspirational messaging, reply-rate collapse for popular users, and demographic correlates of desirability (age, ethnicity, education). The headline result is that people pursue a hybrid "matching + competition" strategy — aware of their own rank, but still reaching upward — and that the most popular individual in the sample (a 30-year-old woman in New York) received 1,504 messages in one month, about one every 30 minutes around the clock.

## Method
Desirability is measured via PageRank on the directed network of first (initial-contact) messages within each city: x_i = 1 + α·Σ_j a_ij x_j / (Σ_k a_kj), α = 0.85 (standard PageRank damping), solved by iterative substitution. Scores are computed separately for men and women and scaled to a 0–1 rank. "Desirability gap" is defined as the difference in scaled rank between a message's receiver and sender. The paper then runs: (1) fractional regression models of desirability as a function of demographics (age, ethnicity, education), with city interaction terms and clustered standard errors; (2) negative binomial regression of message length (word count) on desirability gap and its square; (3) fractional regression of message positivity (% positive words, LIWC2001) on desirability gap; (4) logistic regression of reply probability on message length/positivity conditional on desirability gap. All models are fit separately by sex and city, with city × covariate interaction terms.

## Datasets and Baselines
One month (Jan 1–31, 2014) of demographic and messaging data from a large, non-niche, free US online dating site, restricted to four metro areas (New York City's five boroughs, Boston, Chicago, Seattle CBSAs) and to active, heterosexual users (excludes ~14% of the user base who identify as gay/bisexual). Per-city active user counts: NYC 44,009 men / 50,618 women; Boston 9,113/9,355; Chicago 28,635/23,236; Seattle 12,721/9,248 (Table I). No baseline algorithms are compared; the paper contrasts its PageRank-based findings against prior desirability/matching studies, most directly Taylor et al. 2011 ("Out of my league"), which used raw message-count popularity instead of PageRank and concluded (weakly) in favor of matching — a conclusion this paper directly disputes methodologically.

## Results
- Both sexes message "up": men and women send initial messages to partners **26% and 23%** further up the desirability ranking than themselves, respectively (abstract rounds this to "about 25%").
- Reply probability declines monotonically with desirability gap for both sexes; men are **more than twice as likely** to receive a reply from a less-desirable woman than from a more-desirable one, and for messages sent to more-desirable women the reply rate **never rises above 21%**.
- Table I reply rates by city/sex: NYC — men 15%, women 34%; Boston — men 17%, women 37%; Chicago — men 18%, women 40%; Seattle — men 20%, women 45%.
- Mean messages sent per active user (Table I): NYC men 23.3 / women 9.4; Boston 14.6/6.3; Chicago 19.0/10.2; Seattle 12.4/7.8. Men send 81% of all initial contacts overall.
- Most popular individual: a 30-year-old woman in New York received 1,504 messages in one month (~1 message every 30 minutes, day and night, for the whole month).
- Desirability regression (Table II, selected coefficients, Boston baseline): age is negative and significant for women (coef. −0.055, z = −3.84) and positive for men (coef. 0.036, z = 2.48); White is positive and significant for men (coef. 0.492, z = 4.33) but not significant for women; Black is negative and significant for women (coef. −0.729, z = −5.77); postgraduate education is negative for women (coef. −0.132, z = −2.90) and positive for men (coef. 0.174, z = 3.29).
- Message length increases with desirability gap for both sexes, "up to twice as long in some cases"; message positivity increases with gap for women but decreases for men (effect "modest but consistent across all four cities and statistically significant, p < 0.001," Table IV).
- Payoff analysis (Fig. 4 bottom panels): longer messages associate with higher reply rates for women (all cities) and for men only in Seattle; more-positive messages associate with slightly *lower* reply rates for men in all four cities.

## Limitations
- The analysis is explicitly descriptive, not causal/mechanistic: the authors state it "cannot reveal the underlying process" (e.g., whether behavior reflects reinforcement learning) that produces the observed messaging/reply patterns.
- PageRank desirability is a proxy built from revealed messaging behavior ("a posteriori... identifying those people who receive the largest number of messages from other desirable people"), not a direct measure of attractiveness or platform-intended ranking.
- Restricted to heterosexual users only; no analysis of same-sex dating markets.
- Restricted to four US metro CBSAs; excludes messaging to/from outlying regions, and results may not generalize beyond this single dating site's population.
- Authors caution that online dating differs from offline dating (higher volume, lower cost per message) and may exaggerate hierarchy/competition effects relative to offline mate markets — "hierarchies of desirability may be more pronounced online than off."

## Heavily Cited Prior Works
- Walster, Aronson, Abrahams, Rottman 1966 — "Importance of physical attractiveness in dating behavior" (classic matching-hypothesis origin)
- Taylor, Fiore, Mendelsohn, Cheshire 2011 — "Out of my league: A real-world test of the matching hypothesis" (most directly critiqued prior study)
- Hitsch, Hortaçsu, Ariely 2010 — "Matching and sorting in online dating," American Economic Review
- Gale & Shapley 1962 — "College admissions and the stability of marriage" (foundational matching-market theory)
- Fiore, Taylor, Zhong, Mendelsohn, Cheshire 2010 — "Who's right and who writes? People, profiles, contacts and replies in online dating" (HICSS)
- Rudder 2015 — *Love, Sex, Race, and Identity: What Our Online Lives Tell Us About Our Offline Selves* (OkCupid data book)
- Brin & Page 1998 — "The anatomy of a large-scale hypertextual web search engine" (PageRank, the mechanism this paper repurposes)

## Bibliography Fields
- **title:** Aspirational pursuit of mates in online dating markets
- **authors or organization:** Elizabeth E. Bruch, M. E. J. Newman (University of Michigan, Ann Arbor)
- **year:** 2018
- **venue or type:** Science Advances (arXiv:1808.04840)
- **link:** https://arxiv.org/pdf/1808.04840
- **tier tag:** Tier 2 applied-on-real-platform-data
- **what they did (≤80 words):** Built a PageRank-based desirability score on real US dating-site messaging networks across four cities, then measured how strongly and consistently men and women pursue more-desirable partners ("aspirational pursuit"), how reply probability falls off with sender-receiver desirability gap, and how message length/content vary with the target's desirability, controlling for age, ethnicity, and education.
- **mechanism relevant to two-sided balancing (≤50 words):** No allocation mechanism — this is measurement, not intervention. Its value is the quantified empirical shape of the exact failure mode the project targets: heavy-tailed desirability, aspirational over-messaging of top users, and reply-rate collapse as a function of desirability gap.
- **metrics used, and the reported effect:** PageRank desirability score, "desirability gap" (percentile-rank difference), reply probability as function of gap, message-count/length/positivity distributions. Effect: +26%/+23% average messaging-up-hierarchy by men/women; reply rate for messages sent up-hierarchy caps under 21%; top individual received 1,504 messages/month.
- **fit for a dating app:** high — direct empirical characterization, from a real dating platform, of the desirability-skew and reply-capacity-collapse dynamics that motivate the whole project; strong grounding evidence even though it offers no algorithmic lever itself.
- **confidence that the item is real and described correctly:** high — all figures and coefficients were read directly from the paper's text, Figures 1–4, and Tables I–VI.

## Project Relevance
Primarily motivating/diagnostic evidence rather than a transferable mechanism. It is the clearest available empirical confirmation of the project's north-star problem statement: a small set of highly desirable users absorbs a disproportionate share of messages/likes (most popular user got 1,504 messages in a month), most senders reach "up" toward already-oversubscribed users (+23–26% desirability gap on average), and reply probability — the reciprocal signal a dating platform's **layer 1 (reciprocal scoring)** model needs to predict — collapses as the gap widens (never exceeding 21% reply rate for upward messages). This is exactly the "reply capacity gets spent disproportionately on top users, so their surplus likes go unanswered" dynamic the project frames as its core failure mode, and it is measured on a real platform rather than assumed theoretically. It does **not** provide a capacity-aware allocation mechanism (layer 2), a market-design lever (layer 3), or an ecosystem/interference-aware metric (layer 4) — it is descriptive statistics on an unmodified marketplace, with no counterfactual or intervention analysis. Best used as a citable empirical baseline/motivation, and as a feature-design reference (desirability gap is a natural predictor for a reciprocal like-back model) rather than as an algorithmic component.

## Reverse Citation Map

