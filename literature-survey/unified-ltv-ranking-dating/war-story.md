# War Story — How the Unified Retention/Revenue Ranking Survey Got Here

**Date:** 2026-08-20
**Scope:** Survey 3, `unified-ltv-ranking-dating`, read across all three model workplaces — `claude_opus/`, `codex-sol/`, `cursor-grok/` — plus the shared root and the project knowledge base.
**Purpose:** A narrative history of this line of work. It records what we believed, what we did, what the evidence showed, and what we changed. Read it to build a mental model. Do not read it to look up a result.

> **Sourcing note.** The field chronology and every "builds on" arrow were checked against the NotebookLM notebook `unified-ltv-ranking-dating` (ID `67046a44-…`), queried 2026-08-20. Project dates come from the `log.md` files in this folder and in `knowledge_base/projects/attribution_based_retention/`. The check corrected two claims, resolved one apparent contradiction, and left one unresolved. Each carries a ★. Three internal inconsistencies found while reading were re-verified by direct `grep` before publication.
>
> **Provenance layer.** Every headline number in this document is traced to its reporting file in the appendix, *Where the numbers come from*. That appendix gives the workplace file and, where one exists, the source card. It does not give page or table numbers inside the original papers, because the workplaces did not record them. The full citation layer is the comparison table inside each workplace, where every card holds the URL, the venue and the extraction.
>
> **Absence claims.** Every statement of the form "no paper does X" means **not found in the corpus reviewed here as of 2026-08-20**. It is not a claim about the literature as a whole. The three workplaces built corpora of 133, 120 and 120 cards independently, and the overlap between them was never measured, so no combined unique-source count exists.

---

## Act 0 — The question the previous story left open

The earlier war story in this project ended with a plan for **attribution**. We would score each in-app event — a like, a match, a conversation — for the retention it caused. Phase 1 produced per-event credit labels. Phase 2 learned to predict those labels at serving time.

That plan answered "which event matters." A second question sat right behind it, unanswered.

The ranker still optimized clicks. Our production design has two parts. A CTR/CVR-style model predicts short-term events. A separate uplift model estimates the extra retention and revenue those events cause. We then **blend the two scores after the fact**.

The blend is the problem. It is a hand-tuned weight between a probability and an effect. No single objective justifies it. So we asked the question that started this survey: **can one model take retention and revenue as its training objective, and make the blend disappear?**

Hold on to that question. It turns out to contain three separate questions, and they do not have the same answer.

---

## Act 1 — Two surveys, and the hole they left

We did not start here. Two surveys came first. Both closed on 2026-04-12.

**Survey 1** (`attribution-based-retention`) went after multi-touch attribution and causal inference for retention. It targeted 100–150 papers and delivered 23. We recorded that run as disappointing. The post-mortem named the reasons: the CATE cluster did not fit the attribution framing, ad-industry depth was shallow, and continuous targets went unaddressed.

**Survey 2** (`proxy-label-learning`) went better. The project log records 87 papers at 96% coverage. It told us to treat attribution scores as privileged information, in the teacher-logit sense. It also found no direct theory for continuous Shapley-labeled supervised objectives.

Between them, those two surveys covered attribution, uplift meta-learners, survival analysis, geo experiments, and proxy-label theory. **They left three areas untouched:** reinforcement learning for retention, long-term-value ranking objectives, and surrogate metrics.

Those three areas are exactly what you need to replace a blend with an objective. That gap is why Survey 3 exists.

---

## Act 2 — Scoping by subtraction

We wrote the Survey 3 brief on 2026-08-15. The move that shaped the whole run was **an exclusion list**.

The brief bans five areas outright: multi-touch attribution, CATE and uplift meta-learners, survival and churn basics, geo and switchback experiments, and proxy-label learning. Surveys 1 and 2 already cover them. One exception survives: cite that work when a paper uses it **inside a ranking model**.

That single exception did a lot of work later. It is why RERUM counts and the X-learner does not.

On top of the exclusions we set eight research questions and nine search directions, seeded with 41 references. We also fixed hard floors: 120 references targeted, 45 as the floor, at least 60% industry sources, and D1–D4 to hold half the corpus before D5–D9 expanded.

---

## Act 3 — Three models, one brief, no cross-reading

