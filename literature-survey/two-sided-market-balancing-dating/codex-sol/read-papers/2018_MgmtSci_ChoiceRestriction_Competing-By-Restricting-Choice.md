# Paper Analysis: Competing by Restricting Choice: The Case of Matching Platforms

**Source:** https://questromworld.bu.edu/platformstrategy/wp-content/uploads/sites/49/2017/06/PlatStrat_2017_paper_46-1.pdf  
**Date analyzed:** 2026-08-19

---

## 1. Summary

**Title:** Competing by Restricting Choice: The Case of Matching Platforms  
**Authors:** Hanna Halaburda, Mikołaj Jan Piskorski, Pınar Yıldırım  
**Abstract:** A matching platform can benefit users by showing more candidates, but every extra option also gives those candidates more alternatives and raises rejection risk. A stylized two-sided dating model shows that network effects can turn negative as choice grows and that restricted- and unrestricted-choice platforms can coexist through self-selection by users with different outside options.

**Key contributions:**

- Microfounds a choice effect and an opposing same-side competition effect.
- Proves that the utility-maximizing menu size varies with a user's outside option or patience.
- Shows how a higher-priced restricted-choice platform can coexist with a cheaper open platform.

**Methodology:** A two-stage heterosexual matching game gives each user `N` candidates, permits at most one final offer, and forms a match only when offers are reciprocal. Preferences are subjective and users differ in the utility of remaining unmatched. The paper derives rejection and expected-utility functions, analyzes monopoly and duopoly platform equilibria, and numerically tests partially correlated preferences.

**Main results:** Under independent preferences, rejection probability is `N/(N+1)`. Simulations show low-outside-option users can peak at only two candidates, while more selective users prefer larger menus. The motivating descriptive fact is that eHarmony charged about 25% more than Match.com while restricting access.

## 2. Experiment Critique

**Design:** Analytical proofs and numerical simulations compare restricted choice, unrestricted choice, a free outside market, and duopoly platforms. There is no causal or observational platform evaluation.

**Statistical validity:** Formal equilibrium claims are proven. The empirical 25% price difference is descriptive; significance tests, confidence intervals, effect sizes from real outcomes, and power calculations are not specified in source.

**Online experiments:** Not specified in source.

**Reproducibility:** Equations and simulation assumptions are provided, including preference-correlation values from 0 to 0.8. Code and a replication package are not specified in source.

**Overall:** The model cleanly isolates competition externalities, but its static simultaneous play, symmetric menu sizes, single-homing, and mostly horizontal preferences limit direct behavioral validity.

## 3. Industry Contribution

**Deployability:** A daily candidate cap or curated batch is straightforward to ship and test.

**Problems solved:** Excessive same-side competition, high rejection rates, wasted likes, and low match probability among motivated users.

**Engineering cost:** Low for a global cap; moderate for segment-specific menu sizes, outside-option estimation, and interference-aware experimentation.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** It derives non-monotone network effects from matching microfoundations and explains why restricting choice can support a premium competing platform.

**Prior work comparison:** Rochet and Tirole (2003) and Katz and Shapiro (1985, 1994) largely assume positive network effects; Damiano and Li (2007) study pricing and matching but not varying menu size; Ellison and Fudenberg (2003) and Ellison, Fudenberg, and Mobius (2004) study coexistence and tipping; Brandenburger and Nalebuff (1996) frame complement/substitute roles; Casadesus-Masanell and Halaburda (2014) study limiting choice without same-side competition.

**Verification:** The source supports the stated mechanism and comparisons. Publication metadata follows the verified survey queue; the queried PDF is a March 2017 working version.

## 5. Dataset Availability

**Datasets mentioned:**

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Numerical preference simulations | Not applicable | Reconstructable | Correlation parameter `h` tested from 0 to 0.8. |
| eHarmony/Match.com descriptive comparison | Not specified | No | Motivation only; not an evaluation dataset. |

**Offline experiment reproducibility:** The model is reconstructable from the paper, but code and raw simulation outputs are not specified in source.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Exact mechanism:** Symmetrically limit each side's candidate menu. Smaller menus reduce the number of alternatives held by a target and therefore reduce same-side competition and rejection. A higher price can further select for users with low outside options and high willingness to match.

