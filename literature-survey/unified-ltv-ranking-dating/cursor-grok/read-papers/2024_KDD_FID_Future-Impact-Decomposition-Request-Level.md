# Paper Analysis: Future Impact Decomposition in Request-level Recommendations

**Source:** https://arxiv.org/pdf/2401.16108.pdf  
**Date analyzed:** 2026-08-16

## Survey Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | Future Impact Decomposition in Request-level Recommendations; Xiaobei Wang, Shuchang Liu, Xueliang Wang, Qingpeng Cai, Lantao Hu, Han Li, Peng Jiang, Kun Gai, Guangming Xie (Kuaishou Technology / Peking University); KDD 2024; https://arxiv.org/pdf/2401.16108.pdf |
| 2 | Source type | Industry paper |
| 3 | Direction | D2 |
| 4 | Problem setting | List-wise RL recommenders where users browse item-by-item but MDP state transitions are only observable at request level; item-wise feedback is available but list-level credit assignment loses item characteristics. |
| 5 | Objective and label definition | Maximize expected cumulative discounted list reward E[∑ γ^i R(s_{t+i}, a_{t+i})]; offline click-or-not (1.0 / −0.2); online linear combination of watch time, like, follow, collect, comment; episode depth capped at 20 offline; 1-week online window; DAU and weekly retention also measured. Delay/sparsity/censoring not specified. |
| 6 | Prediction or incrementality | Policy-value / cumulative-reward RL (A2C); predicts V(s) and item-level advantages; not incrementality/uplift modeling. |
| 7 | Model architecture | Request-level A2C backbone with item-wise TD/actor decomposition (ItemA2C); optional reward-based re-weighting (ItemA2C-W) or adversarial neural weight model (ItemA2C-M) splitting V(s_{t+1}) across items. |
| 8 | Credit assignment | Linear list reward R = ∑ r_{t,k}; equal or weighted share of next-state value V(s_{t+1}) assigned per item via w_{t,k}; item-level advantage A(s_t, i_{t,k}, w_{t,k}) drives pointwise policy updates. |
| 9 | Training data and counterfactual handling | Request-level MDP replay with item-wise rewards; on-policy A2C; compared to supervised BCE click baseline, SlateQ, DDPG, HAC; no explicit off-policy correction described for ItemA2C itself. |
| 10 | Offline and online evaluation | Offline: KuaiSim on ML1M and KuaiRand1K (K=6, depth 20); online A/B on industrial video platform (100M+ DAU, refined ranking K=6, ~500 candidates, 1 week). |
| 11 | Reported gains | KuaiRand: ItemA2C-M total reward 16.03 vs HAC 12.65 (+27% reward, +20% depth); ML1M: 17.94 vs 17.53 (+2.3% / +1.8%); online vs request-level A2C: watch time +0.129%, like +1.103%, follow +0.300%, collect +0.963%, comment +0.221%; DAU +0.028%, retention +0.016%. |
| 12 | Applicability to a two-sided dating recommender | Item-level future-impact decomposition directly addresses slate ranking where multiple profiles get partial feedback; re-weighting by immediate match/like signals could attribute delayed retention to specific shown profiles. One-sided, no reciprocity or congestion modeling. |
| 13 | Unverified claims | Authors note ItemA2C-M adversarial weights diverge from heuristic weights across datasets; performance degrades as list size K grows; not verified for continuous-action DDPG/HAC variants. |

## 1. Summary

**Title:** Future Impact Decomposition in Request-level Recommendations  
**Authors:** Xiaobei Wang, Shuchang Liu, Xueliang Wang, Qingpeng Cai, Lantao Hu, Han Li, Peng Jiang, Kun Gai, Guangming Xie  
**Venue:** KDD 2024

**Abstract (from source):** RL recommenders typically act with list-wise actions while users consume items one-by-one, causing information loss when optimizing only list-level rewards. The paper formulates a request-level MDP with observable item-wise rewards and proposes ItemA2C, decomposing critic TD and actor advantage to the item level while reconstructing the request-level objective via future-impact re-weighting.

