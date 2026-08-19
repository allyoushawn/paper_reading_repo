# Paper Analysis: Optimizing Airbnb Search Journey with Multi-task Learning

**Source:** `/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/Multi-task/2023 (Airbnb) (KDD) Optimizing Airbnb Search Journey with Multi-task Learning.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** Optimizing Airbnb Search Journey with Multi-task Learning
**Authors:** Chun How Tan, Austin Chan, Malay Haldar, Jie Tang, Xin Liu, Mustafa Abdool, Huiji Gao, Liwei He, Sanjeev Katariya (Airbnb Inc.)
**Venue/Year:** KDD 2023 (Applied Data Science Track)

**Abstract (paraphrased):** Airbnb guests often spend weeks exploring and comparing listings before making a reservation request, which the host may then reject or cancel. The long, exploratory search journey and the need to balance guest and host preferences pose unique ranking challenges. The paper presents Journey Ranker, a multi-task deep learning architecture that leverages intermediate guest actions (both positive and negative) as milestones to guide the guest toward a successful, uncancelled booking.

**Key contributions:**
1. **Learning both positive and negative milestones** — modeling the whole guest journey (click through uncancelled booking) rather than a single binary label.
2. **Balancing Guest Journey** — a Combination module that learns to weigh positive vs. negative milestone signals in a context-dependent way.
3. **Modular and extensible model architecture** — four decoupled modules (Shared Representation, Base, Twiddler, Combination) that let the framework be reused for other search/decision journeys (e-commerce, real estate, dating sites are explicitly named as analogous use cases) and other business use cases at Airbnb (Experiences ranking, email marketing).

**Methodology:** Journey Ranker consists of:
- **Shared Representation Module:** listing features (F_L) and context features (F_C, i.e. query + guest) are each passed through MLPs to produce listing embedding Emb_L and context embedding Emb_C.
- **Base Module:** decomposes the probability of the final positive milestone (uncancelled booking, `unc`) into a chain of conditional probabilities over six ordered guest milestones — click (c), long click (lc), payment-page view (pp), reservation request (req), host-accepted booking (book), and uncancelled booking (unc): P(unc) = P(unc|book)·P(book|req)·P(req|pp)·P(pp|lc)·P(lc|c)·P(c). Each term is a separate task head (single-layer MLP) trained with a standard learning-to-rank loss (listwise/pairwise), and losses are summed with an empirical normalization weight `w_task` (the empirical fraction of that milestone that eventually converts to `unc`), so rarer/less-predictive milestones are naturally down-weighted and milestones more predictive of the final booking are effectively up-weighted through this data-driven normalization term.
- **Twiddler Module:** three negative-milestone task heads — rejection, cancellation-by-host (cbh), cancellation-by-guest (cbg) — each a binary classification loss, summed.
- **Combination Module:** a *linear* combination of the Base Module output and the Twiddler outputs, y_Combination = y_Base·α_Base + Σ_t y_t·α_t, where each coefficient α is itself learned end-to-end via an MLP conditioned on the context embedding (not a fixed global weight). The module is trained with its own pairwise loss enforcing the ranking `unc > click > impression > cbg/cbh/rejection`. Gradients from the Combination loss are explicitly frozen from flowing back into the Base/Twiddler modules, so the Combination module only learns how to weigh outputs, not to change their semantics.
- Total loss = Loss_Base + Loss_Twiddler + Loss_Combination.
- Training data: search impressions are multi-labeled (click, long click, payment page, request, accepted booking, uncancelled booking) by attributing the eventual booking's label backward across every earlier search impression of that listing in the guest's journey (not just the last search) — see Figure 2's "label attribution" example.

**Main results:** +0.48% offline NDCG over the previous single-task production baseline (uncancelled-booking-only two-tower DNN) with only a +9.2% parameter increase. Online A/B test: +0.61% uncancelled bookers (Stays), +0.14% clicker→booker conversion, +0.48% growth clicker-to-uncancelled-booker. Deployed to four Airbnb products (Stays, Experiences, Online Experiences, and email marketing) with gains ranging from +0.61% to +9.0% uncancelled bookers/nights-booked depending on product maturity.

## 2. Experiment Critique

- **Offline evaluation:** NDCG with binary relevance (uncancelled booking = 1, else 0), five random initializations, 95% confidence intervals reported. Ablations are principled: an ablation study (Table 2) isolates the contribution of quantity of searches, diversity of searches (clickers vs. requesters), and number of intermediate milestones, each shown to independently and statistically-significantly improve NDCG.
- **Online experiments:** A/B tests reported for four separate products with p-values < 0.01 stated for Table 3 (though not shown in the excerpt for the ablation and design-choice experiments beyond CI bands). Deployment claims ("in production for X products") are stated but not externally verifiable.
- **Reproducibility:** Not reproducible outside Airbnb — trained on ~500M internal searches, proprietary Airbnb production features and labels; no public dataset or code release.
- **Negative result reported plainly:** the authors tried established multi-task techniques for negative transfer (gradient interference reduction, adaptive multi-task loss weighting) and found **no statistically significant offline improvement**, hypothesizing this is because their ten tasks are all decompositions of the same underlying preference (uncancelled booking) rather than genuinely competing objectives. They also tested a non-linear combination in the Combination Module and found it performed similarly to the linear version, so they kept the simpler linear form for interpretability — a case of a design choice justified on interpretability rather than raw performance.

## 3. Industry Contribution

- **Deployability:** Explicitly framed as production-proven — deployed to Airbnb Stays ranking plus three other product surfaces (Experiences, Online Experiences, email marketing) with only a +9.2% parameter increase and similar training throughput/serving latency to the prior single-task baseline. This is a strong deployability signal: the architecture change is modular (four separable modules) and reused with minimal customization across product surfaces.
- **Problems solved:** Reformulates a binary "booking vs. not" ranking problem into a full guest-journey milestone model, addressing (a) ignoring searches without a booked listing, (b) treating all non-booked listings as equally negative despite different intermediate engagement, and (c) discarding negative outcomes (host rejections/cancellations) that carry useful signal about host preference.
- **Engineering cost:** Modest — the Base and Twiddler modules add ten shallow, single-layer MLP heads on top of an existing shared representation, so serving latency and training time are comparable to the prior model. The label-attribution scheme (multi-labeling every prior search impression along a guest's journey) roughly doubles the effective training data volume (~+50% more searches used after trading off noise vs. signal), which is a data-engineering cost but not a model-architecture one.
- **Ranking pipeline framing:** This is a main-stage/first-pass ranking model (not a pre-ranker or re-ranker); it replaces the final scoring function for listing ranking directly.

## 4. Novelty vs. Prior Work

The paper explicitly frames its novelty relative to (a) prior single-objective Airbnb search ranking work (booking-only two-tower baseline, and an earlier attempt combining booking + long-click in one model, and a separately-trained multi-model ensemble combined via grid-search weights online — both of which the paper says failed to match Journey Ranker's stability/gains), and (b) prior industry multi-step-conversion multi-task work the Base Module design is explicitly inspired by (Ma et al. 2020's "Entire Space Multi-Task Model" chain-rule-of-probability decomposition for post-click conversion, cited as ref [12] in the paper). The paper's stated novel contributions beyond that base design are: adding the Twiddler Module (negative milestones, not present in prior chain-rule conversion models) and the Combination Module (learned context-dependent balancing of positive vs. negative milestone outputs, with gradient-freezing from Combination back to Base/Twiddler).

## 5. Dataset Availability

| Dataset | Public? | Size | Notes |
|---|---|---|---|
| Airbnb production search logs (Stays) | No — proprietary | ~500M searches (training) | Internal Airbnb data; not released |
| Airbnb Experiences / Online Experiences / email marketing logs | No — proprietary | Not specified in source | Used only for online deployment results, not offline benchmarking |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Optimizing Airbnb Search Journey with Multi-task Learning," Chun How Tan et al., Airbnb Inc., KDD 2023, https://doi.org/10.1145/3580305.3599881 |
| 2 | Source type | Industry paper (KDD Applied Data Science Track) |
| 3 | Direction | D5 |
| 4 | Problem setting | Ranking candidate listings for a guest across a long, multi-session search journey in a two-sided marketplace (guest vs. host), where the final outcome (uncancelled booking) can be rejected or cancelled by either party. |
| 5 | Objective and label definition | Multi-label per search impression across six ordered milestones (click, long click, payment-page view, reservation request, host-accepted booking, uncancelled booking), decomposed via chain rule of conditional probability. The terminal/target label is "uncancelled booking" — the guest's booking must be host-accepted *and* not cancelled by either party before check-in, so the label implicitly waits out a cancellation window; the paper caps a guest journey at a maximum window of K days and attributes the booking label backward to all searches within that window. No explicit multi-day retention or revenue horizon beyond the booking-completion window itself; "Not specified in source" for the exact value of K or how far post-check-in the label is finalized. |
| 6 | **Prediction or incrementality** | Prediction only — the paper does not address incrementality. All six Base Module tasks and three Twiddler tasks are conditional-probability / classification predictions of guest and host actions; there is no counterfactual or treatment-effect estimation. The paper's own Future Work section explicitly flags this as unaddressed, proposing to "modify the Combination Module to directly optimize business OEC... using Future Incremental Value (FIV) estimations" as a next step — confirming incrementality is not yet part of the deployed system. |
| 7 | Model architecture | Four-module deep MTL architecture: Shared Representation Module (MLPs over listing and context features) → Base Module (6 task-specific MLP heads over the shared embeddings, chain-rule decomposition of positive milestones) and Twiddler Module (3 task-specific MLP heads for negative milestones) → Combination Module (context-conditioned linear combination of Base and Twiddler outputs via learned per-task coefficients, gradient-frozen from the upstream modules). |
| 8 | **Credit assignment** | Per-search-impression, but with backward/retrospective attribution: every search impression of the eventually-booked listing across the guest's entire journey (not just the final search) is labeled positive for that listing's booking outcome. This is journey-level credit assignment collapsed onto individual item-level (listing) impressions, distinct from a single-impression or single-slate attribution. |
| 9 | Training data and counterfactual handling | ~500M internal Airbnb searches; multi-labeled per impression using observed guest/host actions (click, long click, payment page, request, accept, uncancelled). No counterfactual correction — labels are observational actions, not adjusted for exposure/selection bias. |
| 10 | Offline and online evaluation | Offline: NDCG with binary relevance (uncancelled booking = 1), 5 random seeds, 95% CI, ablation studies isolating task count and search diversity. Online: A/B tests across four Airbnb product surfaces with reported p-values < 0.01. |
| 11 | Reported gains | +0.48% NDCG (± 0.05% CI) offline vs. baseline on Airbnb Stays ranking (Table 1); online A/B test: +0.61% uncancelled bookers, +0.14% clicker-to-booker conversion (Stays, Table 3); +2.0% bookers (Experiences ranking) and +9.0% bookers (Online Experiences ranking); +0.7% nights booked / −3.7% unsubscribes (email marketing use case). |
| 12 | Applicability to a two-sided dating recommender | Directly the closest structural analogue found in this survey: guest–host reciprocity (host can reject/cancel), a multi-stage funnel (click → long click → payment page → request → accept → uncancelled), and negative outcomes modeled explicitly (host rejection, host/guest cancellation) all map closely onto a dating app's impression → like → match → conversation cascade with reciprocity and match "unravel" (analogous to booking cancellation). However, the terminal label is still an immediate/near-term product completion (booking), not a delayed multi-week retention or revenue signal — the project would need to extend the chain past "uncancelled booking" to a retention/revenue milestone, which this paper does not do. |
| 13 | Unverified claims | Deployment breadth ("deployed to four different Airbnb products with significant business metrics improvements") and magnitude of gains at Experiences/Online Experiences (+2.0%/+9.0%) are self-reported by Airbnb employees with no external verification or public replication data. The claim that negative-transfer mitigation techniques "did not see stat-sig improvement" is reported qualitatively without full numeric detail in the reviewed pages. |

## Project Relevance

Speaks most directly to **Q4** (how short-term event heads are combined — here via a learned, context-dependent linear Combination Module rather than a fixed weight or single value head) and **Q7** (two-sided/reciprocal market: explicit host-side rejection/cancellation as negative milestones, guest-host preference balancing). Also informs **Q2** (credit assignment: retrospective backward labeling of every impression in a guest's journey) and **Q8** (a real staged-migration precedent — Journey Ranker replaced a single-task production baseline and was validated via both offline ablation and online A/B, one milestone at a time). Does **not** address Q1/Q3/Q5 in the sense the project needs (no retention/revenue objective, no delayed-label handling beyond the booking-completion window, no incrementality) — this is the single most structurally relevant paper found in D5 so far for cascade/credit-assignment/two-sided design, but it stops short of the project's long-horizon retention/revenue target.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `JourneyRanker`._

## Meta Information

- **Authors/Affiliations:** Chun How Tan, Austin Chan, Malay Haldar, Jie Tang, Xin Liu, Mustafa Abdool, Huiji Gao, Liwei He, Sanjeev Katariya — all Airbnb Inc.
- **Venue/Year:** KDD 2023 (Applied Data Science Track)
- **Relevance:** Core
- **Priority:** 1
- **NotebookLM source ID:** `nlm:a32f27cc`
