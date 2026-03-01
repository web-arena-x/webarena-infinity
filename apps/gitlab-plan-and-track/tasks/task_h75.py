import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Priya Patel and type::task label
    priya = None
    for u in state.get("users", []):
        if u.get("name") == "Priya Patel":
            priya = u
            break
    if priya is None:
        return False, "Could not find user 'Priya Patel'."

    task_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "type::task":
            task_label = lbl
            break
    if task_label is None:
        return False, "Could not find label 'type::task'."

    errors = []

    # Epics that originally had no issues: Mobile App v2 and Enterprise SSO Integration
    expected_epics = ["Mobile App v2", "Enterprise SSO Integration"]

    for epic_title in expected_epics:
        epic = None
        for e in state.get("epics", []):
            if e.get("title") == epic_title:
                epic = e
                break
        if epic is None:
            errors.append(f"Could not find epic '{epic_title}'.")
            continue

        # Find the new issue
        expected_issue_title = f"Initial planning for {epic_title}"
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == expected_issue_title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{expected_issue_title}'.")
            continue

        if issue.get("epicId") != epic["id"]:
            errors.append(f"Issue '{expected_issue_title}' not in epic '{epic_title}'.")
        if priya["id"] not in issue.get("assignees", []):
            errors.append(f"Issue '{expected_issue_title}' not assigned to Priya Patel.")
        if task_label["id"] not in issue.get("labels", []):
            errors.append(f"Issue '{expected_issue_title}' missing 'type::task' label.")

    if errors:
        return False, " ".join(errors)

    return True, f"Created planning issues for {len(expected_epics)} empty epics, assigned to Priya Patel."
