
# Sequential Multimodal Evidence Optimization for Product Media Ranking in E-Commerce

**Source:** https://arxiv.org/pdf/2608.15662.pdf | **NLM source id:** ca9271b9-af43-492f-b3b4-2868d784f2f3 | **Year / venue:** CIKM 2026 (arXiv 2608.15662) | **Authors / affiliation:** Prasenjit Dey, Frank McIntyre, Arnab Sinha — Amazon.com Inc. | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Addresses ordering heterogeneous product media (images, lifestyle photos, videos, 3D renders) on e-commerce product pages, where customers swipe through a carousel until they either convert or abandon. Existing systems optimize myopic engagement proxies (clicks, dwell time) or treat media as competing LTR items, ignoring that media are cooperative evidence toward one terminal decision, that attribution to individual assets is unobserved, and that customers truncate sessions at variable depths (endogenous truncation), which can falsely credit early weak assets. **Unit of credit:** per consumed-prefix position (media asset) in an ordered slate. **Outcome:** terminal conversion (purchase, y∈{0,1}) and swipe efficiency (median swipes to conversion). **Bias handling:** Position-Aware Learning (PAL) decomposes the utility logit into content vs. position-only towers during training and discards the position tower at policy/inference time to remove slot-depth leakage; variable-depth supervision trains only at the observed consumed depth (not all prefixes) to prevent early-asset over-crediting; survival-based depth reweighting upweights rare deep prefixes; a two-stage design (frozen trajectory-utility model → autoregressive pointer-network policy trained with survival-weighted reward-to-go) front-loads the most decision-relevant media before likely drop-off.

## 2. Evidence
- **Dataset:** proprietary Amazon mobile session logs, ~150M sessions, millions of products, tens of millions of media assets (electronics, apparel, home, beauty); slates capped at 15.
- **Baselines:** Heuristic (rule-based), CTR (engagement proxy), CLTR-CVR (counterfactual LTR + IPW), Listwise-MM (multimodal listwise), Seq2Slate-Adapt (autoregressive pointer + terminal REINFORCE).
- **Offline off-policy results (relative to heuristic, doubly-robust/SNIPS estimators):** SMEO +6.1% SNIPS-CVR / +5.4% DR-CVR / -15.3% median swipes-to-conversion — best on all three, ahead of Seq2Slate-Adapt (+4.1%/+3.5%/-10.8%) and Listwise-MM (+3.2%/+2.7%/-8.5%).
- **Ablations:** removing PAL costs -1.0% DR-CVR; keeping PAL at policy time costs -1.5% DR-CVR and +3.4% MSC; removing survival weighting costs -1.9% DR-CVR; removing interaction masking costs -0.7% DR-CVR.
- **Deployment:** offline batch pipeline on a 16-GPU V100 cluster (full catalog refresh in a few hours); precomputed orderings served via distributed KV store at sub-5ms lookup latency.

## 3. Limitations
- Retaining the PAL position tower during policy optimization actively degrades performance (policy exploits slot effects instead of content).
- All-prefix supervision (labeling every intermediate step with the terminal outcome) causes false credit leakage to early, uninformative assets — explicitly shown to be incorrect.
- Primary product image is conventionally fixed at slot 1, restricting policy optimization to slots ≥2 (a UX constraint, not a general one).
- Relies on off-policy (SNIPS/DR) evaluation assumptions and propensity clipping since the logged policy is not randomized; MSC is a relative ordering-quality proxy, not a causal swipe estimate.

## 4. Prior works named
- Bello et al. (2019), **Seq2Slate** — autoregressive pointer-network slate re-ranking.
- Zhao et al. (2019) — Position-Aware Learning (PAL) architecture for slot-depth debiasing.
- Dudík, Langford & Li (2011) / Swaminathan & Joachims (2015) — Doubly Robust and Self-Normalized IPS off-policy estimators.
- Vinyals, Fortunato & Jaitly (2015) — Pointer Networks.
- Rennie et al. (2017) — Self-Critical Sequence Training (variance reduction for REINFORCE).

## 5. Project Relevance
- **Answers:** Q1 (2026 industrial sequential-evidence/attribution approach for cooperative-asset ranking).
- **Attributes retention to individual interactions?** No — attributes terminal purchase conversion to individual media assets within a single session, not multi-day retention to interactions.
- **Transferable components:** trajectory-utility model over consumed prefixes; PAL position-bias decoupling; variable-depth supervision (train only at observed stopping depth) as a direct fix for the "credits swipes that would've happened anyway" selection-bias weakness; survival-weighted reward-to-go for front-loading high-value candidates; post-hoc Leave-One-Out counterfactual masking for per-touch attribution without dense labels.
- **Required changes:** replace single-session terminal conversion with a daily-recurring N7 retention label; extend homogeneous media tokens to heterogeneous swipe/match/message event types; drop the fixed-first-slot UX constraint (not applicable to a swipe feed).
- **On last-touch:** doesn't name last-touch directly but structurally argues against any position/last-event-only credit — explicitly shows naive last-position or all-prefix supervision misattributes credit to unobserved deep assets or falsely credits early weak assets when truncation is endogenous.
- **Transfer rating:** adaptable — LOO counterfactual masking plus variable-depth/survival-weighted supervision map cleanly onto per-swipe fractional retention credit, but the outcome and touchpoint vocabulary must be rebuilt for a recurring, heterogeneous-funnel setting.
