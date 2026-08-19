# Fairness in Job Recommendation under Quantity Constraints

- **notebook source_id:** `8c1b6d85`
- **extraction method:** direct PDF read (NotebookLM unavailable)

## Summary
The paper models job recommendation as a **resource allocation problem**: each job posting has a limited "quantity" it can be recommended to (an upper bound to avoid overwhelming the employer with applicants, and a lower bound to guarantee the posting gets minimum exposure), and on top of that constraint they add a **user group fairness** requirement — narrowing the gap in average recommended-job salary between male and female job seekers. They propose a model-agnostic **post-processing re-ranking** framework that solves a 0-1 integer program to maximize total user utility subject to both the quantity constraints and the fairness constraint, and show on a real private dataset that it collapses the gender salary gap in top-10 recommendations from thousands of dollars down to under $1,000 across four different base recommenders, largely without hurting accuracy (and even improving it for the sequential model).

## Method
Base recommenders produce a matching score S_ij for each (job seeker i, job posting j) pair. The framework re-ranks by solving: maximize Σ U_ij(Q_ij) over binary allocation variables Q_ij ∈ {0,1} (does job j appear in user i's top-N list), where the per-pair utility is U_ij(Q_ij) = [1/(1+e^{-S_ij})]·Q_ij (sigmoid of the base score, scaled by whether it's allocated) — subject to three constraints: (1) **quantity constraint** a_j ≤ Σ_i Q_ij ≤ q_j, i.e., each job posting j is shown to at least a_j and at most q_j users; (2) **user group fairness constraint** UGF(Z1, Z2, Q) < ε, where UGF is the absolute difference in expected average recommended-job salary between the two gender groups Z1/Z2; (3) each user gets exactly N recommended items (Σ_j Q_ij = N). The optimization is solved as a 0-1 integer program via the Gurobi solver (with fast heuristics for feasibility). Quantity bounds q_j (upper) and a_j (lower) are set proportional to company size (40–60% of company size as upper bound, 3–5 as lower bound) as a proxy for real hiring demand, since actual hiring-demand data wasn't available.

## Datasets and Baselines
**Dataset:** a private real-world job-recommendation dataset — 17,072 user-company interactions, 3,000 users (with gender), 5,105 companies (with size and salary in USD), split 80/10/10 train/val/test. All base models trained with Bayesian Personalized Ranking (BPR) loss.
**Base recommenders (the framework is applied on top of each, model-agnostically):** PMF (probabilistic matrix factorization, Mnih & Salakhutdinov 2008), BiasedMF (Koren, Bell & Volinsky 2009), NeuMF (neural collaborative filtering, He et al. 2017), STAMP (session-based sequential attention model, Liu et al. 2018).

## Results
Table 1 (top-10 metrics, test set), Baseline vs. re-Ranked:
- **PMF:** NDCG@10 0.0928→0.0924, HR@10 0.1295→0.1265, F1@10 0.0286→0.0280, **UGF@10 $14,368 → $967**
- **BiasedMF:** NDCG@10 0.0760→0.0727, HR@10 0.1066→0.1043, F1@10 0.0236→0.0231, **UGF@10 $16,050 → $960**
- **NeuMF:** NDCG@10 0.0747→0.0740, HR@10 0.1037→0.1025, F1@10 0.0230→0.0227, **UGF@10 $10,666 → $980**
- **STAMP:** NDCG@10 0.0698→0.0728, HR@10 0.0808→0.0902, F1@10 0.0172→0.0190, **UGF@10 $4,155 → $952** (re-ranking *improved* every accuracy metric here)

Headline: the gender salary gap (UGF@10) is cut roughly 90–94% (from a $4.1K–$16K baseline range down to a tight $952–$980 band across all four models) while ranking accuracy is essentially preserved (within ~0.5–4% relative on NDCG/HR/F1), and for the sequential model it actually improves. A separate exposure analysis (Fig. 1b) shows quantity-only constraints (no fairness term) increase exposure for smaller companies (groups G0 <1000 employees, G1 1000–5000) without hurting recommendation accuracy, and reduce over-exposure/unnecessary applications for the largest companies (G2 >5000).

## Limitations
No explicit "Limitations" section is stated in the paper's conclusion. Notable caveats embedded in the method: (1) true company hiring-demand quantities were unavailable, so the quantity bounds a_j/q_j are a **proxy** derived from company size (40–60% upper, 3–5 lower), not actual employer-stated hiring needs; (2) the fairness-accuracy trade-off is controlled by a single ε and only the resulting operating point is reported — the paper notes qualitatively that "adding the fairness constraint will reduce the recommendation quality" in general (shown for NeuMF in Fig. 1a) without exploring the full accuracy-fairness frontier; (3) fairness is defined only along a binary gender axis via one outcome measure (average salary), not other possible protected attributes or fairness definitions.

