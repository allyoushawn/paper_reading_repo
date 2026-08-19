# Paper Analysis: Facilitating the Search for Partners on Matching Platforms

**Source:** Yash Kanoria (Columbia GSB), Daniela Saban (Stanford GSB). Management Science, 2021 (working-paper version dated Feb 2017). NotebookLM source_id `8166a680-4ba6-4ab6-ab2b-abde364efb23`
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** Facilitating the Search for Partners on Matching Platforms: Restricting Agent Actions
**Authors:** Yash Kanoria, Daniela Saban
**Abstract:**
Two-sided matching platforms (labor, accommodation, dating, ride-hailing) let agents search for partners with idiosyncratic, costly-to-discover match values ("beauty lies in the eye of the beholder"). Unconstrained, decentralized search creates externalities: selective recipients waste proposers' screening effort (negative cross-side externality); imbalanced arrival rates force the "long side" into unselective, low-value blind proposing; and vertical quality differences cause "reacher" agents to wait indefinitely for top-tier partners, ignoring average-quality proposals and sometimes dying unmatched. The paper builds a dynamic, steady-state model of strategic search and proves that simple platform interventions — blocking one side from proposing (directional search) and/or hiding quality-tier information — can substantially raise welfare, including Pareto improvements for the worst-off agents.

**Key contributions:**
- A dynamic (continuous-time, steady-state arrivals/departures) two-sided search model with costly screening and Poisson opportunity clocks, more general than static assortment models.
- Proof that when screening costs differ across sides, blocking the higher-cost side from proposing raises average welfare (14.6% improvement example at α=2, c_e=1/16).
- Proof that in unbalanced markets (long side arrives faster), blocking the long side from proposing raises average welfare (up to 10%) and long-side utility (up to 31%), at a bounded cost (<8%) to the short side.
- Extension to vertical quality differentiation: shows that blocking proposals *and* hiding quality-tier information together achieve a Pareto improvement for the lowest-tier agents without hurting others, in the limit of small screening costs.
- Direct empirical grounding in real dating-platform statistics (Tinder) and real platform design choices (Bumble, TaskRabbit, Airbnb Instant Book).

**Methodology:** Continuum-of-agents dynamic model; agents modeled via Poisson opportunity clocks, MNL-free idiosyncratic Uniform(0,1) match values, costly screening, proposal/acceptance strategies with thresholds; solved for "evolutionarily stable stationary equilibria" (ESSE) under no-intervention and under each proposed platform intervention; welfare compared analytically and via numerical simulation.

**Main results:** See Bibliography Fields — headline numbers include a 14.6% welfare gain from proposal-direction intervention under unequal screening costs, up to 31% worker-utility gain / 10% average-welfare gain in unbalanced markets, and real Tinder statistics (71% of men's / 56% of women's first-contact messages get no reply; 59% of women vs. 9% of men like fewer than 10% of profiles seen; <1% of men's likes match vs. >10% of women's).

---

## 2. Experiment Critique

**Design:** Purely theoretical — a dynamic game-theoretic model solved for equilibria, not an empirical study. No platform ran this as an A/B test in the paper itself; the authors instead cite external empirical findings (Tinder usage statistics from a separate working paper, TaskRabbit's 2014 redesign, Bumble's gender ratio) as motivating/corroborating evidence.

**Statistical validity:** N/A in the classical sense — results are closed-form welfare comparisons and numerical simulations of the equilibrium model, not hypothesis tests on sampled data.

**Online experiments (if any):** None conducted by the authors; TaskRabbit's 2014 bidding→invite redesign is cited as real-world corroboration of a directional-search-style intervention improving match efficiency, but that is external secondhand evidence, not evaluated here.

**Reproducibility:** Full model specification, equilibrium characterization theorems, and closed-form welfare formulas are given; numerical simulation parameters (α=2, λ=2, various c) are specified, so the theoretical results are reproducible from the paper.

**Overall:** Rigorous theory paper with clearly stated assumptions (i.i.d. Uniform(0,1) match values, ex-ante homogeneous agents within a side except in the vertical-tier extension, immediate proposal responses, monopolist platform with no pricing). The authors are explicit that these simplifications are for tractability and discuss expected robustness (e.g., response delays would likely amplify the benefit of their interventions, not undermine it).

