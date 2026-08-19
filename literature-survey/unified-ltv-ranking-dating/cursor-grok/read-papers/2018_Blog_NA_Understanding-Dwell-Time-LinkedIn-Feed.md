# Paper Analysis: Understanding Dwell Time to Improve LinkedIn Feed Ranking

**Source:** https://www.linkedin.com/blog/engineering/feed/understanding-feed-dwell-time
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Understanding Dwell Time to Improve LinkedIn Feed Ranking
- **authors or company:** Siddharth Dangi, Johnson Jia, Manas Somaiya, Ying Xuan (LinkedIn Feed AI Team)
- **venue:** LinkedIn Engineering Blog
- **year:** 2018
- **URL:** https://www.linkedin.com/blog/engineering/feed/understanding-feed-dwell-time
- **source type:** blog
- **direction:** D1
- **problem setting:** LinkedIn Feed second-pass ranking scores tens of thousands of candidate posts per member visit using click and viral-action predictions; passive consumers and click bounces make binary engagement signals sparse and noisy.
- **objective and label definition:** Adds P(skip) = P(member dwell time on update < T_skip seconds), a negative engagement label derived from empirical dwell-time CDFs on mobile; existing heads predict P(action), E[downstream clicks/virals | action], and E[upstream value | action] for click/react/comment/share.
- **prediction or incrementality:** Predicts probabilities of skip and standard engagement events from logged impressions—not causal incrementality of exposure on retention.
- **model architecture:** P(skip) logistic regression with member, update, member-update affinity, and contextual features plus boosted-tree-learned interaction features; score reduced proportional to predicted P(skip); dwell-based member-update and update popularity (not-skipped count) features also added to the pipeline.
- **credit assignment:** Pointwise per (member, update) impression labels; skip threshold T_skip estimated where P(action | dwell = T) becomes non-zero via Bayes rule on empirical CDFs; no user-level delayed outcome mapped to individual exposures.
- **training data and counterfactual handling:** Production feed impression logs with on-feed and post-click dwell; standard supervised training on observed actions; no off-policy or counterfactual correction described.
- **offline and online evaluation:** Offline AUC for P(skip) improved by as much as 10% over multiple trainings with dwell-based features; online A/B on a small member fraction reported large decrease in skipped updates, more clicks/viral actions, and more feed time spent before full ramp.
- **reported gains:** P(skip) model AUC +10% offline with dwell features; online A/B: large reduction in skipped updates, increased click/viral engagement, and increased time spent on feed (no exact percentage lifts stated in source).
- **applicability note for a two-sided dating recommender:** Early industrial pattern for turning passive consumption (profile dwell / read time) into a ranking head when likes and matches are sparse—useful for modeling swipe hesitation or quick skips as negative signal alongside CTR/CVR heads.
- **applicability note for a two-sided dating recommender:** Single-sided feed ranking with no reciprocity, congestion on the viewed profile, or retention/revenue labels; skip threshold is global across content types rather than adaptive to viewer or card type.
- **unverified claims:** none
