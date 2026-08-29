# War Story — Two-Sided Market Balancing in Dating-App Recommendation

**Composed:** 2026-08-20 · **Covers:** the shared survey at this folder root and all three model runs (`claude_opus`, `codex-sol`, `cursor-grok`), 2026-08-16 to 2026-08-20.

**Sourcing note.** This narrative reads the three runs' own outputs, then re-checks every contested date, venue, and number against the shared NotebookLM notebook (`d3071ac8-16ef-4460-8991-7701679974c8`) and against the per-paper extraction cards in `*/read-papers/`. A ★ marks a claim this pass corrected. Where the notebook and a directly-read PDF disagree, this document follows the PDF and says so, because the survey itself established that the PDF wins.

Three of five notebook queries failed, two with an incomplete chunked read and one with a timeout, so the market-design and experimentation claims (Acts 3 and 5) were checked against the extraction cards rather than the notebook. That substitution improved the result. The cards carry their own citation corrections, and they resolved four conflicts the notebook could not. A Codex review gate then read this file against the evidence and returned findings under three headings. It found no chronological contradiction, named fourteen overstatements or missing hedges, and named one missed turning point. Every one of those findings is applied below. Nothing here asserts a work as building on something published later than itself. The notebook was asked that question directly for two batches of claims and reported no such relation, and every lineage arrow below was checked by hand for direction.

---

## Act 0 — The framing that decided everything after it

On 2026-08-15 a knowledge-base check returned nothing. No prior note covered reciprocal recommendation, congestion, ecosystem health, or exposure allocation. That absence started this survey.

The problem statement was specific. A match needs a like from both sides. Every impression spends two scarce things, and only one of them is the viewer's attention. The other is the reply capacity of the person shown. Desirability is skewed, so a small group absorbs most incoming likes and cannot answer them. Their surplus likes die. Most other users get few matches and leave. Senders stop trusting the product because their likes rarely become conversations.

From that statement came one decision that shaped every later act. The target is not click-through rate or conversion rate for a single viewer. The target is the health of the whole market. The survey therefore framed the work as exposure allocation under capacity limits with feedback loops, and split the search into four layers: reciprocal scoring, capacity-aware allocation, market-design levers, and ecosystem metrics with interference-aware evaluation.

A second decision proved more consequential than it looked. The survey inverted the usual academic-first convention. Tier 1 became industry sources, Tier 2 applied research on real platform data, and Tier 3 became academic method papers. The rule required at least 60% Tier 1+2, and stated that this mix outranked the reference count. That inversion later forced an explicit correction, because a "Tier 1" company explainer carries weaker causal evidence than a randomized Tier 2 study. The `codex-sol` Phase 5 review had to write that down as a framing fix.

---

## Act 1 — One direction is not enough (2009 → 2015)

The field's first belief was that recommending people is recommending items. Score how much the viewer likes the candidate, then rank.

The first evidence against that belief was diagnostic, not algorithmic. OkCupid's 2009 analysis of its own inbox data showed attention concentrating hard on a small group, and reply rates falling for exactly the people who received the most messages. Bruch and Newman later put a measurement behind it in Science Advances 2018, using a directed PageRank desirability score to show users pursuing partners more desirable than themselves and receiving few replies.

The algorithmic break came from RECON. Pizzato and colleagues published the short paper at RecSys 2010 and the longer case study in UMUAI in 2013. Scoring both directions and combining them with a harmonic mean raised success-at-10 from 23.0% to 42.2% on an Australian dating site. That figure is an offline evaluation on commercial dating logs. The paper reports no online experiment. Tu and colleagues reproduced the direction of that result on Baihe data in 2014, reporting a median 46.84% higher success rate for male suitors under two-sided preferences. ★ That work is an arXiv preprint (arXiv:1401.8042, 2014), not a SocialRecSys paper as one run recorded it. Xia and colleagues then used RECON as a named baseline at ASONAM 2015.

