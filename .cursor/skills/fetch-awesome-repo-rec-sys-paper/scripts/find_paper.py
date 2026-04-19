#!/usr/bin/env python3
"""Search Awesome list README for papers; print title, repo-relative path, URL."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

# paper_reading_repo/.cursor/skills/<this-skill>/scripts/find_paper.py -> repo root is parents[4]
_REPO_ROOT = Path(__file__).resolve().parents[4]
_SIBLING_README = (
    _REPO_ROOT.parent
    / "Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising"
    / "README.md"
)


def _default_readme() -> str:
    env = os.environ.get("AWESOME_REC_SYS_README")
    if env:
        return env
    if _SIBLING_README.is_file():
        return str(_SIBLING_README)
    return "/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/README.md"


DEFAULT_README = _default_readme()

HEADING_RE = re.compile(r"^##\s+(.+)$")
# PDF links in this README use guyulongcs/Deep-Learning-for-Search-Recommendation-Advertisements
URL_PREFIX = (
    "(https://github.com/guyulongcs/Deep-Learning-for-Search-Recommendation-Advertisements/blob/"
)


def strip_md_noise(text: str) -> str:
    return re.sub(r"[*_`]+", "", text).strip()


def extract_markdown_github_pdf_links(line: str) -> list[tuple[str, str]]:
    """Parse [title](url) pairs; handles nested brackets in titles."""
    out: list[tuple[str, str]] = []
    start = 0
    while True:
        u = line.find(URL_PREFIX, start)
        if u < 0:
            break
        paren_open = u
        bracket_close = paren_open - 1
        if bracket_close < 0 or line[bracket_close] != "]":
            start = u + 1
            continue
        depth = 1
        p = bracket_close - 1
        t_open = -1
        while p >= 0:
            if line[p] == "]":
                depth += 1
            elif line[p] == "[":
                depth -= 1
                if depth == 0:
                    t_open = p
                    break
            p -= 1
        if t_open < 0:
            start = u + 1
            continue
        title = line[t_open + 1 : bracket_close]
        paren_close = line.find(")", paren_open)
        if paren_close < 0:
            break
        url = line[paren_open + 1 : paren_close]
        base = url.split("?", 1)[0].lower()
        if base.endswith(".pdf"):
            out.append((title, url))
        start = paren_close + 1
    return out


def blob_relative_path(url: str) -> str | None:
    if "/blob/" not in url:
        return None
    rest = url.split("/blob/", 1)[1]
    slash = rest.find("/")
    if slash < 0:
        return None
    rel = rest[slash + 1 :]
    return unquote(rel)


def token_match(haystack_lower: str, token: str) -> bool:
    """Match token as whole word (alphanumeric/hyphen tokens) to avoid e.g. dien ⊂ gradient."""
    if re.fullmatch(r"[\w-]+", token, re.ASCII):
        pat = rf"(?<![\w-]){re.escape(token)}(?![\w-])"
        return re.search(pat, haystack_lower, re.IGNORECASE) is not None
    return token.lower() in haystack_lower


def line_matches_tokens(haystack: str, tokens: list[str]) -> bool:
    h = haystack.lower()
    return all(token_match(h, t) for t in tokens)


def main() -> int:
    p = argparse.ArgumentParser(description="Find paper paths from Awesome README links.")
    p.add_argument(
        "query",
        nargs="+",
        help="Keywords; every token must match (case-insensitive) in title or path.",
    )
    p.add_argument(
        "--readme",
        default=DEFAULT_README,
        help="Path to README.md (default: env AWESOME_REC_SYS_README, else sibling Awesome clone, else legacy path)",
    )
    p.add_argument(
        "--max",
        type=int,
        default=50,
        help="Max results to print (default 50).",
    )
    args = p.parse_args()
    tokens = [t.lower() for t in args.query if t.strip()]

    path = os.path.expanduser(args.readme)
    if not os.path.isfile(path):
        print(f"README not found: {path}", file=sys.stderr)
        return 2

    section = ""
    matches: list[tuple[str, str, str, str]] = []

    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            hm = HEADING_RE.match(line.strip())
            if hm:
                section = hm.group(1).strip()
                continue
            for title_raw, url in extract_markdown_github_pdf_links(line):
                rel = blob_relative_path(url)
                if not rel or not rel.lower().endswith(".pdf"):
                    continue
                title = strip_md_noise(title_raw)
                blob = f"{title} {rel} {url}".lower()
                if not line_matches_tokens(blob, tokens):
                    continue
                matches.append((section, title, rel, url))

    if not matches:
        print("No matches.", file=sys.stderr)
        return 1

    for i, (sec, title, rel, url) in enumerate(matches[: args.max], 1):
        print(f"{i}. [{sec}] {title}")
        print(f"   path: {rel}")
        print(f"   url:  {url}")
        print()

    if len(matches) > args.max:
        print(f"... and {len(matches) - args.max} more (use --max)", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
