#!/usr/bin/env python3
"""Mechanical author-following and topic harvest over OpenAlex and arXiv (no LLM).

Writes harvest.md (follow log + candidate table) and harvest.json next to this file.
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
PARENT_READ = os.path.join(HERE, "..", "..", "read-papers")
FROM_DATE = "2025-01-01"
MAILTO = "allyoushawn@gmail.com"
UA = f"attribution-survey-harvest/1.0 (mailto:{MAILTO})"

TOPIC_RE = re.compile(
    r"attribut|incrementalit|uplift|causal|conversion|retention|engagement|touchpoint|touch-point|"
    r"shapley|credit assign|counterfactual|\blift\b|treatment effect|marketing|advertis|recommend|"
    r"churn|survival|long-term|long term|lifetime value|\bltv\b|surrogate|holdout|geo experiment|"
    r"switchback|notification|user return|days active|multi-touch|journey",
    re.I,
)

# (display name, institution hint substring, group)
AUTHORS = [
    ("Florian Zettelmeyer", "Northwestern", "Amazon Ads / Northwestern"),
    ("Randall A. Lewis", "Amazon", "Amazon Ads"),
    ("Brett R. Gordon", "Northwestern", "Meta / Northwestern"),
    ("Robert Moakler", "Meta", "Meta"),
    ("Johannes Hermle", "Amazon", "Amazon Ads"),
    ("Cristobal Garib", "Amazon", "Amazon Ads"),
    ("Sishuo Chen", "Alibaba", "Alibaba / Alimama"),
    ("Zhangming Chan", "Alibaba", "Alibaba / Alimama"),
    ("Xiang-Rong Sheng", "Alibaba", "Alibaba / Alimama"),
    ("Han Zhu", "Alibaba", "Alibaba / Alimama"),
    ("Jian Xu", "Alibaba", "Alibaba / Alimama"),
    ("Bo Zheng", "Alibaba", "Alibaba / Alimama"),
    ("Aiyou Chen", "Google", "Google"),
    ("Nicolas Remy", "Google", "Google"),
    ("Marco Longfils", "Google", "Google"),
    ("Dinah Shender", "Google", "Google"),
    ("Stephanie Sapp", "Google", "Google"),
    ("Jon Vaver", "Google", "Google"),
    ("Mukund Sundararajan", "Google", "Google"),
    ("Badih Ghazi", "Google", "Google"),
    ("Pasin Manurangsi", "Google", "Google"),
    ("Lorne Applebaum", "Google", "Google"),
    ("Claudio Gentile", "Google", "Google"),
    ("Robert Busa-Fekete", "Google", "Google"),
    ("Xiangyu Zeng", "Meta", "Meta"),
    ("Amit Jaspal", "Meta", "Meta"),
    ("Julian Runge", "", "Meta / academia (Robyn)"),
    ("Rohan Arava", "Adobe", "Adobe"),
    ("Ritwik Sinha", "Adobe", "Adobe"),
    ("David Arbour", "Adobe", "Adobe"),
    ("Eustache Diemert", "Criteo", "Criteo"),
    ("Damien Lefortier", "", "Criteo"),
    ("Ruihuan Du", "", "JD.com"),
    ("Harikesh S. Nair", "Stanford", "JD.com / Stanford"),
    ("Dongdong Yang", "Southern California", "eBay / USC"),
    ("Sang Su Lee", "Thumbtack", "Thumbtack"),
    ("Weinan Zhang", "Shanghai Jiao Tong", "SJTU"),
    ("Kan Ren", "", "SJTU / Microsoft"),
    ("Jun Wang", "University College London", "UCL"),
    ("Di Yao", "Chinese Academy of Sciences", "ICT / CAS"),
    ("Chang Gong", "Chinese Academy of Sciences", "ICT / CAS"),
    ("Jingping Bi", "Chinese Academy of Sciences", "ICT / CAS"),
    ("Jiaming Tang", "Michigan", "U Michigan"),
    ("Liping Jing", "Beijing Jiaotong", "BJTU"),
    ("Sachin Kumar", "Tata", "TCS Research"),
    ("Balaraman Ravindran", "Indian Institute of Technology Madras", "IIT Madras"),
    ("Susan Athey", "Stanford", "Stanford"),
    ("Stefan Wager", "Stanford", "Stanford"),
    ("Xinkun Nie", "", "Stanford"),
    ("Foster Provost", "New York University", "NYU"),
    ("Brian Dalessandro", "", "NYU / industry"),
    ("Claudia Perlich", "", "NYU / industry"),
    ("Yixuan An", "Renmin", "Renmin / PKU"),
    ("Zihe Wang", "Renmin", "Renmin"),
    ("Yingfei Wang", "", "Renmin / PKU"),
    ("Eva Anderl", "", "Markov attribution"),
    ("Kaifeng Zhao", "", "Shapley MTA"),
    ("Elisenda Molina", "Carlos III", "UC3M"),
    ("Victor Churchill", "Trinity", "Trinity College"),
    ("Iason Filippou", "Crete", "U Crete"),
    ("Ioannis Tsamardinos", "Crete", "U Crete"),
    ("Qingpeng Cai", "Kuaishou", "Kuaishou"),
    ("Shuchang Liu", "Kuaishou", "Kuaishou"),
    ("Kun Gai", "Kuaishou", "Kuaishou"),
    ("Peng Jiang", "Kuaishou", "Kuaishou"),
    ("Xiangyu Zhao", "City University of Hong Kong", "CityU HK / Kuaishou collab"),
    ("Ezra Berger", "DoorDash", "DoorDash"),
    ("Jared Bauman", "DoorDash", "DoorDash"),
]

OPENALEX_TOPICS = [
    "multi-touch attribution",
    "data-driven attribution advertising",
    "conversion attribution causal",
    "incrementality measurement advertising",
    "attribution calibration experiment advertising",
    "Shapley attribution touchpoint",
    "customer journey attribution neural",
    "retention attribution in-app interactions",
    "user retention reinforcement learning recommendation",
    "long-term user engagement credit assignment recommender",
    "notification incrementality retention",
    "dating app recommendation retention",
    "surrogate index long-term outcome retention",
    "counterfactual removal effect user retention",
]

ARXIV_TOPICS = [
    'all:"multi-touch attribution"',
    'all:"data-driven attribution"',
    'all:"conversion attribution"',
    'all:attribution AND all:incrementality',
    'all:attribution AND all:advertising AND all:causal',
    'all:"user retention" AND all:recommend',
    'all:retention AND all:"reinforcement learning" AND all:recommend',
    'all:"retention" AND all:"credit assignment"',
    'all:"long-term" AND all:engagement AND all:recommend',
    'all:"dating" AND all:recommend',
    'all:notification AND all:retention',
    'all:"days active" OR all:"daily active" AND all:causal',
    'all:"surrogate index"',
]


def get_json(url, sleep=1.0):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                data = json.loads(r.read().decode())
            time.sleep(sleep)
            return data
        except Exception as e:  # noqa: BLE001
            err = str(e)
            time.sleep(3 * (attempt + 1))
    return {"__error__": err}


def get_text(url, sleep=3.0):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read().decode()
            time.sleep(sleep)
            return data
        except Exception as e:  # noqa: BLE001
            err = str(e)
            time.sleep(3 * (attempt + 1))
    return "__error__:" + err


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def load_parent_index():
    ids, titles = set(), []
    if not os.path.isdir(PARENT_READ):
        return ids, titles
    for fn in os.listdir(PARENT_READ):
        if not fn.endswith(".md"):
            continue
        stem = fn[:-3]
        parts = stem.split("_", 3)
        if len(parts) == 4:
            titles.append(norm(parts[3].replace("-", " ")))
        try:
            with open(os.path.join(PARENT_READ, fn), encoding="utf-8", errors="ignore") as f:
                head = f.read(4000)
            for m in re.finditer(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", head):
                ids.add(m.group(1))
        except OSError:
            pass
    return ids, titles


def already_covered(title, arxiv_id, parent_ids, parent_titles):
    if arxiv_id and arxiv_id in parent_ids:
        return True
    n = norm(title)
    if len(n) < 20:
        return False
    for t in parent_titles:
        if len(t) >= 20 and (n[:40] in t or t[:40] in n):
            return True
    return False


def abstract_from_inverted(inv):
    if not inv:
        return ""
    pos = {}
    for w, idxs in inv.items():
        for i in idxs:
            pos[i] = w
    return " ".join(pos[i] for i in sorted(pos))


def openalex_author_id(name, hint):
    q = urllib.parse.quote(name)
    data = get_json(f"https://api.openalex.org/authors?search={q}&per-page=10&mailto={MAILTO}")
    if "__error__" in data:
        return None, f"error: {data['__error__'][:80]}"
    results = data.get("results", [])
    if not results:
        return None, "no OpenAlex author"
    if hint:
        for a in results:
            insts = " ".join(i.get("display_name", "") for i in a.get("last_known_institutions", []) or [])
            affs = " ".join(x.get("institution", {}).get("display_name", "") for x in a.get("affiliations", []) or [])
            if hint.lower() in (insts + " " + affs).lower():
                return a["id"], f"matched institution '{hint}'"
        # fall back: single strong candidate
        if len(results) == 1 or results[0].get("works_count", 0) >= 5 * max(1, results[1].get("works_count", 0)):
            return results[0]["id"], "unverified (no institution match; dominant candidate)"
        return None, f"ambiguous ({len(results)} candidates, none at '{hint}')"
    return results[0]["id"], "unverified (no hint; top candidate)"


def openalex_works(filter_expr, search=None):
    sel = "id,title,publication_year,publication_date,primary_location,authorships,ids,abstract_inverted_index"
    url = f"https://api.openalex.org/works?filter={filter_expr}&per-page=50&sort=publication_date:desc&select={sel}&mailto={MAILTO}"
    if search:
        url += f"&search={urllib.parse.quote(search)}"
    data = get_json(url)
    if "__error__" in data:
        return None, data["__error__"]
    return data.get("results", []), None


def work_row(w, source):
    title = w.get("title") or ""
    auths = [a.get("author", {}).get("display_name", "") for a in w.get("authorships", [])][:3]
    insts = []
    for a in w.get("authorships", []):
        for i in a.get("institutions", []) or []:
            n = i.get("display_name")
            if n and n not in insts:
                insts.append(n)
    loc = (w.get("primary_location") or {}).get("source") or {}
    venue = loc.get("display_name") or ""
    ids = w.get("ids", {}) or {}
    arx = ""
    for v in ids.values():
        m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", str(v))
        if m:
            arx = m.group(1)
    url = f"https://arxiv.org/pdf/{arx}.pdf" if arx else (ids.get("doi") or w.get("id") or "")
    abstract = abstract_from_inverted(w.get("abstract_inverted_index"))
    return {
        "year": w.get("publication_year"),
        "date": w.get("publication_date"),
        "title": title,
        "authors": ", ".join(auths),
        "affiliation": "; ".join(insts[:3]),
        "venue": venue,
        "url": url,
        "arxiv": arx,
        "topic_hit": bool(TOPIC_RE.search(title + " " + abstract[:1500])),
        "source": source,
    }


def arxiv_query(q, max_results=50):
    url = f"http://export.arxiv.org/api/query?search_query={urllib.parse.quote(q)}&sortBy=submittedDate&sortOrder=descending&max_results={max_results}"
    txt = get_text(url)
    if txt.startswith("__error__"):
        return None, txt
    ns = {"a": "http://www.w3.org/2005/Atom"}
    try:
        root = ET.fromstring(txt)
    except ET.ParseError as e:
        return None, f"parse error {e}"
    rows = []
    for e in root.findall("a:entry", ns):
        pub = (e.findtext("a:published", default="", namespaces=ns) or "")[:10]
        if pub < FROM_DATE:
            continue
        title = re.sub(r"\s+", " ", e.findtext("a:title", default="", namespaces=ns) or "").strip()
        summ = re.sub(r"\s+", " ", e.findtext("a:summary", default="", namespaces=ns) or "").strip()
        aid = (e.findtext("a:id", default="", namespaces=ns) or "").rsplit("/", 1)[-1]
        aid = re.sub(r"v\d+$", "", aid)
        auths = [a.findtext("a:name", default="", namespaces=ns) for a in e.findall("a:author", ns)][:3]
        rows.append({
            "year": int(pub[:4]) if pub else None,
            "date": pub,
            "title": title,
            "authors": ", ".join(auths),
            "affiliation": "",
            "venue": "arXiv",
            "url": f"https://arxiv.org/pdf/{aid}.pdf",
            "arxiv": aid,
            "topic_hit": bool(TOPIC_RE.search(title + " " + summ[:1500])),
            "source": f"arxiv:{q}",
            "abstract": summ[:400],
        })
    return rows, None


def main():
    parent_ids, parent_titles = load_parent_index()
    follow_log = []
    candidates = {}

    def add(row, how):
        if not row["topic_hit"]:
            return False
        key = row["arxiv"] or norm(row["title"])[:60]
        if not key:
            return False
        row = dict(row)
        row["covered"] = already_covered(row["title"], row["arxiv"], parent_ids, parent_titles)
        if key in candidates:
            candidates[key]["how"] += "; " + how
            return True
        row["how"] = how
        candidates[key] = row
        return True

    # 1. OpenAlex author following
    for name, hint, group in AUTHORS:
        aid, note = openalex_author_id(name, hint)
        if not aid:
            follow_log.append((f"{name} ({group})", "OpenAlex author search", note))
            continue
        short = aid.rsplit("/", 1)[-1]
        works, err = openalex_works(f"authorships.author.id:{short},from_publication_date:{FROM_DATE}")
        if err:
            follow_log.append((f"{name} ({group})", f"OpenAlex works {short}", f"error: {err[:80]}"))
            continue
        hits = []
        for w in works:
            r = work_row(w, f"openalex-author:{name}")
            if add(r, f"OpenAlex author {name}"):
                hits.append(r["title"][:70])
        res = f"{len(hits)} relevant of {len(works)} works 2025–26 [{note}]"
        if hits:
            res += ": " + " | ".join(hits[:6])
        follow_log.append((f"{name} ({group})", f"OpenAlex works {short}", res))
        print(f"[author] {name}: {len(hits)}/{len(works)}", file=sys.stderr)

    # 2. arXiv author following (distinctive names only)
    for name, hint, group in AUTHORS:
        last = name.split()[-1]
        first = name.split()[0]
        if len(last) < 5 and last not in ("Nair", "Zhao", "Gong", "Tang"):
            continue
        q = f'au:"{first} {last}"' if len(last) < 7 else f"au:{last}"
        rows, err = arxiv_query(q, 40)
        if err:
            follow_log.append((f"{name} ({group})", f"arXiv {q}", f"error: {err[:80]}"))
            continue
        hits = [r["title"][:70] for r in rows if add(r, f"arXiv author {name}")]
        res = f"{len(hits)} relevant of {len(rows)} arXiv 2025–26"
        if hits:
            res += ": " + " | ".join(hits[:6])
        follow_log.append((f"{name} ({group})", f"arXiv {q}", res))
        print(f"[arxiv-author] {name}: {len(hits)}/{len(rows)}", file=sys.stderr)

    # 3. OpenAlex topic queries
    for t in OPENALEX_TOPICS:
        works, err = openalex_works(f"from_publication_date:{FROM_DATE}", search=t)
        if err:
            follow_log.append((f"topic: {t}", "OpenAlex search", f"error: {err[:80]}"))
            continue
        hits = [work_row(w, f"openalex-topic:{t}") for w in works]
        n = sum(1 for r in hits if add(r, f"OpenAlex topic '{t}'"))
        follow_log.append((f"topic: {t}", "OpenAlex search 2025+", f"{n} relevant of {len(works)}"))
        print(f"[oa-topic] {t}: {n}/{len(works)}", file=sys.stderr)

    # 4. arXiv topic queries
    for q in ARXIV_TOPICS:
        rows, err = arxiv_query(q, 60)
        if err:
            follow_log.append((f"topic: {q}", "arXiv search", f"error: {err[:80]}"))
            continue
        n = sum(1 for r in rows if add(r, f"arXiv topic {q}"))
        follow_log.append((f"topic: {q}", "arXiv search 2025+", f"{n} relevant of {len(rows)}"))
        print(f"[arxiv-topic] {q}: {n}/{len(rows)}", file=sys.stderr)

    rows = sorted(candidates.values(), key=lambda r: (r.get("date") or ""), reverse=True)
    with open(os.path.join(HERE, "harvest.json"), "w", encoding="utf-8") as f:
        json.dump({"generated": str(date.today()), "follow_log": follow_log, "candidates": rows}, f, indent=1)

    with open(os.path.join(HERE, "harvest.md"), "w", encoding="utf-8") as f:
        f.write(f"# Harvest — OpenAlex + arXiv author following and topic queries (generated {date.today()})\n\n")
        f.write("Mechanical output. `topic_hit` = title/abstract matched the topic regex. `covered` = already in parent `read-papers/`.\n\n")
        f.write("## Follow log\n\n| # | target | method | result |\n|---|---|---|---|\n")
        for i, (a, b, c) in enumerate(follow_log, 1):
            f.write(f"| {i} | {a} | {b} | {c.replace('|', '/')} |\n")
        f.write("\n## Candidates (topic-matched, 2025-01 onward)\n\n")
        f.write("| # | date | title | authors | affiliation | venue | url | covered | how found |\n|---|---|---|---|---|---|---|---|---|\n")
        for i, r in enumerate(rows, 1):
            f.write(
                f"| {i} | {r.get('date') or r.get('year')} | {r['title'].replace('|', '/')} | {r['authors'].replace('|', '/')} | "
                f"{r['affiliation'].replace('|', '/')} | {r['venue'].replace('|', '/')} | {r['url']} | "
                f"{'yes' if r['covered'] else ''} | {r['how'].replace('|', '/')[:120]} |\n"
            )
    print(f"done: {len(follow_log)} follow rows, {len(rows)} candidates", file=sys.stderr)


if __name__ == "__main__":
    main()