**What changed.** Reciprocal scoring stopped being the contribution and became the baseline. Every later method in this corpus that cites anything cites RECON. The notebook confirms that Xia 2015, Kleinerman 2018, DPGNN 2022, TU 2023, NSW 2024, CRRS 2024, and MODE 2026 all cite it.

---

## Act 2 — Scoring both directions still concentrates the market (2014 → 2023)

The next belief followed naturally. If one-directional scoring concentrates likes, then mutual-interest prediction fixes the market.

It does not. A bilateral score still ranks the same desirable people first for everybody. The correction arrived from outside dating. LinkedIn's LiJAR at KDD 2017 forecast application volume per job, then boosted underserved jobs and penalized oversubscribed ones behind a relevance floor. In a live LinkedIn A/B test, applications moved 6.5% toward underserved jobs and 8.7% away from overserved ones, and distribution entropy rose 12%. The total stayed flat. This is one of the few numbers in the whole corpus that is a live production result rather than a simulation. LiJAR remains the closest transferable production mechanism in the whole corpus, and it says something the scoring literature did not: you need an allocation layer above the score.

CyberAgent built the dating version on Tapple. ★ That line starts earlier than two runs recorded. Ramanathan and colleagues published a short paper at RecSys 2020 and the full paper at AAAI-21, titled *A Reciprocal Embedding Framework For Modelling Mutual Preferences*. Two directed embedding models fed a fused reciprocal score, and an online recency re-rank raised real conversions by up to 60%. ★ This pass first called the "+16.9% match recall" figure unconfirmed, because the notebook could only locate the recall results as a plot. That was over-hedging. The extraction card states it directly, as an offline result against a match-only recommender: recall +16.9% on matches and +26.74% on likes. The team then moved from fusion to market clearing. An arXiv paper in 2022 introduced transferable-utility matching on Choo-Siow equilibrium, and the RecSys 2023 paper made it fast with IPFP plus maximum-inner-product search. That line rests on older economics. Its own cards name Gale and Shapley (1962) and Choo and Siow (2006) as the foundations, alongside the contemporary work of Galichon and Salanie (2022).

**What changed.** The mechanism moved from *predicting a pair* to *clearing a market*. Popularity gets penalized by the equilibrium itself rather than by a hand-set rule.

**The market-clearing idea then left the simulator, and this is the beat the survey nearly lost.** Chen, Hsieh and Lin took transferable-utility matching to a live dating platform and ran a field experiment on roughly a thousand users. Their paper, *Reducing Recommendation Inequality via Two-Sided Matching: A Field Experiment of Online Dating*, appeared in the International Economic Review in 2023, after circulating as a working paper. The same authors had studied congestion prediction in a 2019 working paper on economist against machine matchmakers. Later work treats the 2023 experiment as the directly comparable prior study and contrasts it for using coarse group-level rather than individual-level assignment.

★ No run put this in its arc, and this pass missed it until the review gate found it. That omission mattered, because it made 2026 look like the first live test of the whole idea. It was not. `codex-sol` had in fact listed this exact paper among five prescribed next searches, and nobody ran them. The honest sequence is that offline market-clearing and fairness proposals moved onto live dating platforms in 2023, and that 2026 added explicit expected-load constraints and measurement of the downstream conversation.

**And here the story turns again, in a way no single run stated.** The headline "match Gini 0.387 → 0.102" is real, but it describes the RecSys 2023 paper's *synthetic* simulation at crowding parameter 0.5, on the right-side users. ★ On *real* Japanese dating data, in the table published with the Nash-social-welfare work, transferable utility barely moves the Gini at all: the status-quo reciprocal ranker sits at about 0.742 and 0.746, and transferable utility lands at about 0.718 and 0.720. Reaching roughly 0.60 needs the Sinkhorn social-welfare method, and reaching about 0.43 needs the Nash-social-welfare method. ★ That social-welfare baseline is not a CyberAgent method. The cards identify it as Su, Bayoumi and Joachims (2022), *Optimizing Rankings for Recommendation in Matching Markets*, which the Tapple line uses as its comparison target. ★ The often-quoted "Gini 0.75 → 0.60 at Tapple" is therefore not a measured production outcome under a transferable-utility model. It is a model output in that table, and the 0.60 endpoint belongs to the social-welfare variant. One run recorded it as a production result, and the `codex-sol` review had independently flagged the same figure as secondhand.

