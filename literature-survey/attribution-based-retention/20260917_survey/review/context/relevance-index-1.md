# Relevance index 1/4 — Project Relevance sections of all cards (generated)

### User state-based notification volume optimization
`2020_PinterestEngBlog_NotificationVolumeOptimization_User-State-Based-Notification-Volume-Optimization.md`
**Source:** https://medium.com/pinterest-engineering/user-state-based-notification-volume-optimization-7764118f73ff | **Retrieved via:** jina proxy (direct WebFetch returned 403) | **Year / venue:** 2020-04-24 (item metadata listed "2020"), Pinterest Engineering (Medium) | **Authors / team:** Arun Nedunchezhian (Pinterest) | **Analyzed:** 2026-09-17

- **Answers:** Q2 (adjacent) — ties an individual channel (notifications) to an engagement/retention proxy (WAU/DAU) at the user-segment level, not per-touch.
- **Attributes retention to individual interactions?** partly — ties notification-volume decisions to DAU/WAU outcomes, but at the user-segment/channel-budget level, not to individual in-app actions, and with no explicit causal/selection-bias correction.
- **Transferable components:** engagement-tier segmentation (could map to swipe cohorts by recency/frequency); per-segment objective functions (e.g., dormant vs. engaged users weighted differently in the retention label).
- **Required changes:** needs an actual per-interaction (per-swipe) credit mechanism plus counterfactual/selection-bias correction — Pinterest's approach optimizes aggregate volume per cohort and does not attribute credit to individual actions at all.
- **On last-touch:** not discussed.
- **Transfer rating:** adaptable — the engagement-tier segmentation and per-tier objective design is a reusable framing for differentiating swipe cohorts, but it does not itself solve the fractional-credit or selection-bias problem.

### From Clicks to Conversions: Recommendation for long-term reward
`2020_arXiv_ClicksToConversions_Recommendation-For-Long-Term-Reward.md`
**Source:** https://arxiv.org/pdf/2009.00497 | **NLM source id:** cc6d80d3-4a03-479f-b5fc-eb0d2322dfcb | **Year / venue:** 2020, REVEAL '20 workshop (RecSys) | **Affiliation:** ENS Paris Saclay & Criteo | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2 (directly about attribution, but for conversions, not retention/engagement/days-active)
- **Attributes retention to individual interactions?** No — this models e-commerce conversion attribution, not user retention, engagement, or days-active; it does not touch in-app return behavior at all.
- **Transferable components:** the hidden-state-update mechanism for how a click shifts user intent; the discounting/de-biasing logic that separates causally-incremental clicks from merely-correlated ones; the shift from static bandit to full sequential RL where actions change state.
- **Required changes:** the target outcome must move from a one-time e-commerce conversion event to a daily recurring N7 active-retention indicator; RecoGym's homogeneous ad-click event space needs to become a heterogeneous dating funnel (swipe/like/match/message) with event-specific embeddings; and the mechanism needs to produce explicit per-touch fractional credit rather than a single discount factor on the final click.
- **On last-touch:** This is the paper's central topic — it explicitly names and critiques last-click conversion attribution as an industry billing heuristic that is "not a perfect reward-shaping mechanism," biased toward clicks correlated with, not causing, conversions; it proposes a discounting alternative as a fix.
- **Transfer rating:** adaptable — the clearest and most directly on-topic articulation in this batch of *why* last-touch/last-click attribution is biased, though its fix (a single discount factor under a simulation-only, one-shot-conversion setting) needs real extension to fractional, multi-day, multi-event dating-platform credit.

### How Airbnb Measures Future Value to Standardize Tradeoffs
`2021_AirbnbEngBlog_FutureIncrementalValue_How-Airbnb-Measures-Future-Value-To-Standardize-Tradeoffs.md`
**Source:** https://medium.com/airbnb-engineering/how-airbnb-measures-future-value-to-standardize-tradeoffs-3aa99a941ba5 | **Retrieved via:** jina proxy (direct WebFetch returned 403) | **Year / venue:** 2021-07-13 (item metadata listed "n.d."), Airbnb Engineering (Medium) | **Authors / team:** Mitra Akhtari, Jenny Chen, Amelia Lemionet, Dan Nguyen, Hassan Obeid, Yunshan Zhu | **Analyzed:** 2026-09-17