**Metrics and reported effect:** Rejection probability is `N/(N+1)` under independent preferences. In simulations, a user with outside option 0.4 peaks near two candidates; a user with outside option 0.6 peaks near three. Conversations, retention, match Gini, and real match lift are not specified.

**Capacity/congestion relevance:** The model permits one final offer, with an appendix allowing a fixed number of tentative offers. This is a courtship-capacity constraint; it does not model dynamic inbox load or per-recipient exposure allocation.

**Practical mapping:** `N` maps to daily candidate batches or profile-stack limits, an offer maps to a like, and reciprocation maps to a mutual match. Real deployment needs asymmetric capacities, correlated desirability, asynchronous behavior, and soft conversation limits.

**Dating fit: High.** The model is built for reciprocal online dating and directly identifies choice restriction as a congestion lever, though evidence is theoretical.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| [2021_MS_NA_Facilitating-Search-for-Partners.md](./2021_MS_NA_Facilitating-Search-for-Partners.md) | Novelty vs. Prior Work — Comparison | Contrasts Halaburda, Piskorski, and Yildirim's static restricted-choice game with this dynamic search model. |
| [2022_OR_NA_Assortment-Two-Sided-Sequential-Matching.md](./2022_OR_NA_Assortment-Two-Sided-Sequential-Matching.md) | Novelty vs. Prior Work — Comparison | Cites Halaburda et al. as studying limiting choice, then contrasts this paper's pre-choice menus. |
| [2024_MarketingScience_SequentialSearch_Effects-Market-Size-Competition.md](./2024_MarketingScience_SequentialSearch_Effects-Market-Size-Competition.md) | Novelty vs. Prior Work — Background | Cites Halaburda, Piskorski, and Yıldırım (2018) on choice-versus-competition effects. |
| [2026_arXiv_ECDA_Predictive-Models-Two-Sided-Recommendations.md](./2026_arXiv_ECDA_Predictive-Models-Two-Sided-Recommendations.md) | Novelty vs. Prior Work — Background | Cites Halaburda et al. (2018) as restricting choice. |

## Meta Information

**Authors:** Hanna Halaburda, Mikołaj Jan Piskorski, Pınar Yıldırım  
**Affiliations:** Bank of Canada and NYU; IMD; Wharton School  
**Venue:** Management Science  
**Year:** 2018  
**PDF:** available  
**Relevance:** Core  
**Priority:** 2

## Annotated Bibliography Fields

- **Title:** Competing by Restricting Choice: The Case of Matching Platforms
- **Authors/organization:** Hanna Halaburda, Mikołaj Jan Piskorski, Pınar Yıldırım; Bank of Canada/NYU, IMD, Wharton
- **Year:** 2018
- **Venue/type:** Management Science; analytical matching-platform paper
- **Link:** https://questromworld.bu.edu/platformstrategy/wp-content/uploads/sites/49/2017/06/PlatStrat_2017_paper_46-1.pdf
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Built a two-stage reciprocal dating model in which each user sees `N` candidates and can make one offer. The authors derive how more choice improves conditional match quality but increases rejection through same-side competition, then characterize user self-selection and platform competition. Numerical simulations test robustness when preferences contain vertical correlation.
- **Mechanism relevant to two-sided balancing (≤50 words):** Restrict candidate menus on both sides so each target has fewer competing offers. This lowers rejection and can attract motivated users, creating a curated submarket with higher match probability despite less choice.
- **Metrics and reported effect:** Rejection probability `N/(N+1)`; simulated expected utility peaks at small menu sizes for low-outside-option users. eHarmony's price was about 25% above Match.com's. Real match, conversation, and retention effects are not specified.
- **Dating-app fit:** High — a daily batch or swipe-stack cap directly implements the model's market-design lever, but causal product evidence is absent.
- **Confidence:** High on source-scoped theory; medium-high on venue/year because the queried file is a 2017 working version of the 2018 publication.