---

## Act 3 — The product rules are a lever, not a constraint (2015 → 2024)

While the recommender literature worked on scores, economists were arguing that the platform's rules matter at least as much.

The belief they broke was that more choice and cheaper action always help. Arnosti, Johari and Kanoria showed in M&SOM 2021 that cheap, unlimited applications collapse the receiving side's ability to screen, and that caps can restore welfare to both sides. Halaburda, Piskorski and Yildirim showed that restricting the daily choice set reduces same-side rejection competition. ★ Cite that one with care. The manifest labels it Management Science 2018, but the ingested PDF is a working-paper draft dated 2017-03-10 with no journal masthead, and the extraction card flags the gap rather than asserting the journal citation.

Kanoria and Saban argued in Management Science 2021 that *which* side is allowed to search is itself a design variable, which is the formal version of the Bumble rule. Their card states the lineage plainly. They extend the static congestion model of Arnosti, Johari and Kanoria (2014) and the search-restriction work of Halaburda and colleagues (2017) into a dynamic flow setting. Lee and Niederle ran a field experiment on a Korean platform and reported in Experimental Economics 2015 that a scarce virtual rose raised acceptance by 3.3 percentage points. That result did not appear from nowhere. It transfers a signalling mechanism studied in academic job markets by Niederle, Proctor and Roth (2006), Coles and colleagues (2010), and Coles, Kushnir and Niederle (2013).

★ That rose figure needed a correction inside the survey itself. The notebook reported "+7.8 percentage points" in two separate answers. The `codex-sol` Phase 4 review traced that number to a middle-recipient subgroup coefficient in the paper's Table 4, not the overall effect, and replaced it with the card-verified +3.3 points. The review then wrote the instruction "Do not use 7.8" into the record.

Fong's work on market thickness supplies the sharpest lesson for a growth team. Adding members to a thin market can *reduce* matches, because extra choice raises selectivity, unless the like limit moves with market size. ★ This citation is less settled than any run stated, and this pass overstated it once before correcting it. The retrieved PDF is a Stanford working paper dated 2018-09-10, titled *Search, Selectivity, and Market Thickness in Two-Sided Markets*, and its title page credits Jessica Yu. The queue links it to a **differently titled** paper, *Effects of Market Size and Competition in Two-Sided Markets: Evidence from Online Dating*, credited to Jessica Fong in Marketing Science 2024. The extraction card states plainly that this is very likely one research program, but that the identity is not confirmed inside the document. Treat the 2018 working paper as the artifact actually read. Do not cite the Marketing Science 2024 paper as the same work until someone checks it.

**What changed.** Like limits, batch size, signalling tokens, and initiation rules entered the same design space as the ranker.

---

## Act 4 — The objective moved three times (2018 → 2026)

Layer 4 has the least stable history in this corpus. The objective moved three times in eight years, and only the last move was an actual rejection. ★ An earlier draft of this act called it two moves and described the fairness step as a rejection. The review gate caught that, and it was right.

The first move was from relevance to exposure. Singh and Joachims established at KDD 2018 that ranking purely by predicted relevance is itself an allocation decision, and that exposure can be optimized directly under constraints. Do and colleagues extended the idea to two-sided welfare through Lorenz dominance at NeurIPS 2021.

The second move refined the first rather than rejecting it. It shifted the target from aggregate exposure and welfare toward two-sided envy. Tomita and Yokoyama's Nash-social-welfare work at RecSys 2024 put a price tag on that refinement which nobody can argue with. The comparison used real dating data with 200 users per side, but the outcomes are offline model-based expectations rather than a field result. The social-welfare method produced 111.37 expected matches, with envy counts of 434 and 331. Their Nash-social-welfare method produced 90.39 matches, with envy counts of 31 and 14. Fairness cost roughly a fifth of the matches. ★ That work has two versions, and one run listed them as two separate papers. The first is the RecSys 2024 conference paper. The second is a 2026 extended manuscript titled *Balancing Fairness and High Match Rates in Reciprocal Recommender Systems*. ★ Do not call the second one a journal article. The notebook reported it as accepted in ACM Transactions on Recommender Systems, but the extraction card records an arXiv preprint whose own venue field is an unfilled placeholder, submitted for ACM publication. That is one more notebook over-claim.