- **Answers:** Q2 (adjacent) — closest published analogue found to "attributing a long-horizon outcome to individual actions" via observational causal inference, though the outcome is revenue/bookings, not N7 retention or days-active.
- **Attributes retention to individual interactions?** partly — attributes long-term incremental value to discrete platform actions, not specifically to in-app swipe-level interactions or to retention/days-active.
- **Transferable components:** the propensity-score-matching pipeline that builds a counterfactual "would-have-happened-anyway" comparison group directly targets the project's selection-bias weakness; common-support trimming; two-stage match-then-compare architecture.
- **Required changes:** swap the outcome metric to N7 active-or-not; move the unit from discrete named actions to individual swipe/like/match events; add fractional splitting across multiple interactions in a user history (FIV credits one action type at a time, not a sequence); handle two-sided cannibalization analogous to match/conversation effects on both users.
- **On last-touch:** not explicitly named, but PSM is implicitly a rebuttal to naive/last-touch-style crediting — it exists precisely to strip out the "users who did X selected into doing so" bias that a last-touch label would import wholesale.
- **Transfer rating:** adaptable — the PSM counterfactual-matching methodology directly targets the same "swipes that would have happened anyway" selection-bias problem the project's baseline suffers from, though it must be re-scoped from discrete actions to per-swipe fractional credit.

### Improving Instagram notification management with machine learning and causal inference
`2022_MetaBlog_IGNotif_Instagram-Notification-Causal-Management.md`
**Source:** https://engineering.fb.com/2022/10/31/ml-applications/instagram-notification-management-machine-learning/ | **NLM source id:** e535b463-dc13-4f2f-af1b-a4654264ce7d | **Year / venue:** 2022, Meta engineering blog | **Affiliation:** Meta, Instagram Notifications Systems Team (author: Nailong Zhang) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2 direct (as an attribution-adjacent, causal-uplift precedent) and Q1-adjacent (an industry causal/uplift approach, though notification-specific rather than a general attribution framework).
- **Attributes retention to individual interactions?** no — it attributes an activeness outcome to a single binary notification decision (send vs. drop), not to a sequence of heterogeneous in-app interactions; there is no fractional credit-splitting across multiple past actions.
- **Transferable components:** the core causal-uplift reframing — replace "probability of action" (swipe-analogous to CTR) with "incremental probability of N7 retention caused by showing this candidate" — is directly the mental model the project needs; the 50/50 randomized holdout for generating unconfounded training labels is a direct, actionable recipe for addressing the stated selection-bias weakness; the online quantile-calibration trick is a reusable serving-time technique for stabilizing a score-based decision threshold.
- **Required changes:** extend from a single independent binary decision (send/drop one notification) to fractional credit assignment across a multi-touch, multi-day sequence of heterogeneous events (swipe → match → message); the uplift here is a single-shot instantaneous treatment effect, whereas the dating platform needs credit distributed across many earlier touches contributing to one later N7 outcome.
- **On last-touch:** not discussed by name, but the paper's critique of CTR models directly parallels the project's critique of last-touch: both over-credit actions taken by users who were already going to be active/engage regardless of the specific action, i.e., both fail to net out the "would have happened anyway" counterfactual.
- **Transfer rating:** adaptable — the causal-uplift framing and randomized-holdout debiasing recipe are directly reusable design principles, but the method itself operates on a single independent binary decision, not a multi-touch fractional-credit sequence.

