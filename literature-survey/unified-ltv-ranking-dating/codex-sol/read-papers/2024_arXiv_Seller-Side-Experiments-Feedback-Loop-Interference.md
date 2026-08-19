# Paper Analysis: Seller-Side Experiments under Interference Induced by Feedback Loops

**Source:** https://arxiv.org/abs/2401.15811  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** Seller-Side Experiments under Interference Induced by Feedback Loops in Two-Sided Platforms  
**Authors:** Zhihua Zhu; Zheng Cai; Liang Zheng; Nian Si  
**Abstract:** The paper shows that seller-side A/B tests, including counterfactual interleaving, can be biased when pacing feedback makes early exposure alter later rankings.  
**Methodology:** A continuous-time mathematical model links scores, rankings, outcomes, accumulated state, and pacing adjustments. It derives bias under naive and counterfactual-interleaving designs and proposes an empirical interference diagnostic based on within-strategy treatment/control rank comparisons.  
**Main results:** A real advertising experiment reports apparent treatment effects of -23% advertising cost, -27% views, and -21% GMV, with confidence intervals excluding zero; the paper argues feedback-loop interference leads counterfactual interleaving to underestimate the true effect.

## 2. Experiment Critique

**Design:** Theoretical analysis under monotonicity assumptions plus a Tencent marketplace advertising experiment with feedback-controlled pacing.  
**Statistical validity:** Real estimates include confidence intervals: cost [-34%, -12%], views [-38%, -15%], and GMV [-34%, -9%]. The diagnostic establishes inconsistency but does not identify a generally unbiased replacement design.  
**Online experiments:** Yes; real seller-side counterfactual-interleaving experiment.  
**Reproducibility:** Proofs are supplied, but production data and system implementation are proprietary.  
**Overall:** Important warning that sophisticated marketplace experiments can still fail under temporal feedback; direct dating evidence is absent.

## 3. Industry Contribution

**Deployability:** Provides a simple rank-based diagnostic before trusting seller-side experiment results.  
**Problems solved:** Detects hidden bias when exposure consumption, budget, inventory, or cold-start pacing couples test units over time.  
**Engineering cost:** Requires logging both treatment/control counterfactual rankings and pacing state; fixing detected bias needs a redesigned experiment.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First formal treatment of feedback-loop-induced interference in seller-side counterfactual interleaving, backed by production evidence.  
**Prior work comparison:** Challenges counterfactual interleaving and connects it to switchbacks, bipartite/multiple randomization, and feedback-loop experimentation.  
**Verification:** Indexed source only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| Tencent advertising experiment | Not specified in source. | No | Seller-side ranking with pacing feedback. |

**Offline experiment reproducibility:** Theory is inspectable; empirical reproduction is not possible from the source.

## 6. Community Reaction

Not specified in source.

## Survey Card Fields

**Source type:** Industry/academic paper  
**Direction:** D8  
**Problem setting:** Seller/supply-side experiments in two-sided ranked marketplaces with stateful pacing feedback.  
**Objective and label definition:** Estimate treatment effects on seller-side outcomes such as consumption, views, GMV, or retention; labels accumulate over the experimental horizon.  
**Prediction or incrementality:** Causal experiment analysis under interference.  
**Model architecture:** Continuous-time state and ranking model plus counterfactual interleaving experiment design; not a predictive neural model.  
**Credit assignment:** Outcomes are attributed to seller assignment, while the model exposes contamination through rankings and pacing states induced by other assignments and earlier sessions.  
**Training data and counterfactual handling:** Randomized seller groups and dual counterfactual rankings; feedback violates no-interference assumptions.  
**Offline and online evaluation:** Mathematical theorems and a real platform experiment with confidence intervals.  
**Reported gains:** No model gain; documents misleading estimates of -23% cost, -27% views, and -21% GMV under interference.  
**Unverified claims:** General magnitude across domains and an optimal corrected design are not established.

## Project Relevance

**Source-stated facts:** Seller-side retention motivates supply-side tests, and any pacing rule that reacts to accumulated exposure/outcomes can invalidate counterfactual interleaving.

**Survey inference:** Dating candidate exposure, inbox load, popularity caps, and active-pool depletion create analogous feedback. Unified-LTV experiments should log counterfactual ranks/state and prefer designs that randomize time or marketplace clusters when user assignments interact.

**Applicability note:** Core experimental-design caution for reciprocal ranking and congestion controls.  
Use the diagnostic before interpreting seller/candidate-side LTV or retention lift.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## Meta Information

**Authors:** Zhihua Zhu; Zheng Cai; Liang Zheng; Nian Si  
**Affiliations:** Tencent; University of Chicago Booth School of Business  
**Venue:** arXiv  
**Year:** 2024  
**PDF:** Available  
**Relevance:** Core  
**Priority:** 2
