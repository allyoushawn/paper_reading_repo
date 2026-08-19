# Paper Analysis: Rankability-enhanced Revenue Uplift Modeling Framework for Online Marketing

**Source:** Bowei He, Yunpeng Weng, Xing Tang, Ziqiang Cui, Zexu Sun, Liang Chen, Xiuqiang He, Chen Ma, "Rankability-enhanced Revenue Uplift Modeling Framework for Online Marketing," KDD 2024. https://doi.org/10.1145/3637528.3671516
**Date analyzed:** 2026-08-16

## 1. Summary

Bowei He, Chen Ma (City University of Hong Kong), and coauthors from Tencent FiT propose RERUM (Ranking-Enhanced Revenue Uplift Modeling), a framework for uplift modeling when the response is continuous revenue (dollar spend) rather than a binary conversion. The core problem: revenue responses are zero-inflated and long-tailed (most users spend $0–$10,000, a tiny fraction spends $500K+), so standard MSE-based response regression is destabilized by outliers, and prior uplift models optimize pointwise prediction accuracy rather than the ranking quality that actually determines which customers get targeted. RERUM combines three components on top of any existing uplift base model (TAR, CFR, DragonNet, etc.): (1) a Zero-Inflated Lognormal (ZILN) loss that separates the "will this person spend at all" propensity from a lognormal regression on positive spend amounts; (2) a response-ranking loss derived from theoretical error bounds, penalizing within-group and cross-group order violations between predicted and true responses; (3) a listwise uplift-ranking loss that models the probability of an individual being ranked at the top of the population as proportional to their uplift score (a top-one-probability / listwise L2R formulation in the tradition of Cao et al. 2007). The combined objective is trained end-to-end. RERUM is validated offline on the Hillstrom (Men/Women) and a 5M-user Tencent Product dataset, and online via three live mutual-fund marketing campaigns on Tencent FiT (~400M users), where it delivered an average 20.61% lift on sales-revenue LIFT@2 and an estimated $430M/month additional assets under management.

## 2. Experiment Critique

**Design:** Offline evaluation covers two public Hillstrom variants and one large industrial dataset (5M individuals, 1,800+ features), each with an 8:1:1 train/validation/test split and five random seeds; statistical significance is tested with a t-test (p ≤ 0.05), and results are broken out by four AUUC/ranking metrics (AUUC, AUQC, KRCC, LIFT@30) across four backbone models (TAR, CFR-Wasserstein, CFR-MMD, DragonNet). This is a reasonably thorough offline design with backbone-agnostic ablations (Table 2/3) isolating the contribution of ZILN vs. response-ranking vs. listwise-uplift-ranking losses. **Online validity:** the online deployment is a genuine large-scale field experiment (three separate campaigns, ~400M-user population, top-2%-targeted design with randomized treatment/control split within the targeted group), which is stronger evidence than most uplift papers provide. **Reproducibility:** the industrial Product/Tencent-FiT data and the online deployment are not shareable; only the Hillstrom results are independently reproducible. **Limitation the authors note themselves:** adding the ranking losses (UR, RR) slightly degrades raw MAPE regression accuracy relative to ZILN alone — an explicit, reported trade-off rather than a hidden one. **Overall:** solid industrial-strength offline + online evidence, but public reproducibility is limited to Hillstrom.

## 3. Industry Contribution

RERUM is explicitly an industry-deployed system (Tencent FiT wealth-management notification/redpoint targeting), reported with production online-experiment results and an estimated dollar business impact (+$430M/month AUM). It is architecturally "backbone-agnostic" — a loss-function add-on rather than a new network from scratch — which lowers the engineering cost of adoption for a team that already has a DragonNet/TARNet-style uplift model in production. The framework does not, however, address serving latency, feature-pipeline changes, or how the top-2%-targeting policy composes with an existing ranking/serving stack beyond the campaign-targeting use case.

## 4. Novelty vs. Prior Work

