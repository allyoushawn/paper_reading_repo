# Modeling User Retention through Generative Flow Networks

**Source:** https://arxiv.org/pdf/2406.06043 | **NLM source id:** 5884e0ba-ca58-4eed-826d-7764d27bbccd | **Year / venue:** KDD 2024, Barcelona | **Affiliation:** City University of Hong Kong, Kuaishou Technology, Nanyang Technological University | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Standard recommenders optimize immediate item feedback, which fails to reflect long-term retention: retention happens between sessions, between-session activity is unobservable, and there is no clear link between any single recommended item and the eventual return decision. Prior RL approaches treat retention as a session-level reward surrogate but suffer high gradient variance. GFN4Retention treats session-wise recommendation as trajectory generation and aligns trajectory-generation probability with the session's terminal retention reward. **Unit of credit:** per recommendation step/action within a session. **Outcome optimized:** a combined reward `R(S) = R_retention · e^(α·Σr_t)` mixing terminal retention (return frequency) with immediate step feedback (clicks, likes, minus negative signals). **Bias handling:** a Detailed Balance (flow-matching) loss back-propagates the terminal retention signal to every intermediate step, implicitly performing step-wise retention attribution; a Transformer + DNN context-detection encoder models evolving user state; GFN's reward-proportional trajectory sampling avoids over-exploiting naturally hyperactive users rather than explicitly correcting for selection bias.

## 2. Evidence
Offline: KuaiRand-Pure and MovieLens-1M, plus the KuaiSim retention simulator. Baselines: CEM, DIN, TD3, SAC, RLUR. GFN4Retention beats all baselines on return time and retention (e.g., KuaiRand-Pure return time 1.496 vs RLUR 1.786 days, retention 0.163 vs 0.159; MovieLens-1M return time 1.479 vs RLUR 1.723). Live A/B on Kuaishou (10% vs 20% traffic, ranking stages 1 and 2): 1st-stage next-day retention +0.015%, low-activity user retention +0.069%, watch time +0.558%; 2nd-stage retention +0.002%, low-activity retention +0.056%, watch time +0.224% (all starred as significant except the 2nd-stage overall figure).

## 3. Limitations
Removing immediate feedback (retention-only reward) collapses click rate by 45% and like rate by 5%, showing pure terminal retention reward is too sparse to guide item-level quality. The immediate/retention balance parameter α is sensitive in both directions. Log-scale Detailed Balance loss becomes numerically unstable as forward probabilities approach zero, requiring manual smoothing offsets. Extending GFNs to continuous action spaces required assuming Gaussian policy outputs and deterministic top-K selection, a nontrivial extension beyond standard discrete GFNs.

## 4. Prior works named
- Bengio et al. — Flow network based generative models / GFlowNet foundations (Detailed Balance loss)
- Cai et al. (2023) — RLUR: Reinforcing User Retention in a Billion Scale Short Video Recommender System (primary baseline)
- Liu et al. (2023) — Generative flow network for listwise recommendation
- Zhao et al. (2023) — KuaiSim: A comprehensive simulator for recommender systems
- Zhao et al. (2023) — User Retention-oriented Recommendation with Decision Transformer (DT4Rec)

## 5. Project Relevance
- **Answers:** Q2 (published attribution of retention to individual interactions)
- **Attributes retention to individual interactions?** Yes — the Detailed Balance flow-matching objective explicitly back-propagates the end-of-session retention reward to every intermediate step, and the ablation shows non-last steps carry significant retention "flow."
- **Transferable components:** Detailed Balance flow-matching for retention attribution; integrated reward design combining immediate + long-term signal; Transformer+context-detection user-state encoder.
- **Required changes:** GFN4Retention assumes homogeneous per-step item-list actions and a single session-boundary return gap; a dating platform needs heterogeneous action-type embeddings (swipe/match/message) in the forward/backward flows, and the terminal flow must target a rolling daily N7 indicator instead of a one-time session return gap.
- **On last-touch:** The paper states retention has no clear relation to any single prior recommendation step, and its ablation proves that intermediate (non-last) steps carry meaningful attributed flow — a direct argument against last-touch-only crediting.
- **Transfer rating:** adaptable — the flow-matching attribution mechanism is the closest thing in this batch to a genuine per-step credit-assignment method, but it needs rework for heterogeneous, daily-recurring dating-app interactions.
