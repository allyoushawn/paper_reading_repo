# Attribution-based retention — survey manual

Paste-ready prompts: [`PROMPTS.md`](./PROMPTS.md).

## About this study

- **What:** periodic Q1/Q2 follow-ups on industry attribution and attribution-based retention, for a dating-app ranker whose labels come from per-swipe credit of N7 retention.
- **Why not `/literature-survey-nlm attribution-based-retention`:** Phase 0 sees the parent `executive-summary.md` and resumes the 2026-04 corpus. Follow-ups **must** use a new dated subfolder and a prompt from `PROMPTS.md`.
- **How to kick off:** new agent session → paste Prompt A, B, C, or D → replace `YYYYMMDD`.
- **Status (2026-09-18):** parent Runs 1–2 complete (62 cards). Run 3 complete in `20260917_survey/` (50 cards). Parallel Grok run in `20260917_survey_grok/` — discovery done; cards may exist; synthesis may still be missing (Prompt C).

This is **not** Survey 3 (unified LTV/ranking) or Survey 4 (marketplace balancing). Query those notebooks only to classify whether a retention-optimization paper produces **per-interaction credit**.

---

## 1. Map

| Piece | Where |
|---|---|
| This folder | `/Users/fox/Projects/paper_reading_repo/literature-survey/attribution-based-retention/` |
| Parent corpus (Runs 1–2) | `read-papers/` (62), `literature-review.md`, `executive-summary.md`, `requirements.md` |
| Run 3 complete | `20260917_survey/` |
| Run 3 Grok | `20260917_survey_grok/` |
| Shared NotebookLM | `6a3b8a8e-6f2f-4efe-99eb-283983fc95d9` (do **not** `notebook_create`) |
| Related notebooks (Q2-adjacent only) | unified-ltv `67046a44-7490-4fe5-b54a-3f39ef37fdd3`; market-balancing `d3071ac8-16ef-4460-8991-7701679974c8` |
| Decision record | `knowledge_base/projects/attribution_based_retention/literature-survey-run-1-postmortem.md` § Supplement 2026-09-17 |
| Harvest script to copy | `20260917_survey/discovery/harvest.py` |
| Codex prompt template to copy | `20260917_survey/review/codex-draft-prompt-v3-nlm.txt` |
| Generic skill (pipeline only) | `~/.claude/skills/literature-survey-nlm/SKILL.md` |
| Process lessons | `knowledge_base/projects/building_knowledge_and_agent/literature-survey/literature-survey-nlm-design.md` § Run 3 |

---

## 2. Standing questions (every follow-up)

