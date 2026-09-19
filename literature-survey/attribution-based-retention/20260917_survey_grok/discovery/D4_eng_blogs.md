# D4 — Engineering & industry blog discovery (2025-01 → 2026-09)

Discovery run: 2026-09-17. Scope: attribution, incrementality, MTA, retention credit assignment.

**Q1** = marketing/ad attribution, MTA, DDA, incrementality measurement.  
**Q2** = per-interaction credit for delayed retention / long-horizon engagement outcomes.

---

## netflixtechblog.com

| year | title | org | URL | Q1/Q2 | relevance |
|------|-------|-----|-----|-------|-----------|
| 2025 | Part 2: A Survey of Analytics Engineering Work at Netflix | Netflix | https://netflixtechblog.com/part-2-a-survey-of-analytics-engineering-work-at-netflix-4f1f53b4ab0f | Q1 | Synthetic-control incrementality for games UA (installs, engagement, signups), incremental ROI model, incremental account LTV framing. |
| 2026 | A Human-Augmenting Agentic Workflow for Causal Inference | Netflix | https://netflixtechblog.com/a-human-augmenting-agentic-workflow-for-causal-inference-4623f0a9c5af | Q2 | Open-sourced `oci-agent` for observational causal inference; case study includes retention treatment-effect estimation with overlap/trimming diagnostics. |

---

## engineering.fb.com / research.facebook.com

**no results from engineering.fb.com / research.facebook.com for attribution, incrementality, MTA, or retention credit assignment in 2025–2026.**

2025–2026 ads posts (GEM, Adaptive Ranking Model) cover conversion ranking/ROAS, not touchpoint credit or incrementality methodology.

---

## research.google / ai.googleblog.com / blog.google

| year | title | org | URL | Q1/Q2 | relevance |
|------|-------|-----|-----|-------|-----------|
| 2025 | Meridian is now available to everyone | Google | https://blog.google/products/ads-commerce/meridian-marketing-mix-model-open-to-everyone/ | Q1 | Open-source Bayesian MMM with incrementality experiments as priors; reach/frequency and cross-channel budget calibration. |
| 2026 | Drive profitable growth with new data and measurement tools | Google | https://blog.google/products/ads-commerce/data-strength-updates/ | Q1 | Meridian GeoX GA for geo incrementality; agentic MMM tooling; incremental ROAS from first-party data strength. |
| 2026 | Turn your data into decisions: growth in the AI era (Google Marketing Live) | Google | https://blog.google/products/ads-commerce/google-marketing-live-2026-turn-your-data-into-decisions/ | Q1 | Meridian GeoX + Meridian Studio; positions causal geo-experiments as ground truth for media mix decisions. |
| 2026 | Turn data into decisions with unified measurement (Meridian in GA 360) | Google | https://blog.google/products/marketingplatform/analytics/meridian-google-analytics-360/ | Q1 | Integrates Meridian MMM into GA360 for causal cross-channel performance and scenario forecasting. |

---

## engineering.linkedin.com

| year | title | org | URL | Q1/Q2 | relevance |
|------|-------|-----|-----|-------|-----------|
| 2025 | Buyer journey insights with data-driven attribution | LinkedIn | https://www.linkedin.com/blog/engineering/marketing/buyer-journey-insights-with-data-driven-attribution | Q1/Q2 | Production transformer DDA/MTA with paid-media imputation, MMM post-calibration, and counterfactual path-lift aligned to holdout incrementality tests (precursor/public companion to LiDDA). |

---

## doordash.engineering

**no results from doordash.engineering for 2025–2026** on attribution, incrementality, MTA, or retention credit assignment (only pre-2025 marketing-attribution and causal-experiment posts surfaced).

---

## eng.uber.com

| year | title | org | URL | Q1/Q2 | relevance |
|------|-------|-----|-----|-------|-----------|
| 2026 | Beyond Prediction: Solving the Multiple Knapsack Problem at Scale (Tarot) | Uber | https://www.uber.com/blog/solving-multiple-knapsack/ | Q1 | Production uplift-model + CP-SAT optimizer allocates incentive budgets to maximize predicted incremental marketplace ROI under pacing constraints. |

---

## medium.com/airbnb-engineering

**no results from medium.com/airbnb-engineering for 2025–2026** on attribution/incrementality/MTA/retention credit (2022 interleaving-attribution post exists but predates window; 2025 search-ranking work appears as KDD paper below, not a new Medium post in window).

---

## medium.com/pinterest-engineering