Claimed novelty: the first work (per the authors) to jointly address (a) the continuous long-tail revenue-response distribution via ZILN and (b) uplift rankability via a listwise ranking loss, in one framework, with a companion theoretical analysis showing that MSE is a looser error bound than the paper's derived response-ranking losses. The most heavily cited prior works are Devriendt et al. 2020 (the L2R-for-uplift formalization this paper's listwise loss is built on — this is the same paper as file #1 in this batch), Shalit et al. 2017 (TARNet/CFRNet, PEHE), Shi et al. 2019 (DragonNet, one of RERUM's four backbones), Cao et al. 2007 (top-one-probability listwise ranking, the basis of L_lu-rank), Wang, Liu & Miao 2019 (the original ZILN customer-lifetime-value paper, already carded in this survey folder as `2019_arXiv_ZILN_...`), Künzel et al. 2019 (S-/T-Learner baselines), and Gutierrez & Gérardy 2017 (uplift-modeling literature review).

## 5. Dataset Availability

| Dataset | Size | Treatment | Outcome | Horizon | Public? |
|---|---|---|---|---|---|
| Hillstrom-Men / Hillstrom-Women | 64,000 total (split by campaign) | Men's/Women's-merchandise e-mail | Dollar spend | 2 weeks post-campaign | Yes |
| Product (Tencent FiT mutual fund) | 5,000,000+ individuals, 1,800+ features | Incentive coupon | Dollar amount paid for fund purchase | Not stated (offline snapshot) | No (industrial) |
| Tencent FiT online deployment | ~400,000,000-user population, top-2% targeted | Notification "redpoint" | Sales revenue (LIFT@2) | 1 month | No (industrial, online only) |

## 6. Community Reaction

Not assessed in NotebookLM mode.

## 7. Reference Card

1. **Title, authors, venue, year, URL:** "Rankability-enhanced Revenue Uplift Modeling Framework for Online Marketing," Bowei He, Yunpeng Weng, Xing Tang, Ziqiang Cui, Zexu Sun, Liang Chen, Xiuqiang He, Chen Ma, KDD 2024 (Barcelona, Spain). https://doi.org/10.1145/3637528.3671516
2. **Source type:** Academic / industry paper (Tencent FiT + City University of Hong Kong; includes a production online deployment).
3. **Direction:** D6.
4. **Problem setting:** Revenue uplift modeling for online marketing — ranking customers by the causal effect of a marketing treatment (coupon, notification) on continuous dollar-value revenue, under a zero-inflated, long-tailed response distribution.
5. **Objective and label definition:** Joint loss L_overall = L_ZILN + L_r-rank + L_lu-rank + L2 regularization. Label is continuous revenue/spend yᵢ ∈ ℝ. Horizon is stated explicitly and is delayed: "spend" is measured over the **two weeks** following the Hillstrom e-mail campaign; the online Tencent FiT deployment measures sales-revenue LIFT@2 over the **one month** following the notification. No explicit censoring mechanism is described; the two-week/one-month windows appear to be fixed observation cutoffs rather than a modeled delay/censoring process.
6. **Prediction or incrementality:** Incrementality. The paper explicitly defines the estimand as CATE — "we estimate the CATE from the statistical perspective as the uplift effect, that is: τ(xᵢ) = E[Yᵢ|Xᵢ=xᵢ,Tᵢ=1] − E[Yᵢ|Xᵢ=xᵢ,Tᵢ=0]" — and the listwise uplift-ranking loss (L_lu-rank) is derived to rank individuals directly by this treatment-effect contrast, not by a raw predicted-outcome score.
7. **Model architecture:** A representation-learning module feeding separate treatment-response and control-response heads (each predicting a ZILN triple p, μ, σ), layered on top of an existing backbone (TAR, CFR-Wasserstein, CFR-MMD, or DragonNet); trained with the three-term joint loss described above.
8. **Credit assignment:** Not specified in source. The outcome (dollar spend) and the treatment decision are both at the user level — one coupon/notification, one user, one delayed spend total. There is no item-level or impression-level decomposition; RERUM ranks *customers* for a marketing intervention, not *items* within a slate shown to a customer.
9. **Training data and counterfactual handling:** Randomized/RCT-style treatment-control marketing data (e-mail campaign, coupon assignment); the listwise uplift-ranking loss's derivation explicitly invokes the RCT assumption that treated and control covariate distributions are identical, which is what allows the top-one-probability ranking loss to be computed in-batch. No observational-data adjustment (propensity weighting, doubly robust) is used.
10. **Offline and online evaluation:** Offline — AUUC, AUQC, Kendall Rank Correlation Coefficient (KRCC), and LIFT@30 on Hillstrom-Men, Hillstrom-Women, and the Tencent Product dataset, averaged over five random seeds with t-test significance. Online — three live marketing campaigns on the Tencent FiT platform (~400M-user population), top-2%-targeted, randomized treatment/control within the targeted group, measured by sales-revenue LIFT@2 over one month.
11. **Reported gains:** Offline — RERUM(TAR) improved AUUC by 11.45% (Hillstrom-Men), 10.82% (Hillstrom-Women), and 5.70% (Product) over base TAR; RERUM(DragonNet) improved LIFT@30 by 21.98% on average across the three datasets. Online — sales-revenue LIFT@2 improved 9.20% (Campaign 1), 37.24% (Campaign 2), and 15.43% (Campaign 3) over the prior production model, average 20.61%, translating to an estimated +$430M/month AUM.
12. **Applicability to a two-sided dating recommender:** Not addressed — RERUM ranks a single population of customers for a marketing-style intervention; there is no reciprocal match, congestion, or two-sided fairness consideration. Its revenue-over-weeks horizon and CATE-based ranking objective are structurally close to what the dating-app project needs, but the treatment (coupon/notification to a customer) and the ranking unit (customer, not item/profile) would both need to be redefined for a recommender-slate setting.
13. **Unverified claims:** The $430M/month AUM figure and the "world's largest online fintech marketing platforms" framing are self-reported by the authors (Tencent FiT employees) and are not independently auditable from the paper alone. The claim that "when the uplift is estimated perfectly, the rankability of the model is also maximized" is asserted without a formal proof in the retrievable text.

