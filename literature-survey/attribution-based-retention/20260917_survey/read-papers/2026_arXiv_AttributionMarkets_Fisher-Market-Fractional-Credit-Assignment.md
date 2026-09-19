
# Attribution Markets: A Fisher-Market Formulation for Fractional Credit Assignment Between Planned Tasks and Performed Actions

**Source:** https://arxiv.org/pdf/2607.20694.pdf | **NLM source id:** 98e96997-d361-431a-8573-119c026f8604 | **Year / venue:** arXiv 2607.20694 | **Authors / affiliation:** Salavat Ishbulatov — Independent researcher (doplan.ai) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Personal/organizational planning systems keep two drifting records — planned tasks (effort budgets) and performed actions (logged durations) — bridged today by an exclusive, all-or-nothing link (an action is 100% credited to one task or 0%), which strands genuinely related but unlinked effort and creates false-stall reports. The paper formulates the bridge as a **quasi-linear Fisher market**: tasks are budget-constrained buyers, logged actions are divisible goods, and a fused text/structural/temporal signal sets each buyer's valuation. **Unit of credit:** fractional share of a performed action's duration allocated to a task (via a share matrix W). **Outcome attributed:** task progress/completion (not retention). **Bias/over-crediting handling:** two market instruments — a seller reserve price ρ and a buyer cash option u₀ — yield three theorems: Conservation (no hour credited twice), a Hard Budget Cap (a task can't receive more credit than its planned budget), and a provable Junk Filter (affinity below a threshold gets exactly zero credit, not a diffuse near-zero share). A concave completion-utility extension discounts progress as a task nears its planned budget; a one-parameter entropy-regularized generalization unifies the sharp market solution with smoothed optimal-transport (Sinkhorn) allocation, with regularization strength selected from estimated affinity-noise level.

## 2. Evidence
- **Setup:** purely synthetic/theoretical evaluation — random and adversarial instances at "personal-planner scale"; no production deployment or online experiment.
- **Compared rules:** softmax, entropy-regularized optimal transport (Sinkhorn), hard (exclusive) assignment, and the proposed market.
- **Key result (share sparsity):** softmax and Sinkhorn are dense (≈0 sparsity — every task gets a nonzero sliver of every action); hard assignment is sparse (≈0.9) but not fractional; the market is the only rule that is both fractional and sparse (≈0.85), i.e., it alone can report an exact zero credit rather than a diffuse noise value.
- **De-circularized, multi-seed noise benchmark:** the market's sharp, zero-entropy equilibrium is *more* sensitive to affinity noise than entropy-regularized OT's permanently smoothed one — the paper's own headline weak spot, resolved via the entropy-regularized generalization.
- **Convergence:** the satiation-threshold fixed point (for the completion-utility extension) is proven to exist (Brouwer) and be locally unique under an explicit diagonal-dominance condition; convergence failed in 1 of 10 adversarial instances, so a deployment should monitor the residual and fall back to the linear market if it doesn't shrink.

## 3. Limitations
- Convergence for the completion-seeking extension is only conditional; the sufficient condition (diagonal dominance) can fail and did in 1/10 adversarial instances.
- The market can still over-credit genuinely close/adjacent tasks beyond what a stricter causal notion would allow.
- The mean-variance extension only solves the per-task subproblem, leaving the joint equilibrium an open variational-inequality question.
- Evaluation is entirely synthetic and confined to personal-planner scale; validation at deployment/organizational scale and against real user corrections is explicitly left as future work.
- The general-τ entropy-regularized case has no efficient tuned algorithm yet (an "obvious" alternating-scaling scheme is left as future work).

## 4. Prior works named
- Eisenberg & Gale — the classical Fisher market, repurposed here for attribution.
- Minsky — origin of the general credit-assignment problem.
- Reinforcement learning temporal credit assignment literature (cited generically).
- Early data-driven multi-touch attribution: bagged logistic regression and Markov-chain removal-effect models.
- Causal MTA literature — reweighting journeys to remove confounding before attributing credit.

## 5. Project Relevance
- **Answers:** Q1 (a 2026 fractional-credit-assignment mechanism related to, and explicitly positioned against, MTA).
- **Attributes retention to individual interactions?** Partly — it is a general-purpose fractional credit-assignment framework (explicitly framed via MTA) applied to task/action effort logs, not to user retention/engagement.
- **Transferable components:** Fisher-market equilibrium with hard budget caps and a provable junk filter (exact zero credit for low-affinity swipes, rather than diffuse fractional noise across the whole swipe history); multi-signal log-odds affinity fusion (text + structural link + temporal decay) directly analogous to fusing profile-similarity, match, and recency signals per swipe; noise-adaptive entropy regularization for robustness.
- **Required changes:** re-frame task "hour budgets" as user attention capacity or retention-value budgets (candidate profiles have no natural hour budget); replace logged action duration with heterogeneous, non-duration interaction types (swipe/like/match/message); replace one-off task-completion progress with a daily-recurring N7 retention target.
- **On last-touch:** explicitly critiques the standard exclusive all-or-nothing linking rule (functionally last-touch/single-link attribution) for making genuinely related, unlinked effort invisible and reporting false stalls; separately notes MTA supplies fractional-credit framing but lacks a budget/price mechanism to prevent over-crediting.
- **Transfer rating:** adaptable — the budget-capped, junk-filtered market mechanism is a strong candidate for turning the current uncapped/last-touch credit rule into a bounded, sparse fractional-credit scheme, but the domain objects (budgets, goods, outcome) all need re-mapping from task-planning to retention.
