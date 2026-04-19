Date: 2026-04-11
Topic: Learning with Proxy Labels / Surrogate Supervision / Noisy Labels

# Proxy Label Learning - Survey Requirements

## Request

Survey the literature on training supervised models using proxy (surrogate) labels rather than ground-truth labels. The motivating use case is training a model using attribution-derived labels (e.g., Shapley scores) as training signal — not ground truth. Such labels are noisy and encode the assumptions of the attribution model. Key questions:

1. What happens when a model is trained on proxy/surrogate labels instead of ground truth? Does it generalize correctly?
2. How does label noise — especially instance-dependent, feature-dependent, or systematic noise — affect learned model behavior?
3. What are robust training techniques for noisy-label regimes?
4. How does bias from the label-generating process (e.g., attribution model, teacher model, weak labeler) propagate into the student model?
5. When do models trained on proxy labels generalize to the true task?

## Core Keywords

- learning with noisy labels
- proxy labels / surrogate labels / surrogate supervision
- weakly supervised learning
- pseudo labels / self-training
- programmatic weak supervision / data programming
- knowledge distillation (label bias propagation aspect)
- instance-dependent label noise
- label noise robustness / loss correction
- label noise transition matrix
- semi-supervised learning (pseudo-label branch)
- attribution-derived labels / Shapley score supervision
- teacher-student bias propagation
- reward model generalization (RLHF context)

## Target Conferences / Journals

**Primary (Priority 1):**
- NeurIPS, ICML, ICLR — core ML theory and methods venues

**Secondary (Priority 2–3):**
- KDD, WWW, RecSys — industry-relevant applications
- CVPR, ECCV — noisy label work in vision
- ACL, EMNLP — NLP weak supervision applications
- AISTATS — theoretical contributions

**Journals:**
- IEEE TNNLS, JMLR, IEEE TPAMI

## Target Engineering Blogs

- netflixtechblog.com (proxy metrics / surrogate objectives)
- engineering.fb.com (weak supervision at scale)
- research.google (data programming, reward modeling)
- amazon.science (privileged features distillation)
- ai.googleblog.com
- lilianweng.github.io (excellent survey posts on noisy labels, semi-supervised)

## Search Query List

1. `site:arxiv.org learning proxy labels surrogate supervision generalization bias`
2. `site:arxiv.org noisy label learning deep neural networks`
3. `"learning with noisy labels" NeurIPS ICML ICLR 2020 2021 2022 2023 2024`
4. `"programmatic weak supervision" OR "data programming" labeling functions NeurIPS ICML ICLR 2019 2020 2021 2022`
5. `"instance-dependent noise" OR "feature-dependent label noise" model generalization 2021 2022 2023 2024`
6. `"pseudo label bias" OR "confirmation bias" self-training weakly supervised NeurIPS ICML 2021 2022 2023`
7. `"teacher-student" bias soft labels distillation generalization analysis`
8. `Shapley attribution noisy label training generalization bias`
9. `"reward model" proxy label generalization RLHF 2022 2023 2024`
10. `"privileged features distillation" teacher proxy label recommendation ranking`
11. `https://api.semanticscholar.org/graph/v1/paper/search?query=noisy+label+learning+deep+neural+networks&fields=title,year,venue,citationCount,externalIds,authors&limit=25`
12. `https://api.semanticscholar.org/graph/v1/paper/search?query=weakly+supervised+learning+proxy+labels&fields=title,year,venue,citationCount,externalIds,authors&limit=20`

## Survey Scope and Constraints

