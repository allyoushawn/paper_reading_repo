
# ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization

**Source:** https://arxiv.org/pdf/2605.08881.pdf | **NLM source id:** 916117a6-16d6-4277-ad48-fd92b7e60f51 | **Year / venue:** ICLR 2026 (arXiv 2605.08881) | **Authors / affiliation:** Yuguang Liu, Luyao Xia, Hu Liu, Zhangxi Yan, Jian Liang, Han Li, Kun Gai — Kuaishou Technology, Beijing; The University of Auckland | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Studies "Consumption Drives Production" (CDP) creator ecosystems: attributing a user's video-consumption sequence to a subsequent content-upload event. Three obstacles motivate the method: no ground-truth attribution labels, unobserved system-level confounding (latent intent, peer effects, platform strategy bias) that defeats standard backdoor/IPW adjustment, and a high-cardinality treatment space (billions of touchpoints) that breaks positivity. **Unit of credit:** per consumed touchpoint (video) in a user's time-ordered consumption sequence. **Outcome attributed:** binary upload/creation event Y within the consumption horizon (not retention). **Bias handling:** front-door identification via a latent mediator M ("inspiration"), made observable through an adversarially-learned proxy Y′ (music/template/embedding similarity between consumed and uploaded content) — a discriminator with gradient reversal suppresses Y′→Y leakage so M carries only the T→M→Y causal signal; observed confounders (X→T) are handled by IPW; positivity in the huge treatment space is preserved by restricting front-door marginalization to a contrastively-identified (InfoNCE) high-match touchpoint subset. Credit for touchpoint τⱼ is the counterfactual drop in upload probability when τⱼ is deleted from the sequence.

## 2. Evidence
- **Production data:** Kuaishou CDP logs, 100 consecutive days, >30B training instances, 400M DAU, billion-level treatment candidates; 2:3 positive:negative sampling.
- **Public benchmark:** Criteo Attribution Modeling dataset (30 days, avg. sequence length 2.68, max 880).
- **Baselines:** Logistic Regression, deepMTA, Double Machine Learning, DESCN, CausalMTA.
- **Offline results (Kuaishou):** ALM-MTA AUC 0.9070, log-loss 0.1384, gAUC 0.8210, grouped AUUC 0.8686 — best on all four metrics (vs. CausalMTA AUC 0.8167/AUUC 0.8493, next best). Upload coverage 0.39→0.58 (1.49×); avg. attributed touchpoints/upload 2.93→7.31 (2.49×); precision 4.32%→21.88% (54% in top-confidence bucket, recall 7.95%→11.67%).
- **Public Criteo results:** AUC 0.9729 vs. CausalMTA 0.9659; lowest cost-per-action across budget constraints.
- **Online production deployment (400M DAU):** DAU +0.04%, daily active creators +0.6%, unit exposure efficiency +670%, producer WAU +0.566%, production traffic efficiency +0.504%, uploads/user +0.569%; platform-health metrics (active devices, time spent) fluctuate negligibly.

## 3. Limitations
- Higher initial training loss from the multi-task/adversarial objective (though final log-loss is lower than baselines).
- Sensitive to proxy Y′ quality/coverage: strict exact-match proxy only covers 16.8% of uploads and yields a smaller creator-DAU lift (+0.32%) than the full enriched proxy set (+0.514%).
- Assumes touchpoint uplifts are linearly aggregable and evaluates single-touchpoint deletion only; higher-order interactions (e.g., leave-two-out) left to future work.
- Coverage-vs-precision threshold selection for downstream ranking is an open tuning problem.

## 4. Prior works named
- Yao et al. (2022), **CausalMTA** — backdoor-adjustment sequence-level causal MTA; ALM-MTA's primary baseline.
- Neuberg (2003) / Pearl — front-door identification criterion.
- Miao, Geng & Tchetgen Tchetgen (2018) — proxy-variable identification for unmeasured confounders.
- Ganin et al. (2016) — domain-adversarial training / gradient reversal.
- Arava et al. (2018), **deepMTA**, and Shao & Li (2011) — deep attention and data-driven MTA sequence models.

## 5. Project Relevance
- **Answers:** both Q1 and Q2 (front-door causal MTA is a 2026 industrial approach; also attributes an in-app behavioral outcome — uploads — to individual interactions, though not retention).
- **Attributes retention to individual interactions?** No — attributes content-upload probability, not N7 retention/engagement, to individual consumed touchpoints.
- **Transferable components:** front-door identification via adversarial proxy mediator (bypasses unobserved confounding without requiring backdoor ignorability); counterfactual touchpoint-deletion credit Δ(τⱼ); InfoNCE contrastive overlap control for positivity in huge treatment spaces; IPW reweighting.
- **Required changes:** swap binary upload outcome Y for daily-recurring N7 retention label; extend the homogeneous video-touchpoint sequence to heterogeneous swipe/like/match/message events with type + temporal-gap embeddings; redefine proxy Y′ from content-similarity to a dating-funnel synergy signal (e.g., match/high-dwell-conversation likelihood).
- **On last-touch:** explicitly cites last-touch as an early rule-based heuristic that data-driven MTA (logistic regression, Markov-chain removal effects, RNN, Shapley) moved beyond; critiques rule/similarity-based industrial methods for lacking causal identifiability and ignoring heterogeneous treatment effects.
- **Transfer rating:** adaptable — the front-door deconfounding and counterfactual-deletion machinery transfers directly, but the outcome, touchpoint typology, and proxy definition all need redesign for daily-recurring, heterogeneous-touch retention.
