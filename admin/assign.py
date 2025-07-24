import pandas as pd
from collections import defaultdict
from itertools import cycle

HEAVY_REVIEWERS = ["nate", "nathan"]
LIGHT_REVIEWERS = ["peter", "greg", "andrea", "misty", "will", "pranav", "ryan"]
INPUT_CSV = "attendees.csv"
OUTPUT_MD = "reviewer_assignments.md"

df = pd.read_csv(INPUT_CSV)

non_speakers = df[
    df["Would you like to propose a talk or session?"].str.strip().str.lower() != "yes"
]

applicants = non_speakers.reset_index(drop=True)

assignments = []
review_counts = defaultdict(int)
heavy_cycle = cycle(HEAVY_REVIEWERS)
light_cycle = cycle(LIGHT_REVIEWERS)

for idx, row in applicants.iterrows():
    name = row["Name"]
    email = row["Email"]
    affiliation = row.get("Affiliation", "")
    title = row.get("Job title/role", "")
    support = row.get("Do you need financial support to attend?", "")
    motivation = row.get(
        "Why would you like to attend WERQSHOP? What would you like to get out of the event? Do you have experience in the error mitigation/resilience space?",
        "",
    )

    heavy = next(heavy_cycle)
    light = next(light_cycle)

    app_info = {
        "name": name,
        "email": email,
        "affiliation": affiliation,
        "title": title,
        "support": support,
        "motivation": motivation,
        "reviewers": [heavy, light],
    }

    assignments.append(app_info)
    review_counts[heavy] += 1
    review_counts[light] += 1

md_lines = ["# WERQSHOP Application Review\n"]

for i, app in enumerate(assignments, 1):
    md_lines.append(f"## {i}. {app['name']}\n")
    md_lines.append(f"- **Email**: {app['email']}")
    md_lines.append(f"- **Affiliation**: {app['affiliation']}")
    md_lines.append(f"- **Job Title**: {app['title']}")
    md_lines.append(f"- **Financial Support Requested**: {app['support']}")
    md_lines.append(f"- **Motivation**:\n\n> {app['motivation'] or '_No response_'}\n")

    for reviewer in app["reviewers"]:
        md_lines.append(f"### Review by {reviewer.capitalize()}")
        md_lines.append("- **Score**: ________\n\n")
    md_lines.append("### Review by ...")
    md_lines.append("- name: **Score**: ________\n\n")
    md_lines.append("- name: **Score**: ________\n\n")
    md_lines.append("**Notes**:\n\n - ... \n")
    md_lines.append("\n---\n")

print(review_counts)

with open(OUTPUT_MD, "w") as f:
    f.write("\n".join(md_lines))