---

## 3. Industry Contribution

**Deployability:** Directly deployable as market-design policy levers, not as an ML model — "block one side from proposing" (à la Bumble) and "hide desirability/quality signals" (the paper explicitly compares this to Tinder's internal, never-publicly-revealed Elo-style rating) are both product/policy decisions rather than infrastructure builds.

**Problems solved:** Precisely the project's core problem — wasted likes/screening effort from skewed desirability, "reacher" agents (over-selective users chasing top-tier partners) causing churn ("dying unmatched"), and the resulting low conversion rate for average users.

**Engineering cost:** Low relative to most ranking/ML interventions — implementing directional search or hiding a popularity/desirability signal is largely a product/policy change, not a new model architecture; the harder part is knowing *when* (which regime of screening cost / arrival imbalance) each lever pays off, which requires estimating the underlying market parameters (screening costs, arrival imbalance, quality dispersion).

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First dynamic (steady-state arrivals/departures) model of two-sided platform search with costly screening that derives *specific, implementable* platform interventions (directional search, information hiding) with provable welfare guarantees, including a Pareto improvement result under vertical differentiation — extending static/synchronous congestion models (Arnosti, Johari & Kanoria 2014) and search-restriction literature (Halaburda, Piskorski & Yıldırım 2017) to a dynamic flow setting.

**Prior work comparison (top cited works per source):**
1. Gale & Shapley (1962), "College admissions and the stability of marriage" — foundational stable-matching theory.
2. Roth (1982); Roth & Peranson (1999) — matching market design under capacity constraints (residency match).
3. Pissarides (2000), "Equilibrium unemployment theory" — benchmark search-friction macro model.
4. Rochet & Tirole (2003), "Platform competition in two-sided markets" — cross-side externalities framework.
5. Hopenhayn (1992), "Entry, exit, and firm dynamics in long run equilibrium" — stationary equilibrium concept source.
6. Weintraub, Benkard & Van Roy (2008), "Markov perfect industry dynamics with many firms" — mean-field equilibrium formulation.
7. Fradkin (2015), "Search frictions and the design of online marketplaces" — empirical search-friction evidence (Airbnb).

**Verification:** Novelty claim holds up — the paper is explicit about its relationship to prior congestion-management work (Arnosti et al., Halaburda et al., Kanoria & Saban's own earlier line) and states it "complements this line of work by considering a stylized static model while allowing for more agent heterogeneity and using the assortment shown to each user as a design lever" relative to the companion Assortment Planning paper (Ashlagi et al.) also in this notebook — the two papers are explicitly cross-referenced and complementary (proposal-restriction/information levers here vs. menu/assortment-size levers there).

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| No primary dataset — theoretical model + numerical simulation | — | N/A | Model parameters fully specified for reproducibility |
| Tinder usage statistics (cited from Tyson, Perta, Haddadi & Seto, "A first look at user activity on Tinder," 2016) | — | External working paper, not directly accessible here | Used as motivating empirical corroboration only |

**Offline experiment reproducibility:** The theoretical/simulation results are fully reproducible from the paper; the cited Tinder statistics are secondhand from an external source not verified independently in this analysis.

---

## 6. Community Reaction

Not assessed for this source (out of scope for Phase 3 batch processing).

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Yash Kanoria, Daniela Saban
**Affiliations:** Columbia Business School; Stanford Graduate School of Business
**Venue:** Management Science, 2021
**Year:** 2021
**PDF:** Not fetched directly — analyzed via NotebookLM source
**Relevance:** Core — directly addresses market-design levers and reciprocal-search dynamics for the project's exact problem, with explicit dating-platform (Tinder, Bumble) grounding
**Priority:** 1

---

## Bibliography Fields

- **title:** Facilitating the Search for Partners on Matching Platforms: Restricting Agent Actions
- **authors or organization:** Yash Kanoria (Columbia GSB), Daniela Saban (Stanford GSB)
- **year:** 2021 (working paper version 2017)
- **venue or type:** Management Science (journal)
- **link:** Not directly retrieved from source (Management Science 2021; earlier working-paper versions circulated from 2017)
- **tier tag:** Tier 2 — Applied research / field-grounded theory on real matching and dating platforms
- **what they did (≤80 words):** Built a dynamic steady-state model of two-sided platform search with costly screening and idiosyncratic match values, then proved that simple platform interventions — blocking the more-selective or longer/faster-arriving side from proposing first, and hiding desirability/quality-tier information from the other side — raise average welfare and can produce Pareto improvements for the worst-off agents, grounding the analysis directly in real Tinder, Bumble, and TaskRabbit data and design choices.
- **mechanism relevant to two-sided balancing (≤50 words):** Directional-search and information-hiding market-design levers that prevent "reacher" agents from wastefully waiting for top-tier partners while ignoring average proposals, and prevent the long/high-desirability side from being flooded with low-value blind proposals — directly reducing "wasted likes" and churn from unmatched over-selective users.
- **metrics used, and the reported effect:** Average steady-state welfare, per-side (worker/employer) utility, and churn ("dying unmatched") rate. Reported effects: 14.6% average-welfare gain (unequal screening costs, α=2); up to 31% long-side utility gain and 10% average-welfare gain in unbalanced markets (<8% short-side loss); Pareto-improving welfare gain for bottom-tier agents under vertical differentiation with hidden quality + blocked proposals. Cited real Tinder stats: 71%/56% (men/women) of first messages unanswered; 59% of women vs. 9% of men like <10% of profiles seen; <1% of men's likes match vs. >10% of women's.
- **fit for a dating app:** high — the paper explicitly analyzes dating platforms (Tinder, Bumble, OkCupid) as primary examples throughout, cites real dating-platform statistics that mirror the project's stated desirability-skew and wasted-likes problem almost verbatim, and derives concrete, low-engineering-cost market-design levers (directional search, hiding popularity signals) directly actionable for the project.
- **confidence that the item is real and described correctly:** high (NotebookLM grounded answer with extensive direct quotes, explicit equations, a full related-work bibliography matching known real citations, and verbatim Tinder/Bumble/TaskRabbit references; source_id validated across all three independent queries).

---

## Project Relevance

This is very likely the single most directly relevant source found in this batch, and among the most relevant in the survey to date. The paper's motivating statistics are essentially a direct empirical description of the project's stated problem: on Tinder, 59% of women (vs. 9% of men) like fewer than 10% of the profiles they see, and fewer than 1% of men's likes result in a match versus over 10% of women's — the exact "desirability skew absorbs most likes and cannot reply to all of them" dynamic the project's north star describes, down to the specific mechanism (the paper's "reacher" employers who ignore average proposals while waiting for a top-tier match, some of whom "die" — i.e., churn — unmatched, exactly mirroring the project's "senders lose trust because their likes never become conversations" framing). The paper's core deliverable is a set of **market-design levers** (Layer 3 in the project taxonomy) rather than a ranking model: (1) directional search — forcing the side more likely to be flooded with low-value proposals (mapped to over-subscribed/high-desirability users) to instead be the receiving side, which the paper explicitly ties to Bumble's women-message-first design and notes empirically correlates with a healthier (near 50/50) gender balance than competitor platforms; (2) hiding quality/popularity information, which the paper explicitly compares to Tinder's internal, never-publicly-revealed Elo-style desirability score — directly actionable as "don't expose like-counts or desirability signals to users" for the project. The paper is also directly complementary to the companion Assortment Planning source in this same notebook (`2022_OperationsResearch_NA_Assortment-Planning-Two-Sided-Sequential-Matching.md`): that paper controls *how many and which* suppliers appear in a menu (an exposure-allocation lever), while this paper controls *who is allowed to initiate* and *what information is visible* (proposal-direction and information-design levers) — together they cover Layers 2 and 3 of the project's four-layer framing. One limitation for direct adoption: the model assumes ex-ante homogeneous agents within a side (except in the two-tier vertical-differentiation extension), so translating its thresholds into a fully personalized reciprocal-scoring system (Layer 1) would require further work, and the model does not address online-experimentation design under interference (Layer 4) at all.
