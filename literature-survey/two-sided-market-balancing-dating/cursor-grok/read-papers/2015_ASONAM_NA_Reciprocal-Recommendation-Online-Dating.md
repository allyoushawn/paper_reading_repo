# 2015 ASONAM — Reciprocal Recommendation System for Online Dating

**Title:** Reciprocal Recommendation System for Online Dating  
**Authors:** Peng Xia, Benyuan Liu, Yizhou Sun, Cindy Chen  
**Year / venue:** 2015, ASONAM  
**Link:** https://arxiv.org/abs/1501.06247  
**Tier:** 2  
**nlm:** f3e7044f-0935-451f-840f-1b0baaa35cd4 (in shared queue; not re-extracted via NLM this run)

## Summary
Baihe.com (Chinese heterosexual dating site): 60M registered users; 200k sampled (Nov 2011 registrations; 139k male / 61k female) with send/reply traces. Reciprocal score from content prefs plus **interest similarity** (shared recipients) and **attractiveness similarity** (shared senders). CF variants beat content-based and beat RECON / HCF on precision and recall (figures; no single headline %). Behavioral result: men optimize their own interest and ignore inbound attractiveness; women do both.

## Project Relevance
**High** as the Chinese-dating *data* card (Baihe, not 探探). Scoring is RECON-family, not capacity-aware. Does not substitute for a Tantan/Momo/Soul engineering ranking post.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|------------|------|--------------|
| [2023_IEEEAccess_GFRR_Graph-Fusion-Reciprocal.md](./2023_IEEEAccess_GFRR_Graph-Fusion-Reciprocal.md) | related work | Cited as a collaborative-filtering RRS on dating; GFRR replaces CF similarities with send/reply GNNs. |
