# Paper Analysis: Bidding Machine: Learning to Bid for Directly Optimizing Profits in Display Advertising

**Source:** https://arxiv.org/pdf/1803.02194.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Bidding Machine: Learning to Bid for Directly Optimizing Profits in Display Advertising  
**Authors:** Kan Ren, Weinan Zhang, Ke Chang, Yifei Rong, Yong Yu, Jun Wang  
**Abstract:**  
RTB advertisers traditionally pipeline utility prediction, cost forecasting, and bidding strategy. Bidding Machine jointly optimizes these pieces so CTR learning gradients reweight bid error by market-price density (“market sensitivity”), learns a parametric win-price distribution, and derives budgeted linear bids under second-price auctions. Supports offline alternating training and online FTRL-style updates.

**Key contributions:**
- Joint objective (Expected Utility and Risk–Return surrogates) linking classification loss to profit.
- Integrated bid-landscape module and constrained linear bid policy.
- Large offline lifts on iPinYou/YOYI and live A/B phases on YOYI PLUS.

**Methodology:**  
Maximize $\int R(x,y;b,\theta,\phi)p_x dx$ with $R = vy - c(\cdot)$ times win probability $w_\phi(b(f_\theta(x)))$; chain-rule gradients (Eqs. 8, 12); double optimization for market $\phi$ and CTR $\theta$; Algorithm 2 serving path.

**Main results:**  
Offline average profit +71.2% (EU) / +78.2% (RR) vs CE on iPinYou; ROI +202% / +217%; high-bid tail 1.49% vs 14.0% auctions $>300$; online Phase I: EU +25.5% profit vs CE, +53.0% vs FM on 89M+ auctions; Phase II BM ~2× profit vs cost vs baselines on 224M auctions.

---

## 2. Experiment Critique

**Design:**  
iPinYou (9 campaigns, train/test split) and YOYI (8 days); baselines CE, SE, FM, CELIN, ORTB, PRUD; budget sweeps $1/64\ldots1/2$ of historical spend for strategy arm.

**Statistical validity:**  
Mann–Whitney $U$: EU/RR significantly beat SE on AUC ($p<10^{-6}$); not significantly vs CE on AUC (authors note profit-not-AUC objective); RMSE and ANLP improvements $p<10^{-6}$ vs baselines.

**Online A/B tests:**  
YOYI PLUS DSP; cookie-randomized traffic; Phase I Jan 25–26 2016 desktop; Phase II April 2017 mobile (30 days); matched budgets (CNY).

**Reproducibility:**  
Paper links repeatable code (goo.gl/uCmdLR), iPinYou and YOYI dataset URLs in footnotes; specific numeric hyperparameter grid not specified in source.

**Overall:**  
Strong offline + production evidence for profit-centric CTR learning; scope is auction-time bidding, not sequence attribution.

---

## 3. Industry Contribution

**Deployability:**  
Deployed components on a major Chinese DSP (>10B auctions/day cited for host platform scale).

**Problems solved:**  
Reduces overbidding and aligns CTR training with economic outcomes under market competition.

**Engineering cost:**  
Not specified in source.

---

## 4. Novelty vs Prior Work

**Paper's claimed novelty:**  
First unified “bidding machine” framing with joint CTR + landscape + functional bid optimization for profit.

**Prior work comparison:**  
Related work section positions vs cost-sensitive CTR and ORTB references.

**Verification:**  
Not specified in source (NotebookLM batch; no independent novelty web search).

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| iPinYou | http://goo.gl/9r8DtM (paper footnote) | Yes | Public benchmark |
| YOYI | http://goo.gl/xaao4q (paper footnote) | Yes | Released for research |

**Offline experiment reproducibility:**  
Code link advertised in paper; hyperparameters partially unspecified in source.

---

## 6. Community Reaction

Not searched in this batch (NotebookLM-only ingestion).

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** Kan Ren; Weinan Zhang; Ke Chang; Yifei Rong; Yong Yu; Jun Wang  
**Affiliations:** Shanghai Jiao Tong University; Meituan-Dianping (Y. Rong); University College London (J. Wang)  
**Venue:** arXiv  
**Year:** 2018  
**PDF:** downloaded (arXiv)  
**Relevance:** Related  
**Priority:** 2

---

## NotebookLM — Project alignment (requirements.md §Project Context)

1. **Per-touchpoint fractional credit on multi-touch paths:** No — predicts utility and bids for **each auction impression**; no fractional allocation of a conversion across a sequence of prior product interactions.  
2. **Continuous fractional training targets for retention:** No — binary click/conversion supervision $y\in\{0,1\}$ for probability learning.  
3. **Heterogeneous touch types / self-selection:** Not specified in source.
