import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find epic "Database Optimization"
    db_epic = None
    for epic in state.get("epics", []):
        if epic.get("title") == "Database Optimization":
            db_epic = epic
            break
    if db_epic is None:
        return False, "Could not find epic 'Database Optimization'."
    db_epic_id = db_epic["id"]

    # Find label "priority::high"
    high_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "priority::high":
            high_label = lbl
            break
    if high_label is None:
        return False, "Could not find label 'priority::high'."
    high_label_id = high_label["id"]

    # Find ALL issues with epicId == db_epic_id
    epic_issues = []
    for issue in state.get("issues", []):
        if issue.get("epicId") == db_epic_id:
            epic_issues.append(issue)

    if len(epic_issues) == 0:
        return False, "No issues found in 'Database Optimization' epic."

    if len(epic_issues) < 5:
        return False, f"Expected at least 5 issues in 'Database Optimization' epic, found {len(epic_issues)}."

    # Check each issue has weight == 8 and priority::high label
    errors = []
    for issue in epic_issues:
        title = issue.get("title", issue.get("id"))
        if issue.get("weight") != 8:
            errors.append(f"Issue '{title}' has weight={issue.get('weight')}, expected 8.")
        if high_label_id not in issue.get("labels", []):
            errors.append(f"Issue '{title}' missing 'priority::high' label.")

    if errors:
        return False, " ".join(errors)

    return True, f"All {len(epic_issues)} issues in 'Database Optimization' epic have weight=8 and 'priority::high' label."
