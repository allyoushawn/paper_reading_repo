# War Story — Two-Sided Market Balancing in Dating-App Recommendation

**Composed:** 2026-08-20 · **Covers:** the shared survey at this folder root and all three model runs (`claude_opus`, `codex-sol`, `cursor-grok`), 2026-08-16 to 2026-08-20.

**Sourcing.** This narrative reads the three runs' outputs, then re-checks every contested date, venue, and number against the per-paper extraction cards in `*/read-papers/` and against the shared NotebookLM notebook (`d3071ac8-16ef-4460-8991-7701679974c8`). Where the notebook and a directly-read PDF disagree, this document follows the PDF. Three of five notebook queries failed, so the market-design and experimentation claims in Acts 3 and 5 rest on the extraction cards. A Codex review gate then read the draft against the same evidence. The correction record for this pass lives in `log.md`.

---

## Act 0 — The framing that decided everything after it

On 2026-08-15 a knowledge-base check returned nothing. No prior note covered reciprocal recommendation, congestion, ecosystem health, or exposure allocation. That absence started this survey.

The problem statement was specific. A match needs a like from both sides. Every impression spends two scarce things, and only one of them is the viewer's attention. The other is the reply capacity of the person shown. Desirability is skewed, so a small group absorbs most incoming likes and cannot answer them. Their surplus likes die. Most other users get few matches and leave. Senders stop trusting the product because their likes rarely become conversations.

From that statement came one decision that shaped every later act. The target is not click-through rate or conversion rate for a single viewer. The target is the health of the whole market. The survey therefore framed the work as exposure allocation under capacity limits with feedback loops, and split the search into four layers: reciprocal scoring, capacity-aware allocation, market-design levers, and ecosystem metrics with interference-aware evaluation.

A second decision proved more consequential than it looked. The survey inverted the usual academic-first convention. Tier 1 became industry sources, Tier 2 applied research on real platform data, and Tier 3 became academic method papers. The rule required at least 60% Tier 1+2, and stated that this mix outranked the reference count. That inversion has a cost worth naming. A Tier 1 company explainer carries weaker causal evidence than a randomized Tier 2 study. The tier order ranks operational relevance, not reliability.

---

## Act 1 — One direction is not enough (2009 → 2015)

The field's first belief was that recommending people is recommending items. Score how much the viewer likes the candidate, then rank.

The first evidence against that belief was diagnostic, not algorithmic. OkCupid's 2009 analysis of its own inbox data showed attention concentrating hard on a small group, and reply rates falling for exactly the people who received the most messages. Bruch and Newman later put a measurement behind it in Science Advances 2018, using a directed PageRank desirability score to show users pursuing partners more desirable than themselves and receiving few replies.

The algorithmic break came from **RECON**. Pizzato and colleagues published the short paper at RecSys 2010 and the longer case study in UMUAI in 2013. Scoring both directions and combining them with a harmonic mean raised success-at-10 from 23.0% to 42.2% on an Australian dating site. That figure is an offline evaluation on commercial dating logs. The paper reports no online experiment. Tu and colleagues reproduced the direction of that result on Baihe data in 2014, reporting a median 46.84% higher success rate for male suitors under two-sided preferences (arXiv:1401.8042). Xia and colleagues then used RECON as a named baseline at ASONAM 2015.

**What changed.** Reciprocal scoring stopped being the contribution and became the baseline. Every later method in this corpus that cites anything cites RECON. Xia 2015, Kleinerman 2018, DPGNN 2022, TU 2023, NSW 2024, CRRS 2024, and MODE 2026 all cite it.

---

## Act 2 — Scoring both directions still concentrates the market (2014 → 2023)

The next belief followed naturally. If one-directional scoring concentrates likes, then mutual-interest prediction fixes the market.

It does not. A bilateral score still ranks the same desirable people first for everybody. The correction arrived from outside dating. LinkedIn's **LiJAR at KDD 2017** forecast application volume per job, then boosted underserved jobs and penalized oversubscribed ones behind a relevance floor. In a live LinkedIn A/B test, applications moved 6.5% toward underserved jobs and 8.7% away from overserved ones, and distribution entropy rose 12%. The total stayed flat. This is one of the few numbers in the whole corpus that is a live production result rather than a simulation. LiJAR remains the closest transferable production mechanism in the corpus, and it says something the scoring literature did not: you need an allocation layer above the score.