We then made an unusual choice. **Three models ran the identical brief in isolated workplaces.**

The rule was strict. Each model owned one subfolder. Nobody read another model's folder. The shared root held only the brief, the requirements, the queue and the log. The queue was append-only. One NotebookLM notebook served all three.

The reason was simple. One survey run gives you one reading of the literature. It gives you no way to tell a real finding from an artifact of the model that found it. Three independent runs make agreement mean something.

The runs closed across three days. `cursor-grok` finished 2026-08-17 with 120 cards. `claude_opus` finished 2026-08-17 with 133 cards. `codex-sol` finished 2026-08-18 with 120 selected sources and 118 substantive extractions.

Independence held. Both later logs record the check explicitly.

---

## Act 4 — What the field actually did

Here is the arc the corpus describes. Years were verified against the notebook.

**2008–2014 — the censored label.** Elkan and Noto (KDD 2008) established that an unlabeled sample is not a negative sample. Chapelle at Criteo (KDD 2014) turned that into the delayed feedback model, and showed that naive same-day labeling **underpredicts conversions by 21%**. That paper is the most-cited baseline in the entire corpus. Every later method that trains on a pending label descends from it.

**2017–2019 — make it an MDP.** The first answer to "optimize the long term" was reinforcement learning. DRN at Microsoft (WWW 2018) folded user return frequency into the reward. Pinterest's notification volume control (KDD 2018) maximized site-wide DAU under a volume budget. SlateQ (Google, IJCAI 2019) decomposed a slate's long-term value into item-level values. Top-K off-policy REINFORCE (Google, WSDM 2019) scaled policy gradients to a huge action space.

**2018–2022 — the cascade, and its proven bias.** In parallel the multi-task cascade matured, and the order of events matters here. ESMM (Alibaba, SIGIR 2018) modeled CTR and CVR over the whole impression space, and became the corpus's second most-cited baseline. MMoE (Google, 2018) became the standard shared backbone. Two years later, Alibaba's own Multi-IPW and Multi-DR work (WWW 2020) **proved ESMM biased**. AITM (Meituan, KDD 2021) then extended the cascade to deeper funnels on a separate branch. ESCM² (SIGIR 2022) closed the loop the 2020 critique opened, with a counterfactual regularizer.

**2019–2025 — stop hand-tuning the blend.** This strand sits closest to our problem. PE-LTR (Alibaba, RecSys 2019) and Amazon's stochastic label aggregation (WWW 2020) started learning the weights. BatchRL-MTF (Zhang et al., Tencent, KDD 2022) treated fusion as a session-level MDP, solved it with conservative Q-learning, and reported +2.55% dwell time and +9.65% positive-interaction rate at hundreds of millions of users. Tencent then published UnifiedRL and EnhancedRL (2024) as successors. Kuaishou's xMTF (WWW 2025) **replaced BatchRL-MTF's fixed log-sum formula** with formula-free monotonic fusion cells. The migration is documented end to end: fixed formula, then learned weights, then no formula at all.

**2021–2022 — change the label, not the algorithm.** Two works showed you can buy much of the long-horizon win without RL. Google's user-response models (2021) added supervised auxiliary heads to REINFORCE, and the notebook confirms this **explicitly builds on** Chen et al. (2019). PinnerFormer (Pinterest, KDD 2022) trained one user representation against a dense multi-day future-action window instead of next-item prediction. The notebook confirms PinnerFormer **explicitly modifies** the all-action objective of SASRec (Kang and McAuley, 2018). Both arrows point backward.

**2023–2025 — retention becomes the reward.** Kuaishou dominates this stretch. RLUR (WWW 2023) framed retention as an infinite-horizon MDP and minimized return-to-app time. Its online test ran about 150 days and moved app opens +0.450%, DAU +0.2%, and D7 +0.063%. TSCAC (WWW 2023) added constraints so engagement gains could not eat sparse interactions. GFN4Retention (KDD 2024) pushed a sparse session-level reward back onto item-level feedback. AURO (2025) **builds on RLUR** and attacks non-stationarity with a contrastive state-abstraction network.