### 
`2023_KDD_ImpatientBandits_Optimizing-Recommendations-Long-Term-Without-Delay.md`
**Source:** https://arxiv.org/pdf/2307.09943.pdf | **NLM source id:** efd1746f-02ac-4f6a-8849-446ff29ee4e2 | **Year / venue:** KDD 2023 (arXiv 2307.09943) | **Authors / affiliation:** Thomas M. McDonald (Univ. of Manchester, internship at Spotify), Lucas Maystre, Mounia Lalmas, Kamil Ciosek (Spotify), Daniel Russo (Columbia University & Spotify) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2, direct (an industry paper — Spotify — explicitly about forecasting a delayed, retention-like outcome from early interaction signals, cited by the survey as "Q2 direct").
- **Attributes retention to individual interactions?** No — forecasts population/item-level delayed engagement (stickiness) from early aggregate activity traces; does not attribute retention to a specific user's individual historical interactions (swipes/likes), and explicitly integrates out user-level heterogeneity in its core (non-contextual) model.
- **Transferable components:** intermediate-outcome/trace forecasting (using early post-exposure signals to predict a delayed N7-style outcome without waiting the full window) is highly relevant; the Bayesian filter over partial traces and meta-learned prior/noise covariances that encode how predictive early signals are of later ones; Thompson-sampling exploration under delayed reward.
- **Required changes:** move from a non-contextual, per-item bandit to a contextual, per-user multi-touch attribution model; expand the homogeneous daily-activity trace to heterogeneous interaction types (swipe/like/match/message); replace the single terminal 60-day cumulative reward with a recurring daily N7 binary retention target evaluated on rolling reference dates.
- **On last-touch:** does not name last-touch/last-click explicitly, but its central empirical finding — that a short-term proxy (day-two return) tracks well briefly then plateaus at high regret because it's misaligned with the true long-term goal — is a direct structural argument against the production baseline's late-only/most-recent-swipe credit rule.
- **Transfer rating:** adaptable — the progressive-feedback/early-signal-forecasting machinery is directly reusable for early N7-retention prediction, but attributing that retention to specific prior swipes requires moving well beyond this paper's non-personalized, single-item bandit framing.

### Round 2: A Survey of Causal Inference Applications at Netflix
`2023_NetflixTechBlog_CausalInferenceSurveyRound2_Round-2-A-Survey-of-Causal-Inference-Applications-At-Netflix.md`
**Source:** https://netflixtechblog.com/round-2-a-survey-of-causal-inference-applications-at-netflix-fd78328ee0bb | **Retrieved via:** attempted WebFetch (403 Forbidden) and jina proxy (also blocked — page required JS/cookies, no content returned) | **Year / venue:** ~2023, Netflix Tech Blog | **Authors / team:** unknown (not verified) | **Analyzed:** 2026-09-17

- **Answers:** unknown — likely Q2-adjacent based on title ("causal inference applications," a survey format, at a company known for engagement/retention modeling), but unverified.
- **Attributes retention to individual interactions?** unknown — not verified.
- **Transferable components:** unknown — not verified.
- **Required changes:** unknown — not verified.
- **On last-touch:** unknown — not verified.
- **Transfer rating:** background (default, unverified) — no confirmed content; recommend a manual retry (e.g., browser fetch or Wayback Machine) if this source is needed for the survey.

### Interpretable User Retention Modeling in Recommendation
`2023_RecSys_IURO_Interpretable-User-Retention-Modeling.md`
**Source:** RecSys 2023 PDF (no URL provided) | **NLM source id:** 6e3b6f55-e08a-4e8e-9159-0deefceea5c9 | **Year / venue:** 2023, RecSys (best short paper) | **Affiliation:** Northeastern University (Shenyang, China) and WeChat/Tencent (Beijing, China) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2 direct — this is the closest match found to "attribution of retention to individual in-app interactions" with a working, deployed method.
- **Attributes retention to individual interactions?** yes — computes a per-interaction (per-item) retention score s_ui for every item in a user's history via a learned scorer, aggregated with attention, and validated online.
- **Transferable components:** the per-interaction UI retention scorer and attention-aggregation architecture as a template for a per-swipe scorer; the activity-weighted supervision term W_u as a direct mechanism for down-weighting the selection-bias effect of naturally active users; the contrastive "aha item" mechanism to avoid spreading credit uniformly; RMIL's use of future behavior as a causal anchor, directly analogous to using later matches/conversations to guide which earlier swipes get credit.
- **Required changes:** extend the homogeneous item-click UI scorer to heterogeneous event types (swipe, match, message) via event-type embeddings; move from a single next-3-day binary/regression target to a recurring daily N7 window; validate whether the linear online blending (α·ctr + (1−α)·s_ui) generalizes to a ranking model that must predict incremental retention value rather than blend with CTR.
- **On last-touch:** directly relevant — the paper shows uniform/naive weighting across the interaction history (IURO-AVG) performs far worse than attention-weighted attribution (AUC 0.5838 vs 0.8445), demonstrating empirically that retention credit is highly non-uniform and that non-last-touch "aha items" earlier in the sequence are often the true drivers — a direct empirical argument against last-touch-style attribution.
- **Transfer rating:** adaptable — architecture and bias-handling mechanisms transfer well, but must be extended from homogeneous content clicks to heterogeneous swipe/match/message events and from a static 3-day target to a recurring N7 window.

