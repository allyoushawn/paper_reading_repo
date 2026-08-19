Date: 2026-08-17 (finalized in Phase 3.5)
Topic: Unified retention/revenue ranking model for a two-sided dating recommender

# Unified Retention/Revenue Ranking Model — Methodology Fundamentality Tracking

Workplace: `claude_opus/`. Finalized over **133 paper cards**.

## What the counts measure, and what they do not

The **mention count** is the number of the 133 cards in which a method name appears with a word
boundary. It is a defensible proxy for how load-bearing a method is in this corpus, and it is what
the counts below report.

It is **not** a strict "used as a baseline" count. A method's own paper mentions it too, and a
related-work citation counts the same as an experimental comparison. Where a proposing paper is in the
corpus, subtract one to approximate the baseline-use count.

**A first pass using substring matching was discarded.** It returned DIN in 133 cards and PLE in 131,
because those strings occur inside *finding*, *according*, *example* and *multiple*. Every count below
uses word-boundary matching. Anyone extending this file must do the same.

## The ranking below is biased by corpus composition — read this before using it

**D7 (delayed feedback) holds 18 of 133 cards, and that direction cites its own lineage densely.**
The delayed-feedback family therefore dominates the top of this table partly because of how many D7
papers the corpus contains, not purely because of field-wide importance.

The over-weighting is itself an artefact: the local Awesome repo used in discovery is rich in
advertising conversion-delay work, which inflated D7 relative to the survey's actual priorities.
**Treat cross-direction comparisons in this table as unreliable.** Within-direction rankings are sound.

## Composite score

`Composite = (mention count × 3) + (derived variants × 2) + (simplicity × 1) + (consistency × 2)`

- **simplicity:** 5 = 1–2 components, 4 = 3, 3 = 4, 2 = 5, 1 = 6+.
- **consistency:** set to **3 (neutral) for every method**, because the nine directions share no
  benchmark. Delayed-feedback work reports on Criteo and Taobao; retention RL on Kuaishou logs and
  KuaiSim; reciprocal work on matching-market data; surrogate work on experiment corpora. A variance
  figure across these is meaningless. **The consistency term therefore contributes nothing to the
  ranking and is retained only for formula compatibility.**

## Methodology Table — sorted by composite score

| Rank | Method | Proposal paper (year) | Mentions (of 133) | Derived variants in corpus | Components | Simplicity | Composite |
|---|---|---|---|---|---|---|---|
| 1 | **DFM** (delayed feedback model) | Chapelle, Criteo, KDD 2014 | 19 | 10+ (FNW, FNC, ES-DFM, DEFER, DEFUSE, FSIW, NoDeF, ESDF, NBDFM, DDFM) | 2 | 5 | **85** |
| 2 | **IPS / inverse propensity scoring** | classical | 13 | 6 (SNIPS, DR, DiPS, IPW-MF, CFRR, ESCM2-IPS) | 1 | 5 | **59** |
| 3 | **ESMM** (entire-space multi-task) | Ma et al., Alibaba, SIGIR 2018 | 12 | 5 (ESM2, ESCM2, HM3, ESDF, Multi-IPW/DR) | 2 | 5 | **54** |
| 4 | **MMoE** | Ma et al., Google, KDD 2018 | 13 | 4 (MoSE, PLE, CGC, Trinity) | 4+ experts | 3 | **53** |
| 5 | **ZILN** (zero-inflated lognormal) | Wang, Liu, Miao, Google, 2019 | 7 | 4 (GRePO-LTV, **RERUM**, CC-OR-Net, CDAF) | 1 | 5 | **37** |
| 6 | **TD3** | Fujimoto et al. | 8 | 2 (UWAC+TD3, AURO) | 1 | 5 | **36** |
| 7 | **SlateQ** | Ie et al., Google, IJCAI 2019 | 6 | 2 (FSQ, ItemA2C lineage) | 1 | 5 | **30** |
| 8 | **TARNet / CFRNet** | Shalit et al., 2017 | 4 | 4 (DragonNet, PTONet, IDUM, ESCM2-DR) | 2 | 5 | **28** |
| 9 | **SASRec** | Kang & McAuley | 6 | 1 (PinnerFormer) | 1 | 5 | **28** |
| 10 | **RLUR** | Cai et al., Kuaishou, WWW 2023 | 6 | 0 direct | 5 | 2 | **26** |

Also load-bearing but below the top ten: ES-DFM (8), FNW (7), DEFUSE (7), FSIW (6), DEFER (5),
Wide & Deep (6), CEM (6), SAC (6), DDPG (6), LFRR (5), Shared-Bottom (4), PLE (4), BPR (4),
AITM (3), DragonNet (3), LightGCN (2), HSTU (2), ESM2 (2), ESCM2 (2).