**2019–2026 — do not wait for the horizon.** Athey, Chetty, Imbens and Kang introduced the surrogate index (2019). Battocchi et al. at Microsoft Research added a dynamically adjusted version (DASI). Spotify's Impatient Bandits (KDD 2023) combined partial activity traces through a Bayesian filter, and explained 50% of the prior variance from 8 days of traces — **in simulation, with no live A/B test**. ★ **Correction applied:** my draft had Impatient Bandits citing Maystre et al. 2024, which would point forward in time. The notebook settles it. Impatient Bandits (August 2023) cites the **February 2023 arXiv preprint** (arXiv:2302.03561) of that work, published in July 2024. The arrow points backward. Later work kept sharpening the read: Spotify's LOPE (2024) on a live test, Pareto-optimal proxy metrics, and PROXIMA (2026), which scores a proxy for **segment-level fragility**.

**2019–2026 — LTV heads reach production rankers.** This strand runs alongside everything above rather than after it, and it starts earlier than the generative work that often gets credited with it. ZILN (Google, 2019) supplied the zero-inflated revenue loss that the rest of the strand reuses. ODMN (Kuaishou, CIKM 2022) put multi-horizon revenue on a billion-user system. LinkedIn's LiRank (KDD 2024) and Pinterest's Save, Revisit, Retain followed. Alibaba's PDQ-LTV (2026) **builds on** Zhan et al. (2022) for watch-time debiasing.

**2024–2026 — the generative turn.** Only now do generative rankers arrive: HSTU (Meta, ICML 2024), OneRec and OneRec-V2 (Kuaishou, 2025), MTGR (Meituan, 2025), and Netflix's GenRec and GenPage (2026). They are the newest layer, not the foundation of the LTV work above.

**2018–2026 — reciprocity, on its own track.** The two-sided strand never merged with the strands above. SMILE (NeurIPS 2018) and the Palomares survey (2021) worked from static snapshots. CyberAgent produced a run of matching-market papers from 2022 onward. Yang et al. (KDD 2024) reformulated reciprocal metrics. Then ECDA (2026) delivered what the strand had lacked: a per-receiver exposure quota, a two-week calendar window, and a **large regional field experiment on a live dating platform**.

One workplace states the disconnect plainly: in the corpus it reviewed, **market-clearing methods and learned fusion never appear in the same system**.

---

## Act 5 — What broke, what was confirmed, and what turned out to be missing

The chronology is the easy half. The valuable half is what the survey did to our beliefs. An independent review pushed back on the first draft of this act, and correctly: several items below were **not** beliefs the survey overturned. They were constraints we already wrote into the brief, and the survey confirmed them with evidence. That distinction matters, so each item is now tagged.

**REVERSAL — the Instagram Explore myth.** We treated Meta's Instagram Explore value model (*Scaling the Instagram Explore Recommendations System*, 2023) as settled precedent for unified long-term ranking. It is cited that way constantly. Reading its stated objective shows a **fixed-weight linear fusion over short-term engagement probabilities**, with no horizon and no delay handling stated anywhere. That reframed the whole project. We are not adopting a proven industry pattern. We are moving a research-stage idea into production. One caution on this finding: only `claude_opus` extracted that source. Both `codex-sol` and `cursor-grok` recorded it as an extraction failure, so the reversal rests on a single workplace's reading.

**CONFIRMED — a debiased prediction is not an effect.** The brief already instructed the survey to track this for every reference. The survey supplied the evidence. Methods that look causal — IPS weighting, doubly-robust estimation, ESCM² — mostly **debias a prediction**. One workplace put the consequence in one line: conventional outcome losses rank high-propensity users, not persuadable users. That is our own constraint, restated by the literature: retention conditional on exposure is not the effect of exposure, because active users retain regardless.

**REVERSAL — most retention-RL evidence is circular.** Much of the RL-for-retention literature evaluates on the KuaiSim simulator (Zhao et al., NeurIPS 2023). One workplace reports that KuaiSim draws retention as `Geometric(p_ret)`, where `p_ret` rises with the immediate reward the policy is optimizing. If that reading is right, the simulator assumes the conclusion. The survey adopted a hard rule either way: label every result as online A/B or simulator, and never compare the two. RLUR's online test survives that filter. Much of the rest does not. Check the KuaiSim configuration directly before repeating the circularity claim.

