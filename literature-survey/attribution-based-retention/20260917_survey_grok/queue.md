# Queue — 20260917_survey_grok

Format: `id | year | title | source/venue | url | Q1/Q2/both | priority | nlm:<source_id or pending or failed:reason> | status`

Priority: 1 = Q2 direct / 2025–26 industry attribution system; 2 = follow-list 2025–26; 3 = 2025–26 academic MTA; 4 = adjacent RL-retention.

Do not re-process titles already in `../read-papers/`. Shared notebook: `6a3b8a8e-6f2f-4efe-99eb-283983fc95d9`.

## To Process

(empty — G1–G15 processed; expansion G16–G25 processed; G26–G27 stub cards after NLM/jina/WebFetch failure)
# duplicate NLM sources of G15 (delete if approved): html 140fe6f7-31c0-4003-aed0-cb964b46adaa ; abs 5c876e0b-eb45-4009-a864-dc44357f7427

## Already in parent notebook — do not re-ingest

- LiDDA (2505.09861), Amazon Ads MTA (2508.08209), MAL (2508.15217), CABB (2507.15113), PVM (2511.22918), CDA (2512.21211), MAC/MoAE (2603.02184), Attribution Sets (2602.06276)
- PIE (2304.06828), Robyn (2403.14674), Graphical MTA (2302.06075)

## Skipped

- TRMTA (ISCAIT 2025 IEEE) | paywall
- Amazon OOH incrementality blog | geo experiment, not per-touch
- Privacy Sandbox ARA / PoPETs 2025 | measurement infra
- SDMTA / Interpretable State and Time Dependent MTA (Soucar, ICML 2026 in review) | no PDF
- Nair 2025 RTB causal inference (Marketing Science) | not MTA credit; paywall
- Patent/academic MTA surveys (ICOA, Frontiers FBF, post-cookie review) | no production system
- Efficient Shapley influence in social networks (2026) | not conversion-path MTA
- Google Meridian blogs | MMM / geo incrementality, no user-level credit
- Uber Tarot, Stripe/Shopify incrementality blogs | treatment-level lift, not per-touch retention
- Dating RCTs / survival (WLY, choice capacity, positive churn, assortment, mobile adoption, premium) | engagement/churn, not swipe→days-active credit
- Match Group / Tinder / Hinge / Bumble engineering | **no results** (D3+D4)
- D2 author teams with nothing new: JD/Nair MTA, eBay DeepMTA, SJTU DARNN, ICT CausalMTA, DCRMTA, CAMTA, Athey/Wager/Nie marketing-attribution, Provost/Dalessandro/Perlich, listed names Yixuan An / Zihe Wang
- Wrong arXiv ingest (not extracted): 2208.07022 text-to-image; 2003.07302 Dash hashing; 2002.05792 shrinkage — Surrogate ACM is `cb0d9351…`; Duolingo is `3f40b05f…`

## Done