**Key contributions:**
- Request-level MDP with item-wise observable rewards and linear list aggregation.
- ItemA2C: equal-weight item decomposition of A2C losses.
- ItemA2C-W: reward-based future impact re-weighting with hyperparameter α.
- ItemA2C-M: model-based adversarial re-weighting network.
- Proof that weighted item targets reconstruct request-level value; offline sim + live A/B validation.

**Methodology:** Standard request-level A2C critic V(s) plus item-wise target Ψ_w(s_t, i_{t,k}) = r_{t,k} + w_{t,k} γ(1−d) V(s_{t+1}) with ∑ w_{t,k}=1; actor loss per item using item-level advantage; weight model trained adversarially by reversing actor loss in ItemA2C-M.

**Main results:** ItemA2C-M best on KuaiRand1K and ML1M simulators; live video ranking gains on engagement and retention metrics vs request-level A2C; supervised click baseline and SlateQ underperform.

## 2. Experiment Critique

**Design:** Strong offline baselines (HAC, SlateQ, DDPG, supervision) on two public simulators; ablations on K and α; online A/B with 10% traffic per variant plus 20% LTR holdout.

**Statistical validity:** Offline improvements reported with variance; p<0.05 noted for KuaiRand lift vs HAC; online metrics described as statistically significant.

**Online experiments:** One-week industrial video refined-ranking test; multi-signal reward (not click-only); retention/DAU reported.

**Reproducibility:** ML1M and KuaiRand1K preprocessing described; KuaiSim-based simulator; production system details partially proprietary.

**Overall:** Clear ablation of decomposition vs request-level RL; authors acknowledge decay at large K, platform-dependent optimal re-weighting, and restriction to late ranking stages where all K items receive feedback.

## 3. Industry Contribution

**Deployability:** ItemA2C adds no extra serving parameters vs A2C; ItemA2C-M adds offline training cost only; deployed in refined ranking stage of 100M+ user video app.

**Problems solved:** Misalignment between list-wise RL actions and item-wise user browsing; uniform splitting of future value across slate items.

**Engineering cost:** Requires item-wise feedback logging in request-level MDP pipeline; adversarial weight model optional; not suited to early retrieval with massive pools.

## 4. Novelty vs. Prior Work

**Claimed novelty:** Item-level future impact decomposition under request-level state transitions; reward-based and learned re-weighting; theoretical reconstruction of request-level A2C objective.

**Prior work named in source:**
- Ie et al., SlateQ (IJCAI 2019) — single-choice slate decomposition baseline.
- Liu et al., HAC / latent action space (WWW 2023) — primary request-level baseline.
- Zhao et al., KuaiSim (2023) — offline simulator.
- Cai et al., TCAC (WWW 2023) — related actor-critic industrial video work.
- Mnih et al., A2C (ICML 2016); Lillicrap et al., DDPG (ICLR 2016).
- Gao et al., KuaiRand (CIKM 2022).

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| MovieLens 1M | Public | Yes | 10-core filtering, chronological episodes |
| KuaiRand1K | Public (KuaiRand) | Yes | Short-video sequential data |
| Industrial video platform | Proprietary | No | Online A/B traffic |

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

Directly relevant to **Q2 credit assignment**: decomposes list-level future value V(s_{t+1}) to item-level weights for ranking decisions under delayed session outcomes. Speaks to **Q4 short/long fusion** via immediate item reward plus weighted future impact. **Q8 migration**: compares supervised click LTR to RL ItemA2C with retention gains. Does not address **Q7** reciprocity/congestion or **Q5** incrementality.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| *(To be filled in during Phase 3.7)* | | |

## Meta Information

- **Authors:** Xiaobei Wang, Shuchang Liu, Xueliang Wang, Qingpeng Cai, Lantao Hu, Han Li, Peng Jiang, Kun Gai, Guangming Xie
- **Affiliations:** Kuaishou Technology; Peking University; unaffiliated (Kun Gai)
- **Venue:** KDD 2024
- **Year:** 2024
- **Relevance:** Core
- **Priority:** 1
- **Workplace:** cursor-grok
- **nlm:** f2d45264-e73c-42ed-9104-eccee63801bf
