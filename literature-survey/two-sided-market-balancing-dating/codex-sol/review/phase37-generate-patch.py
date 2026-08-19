from collections import defaultdict
from pathlib import Path


workplace = Path(__file__).resolve().parent.parent
raw = (workplace / "review/phase37-codex-raw.txt").read_text()
relations = defaultdict(list)

for line in raw.splitlines():
    if not line.startswith("RELATION | "):
        continue
    parts = line.split(" | ")
    if len(parts) != 7:
        continue
    _, target, mentioning, classification, context, summary, _ = parts

    # The reviewer explicitly acknowledged mapping Pizzato et al. (2010) and
    # bare RECON mentions to the distinct 2013 UMUAI card. Keep only the
    # survey's explicit title-level mention of the 2013 paper.
    if (
        target == "2013_UMUAI_RECON_Recommending-People-To-People.md"
        and mentioning
        != "2021_InfoFusion_NA_Reciprocal-Recommender-Systems-Survey.md"
    ):
        continue

    row = (
        f"| [{mentioning}](./{mentioning}) | {context} — {classification} | "
        f"{summary} |"
    )
    relations[target].append(row)

cards = sorted((workplace / "read-papers").glob("*.md"))
print("*** Begin Patch")
for card in cards:
    rows = relations.get(card.name) or [
        "| No verified inbound mentions within the 45-source corpus. | — | — |"
    ]
    print(f"*** Update File: {card}")
    print("@@")
    print("-| Mentioning Paper | Section | Summary of Mention |")
    print("-|-----------------|---------|-------------------|")
    print("-| (To be filled in during Phase 3.7) | | |")
    print("+| Mentioning Paper | Mention Context | Summary of Original Wording |")
    print("+|------------------|-----------------|-----------------------------|")
    for row in rows:
        print(f"+{row}")
print("*** End Patch")

print(
    f"Verified relations after strict paper-identity filtering: "
    f"{sum(map(len, relations.values()))}",
    file=__import__("sys").stderr,
)
