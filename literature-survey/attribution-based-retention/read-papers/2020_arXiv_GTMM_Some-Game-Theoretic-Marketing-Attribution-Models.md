# Paper Analysis: Some game theoretic marketing attribution models

**Source:** https://arxiv.org/pdf/2012.00812.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Some game theoretic marketing attribution models  
**Authors:** Elisenda Molina, Juan Tejada, Tom Weiss (UC3M, UCM, Deductive Inc.)  
**Abstract:** Formalizes marketing channel attribution as benefit allocation on conversion paths using cooperative TU games (extended sum game + Shapley value) and as bankruptcy problems (PROP and CEL rules), with extensions for channel repetition and positional order via fictitious players.

**Key contributions:**
- Shapley-value attribution on sum games when order and/or repetition of channels on paths matter.
- Bankruptcy formulation where total claims exceed campaign estate; PROP vs CEL rules (CEL excludes weak channels).
- Axiomatic characterization (efficiency, symmetry, monotonicity in repetition, etc.) on toy numeric examples.

**Methodology:** KPI function \(f\) maps paths/combinations to nonnegative benefit; sum-game characteristic function aggregates subset KPIs; Shapley closed form \(\phi_i=\sum_{S\ni i} f(S)/|S|\) in base case; repetition uses replicated fictitious players; order uses extended players \(ij\) for channel \(i\) at position \(j\); bankruptcy maps claims \(c_i=\sum_{S\ni i} f(S)\) to estate \(F=\sum_S f(S)\).

**Main results:** Theoretical propositions and small numerical tables (Examples 1–5) showing CEL vs PROP behavior, decomposition with order players, and failure modes (CEL may not decompose additively across positions).

---

## 2. Experiment Critique

**Design:** No empirical datasets; axioms and toy campaigns with 2–3 channels.

**Statistical validity:** N/A for prediction; proofs and example-driven intuition.

**Online experiments (if any):** Not specified in source.

**Reproducibility:** Fully specified math; no code artifact referenced in extracted material.

**Overall:** Clean axiomatic layer for path-aware Shapley and bankruptcy rules; no calibration to logged ad data in this source.

---

## 3. Industry Contribution

**Deployability:** Low direct deployment—requires reliable KPI \(f\) per path or combination and assumes KPI already defined.

**Problems solved:** Incentive-aligned splitting of credit under repetition/order sensitivity and deficit-style over-claiming across channels.

**Engineering cost:** Moderate if \(f\) is precomputed from logs; exponential substructures avoided by moving to bankruptcy rules for large \(n\).

---

## 4. Novelty vs. Prior Work

Extends Morales (2016), Zhao et al. (2018), Cano-Berlanga et al. on sum games; cites Dalessandro et al. (2012) as early cooperative-game attribution; contrasts deterministic KPI-based approach vs probabilistic Markov/Shapley lines (e.g., Singal et al. 2019).

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Toy examples only | N/A | N/A | Synthetic KPI tables in paper |

**Offline experiment reproducibility:** Not specified in source.

---

## 6. Community Reaction

Not specified in source.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** Elisenda Molina; Juan Tejada; Tom Weiss  
**Affiliations:** Universidad Carlos III de Madrid; Universidad Complutense de Madrid; Deductive Inc.  
**Venue:** arXiv (cs.GT / econ)  
**Year:** 2020  
**PDF:** https://arxiv.org/pdf/2012.00812.pdf  
**Relevance:** Core  
**Priority:** 2

---

## Project Relevance

**(A)** The framework allocates nonnegative **channel-level** credit from path KPIs; fictitious players yield position- or repetition-specific Shapley components, but the paper does **not** frame outputs as supervised training labels for a downstream ranker.

**(B)** KPI \(f\) is nonnegative on paths and can represent a wide benefit notion; **continuous engagement such as user-days-active is not specified in source.**

**(C)** Not specified in source.
