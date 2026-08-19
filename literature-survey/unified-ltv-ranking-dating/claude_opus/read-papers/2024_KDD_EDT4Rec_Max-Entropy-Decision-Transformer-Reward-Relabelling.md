# Paper Analysis: Maximum-Entropy Regularized Decision Transformer with Reward Relabelling for Dynamic Recommendation

**Source:** `/Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/2406.00725.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

Xiaocong Chen, Siyu Wang, Lina Yao (Data61 CSIRO / UNSW). KDD '24. EDT4Rec addresses two shortcomings of Decision-Transformer-based offline RL recommenders: (1) inability to "stitch" together sub-optimal trajectory segments into a better one (because reward-to-go conditioning is computed as a fixed sum over the observed trajectory, so it cannot recombine partial paths), and (2) limited exploration once online fine-tuning begins, since a Decision Transformer trained purely on offline data treats the dataset as covering all relevant possibilities. EDT4Rec's fixes: **max-entropy enhanced exploration**, which imposes a lower bound on policy entropy (Lagrangian-relaxed, SAC-inspired) computed at the sequence level over the Decision Transformer's context window; and **RTG (return-to-go) relabeling**, which uses a CQL-trained Q-function to selectively replace RTG values with learned Q-value lower bounds when they exceed the observed trajectory return, then propagates the revised RTG backward through the trajectory (Algorithm 1) to fix training/inference consistency. Evaluated across six offline recommendation datasets (KuaiRand-1k, LibraryThing, MovieLens-20M, GoodReads, Netflix, Book-Crossing) converted into binary-click simulation environments, plus the VirtualTaobao online simulator, against DDPG, SAC, TD3, DT, DT4Rec, and CDT4Rec.

## 2. Experiment Critique

The reward is a generic binary click signal (ratings above 75% of max scale count as positive feedback) — not retention or revenue, and not derived from a real interactive system; five of six offline datasets are static rating/review corpora retrofitted into RL environments by the authors, which is a substantial reformulation with no ground-truth online validation. The one genuinely interactive environment (VirtualTaobao) is itself a simulator, not a real platform. Ablations (Figure 4: EDT4Rec-E excludes the exploration goal, EDT4Rec-R excludes reward relabeling) show reward relabeling contributes more than the exploration component, and results include variance bands across the six datasets in Table 1, which is a stronger reproducibility signal than many RL-for-RS papers provide. No statistical significance testing beyond confidence-interval overlap is reported for the online-simulator comparison.

## 3. Industry Contribution

Positioned entirely as offline-RL methodology; no production deployment or industry adoption is claimed. The reward-relabeling mechanism (Algorithm 1) is architecturally interesting as a general answer to "how do you propagate a trajectory-level (delayed) reward backward to earlier decision points" but is validated only on click-level rewards, not on the multi-week delayed retention/revenue horizons relevant to this project.

## 4. Novelty vs. Prior Work

Directly extends DT4Rec (Zhao et al., "User Retention-Oriented Recommendation with Decision Transformer," WWW 2023) and CDT4Rec (Wang et al., "Causal Decision Transformer for Recommender Systems via Offline Reinforcement Learning," SIGIR 2023) — both of which the paper uses as baselines and both of which are notable candidates for this survey's corpus (CDT4Rec claims a causal mechanism; DT4Rec targets retention specifically, unlike this paper). The core novelty relative to those is (a) the max-entropy exploration bound adapted from SAC and applied at the DT sequence level rather than per-timestep, and (b) the CQL-guided RTG relabeling to solve the "stitching" limitation that the authors argue standard reward-conditioning (vanilla DT, DT4Rec) inherits.

## 5. Dataset Availability

| Dataset | Type | Public | Notes |
|---|---|---|---|
| KuaiRand-1k | Offline, video | Yes | Unbiased sequential recommendation dataset |
| LibraryThing | Offline, books | Yes | Includes social relationships |
| MovieLens-20M | Offline, movies | Yes | Standard benchmark |
| GoodReads | Offline, books | Yes | Review/rating data |
| Netflix Prize | Offline, movies | Yes (legacy release) | Rating data only |
| Book-Crossing | Offline, books | Yes | Rating data |
| VirtualTaobao | Online simulator | Yes (open-source simulator) | Used for online RQ1/RQ2/RQ3 experiments; CTR as reward |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | Maximum-Entropy Regularized Decision Transformer with Reward Relabelling for Dynamic Recommendation; Xiaocong Chen, Siyu Wang, Lina Yao (Data61, CSIRO; UNSW); KDD 2024; https://arxiv.org/abs/2406.00725 |
| 2 | Source type | Academic |
| 3 | Direction | D2 |
| 4 | Problem setting | Offline reinforcement learning for recommendation using a Decision Transformer backbone; addresses trajectory "stitching" (combining sub-optimal offline segments into a better policy) and insufficient exploration during online fine-tuning. Not retention- or revenue-specific. |
| 5 | Objective and label definition | Reward is binary click feedback per interaction: for rating-based datasets, any rating exceeding 75% of the maximum scale is labeled positive feedback, the rest negative. The training target is return-to-go (RTG), the sum of future rewards over a trajectory, used to condition the Decision Transformer's action prediction. No day-scale delay horizon is defined — "delay" here means the RTG-relabeling problem within a single interaction trajectory, not multi-day/multi-week outcome delay. Not specified in source: any notion of retention-day or revenue-week horizon. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. The policy predicts actions that maximize expected discounted click-based reward; no causal or counterfactual estimate of exposure effect is computed. |
| 7 | Model architecture | Causal (decoder-only) Decision Transformer taking tokenized (RTG, state, action) triples over a context window K; policy is a stochastic Gaussian (continuous action) parameterized by the transformer output. Max-entropy exploration term added as a Lagrangian-relaxed constraint on sequence-level policy entropy (Eq. 5–8). RTG relabeling (Algorithm 1) uses a CQL-trained Q-function to lower-bound and backward-propagate revised RTG values through the trajectory, then a second backward pass (Algorithm 1, Step 2) restores R_t = r_t + R_{t+1} consistency for the transformer's input sequence. |
| 8 | Credit assignment | This is the paper's central mechanism, though applied to click-level, not retention-level, reward: RTG relabeling uses a CQL-learned Q-function as a reliable lower bound on the true value function, and selectively replaces the RTG at each timestep when the learned Q-value exceeds the RTG from the raw trajectory sum, then propagates the revision backward across the whole trajectory. This gives every earlier item exposure a revised return estimate reflecting value that can be observed from *other* trajectories through the same state, not just the trajectory the state happened to appear in — a genuine partial solution to the "outcome attributed to which earlier item" question, but for click reward, not delayed retention/revenue. |
| 9 | Training data and counterfactual handling | Offline dataset of (state, action, next-state, reward) tuples per user, converted from static rating/click logs; top-N highest-return trajectories seeded into a replay buffer, refreshed with online rollouts during fine-tuning (Algorithm 2). CQL is used specifically because it provides a *lower bound* on the true Q-function under distributional shift between the offline data and the induced policy — this is the paper's only explicit handling of the offline/counterfactual-distribution-shift problem; it is not a causal-inference framework in the treatment-effect sense. |
| 10 | Offline and online evaluation | Offline: Recall, Precision, nDCG on six converted datasets against DDPG, SAC, TD3, DT, DT4Rec, CDT4Rec (Table 1). Online: CTR over 100,000 timesteps in the VirtualTaobao simulator (Figure 3), with hyperparameter studies on g_online and context length K, and an ablation (Figure 4) isolating the exploration and relabeling components. No real-platform online test. |
| 11 | Reported gains | On KuaiRand-1k, EDT4Rec achieves Recall 31.256±0.241 vs. the next-best baseline CDT4Rec's 30.322±0.208 (Table 1); similar single-digit-percent margins hold across LibraryThing, Book-Crossing, GoodReads, MovieLens-20M, and Netflix. On the VirtualTaobao online simulator, EDT4Rec shows higher average CTR with tighter variance than DT, DT4Rec, and CDT4Rec (Figure 3a), though no single summary percentage is given in the text. |
| 12 | Applicability to a two-sided dating recommender | Low direct applicability — reward is generic click feedback with no retention/revenue framing and no treatment of reciprocity, congestion, or a two-sided market. The RTG-relabeling technique for backward credit propagation is a transferable *idea* for the project's Q2, but would need re-deriving against a multi-week delayed retention/revenue reward rather than per-click reward. |
| 13 | Unverified claims | The claim that CDT4Rec's "causal mechanism" and DT4Rec's retention focus are meaningfully weaker than EDT4Rec's approach rests only on the six offline benchmarks and one simulator, none of which involve retention or revenue outcomes — so the comparison does not actually test the retention/causal claims those baselines make. |

## Project Relevance

Low-to-moderate relevance. The paper does not touch retention, revenue, delayed multi-day/multi-week labels, or two-sided-market structure (**Low project relevance for Q3, Q4, Q7**), but its RTG-relabeling / CQL-backward-propagation mechanism is a reusable technical pattern for **Q2** (credit assignment for a delayed outcome) if adapted to a retention/revenue reward. It also surfaces two directly relevant related-work candidates for the survey corpus: DT4Rec (retention-focused Decision Transformer) and CDT4Rec (claims a causal mechanism) — see return block.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `EDT4Rec`._

## Meta Information

- **Authors:** Xiaocong Chen, Siyu Wang, Lina Yao
- **Affiliations:** Data61, CSIRO, Australia; The University of New South Wales, Sydney
- **Venue:** KDD 2024 (30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining)
- **Year:** 2024
- **Relevance:** Related
- **Priority:** 3
- **nlm:dadd6014**