CyberAgent built the dating version on Tapple. Ramanathan and colleagues published a short paper at RecSys 2020 and the full paper at AAAI-21, titled *A Reciprocal Embedding Framework For Modelling Mutual Preferences*. Two directed embedding models fed a fused reciprocal score, and an online recency re-rank raised real conversions by up to 60%. Against a match-only recommender, the framework also raised offline recall by 16.9% on matches and 26.74% on likes. The team then moved from fusion to market clearing. An arXiv paper in 2022 introduced transferable-utility matching on Choo-Siow equilibrium, and the RecSys 2023 paper made it fast with IPFP plus maximum-inner-product search. That line rests on older economics. Its own cards name Gale and Shapley (1962) and Choo and Siow (2006) as the foundations, alongside the contemporary work of Galichon and Salanie (2022).

**What changed.** The mechanism moved from *predicting a pair* to *clearing a market*. Popularity gets penalized by the equilibrium itself rather than by a hand-set rule.

**Then the market-clearing idea left the simulator.** Chen, Hsieh and Lin took transferable-utility matching to a live dating platform and ran a field experiment on roughly a thousand users. Their paper, *Reducing Recommendation Inequality via Two-Sided Matching: A Field Experiment of Online Dating*, appeared in the International Economic Review in 2023, after circulating as a working paper. The same authors had studied congestion prediction in a 2019 working paper on economist against machine matchmakers. Later work treats the 2023 experiment as the directly comparable prior study, and contrasts it for using coarse group-level rather than individual-level assignment. The honest sequence is therefore that offline market-clearing and fairness proposals moved onto live dating platforms in 2023, and that 2026 added explicit expected-load constraints and measurement of the downstream conversation.

**And here the story turns again.** The headline "match Gini 0.387 → 0.102" is real, but it describes the RecSys 2023 paper's *synthetic* simulation at crowding parameter 0.5, on the right-side users. On *real* Japanese dating data, in the table published with the Nash-social-welfare work, transferable utility barely moves the Gini at all. The status-quo reciprocal ranker sits at about 0.742 and 0.746, and transferable utility lands at about 0.718 and 0.720. Reaching roughly 0.60 needs the Sinkhorn social-welfare method, and reaching about 0.43 needs the Nash-social-welfare method. That social-welfare baseline is not a CyberAgent method. It is Su, Bayoumi and Joachims (2022), *Optimizing Rankings for Recommendation in Matching Markets*, which the Tapple line uses as its comparison target. The frequently quoted "Gini 0.75 → 0.60 at Tapple" is therefore not a measured production outcome under a transferable-utility model. It is a model output in that table, and the 0.60 endpoint belongs to the social-welfare variant.

---

## Act 3 — The product rules are a lever, not a constraint (2015 → 2024)

While the recommender literature worked on scores, economists were arguing that the platform's rules matter at least as much.

The belief they broke was that more choice and cheaper action always help. Arnosti, Johari and Kanoria showed in M&SOM 2021 that cheap, unlimited applications collapse the receiving side's ability to screen, and that caps can restore welfare to both sides. Halaburda, Piskorski and Yildirim showed that restricting the daily choice set reduces same-side rejection competition. Cite that one with care. The artifact read here is a working-paper draft dated 2017-03-10 with no journal masthead. The Management Science 2018 attribution is not confirmed inside the document.

Kanoria and Saban argued in Management Science 2021 that *which* side is allowed to search is itself a design variable, which is the formal version of the Bumble rule. Their card states the lineage plainly. They extend the static congestion model of Arnosti, Johari and Kanoria (2014) and the search-restriction work of Halaburda and colleagues (2017) into a dynamic flow setting.

Lee and Niederle ran a field experiment on a Korean platform and reported in Experimental Economics 2015 that a scarce virtual rose raised acceptance by 3.3 percentage points. Use that overall effect. The paper's Table 4 also carries a larger coefficient of 7.8 points, but that number belongs to a middle-recipient subgroup and is not the headline result. The rose finding did not appear from nowhere. It transfers a signalling mechanism studied in academic job markets by Niederle, Proctor and Roth (2006), Coles and colleagues (2010), and Coles, Kushnir and Niederle (2013).