The third move is the real rejection. MRet argued that both earlier objectives are wrong. Kishimoto and colleagues published *Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching* at ICLR 2026 (arXiv:2602.15752). ★ Two runs disagreed on its status, one calling it a preprint and one calling it ICLR 2026. The notebook settles it as an ICLR 2026 conference paper. Its synthetic result is the memorable one: maximizing matches and randomizing produce almost the same retention, and MRet retains more users while taking only about 70% of the match volume that match-maximization produces. ★ That 70% figure is synthetic. On real, very sparse dating data the paper reports the highest retention of all methods tested but gives no magnitude. Both cautions in the runs were right about different experiments.

In parallel the measurement side moved. Yang and colleagues at KDD 2024 replaced one-sided recall with reciprocal coverage, bilateral stability, and reciprocal NDCG, and added a vacant-slot re-rank so that a slate produces *distinct* matches.

★ One survey-of-surveys point needs fixing. Two runs disagreed on the year of the Mashayekhi e-recruitment survey. The cards give ACM Computing Surveys **2024**, by Mashayekhi, Li, Kang, Lijffijt and De Bie at Ghent University. One run log still records 2022, so check the ACM record before citing this outside the team. That survey cites LiJAR and deliberately excludes dating to bound its scope, so it does not close this survey's own gap.

**What changed.** The north star moved from relevance, to constrained exposure and welfare, to two-sided envy, and finally to retention. Only the last step rejects what came before. The three earlier steps refine one another. Notably, the group that built the transferable-utility line also co-authored MRet, so the field's own leaders published the argument against their earlier objective.

---

## Act 5 — The measuring instrument was wrong (2021 → 2025)

Every mechanism above shares one problem. A treated user consumes the same person's reply capacity that a control user needs. Ordinary user-split A/B testing therefore measures the wrong thing.

Johari, Li, Liskovich and Weintraub formalized this in Management Science 2022 and showed that the least-biased side to randomize depends on which side is congested. Holtz and colleagues measured it. Their Airbnb pricing meta-experiment, published in Management Science in 2025, found that 19.76% of the naive individual-level estimate was interference. The two lines ran in parallel rather than in sequence, because working-paper versions of both circulated years before publication. ★ The notebook also produced a supply-constrained and demand-constrained split of that number in one answer. The `codex-sol` review checked the card and removed it, because the paper reports only the overall figure and states the subgroup difference is not significant.

★ One much-cited item in this area was mislabelled in every run, and the cards resolve it in full. The ingested "Multiple Randomization Designs" document is *Multiple Randomization Designs: Estimation and Inference with Interference*, by Masoero, Vijaykumar, Richardson, McQueen, Rosen, Burdick, Bajari and Imbens. Its own header is dated 2025-12-02, and it is version 4 of an arXiv record first assigned in December 2021. It *cites* the earlier Bajari and colleagues proposal as prior work rather than being that work. The brief called it "Bajari et al. 2021," which named the wrong artifact.

LinkedIn's UniCoRn showed how to run a producer-side experiment when the outcome depends on who viewed. It reports weekly-active-user lift of 0.51% for candidate generation and 0.13% for ranking, and session lift of 0.57% and 0.11%, measured on the viewee side using 40% of viewer-side traffic. Hayashi, Goda and Saito supplied matching-specific off-policy evaluation at RecSys 2025, because standard estimators are unstable when the reward is a sparse two-stage event.

**What changed.** Interference-aware design stopped being a statistical nicety and became a precondition. Without it, none of Acts 2 to 4 can be tested honestly on a real product.