### Optimizing for the Long-Term Without Delay (Impatient Bandits)
`2023_SpotifyBlog_ImpatientBandit_Optimizing-Long-Term-Without-Delay.md`
**Source:** https://research.atspotify.com/2023/07/optimizing-for-the-long-term-without-delay | **NLM source id:** f9864eeb-df64-4530-9ca6-92d2063153a9 | **Year / venue:** 2023, Spotify Research blog (underlying paper: McDonald et al., KDD 2023, "Impatient Bandits: Optimizing for the Long-Term Without Delay") | **Affiliation:** Spotify Research | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** neither directly — this is about the cold-start/delayed-reward learning problem for ranking new items, not attribution of an outcome to which past user actions caused it; only tangentially related to Q2 via its "intermediate outcome as an early signal of a delayed outcome" idea.
- **Attributes retention to individual interactions?** no — it forecasts a delayed population-level item reward from early intermediate signals; it does not decompose an observed outcome into credit for specific prior user actions, and it explicitly integrates out user-level (i.e., per-swipe) heterogeneity.
- **Transferable components:** the core "trace" idea — using early post-swipe/post-match signals (e.g., day-1 to day-3 activity) as a leading indicator to predict N7 retention sooner, reducing label-delay/cold-start pain for a ranking model that needs N7 labels quickly; Bayesian belief updating as data progressively arrives could inform how a candidate-scoring model updates its estimate of a swipe's eventual retention value before the full 7-day window completes.
- **Required changes:** move from a non-contextual, item-level, homogeneous daily-engagement trace to a per-user, per-swipe, heterogeneous-event (swipe/match/message) attribution model; this paper does not do credit splitting at all, so essentially the entire attribution mechanism would need to be built on top of its label-timing idea, not borrowed from it.
- **On last-touch:** not discussed; the paper's relevant critique is of short-term proxies (clicks/streams) as misaligned surrogates for long-term outcomes, conceptually parallel to (but not the same as) the project's critique of last-touch attribution.
- **Transfer rating:** background — useful only as a label-timing/cold-start idea (early signals predict delayed N7 outcome), not as an attribution or credit-assignment method; the project's core need (fractional per-swipe credit, selection-bias correction) is out of scope for this paper.

### User Retention-oriented Recommendation with Decision Transformer
`2023_WWW_DT4Rec_User-Retention-Oriented-Recommendation-Decision-Transformer.md`
**Source:** https://arxiv.org/html/2303.06347v1 | **NLM source id:** 340177ed-c957-4263-a5da-79b22e29b3a9 | **Year / venue:** WWW 2023, Austin | **Affiliation:** City University of Hong Kong, Wuhan University, Baidu Inc. | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2 adjacent (no explicit per-interaction attribution, but retention-conditioned sequence modeling)
- **Attributes retention to individual interactions?** No — DT4Rec is an autoregressive policy-generation model; it conditions on a return-to-go prompt but never decomposes sequence-level retention into per-item/per-swipe fractional credit, nor computes counterfactual removal effects.
- **Transferable components:** return-to-go sequence prompting (recasting N7 active-days as a future cumulative target); auto-discretized reward prompts; weighted contrastive policy learning using low-retention sequences as negatives.
- **Required changes:** to get fractional per-swipe credit, one would need to extract Transformer attention weights or run counterfactual leave-one-out prompt masking — DT4Rec itself only outputs next-item recommendations, not credit labels; it also assumes a single homogeneous action type, so heterogeneous swipe/match/message event encoders would need to be added.
- **On last-touch:** Not named explicitly, but the paper's central argument — that immediate/myopic feedback optimization fails to capture retention, which depends on multi-step cumulative context — is a direct critique of last-touch-style crediting.
- **Transfer rating:** adaptable — the return-to-go framing and contrastive training against low-retention sequences are reusable ideas, but the model itself must be repurposed (via attention extraction or ablation) to produce credit labels rather than recommendations.

