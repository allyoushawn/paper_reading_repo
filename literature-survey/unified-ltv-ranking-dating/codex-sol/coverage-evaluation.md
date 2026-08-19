---
model_identifier: codex-sol
date: 2026-08-18
structural_deliverable_coverage: 31/31
source_extraction: 118/120
substantive_evidence_validation: partial
url_validation: 120/120 resolved (94 direct HTTP, 24 browser-public, 2 canonical replacements)
project_context_representation: 8/8
implementation_validation: pending
---

# Coverage Evaluation

## Result

The package has **31/31 structural requirements represented**. This is not a claim of complete evidence validation. Substantive indexed extraction exists for **118/120** selected sources; two selected blog sources have metadata-only failure cards. Several fallback cards contain incomplete fields. URL validation resolved **120/120** selected references: 94 responded directly over HTTP, 24 were verified as public browser-accessible sources, and 2 dead URLs were replaced with canonical primary URLs. See [url-validation.md](url-validation.md).

The eight dating-project constraints are represented in the synthesis, but their proposed definitions, thresholds, causal design, and operating behavior require project-data validation. The package is a strategic proposal, not implementation-ready.

## Corpus gates — structurally represented 13/13

| Requirement | Recorded evidence | Status boundary |
|---|---|---|
| Target 120 selected references | 120 unique selected source IDs/titles | Structurally met |
| Hard floor 45 substantive references | 118 cards have substantive extraction | Extraction floor met |
| At least 60% industry sources | 97/120 selected rows are non-academic categories | Selection-composition fact; not ecosystem prevalence |
| D1 floor | 17 rows including dual-tagged D1/D5 | Structurally met |
| D2 floor | 22 rows | Structurally met |
| D3 floor | 10 rows | Structurally met |
| D4 floor | 11 rows | Structurally met |
| D5 floor | 9 rows including dual-tagged D1/D5 | Structurally met |
| D6 floor | 10 rows | Structurally met |
| D7 floor | 14 rows | Structurally met |
| D8 floor | 22 rows | Structurally met |
| D1–D4 at least 50% | 60/120 = 50.0% | Structurally met |
| URL required per source | 120/120 resolved in `url-validation.md`; 2 canonical replacements applied | Validated |

## Per-source artifacts — structural 3/3; substantive 118/120

| Requirement | Recorded evidence | Status boundary |
|---|---|---|
| One card per selected source | 120 Markdown card files | File presence 120/120 |
| One linked comparison row per source | 120 unique linked rows | Structural presence 120/120 |
| Required card dimensions | All 13 dimensions exist as columns | Schema present; substantive extraction 118/120 and some fallback fields incomplete |

The two metadata-only failures are Pinterest Engineering’s *Multi-task Learning and Calibration for Utility-based Home Feed Ranking* and Meta’s *Instagram Explore Recommender System*. Their substantive evidence status is failed, not inferred from title/metadata.

## Research questions — structurally represented 8/8

Each question has a scoped claim, linked cards, supported scope, and inference caveat in [claim-evidence-table.md](claim-evidence-table.md).

| Question | Structural answer | Evidence status |
|---|---|---|
| Q1 long-term objective | Present | Selected-corpus component evidence; architecture ranking is inference |
| Q2 delayed credit assignment | Present | Source mechanisms; dating attribution remains unresolved |
| Q3 labels/horizons/delay | Present | Source horizons/losses; dating definitions are inference |
| Q4 fusion | Present | Selected fusion mechanisms; no prevalence claim |
| Q5 uplift/incrementality | Present | Source treatment definitions; project causal head is inference |
| Q6 evaluation/interference | Present | Source estimator/design properties plus proposed project protocol |
| Q7 two-sided constraints | Present | Direct/adjacent evidence; long-horizon dating value unvalidated |
| Q8 migration | Present | Component evidence; exact sequence is inference |

## Synthesis deliverables — structural 7/7

| Deliverable | Artifact/section | Status boundary |
|---|---|---|
| All-reference comparison | comparison-table.md | 120 linked rows; not 120/120 evidence-validated |
| Taxonomy plus represented adopters | Review and executive summary | Scoped to selected corpus |
| Three ranked architectures | Review and executive summary | Survey inference |
| Staged migration and gates | Review and executive summary | Operational proposal requiring approval/power |
| Dating labels and horizons | Explicit definitions/losses/maturity | Survey inference requiring data validation |
| Evaluation plan | Pair estimand plus market-cluster design | Identification proposal, not executed validation |
| Gaps and top-10 order | Review and executive summary | Present |

## Project-context representation — 8/8

| Constraint | Structural treatment | Validation status |
|---|---|---|
| Reciprocity | Bilateral outcomes and allocation | Pending project-data validation |
| Congestion | Receiver load/capacity, concentration, spillovers | Pending capacity-model validation |
| Funnel cascade | Like → match → qualified conversation auxiliaries | Pending label audit |
| Low base rates | Entire-space losses, PR diagnostics, staged OPE | Pending power/support analysis |
| Delayed labels | Maturity masks and accounting lags | Pending empirical maturity curves |
| Mixed revenue | Finance-defined subscription + a-la-carte net value | Pending Finance approval |
| Success paradox | Explicit success-exit guardrail; inactivity not success | Pending instrumentation/bias audit |
| Prediction vs incrementality | Separate conditional, pair-causal, and market-policy estimands | Pending randomized identification |

## Outstanding validation

- Repair or re-extract incomplete comparison/card fields if 120/120 substantive evidence is required.
- Obtain product-owner definitions and Trust & Safety/Finance approval for labels, caps, margins, and accounting.
- Power the market-cluster experiment and quantify cross-cluster interactions.
- Validate assignment propensities, overlap, ESS, and CI coverage before causal-head promotion.
- Do not describe the package as implementation-ready or fully evidence-validated.
