# Paper Analysis: Towards a Fair Marketplace — Trade-off between Relevance, Fairness & Satisfaction in RecSys

**Source:** Spotify Research Blog, published 22 Oct 2018, authors Rishabh Mehrotra, James McInerney, Hugues Bouchard, Mounia Lalmas, Fernando Diaz (https://research.atspotify.com — blog recap of the CIKM 2018 paper)
**Date analyzed:** 2026-08-16

**Note on redundancy:** This source is the Spotify Research blog write-up of the same underlying work already covered in `2018_CIKM_NA_Towards-Fair-Marketplace-Counterfactual-Evaluation.md` (Mehrotra et al., CIKM 2018). Per the batch manifest this is a secondary/redundant source; this file is kept brief and defers to the CIKM file for the primary analysis.

---

## 1. Summary

**Title:** Towards a Fair Marketplace: Trade-off between Relevance, Fairness & Satisfaction in RecSys
**Authors:** Rishabh Mehrotra, James McInerney, Hugues Bouchard, Mounia Lalmas, Fernando Diaz (Spotify)
**Abstract:**
Blog-form summary of Spotify's research on two-sided marketplace recommendation, addressing "superstar economics" (a small set of popular artists absorb most exposure) via a joint relevance/fairness/satisfaction optimization framework, group-fairness metric, and user-affinity-aware adaptive policies, evaluated with offline counterfactual estimation.

**Key contributions:**
- Group fairness metric (ψ) rewarding recommended sets diverse across artist popularity bins.
- Seven recommendation policy variants (global interpolated/probabilistic/guaranteed-relevance, plus two user-affinity-adaptive policies) trading off relevance vs. fairness via a parameter β.
- Adaptive (user-affinity-aware) policies personalize the trade-off per user rather than applying a global fairness weight.
- Advocates counterfactual offline evaluation over live A/B tests for measuring user satisfaction under different fairness policies.

**Methodology:** Same as the CIKM 2018 paper — see that file for full method detail. This blog condenses the same policy definitions and evaluation.

**Main results:** Adaptive (user-affinity) policy achieves best trade-off: 9–21% satisfaction gain with only 15–17% fairness loss, vs. 42–64% fairness loss for the global interpolated policy; pure-fairness focus costs 35% relative satisfaction vs. pure-relevance.

---

## 2. Experiment Critique

Not re-analyzed in detail here — identical experimental design (offline counterfactual evaluation on Spotify listening logs, β-parameterized policy family) to the CIKM 2018 paper. See `2018_CIKM_NA_Towards-Fair-Marketplace-Counterfactual-Evaluation.md` for the full critique.

---

## 3. Industry Contribution

Same as CIKM 2018 paper — a deployed-at-Spotify-scale framework for balancing consumer relevance and supplier exposure fairness via a tunable, user-adaptive recommendation policy.

---

## 4. Novelty vs. Prior Work

Not specified in source — per NotebookLM, this blog post (unlike the peer-reviewed paper) contains no related-work section or academic bibliography.

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Spotify internal listening/streaming logs | N/A | No | Internal production data |

**Offline experiment reproducibility:** Not reproducible — internal data only.

---

## 6. Community Reaction

No significant community discussion found (not investigated as part of this NotebookLM-based extraction).

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Rishabh Mehrotra, James McInerney, Hugues Bouchard, Mounia Lalmas, Fernando Diaz
**Affiliations:** Spotify
**Venue:** Spotify Research Blog (recap of CIKM 2018 paper)
**Year:** 2018
**PDF:** Not available — web article, accessed via NotebookLM source
**Relevance:** Related (redundant with existing CIKM 2018 file)
**Priority:** 2

---

## Bibliography Fields

- **title:** Towards a Fair Marketplace: Trade-off between Relevance, Fairness & Satisfaction in RecSys
- **authors or organization:** Rishabh Mehrotra, James McInerney, Hugues Bouchard, Mounia Lalmas, Fernando Diaz; Spotify
- **year:** 2018
- **venue or type:** Spotify Research Blog (recap of CIKM 2018 paper)
- **link:** https://research.atspotify.com (Towards a Fair Marketplace: Trade-off between Relevance, Fairness & Satisfaction in RecSys)
- **tier tag:** Tier 1 — Adjacent marketplace (music streaming) — secondary/redundant source

**what they did (≤80 words):** Spotify researchers address "superstar economics" (a small set of popular artists absorbing most listener attention) with a joint relevance/fairness/satisfaction optimization framework: a group-fairness metric over artist popularity bins, seven recommendation policies trading off relevance vs. fairness via parameter β, and user-affinity-aware adaptive policies that personalize the trade-off per listener, evaluated via offline counterfactual estimation on Spotify listening logs. Same underlying work as the CIKM 2018 paper already in this repo.

**mechanism relevant to two-sided balancing (≤50 words):** Per NotebookLM, exposure redistribution away from over-subscribed ("superstar") suppliers is directly addressed via the group-fairness metric and user-affinity adaptive policies. However, reciprocal/mutual-interest scoring and per-user reply-capacity limits are not addressed — the consumption model assumes infinite-capacity suppliers (a song can be streamed by unlimited listeners).

**metrics used, and the reported effect:** Group fairness (ψ) across popularity bins; user satisfaction (tracks listened). Adaptive policy: 9–21% satisfaction gain with 15–17% fairness loss vs. 42–64% fairness loss for global interpolated policy; pure-fairness-only focus costs 35% relative satisfaction vs. pure-relevance.

**fit for a dating app:** medium — reason: per NotebookLM, the exposure-redistribution mechanism (group fairness + user-affinity-adaptive policy) is a directly transferable pattern for de-concentrating attention from over-subscribed profiles, but the underlying model assumes infinite-capacity suppliers and has no reciprocal-consent or reply-capacity mechanism, both central to the dating-match problem — and this source duplicates the already-indexed CIKM 2018 paper.

**confidence that the item is real and described correctly:** high — all three NotebookLM queries returned `sources_used` matching this source_id, with detailed, internally consistent content matching the known CIKM 2018 paper (same authors, same β-policy framework, same metrics).

---

## Project Relevance

Per NotebookLM's direct answer, this source's mechanism addresses the project's exposure-allocation layer but not its reciprocal-scoring or capacity layers. It directly tackles "superstar economics" — the same over-subscription phenomenon the project's north star describes — via a group-fairness metric (ψ) that rewards recommendation sets diverse across supplier popularity bins, and user-affinity-adaptive policies that redistribute exposure to under-exposed suppliers selectively (only for users with affinity toward diverse content), achieving 9–21% satisfaction gains with only 15–17% fairness loss versus 42–64% loss for a naive global policy. This is a transferable exposure-redistribution technique. However, NotebookLM confirms three concrete gaps versus the project's needs: (1) no reciprocal or mutual-interest scoring — the marketplace is strictly unilateral consumption (listener → artist), not bilateral consent; (2) no per-supplier capacity or reply-capacity limit — the model assumes infinite-capacity suppliers (a track can be streamed without limit), unlike a person's finite reply bandwidth; (3) no interference-aware evaluation — the offline counterfactual framework ignores that one user's consumption doesn't deplete a shared resource, so it would overestimate outcomes if applied naively to a capacity-constrained dating market. As this is a secondary/redundant source for the same paper as `2018_CIKM_NA_Towards-Fair-Marketplace-Counterfactual-Evaluation.md`, treat that file as primary for citation purposes; this file exists only because it has its own source_id in the survey's source list.
