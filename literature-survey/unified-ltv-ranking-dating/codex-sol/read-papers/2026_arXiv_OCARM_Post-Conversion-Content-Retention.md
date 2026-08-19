# Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling

- **Source index:** 102
- **Source ID:** `dc23ab85-0648-42fa-821c-297f4dc06534`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Authors:** Tianbao Ma, Ruochen Yang, Chengen Li, Yuexin Shi, Jiangxia Cao, Linxun Chen, Zhaojie Liu, Yanan Niu, Han Li, Kun Gai
- **Affiliation:** Kuaishou Technology
- **Year / venue:** 2026 / arXiv:2604.25839
- **Direction / priority:** D4 retention and long-term value / Priority 3
- **URL:** https://arxiv.org/abs/2604.25839

## 1. Summary

The paper studies retention prediction for real-time-bidding user re-engagement. At bid time, the model cannot observe the post-conversion onboarding content that a user will later consume, even though this content is highly predictive of retention. OCARM handles this train–serve asymmetry in two stages. A teacher deliberately receives the future onboarding sequence during training and compresses its within-day and across-day structure with a Hierarchical Attention Encoder. The teacher is then frozen, and a serving-time user encoder learns to infer the teacher representation from observable features. The final model predicts LT1 and LT7 retention using only features available at inference.

On an industrial short-video dataset with millions of users and billions of interactions, the complete HAE/SFE variant improves AUC by 0.72% for LT1 and 0.46% for LT7 over the stated baseline. An online deployment reports, for non-uninstalled users, +20.468% re-engaged devices and +11.548% LT30; for uninstalled users, +34.430% and +22.179%, respectively. The indexed source does not specify confidence intervals, traffic allocation, or the exact experiment duration.

## 2. Experiment Critique

### Design and evidence

The staged ablation is useful: MLP teacher/MLP student, HAE teacher/MLP student, then HAE teacher/SFE student. It separates gains from richer future-content encoding and stronger representation inference. The scale and online results support practical feasibility.

### Validity concerns

- The objective is predictive, not causal. Future onboarding content may proxy latent intent rather than mediate an actionable treatment effect.
- The teacher learns under the historical content policy. A material recommender-policy shift could break the mapping from pre-conversion features to the distilled representation.
- The online table lacks uncertainty estimates, sample sizes, allocation details, and exact duration in the indexed source, limiting statistical auditability.
- The paper evaluates short-video re-engagement, not reciprocal recommendation or a two-sided market.

## 3. Industry Contribution / Project Relevance

OCARM offers a concrete recipe for exploiting downstream behavioral sequences without violating online feature availability: privileged-information training followed by distillation into a serving-safe representation. For the dating project, an analogous teacher could use post-exposure match, reply, conversation, subscription, and later-session trajectories while the production student consumes only information available at ranking time.

The approach does **not** itself solve unified policy optimization. It predicts retention labels and leaves ranking, incrementality, reciprocity, candidate congestion, delayed revenue, and the success paradox outside the formulation. Its most credible role is as a representation-learning component inside a causal or policy-learning stack, with strict temporal splits and policy-shift monitoring.

## 4. Novelty

The main novelty is the explicit distillation of otherwise inaccessible post-conversion content into a serving-time representation, with a hierarchical teacher for multi-day content and a student feature encoder. This is more specific than ordinary knowledge distillation because the teacher has privileged temporal information unavailable at inference.

## 5. Dataset Availability

The experiments use proprietary short-video platform data comprising millions of users and billions of interactions. A public dataset or release link is **Not specified in source**.

## 6. Community Reaction

Not specified in source. The indexed document is a 2026 arXiv preprint and contains no independent community-reaction evidence.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## 8. Meta Information

- **Data domain:** Industrial short-video RTB re-engagement
- **Outcomes:** LT1, LT7, LT30 retention; re-engaged devices
- **Method family:** Privileged-information teacher–student distillation
- **Causal identification:** None stated
- **Two-sided constraints:** Not modeled
- **Code / data release:** Not specified in source
