import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find milestone "Bug Bash Week"
    bug_bash_milestone = None
    for ms in state.get("milestones", []):
        if ms.get("title") == "Bug Bash Week":
            bug_bash_milestone = ms
            break
    if bug_bash_milestone is None:
        return False, "Could not find milestone 'Bug Bash Week'."

    # Check dates
    if bug_bash_milestone.get("startDate") != "2026-03-10":
        return False, f"Milestone 'Bug Bash Week' has startDate='{bug_bash_milestone.get('startDate')}', expected '2026-03-10'."
    if bug_bash_milestone.get("dueDate") != "2026-03-14":
        return False, f"Milestone 'Bug Bash Week' has dueDate='{bug_bash_milestone.get('dueDate')}', expected '2026-03-14'."

    bug_bash_id = bug_bash_milestone["id"]

    # Find label "type::bug"
    bug_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "type::bug":
            bug_label = lbl
            break
    if bug_label is None:
        return False, "Could not find label 'type::bug'."
    bug_label_id = bug_label["id"]

    # Expected open bug issues that had no milestone (by title)
    expected_titles = [
        "File upload fails silently for files > 50MB",
        "Fix dropdown menu position clipping at viewport edges",
        "Fix typo in 404 error page message",
    ]

    issues_by_title = {}
    for issue in state.get("issues", []):
        if issue.get("title") in expected_titles:
            issues_by_title[issue.get("title")] = issue

    missing = [t for t in expected_titles if t not in issues_by_title]
    if missing:
        return False, f"Could not find expected open bug issues: {missing}"

    # Check each issue is now in Bug Bash Week milestone
    errors = []
    for title, issue in issues_by_title.items():
        if issue.get("milestoneId") != bug_bash_id:
            errors.append(f"'{title}' not moved to 'Bug Bash Week' milestone.")

    if errors:
        return False, " ".join(errors)

    return True, f"Milestone 'Bug Bash Week' (March 10-14, 2026) created and {len(expected_titles)} open type::bug issues without milestones moved into it."
