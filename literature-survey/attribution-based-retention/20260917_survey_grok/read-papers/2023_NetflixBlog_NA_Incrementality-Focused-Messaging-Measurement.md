# Incrementality-Focused Messaging Measurement (Netflix) — stub

**Source:** https://medium.com/notificationsblog/incrementality-focused-messaging-measurement-all-the-time-everywhere-94ef0c229368  
**Date analyzed:** 2026-09-18  
**NLM source id:** nlm:failed:url-and-jina-and-webfetch  
**Queue id:** G26  
**Q2 class:** PARTIAL

---

## 1. Summary

Stub card. NotebookLM could not ingest the Medium URL; jina.ai and direct WebFetch also failed (Cloudflare / timeout). Discovery notes (D3, D4) describe a Netflix production messaging system with an always-on ~2% message holdback that estimates **incremental downstream viewing** per notification/message, contrasting open/click metrics with incremental watch.

## 2. Evidence

Not specified in source (fetch failed). D3 records: per-message causal incrementality via randomized withholding — a touchpoint-level incrementality design for **notifications**, not per-feed-item or swipe retention credit.

## 3. Limitations

Cannot verify numbers from the primary text in this run.

## 4. Prior works named

Not specified in source.

## 5. Project Relevance

- **Answers:** Q2 adjacent (notification incrementality), not swipe MTA.
- **Q2 class:** PARTIAL (touchpoint holdback, not in-app item).
- **Per-interaction credit:** per **message** incremental viewing, not per-swipe N7.
- **Last-touch replacement:** holdout incrementality is a calibration device for observational credit, analogous to Amazon Ads MTA's RCT calibration, not a full multi-touch retention labeler.
- **Transfer rating:** adaptable as a **notification-level** incrementality fixture, not as swipe attribution.

**Low project relevance** for swipe-level N7 labels; useful as a measurement pattern.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**PDF:** unavailable — NLM URL fetch failed; jina Cloudflare; WebFetch timeout  
**Relevance:** Related  
**Priority:** 3