## Heavily Cited Prior Works
- Rendle et al. (2012), "BPR: Bayesian Personalized Ranking from implicit feedback" — the training loss used for every base model
- Koren, Bell & Volinsky (2009), matrix factorization techniques — BiasedMF baseline
- He et al. (2017), "Neural Collaborative Filtering" — NeuMF baseline
- Liu, Zeng, Mokhosi & Zhang (2018), "STAMP" — sequential base model
- Zhang, Zhao & Friedman (2017) and Zhang et al. (2016) — economic/Pareto-efficient resource-allocation recommendation, the conceptual basis for framing recommendation as resource allocation with a utility-maximization objective
- Patro, Biswas, Ganguly, Gummadi & Chakraborty (2020), "FairRec: Two-Sided Fairness for Personalized Recommendations in Two-Sided Platforms" — cited as related two-sided/multi-stakeholder fairness work
- Mehrotra, McInerney, Bouchard, Lalmas & Diaz (2018), "Towards a fair marketplace" — cited for jointly optimizing fairness and relevance in two-sided marketplaces

## Bibliography Fields
- **title:** Fairness in Job Recommendation under Quantity Constraints
- **authors or organization:** Yunqi Li, Hanxiong Chen, Yongfeng Zhang (Rutgers University); Michiharu Yamashita, Dongwon Lee (Penn State University)
- **year:** 2023 (inferred from the source URL `aaai23-fair.pdf`; **no explicit venue/year banner, footer, or copyright line is visible on the pages read** — this is not independently confirmed from in-text content)
- **venue or type:** AAAI 2023, inferred from filename/URL only — **CITATION CORRECTION note applies below**
- **link:** https://pike.psu.edu/publications/aaai23-fair.pdf
- **tier tag:** Tier 2 applied-on-real-platform-data (private real-world dataset with real company/gender/salary fields, though not a live-deployed system evaluation)
- **what they did (≤80 words):** Modeled job recommendation as a resource-allocation problem with per-job upper AND lower quantity quotas (avoid over-exposure/guarantee minimum exposure) plus a gender-based salary-gap fairness constraint, solved as a model-agnostic post-processing 0-1 integer program on top of any base recommender's score, evaluated on a private real dataset across four base models.
- **mechanism relevant to two-sided balancing (≤50 words):** Directly implements a supply-side per-item capacity constraint (upper AND lower quota on how many users a listing is shown to) analogous to reply-capacity limits, combined with a demand-side group-fairness constraint, via model-agnostic re-ranking — composable on top of any existing scorer.
- **metrics used, and the reported effect:** NDCG@10, HR@10, F1@10, UGF@10 ($ salary gap); re-ranking cut UGF@10 from $4,155–$16,050 (baseline) to $952–$980 across 4 base models while accuracy metrics stayed roughly flat or improved.
- **fit for a dating app:** high — the upper+lower quantity-constrained re-ranking is a close structural analogue to per-user reply-capacity allocation (cap over-liked "superstar" exposure, guarantee a floor for under-shown users), is model-agnostic so composes with any reciprocal scorer, and is validated on real interaction data with a real fairness metric and effect size.
- **confidence that the item is real and described correctly:** high for content (read directly); medium for exact venue/year (inferred from URL, not confirmed on the page).

**CITATION CORRECTION:** the manifest tag "AAAI2023" could not be independently confirmed from the PDF text itself — no AAAI conference banner, copyright footer, or proceedings citation appears on the 5 pages read (unlike the companion "Matching Market Design with Constraints" AAAI-22 paper in this same batch, which does show an explicit AAAI banner). The year/venue is carried over from the source URL (`pike.psu.edu/publications/aaai23-fair.pdf`) as the best available evidence, not verified in-text.

## Project Relevance
High relevance to **layer 2 (capacity-aware exposure allocation)** — this is the closest mechanism in this batch to "cap likes/exposure to desirable users, guarantee a floor for under-shown users," expressed as a clean, model-agnostic quota re-ranking optimization with a demonstrated large effect size on a real dataset. Touches **layer 3 (market-design levers)** loosely, since setting quotas is itself a market-design lever, and **layer 4 (ecosystem metrics)** loosely via UGF as a group-fairness outcome metric (though it measures average recommended-item salary, not match-Gini, wasted-likes, or two-sided retention — a narrower metric than the project needs). **Disanalogy to flag:** a job posting's "capacity" here is an externally set business policy (company hiring quota, dialed via company size), not an emergent constraint from a person's own finite time/reply capacity — companies do not reciprocally "swipe back" on individual candidates the way a matched dating user must actively respond, so the *supply-side quota mechanism* transfers well but the *underlying reason for scarcity* does not.

## Reverse Citation Map
