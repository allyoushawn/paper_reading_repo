# Paper Analysis: Recommending People to People: The Nature of Reciprocal Recommenders with a Case Study in Online Dating

**Source:** https://www.dropbox.com/s/cb93kjvlolh1n7q/2012_UMUAI_Pizzato_etal_UMUAI.pdf?dl=1  
**Date analyzed:** 2026-08-18

---

## 1. Summary

**Title:** Recommending People to People: The Nature of Reciprocal Recommenders with a Case Study in Online Dating  
**Authors:** Luiz Pizzato, Tomek Rej, Joshua Akehurst, Irena Koprinska, Kalina Yacef, Judy Kay  
**Abstract:** The paper characterizes people-to-people recommendation as a reciprocal problem with subject/object and proactive/reactive roles. Its RECON case study learns bilateral compatibility from implicit behavior, combines the two directions harmonically, incorporates negative preferences, and studies popularity overload and recommendation spread on commercial dating logs.

**Key contributions:**
- Defines a taxonomy and success boundaries for reciprocal recommenders.
- Shows implicit behavior predicts connection success better than stated preferences.
- Evaluates harmonic reciprocal scoring, negative preferences, and spread across popularity groups.

**Methodology:** RECON estimates x→y and y→x compatibility from attribute distributions learned from past contacts, combines them with a harmonic mean, and optionally subtracts learned negative preference. Priority weights can adjust the relative importance of subject and object scores.

**Main results:** RECON S@10 is 42.20% versus 23.00% for a non-reciprocal recommender and 17.3% for keyword search. R@100 is 10.80% versus 5.90%. Adding negative preference raises S@1 from 31.78% to 37.46%.

---

## 2. Experiment Critique

**Design:** More than 90,000 users and 1.4 million expressions of interest are split into four training weeks and two test weeks. Baselines are unaided search, unilateral recommendation, and standard collaborative filtering; alternative time partitions are said to give similar results.

**Statistical validity:** Mann-Whitney-Wilcoxon tests find negative-preference gains significant at 95% confidence only through top-5. At top-10/top-100 the positive and combined recommenders converge, and F@100 exceeds the 54.19% baseline.

**Online experiments (if any):** Not specified in source.

**Reproducibility:** Formulas and splits are described, but data, code, random seeds, and full hyperparameters are not specified.

**Overall:** This is unusually direct evidence for reciprocal dating recommendation and overload. Its content features and offline design are dated, and it does not causally test capacity interventions.

---

## 3. Industry Contribution

**Deployability:** Harmonic aggregation, negative-feedback features, and popularity-aware monitoring are simple enough to serve as baselines or guardrails.

**Problems solved:** One-sided recommendations, explicit-preference mismatch, repeated rejection, superstar concentration, and neglected reactive users.

**Engineering cost:** Requires reliable negative feedback, robust implicit-preference updates, and protections against historical exposure bias.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** A systematic reciprocal-recommender taxonomy backed by a commercial online-dating case study.

**Prior work comparison:** RECON extends the authors' earlier reciprocal scorer; Malinowski et al. study bilateral job matching; Gale-Shapley supplies stable-matching foundations; Diaz et al. model two-sided relevance; Kim et al. aggregate bidirectional intentions.

**Verification:** The supplied primary manuscript verifies the title, authors, journal, mechanisms, and experiments; the queue records the publication as UMUAI 2013.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Commercial online-dating logs | Not specified in source | No | More than 90,000 users and 1.4M EOIs; platform unnamed. |
| Explicit/implicit subset | Not specified in source | No | 8,000 users and 116,000 interactions. |

**Offline experiment reproducibility:** Not independently reproducible because data and code are not released in the source.

---

## 6. Community Reaction

No significant community discussion found.

---

## Project Relevance

**Mechanism:** Harmonic aggregation suppresses pairs with weak return interest; negative preferences reduce avoidable rejection. The paper also segments proactive, reactive, active, and popular users and compares recommendation spread rather than accuracy alone.

**Metric/effect:** S@10 rises to 42.20% from 23.00% unilateral and 17.3% search. Very popular 11% receive 48.4% of EOIs, and women's reply success falls from 28% at four EOIs to 11.31% at 50+.

**Capacity/congestion:** Congestion and spread are evidenced, but no hard capacity constraint is optimized. RECON is reported to spread recommendations more evenly than collaborative filtering; formal Gini, wasted-like rate, conversations, retention, feedback loops, and interference are not specified.

**Dating mapping:** Use implicit like history for directional probability, combine both sides harmonically, track left swipes as negative preference, and treat current incoming load as a separate allocator input. Load-based weighting is an extension, not a tested result of the source.

**Dating fit: High.** It directly connects reciprocal scoring, rejection, popularity overload, and spread on dating data, though its capacity treatment remains soft and observational.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| [2021_InfoFusion_NA_Reciprocal-Recommender-Systems-Survey.md](./2021_InfoFusion_NA_Reciprocal-Recommender-Systems-Survey.md) | Novelty vs. Prior Work — Comparison | Survey organizes and compares Pizzato et al.'s RECON / *Recommending People to People* as foundational RRS work. |

---

## Meta Information

**Authors:** Luiz Pizzato, Tomek Rej, Joshua Akehurst, Irena Koprinska, Kalina Yacef, Judy Kay  
**Affiliations:** CHAI, School of Information Technologies, University of Sydney  
**Venue:** User Modeling and User-Adapted Interaction  
**Year:** 2013  
**PDF:** available via supplied Dropbox link  
**Relevance:** Core  
**Priority:** 3

---

## Annotated Bibliography Fields

**Title:** Recommending People to People: The Nature of Reciprocal Recommenders with a Case Study in Online Dating  
**Authors/org:** Luiz Pizzato, Tomek Rej, Joshua Akehurst, Irena Koprinska, Kalina Yacef, Judy Kay; University of Sydney  
**Year:** 2013  
**Venue/type:** User Modeling and User-Adapted Interaction; journal paper  
**Verified link:** https://www.dropbox.com/s/cb93kjvlolh1n7q/2012_UMUAI_Pizzato_etal_UMUAI.pdf?dl=1  
**Tier:** 3  
**What they did:** The paper defines reciprocal-recommender roles and outcomes, evaluates RECON's harmonic bilateral scoring on commercial dating logs, compares implicit with stated preferences, adds negative-preference suppression, and studies activity, popularity, reply overload, and recommendation spread.  
**Mechanism:** Combine both directional compatibilities harmonically, learn from implicit positive and negative actions, and monitor whether recommendations collapse onto popular users.  
**Metrics/effect:** RECON S@10 42.20% vs. 23.00% unilateral and 17.3% search; S@1 with negative preference 37.46% vs. 31.78%; reply success falls to 11.31% at 50+ EOIs.  
**Dating fit + reason:** High — direct dating evidence links reciprocal scoring to rejection, overload, and spread, although no hard capacity optimization or retention test is provided.  
**Confidence:** High — primary manuscript and source-scoped evidence; platform and dataset are proprietary.
