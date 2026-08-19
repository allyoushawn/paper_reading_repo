# Paper Analysis: Off-Policy Evaluation and Learning for Matching Markets

**Source:** https://arxiv.org/abs/2507.13608  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** Off-Policy Evaluation and Learning for Matching Markets  
**Authors:** Yudai Hayashi; Shuhei Goda; Yuta Saito  
**Abstract:** DiPS and DPR are off-policy estimators designed for sparse two-stage matching funnels. They use an intermediate first-side engagement label together with response/match models to improve bias-variance control over DM, IPS, and DR.  
**Methodology:** DiPS importance-weights the first-stage reward and imputes the conditional second-stage response. DPR adds a direct match model as a doubly robust correction; both extend to policy-gradient learning.  
**Main results:** Synthetic experiments and production A/B logs from Wantedly show improved policy-value estimation, selection, and offline learning across configurations. Exact aggregate improvements are not specified in the indexed content.

## 2. Experiment Critique

**Design:** Controlled simulation plus real logs covering 21,736 companies, 17,460 job seekers, and 1.2% match reward prevalence; real A/B outcomes serve as policy-value validation.  
**Statistical validity:** The paper derives estimator bias and variance and evaluates mean squared error and policy-selection ErrorRate. Detailed uncertainty for the production results is not specified in the indexed content.  
**Online experiments:** Uses logs and results from existing production A/B tests; the proposed policies' prospective live deployment is not specified.  
**Reproducibility:** Mathematical estimators are explicit, but Wantedly data are proprietary and code availability is not specified.  
**Overall:** Highly relevant evaluation methodology for reciprocal funnels; practical evidence is limited to job matching and sparse-match value.

## 3. Industry Contribution

**Deployability:** Can screen candidate policies using existing logging-policy data before expensive A/B tests and can furnish offline policy gradients.  
**Problems solved:** Large action spaces, bidirectional sparse rewards, high importance-weight variance, and unreliable policy selection.  
**Engineering cost:** Requires known/estimated logging propensities and calibrated first-stage, conditional-response, and match models.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** New hybrid OPE estimators that exploit matching-market intermediate labels instead of treating the final match as a single sparse reward.  
**Prior work comparison:** Recombines DM, IPS, and DR and extends Switch-DR/MIPS logic to a two-stage reciprocal reward structure.  
**Verification:** Indexed source only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| Synthetic matching data | Not specified in source. | Reconstructable in principle | Ground-truth policy values. |
| Wantedly Visit A/B logs | Not specified in source. | No | 21,736 companies, 17,460 seekers, 1.2% rewards. |

**Offline experiment reproducibility:** Partial for simulation; low for the proprietary real-data validation.

## 6. Community Reaction

Not specified in source.

## Survey Card Fields

**Source type:** Industry/academic paper  
**Direction:** D8  
**Problem setting:** Reciprocal job and dating recommendation with two decisions, huge action spaces, and sparse final matches.  
**Objective and label definition:** Estimate or optimize expected matches; first-stage binary interest and conditional second-stage response multiply into the final match label.  
**Prediction or incrementality:** Off-policy counterfactual policy evaluation and learning, not unit-level uplift prediction.  
**Model architecture:** DiPS and DPR hybrid estimators combining importance ratios with conditional reply and direct match regressions; policy-gradient extensions.  
**Credit assignment:** A recommendation receives credit through a staged company-interest then seeker-response funnel; importance ratios shift from logging to target policy.  
**Training data and counterfactual handling:** Logged bandit data under an old policy, with common-support and propensity assumptions; A/B logs validate estimates.  
**Offline and online evaluation:** Simulation and retrospective production A/B validation using MSE, ErrorRate, and policy learning; no new live deployment reported.  
**Reported gains:** Consistently better evaluation/selection/learning than conventional estimators; exact aggregate numeric gain not specified in source.  
**Unverified claims:** Dating transfer, long-term retention/revenue value, interference handling, and production policy lift are not established.

## Project Relevance

**Source-stated facts:** The formulation explicitly covers dating and decomposes a mutual outcome into an initiator action and recipient response, using logged-policy correction to evaluate new rankers.

**Survey inference:** Dating can reuse DiPS/DPR with like, match, reply, and conversation milestones to reduce variance when final LTV is rare. Extending the terminal reward from match count to delayed LTV requires maturity correction, while cross-user congestion and interference remain outside the estimator.

**Applicability note:** Core reference for offline evaluation of reciprocal ranking policies.  
Generalize the two-stage reward to delayed multi-stage dating value and validate against A/B tests.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## Meta Information

**Authors:** Yudai Hayashi; Shuhei Goda; Yuta Saito  
**Affiliations:** Wantedly; Independent Researcher; Cornell University  
**Venue:** RecSys  
**Year:** 2025  
**PDF:** Available  
**Relevance:** Core  
**Priority:** 2
