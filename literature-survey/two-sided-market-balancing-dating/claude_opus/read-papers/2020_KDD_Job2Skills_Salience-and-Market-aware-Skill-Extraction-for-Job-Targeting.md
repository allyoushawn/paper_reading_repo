# Salience and Market-aware Skill Extraction for Job Targeting

- **notebook source_id:** `49771075`
- **extraction method:** direct PDF read (NotebookLM unavailable)

## Summary
LinkedIn's job-targeting systems (reactive Job Search, proactive "Jobs You May Be Interested In"/JYMBII) need to extract the important skills from a job posting so the posting can be shown to members with matching skills. Standard named-entity-recognition (NER)-based skill extraction just detects mentioned skills with equal weight, ignoring (a) which mentioned skills are actually *salient* (core to the job) vs. incidental, and (b) whether there's enough member-side "market supply" of people who have that skill for targeting to be useful. The authors build Job2Skills, an XGBoost model combining multi-resolution (sentence/segment/job-level) deep-learning salience embeddings with member- and job-side market-supply signals, trained on a mix of expert-labeled and distantly-supervised (from actual applicant/hire outcomes) data. Deployed at LinkedIn, it improved offline AUROC by +52.84% to +62.67% over the salience-and-market-agnostic baseline, lifted JYMBII job-recommendation onsite apply rate by +1.92% and member coverage by +6.71% in a 7-day online A/B test, and cut job-poster skill-suggestion rejection rate by up to 37.06%.

## Method
Formulated as an optimization: given a job posting p and a skill set S, extract a t_s-sized skill subset S_p that maximizes the sum of each skill's "utility" U(p,s) — the increase in the probability that qualified members apply, under the assumption that a skill's utility is driven by (1) having sufficient market supply (enough members M_s who hold it) and (2) being salient (core, not incidental) to the posting. This differs from the naive "salience-and-market-agnostic" baseline, which just estimates Pr(skill mentioned in posting content) via a plain skill tagger + NER, ignoring both criteria.
- **Multi-resolution skill salience:** three neural sub-models estimate Pr(s | context) at increasing scope — (a) sentence-level: BERT/FastText-encoded sentence + skill surface form → sigmoid classifier (Eq. 6); (b) segment-level: cosine similarity between a skill's entity embedding and the mean-pooled embedding of all skills mentioned in the same job segment (e.g., "requirements", "benefits") (Eq. 8); (c) job-level: similarity between the skill and the mean-pooled embedding of all title+skill entities in the whole posting (Eq. 9). Entity embeddings are learned via a skip-gram objective over LinkedIn member profiles (Eq. 7).
- **Market-aware signals:** member-side skill supply Pr(s|M) (overall popularity) plus finer-grained cohort affinities via pointwise mutual information (PMI) and entropy of a skill given a member cohort (partitioned by attributes like industry × title) (Eq. 10); job-side skill demand via PMI of the skill given the job-posting segment label.
- **Final model:** XGBoost binary classifier combining the salience probabilities and market-supply/demand features as inputs, trained with logistic loss on job-skill pairs (Eq. 11) to predict whether a skill is a salient, market-aware job-targeting skill for a given posting.
- **Ground-truth data collection (no gold labels exist):** (1) Job Targeting (JT) dataset — job posters' own selected/accepted vs. rejected skill suggestions (positive/negative), a small but high-quality expert-labeled set; (2) Quality Applicant (QA) dataset — distant supervision: skills common to actual applicants who received positive recruiter feedback are treated as positive, others as negative, expanding coverage cheaply.

## Datasets and Baselines
**Data:** 16 months of LinkedIn's English Premium job postings, ~3 million job-skill training/eval pairs (60/20/20 train/val/test split), built from the JT and QA datasets described above; entity/skill embeddings trained on LinkedIn's 645M-member profile base.

