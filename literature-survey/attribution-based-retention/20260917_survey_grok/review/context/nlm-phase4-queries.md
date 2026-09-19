# Phase 4-A queries (this-run sources G1–G25 only)

Notebook: `6a3b8a8e-6f2f-4efe-99eb-283983fc95d9`

## Q1 mechanisms

Across ONLY the scoped sources, list every mechanism that assigns delayed retention, days-active, revisit, conversion, or long-term engagement credit to an individual in-app interaction, item, notification, or ad touchpoint. For each named paper give: (a) full title and company; (b) unit of credit (item / swipe / match / message / ad touch); (c) outcome (N-day return, watch time, purchase, etc.); (d) whether the credit is causal identification, surrogate linkage, RL advantage/flow, or heuristic MTA; (e) whether it produces a reusable per-interaction credit table versus only a ranking/RL policy. Prefer the paper's own wording. Do not invent papers not in these sources. Do not call RL retention optimizers "attribution" unless they publish per-touch credit.

## Q2 industry SOTA

Across ONLY the scoped sources, what is the latest industry-authored attribution system dated 2025-01 to 2026-09? Cover LOTUS (Alibaba), Integrated Marketing Attribution (Lowe's), LinkedIn buyer-journey data-driven attribution, ALM-MTA, and any other production MTA in these sources. For each: company, year, method family (Shapley/Markov/DDA/front-door/LLM-touchpoint), outcome being attributed, whether experiment-calibrated, whether user-level per-touch credit. This is advertising/conversion attribution unless the paper says retention. Do not claim retention attribution unless the paper explicitly attributes retention/days-active to touches.

## Q3 last-touch replacement

A dating platform currently assigns binary N7 (active on day 7 after a reference day) to the user's most recent swipes (last-touch). Using ONLY these sources, describe candidate replacements that map credit onto swipe / match / conversation touchpoints. For each candidate design (removal-effect or Shapley; experiment-calibrated DDA; survival/time-to-event head; surrogate save-revisit; IURO-style per-item retention scores; notification holdback calibration; item-wise future-impact decomposition), name the source paper, the exact credit object it estimates, what would map to swipe vs match vs conversation, and what it does NOT estimate. Flag whether any paper estimates the incremental effect of removing one swipe (or one item) on N7. Do not call a score "incremental" unless the paper estimates that contrast.

## Q4 bias devices and evaluation

Across ONLY these sources, catalog selection-bias / confounding devices and evaluation protocols relevant to attributing a delayed binary retention label to earlier in-app actions. Include always-on holdbacks, interleaving/counterfactual evaluation, experiment-calibrated DDA, front-door identification, sleeping/recovering bandits, and RCT vs observational gaps. For each device: what bias it addresses, what it does not identify, and whether it yields per-interaction credit. List negative evidence from these sources: methods that optimize retention without producing per-touch credit.
