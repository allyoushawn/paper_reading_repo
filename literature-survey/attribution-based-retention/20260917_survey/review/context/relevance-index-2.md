# Relevance index 2/4 — Project Relevance sections of all cards (generated)

### Stratified Expert Cloning for Retention-Aware Recommendation at Scale
`2025_CIKM_SEC_Stratified-Expert-Cloning-Retention-Aware-Recommendation.md`
**Source:** https://arxiv.org/html/2504.05628v2 | **NLM source id:** 3428b363-efef-4206-9892-dcc167d97303 | **Year / venue:** CIKM 2025, Seoul | **Affiliation:** Kuaishou Technology, Peking University | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** neither directly — SEC is a policy-cloning method, not an attribution or industry-attribution paper (weakly Q2-adjacent by exclusion).
- **Attributes retention to individual interactions?** No — SEC clones expert state-action trajectories via behavior-cloning loss; it never isolates or scores the marginal contribution of an individual swipe/action.
- **Transferable components:** multi-level retention/activity stratification (mirrors the platform's own engaged-vs-casual user segmentation); Action Entropy Regularization to prevent the ranker from collapsing onto a narrow candidate set.
- **Required changes:** SEC would need to be replaced by, or paired with, an explicit credit-assignment layer (e.g., a causal/counterfactual model or attention-weight extraction) since it only clones policies; it also treats actions homogeneously and optimizes a fixed 7-day window rather than rolling daily N7 labels, so funnel-stage (swipe→match→conversation) modeling and rolling time-decay would need to be added.
- **On last-touch:** Not discussed — the paper compares against RL/GFN baselines on immediate-vs-long-term optimization, not attribution heuristics.
- **Transfer rating:** background — useful for the stratification and diversity-regularization ideas, but it is not itself an attribution mechanism and cannot directly produce per-swipe fractional credit.

### Smarter promotions with causal machine learning
`2025_DoorDashBlog_CausalPromotions_Smarter-Promotions-With-Causal-Machine-Learning.md`
**Source:** https://careersatdoordash.com/blog/doordash-smarter-promotions-with-causal-machine-learning/ | **Retrieved via:** jina proxy (direct WebFetch returned 403) | **Year / venue:** 2025-12, DoorDash Engineering Blog | **Authors / team:** Kun Hu, Muxi Xu (DoorDash) | **Analyzed:** 2026-09-17

- **Answers:** Q1 — a modern (2025) industry causal-uplift approach directly analogous to the "swipes that would have happened anyway" selection-bias problem named in the project.
- **Attributes retention to individual interactions?** partly — attributes incremental purchase (not retention) to an individual treatment (promotion), at user level rather than per-touch.
- **Transferable components:** Double ML / heterogeneous treatment-effect framework to separate incremental from inevitable outcomes; continuous-treatment modeling; constrained allocation optimization.
- **Required changes:** swap outcome from binary purchase to N7 retention; move treatment unit from promotion-received to individual swipe/like/match; add temporal/sequence handling and fractional (not single-treatment) credit splitting across multiple interactions.
- **On last-touch:** not directly critiqued, but the framework's premise — that naive credit overpays for "always-buyers" — mirrors this project's critique of last-touch's selection-bias weakness.
- **Transfer rating:** adaptable — its causal framework for isolating incremental effect from users who would have converted anyway maps directly onto the project's stated selection-bias weakness, pending reframing to interaction-level, multi-touch, retention outcomes.

### Optimizing DoorDash's Marketing Spend with Machine Learning
`2025_DoorDashBlog_MarketingSpendML_Optimizing-Marketing-Spend-With-Machine-Learning.md`
**Source:** https://careersatdoordash.com/blog/optimizing-marketing-spend-with-ml/ | **Retrieved via:** jina proxy (direct WebFetch returned 403) | **Year / venue:** item metadata lists 2025-04; page byline shows July 31, 2020 — date discrepancy, flagged not resolved | **Authors / team:** Aman Dhesi, Robert B. Kaspar (DoorDash) | **Analyzed:** 2026-09-17

- **Answers:** Q1 — confirms the tag's flagged claim: DoorDash explicitly uses a **modified last-touch attribution** model, at the channel level.
- **Attributes retention to individual interactions?** no — attributes new-user acquisition conversion to a marketing channel, not retention to an in-app interaction.
- **Transferable components:** synthetic-data augmentation for sparse/noisy interaction data; general cost-curve / budget-allocation framing.
- **Required changes:** unit of credit must move from channel to individual in-app interaction; outcome must move from acquisition conversion to N7 retention; last-touch must be replaced by a fractional/causal credit scheme.
- **On last-touch:** explicitly confirmed — DoorDash uses "modified last-touch attribution" at the channel level as the uncritiqued foundation for its cost curves.
- **Transfer rating:** background — confirms modified last-touch is still current industry practice (useful negative evidence for Q1) but offers no fractional-credit or bias-correction method to transfer.

### Update on Plans for Privacy Sandbox Technologies (Attribution Reporting API retired)
`2025_GoogleBlog_PrivacySandboxUpdate_Attribution-Reporting-API-Retired.md`
**Source:** https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies | **Retrieved via:** NotebookLM source da122d2b-c07a-4520-93b1-90e48a2a77aa | **Year / venue:** 2025-10, Google Blog | **Authors / team:** Anthony Chavez (VP, Privacy Sandbox, Google) | **Analyzed:** 2026-09-17

- **Answers:** Q1 (context only)
- **Attributes retention to individual interactions?** no — this is a web ad-measurement policy announcement, not a retention/interaction attribution method.
- **Transferable components:** none at the modeling level; only macro context that browser-based multi-touch ad-attribution infrastructure is being wound down industry-wide.
- **Required changes:** N/A — would need an entirely separate in-app causal/sequence attribution approach.
- **On last-touch:** not discussed; the retired API concerned privacy-preserving multi-touch ad conversion measurement, not a last-touch vs. multi-touch comparison.
- **Transfer rating:** background — informs the Q1 industry landscape (browser ad-attribution APIs being retired in favor of open standards) but offers no method transferable to per-swipe retention credit.

### The Surrogate Index: Combining Short-Term Proxies to Estimate Long-Term Treatment Effects More Rapidly and Precisely
`2025_REStud_SurrogateIndex_Combining-Short-Term-Proxies-Long-Term-Treatment-Effects.md`
**Source:** https://arxiv.org/pdf/1603.09326.pdf | **NLM source id:** fa0d650a-9370-4fff-bba9-f0fb2529d026 | **Year / venue:** REStud 2025 (arXiv 1603.09326, updated Aug 2024) | **Authors / affiliation:** Susan Athey (Stanford GSB & Economics, NBER), Raj Chetty (Harvard Economics, NBER), Guido W. Imbens (Stanford, NBER), Hyunseung Kang (University of Wisconsin-Madison, Statistics) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2 background (foundational surrogate/proxy-outcome methodology relevant to modeling delayed retention).
- **Attributes retention to individual interactions?** No — estimates the population-level average treatment effect of a binary macro intervention using short-term proxies; not a multi-touch or per-interaction attribution method.
- **Transferable components:** The core idea — combine several early post-swipe signals (day 1-6 activity, matches, message replies) into a single surrogate index that predicts N7 retention without waiting the full 7 days — is directly reusable for early/fast retention-label construction; the multi-surrogate "anti-gaming" property (combining swipes with downstream matches/conversations) is conceptually the same fix needed against "credits swipes that would have happened anyway" if one surrogate alone (e.g., swipe count) were used; the doubly robust influence-function estimator is a reusable bias-robust estimation pattern.
- **Required changes:** This is a population ATE estimator for a single binary treatment, not a per-touch fractional-credit mechanism — would need to be reframed around a sequence of many candidate-profile "treatments" (each swipe) rather than one program assignment; the outcome must become the recurring daily N7-active binary, and the surrogate vocabulary must expand to heterogeneous event types (swipe/match/message) with time-gap structure.
- **On last-touch:** Not discussed directly — but the paper's core empirical point (a single short-term proxy like clicks alone is exploitable/misleading, i.e., "clickbait") is structurally the same critique the dating platform would level against giving 100% credit to the single last swipe.
- **Transfer rating:** adaptable — the surrogate-index construction and multi-signal anti-gaming logic transfer well conceptually to fast/robust retention labeling, even though the underlying estimand (single binary-treatment ATE) is not itself a multi-touch attribution mechanism.

### Coarse-to-fine Dynamic Uplift Modeling for Real-time Video Recommendation
`2025_RecSys_CDUM_Coarse-to-fine-Dynamic-Uplift-Modeling.md`
**Source:** https://arxiv.org/pdf/2410.16755.pdf | **NLM source id:** 0cd04f39-39ef-4623-9cea-98612bd68d7c | **Year / venue:** RecSys 2025 | **Authors / affiliation:** Chang Meng, Chenhao Zhai, Xueliang Wang, Shuchang Liu, Xiaoqiang Feng, Lantao Hu, Han Li (Kuaishou Technology); Chenhao Zhai, Xiu Li (Tsinghua Shenzhen International Graduate School); Kun Gai (Unaffiliated) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** both
- **Attributes retention to individual interactions?** no — CDUM estimates request-level individual treatment effects for a macro strategy decision (enable/disable a duration-bucket treatment), not fractional credit across a user's individual past swipes/likes/matches.
- **Transferable components:** the coarse-to-fine two-stage paradigm (offline long-term-preference model + online real-time-interest model correcting it); the guidance/indicator treatment-refine mechanism for handling multiple heterogeneous treatments without gradient interference; use of unbiased LT7/LT30-style metrics as validation targets.
- **Required changes:** move from macro per-request bucket-enablement decisions to micro-level per-interaction sequence attribution with counterfactual credit differentials; replace average-pooled interaction embeddings with event-type-aware (swipe/like/match/message) sequence modeling; re-anchor the outcome to a daily-recurring rolling N7 retention target rather than a single treatment window.
- **On last-touch:** does not name last-touch/last-click explicitly, but critiques static offline-feature uplift models and non-causal heuristics for failing to isolate true incremental effect from organic baseline activity — directly analogous to the selection-bias critique of last-touch attribution.
- **Transfer rating:** adaptable — a request-level causal uplift framework, not a multi-touch attribution model, but its two-stage offline/online design and bias-aware treatment effect estimation are strong building blocks for retention-credit modeling.

### AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems
`2025_WWW_AURO_Adaptive-User-Retention-Optimization-RL.md`
**Source:** https://arxiv.org/pdf/2310.03984.pdf | **NLM source id:** ad961918-6d05-4369-a28d-7180ccf96629 | **Year / venue:** WWW 2025 (ACM Web Conference 2025) | **Authors / affiliation:** Zhenghai Xue (NTU Singapore), Qingpeng Cai* (Kuaishou Technology, corresponding), Bin Yang, Lantao Hu, Peng Jiang (Kuaishou Technology), Kun Gai (Unaffiliated), Bo An (NTU Singapore & Skywork AI) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2
- **Attributes retention to individual interactions?** partly — AURO learns Q(s,a)/V(s) to value recommendation actions toward retention, but does not compute explicit fractional multi-touch attribution credit across historical swipe/like/match events; it's a policy-optimization framework, not an attribution model.
- **Transferable components:** value-based state abstraction φ(s) for detecting engagement-state shifts (e.g., highly-active vs. churn-risk users) that could gate candidate-profile scoring; guarded/rejection-sampled exploration to avoid surfacing low-value candidates that risk churn.
- **Required changes:** convert from online RL policy control to offline supervised sequence attribution — Q-values/state abstractions would need to become counterfactual credit differentials per swipe; action space must move from continuous scoring vectors to heterogeneous discrete touch types (swipe, like, match, message).
- **On last-touch:** does not explicitly critique last-touch/last-click attribution, but shows myopic optimization of immediate feedback (clicks/likes) fails to maximize long-term retention and can increase churn — supporting the case against last-touch-only credit.
- **Transfer rating:** adaptable — an RL policy-optimization algorithm rather than a multi-touch attribution model, but its value-based state abstraction and guarded Q-estimation are adaptable building blocks for valuing candidate-profile impact on retention.

### Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems
`2025_arXiv_PinterestSRR_Save-Revisit-Retain-Scalable-Retention-Framework.md`
**Source:** https://arxiv.org/pdf/2511.18013.pdf | **NLM source id:** f7f34e82-7545-4be7-885a-8bdb87041b12 | **Year / venue:** 2025, arXiv 2511.18013 (AAAI 2026) | **Affiliation:** Pinterest Inc. | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2 (partly — direct empirical example of attributing retention-relevant behavior to an individual saved item, though not fractional across a full interaction sequence); not really Q1.
- **Attributes retention to individual interactions?** partly — attributes a specific surrogate outcome (same-item revisit within 0–6 days) to a specific save action, but does not attribute the ultimate DAU/retention outcome fractionally across a full multi-touch history; it is single-touch (save → its own revisit), not multi-touch credit splitting.
- **Transferable components:** the surrogate-attribution pattern (link a candidate-level action to a well-defined, temporally-bounded downstream event) as a template for defining swipe→match/message surrogate labels; adding an auxiliary head to an existing multi-task ranker at zero serving cost; unique-user normalization of popularity features to dampen power-user skew.
- **Required changes:** extend from a single action-pair surrogate (save→revisit on the same item) to a full heterogeneous funnel (swipe→match→message→return) and to fractional credit across multiple candidates rather than a strict same-item link; move from "did this exact item get revisited" to "was next-7-day app-level retention driven by this swipe," which requires distributing credit across many swipes rather than a 1:1 item attribution.
- **On last-touch:** not explicitly discussed; the paper implicitly critiques systems that focus only on immediate in-session engagement (clicks/saves) and ignore multi-day return dynamics, and notes a prior click→revisit two-model approach (Zhang et al. 2021) was too costly to serve — motivating their integrated single-model approach instead.
- **Transfer rating:** adaptable — the surrogate-attribution and zero-cost multi-task-head pattern transfer well, but the method is single-touch item-level attribution, not the fractional multi-touch credit splitting the project needs.

### 
`2025_arXiv_RecAPC_Modeling-Churn-Recommender-Systems-Aggregated-Preferences.md`
**Source:** https://arxiv.org/pdf/2502.18483.pdf | **NLM source id:** 20670606-4205-4316-938c-c86aaaec03b0 | **Year / venue:** 2025, arXiv 2502.18483 | **Authors / affiliation:** Gur Keinan, Omer Ben-Porat — Technion, Israel Institute of Technology | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2 (background/negative case — a 2025 recsys paper studying session engagement under churn, but not attributing multi-day retention to individual interactions).
- **Attributes retention to individual interactions?** No — optimizes cumulative in-session likes before churn; does not perform multi-touch credit assignment or attribute multi-day active-day/retention outcomes to historical interactions.
- **Transferable components:** Bayesian belief tracking over user-persona clusters updated on positive feedback; upper/lower value bounds for pruning candidate sequences by churn risk; the finite-time exploration→exploitation convergence result.
- **Required changes:** would need to shift from *online single-session policy planning* to *offline sequence-level credit attribution*; extend binary like/dislike-terminates-session feedback to heterogeneous multi-stage funnel events where negative feedback (a left swipe) does not end the session; retarget the objective from in-session cumulative likes to a daily-recurring N7 active-retention label.
- **On last-touch:** not discussed at all — the paper neither mentions nor critiques last-touch/last-click attribution.
- **Transfer rating:** background — a well-executed churn/exploration-exploitation POMDP paper adjacent to engagement modeling, but it is a policy-planning method, not an attribution method, and requires substantial reformulation to be relevant.

### Retentive Relevance: Capturing Long-Term User Value in Recommendation Systems
`2025_arXiv_RetentiveRelevance_Capturing-Long-Term-User-Value.md`
**Source:** https://arxiv.org/pdf/2510.07621.pdf | **NLM source id:** 3aa276f2-3423-47de-b659-ac3acf484bdc | **Year / venue:** arXiv 2510.07621, 2025 | **Authors / affiliation:** Saeideh Bakhshi, Phuong Mai Nguyen, Cayman Simpson, Qifan Wang (Meta, Menlo Park); Robert Schiller, Tiantian Xu (Meta, New York); Pawan Kodandapani (Meta, Boston); Andrew Levine (Meta, San Francisco) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2
- **Attributes retention to individual interactions?** partly — predicts a per-item (u,v) forward-looking retention-intent proxy and uses it to boost/demote that item in ranking, but does not perform multi-touch sequence credit attribution (e.g., Shapley/counterfactual path masking) across a user's swipe/like/match/message history.
- **Transferable components:** forward-looking behavioral-intent labels as a stronger ground truth than implicit signals (adaptable to "How likely to return after swiping/matching on this profile?"); CBPS propensity debiasing for power-swipers vs. cold-start users; precision-calibrated boost/demote score adjustment at the ranking stage; the finding that intent proxies are disproportionately valuable for low-signal/cold-start users.
- **Required changes:** extend from single-item intent prediction to multi-touch sequence attribution across a full swipe→like→match→message journey; incorporate heterogeneous dating-funnel touch types rather than homogeneous video views; re-anchor the binary next-day retention target to a rolling N7 active-retention indicator.
- **On last-touch:** does not name last-touch/last-click explicitly, but shows short-term implicit engagement signals are nearly orthogonal to actual return intent (MI<0.15) and fail to predict next-day retention, while alternative retrospective surveys also add nothing — evidence that myopic/implicit touchpoint signals (the same class as last-touch) underperform forward-looking intent measures.
- **Transfer rating:** adaptable — a per-item intent-prediction and ranking-adjustment framework, not a multi-touch attribution model, but its intent-based labeling, debiasing, and calibrated score-adjustment architecture transfer well to candidate-profile retention ranking.

### A Large Scale Heterogeneous Treatment Effect Estimation Framework and Its Applications of Users' Journey at Snap
`2025_arXiv_SnapHTE_Large-Scale-Heterogeneous-Treatment-Effect-Users-Journey-Snap.md`
**Source:** https://arxiv.org/pdf/2512.03060.pdf | **NLM source id:** 59173a97-7b15-4ae3-a813-1e80790cddf1 | **Year / venue:** 2025-12, arXiv:2512.03060, Snap (retrieved paper text carries an unedited "CJO2022" ACM template placeholder venue string, treated as a template artifact rather than the actual venue) | **Authors / affiliation:** Li Shi, Jing Pan, Paul Lo, Jonathan Grotts, Crystal Pan, Ben Thompson, Mattia Fumagalli, Amit Adur — Snap Inc., Santa Monica, CA | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q1 (also touches Q2 via the User Sensitivity application)
- **Attributes retention to individual interactions?** Partly — User Sensitivity estimates incremental engagement/retention-type impact per user from ad-exposure holdouts, but it is a user-level uplift score, not a per-touchpoint/sequence credit decomposition.
- **Transferable components:** T-learner with randomized-holdout debiasing to isolate true incremental lift from organic ("would-happen-anyway") activity; DCN base architecture; incremental (non-catastrophic-forgetting) weekly retraining pipeline; AUUC-based uplift evaluation.
- **Required changes:** Move from a single scalar per-user CATE to per-swipe/per-touchpoint fractional credit; ingest heterogeneous, multi-stage event types (swipe, match, message) with temporal structure rather than static user features; retarget from ad-conversion/engagement-drop to a recurring N7 active-on-day-7 label.
- **On last-touch:** Not addressed directly; the paper's broader critique is that correlated (non-causal) labels generally mislead ranking/targeting systems, which is consistent with the last-touch critique but not phrased that way.
- **Transfer rating:** adaptable — the T-learner/holdout-debiasing and incremental-training machinery transfer well; the credit unit needs to shift from per-user to per-interaction.

### Policy Design for Two-sided Platforms with Participation Dynamics
`2025_arXiv_TwoSidedPolicy_Policy-Design-Two-sided-Platforms-Participation-Dynamics.md`
**Source:** https://arxiv.org/pdf/2502.01792.pdf | **NLM source id:** 7fdbc3ee-d5de-4e48-b7ba-5b4f17b60ed2 | **Year / venue:** ICML 2025 (PMLR 267) | **Authors / affiliation:** Haruka Kiyohara, Sarah Dean (Cornell University); Fan Yao (University of Virginia) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q2
- **Attributes retention to individual interactions?** no — optimizes viewer-subgroup/provider-subgroup exposure allocation for aggregate long-term social welfare under population dynamics; does not attribute retention/engagement/active-days to individual interactions at all.
- **Transferable components:** two-sided participation-dynamics framing (swiper satisfaction and candidate-profile "supply" reinforcing each other); exposure-distributing / "growing the pie" allocation to avoid concentrating exposure on already-popular profiles; the policy-regret vs. population-regret decomposition as a conceptual lens for evaluating short-term vs. long-term costs of an attribution/ranking policy.
- **Required changes:** move entirely from subgroup-level matching-probability optimization to individual per-swipe sequence attribution; replace aggregate viewer-satisfaction/provider-exposure metrics with heterogeneous per-touch event modeling (swipe, like, match, message); re-anchor the welfare objective to a daily-recurring rolling N7 active-retention indicator per user.
- **On last-touch:** does not discuss last-touch/last-click attribution by name, but rigorously shows myopic-greedy policies (which optimize only immediate utility) are optimal only under a narrow linear/homogeneous condition and otherwise cause population collapse — a structural analogue to the critique that last-touch (a myopic heuristic) ignores dynamics beyond the immediate touchpoint.
- **Transfer rating:** background — a control/game-theoretic two-sided marketplace policy-design paper, not an attribution or retention-credit model; useful conceptually (population dynamics, exposure fairness) but not a direct building block for per-swipe credit assignment.

### Highlights of Booking.com's publication in 2025
`2026_BookingAIBlog_2025PublicationHighlights_Highlights-of-Booking-Com-Publication-in-2025.md`
**Source:** https://booking.ai/highlights-of-booking-coms-publication-in-2025-1c1a6deba066 | **Retrieved via:** jina proxy (direct WebFetch returned 403) | **Year / venue:** 2026-01-20, Booking.com (booking.ai Medium blog) | **Authors / team:** multiple (incl. Dmitri Goldenberg, Philipp Hager; roundup of 8 accepted papers) | **Analyzed:** 2026-09-17

- **Answers:** Q1 — represents current (2025–2026) industry practice in causal promotion attribution, adjacent to but not the same problem as retention attribution.
- **Attributes retention to individual interactions?** partly — attributes conversion (not retention/days-active) to promotional touchpoints, and only for converted sessions.
- **Transferable components:** retrospective / "converted-only" estimation to reduce noise; causal uplift framing (references an AddIPW-style estimator) for interference-aware multi-touch settings.
- **Required changes:** replace conversion outcome with N7 retention; cannot rely on "converted-only" filtering since retention labels exist regardless of conversion, and dropping non-matching swipes would reintroduce the very selection bias the project wants removed; extend single-touchpoint promotion credit to a multi-swipe sequence.
- **On last-touch:** not directly discussed in this summary; no explicit comparison to last-touch/last-click.
- **Transfer rating:** adaptable — describes live, large-scale causal promotion-attribution work adjacent to the project's problem, but the "converted-only" simplification runs counter to the project's specific need to also credit non-converting earlier swipes.

### 
`2026_CIKM_SMEO_Sequential-Multimodal-Evidence-Optimization-Product-Media-Ranking.md`
**Source:** https://arxiv.org/pdf/2608.15662.pdf | **NLM source id:** ca9271b9-af43-492f-b3b4-2868d784f2f3 | **Year / venue:** CIKM 2026 (arXiv 2608.15662) | **Authors / affiliation:** Prasenjit Dey, Frank McIntyre, Arnab Sinha — Amazon.com Inc. | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

- **Answers:** Q1 (2026 industrial sequential-evidence/attribution approach for cooperative-asset ranking).
- **Attributes retention to individual interactions?** No — attributes terminal purchase conversion to individual media assets within a single session, not multi-day retention to interactions.
- **Transferable components:** trajectory-utility model over consumed prefixes; PAL position-bias decoupling; variable-depth supervision (train only at observed stopping depth) as a direct fix for the "credits swipes that would've happened anyway" selection-bias weakness; survival-weighted reward-to-go for front-loading high-value candidates; post-hoc Leave-One-Out counterfactual masking for per-touch attribution without dense labels.
- **Required changes:** replace single-session terminal conversion with a daily-recurring N7 retention label; extend homogeneous media tokens to heterogeneous swipe/match/message event types; drop the fixed-first-slot UX constraint (not applicable to a swipe feed).
- **On last-touch:** doesn't name last-touch directly but structurally argues against any position/last-event-only credit — explicitly shows naive last-position or all-prefix supervision misattributes credit to unobserved deep assets or falsely credits early weak assets when truncation is endogenous.
- **Transfer rating:** adaptable — LOO counterfactual masking plus variable-depth/survival-weighted supervision map cleanly onto per-swipe fractional retention credit, but the outcome and touchpoint vocabulary must be rebuilt for a recurring, heterogeneous-funnel setting.