| year | title | org | URL | Q1/Q2 | relevance |
|------|-------|-----|-----|-------|-----------|
| 2026 | Handling Online-Offline Discrepancy in Pinterest Ads Ranking System | Pinterest | https://medium.com/pinterest-engineering/handling-online-offline-discrepancy-in-pinterest-ads-ranking-system-8fd662da4c2d | Q1 | Mentions dedicated work optimizing view-through checkout **attribution time window** for conversion-model training (not full MTA system write-up). |
| 2026 | From Clicks to Conversions: Architecting Shopping Conversion Candidate Generation at Pinterest | Pinterest | https://medium.com/pinterest-engineering/from-clicks-to-conversions-architecting-shopping-conversion-candidate-generation-at-pinterest-04cae5e1455b | Q1 | Conversion/ROAS modeling at retrieval layer; uses delayed offsite conversion labels and advertiser-attributed events, but not touchpoint credit allocation. |

---

## shopify.engineering

| year | title | org | URL | Q1/Q2 | relevance |
|------|-------|-----|-----|-------|-----------|
| 2026 | The generative recommender behind Shopify's commerce engine | Shopify | https://shopify.engineering/generative-recommendations | Q2 | Trains for **incremental recall** (true positives missed by ensemble) via boosting-style hard negatives; online A/B lifts on orders/conversion/recall@k. |

---

## stripe.com/blog

| year | title | org | URL | Q1/Q2 | relevance |
|------|-------|-----|-----|-------|-----------|
| 2025 | Testing the conversion impact of 50+ global payment methods | Stripe | https://stripe.com/blog/testing-the-conversion-impact-of-50-plus-global-payment-methods | Q1 | Large-scale holdback experiment measuring incremental conversion/revenue lift from surfacing additional payment methods (100% incrementality cited for some bank debits). |
| 2026 | Testing the impact of Adaptive Pricing across 1.5M subscription checkout sessions | Stripe | https://stripe.com/blog/adaptive-pricing-for-subscriptions | Q1/Q2 | 1% randomized holdback estimates incremental signup conversion (+4.7%) and LTV per session (+5.4%) from localized pricing. |

---

## amazon.science

| year | title | org | URL | Q1/Q2 | relevance |
|------|-------|-----|-----|-------|-----------|
| 2025 | A first-of-its-kind experiment to measure the impact of out-of-home advertising | Amazon | https://www.amazon.science/blog/a-first-of-its-kind-experiment-to-measure-the-impact-of-out-of-home-advertising | Q1 | Geo-randomized OOH experiment with survey-based exposure fractions; synthetic control / DiD for causal incrementality of metro-rail ads on sales. |

---

## engineering.atspotify.com / research.atspotify.com

**no results from engineering.atspotify.com / research.atspotify.com for 2025–2026** on attribution, MTA, or marketing incrementality.

2025–2026 posts cover experimentation infrastructure, contextual bandits, and long-term effect estimation (LOPE/survival) without per-touchpoint marketing or retention credit assignment.

---

## eng.snap.com / engineering.snap.com

**no results from eng.snap.com for 2025–2026** on attribution, incrementality, MTA, or retention credit assignment.

2026 experimentation-platform GPU post supports A/B infrastructure (CUPED, HTe, SRM) but does not document ads incrementality or touchpoint credit.

---

## lyft.com/engineering

**no results from lyft.com/engineering for 2025–2026** on attribution, incrementality, MTA, or retention credit assignment.

---

## booking.engineering / booking.com blog

**no results from booking.engineering for 2025–2026** on attribution/incrementality methodology.

Partner Click Magazine earnings posts mention “incremental bookings” from Genius/Connected Trip but contain no engineering measurement write-up.

---

## news.ycombinator.com — multi-touch attribution / incrementality discussions (2025–2026)

| year | title | org | URL | Q1/Q2 | relevance |
|------|-------|-----|-----|-------|-----------|
| 2025 | Google knows who visited. Stripe knows who paid. I built the missing link (Boone) | Show HN / Boone | https://news.ycombinator.com/item?id=44756019 | Q1 | Thread on stitching UTM/referrer capture to Stripe revenue for source-level paying-customer attribution. |
| 2026 | Show HN: Trace – Lightweight install attribution and deep links for mobile apps | Show HN / Trace | https://news.ycombinator.com/item?id=47322543 | Q1 | Mobile install attribution via deep-link matching + probabilistic signals; CLI-first MTA-adjacent tooling discussion. |
| 2026 | Attribution in the Browser: Who Benefits from Mozilla/Google/Meta's Ad Standard | HN discussion | https://news.ycombinator.com/item?id=48409244 | Q1 | Debate on W3C Attribution API vs MMP/web2app attribution overlap (privacy-preserving aggregate conversion measurement). |
| 2026 | Show HN: Revliu – Multi-touch attribution from acquisition to revenue | Show HN / Revliu | https://news.ycombinator.com/item?id=49625804 | Q1 | SaaS MTA stack linking anonymous journey → signup → Stripe revenue by source/campaign. |
| 2026 | Hershey Bets on Agentic AI to Rethink $2B in Marketing Spend (thread) | HN discussion | https://news.ycombinator.com/item?id=48178929 | Q1 | Discusses MMM vs fuzzy attribution windows and faster incrementality/MMM iteration (Mutinex/Tracer). |