Fong's work on market thickness supplies the sharpest lesson for a growth team. Adding members to a thin market can *reduce* matches, because extra choice raises selectivity, unless the like limit moves with market size. This citation is less settled than it looks. The retrieved PDF is a Stanford working paper dated 2018-09-10, titled *Search, Selectivity, and Market Thickness in Two-Sided Markets*, and its title page credits Jessica Yu. The queue links it to a **differently titled** paper, *Effects of Market Size and Competition in Two-Sided Markets: Evidence from Online Dating*, credited to Jessica Fong in Marketing Science 2024. These are very likely one research program, but the document does not confirm the identity. Treat the 2018 working paper as the artifact actually read. Do not cite the Marketing Science 2024 paper as the same work until someone checks it.

**What changed.** Like limits, batch size, signalling tokens, and initiation rules entered the same design space as the ranker.

---

## Act 4 — The objective moved three times (2018 → 2026)

Layer 4 has the least stable history in this corpus. The objective moved three times in eight years, and only the last move was an actual rejection.

The first move was from relevance to exposure. Singh and Joachims established at KDD 2018 that ranking purely by predicted relevance is itself an allocation decision, and that exposure can be optimized directly under constraints. Do and colleagues extended the idea to two-sided welfare through Lorenz dominance at NeurIPS 2021.

The second move refined the first rather than rejecting it. It shifted the target from aggregate exposure and welfare toward two-sided envy. Tomita and Yokoyama's Nash-social-welfare work at RecSys 2024 put a price tag on that refinement which nobody can argue with. The comparison used real dating data with 200 users per side, but the outcomes are offline model-based expectations rather than a field result. The social-welfare method produced 111.37 expected matches, with envy counts of 434 and 331. Their Nash-social-welfare method produced 90.39 matches, with envy counts of 31 and 14. Fairness cost roughly a fifth of the matches. That work exists in two versions of one line of research. The first is the RecSys 2024 conference paper. The second is a 2026 extended manuscript titled *Balancing Fairness and High Match Rates in Reciprocal Recommender Systems*. The second is an arXiv preprint submitted for ACM publication, and its own venue field is an unfilled placeholder. Do not cite it as a journal article.

The third move is the real rejection. MRet argued that both earlier objectives are wrong. Kishimoto and colleagues published *Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching* at ICLR 2026 (arXiv:2602.15752). Its synthetic result is the memorable one. Maximizing matches and randomizing produce almost the same retention, and MRet retains more users while taking only about 70% of the match volume that match-maximization produces. That 70% figure is synthetic. On real, very sparse dating data the paper reports the highest retention of all methods tested, but gives no magnitude.

In parallel the measurement side moved. Yang and colleagues at KDD 2024 replaced one-sided recall with reciprocal coverage, bilateral stability, and reciprocal NDCG, and added a vacant-slot re-rank so that a slate produces *distinct* matches. The e-recruitment survey by Mashayekhi, Li, Kang, Lijffijt and De Bie at Ghent University appeared in ACM Computing Surveys in 2024. It cites LiJAR and deliberately excludes dating to bound its scope, so it does not close this survey's own gap.

**What changed.** The north star moved from relevance, to constrained exposure and welfare, to two-sided envy, and finally to retention. Only the last step rejects what came before. The three earlier steps refine one another. Notably, the group that built the transferable-utility line also co-authored MRet, so the field's own leaders published the argument against their earlier objective.

---

## Act 5 — The measuring instrument was wrong (2021 → 2025)

Every mechanism above shares one problem. A treated user consumes the same person's reply capacity that a control user needs. Ordinary user-split A/B testing therefore measures the wrong thing.

Johari, Li, Liskovich and Weintraub formalized this in Management Science 2022 and showed that the least-biased side to randomize depends on which side is congested. Holtz and colleagues measured it. Their Airbnb pricing meta-experiment, published in Management Science in 2025, found that 19.76% of the naive individual-level estimate was interference. That paper reports the overall figure only, and states that the difference between supply-constrained and demand-constrained listings is not significant. The two lines ran in parallel rather than in sequence, because working-paper versions of both circulated years before publication.

One much-cited item in this area needs an exact citation. The "Multiple Randomization Designs" document is *Multiple Randomization Designs: Estimation and Inference with Interference*, by Masoero, Vijaykumar, Richardson, McQueen, Rosen, Burdick, Bajari and Imbens. Its own header is dated 2025-12-02, and it is version 4 of an arXiv record first assigned in December 2021. It *cites* the earlier Bajari and colleagues proposal as prior work rather than being that work.

LinkedIn's UniCoRn showed how to run a producer-side experiment when the outcome depends on who viewed. It reports weekly-active-user lift of 0.51% for candidate generation and 0.13% for ranking, and session lift of 0.57% and 0.11%, measured on the viewee side using 40% of viewer-side traffic. Hayashi, Goda and Saito supplied matching-specific off-policy evaluation at RecSys 2025, because standard estimators are unstable when the reward is a sparse two-stage event.

