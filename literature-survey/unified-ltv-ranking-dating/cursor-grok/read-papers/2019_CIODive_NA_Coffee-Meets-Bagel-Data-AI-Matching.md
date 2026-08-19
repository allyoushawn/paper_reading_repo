# Paper Analysis: How Coffee Meets Bagel leverages data and AI for love

**Source:** https://www.ciodive.com/news/coffee-meets-bagel-dating-technology-ai-data/548395/  
**Date analyzed:** 2026-08-16  
**Workplace:** cursor-grok

## Survey Card

- **title:** How Coffee Meets Bagel leverages data and AI for love
- **authors or company:** Alex Hickey (CIO Dive); interviewed Will Wagner, CTO, Coffee Meets Bagel
- **venue:** CIO Dive
- **year:** 2019
- **URL:** https://www.ciodive.com/news/coffee-meets-bagel-dating-technology-ai-data/548395/
- **source type:** industry blog
- **direction:** D8
- **problem setting:** Mobile-only curated dating app (#LadiesChoice): men receive up to 21 daily "bagel" matches; interested men trigger up to six curated matches for women; product optimizes meaningful connections over swipe volume; 50Mth connection milestone cited at interview time.
- **objective and label definition:** Success = deep meaningful connections moving offline, not time-on-app or like counts; KPIs evolving toward connect/chat on-platform and sharing personal information; explicit rejection of likes/time as success proxies; no retention/LTV model or label horizon specified.
- **prediction or incrementality:** Deep neural network "blended" matcher: nine models score candidates, system converges to final match score; not described as incrementality or causal uplift modeling.
- **model architecture:** Nine-model ensemble with converged score; discovery section plus daily curated batches; asymmetric caps (up to 21 bagels for men, up to six for women after male interest); AWS-primary, GCP-secondary mobile stack; outsourced phone verification and BI.
- **credit assignment:** Not specified in source; batch daily curation rather than per-impression attribution.
- **training data and counterfactual handling:** Signup explicit attributes plus implicit behavior over time; company testing whether arbitrary filters (e.g., height) limit matches and may prompt preference updates; no counterfactual or off-policy methodology described.
- **offline and online evaluation:** #LadiesChoice claimed >50% of women felt more control; no A/B metrics, match-rate, or retention numbers reported; qualitative product narrative only.
- **reported gains:** #LadiesChoice helped >50% of female users feel more control (company-reported); average male wanted 17 bagels/day vs average woman wanted four "high quality" bagels (company-reported); no model accuracy or revenue/retention lifts in source.
- **applicability note for a two-sided dating recommender:** Asymmetric daily caps and female-initiated second stage are a real production pattern for congestion control and bilateral consent in curated dating (vs unlimited swipe feeds).
- **applicability note for a two-sided dating recommender:** Article lacks reproducible metrics, model architecture detail, and LTV/retention optimization — nine-model ensemble is opaque for benchmarking unified ranking objectives.
- **unverified claims:** "Nine models" blended scoring and >50% female control improvement are company-reported without independent validation in source.