**The gap that survived all three runs.** No run found a dating-log off-policy evaluation, as of 2026-08-20. Hayashi's experiment runs on Wantedly job-matching logs. UniCoRn is LinkedIn. Holtz is Airbnb. All three runs searched for a dating-native interference design, and all three logged the same null.

---

## Act 6 — 2026 makes the cost explicit

The most uncomfortable paper in this corpus is also the most useful, because it measured what the others stopped short of measuring. ★ An earlier draft called it the only real dating field experiment. That was wrong, and Act 2 now carries the 2023 experiment it overlooked. The defensible claim is narrower. This is the only directly read paper here that field-tests an explicit expected-load allocator *and* follows the effect through to downstream messaging.

Sekiya, Otani, Komatsu, Ohkawa and Noda dated their paper 2026-02-24 and posted it to arXiv on 2026-02-23. Their method, exposure-constrained deferred acceptance, limits a receiver's exposure by *expected likes or dates* rather than by headcount. They introduce a congestion-adjusted metric called effective dates, which discounts matches that involve overloaded receivers.

Two kinds of evidence follow, and the survey must not blend them.

**Offline simulation, calibrated on real CoupLink candidate data.** The method raised effective dates from the deployed recommender's 0.0584 to 0.0623, and receiver dating probability from 0.0863 to 0.0932. This is a simulation on real data, not a live outcome.

**A live geographic rollout.** Kanto received the treatment and Kansai-Tokai acted as control, for two weeks from 2026-01-13. The study was pre-registered (AEARCTR-0015446) and approved by a University of Tokyo review board. Read the results carefully, because the significance pattern carries the whole lesson.

- Receiver-side likes rose clearly, by 0.264 in the full sample and 0.334 with the tail excluded. Both results are significant at the 1% level. The allocator does move exposure.
- Total dates fell significantly at the *prediction* stage, by 0.003. In *realized* behaviour the full-sample estimate is −0.002 and not significant.
- The realized effective-dates gain of +0.003 reaches significance only after excluding the top 0.1% most congested receiver-days. The full-sample realized estimate is +0.002 and not significant.
- Post-match messaging did not improve. In the full sample the receiver message average fell by 0.004, significant only at the 10% level. With the tail excluded, every messaging outcome is exactly 0.000.

Two design limits belong with those numbers. The comparison uses only two geographic macro-clusters, which the authors themselves flag. The headline effective-dates result depends on a tail exclusion.

**What changed.** Capacity-aware allocation acquired a dating field test that reaches all the way to conversation, and the conversation did not move. This is stronger than silence and weaker than a refutation. Messaging was measured, and the estimate is null or slightly negative. The survey's own target includes conversations, so the best available evidence supports the matching half of the objective and returns a null on the other half. `codex-sol` reached the same conclusion independently and recorded it as unresolved.

## Act 7 — The survey's own war: three models, one notebook, three tool failures

The research story above was assembled while the tooling failed in three different ways. Each failure changed a belief about how to run this kind of survey.

**`claude_opus` — the extraction pivot.** The run drove NotebookLM hard, at one point with 16 concurrent agents each firing about a dozen queries. A `cursor-grok` run on the same account had already spent quota that day. The account hit `RESOURCE_EXHAUSTED`, a token refresh did not help, and `nlm doctor` passed every check, which proved the block was quota and not authentication. Rather than wait, the run downloaded the papers and read the PDFs directly. **That accident produced the run's most valuable output.** Reading real results sections caught eight citation errors that metadata alone would have carried forward. It found that one ingested PDF is *Platform Design in Curated Dating Markets*, a different blinded manuscript, and not the seed paper the brief named. It found that the Fong source is the working paper. It found that a blocked `source_add` still creates a source record with no content, that NotebookLM then answers fluently about that empty record, and that it has been observed inventing a title for one.

