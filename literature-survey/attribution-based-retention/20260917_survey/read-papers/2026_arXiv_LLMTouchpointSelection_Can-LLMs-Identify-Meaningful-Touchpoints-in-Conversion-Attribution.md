# Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?

**Source:** https://arxiv.org/html/2608.28649v1 | **NLM source id:** 32c86ead-a887-40ef-84ee-da9eaa3cff38 | **Year / venue:** 2026, CIKM '26 (arXiv:2608.28649) | **Authors / affiliation:** Jinqi Wu, Sishuo Chen, Zhangming Chan, Yong Bai, Chao Yi, Han Zhu, Shuodian Yu, Lei Zhang, Sheng Chen, Chenghuan Hou, Jian Xu, Chaoyou Fu — Nanjing University; Taobao & Tmall Group of Alibaba | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Conversion attribution in e-commerce splits into touchpoint *selection* (which historical interactions mattered) and weight *allocation* across them. Prior selection methods rely on heuristic rules (taxonomy/shop matching, collaborative-filtering similarity) and miss "implicitly-related" touchpoints — semantically related but with no explicit taxonomy/CF overlap (e.g. camera + memory card). The paper builds SILVA, a human-annotated benchmark (1,000 conversions, 69,680 touchpoints, 3-day lookback) showing 19.09% of touchpoints are explicitly-related and a further 14.91% are implicitly-related and thus invisible to heuristic rules. It then evaluates 8 LLMs (pairwise vs. listwise prompting) at classifying touchpoints as Irrelevant/Explicit/Implicit, and proposes LOTUS, which feeds LLM-selected touchpoints as auxiliary positive labels into a production CVR model. **Unit of credit:** per touchpoint (historical interaction), a 3-way classification, not a continuous weight. **Outcome:** e-commerce purchase conversion / CVR prediction (GAUC). **Bias handling:** does not address engagement-level selection bias; instead replaces mechanical heuristic-rule matching with LLM semantic reasoning to reduce a different failure mode (missed implicit relevance).

## 2. Evidence
SILVA benchmark from a platform with hundreds of millions of DAU. Best explicit-touchpoint F1 = 0.9095 (Gemini-3.1-Pro, pairwise); best implicit F1 only 0.5426 (GPT-5.5, pairwise) — vs. ~0.15 random-guess baseline. Pairwise prompting beats listwise on every model (avg overall F1 0.6954 vs 0.6490). Downstream: LOTUS gives +0.35pp GAUC over the in-shop production baseline (Base) and +0.15pp over the heuristic cross-shop baseline (CABB) on a production-scale CVR model (hundreds of millions of active users); authors note 0.1pp GAUC is empirically sufficient to move revenue at this scale.

## 3. Limitations
Implicit-touchpoint F1 remains far below explicit (≤0.54 vs ≥0.90) — substantial gap to human-level understanding. Listwise prompting degrades badly on smaller (<100B) models. Pairwise LLM inference over full clickstreams is computationally expensive at production scale. Chain-of-thought/"thinking" mode gives only marginal gains (+0.008–0.02 F1), suggesting current reasoning is not tuned for this task.

## 4. Prior works named
- CABB (Zeng et al. 2026) — heuristic cross-shop touchpoint selection via CF signals
- MAL (Chen et al. 2025) — multi-attribution learning for CVR prediction
- CausalMTA (Yao et al. 2022) — eliminating user confounding bias in causal MTA
- Shao & Li (2011) — data-driven multi-touch attribution models
- Wei et al. (2022) — chain-of-thought prompting

## 5. Project Relevance
- **Answers:** Q1
- **Attributes retention to individual interactions?** No — attributes discrete e-commerce purchase conversion to prior touchpoints, not recurring retention/days-active.
- **Transferable components:** Two-stage selection-then-allocation framing; LLM-based pairwise semantic scoring to surface implicitly-relevant interactions beyond rule-matching; using LLM-attributed labels as auxiliary training targets for a production ranking/prediction model.
- **Required changes:** Re-anchor the target from single purchase conversion to recurring N7 retention; adapt prompts/features from product metadata to heterogeneous dating actions (swipe, match, message) with temporal gaps; run LLM scoring offline to distill into a lightweight online ranker (real-time LLM calls per swipe are infeasible at scale).
- **On last-touch:** Does not name last-touch explicitly but shows in-shop/single-item heuristic baselines are "blind" to the 14.91% of touchpoints that are implicitly relevant, understating the value of full-path attribution.
- **Transfer rating:** adaptable — the LLM semantic-selection and auxiliary-label mechanism transfers, but the outcome must move from a one-time purchase to a recurring multi-touch retention label.
