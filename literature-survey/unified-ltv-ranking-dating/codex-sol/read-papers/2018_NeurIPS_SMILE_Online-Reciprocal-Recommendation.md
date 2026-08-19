# Online Reciprocal Recommendation with Theoretical Performance Guarantees

- **Source index:** 120
- **Source ID:** `aef5c663-2ef3-4556-a4b9-4c755be7e23b`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Authors:** Fabio Vitale, Nikos Parotsidis, Claudio Gentile
- **Affiliations:** Sapienza University of Rome, University of Lille/INRIA, University of Rome Tor Vergata, Google
- **Year / venue:** 2018 / NeurIPS
- **Direction / priority:** D8 online reciprocal recommendation / Priority 3 (core)
- **URL:** https://proceedings.neurips.cc/paper/2018/hash/2d6cc4b2d139a53512fb8cbb3086ae2e-Abstract.html

## 1. Summary

The paper models reciprocal recommendation as sequential discovery of mutual positive edges in a bipartite graph. At each round one active user receives one recommendation; a match is revealed only after both directed preferences are queried positively, possibly at different times. Without structure, rapid learning is impossible. Under approximate clusterability of users’ preference rows, SMILE explores representatives, identifies clusters, then exploits shared patterns. Theory shows match discovery comparable up to constants with a clairvoyant matchmaker when the horizon and number of matches are sufficiently large.

I-SMILE, an interleaved implementation, is tested on four 2000×2000 synthetic markets and dense subsets of a public Czech dating dataset (from roughly 1,000×1,286 to 2,265×3,939 users). It clearly outperforms uniform random and an oblivious baseline in match-discovery curves on all tested datasets. Exact area-under-curve improvements are **Not specified in source**.

## 2. Experiment Critique

The paper supplies impossibility results, positive guarantees, computational analysis, and public-data tests. The staged, asynchronous feedback model is realistic for reciprocal apps, and checking cluster radii on real data partially validates the structural assumption.

The empirical benchmark is heavily densified by repeatedly removing users with few ratings; missing ratings are treated as dislikes and ratings above two as likes. This selection and binarization differ from production exposure logs. Baselines are intentionally simple, feedback is noiseless and stationary in the main model, the two sides are conceptually balanced, and login frequencies are omitted. No live experiment or long-term welfare outcome is reported.

## 3. Industry Contribution / Project Relevance

SMILE contributes the exploration side of dating recommendation: mutual preference is sparse, delayed, and costly to discover, so cluster structure can reduce sample complexity. Interleaving exploration and exploitation is more relevant than a one-time offline preference model for new users and changing markets.

For unified LTV, the discovery reward must extend beyond mutual likes to conversations, retention, and revenue, while respecting candidate attention. Cluster-based exploration can also reinforce stereotypes or expose users unfairly, so production use needs uncertainty, individual overrides, privacy checks, and load constraints. The theory does not address causal long-term effects or congestion.

## 4. Novelty

This is an early rigorous sequential-learning treatment of reciprocal recommendation, with limits absent structure and near-clairvoyant match-discovery guarantees under clusterability.

## 5. Dataset Availability

The Czech dating ratings dataset cited from Brozovsky and Petricek is public. An official code repository is **Not specified in source**.

## 6. Community Reaction

Not specified in source beyond NeurIPS 2018 publication.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## 8. Meta Information

- **Feedback:** Binary directed like/dislike
- **Interaction:** One active user and one recommendation per round
- **Objective:** Number of mutual likes discovered by horizon T
- **Assumption:** Approximate preference clusterability
- **Long-term/interference modeling:** None
- **Project role:** Reciprocal exploration/cold-start theory