---

## Match Group / Tinder / Hinge / Bumble engineering

**no results from Match Group / Tinder / Hinge / Bumble engineering blogs for 2025–2026** on attribution, incrementality, MTA, or retention credit assignment (only MarTech job postings referencing AppsFlyer/SKAN/MMM hiring).

---

## Kuaishou / Tencent / ByteDance — English tech blogs

**no English-language tech blog posts found from Kuaishou, Tencent, or ByteDance in 2025–2026** on attribution/incrementality/MTA/retention credit.

Related 2025–2026 **papers** (not company blogs) include Kuaishou ALM-MTA (front-door causal MTA) and ByteDance/TikTok cannibalization-corrected attribution (arXiv); omitted here per blog-only scope.

---

## Conference industry / applied tracks (2025–2026)

### RecSys 2025

| year | title | org | URL | Q1/Q2 | relevance |
|------|-------|-----|-----|-------|-----------|
| 2025 | Agentic Personalisation of Cross-Channel Marketing Experiences | Booking.com (authors: Abboud, Hanna, Jeunen, Raheja, Wheeler) | https://doi.org/10.1145/3705328.3748125 | Q1 | DiD/sparse-ITS individual treatment effects + Thompson sampling to optimize **incremental** engagement across email/push/in-app; deployed ~150M users. |

### KDD 2025

| year | title | org | URL | Q1/Q2 | relevance |
|------|-------|-----|-----|-------|-----------|
| 2025 | Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking | Airbnb | https://doi.org/10.1145/3711896.3737232 | Q2 | Defines booking **event attribution** to all in-experiment listing exposures (multi-session journeys); interleaving + counterfactual eval vs A/B ground truth. |
| 2025 | Robust Uplift Modeling with Large-Scale Contexts for Real-time Marketing | Kuaishou + academia | https://doi.org/10.1145/3690624.3709293 | Q1 | Context-aware uplift modeling for real-time marketing incentives on large item spaces (incremental response estimation under distribution shift). |
| 2025 | Dynamic Synthetic Controls vs. Panel-Aware Double Machine Learning for Geo-Level Marketing Impact Estimation | Industry/academia (KDD Causal ML workshop) | https://doi.org/10.48550/arxiv.2508.20335 | Q1 | Benchmarks geo incrementality estimators (Augmented SCM vs panel-DML) for marketplace marketing lift. |

**KDD 2025 ADS track:** no additional LiDDA/Amazon-MTA/industry MTA paper titles matched attribution/incrementality keywords in public ADS listings (LiDDA remains arXiv/industry preprint).

### WWW 2025 (Industry Track)

| year | title | org | URL | Q1/Q2 | relevance |
|------|-------|-----|-----|-------|-----------|
| 2025 | Amazon Ads Multi-Touch Attribution | Amazon Ads | https://arxiv.org/pdf/2508.08209 | Q1 | RCT-calibrated ML MTA allocating conversion credit across Amazon Ads touchpoints (PIE extension). |

*(Published as Amazon Ads whitepaper/industry release Aug 2025; WWW industry-track call covers deployed applied work—verify exact WWW session listing separately if needed.)*

### CIKM 2025 (Applied Research Track)

| year | title | org | URL | Q1/Q2 | relevance |
|------|-------|-----|-----|-------|-----------|
| 2025 | See Beyond a Single View: Multi-Attribution Learning Leads to Better Conversion Rate Prediction (MAL) | Alibaba Taobao/Tmall | https://arxiv.org/abs/2508.15217 | Q1 | Multi-attribution learning for conversion prediction with explicit multi-touch feature views (not full causal incrementality system). |

**CIKM 2025:** no LiDDA or dedicated incrementality-measurement applied paper located in accepted-paper index grep.

### WSDM 2026 (Industry Day)

**no published WSDM 2026 Industry Day talks found on attribution, incrementality, MTA, or retention credit** (2026 CFP theme: LLMs/agentic AI in industrial settings; no attribution-specific accepted agenda at time of search).

---

## Summary sentence

**8 blogs with in-window hits** (Netflix, Google, LinkedIn, Uber, Pinterest, Shopify, Stripe, Amazon Science) vs **9 blogs/venues with explicit no-results logs** (Meta, DoorDash, Airbnb Medium, Spotify, Snap, Lyft, Booking engineering, Match Group dating apps, Chinese English blogs).