**What changed.** Interference-aware design stopped being a statistical nicety and became a precondition. Without it, none of Acts 2 to 4 can be tested honestly on a real product.

**The gap this layer still has.** Repeated searches found no dating-log off-policy evaluation, as of 2026-08-20. Hayashi's experiment runs on Wantedly job-matching logs. UniCoRn is LinkedIn. Holtz is Airbnb. The dating-native interference design does not exist in this corpus.

---

## Act 6 — 2026 makes the cost explicit

The most uncomfortable paper in this corpus is also the most useful, because it measured what the others stopped short of measuring. It is the only directly read paper here that field-tests an explicit expected-load allocator *and* follows the effect through to downstream messaging.

Sekiya, Otani, Komatsu, Ohkawa and Noda dated their paper 2026-02-24 and posted it to arXiv on 2026-02-23. Their method, exposure-constrained deferred acceptance, limits a receiver's exposure by *expected likes or dates* rather than by headcount. They introduce a congestion-adjusted metric called effective dates, which discounts matches that involve overloaded receivers.

Two kinds of evidence follow, and the survey must not blend them.

**Offline simulation, calibrated on real CoupLink candidate data.** The method raised effective dates from the deployed recommender's 0.0584 to 0.0623, and receiver dating probability from 0.0863 to 0.0932. This is a simulation on real data, not a live outcome.

**A live geographic rollout.** Kanto received the treatment and Kansai-Tokai acted as control, for two weeks from 2026-01-13. The study was pre-registered (AEARCTR-0015446) and approved by a University of Tokyo review board. Read the results carefully, because the significance pattern carries the whole lesson.

- Receiver-side likes rose clearly, by 0.264 in the full sample and 0.334 with the tail excluded. Both results are significant at the 1% level. The allocator does move exposure.
- Total dates fell significantly at the *prediction* stage, by 0.003. In *realized* behaviour the full-sample estimate is −0.002 and not significant.
- The realized effective-dates gain of +0.003 reaches significance only after excluding the top 0.1% most congested receiver-days. The full-sample realized estimate is +0.002 and not significant.
- Post-match messaging did not improve. In the full sample the receiver message average fell by 0.004, significant only at the 10% level. With the tail excluded, every messaging outcome is exactly 0.000.

Two design limits belong with those numbers. The comparison uses only two geographic macro-clusters, which the authors themselves flag. The headline effective-dates result depends on a tail exclusion.

**What changed.** Capacity-aware allocation acquired a dating field test that reaches all the way to conversation, and the conversation did not move. This is stronger than silence and weaker than a refutation. Messaging was measured, and the estimate is null or slightly negative. The survey's own target includes conversations, so the best available evidence supports the matching half of the objective and returns a null on the other half.

---

## Act 7 — The survey's own war: three models, one notebook, three tool failures

The research story above was assembled while the tooling failed in three different ways. Each failure changed a belief about how to run this kind of survey.

**`claude_opus` — the extraction pivot.** The run drove NotebookLM hard, at one point with 16 concurrent agents each firing about a dozen queries. A `cursor-grok` run on the same account had already spent quota that day. The account hit `RESOURCE_EXHAUSTED`, a token refresh did not help, and `nlm doctor` passed every check, which proved the block was quota and not authentication. Rather than wait, the run downloaded the papers and read the PDFs directly. **That accident produced the run's most valuable output.** Reading real results sections caught eight citation errors that metadata alone would have carried forward. It found that one ingested PDF is *Platform Design in Curated Dating Markets*, a different blinded manuscript, and not the seed paper the brief named. It also found the mechanism behind a whole class of silent failures. A blocked `source_add` still creates a source record with no content, and NotebookLM then answers fluently about that empty record. It has been observed inventing a title for one.

**`cursor-grok` — the shared-state failure.** The merged queue file's own header records what happened. This run recreated the shared `queue.md` ten minutes after `claude_opus` created it, without reading the existing file, and overwrote its 93 entries despite an append-only rule. Nothing was lost, because the two versions were merged, but the merged file still carries duplicated tier headers as a scar. The lesson the run recorded is blunt. Keep a private authoritative copy per run, and re-check shared files before trusting them. The same run also lost work permanently. A 61-hit deep-research task from 2026-08-16 could never be imported, and the task itself later disappeared.