**REVERSAL — a surrogate is a causally validated, explicitly lossy instrument.** We expected a validated surrogate to let us read a slow metric quickly. Two Netflix results changed that in one move. *Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix* (Zhang et al., arXiv 2023) covered 1,098 arms and found about 95% agreement between a 14-day and a 63-day read — but only **79% precision and 65% recall** on launch decisions, with zero false launches among tests significantly negative at 63 days. A Netflix follow-up (Bibaut, Chou, Ejdemyr and Kallus, 2024) then showed that the obvious way to validate a surrogate is wrong: correlating a user-level short signal with the long-run outcome is **biased**, and the fitted slope can carry the **wrong sign**. The rule is concrete. Do not validate a surrogate by correlating user-level likes with D30. Use a causal estimator across experiments, and plan for missed true positives.

**CONFIRMED — more engagement is not more retention.** Our brief already named the success paradox, where a good match ends the user's tenure. Pinterest's notification work (KDD 2018) and Duolingo's bandit study (KDD 2020) both found that **fewer** interventions can raise long-term engagement. TSCAC (Kuaishou, WWW 2023) is the sharpest case, because the reversal happened inside one deployment: optimizing WatchTime (+0.379%) and Share (+3.376%) drove **Comment down 0.619%**. The paradox is real and it has an analogue in production systems.

**REVERSAL — SlateQ does not transfer.** We assumed SlateQ solved item-level credit assignment. Both of its licensing assumptions fail here. Users engage several candidates per session, so *Single Choice* breaks. A match needs a delayed action by the other person, so *Reward Dependence on Selection* breaks. Worse, Kuaishou's ItemA2C tried decomposing the RL critic to item level and it **failed**. The critic had to stay list-level. One workplace answers our credit-assignment question in three words: most do not.

**REVERSAL — generative rankers unify the cascade, not the objective.** OneRec-V2 rewards a same-session watch-time quantile, and its own limitations section treats 7-day return as an evaluation metric only. MTGR trains on CTR and CTCVR. Netflix's GenRec (2026) supplies the sharpest illustration: **+0.115% on short-term engagement, and +0.006% on the long-term core metric**. That is one comparison from one system, not a general law. It is enough to show the architectural question and the objective question are separable, and not enough to settle how every generative ranker behaves.

**CONFIRMED — ranking on relevance alone breaks a two-sided market.** *Managing Congestion in Two-Sided Platforms* (arXiv 2023) reports naive ranking sending the top 20% of rooms roughly all requests, and finds that mixing in a little random ranking holds utility with less congestion. It is a structural model, not an ML ranker. CyberAgent's *Fast and Examination-agnostic Reciprocal Recommendation* (RecSys 2023) raises expected matches from 219.56 to 332.91 on a 200-user synthetic benchmark. Its *Fair Reciprocal Recommendation* follow-up (RecSys 2024) shows a welfare-maximizing ranker beating a fair one on raw matches (111.37 against 90.39) while carrying **fourteen times the envy** (434 against 31). These are small and mostly synthetic benchmarks. They establish that the trade-off is real. Making reciprocal allocation a distinct pipeline stage is our proposed response to it, not a finding the benchmarks compel.

**THE GAP THAT MATTERS MOST — the target system does not exist in the surveyed dating literature.** This is the bridge from field history to our plan, and it is more load-bearing than most of the reversals above. Three findings, each confirmed by more than one workplace independently:

- **No dating paper in the reviewed corpus trains on retention or subscription revenue.** The dating work optimizes matches, dates, chat duration and welfare.
- **No two-sided retention MDP appears anywhere in the reviewed corpus.** The retention-RL work is one-sided video.
- **No paper in the reviewed corpus models a mixed revenue stream** — subscriptions and a la carte purchases together. ZILN covers one monetary process.

Those three claims are auditable. Here is where each comes from:

| Absence claim | Reporting workplace | Searched subset and denominator | Where it is recorded |
|---|---|---|---|
| No dating paper trains on retention or subscription revenue | `cursor-grok` | D8 (two-sided/reciprocal), 22 of its 120 cards | `cursor-grok/literature-review.md` §Q7, "No D8 paper trains on D7 retention or subscription LTV" |
| No two-sided retention MDP | `cursor-grok` | Full 120-card corpus, open-gap audit item 5 | `cursor-grok/literature-review.md` §Open gaps |
| No mixed revenue stream modelled | `claude_opus` | Full 133-card corpus | `claude_opus/executive-summary.md`, "No paper among the 133 models a mixed revenue stream" |