**`cursor-grok` — the shared-state failure.** The merged queue file's own header records what happened. This run recreated the shared `queue.md` ten minutes after `claude_opus` created it, without reading the existing file, and overwrote its 93 entries despite an append-only rule. Nothing was lost, because the two versions were merged, but the merged file still carries duplicated tier headers as a scar. The lesson the run recorded is blunt: keep a private authoritative copy per run, and re-check shared files before trusting them. The same run also lost work permanently. A 61-hit deep-research task from 2026-08-16 could never be imported, and the task itself later disappeared.

**`codex-sol` — the review-gate failure, and the discipline it forced.** Every one of its three review gates first tried the Codex CLI, and every one failed with an account usage-limit error, so all three fell back to the Cursor agent in read-only mode. That fallback still did the job, and this run's Phase 4 review is the single most valuable artifact in the folder. It treated NotebookLM as a witness to cross-examine rather than as an oracle. It caught the rose subgroup coefficient. It caught Nash-social-welfare Gini figures that belong to a different paper. It caught an exposure-constrained-deferred-acceptance likes figure absent from the card. It caught a favorites coefficient the card contradicts. It overturned the notebook's claim that DPGNN is the only method used as a direct baseline, finding four such cases across three methods. It also corrected its own reviewer: a Phase 3.7 footer claimed 42 citation relations while the body held 41, and a strict paper-identity filter cut those to 33.

**What changed, across all three.** The belief that a retrieval notebook over 140 sources is a reliable citation oracle did not survive contact with the corpus. Two things replaced it. Read the actual document when the claim carries a number. Run an adversarial review that is allowed to delete a fluent answer.

---

## Epilogue — Where the three runs disagree, and what this pass found

This section is an audit rather than an act. Nothing in the field's causal development turns on it. It exists so the next reader knows which claims are safe to reuse. The runs did not converge, and the differences are informative rather than embarrassing.

| Dimension | `claude_opus` | `cursor-grok` | `codex-sol` |
|---|---|---|---|
| Bibliography size | 82 distinct works from 86 extraction files | 72 annotated | 45 selected |
| Tier 1+2 share | 64.8% | 86% | 86.7% |
| Extraction method | direct PDF reads after the quota block | NotebookLM extracts plus live pages | NotebookLM plus per-card verification |
| Distinctive artifact | eight citation corrections | reverse-citation map, 18 edges | adversarial Phase 4 and 5 reviews |
| Headline lean | build a reciprocal expected-load re-ranker | market-clearing plus separate match-health KPIs | four-stage market layer, evidence limits stated |

★ The count requirement itself was rewritten mid-survey, according to the shared `requirements.md`. That file originally set a 60–100 item floor for NotebookLM runs. After `codex-sol` finished with 45 verified items at 86.7% Tier 1+2 and zero coverage gaps, the document was corrected to make 30–50 authoritative and to mark the 60–100 floor stale. That is a defensible call, because the mix rule always outranked the count. It is worth recording plainly, because the requirement changed to match the result rather than the result changing to match the requirement.

★ One cross-run dispute was resolved today, against the run that was most careful. `codex-sol` excluded Hinge's "double-digit increase in matches" because it could not verify the number inside its own 45-card corpus, and wrote "Do not import that number into this corpus." The number is real. It appears in Hinge's newsroom post *Evolving Together: How Daters Helped Shape Hinge in 2025*, dated 2025-11-10, attributed to an updated deep-learning algorithm that predicts mutual compatibility. ★ That same check also confirms the post does *not* mention Gale-Shapley. The 2018 TechCrunch article about "Most Compatible" does credit Gale-Shapley, and the two claims had been merged in places.

★ The verification oracle failed in **both** directions, which is the most transferable lesson here. It invented and misattributed numbers, as Act 3 and Act 5 show. It also *denied* sources that exist. Asked about Tinder's two-tower P(Match) work, it answered "not in sources." Yet `cursor-grok` holds a full card for that work, with a notebook source identifier. The card names Sokolov, Hickey and Du, Tinder Tech Blog, 2025. It reports +6.5% match rate and +22% match volume for P(Match), against +3.8% swipe-right rate for P(Like). The explanation is the empty-record failure that `claude_opus` had already documented, because Medium-hosted pages ingest as records with no readable body. The same happened for the 2021 OkCupid voter-and-votee post. Those two numbers are blog-reported and were cited from the live pages, and they should be labelled that way rather than dropped.