### Reinforcing User Retention in a Billion Scale Short Video Recommender System
`2023_WWW_RLUR_Reinforcing-User-Retention-Billion-Scale-Short-Video-Recommender.md`
**Source:** https://arxiv.org/pdf/2302.01724 | **NLM source id:** 21bf4037-1292-40df-a0db-714075d0f41c | **Year / venue:** WWW 2023, Austin | **Affiliation:** Kuaishou Technology | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2 adjacent
- **Attributes retention to individual interactions?** Partly — a Retention Critic estimates step-wise expected retention value via TD learning, so each request gets an implicit value estimate, but RLUR is an online policy-optimization framework, not an offline credit-decomposition model that produces per-swipe fractional labels.
- **Transferable components:** framing N7 as minimizing/predicting a time-to-return target; uncertainty normalization (dividing observed by predicted return time) to strip organic/exogenous noise; activity-based cohort stratification to prevent power-swiper selection bias; dual critic (long-term + immediate) architecture.
- **Required changes:** RLUR's action space is a per-request ensembling weight vector over homogeneous video-scoring models — a dating platform needs per-candidate-profile exposure evaluation across heterogeneous funnel actions (swipe/match/message) with corresponding state/event encoders, and the session-gap reward must be re-anchored to a rolling daily N7 active indicator.
- **On last-touch:** Not named explicitly, but the paper states outright that retention "is difficult to decompose... to each item," which is the core argument against assigning full credit to the most recent (last-touch) swipe.
- **Transfer rating:** adaptable — the uncertainty-normalization and cohort-stratification debiasing techniques are directly reusable for isolating incremental retention lift from organic swiping.