Each denominator is one workplace's own corpus. The three corpora were built independently and their overlap was never measured, so these do not compose into a single larger denominator.

Add the horizon mismatch: the delayed-feedback literature operates at hours to days, and our horizons run to weeks. Add the provenance problem: the reward-weighting pattern our runs rank first traces to Netflix's *Reward Innovation for Long-Term Member Satisfaction* (RecSys 2023), which is one of six sources confirmed to exist and permanently unreachable. Nobody in this survey could read the keystone paper.

Together these mean the survey did not find our target system anywhere. It found the components, in other products, at other horizons, on one side of the market.

---

## Act 6 — Halfway through, the tooling collapsed

The survey ran on NotebookLM. On 2026-08-16, NotebookLM stopped.

`claude_opus` hit a session quota at 16 of 133 papers, resumed, then hit `RESOURCE_EXHAUSTED` at 44 of 133. The run verified the failure three independent ways before acting. Two subagents reproduced it. `refresh_auth` succeeded while the error persisted. The lead reproduced it directly. The MCP server then disconnected.

The response is the part worth remembering. The in-flight batches **escalated instead of writing cards from memory**, on the explicit grounds that substituting the model's own knowledge would violate the do-not-invent rule. The run then routed around the tool: 31 local PDFs from the Awesome repository, then 59 more downloaded and verified by `%PDF` magic header, 92 MB in total, gitignored.

`cursor-grok` hit the same wall at roughly 45 cards. It finished from arXiv and direct URLs, and flagged that portion as not grounded in the notebook.

`codex-sol` never hit the wall. It had used **scoped batch queries over about 15 sources at a time**, plus targeted content calls, instead of one query per paper. That difference in query shape is the whole explanation for why one run of three stayed on the intended tool. It is the single most reusable operational lesson in this survey.

Two more honest records deserve mention. `claude_opus` finished with D1–D4 at 43% against a 50% floor, and logged it as an **open deviation** rather than cutting D8. Cutting D8 would have deleted every piece of dating-industry evidence in the corpus. And `codex-sol` wrote **explicit failure cards** for the two sources it could not extract, rather than filling them in from the title.

---

## Act 7 — The review gate said no twice, then missed one

Only `codex-sol` ran an independent CLI review. It took three passes.

**Round 1 — NEEDS_FIXES.** Zero critical findings, five high, four medium. The high findings were substantive. "Source-backed" claims were not auditable at claim level. Several comparison rows were malformed, one architecture field reading literally `Model identifier: codex-sol`. The "100% coverage" framing treated a populated URL cell as proof of a working link. The Rank-1 utility contradicted itself, placing 90-day revenue in the serving utility in one section and shadow-only in another. The incrementality stage had no defined estimand. The evaluation plan omitted confidence intervals, power and stop rules.

**Round 2 — NEEDS_FIXES, much narrower.** All five high findings were confirmed resolved with proof-of-reading citations. Two medium findings survived: stale text still describing URLs as unvalidated.

**Round 3 — PASS.**

The gate earned its place. A self-contradiction on the serving utility is exactly the error a survey's own author cannot see.

It also shows its limit. The round-2 finding named two files. Both were fixed. **A third file kept the stale text.** `codex-sol/literature-review.md` still carries `url_validation: pending` in its frontmatter and "URL validation is pending" in its body, while `executive-summary.md` and `coverage-evaluation.md` both record 120 of 120 resolved. A review that fixes the instances it was pointed at does not fix the class. Verified by direct `grep` on 2026-08-20.

This document went through the same gate, and the same thing nearly happened to it. The review returned NEEDS_FIXES with one critical finding: the closing argument had collapsed three separate propositions into one. The next section is the corrected version.

---

## Act 8 — Where three independent runs agreed, and the one place they split

The three workplaces used different names and landed in nearly the same place.