★ A correction can also fail to travel inside one run. `claude_opus` recorded the Masoero finding in its `log.md` and its `RESUME-HERE.md`. Its own `method-tracker.md` still lists the method as "Bajari et al., arXiv 2021." The `codex-sol` tracker carries a different partial version. It pairs the 2021 arXiv year with the Masoero byline. Both trackers are wrong in different directions, and both sit beside a correct log entry. A citation fix is not applied until every artifact that repeats the citation is updated.

★ One thread stays genuinely open. The Rios, Saban and Zheng assortment work is potentially the largest reported dating **field** result in this corpus, and no two runs agree on its identity. The year is recorded as M&SOM 2022 in one place and M&SOM volume 25, issue 4, 2023 in another. The reported lift appears as 25% or more, at least 27%, and 40%, from three different pages. The one thing all runs agree on is that the ingested PDF is a *different* manuscript, so nobody read the paper itself. Do not cite this work until someone opens the published article.

★ Finally, this pass re-checked two numbers the notebook contradicted, and the notebook lost both times. It quoted a weaker baseline row for exposure-constrained deferred acceptance, and it reported MRet's retention magnitude as unspecified. The directly-read PDF cards held the better answers in both cases, exactly as `claude_opus` predicted after its extraction pivot.

---

## The arc in one sentence

The field moved from *score the viewer*, to *score both directions*, to *clear the market under capacity*, to *change the product rules too*, to *stop counting matches and start counting retention*, then out of the simulator onto live dating platforms in 2023, and finally to a 2026 field test that improved congestion-adjusted matching and returned a null on conversation. The survey that assembled this arc learned the same thing three separate times, from three different tool failures. A retrieval notebook is a witness to cross-examine, not an oracle to quote.

## Standing direction

1. Add a reciprocal term that conditions on the other side's remaining reply capacity. Tinder reports having A/B tested this shape as P(Match) against P(Like).
2. Put an explicit allocation layer above the score. Start with LiJAR-style soft boost and penalty behind a relevance floor, because it is the only live production A/B result in the corpus. Treat exposure-constrained deferred acceptance as the dating-native target design, and expect it to move matching before it moves conversation.
3. Keep like caps, batch size, initiation rules, and scarce signals inside the same design space as the model.
4. Replace swipe-rate north stars with match distribution, wasted-like rate, conversations, and two-sided retention. Report effects separately for sender-constrained, receiver-constrained, and balanced segments.
5. Do not test any of the above on a user-split A/B. Use geographic, cluster, or two-sided randomization.

## Load-bearing caveats to carry forward

- No study in this corpus validates the whole chain in one dating system. The strongest field result improves congestion-adjusted matching, and returns a null on conversation.
- Capacity has no agreed definition. The corpus uses hard budgets, forecast demand, vacancy, and equilibrium outside options, and none is calibrated to a measured reply capacity.
- Most transferable mechanisms come from markets with renewable supply — jobs, music, listings, rides. They transfer only after "item availability" is replaced by a person's scarce reply bandwidth.
- Synthetic and real results diverge sharply for the same method. Transferable utility flattens the Gini dramatically in simulation and barely at all on the real dating table in Act 2.
- These are corpus-level nulls as of 2026-08-20, not proof of non-existence. No run found a dating-log off-policy evaluation, a Bumble engineering ranking source, or an official Chinese dating-ranking engineering source, despite repeated searches by two runs.
- The CyberAgent RecSys 2023 and RecSys 2024 papers are shared with Survey 3. If both surveys are used together, do not count them twice.
- The 2023 Chen, Hsieh and Lin field experiment is cited by three papers in this corpus but was never read directly by any run. Read it before making any claim about which work first field-tested this idea.
- Several citations still need a version decision before external use: Fong's working paper against the Marketing Science 2024 version, the Fong author-surname question, and the working-paper versions cited for Halaburda, Kanoria-Saban, Arnosti and Ashlagi.