### 
`2024_KDD_CRRS_Revisiting-Reciprocal-Recommender-Systems-Metrics-Formulation-Method.md`
**Source:** https://arxiv.org/pdf/2408.09748.pdf | **NLM source id:** 54ce1645-9722-4202-9da0-c5145e6ed871 | **Year / venue:** KDD 2024 (arXiv 2408.09748) | **Authors / affiliation:** Chen Yang, Sunhao Dai, Yupeng Hou, Wayne Xin Zhao*, Jun Xu, Yang Song, Hengshu Zhu — Nanbeige Lab/BOSS Zhipin; Gaoling School of AI, Renmin University of China; UC San Diego; Career Science Lab, BOSS Zhipin (*corresponding) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2 (models a dating-platform recommendation causally, though the outcome is match, not N7 retention).
- **Attributes retention to individual interactions?** No — attributes bilateral match probability to a recommendation-treatment pair, not retention/active-days to swipe-level interactions over time.
- **Transferable components:** bilateral potential-outcome treatment formulation (distinguishing one-sided vs. mutual exposure) directly maps onto distinguishing a one-sided swipe from a mutual match; the vacant-slot IsMax reranking (opportunity cost of showing candidate B vs. an alternative) is directly relevant to ranking-time incremental-value scoring; redundant-exposure filtering.
- **Required changes:** re-anchor the potential outcome from a single match event to a recurring daily N7 retention indicator; extend the binary bilateral treatment (T_A,T_B) to a full heterogeneous, temporally-ordered interaction sequence (swipe→like→match→message) rather than a single recommendation decision; move from pairwise static scoring to per-swipe sequence-level credit across rolling windows.
- **On last-touch:** does not discuss last-touch/last-click directly; instead critiques single-sided, independent evaluation (the structural analogue of ignoring the other side's touch) for double-counting and for missing that bilateral recommendations jointly cause a match.
- **Transfer rating:** adaptable — the causal bilateral-treatment and vacant-slot-opportunity-cost ideas transfer to ranking-time incremental value estimation, but the paper targets one-shot match probability, not multi-touch fractional retention credit over a swipe sequence.

### Modeling User Retention through Generative Flow Networks
`2024_KDD_GFN4Retention_Modeling-User-Retention-Generative-Flow-Networks.md`
**Source:** https://arxiv.org/pdf/2406.06043 | **NLM source id:** 5884e0ba-ca58-4eed-826d-7764d27bbccd | **Year / venue:** KDD 2024, Barcelona | **Affiliation:** City University of Hong Kong, Kuaishou Technology, Nanyang Technological University | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2 (published attribution of retention to individual interactions)
- **Attributes retention to individual interactions?** Yes — the Detailed Balance flow-matching objective explicitly back-propagates the end-of-session retention reward to every intermediate step, and the ablation shows non-last steps carry significant retention "flow."
- **Transferable components:** Detailed Balance flow-matching for retention attribution; integrated reward design combining immediate + long-term signal; Transformer+context-detection user-state encoder.
- **Required changes:** GFN4Retention assumes homogeneous per-step item-list actions and a single session-boundary return gap; a dating platform needs heterogeneous action-type embeddings (swipe/match/message) in the forward/backward flows, and the terminal flow must target a rolling daily N7 indicator instead of a one-time session return gap.
- **On last-touch:** The paper states retention has no clear relation to any single prior recommendation step, and its ablation proves that intermediate (non-last) steps carry meaningful attributed flow — a direct argument against last-touch-only crediting.
- **Transfer rating:** adaptable — the flow-matching attribution mechanism is the closest thing in this batch to a genuine per-step credit-assignment method, but it needs rework for heterogeneous, daily-recurring dating-app interactions.

### Estimating long-term outcome of algorithms (Long-term Off-Policy Evaluation and Learning)
`2024_SpotifyBlog_LongTermOutcome_Estimating-Long-Term-Outcome-Of-Algorithms.md`
**Source:** https://research.atspotify.com/2024/05/estimating-long-term-outcome-of-algorithms | **NLM source id:** 36958832-a712-4f91-8e1f-65d73cdca0ce | **Year / venue:** 2024, Spotify Research blog (underlying paper: WWW 2024) | **Affiliation:** Spotify Research | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q1 (recent, 2024, industry-published long-term evaluation method) — not Q2, since it evaluates policies, not individual interactions.
- **Attributes retention to individual interactions?** No — LOPE estimates the aggregate long-term outcome of an entire algorithm/policy from short-term experiment data; it does not decompose retention into per-swipe or per-touch fractional credit.
- **Transferable components:** the surrogate-effect/action-effect decomposition — separating "this candidate got a lot of short-term swipes" (surrogate) from "this candidate has real incremental retention value" (action effect) — maps directly onto the platform's "would have swiped anyway" selection-bias problem; counterfactual/importance weighting of short-term signals to reduce label variance.
- **Required changes:** shift the unit of analysis from policy-level evaluation to per-touch fractional credit; incorporate heterogeneous touchpoints (swipe/match/message) into the short-term surrogate reward; re-anchor to a rolling daily N7 retention target rather than a single long-horizon evaluation window.
- **On last-touch:** Not named explicitly, but the paper's critique of the surrogacy assumption — that short-term signals alone (which is what last-touch attribution effectively uses) can badly misrepresent long-term causal impact, by up to 71% higher MSE — is functionally the same critique the platform has of last-touch attribution.
- **Transfer rating:** adaptable — the surrogate/action-effect decomposition is conceptually the best available tool in this batch for separating genuine incremental retention value from "engaged users swipe more anyway," even though it operates at policy level rather than per-swipe.

