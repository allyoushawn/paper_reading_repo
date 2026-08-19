# Paper Analysis: Learning Hiring Preferences: The AI Behind LinkedIn Jobs

**Source:** https://www.linkedin.com/blog/engineering/learning/learning-hiring-preferences-the-ai-behind-linkedin-jobs  
**Date analyzed:** 2026-08-18  
**Source ID:** 0f0bb519-890d-4f88-99ee-00e98360f699  
**Model identifier:** codex-sol  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)  
**Query status:** notebook_query intentionally not called; source_get_content success

---

## Required Survey Card Fields

- **Title:** Learning Hiring Preferences: The AI Behind LinkedIn Jobs
- **Authors or company:** LinkedIn
- **Venue:** LinkedIn-Engineering
- **Year:** 2019
- **URL:** https://www.linkedin.com/blog/engineering/learning/learning-hiring-preferences-the-ai-behind-linkedin-jobs
- **Source type:** company blog
- **Direction:** D8
- **Problem setting:** See §1, “Core problem and contribution.”
- **Objective and label definition, with horizon and delay handling:** See §1, “Objective” and “Labels.”
- **Prediction or incrementality:** Not specified in source. Indexed evidence does not establish exposure-effect identification; treat the method as prediction or optimization unless validated experimentally.
- **Model architecture:** See §1, “Architecture.”
- **Credit assignment:** See §1, “Credit assignment.”
- **Training data and counterfactual handling:** See §1, “Training evidence,” and prediction/incrementality above.
- **Offline and online evaluation:** See §2.
- **Reported gains:** See §2; no metric is added beyond indexed-source evidence.
- **Applicability to a two-sided dating recommender:** See § Project Relevance.
- **Unverified claims:** Dating transfer statements are explicitly labeled as survey inference.

---

## 1. Summary

### Core problem and contribution — indexed-source evidence

- We're now rolling out this feature globally alongside an updated version of the algorithm powering it.
- This new algorithm, which is used throughout the Jobs platform, performs nearly 20% better than the previous version in generating recommendations when we simulate our members' past…
- The technique we leverage to train the targeting to get smarter is called "online learning," which is learning that happens in real time as our members use…
- Based on how you interact with candidates, our algorithm learns your preferences and delivers increasingly relevant candidates across the Jobs product.

### Objective — indexed-source evidence

- This also gives us the ability to incorporate online learning from user feedback across additional channels outside our Jobs product in the future like Recruiter Search.
- Our matching technology shows up on both the job-seeker and company side throughout our Jobs product.

### Labels, horizon, delay, sparsity, and censoring — indexed-source evidence

- The technique we leverage to train the targeting to get smarter is called "online learning," which is learning that happens in real time as our members use…

### Architecture — indexed-source evidence

Not specified in source.

### Credit assignment — indexed-source evidence

- For each hiring project, we want to learn which profiles attributes (e.g., skill, title, industry, etc.) might be most relevant based upon the feedback for each candidate…

### Training data, baselines, and counterfactual evidence

Not specified in source.

---

## 2. Experiment Critique

### Offline and online evaluation — indexed-source evidence

- When comparing a model with online learning versus a model without online learning, we found that online learning features provide 49.61% lift in NDCG@1 (averaged over all…

### Reported gains — indexed-source evidence

- This new algorithm, which is used throughout the Jobs platform, performs nearly 20% better than the previous version in generating recommendations when we simulate our members' past…
- We’ve been actively surveying our job posters and many of the improvements we’ve made have come from this member feedback.

### Limitations, failure modes, and negative results — indexed-source evidence

- One of the challenges we face in building our products is that we’d like for the relevance aspects to be unified across these different channels so that…

**Statistical validity:** Not specified in source beyond the indexed evidence above.  
**Reproducibility:** Not specified in source.

---

## 3. Industry Contribution

**Deployability:** Not specified in source.  
**Problems solved:** See the source-grounded problem and objective evidence in §1.  
**Engineering cost:** - Thank you to Neha Jain and Erik Buchanan for leading the engineering teams responsible for these innovations and to Skylar Payne , Nadeem Anjum , David DiCato…

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** See §1 source evidence.  
**Prior work comparison:** Not specified in source. Indexed content does not provide a defensible top-5–7 ranking by citation frequency.  
**Verification:** No independent novelty verification was performed in this fallback batch.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Dataset or production logs described by the source | Not specified in source. | Not specified in source. | Indexed evidence is summarized in §1 where available. |

**Offline experiment reproducibility:** Not specified in source.

---

## 6. Community Reaction

Not specified in source.

---

## Project Relevance

**Source-grounded facts:** The evidence snippets above summarize only material present in the indexed source.

**Survey inference:** This source is relevant to reciprocal or two-sided ranking, marketplace interference, congestion, or bilateral experimentation. For dating, any transfer must be tested with 7–30 day retention and weeks-long subscription/à-la-carte revenue labels while keeping like, match, and conversation heads as migration auxiliaries.

**Prediction vs. incrementality:** Not specified in source. Indexed evidence does not establish exposure-effect identification; treat the method as prediction or optimization unless validated experimentally.

**Reciprocity and congestion:** This direction directly targets two-sided or reciprocal concerns where the evidence above supports them; dating still needs candidate-capacity and bilateral-acceptance checks.

**Cascade and low base rates:** Map the method to impression → like → match → conversation → retention/revenue only as a survey hypothesis; validate calibration and rare-event behavior.

**Success paradox:** Not specified in source. Protect match quality and successful off-platform outcomes so retention/revenue optimization does not penalize successful matching.

**Evaluation implication:** Add bilateral outcome metrics, candidate exposure concentration, delayed-label backtests, and randomized incrementality checks to any source protocol.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** LinkedIn (individual authors not taken from selected-source metadata)  
**Affiliations:** LinkedIn  
**Venue:** LinkedIn-Engineering  
**Year:** 2019  
**PDF:** NotebookLM indexed source available  
**Relevance:** Related  
**Priority:** 2
