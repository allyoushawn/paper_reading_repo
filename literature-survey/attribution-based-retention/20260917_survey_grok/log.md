# Log — 20260917_survey_grok

## 2026-09-17 — Run start (lead: Cursor Grok 4.6)

- Independent of sibling `../20260917_survey/` (Claude). Same Q1/Q2; this folder is the Grok-owned deliverable.
- Parent corpus: 62 papers in `../read-papers/`; parent NLM notebook `6a3b8a8e…` (72 sources) used query-only.
- Created this-run NLM notebook `ff0bf9af-ec18-4314-b1af-762af114f4a1` by mistake. User directed reuse of parent notebook `6a3b8a8e…`. Switched; unused notebook is not the source of truth.
- Codex CLI probe: OK (`gpt-5.6-sol`).
- Next: NLM deep research (Q1, Q2) on the shared parent notebook, author-follow + industry discovery, related-survey harvest.
- Started Q1 deep research on shared notebook `6a3b8a8e…`, task `ChAwMzEzOTM5MjczMDBhOTM5EAgaBGJiOTAqA3Vzdw`.

## 2026-09-17 — D1 follow-up

- [Industry author discovery](69f488e1-4a71-4afd-8806-4d0494dddd87) wrote `discovery/D1_industry_authors.md` (10 new candidates; Amazon Ads named-authors and Criteo: nothing new).
- Semantic Scholar topic search mostly 429; retried via OpenAlex (`discovery/D5b_openalex.md`).
- Skipped parent duplicates (LiDDA, Amazon MTA, MAL, CABB, PVM, CDA, PIE v2, Robyn v3, Graphical MTA journal version).
- Ingested 11 new sources into shared notebook `6a3b8a8e…` (LOTUS, IMA, LinkedIn DDA blog, FID, RevisitMTL, MRet, RLUR, GFN4Retention, AURO, SEC, OCARM).

## 2026-09-17 — D2/D3/D4 follow-up

- [Academic author discovery](26d8a5e4-661f-4228-a180-368285cd7f52): 8/9 classic MTA teams have no 2025–2026 MTA paper; 9 topic candidates, 0 Q2 hits. ALM-MTA/IMA already queued.
- [Retention attribution discovery](39ac9f16-28de-4736-8ef0-d3906874152c): 0 strict per-touch retention-attribution papers; partial hits RevisitMTL, IURO, FID; Match Group/Tinder/Hinge/Bumble: no publications.
- [Engineering blog discovery](0dc45093-784b-4415-9104-b48749248606): 8 blogs with in-window hits; 9 explicit no-results including dating-app engineering blogs.
- Ingested IURO RecSys 2023 (`47cf0db1…`) and IURO+ TOIS 2026 (`dc389695…`) into the shared notebook. Airbnb arXiv + Netflix blogs failed NLM URL fetch (retry pending).

## 2026-09-18 — literature-survey-nlm run (resume)

- Phase reached: Phase 5 complete
- Papers in queue: Done(25) / Done-stub(2) / To Process(0) / Skipped(listed in queue.md)
- Coverage: 100% of this-run Request items (Q1, Q2, last-touch replacement, 2026-06-13 verdict) with Project Context fitness pass (binary N7, swipe/match/conversation mapping, selection bias, production evidence)
- Outputs touched: literature-review.md, executive-summary.md, method-tracker.md
- NLM notebook source count: 170 (shared notebook `6a3b8a8e…`; 72 at parent start of this workstream; accidental notebook `ff0bf9af-…` unused)
- Notable: 27 cards (G1–G27); no TRUE retention MTA; v1 is a removal score, not incremental N7; Codex `gpt-5.6-sol` drafted; Claude Opus reviewed (PASS WITH FIXES)
- Phase 3: 2 NLM queries/paper (facts + project relevance). Expansion G16–G25 from discovery. Netflix G26/G27 remain `nlm:failed:url-and-jina-and-webfetch` stubs. Airbnb later ingested as `4c1119dd…`.
- Phase 4-A: four scoped synthesis queries (mechanisms retried after timeout). Related notebooks queried; GFN/MRet over-classified TRUE there, NOT on cards.
- Phase 3.7 skipped (user: Codex 3.5-lite / 4-B / 5 only). No `survey.md`; three standard files instead.
- Independent review applied: keep binary N7; ALM-MTA cited as arXiv 2026 (ICLR not on card); FID restored to PARTIAL per D3; section titles neutralized; dating-vertical negative added; Netflix holdback row unscored. Number-stripping of 100× / millions of users / 2% boost / three years / Deep Twin rejected — those claims are on the cards.