- **Q1.** What is the latest attribution-based approach in industry? Scope: production or industry-authored attribution systems in the **new window** (day after the last completed run through today), plus newest work from the [follow list](#4-follow-list).
- **Q2.** Has anyone published **attribution-based retention** — credit for retention / engagement / days-active assigned to **individual in-app interactions** (recs, matches, messages, notifications, swipes)? **No date limit**, but skip titles already carded in the parent or a prior dated run. Academic work counts iff it names a production dataset or deployment.
- **Deliverable.** A recommendation that replaces (or confirms) last-touch: N7 (active on day 7) assigned to the user's most recent swipes. Must map credit onto swipe / like / match / conversation.

Last completed Q1 window: **2025-01 → 2026-09**. Next run's Q1 window starts **2026-09-18** unless a later dated run has finished.

---

## 3. Project context (north star)

**Product.** Dating platform. Swipe → mutual like = match → conversation.

**Goal.** Attribute a user's retention to particular swipes so a ranker can predict, per candidate profile, the incremental retention value of showing it. Attribution scores are **training labels**, not the serving model.

**Production baseline to beat.** Last-touch: the N7 label is assigned to the most recent swipes. Weaknesses: ignores earlier swipes; ignores later match/conversation; credits activity that would have happened anyway; no fractional credit.

**Standing recommendation (Run 3, 2026-09-17) — confirm or revise, do not copy blindly:**

1. **v1** predictive deletion residual \(c_j=\hat P(N7\mid H)-\hat P(N7\mid H\setminus\{e_j\})\) with user-prevalence normalization, conservation, typed event lineage, **exposure holdout + placebo-touch**. v1 is **not** incremental.
2. **v2** experiment-calibrated causal sequence attribution (treated/control/propensity heads) + discrete-time survival hazard.
3. **v3** optional front-door (match/conversation mediator) or flow credit (GFN). Gate on evidence that covariate adjustment is still biased.

**A paper is useful iff it:** produces per-interaction (or per-action incremental) credit; handles a recurring binary or time-to-event outcome; addresses selection bias (engaged users interact more); is deployed or evaluated on production data; is in the Q1 window **or** from a follow-list team.

**Analogies.** Ad touchpoint → swipe or match. Conversion → N7 (recurring). Attribution window → lookback per interaction type. Channel → like / match / conversation / notification.

---

## 4. Follow list

Check **every row** for output in the new Q1 window. Log `"nothing new"` — a null is a finding. Extend the list with teams discovered in the previous dated run (TikTok ETDC, LinkedIn 2026 targeting, Snap HTE, WeChat IURO, Instagram notifications, Pinterest Downstream Rewards / RevisitMTL).

| Group | Names | Anchor paper |
|---|---|---|
| LinkedIn | Bencina et al.; Wei et al. 2026 targeting | LiDDA (2025); From Prediction to Incrementality (2026) |
| Amazon Ads | Lewis, Zettelmeyer, Gordon, Garib, Hermle | Amazon Ads MTA (2025) |
| Alibaba / Alimama | Chen, Chan, Sheng, Zhu, Xu, Zheng, Wu | MAL, MoAE, LOTUS, CanniUplift |
| Google | Vaver, Sundararajan, Ghazi, Chen, Remy, TEDDA/UDDA/ARA authors | Trimmed Match, TEDDA, Attribution Sets |
| Meta | Gordon, Moakler, Zeng, Runge; Zhang (IG notif) | PIE, CABB, Robyn, IG notification uplift |
| Adobe | Arava, Sinha, Arbour | DNAMTA, Graphical MTA |
| Criteo | Diemert, Lefortier | Attribution-aware bidding |
| JD / Stanford | Du, Nair | JDMTA |
| eBay / USC | Yang, Dyer | DeepMTA |
| Netflix | causal inference / messaging | incrementality blogs |
| DoorDash | Berger, Bauman | Switchback |
| Thumbtack | Lee, Raghavan | Panel DML |
| SJTU / UCL | Zhang, Ren, Wang, Yu | DARNN |
| ICT / CAS | Yao, Gong, Bi | CausalMTA / CausalMMM |
| U Michigan / BJTU | Tang, Jing | DCRMTA |
| TCS / IIT | Kumar, Ravindran | CAMTA |
| Stanford / Berkeley | Athey, Wager, Nie | Causal forest, R-learner |
| NYU | Provost, Dalessandro, Perlich | Causally motivated attribution |
| Kuaishou | Cai, Liu, Gai, Jiang | RLUR, GFN4Retention, FID, ALM-MTA |
| ByteDance / TikTok | ETDC+HCA authors | Attributed, But Not Incremental (ADKDD 2026) |
| Snap | Fumagalli et al. | Snap HTE (2025) |
| Tencent / WeChat | IURO authors | IURO RecSys 2023, IURO+ TOIS 2026 |
| Pinterest | Downstream Rewards; RevisitMTL | RecSys 2026; AAAI 2026 |
| Spotify | Impatient Bandits | KDD 2023 |
| Tencent, Match Group / Tinder / Hinge / Bumble, Duolingo, gaming | any retention or engagement attribution | often null — still log |

---

## 5. How a periodic run works

### Folder rule

```
attribution-based-retention/
  read-papers/                  ← parent; never overwrite
  YYYYMMDD_survey/              ← THIS run (primary)
  YYYYMMDD_survey_grok/         ← optional independent parallel; do not merge
```

Write **only** inside the dated folder (and that run's `log.md` / Result summary). Do not edit sibling dated folders or the parent's cards. Do not edit `SURVEY-MANUAL.md` / `PROMPTS.md` unless the standing questions or pipeline changed.

### Pipeline (copy Run 3, not the generic skill's Phase 0 resume)

1. **Create** `YYYYMMDD_survey/` with README (Q1 window filled in), `notebooklm-state.md` pointing at `6a3b8a8e-…`, `queue.md`, `discovery/`, `read-papers/`, `review/`, `log.md`.
2. **Discovery — mechanical first.** Copy `harvest.py`; run OpenAlex + arXiv for the follow list and Q1 topic queries. Do **not** launch four parallel LLM discovery agents (Run 3 they all 429'd). Reserve LLM agents for D3 (Q2 + negative evidence) and D4 (engineering blogs), with a tool-call cap and incremental file writes.
3. **NLM.** Reuse the shared notebook. `source_add(..., wait=False)` then poll. Normalize arXiv `abs/` → `pdf/`. Cap 290 sources before overflow. Concurrent `research_status(task_id=)` is unreliable — fall back to `query=`. Save deep-research reports to `discovery/`; do not expect `research_import` on hit 0.
4. **Blogs.** If `source_add` fails twice, `https://r.jina.ai/<url>`. Record `nlm:failed:…` plus a short card. Do not silently drop.
5. **Cards.** Batches of 3–5. Prefer **2** independent `notebook_query` calls per paper (facts + project relevance), `source_ids` scoped, **no** `conversation_id`. Filenames from `paper-reader`. Target **40–60** new cards. Skip anything already in parent or a prior dated `read-papers/`.
6. **Q2 classification** (required on every Q2 card):
   - **TRUE** — identified per-touch credit of retention/days-active to a specific in-app action (causal or explicit multi-touch decomposition).
   - **PARTIAL** — item/action-level retention scores or surrogate linkage; confounding not identified.
   - **NOT attribution** — RL / LTR / bandit / surrogate **policy** with no per-exposure credit table.
   RLUR, GFN4Retention, AURO, SEC, OCARM, MRet are **not** automatically TRUE.
7. **Review surface.** `review/context/` relevance index + card summaries, each file **< 30 KB**. Four NLM cross-source queries: mechanisms; industry SOTA; last-touch replacement designs; bias devices + evaluation.
8. **Codex draft.** Skill name **`claude-literature-survey-nlm`** (not `claude-literature-survey` — that stalls). Steps only: 3.5-lite tracker, 4-B literature-review, 5 executive-summary. Proof-of-reading required. Adapt `codex-draft-prompt-v3-nlm.txt` to **this** folder's paths.
9. **Independent review** by a *different* model. Raw output in `review/`. Verify numbers against cards before applying fixes. v1 credit must not be called incremental unless a cited paper estimates that exact N7 contrast.
10. **Close.** Fill Result summary in this run's `requirements.md`. Append `log.md`. Update `knowledge_base/projects/attribution_based_retention/log.md` with an `ingest` line. Do **not** rewrite parent `requirements.md` except appending a new Run N result block if the user asks.

### Independence (Prompt B)

The parallel run may use sibling layout as a **process** template. It must **not** read the sibling `executive-summary.md` / `literature-review.md` / `method-tracker.md` until its own three files exist.

---

## 6. After a run finishes

1. Point the user at `YYYYMMDD_survey/executive-summary.md`.
2. Append one `ingest` line to `knowledge_base/projects/attribution_based_retention/log.md`.
3. If Q1/Q2/recommendation **changed**, update the project README “Next Direction” and the postmortem with a new dated supplement — do not silently overwrite the 2026-09-17 record.
4. Refresh the Status line and Q1 window start date in this file.

---

## 7. Anti-patterns (from Run 1 and Run 3)

- Invoking `/literature-survey-nlm attribution-based-retention` and letting Phase 0 “complete” against the parent summary.
- Four parallel LLM discovery agents (session 429). Use `harvest.py`.
- Naming Codex skill `claude-literature-survey` (stalls). Use `claude-literature-survey-nlm`.
- Calling v1 deletion residuals “incremental.”
- Treating GFN/RLUR/MRet as attribution without the TRUE/PARTIAL/NOT test.
- Taking “no dating-company blog” as “no literature” (Run 3 web search missed WeChat IURO; OpenAlex found it).
- Merging primary and `_grok` folders, or writing cards into the parent `read-papers/`.
- Creating a second topic notebook (`ff0bf9af-…` was a mistake; ignore it).
- Duplicating this manual into the knowledge base (the KB file is a pointer only).
