# Survey Card

| Field | Value |
|-------|-------|
| **Title** | The Surrogate Index: Combining Short-Term Proxies to Estimate Long-Term Treatment Effects More Rapidly and Precisely |
| **Authors** | Susan Athey, Raj Chetty, Guido W. Imbens, Hyunseung Kang |
| **Venue** | NBER Working Paper 26463 (rev. 2024) |
| **Year** | 2019 (rev. 2024) |
| **Type** | Academic |
| **Survey Phase** | D3 — Surrogates / Evaluation |
| **NLM Source ID** | f19c6829-6721-46d7-b6b5-9fc1301a9b16 |
| **PDF** | https://www.nber.org/system/files/working_papers/w26463/w26463.pdf |
| **One-line summary** | Formal surrogate-index framework combining experimental + observational samples to estimate long-term treatment effects from short-term proxies. |
| **Core mechanism** | Data fusion under Unconfoundedness + Surrogacy (Prentice) + Comparability; surrogate index \(\mu(s,x,O) = E[Y|S,X,O]\). |

**Dating applicability:** Foundational method for combining multiple short-horizon experiment metrics (matches, replies, session length) into a single surrogate index predicting 90-day retention — using observational logs to learn the proxy→outcome mapping and a held-out experiment arm to estimate treatment effects.

---

# Paper Reader

## 1. Problem & Motivation

Primary outcomes (lifetime earnings, long-term employment, mortality) are observed with long delay. Researchers have short-term proxies and need timely, principled treatment-effect estimates — not ad-hoc qualitative weighting of disparate short-run metrics.

## 2. Method

**Data fusion setup:**
- **Experimental sample** (\(P_i=E\)): observe \(W_i, S_i, X_i\); **\(Y_i\) missing**
- **Observational sample** (\(P_i=O\)): observe \(S_i, X_i, Y_i\); **\(W_i\) missing**

**Three assumptions:**
1. **Unconfoundedness:** Random assignment in experimental sample
2. **Surrogacy (Prentice):** \(W_i \perp Y_i \mid S_i, X_i, P_i=E\) — treatment effect fully mediated by surrogates
3. **Comparability:** \(P_i \perp Y_i \mid S_i, X_i\) — outcome distribution identical across samples

**Surrogate index:** \(\mu(s,x,p) = E[Y_i \mid S_i=s, X_i=x, P_i=p]\)

**Estimators:** Surrogate Index, Surrogate Score, Influence Function (doubly robust), Double Matching.

Under surrogacy + comparability: ATE on surrogate index equals ATE on long-term outcome.

## 3. Evaluation

**GAIN job training program (California, 1980s):**
- **Experimental:** Riverside county RCT (\(N_E=5{,}445\)); long-term outcomes withheld
- **Observational:** Alameda, Los Angeles, San Diego (\(N_O=13{,}725\)); treatment withheld
- **Surrogates:** Quarterly employment, earnings, aid receipt for first \(t\) quarters (\(t=1..36\))
- **Primary outcomes:** 36-quarter (9-year) average employment rate and earnings

**Baselines:** 36-quarter experimental benchmark; naive estimator (short-run TE as long-run TE).

## 4. Key Results

**Experimental benchmark:** +6.4 pp employment (s.e. 1.2); +\$249 earnings (s.e. \$83) over 36 quarters.

**At t=6 quarters (employment):**

| Estimator | Estimate (s.e.) |
|-----------|-----------------|
| Naive | 0.117 (0.010) |
| Surrogacy Index | **0.061 (0.006)** |
| Surrogacy Score | **0.063 (0.006)** |
| Influence Function | **0.065 (0.006)** |

All three surrogate estimators within 2 SE of benchmark at **t≥5 quarters**; naive takes **>25 quarters**.

**Earnings at t=6:** Surrogacy Index \$238.8 (s.e. \$31.5) vs benchmark \$249.

**Precision gain:** With 6-quarter surrogates, SE incorporating surrogacy is **0.33×** the SE without surrogacy knowledge.

**Assumption tests:** Surrogacy violated at t≤3 (significant direct treatment effects); comparability persistently violated (Riverside "jobs first" vs other sites' human-capital focus).

## 5. Limitations

- Surrogacy, Comparability, Unconfoundedness are strong; violations yield wide bounds.
- Unbounded outcomes: uninformative bounds if surrogacy/comparability fail.
- GAIN validation shows surrogacy violated at short horizons; comparability violated due to site heterogeneity.
- Naive estimator performs very poorly.
- Not a recommender-system paper; clickbait example is illustrative only.

## 6. Prior Work Cited

Prentice (1989) surrogate endpoints; Baron & Kenny (1986) mediation; Day & Duffy (1996) trial design; Frangakis & Rubin (2002) principal stratification; LaLonde (1986) experimental validation; Rosenbaum & Rubin (1983b) propensity score; Rässler (2004, 2012) data fusion.

---

# Project Relevance

**Foundational for D3.** Establishes the surrogate-index formalism that downstream industry papers (Tripuraneni 2024, LOPE 2024, Impatient Bandits, industry workshop) build on. For dating: provides the statistical template for fusing short-horizon experiment metrics with observational retention data to estimate long-term treatment effects without waiting for full label maturity. Directly addresses incrementality (ATE) not prediction. No ranking model, credit assignment, two-sided market, or CTR migration path.

---

# Reverse Citation Map

| This paper cites → | Notes |
|--------------------|-------|
| | |

| ← Cited by this survey | Notes |
|------------------------|-------|
| | |

---

# Meta Information

| Field | Value |
|-------|-------|
| **Card date** | 2026-08-16 |
| **Workplace** | cursor-grok |
| **Reader** | NotebookLM Q1–Q3 (source f19c6829-6721-46d7-b6b5-9fc1301a9b16) |
| **Community Reaction** | No significant community discussion found. |
