# Requirements — 20260917_survey_grok

Date: 2026-09-17
Parent: `../requirements.md` (Runs 1–2, April 2026). Independent of sibling `../20260917_survey/`.

## Request

Answer two follow-up questions against the parent attribution-based-retention survey, then recommend a replacement for last-touch N7 swipe attribution on a dating platform.

- **Q1.** What is the latest attribution-based approach in the industry? (2025-01 to 2026-09 industry/production systems, plus newest output from classic-paper authors/teams.)
- **Q2.** Is there any published attribution-based retention in industry? (No date limit. Academic work counts only with a production dataset or deployment.)

## Core keywords

- multi-touch attribution, data-driven attribution, causal attribution, conversion attribution
- incrementality measurement, attribution calibration
- Shapley / Markov / attention-based attribution
- retention attribution, engagement attribution, credit assignment for long-term retention
- incremental value of a recommendation / notification / swipe / match on days-active
- last-touch vs multi-touch vs removal-effect vs experiment-calibrated DDA

## Search strategy (mandatory)

1. **Author and team following.** For every row of the follow list in `./README.md`, search OpenAlex / Semantic Scholar / arXiv / web for 2025–2026 output. Log every check, including "nothing new found".
2. **Q1 topic queries (2025–2026).** multi-touch attribution; data-driven attribution; causal attribution; conversion attribution; incrementality measurement; attribution calibration; attention-based attribution; Shapley attribution advertising; privacy-preserving attribution; production MTA LinkedIn Amazon Google Meta Alibaba.
3. **Q2 topic queries (no date limit).** retention attribution; engagement attribution; credit assignment for long-term user retention; RL for user retention; incremental value of a recommendation or notification on retention; dating app match or like effect on retention; days-active causal effect of in-app action; survival attribution of app events.
4. **Engineering blogs and industry venues, 2025–2026.** Parent B1–B11 plus Amazon Science, Alibaba/Alimama, Snap, Spotify Research, Pinterest, Uber, Airbnb, DoorDash, Lyft, Booking, Match Group / Tinder / Hinge / Bumble, Kuaishou, Tencent, ByteDance; venues KDD, WWW, CIKM, RecSys, WSDM, SIGIR, ADKDD 2025–2026.
5. **NotebookLM.** Reuse the parent notebook `6a3b8a8e-6f2f-4efe-99eb-283983fc95d9` for queries, deep research, and ingesting new sources. Do not create a second topic notebook. Also query related notebooks `unified-ltv-ranking-dating` and `two-sided-market-balancing-dating` for Q2-adjacent retention work.
6. **Related internal surveys.** Harvest Q2 candidates from `literature-survey/unified-ltv-ranking-dating/` (RLUR, GFN4Retention, AURO, SEC, OCARM, RevisitMTL) and `literature-survey/two-sided-market-balancing-dating/` (MRet). These are retention-optimization papers, not MTA; record whether they produce per-interaction credit.

## Scope and constraints

- Target: 25–50 **new** items processed into `./read-papers/`. Do not re-process papers already in parent `../read-papers/`.
- Priority: (a) Q2 hits from any platform; (b) 2025–2026 industry attribution systems; (c) 2025–2026 output from the follow list; (d) 2025–2026 academic MTA.
- Exclude: pure CTR/CVR with no attribution/causal component; MMM-only unless it introduces user-level credit; LLM text attribution.
- Per-paper extraction through NotebookLM `notebook_query` scoped by `source_ids`, three queries per paper.
- Synthesis: NotebookLM cross-source queries, Codex draft, optional Cursor independent review. Raw reviewer outputs in `./review/`.
- Recommendation must beat last-touch N7 → latest swipes, and must state how it maps to swipe / match / conversation touchpoints.

## Project Context

See `./README.md` for the canonical Project Context. This file references it; do not duplicate.

## Result summary

- **Cards:** 41 in `./read-papers/` (G1–G15 processed; expansion G16–G25 processed; G26–G27 Netflix stubs; RecSys 2026 addendum G28–G40 NLM-extracted 2026-09-24; G41 Zhang/Gao Causal Transformer MTA paywall stub). G23 Downstream Rewards not re-extracted; RecSys 2026 venue noted on the existing card. Parent `../read-papers/` was not re-processed.
- **Categories in `literature-review.md`:** 6 (+ low-relevance); RecSys 2026 papers folded into existing categories.
- **Q1.** Latest carded industry attribution (2025–26): Liu et al., *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization*, arXiv 2026 (front-door deletion scores at Kuaishou, upload outcome); Wu et al., *Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?*, CIKM 2026 (LLM touch selection for CVR); Bhat et al., *Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM*, arXiv 2026 (campaign-level, no user-level credit); Bencina et al., *Buyer Journey Insights with Data-Driven Attribution*, LinkedIn Engineering 2025 (sequence DDA calibrated to holdouts/MMM). RecSys 2026 Zhang and Gao Causal Transformer MTA is a paywalled advertising-conversion stub (G41) and does not displace ALM-MTA. Amazon Ads MTA 2025 remains parent-only (no new card this run).
- **Q2.** No TRUE per-touch retention MTA after RecSys 2026 addendum (G28–G41 all NOT). PARTIAL still: RevisitMTL, IURO, IURO+, FID, Netflix message holdback (stub). NOT: RLUR, GFN4Retention, AURO, SEC, OCARM, MRet, MODE, PROMISE, STEPS, Cascade Reward, Spillover CBR (LT-7 ATE not credit), and remaining RL/LTR/bandit cards. Match Group / Tinder / Hinge / Bumble: no publications (D3). Related notebooks over-classified GFN/MRet as TRUE; cards override.
- **Recommendation.** Keep binary N7. v1 = interpretable removal score (not incremental lift) mapped onto swipe/match/conversation tokens, after Liu et al. ALM-MTA + Ding et al. IURO+. v2 = calibrated deep DDA + discrete-time survival head after Bencina et al. LinkedIn DDA. Add v3 persistent holdbacks after Vlontzos et al. *Incremental Recommendation via Causal Models*, arXiv 2026, plus spillover-contained cluster tests after Min et al. RecSys 2026, before claiming incremental N7.
- **Review:** Codex draft `review/v1-codex-draft-raw.txt` (16/16 proof quotes); Claude Opus independent review `review/v1-claude-review-raw.txt` (PASS WITH FIXES; 7 items; 5 applied, 2 number-stripping items rejected after card verification). RecSys 2026 addendum: Codex `review/v2-recsys-addendum-codex-raw.txt` (PASS WITH FIXES: truncated review surface omitted three production numbers that are on G30/G34/G40 cards; Zhang/Gao not overclaimed; plan unchanged).
- **NLM notebook:** `6a3b8a8e-6f2f-4efe-99eb-283983fc95d9`, 163 sources after RecSys addendum ingest (148 immediately before this addendum; 72 at parent start of this workstream). Accidental notebook `ff0bf9af-…` unused.