G1 | 2026 | Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution? (LOTUS) | CIKM 2026 / Alibaba | https://arxiv.org/pdf/2608.28649.pdf | Q1 | 1 | nlm:118a06c8-9072-4e89-bab7-f1e22de5a51a | done | `read-papers/2026_CIKM_LOTUS_Meaningful-Touchpoints-Conversion-Attribution.md`
G2 | 2026 | Integrated Marketing Attribution (IMA) | arXiv / Lowe's | https://arxiv.org/pdf/2606.16878.pdf | Q1 | 2 | nlm:61bdb620-ede0-430e-a39d-f7888235fd5c | done | `read-papers/2026_arXiv_IMA_Integrated-Marketing-Attribution.md`
G3 | 2025 | Buyer Journey Insights with Data-Driven Attribution | LinkedIn Engineering blog | https://www.linkedin.com/blog/engineering/marketing/buyer-journey-insights-with-data-driven-attribution | Q1 | 1 | nlm:7a88f033-bb50-43c2-ae8e-f2fd407c8ebb | done | `read-papers/2025_LinkedIn_LiDDA_Buyer-Journey-Data-Driven-Attribution.md`
G4 | 2024 | Future Impact Decomposition in Request-level Recommendations (FID) | KDD / Kuaishou | https://arxiv.org/pdf/2401.16108.pdf | Q2 | 1 | nlm:088b1ae5-f3f7-4ccc-88db-d6e8408e50f1 | done | `read-papers/2024_KDD_FID_Future-Impact-Decomposition.md`
G5 | 2026 | Save, Revisit, Retain (RevisitMTL) | AAAI / Pinterest | https://arxiv.org/pdf/2511.18013.pdf | Q2 | 1 | nlm:6d64098b-cfd7-44cc-9e0d-14a3b30bba04 | done | `read-papers/2026_AAAI_RevisitMTL_Save-Revisit-Retain.md`
G6 | 2026 | Retention-Optimized Two-Sided Matching (MRet) | ICLR / dating platform | https://arxiv.org/pdf/2602.15752.pdf | Q2 | 1 | nlm:da74515a-9d0d-4f88-9161-7aa430fe7686 | done | `read-papers/2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md`
G7 | 2023 | RLUR | WWW / Kuaishou | https://arxiv.org/pdf/2302.01724.pdf | Q2 | 4 | nlm:7d87bba2-fe8d-4f09-87ad-713b22aaca47 | done | `read-papers/2023_WWW_RLUR_Reinforcing-User-Retention.md`
G8 | 2024 | GFN4Retention | KDD / Kuaishou | https://arxiv.org/pdf/2406.06043.pdf | Q2 | 4 | nlm:1000111e-44ac-4cc3-a39f-584e06ac7da6 | done | `read-papers/2024_KDD_GFN4Retention_Modeling-User-Retention.md`
G9 | 2025 | AURO | WWW / Kuaishou | https://arxiv.org/pdf/2310.03984.pdf | Q2 | 4 | nlm:db4edc42-fa93-4822-8a60-f0c7116ffa57 | done | `read-papers/2025_WWW_AURO_Adaptive-User-Retention-Optimization.md`
G10 | 2025 | SEC | CIKM / Kuaishou | https://arxiv.org/pdf/2504.05628.pdf | Q2 | 4 | nlm:d9a6d934-5dad-4efc-8e08-c62a0184f137 | done | `read-papers/2025_CIKM_SEC_Stratified-Expert-Cloning.md`
G11 | 2026 | OCARM | arXiv / Kuaishou | https://arxiv.org/pdf/2604.25839.pdf | Q2 | 4 | nlm:7f131324-1d54-4dd2-8a1c-98f5f0ce8dfd | done | `read-papers/2026_arXiv_OCARM_Post-Conversion-Content-Retention.md`
G12 | 2026 | ALM-MTA: Front-Door Causal Multi-Touch Attribution for Creator-Ecosystem Optimization | ICLR 2026 | https://arxiv.org/pdf/2605.08881.pdf | Q1 | 2 | nlm:42ed27d5-3e90-483f-b728-e5cdab72cfcd | done | `read-papers/2026_ICLR_ALM-MTA_Front-Door-Causal-Multi-Touch-Attribution.md`
G13 | 2023 | Interpretable User Retention Modeling in Recommendation (IURO) | RecSys / Tencent WeChat | https://dl.acm.org/doi/pdf/10.1145/3604915.3608818 | Q2 | 1 | nlm:47cf0db1-92bc-49da-b44f-af65cea80083 | done | `read-papers/2023_RecSys_IURO_Interpretable-User-Retention-Modeling.md`
G14 | 2026 | Rethinking User Retention Modeling in Recommendation (IURO+) | TOIS / Tencent WeChat | https://dl.acm.org/doi/pdf/10.1145/3790098 | Q2 | 1 | nlm:dc389695-c31e-4eba-a1d2-00268bcf0ac1 | done | `read-papers/2026_TOIS_IURO+_Rethinking-User-Retention-Modeling.md`
G15 | 2025 | Harnessing Interleaving and Counterfactual Evaluation for Airbnb Search Ranking | KDD / Airbnb | https://arxiv.org/pdf/2508.00751.pdf | Q2 | 3 | nlm:4c1119dd-6713-4864-a194-a53a14065084 | done | `read-papers/2025_KDD_NA_Interleaving-Counterfactual-Airbnb-Search.md`
G16 | 2025 | Impatient Bandits: Optimizing Recommendations for the Long-Term Without Delay | JMLR / Spotify | https://arxiv.org/pdf/2501.07761.pdf | Q2 | 4 | nlm:c7d8e9d2-5ee2-4cbf-ab8a-15cba733edc1 | done | `read-papers/2025_JMLR_ImpatientBandits_Optimizing-Recommendations-Long-Term.md`
G17 | 2023 | DT4Rec: User-Retention Oriented Decision Transformer | WWW | https://arxiv.org/pdf/2303.06347.pdf | Q2 | 4 | nlm:cf9de03f-0d61-4f7e-85ee-1cc46fb9ef3c | done | `read-papers/2023_WWW_DT4Rec_User-Retention-Oriented-Decision-Transformer.md`
G18 | 2026 | Incremental Recommendation with Causal Models | arXiv | https://arxiv.org/pdf/2608.26804.pdf | Q2 | 3 | nlm:15cdd352-b889-48d8-a3d5-4bdabefd67f8 | done | `read-papers/2026_arXiv_NA_Incremental-Recommendation-Causal-Models.md`
G19 | 2024 | Learned Ranking Function (LRF) — YouTube | RecSys / Google | https://arxiv.org/pdf/2408.06512.pdf | Q2 | 4 | nlm:9a650298-5c0c-48d2-9597-450c32a73457 | done | `read-papers/2024_RecSys_LRF_Learned-Ranking-Function-YouTube.md`
G20 | 2022 | Long-run User Value Optimization | arXiv / Meta | https://arxiv.org/pdf/2204.11421.pdf | Q2 | 4 | nlm:d017d9e2-9833-4411-b351-5d5a4fe920cc | done | `read-papers/2022_arXiv_NA_Long-run-User-Value-Optimization-Meta.md`
G21 | 2022 | Surrogate for Long-Term User Experience | KDD / Google | https://dl.acm.org/doi/pdf/10.1145/3534678.3539073 | Q2 | 4 | nlm:cb0d9351-5064-4c9b-b669-e5f25fe0203f | done | `read-papers/2022_KDD_NA_Surrogate-Long-Term-User-Experience.md`
G22 | 2024 | Sequential Recommendation: Immediate Feedback and Long-term Retention | arXiv | https://arxiv.org/html/2404.03637 | Q2 | 4 | nlm:305cd94b-33e0-46f8-961a-2228a9d46046 | done | `read-papers/2024_arXiv_NA_Sequential-Rec-Immediate-Feedback-Long-term-Retention.md`
G23 | 2026 | Model-agnostic Downstream Rewards for Long-Term Engagement | arXiv | https://arxiv.org/html/2607.14192 | Q2 | 4 | nlm:1a74145c-f8bc-438b-a5ea-965b29abab16 | done | `read-papers/2026_arXiv_DownstreamRewards_Long-Term-Engagement-Optimization.md`
G24 | 2026 | Direct Causal Effect Optimization (DCEO) | arXiv | https://arxiv.org/html/2608.25635 | Q2 | 3 | nlm:d18bf088-6fb0-4082-952c-2a13f61ffc2e | done | `read-papers/2026_arXiv_DCEO_Direct-Causal-Effect-Optimization.md`
G25 | 2020 | Sleeping / Recovering Bandits for Notifications (RDSA) | KDD / Duolingo | https://research.duolingo.com/papers/yancey.kdd20.pdf | Q2 | 4 | nlm:3f40b05f-169b-4e36-b317-fdadf7a86bc1 | done | `read-papers/2020_KDD_RDSA_Sleeping-Recovering-Bandit-Notifications.md`
G26 | 2023 | Incrementality-Focused Messaging Measurement | Netflix blog | https://medium.com/notificationsblog/incrementality-focused-messaging-measurement-all-the-time-everywhere-94ef0c229368 | Q2 | 1 | nlm:failed:url-and-jina-and-webfetch | done-stub | `read-papers/2023_NetflixBlog_NA_Incrementality-Focused-Messaging-Measurement.md`
G27 | 2026 | A Human-Augmenting Agentic Workflow for Causal Inference (oci-agent) | Netflix techblog | https://netflixtechblog.com/a-human-augmenting-agentic-workflow-for-causal-inference-4623f0a9c5af | Q2 | 3 | nlm:failed:url-and-jina-and-webfetch | done-stub | `read-papers/2026_NetflixBlog_oci-agent_Causal-Inference-Workflow.md`