| | Rank 1 | Rank 2 | Rank 3 |
|---|---|---|---|
| `claude_opus` | Reward-weighted short-term labels | Unified multi-task ranker, long-horizon head | Bilateral causal ranker on a delayed outcome |
| `cursor-grok` | Auxiliary-head LTV fusion | Retention-ensemble RL | Unified reward ranker |
| `codex-sol` | Reciprocal multi-task LTV ranker (30-day return and revenue, 90-day shadow) | Bilateral causal LTV ranker | Slate value RL or generative policy |

Read the columns.

**A multi-task ranker with long-horizon heads takes first place three times out of three.** No workplace read another. That agreement is evidence, not consensus.

**Generative and reward-model rankers come last three times out of three.** The GenRec falloff illustrates why.

**All three demote the uplift model out of the serving formula immediately.** `cursor-grok` states the supporting count: zero of its 120 cards document a CATE score inside a swipe-ranker's serving formula. `codex-sol` reduces the uplift model to a frozen audit benchmark, promotable only if six named conditions hold. `claude_opus` keeps it running in parallel and untouched during the early stages.

**Here is where they split.** Two of the three put a bilateral causal ranker on the roadmap as the destination. The third leaves it off the ranked list entirely and moves uplift permanently to evaluation. Its stated reason is blunt: no source in its corpus documents deleting the uplift model and putting CATE in the ranker. `codex-sol` occupies the middle ground and names the precondition — that step needs logged randomized exposure with validated propensities and overlap, not observational logs.

One more agreement, reached two different ways. **The "fundamentality" ranking in the method trackers is an artifact.** One run warned against reading it as quality. The other recomputed the formula and confirmed the score is explained **entirely by how often other corpus papers cite a method as a baseline**. Every other term in the formula evaluates to zero. New industrial methods score low because they are new, not because they are weak.

All three also agree on the status of what they produced. It is a strategic proposal. `codex-sol` closes with the instruction outright: do not describe the package as implementation-ready or fully evidence-validated.

---

## Where we are, and where we are going

**The arc in one sentence.** We set out to find the industry pattern for a single ranker trained on retention and revenue, found that the most-cited precedent does not do what it is cited for and that no surveyed dating system does it at all, and came away with a staged path in which each layer is a gated hypothesis rather than an adoption.

**The founding question contained three questions.** This is the correction that matters most, and an independent review is what forced it. "Replace the blend with one model trained on retention and revenue" is not one proposition. It is three, and the evidence treats them very differently.

1. **Replace the fixed post-hoc blend with learned fusion.** This is the best-supported layer. Tencent, Kuaishou, Airbnb and Pinterest all did it, and the progression from fixed formula to learned weights to no formula is documented end to end. Our runs rank it first, unanimously. It is still a hypothesis to test here, because none of that work is two-sided and none of it is dating. Treat it as **the lowest-risk thing to test first**, not as a settled adoption.
2. **Train long-horizon retention and revenue heads directly.** Plausible, with real precedent — ZILN, ODMN, PinnerFormer, LiRank. But no surveyed dating system does it, no surveyed system does it on a mixed revenue stream, and the delay literature that would tell us how to handle the labels operates at hours to days rather than weeks. **Plausible but unvalidated for this setting.**
3. **Put the incremental causal effect of exposure inside the training objective.** This is where the original framing pointed, and it is the layer with no documented precedent in any of the three corpora. It also is not identifiable from observational logs. It needs randomized exposure, validated propensities and overlap. **This remains research.** Two of three runs keep it as the destination. One takes it off the road entirely.

The first draft of this document said the premise "survived in half." That was too binary, and the review was right to reject it. Layer 1 is supported as a first test, layer 2 is plausible but unproven here, layer 3 is research.

**The standing plan** is the staged path the three runs broadly share. Stage 0 is the first step. Stage 1 is the first gate that can stop everything after it.

| Stage | Change | Gate to proceed |
|---|---|---|
| 0 | Instrument the join from event to 30-day retention and revenue. Log propensities and both-side actions. Ship nothing. | Replay reproduces assignment. Leakage tests pass. |
| 1 | **Validate a surrogate against past experiments, with a causal estimator.** | Precision and recall measured, not assumed. |
| 2 | Add long-horizon heads in shadow. Serving unchanged. | Heads calibrated on held-out horizons. |
| 3 | Replace the hand-tuned blend with learned fusion. Move uplift out of serving. | Fusion beats the blend on a long-horizon metric. No match-quality regression. |
| 4 | Add reciprocal allocation and a receiver-capacity penalty. | Match lift without overload or fairness regression. |
| 5 | Only under logged randomized exposure, move incrementality inside the objective. | Cluster-robust interval agrees with a powered market experiment. |