## Top Method Analysis

### Rank 1: DFM — Modeling Delayed Feedback in Display Advertising (Chapelle, KDD 2014) — 85

- **Why fundamental:** the root of an entire sub-literature. Every delayed-feedback method in this
  corpus is a descendant, and most benchmark directly against it. It established the framing that a
  not-yet-converted sample is not a negative sample.
- **Caveat for this project:** it assumes an **exponential delay distribution** and operates at an
  advertising timescale of hours to days. The project needs 7–30 day retention and multi-week revenue.
  The framing transfers; the distributional assumption and timescale do not.
- **Used as a baseline by:** FSIW, ES-DFM, DEFER, DEFUSE, ESDF, NoDeF, NBDFM, DDFM, and others.

### Rank 2: IPS and its doubly-robust descendants — 59

- **Why fundamental:** the shared correction machinery across three otherwise disconnected
  directions — uplift modelling (D6), off-policy evaluation (D3), and entire-space debiasing (D5).
- **Critical distinction the survey repeatedly had to make:** IPS used to **debias a prediction** is
  not the same as IPS used to **estimate an incremental effect**. CFRR and ESCM2 do the former;
  RERUM and CRRS do the latter. Cards record which, per paper.

### Rank 3: ESMM — 54, and Rank 8: TARNet/CFRNet — 28

- ESMM is the structural transfer for the project's cascade, **but it is provably biased** (shown by
  Alibaba's Multi-IPW/Multi-DR, WWW 2020). **Adopt ESCM2**, which folds a counterfactual regularizer
  onto the same structure. For a cascade deeper than two stages, **AITM** is the better structure.
- TARNet/CFRNet underpin nearly every deep uplift model in D6. The project's existing uplift model
  almost certainly sits in this family.

### Rank 5: ZILN — 37, and the most transferable single component in the corpus

- **Why it matters more than its rank suggests.** ZILN handles a **zero-inflated, heavy-tailed
  monetary outcome** — most users spend nothing, a few spend a great deal. Dating-app revenue has
  exactly that shape, since most users never subscribe.
- **It is the only component that appears in three distinct roles:** as a lifetime-value loss
  (Google), inside a Pareto multi-objective LTV model (GRePO-LTV), and **inside an uplift ranking
  objective (RERUM)**. That third use is the bridge the project needs, because it demonstrates
  incrementality and a delayed heavy-tailed revenue label composing in one ranking loss.
- **Recommended as the revenue-head loss** in any candidate architecture.

### Rank 7: SlateQ — 30, with assumptions that fail here

- The cleanest published slate-to-item credit-assignment decomposition, and the leading answer to
  research question Q2.
- **Both licensing assumptions break in a dating app.** Single Choice fails because viewers like
  several candidates per session. Reward/Transition Dependence on Selection fails harder, because a
  match requires the *other side* to act — an external, delayed decision outside its single-agent MDP.
- Its LP and top-k slate optimization remain reusable once item-level values exist. The decomposition
  does not transfer without extension to a two-agent reward.

### Rank 10: RLUR — 26, and the evidence-quality note that matters most

- The canonical retention-as-RL-reward system, with a **genuine billion-user online A/B result**.
- **Several other retention-RL papers in this corpus are evaluated on KuaiSim, whose retention signal
  is synthetic and circular** — `Geometric(p_ret)` where `p_ret` rises with the immediate reward the
  policy optimizes. A policy that raises immediate reward mechanically raises its simulated retention.
- **When ranking candidate architectures, separate online-A/B evidence from simulator evidence and
  never compare the two.**

## Methods that appear once but matter disproportionately

These have low mention counts because they are recent or niche, yet they carry the survey's key
findings. **Do not let the composite score bury them.**

| Method | Paper | Why it matters |
|---|---|---|
| **CRRS** | Revisiting Reciprocal Recommender Systems, KDD 2024 | The only **bilateral-treatment potential-outcome** model — reciprocity plus genuine incrementality. Missing only the long horizon. |
| **RERUM** | Rankability-enhanced Revenue Uplift Modeling, KDD 2024 | Listwise **uplift ranking over a ZILN revenue outcome** on a 2–4 week horizon. Proof the two halves compose. |
| **ItemA2C** | Future Impact Decomposition, Kuaishou, KDD 2024 | Splits slate-level future value across items losslessly; **negative result** that decomposing the critic fails. |
| **Reward-weighted labels** | Netflix GenRec / GenPage | Long-horizon signal enters through **per-example weights**, not labels. The lowest-risk migration first step. |
| **ECDA** | Integrating Predictive Models into Two-Sided Recommendations, 2026 | The only reciprocal method with a real **2-week calendar window**, plus a per-receiver exposure quota. |