## Project Relevance

This is the strongest candidate in the batch for breaking the survey's provisional conclusion. It speaks to **Q1** (revenue as training objective, with an explicit 2-week/1-month horizon that matches the project's own "revenue over weeks" definition), **Q5** (uplift/incrementality embedded directly in the ranking loss via the listwise top-one-probability formulation), and **Q3** (label/horizon definition for a continuous, zero-inflated revenue outcome — directly relevant to the project's revenue-mix constraint). It does **not** speak to **Q2** (credit assignment from a delayed outcome to an item-level decision — RERUM's unit of ranking is the customer, not an item/profile shown to a viewer) or **Q7** (two-sided/reciprocal market, congestion, fairness — entirely absent; RERUM is a single-sided marketing-targeting problem). The treatment here (coupon, notification) is a customer-level marketing intervention, not the item-exposure-within-a-ranking treatment the dating-app project needs — so while RERUM is architecturally the closest paper found so far to "long-horizon revenue objective + incrementality in a ranking loss," its ranking problem (who to target) is not the same ranking problem as the project's (which candidate profile to expose, and in what position).

**Counterexample verdict: YES — ranks customers by an explicit CATE estimate (Q1 = incrementality) on a genuinely delayed revenue outcome (2 weeks to 1 month, matching the project's own "revenue over weeks" horizon), which breaks the letter of the provisional claim; caveat: the treatment is a marketing coupon/notification to a customer, not an item exposure within a ranked slate, so the ranking problem itself (who-to-target vs. what-to-show) differs from the project's need.**

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2020_arXiv_PCG_Learning-To-Rank-For-Uplift-Modeling.md](./2020_arXiv_PCG_Learning-To-Rank-For-Uplift-Modeling.md) | Related Work / Experiments | Names this paper's method (`RERUM`) |

_1 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `RERUM` across all 133 cards._

## Meta Information

- **Authors:** Bowei He, Yunpeng Weng, Xing Tang, Ziqiang Cui, Zexu Sun, Liang Chen, Xiuqiang He, Chen Ma
- **Affiliations:** FiT, Tencent (Shenzhen, China); City University of Hong Kong
- **Venue:** KDD 2024 (30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining), Barcelona, Spain
- **Year:** 2024
- **Relevance:** Core
- **Priority:** 3
- **NotebookLM source:** nlm:cfc316a0-65fd-4330-8add-d39b74011f4d