**Do not skip Stage 1.** Every later stage depends on reading a long-horizon result faster than the horizon, and on knowing how lossy that read is.

**Load-bearing caveats we carry forward:**

- **Item-level credit for a reciprocal, delayed outcome is unsolved in the reviewed corpus.** SlateQ's assumptions fail here, and Kuaishou's own attempt to decompose the critic failed. Anything we build on this point is new work, not adoption.
- **Prediction is not incrementality.** Keep the distinction on every card, every model and every review.
- **Congestion is an architecture gap, not a modeling gap.** A per-receiver exposure quota needs coordination across viewers. A per-request ranker cannot express it.
- **The worst measurement failure mode is interference through the training data.** A treatment changes what the shared model learns, which contaminates the control group with no direct user-to-user interference at all.
- **The dating industry publishes almost nothing.** Match Group, Bumble, Coffee Meets Bagel, Tantan and Soul returned nothing usable to any of the three runs. Grindr's 2023 blog post states that it runs no discovery ranker, which makes it a useful negative control — unifying the ranker is not universal practice even within dating. That post is three years old and should be rechecked. CyberAgent and the CoupLink field experiment are the real exception. Everything else transfers from LinkedIn Jobs, Airbnb and online recruitment, and every transfer is an assumption.

**Contested claims, flagged rather than asserted:**

- ★ **Resolved — PinnerFormer's horizon.** The notebook says a 14-day window. One card says 28 days. A second workplace reconciles them: the model **trains to 28 days and evaluates 14-day future actions**. Both numbers are right about different things.
- ★ **Corrected — the Kawamura paper.** `claude_opus` records "Kawamura et al., *Revisiting Reciprocal Recommender Systems*, KDD 2024." The notebook and `codex-sol` agree independently that these are two works. *Revisiting Reciprocal Recommender Systems* is Yang et al. (KDD 2024). *Counterfactual Reciprocal Recommender Systems* is Kawamura, Udagawa and Tateno (2025, KDD TSMO workshop). Treat them as distinct. `cursor-grok/read-papers/` settles it independently: it holds two separate cards, `2024_arXiv_NA_Revisiting-Reciprocal-Recommender-Systems.md` and `2025_arXiv_NA_Counterfactual-Reciprocal-Recommender-User-Matching.md`.
- ★ **Unresolved — Tripuraneni et al., *Choosing a Proxy Metric from Past Experiments*.** One card says Google, KDD 2024. The notebook says Spotify, 2023. A preprint a year ahead of publication explains the date. The affiliation conflict does not resolve, so this story names no company.
- **Verified contradiction — OCARM.** In `cursor-grok/literature-review.md`, the body text reports online LT30 at +20.47% and +34.43%. The comparison table reports +11.55% and +22.18% for the same split. Confirmed by `grep` at lines 465 and 899. Do not cite either number until the source card is checked.
- **Verified inconsistency — OCPC.** The running text in `claude_opus/literature-review.md` cites KDD 2019. Its own source filename says 2017.
- **Verified staleness — URL validation.** See Act 7. Three files in one workplace disagree about whether URLs were validated.
- **Contested year — DASI.** Microsoft Research's dynamically adjusted surrogate index is dated 2020 by the notebook and 2021 by a workplace card. This document gives no year.
- **Minor.** `codex-sol/literature-review.md` names "seven recurring paradigms" in prose while its own tables list nine rows. The prose merges uplift and surrogate indexing into one item. This is a presentation inconsistency, not a substantive one.
- **Company-reported numbers are not paper results.** Hinge's "8x more likely to go on dates" reaches this corpus through a press article, not a paper. Several blog-sourced lifts carry no number at all, and the survey marks them rather than guessing.

---

## Appendix — where the numbers come from