**Baseline:** the existing production model — a logistic regression model using skill-appearance features (is the skill mentioned? where? mention frequency) and other engineered "global-level" features; i.e., the salience-and-market-agnostic NER-style approach.

**Metrics:** relative AUROC improvement (offline); online A/B test metrics — Onsite Apply rate, Job Save rate, Member Coverage (for JYMBII recommendations); Skill Add Rate and Skill Reject Rate (for the job-posting skill-suggestion flow).

## Results
- **Offline AUROC (Table 1):** Job2Skills trained on JT+QA improves overall (JT+QA) AUROC by **+62.67%** relative to the salience-and-market-agnostic baseline; +55.77% on JT-only eval, +49.27% on QA-only eval (using single-dataset training the improvements are +50.81%/+29.30%/+76.37% respectively across configurations, per Table 1's rows).
- **Ablation (Table 2):** full model (market + salience features) gives +56.99% AUROC improvement over baseline. Salience-only features: +55.43%. Market features (member+job) only: +54.91%. Member features only: +46.47%. Job features only: +49.88%. Combining salience + market features improves AUROC by +1.56% over salience-only, showing market-dynamics signal adds information beyond text-based salience alone.
- **Online JYMBII A/B test (Table 3, 20% traffic, 7 days):** Onsite Apply **+1.92%**, Job Save **+2.66%**, Member Coverage **+6.71%**.
- **Online skill-suggestion A/B test (Table 4, 50% traffic, 4 weeks):** market-aware-only model: Skill Add Rate −31.44%, Skill Reject Rate −33.71%; market-and-salience-aware (full) model: Skill Add Rate −33.75%, Skill Reject Rate **−37.06%** (i.e., recruiters manually add or reject far fewer of the suggested skills, meaning suggestions are better).
- **Qualitative/case studies:** Job2Skills detected a 293%/3.17%-share increase in Macy's SWE-related job postings two months before Macy's public tech-expansion announcement (Feb 2020); captured Azure's skill-popularity seasonality correlated with Microsoft's Q3 2018 cloud-revenue growth (93%); revealed that the baseline over-selects specific tool names (e.g., "TSO" mis-tagged as "Time Sharing Option" instead of "Transportation Security Officer" in US government postings) while Job2Skills correctly filters these out and better differentiates entry-level (domain-specific skill) vs. director-level (management/leadership skill) job requirements.

## Limitations
- Ground-truth labels are inherently indirect: JT labels come from a small subset of postings created through LinkedIn's own job-creation flow (not representative of all postings), and QA labels are "distantly supervised" (an approximation — applicants who applied and got positive recruiter feedback are assumed, not proven, to hold the truly salient skills for that job).
- The production/deployed job-level salience sub-model uses FastText instead of BERT specifically to reduce latency, at a stated 3% salience-accuracy cost — i.e., the reported best offline numbers are not fully what's running in production.
- The paper does not report statistical significance (p-values/confidence intervals) for the online A/B test lifts.
- Related-work section (§7) notes competing skill-analysis methods (SPTM, TATF, DuerQuiz, HIPO) are all limited to small-scale IT job sets or hand-picked skill taxonomies (≤1,351 skills), implying Job2Skills' scale claim is a comparative strength, but the paper does not quantify its own taxonomy's coverage limits or error rate directly.
- No discussion of fairness/bias in skill targeting (e.g., whether market-supply weighting could suppress skills held disproportionately by under-represented groups) — not addressed at all.

## Heavily Cited Prior Works
- Borisyuk, Zhang, Kenthapadi (2017) — LiJAR: "A system for job application redistribution towards efficient career marketplace" (KDD) — cited in related work as prior LinkedIn marketplace-efficiency work on job targeting/redistribution, contrasted as not addressing entity-representation quality.
- Kenthapadi, Le, Venkataraman (2017) — "Personalized job recommendation system at LinkedIn: Practical challenges and lessons learned" (RecSys) — the JYMBII system this paper improves.
- Li, Arya, Sinha (2016) — "How to get them a dream job? Entity-aware features for personalized job search ranking" (KDD).
- Devlin, Chang, Lee, Toutanova (2018) — BERT, used as one of the sentence-level salience encoders.
- Bojanowski, Grave, Joulin, Mikolov (2017) — FastText, used as the production salience encoder (for latency).
- Nadeau & Sekine (2007) — survey of named entity recognition and classification, framing the "traditional" NER-based skill extraction baseline this paper argues against.
- Chen & Guestrin (2016) — XGBoost, the model class used for the final Job2Skills utility classifier.

## Bibliography Fields
- **title:** Salience and Market-aware Skill Extraction for Job Targeting
- **authors or organization:** Baoxu Shi, Jaewon Yang, Feng Guo, Qi He (LinkedIn Corporation, USA)
- **year:** 2020
- **venue or type:** KDD '20 (ACM SIGKDD Conference on Knowledge Discovery and Data Mining), August 2020, San Diego, California, USA
- **link:** https://arxiv.org/pdf/2005.13094
- **tier tag:** Tier 1 industry (deployed at LinkedIn with reported online A/B test results)
- **what they did (≤80 words):** Built Job2Skills, an XGBoost model that scores job-posting skills by combining multi-resolution (sentence/segment/job-level) neural salience estimates with member- and job-side market-supply/demand signals (PMI-based), trained on expert-labeled and distantly-supervised job-applicant outcome data, to replace a naive NER-style "any mentioned skill counts equally" baseline. Deployed in LinkedIn's job recommendation (JYMBII) and job-posting skill-suggestion products with measured A/B test gains.
- **mechanism relevant to two-sided balancing (≤50 words):** Its "market-aware" signal — weighting entity/skill importance by how much supply exists on the other side of the market (Pr(s|M), cohort PMI) — is conceptually the closest analog to reciprocal/capacity thinking here: it discounts skills too scarce or too abundant on the demand-response side, similar in spirit to discounting over/under-supplied match candidates.
- **metrics used, and the reported effect:** AUROC (offline, +52.84% to +62.67% relative), Onsite Apply (+1.92%), Job Save (+2.66%), Member Coverage (+6.71%), Skill Add/Reject Rate (down 33.75%/37.06%) — all from a single production A/B test, no significance testing reported.
- **fit for a dating app:** low — the paper's core mechanism is entity/skill salience extraction (an NLP information-extraction problem) plus a supply-weighting heuristic for job-to-candidate targeting; it is single-sided (jobs targeting candidates by attribute match, not bilateral acceptance) and has no capacity constraint, no reciprocal scoring, and no exposure-fairness mechanism. The "market supply" idea is a weak, indirect analogy to desirability skew, not a transferable lever.
- **confidence that the item is real and described correctly:** high — full 9-page paper read directly; all numbers taken verbatim from Tables 1-4 and the text of §5.

## Project Relevance
**Low project relevance.** Job2Skills solves skill-entity extraction and salience/market-supply-weighted job targeting — a single-sided content-to-candidate matching problem with no notion of mutual/bilateral acceptance, no per-user capacity constraint, and no exposure-fairness or market-design lever. It does not address reciprocal scoring (layer 1: there is no "does the candidate like the job back" concept beyond apply/save conversion), capacity-aware allocation (layer 2: no cap on how many postings can point at one candidate), market-design levers (layer 3), or ecosystem/interference metrics (layer 4: their metrics are conversion-style — apply rate, save rate, coverage — not spread/Gini/wasted-likes measures). The "market supply" concept (weighting by how many members hold a skill) is a surface-level echo of desirability-skew reasoning but does not transfer as a mechanism — it discounts *content attributes* by population frequency, not *people* by their finite reply capacity. Disanalogy: LinkedIn job postings can absorb effectively unlimited applicants (no capacity scarcity on the "supply" side being measured), unlike a dating profile's finite, human reply capacity.

## Reverse Citation Map
