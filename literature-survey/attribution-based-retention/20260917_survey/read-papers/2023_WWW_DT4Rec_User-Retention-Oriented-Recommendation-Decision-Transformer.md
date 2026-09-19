# User Retention-oriented Recommendation with Decision Transformer

**Source:** https://arxiv.org/html/2303.06347v1 | **NLM source id:** 340177ed-c957-4263-a5da-79b22e29b3a9 | **Year / venue:** WWW 2023, Austin | **Affiliation:** City University of Hong Kong, Wuhan University, Baidu Inc. | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Optimizing immediate feedback risks clickbait that erodes trust; online RL exploration for retention is too risky; offline RL suffers value-estimation instability or unbounded off-policy variance. DT4Rec is the first adaptation of the Decision Transformer to retention-oriented recommendation, casting offline RL as autoregressive sequence modeling conditioned on a target reward. **Unit of credit:** per recommendation step (an action generates a list of N items given history) — DT4Rec generates lists autoregressively conditioned on a return-to-go prompt rather than computing explicit fractional multi-touch attribution. **Outcome optimized:** user retention `e_t` = number of days logged in over the next K intervals (K=7 for IQiYi, K=1 month for ML-1M) via a return-to-go (cumulative future retention) target. **Bias handling:** an auto-discretized reward prompt preserves partial-order between reward levels, and a weighted contrastive loss treats low-reward trajectories as negative samples (weighted ∝ 1/return-to-go) to force the model to avoid sub-optimal patterns rather than ignore them — addressing the train/inference reward-conditioning mismatch, not selection bias directly.

## 2. Evidence
Datasets: IQiYi (3M users, 4M items, 71M interactions, avg. retention 4.80/7 days) and ML-1M (6,014 users, avg. retention 4.13 months). Baselines: BERT4Rec, SASRec (accuracy), TopK, LIRD (retention/RL), DT4Rec-R (ablation w/o reward conditioning). Offline only, no live A/B. Retention metrics (MB-URS/SB-URS/IUR/NRC on IQiYi): DT4Rec 6.05/72,270/26.0%/1.4% vs. best baseline LIRD 5.63/63,572/17.3%/1.9% (all significant, p<0.05); similar gains on ML-1M and on accuracy metrics (BLEU/ROUGE/NDCG/HR).

## 3. Limitations
Standard DT inference is prompted with the maximum target reward, which rarely appears in sub-optimal training trajectories, causing an out-of-distribution mismatch; without the contrastive loss, performance collapses (SB-URS -9.82%, IUR -29.6% on IQiYi). Naive continuous reward-prompt MLPs fail to preserve partial-order distances (1.49–1.82% drop). Standard off-policy evaluation (IS/WIS) shows high variance, motivating the paper's own MB-URS/SB-URS metrics instead.

## 4. Prior works named
- Chen et al. (2021) — Decision Transformer: Reinforcement learning via sequence modeling
- Kang & McAuley (2018) — SASRec
- Wu et al. (2017) — Returning is Believing: Optimizing long-term user engagement (source of IUR/NRC metrics)
- Chen et al. (2019) — Top-K off-policy correction for a REINFORCE recommender system
- Zhao et al. (2017) — LIRD: Deep reinforcement learning for list-wise recommendations

## 5. Project Relevance
- **Answers:** Q2 adjacent (no explicit per-interaction attribution, but retention-conditioned sequence modeling)
- **Attributes retention to individual interactions?** No — DT4Rec is an autoregressive policy-generation model; it conditions on a return-to-go prompt but never decomposes sequence-level retention into per-item/per-swipe fractional credit, nor computes counterfactual removal effects.
- **Transferable components:** return-to-go sequence prompting (recasting N7 active-days as a future cumulative target); auto-discretized reward prompts; weighted contrastive policy learning using low-retention sequences as negatives.
- **Required changes:** to get fractional per-swipe credit, one would need to extract Transformer attention weights or run counterfactual leave-one-out prompt masking — DT4Rec itself only outputs next-item recommendations, not credit labels; it also assumes a single homogeneous action type, so heterogeneous swipe/match/message event encoders would need to be added.
- **On last-touch:** Not named explicitly, but the paper's central argument — that immediate/myopic feedback optimization fails to capture retention, which depends on multi-step cumulative context — is a direct critique of last-touch-style crediting.
- **Transfer rating:** adaptable — the return-to-go framing and contrastive training against low-retention sequences are reusable ideas, but the model itself must be repurposed (via attention extraction or ablation) to produce credit labels rather than recommendations.