Each row gives the reporting file inside this survey. Follow the card link for the URL and the extraction. Numbers are as the cards record them, not independently re-derived here.

| Number in this document | Paper / system | Reporting file |
|---|---|---|
| 87 papers at 96% coverage (Survey 2) | `proxy-label-learning` run | `knowledge_base/projects/attribution_based_retention/log.md`, 2026-04-12 |
| Naive same-day labeling underpredicts conversions 21% | Chapelle, DFM, Criteo, KDD 2014 | `cursor-grok/literature-review.md` §D7 · card `cursor-grok/read-papers/2014_KDD_DFM_Modeling-Delayed-Feedback-Display-Advertising.md` |
| +2.55% dwell, +9.65% positive interactions | BatchRL-MTF, Tencent, KDD 2022 | `cursor-grok/literature-review.md` §D1 · card `cursor-grok/read-papers/2022_KDD_BatchRL-MTF_Multi-Task-Fusion-Long-Term-Satisfaction.md` |
| +0.450% app opens, +0.2% DAU, +0.063% D7, ~150-day test | RLUR, Kuaishou, WWW 2023 | `cursor-grok/literature-review.md` §D2 · card `cursor-grok/read-papers/2023_WWW_RLUR_Reinforcing-User-Retention-Billion-Scale.md` |
| 50% of prior variance from 8 days of traces, simulation only | Impatient Bandits, Spotify, KDD 2023 | `cursor-grok/literature-review.md` §D3 · card `cursor-grok/read-papers/2023_KDD_NA_Impatient-Bandits-Long-Term-Without-Delay.md` |
| 200 A/B tests, 1,098 arms, ~95% agreement, 79% precision, 65% recall | Zhang et al., Netflix, arXiv 2023 | `claude_opus/executive-summary.md` §6 · card `cursor-grok/read-papers/2023_arXiv_NA_Evaluating-Surrogate-Index-200-AB-Tests-Netflix.md` |
| User-level surrogate validation is biased, slope can flip sign | Bibaut, Chou, Ejdemyr, Kallus, Netflix, 2024 | `cursor-grok/executive-summary.md` Deliverable 6 · card `cursor-grok/read-papers/2024_Blog_NA_Improve-Next-Experiment-Proxy-Metrics-Netflix.md` |
| WatchTime +0.379%, Share +3.376%, Comment −0.619% | TSCAC, Kuaishou, WWW 2023 | `cursor-grok/literature-review.md` §D2 · card `cursor-grok/read-papers/2023_WWW_TCAC_Two-Stage-Constrained-Actor-Critic.md` |
| +0.115% short-term engagement, +0.006% long-term core | GenRec, Netflix, arXiv 2026 | `cursor-grok/literature-review.md` §D9 · card `cursor-grok/read-papers/2026_arXiv_GenRec_LLM-Backed-Recommendation-Ranker-Netflix.md` |
| 332.91 vs 219.56 expected matches, n=200 synthetic | CyberAgent, Fast TU, RecSys 2023 | card `cursor-grok/read-papers/2023_RecSys_NA_Fast-Examination-Agnostic-Reciprocal-Recommendation.md` |
| 111.37 matches / envy 434 vs 90.39 / envy 31 | CyberAgent, Fair Reciprocal NSW, RecSys 2024 | card `cursor-grok/read-papers/2024_RecSys_NA_Fair-Reciprocal-Recommendation-Matching-Markets.md` |
| Top 20% of rooms take roughly all requests | *Managing Congestion in Two-Sided Platforms*, arXiv 2023 | `cursor-grok/literature-review.md` line 715 · card `cursor-grok/read-papers/2023_arXiv_NA_Managing-Congestion-Two-Sided-Platforms.md` |
| D1–D4 at 43% against a 50% floor | `claude_opus` run deviation | `claude_opus/literature-review.md` line 428 |
| 133 / 120 / 120 cards; 118 substantive; 120/120 URLs | the three runs | `unified-ltv-ranking-dating/log.md` · each workplace `run-state.md` |

**Two limits of this appendix.** Every row now resolves to a reporting file, and every paper-derived row also names its source card. It does not resolve the page or table inside the original paper. And a card is a workplace's extraction of a paper, so an error in the card propagates here unchanged. The three verified contradictions listed above are the known cases.