## Author-follow log

| Group | 2025–2026 result |
|---|---|
| LinkedIn / Bencina | LiDDA in parent; NEW production blog (G3) |
| Amazon Ads Lewis/Zettelmeyer/Gordon | Amazon MTA in parent; nothing new from named authors |
| Alibaba Chen/Chan/Sheng | MAL + MAC in parent; NEW LOTUS (G1) |
| Google Vaver/Sundararajan/Ghazi | Attribution Sets in parent; Privacy Sandbox infra only |
| Meta Moakler/Runge/Zeng | CABB in parent; PIE/Robyn already ingested |
| Adobe Arava/Sinha/Arbour | Graphical MTA journal version of ingested preprint |
| Criteo Diemert/Lefortier | nothing new |
| JD / Nair | nothing new on MTA; tangential RTB paper skipped |
| eBay Yang/Dyer | nothing new |
| SJTU/UCL Zhang/Ren/Wang/Yu | nothing new on MTA |
| ICT Yao/Gong/Bi | nothing new on CausalMTA/CausalMMM |
| Tang/Jing DCRMTA | nothing new |
| Kumar/Ravindran CAMTA | nothing new |
| Athey/Wager/Nie | nothing new on marketing attribution |
| Provost/Dalessandro/Perlich | nothing new |
| Renmin An/Wang | listed names do not match PVM authors; PVM already in parent |
| Kuaishou Cai/Liu/Gai/Jiang | RLUR/GFN/AURO/SEC/FID/OCARM/ALM-MTA queued |
| Tencent / ByteDance / Snap / Spotify / Pinterest / Duolingo / Match Group | see D3/D4; IURO + RevisitMTL are the Q2-partial hits |

## Engineering blog search log (D4)

| Blog | 2025–2026 |
|---|---|
| netflixtechblog.com | hits: analytics incrementality survey; oci-agent causal/retention (NLM fetch failed) |
| engineering.fb.com | no results |
| research.google / blog.google | Meridian MMM / GeoX (skipped: MMM-only) |
| engineering.linkedin.com | Buyer journey DDA (G3) |
| doordash.engineering | no results |
| eng.uber.com | Tarot incentive uplift (skipped) |
| medium.com/airbnb-engineering | no results (KDD paper is G15) |
| medium.com/pinterest-engineering | ads conversion window / shopping CG (not MTA) |
| shopify.engineering | generative rec incremental recall (skipped) |
| stripe.com/blog | payment/pricing holdbacks (skipped) |
| amazon.science | OOH experiment (skipped) |
| Spotify engineering/research | no results |
| Snap engineering | no results |
| lyft.com/engineering | no results |
| booking.engineering | no results |
| Match Group / Tinder / Hinge / Bumble | no results |
| Kuaishou / Tencent / ByteDance English blogs | no results |