- **Target number of papers:** 80–120 (proxy-label learning is focused enough that 200 would be excessive; confirming target with user if needed)
- **Year range:** 2019–2026 (except seminal works like Natarajan et al. 2013, Co-teaching 2018, Snorkel 2016-2017)
- **Must include:**
  - Seminal noisy-label learning papers (MentorNet, Co-teaching, DivideMix, PENCIL, ELR)
  - Noise transition matrix estimation methods (Dual-T, T-revision)
  - Instance-dependent noise methods (IDN-specific approaches)
  - Programmatic weak supervision / Snorkel ecosystem
  - Pseudo-label / self-training bias propagation work
  - Knowledge distillation soft-label bias papers
  - Privileged features distillation (proxy labels at recommendation ranking)
  - Reward model generalization in RLHF (proxy reward = proxy label)
  - Survey/overview papers on noisy labels
  - Theoretical papers on generalization under label noise
- **Exclude:**
  - Papers primarily about crowdsourcing annotation aggregation (Dawid-Skene and variants) unless they also study downstream model behavior
  - Domain adaptation papers that only incidentally mention noisy labels
  - Federated learning papers unless primarily about label noise
  - Medical imaging papers unless the label noise methodology is generalizable
  - Papers where "noisy" refers to data/feature noise, not label noise
- **Adjacent-field expansion plan:**
  1. RLHF reward model bias → proxy reward literature
  2. Semi-supervised learning (self-training branch)
  3. Knowledge distillation (bias from teacher)
  4. Curriculum learning (related to sample selection under noise)
  5. Data valuation (Shapley-based, relevant to attribution-derived labels)

## Project Context

**Project:** Attribution-based incremental user retention on a dating platform.

**Two-phase system:**
1. An attribution model assigns fractional credit scores (e.g., Shapley values) to user interactions (conversations, likes, matches) for driving user days-active. These scores are the **proxy labels**.
2. A supervised model is trained on those proxy labels to generalize — predicting the retention contribution of new interactions in real time.

**This survey covers Phase 2** — the supervised learning side, specifically: what happens when the training labels are attribution-derived proxy scores rather than ground truth?

**Key framing for paper evaluation:**
- The proxy labels here are **continuous** (fractional credit scores), not binary — prioritize noisy-label methods that handle continuous or soft labels, not just class-label corruption
- The noise is **systematic and model-induced**: it reflects the assumptions of the attribution model (e.g., Shapley assumes equal marginal contributions), not random annotation error — prioritize papers that study structured/systematic bias over random i.i.d. noise
- The downstream goal is **generalization to new interactions at inference time**, not just fitting the training set — prioritize papers that study whether proxy-label models generalize to true task performance
- **Privileged features distillation** and **RLHF reward model generalization** are high-relevance analogs: in both cases, a proxy signal (teacher output / reward model score) supervises a student model, and the question is whether the student learns the right thing

**What "useful for this project" means:**
- A method is useful if it either (a) provides theoretical guarantees on when proxy-label supervised models generalize, or (b) provides practical techniques for training models robustly under systematic label bias

## Summary of Actual Search Results

- **Total papers:** **86** markdown analyses in `read-papers/` (some legacy duplicate filenames for a few arXiv stubs); NotebookLM main notebook `6fbcf9e6-3833-4660-8b56-67b0b98bf394` holds **95** sources after overflow merge + Phase 3 adds (includes blogs, duplicate URL stubs from arXiv redirects, and industry PDFs).
- **Number of categories:** Six synthesis buckets in `literature-review.md` (sample selection; pseudo-label / SSL; PFD and KD; loss correction and transition models; programmatic weak supervision; RLHF proxy rewards) plus peripheral vision and diffusion notes.
- **Key findings:** Robust learning under **proxy labels** combines **transition-matrix and robust losses**, **small-loss and curriculum selection**, **SSL hybrids (DivideMix-style)**, and **distillation from privileged or teacher signals**. RLHF reward modeling and ranking distillation provide the closest large-scale precedents for **systematic proxy–true mismatch** and **train/serve skew**. **Coverage** against the Request + Must Include + Core Keywords checklist in this file is approximately **96%** (19/20 items have explicit supporting notes in `literature-review.md` / `executive-summary.md`); the remaining gap is **direct theory for continuous Shapley scores as labels**, which is only addressed by analogy through soft-label KD, PFD, and RLHF proxy-reward literature.