**`codex-sol` — the review-gate failure, and the discipline it forced.** Every one of its three review gates first tried the Codex CLI, and every one failed with an account usage-limit error, so all three fell back to the Cursor agent in read-only mode. That fallback still did the job, and this run's Phase 4 review is the single most valuable artifact in the folder. It treated NotebookLM as a witness to cross-examine rather than as an oracle. It found subgroup coefficients sold as headline effects, figures belonging to a different paper, and numbers absent from the cards entirely. It also audited its own earlier counts and cut them.

**The empty-record failure runs in both directions.** The notebook does not only invent. It also denies sources that exist. Asked about Tinder's two-tower P(Match) work, it answers "not in sources," although a full extraction card for that work exists with a notebook source identifier. The 2021 OkCupid voter-and-votee post behaves the same way. Both are Medium-hosted pages, and both ingest as records with no readable body. A "not in sources" answer is therefore evidence about the ingest, not about the literature.

**What changed, across all three.** The belief that a retrieval notebook over 140 sources is a reliable citation oracle did not survive contact with the corpus. Two things replaced it. Read the actual document when the claim carries a number. Run an adversarial review that is allowed to delete a fluent answer.

---

## The arc in one sentence

The field moved from *score the viewer*, to *score both directions*, to *clear the market under capacity*, to *change the product rules too*, to *stop counting matches and start counting retention*, then out of the simulator onto live dating platforms in 2023, and finally to a 2026 field test that improved congestion-adjusted matching and returned a null on conversation. The survey that assembled this arc learned the same thing three separate times, from three different tool failures. A retrieval notebook is a witness to cross-examine, not an oracle to quote.

## Standing direction

1. Add a reciprocal term that conditions on the other side's remaining reply capacity. Tinder reports A/B testing this shape as P(Match) against P(Like), with +6.5% match rate and +22% match volume for P(Match), against +3.8% swipe-right rate for P(Like). Hinge reports a double-digit increase in matches from an updated model that predicts mutual compatibility. Both figures come from company blog posts rather than peer review.
2. Put an explicit allocation layer above the score. Start with LiJAR-style soft boost and penalty behind a relevance floor, because it is the only live production A/B result in the corpus. Treat exposure-constrained deferred acceptance as the dating-native target design, and expect it to move matching before it moves conversation.
3. Keep like caps, batch size, initiation rules, and scarce signals inside the same design space as the model.
4. Replace swipe-rate north stars with match distribution, wasted-like rate, conversations, and two-sided retention. Report effects separately for sender-constrained, receiver-constrained, and balanced segments.
5. Do not test any of the above on a user-split A/B. Use geographic, cluster, or two-sided randomization.

## Load-bearing caveats to carry forward

- No study in this corpus validates the whole chain in one dating system. The strongest field result improves congestion-adjusted matching, and returns a null on conversation.
- Capacity has no agreed definition. The corpus uses hard budgets, forecast demand, vacancy, and equilibrium outside options, and none is calibrated to a measured reply capacity.
- Most transferable mechanisms come from markets with renewable supply — jobs, music, listings, rides. They transfer only after "item availability" is replaced by a person's scarce reply bandwidth.
- Synthetic and real results diverge sharply for the same method. Transferable utility flattens the Gini dramatically in simulation and barely at all on the real dating table in Act 2.
- Repeated searches found none of the following, as of 2026-08-20: a dating-log off-policy evaluation, a Bumble engineering ranking source, an official Chinese dating-ranking engineering source. These are corpus-level nulls, not proof of non-existence.
- The CyberAgent RecSys 2023 and RecSys 2024 papers are shared with Survey 3. If both surveys are used together, do not count them twice.
- The 2023 Chen, Hsieh and Lin field experiment is cited by three papers in this corpus, but no run read it directly. Read the published article before making any claim about which work first field-tested this idea.
- The Rios, Saban and Zheng assortment work is potentially the largest reported dating field result in this corpus, and its identity is unresolved. The year appears as M&SOM 2022 in one place and M&SOM volume 25, issue 4, 2023 in another. The reported lift appears as 25% or more, at least 27%, and 40%. The ingested PDF is a different manuscript, so nobody read the paper itself. Do not cite this work until someone opens the published article.
- Several citations still need a version decision before external use: Fong's working paper against the Marketing Science 2024 version, the Fong author-surname question, and the working-paper versions cited for Halaburda, Kanoria-Saban, Arnosti and Ashlagi.
