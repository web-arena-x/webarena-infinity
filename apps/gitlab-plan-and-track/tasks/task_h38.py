import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find priority::medium label
    med_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "priority::medium":
            med_label = lbl
            break
    if med_label is None:
        return False, "Could not find label 'priority::medium'."

    med_id = med_label["id"]

    # Expected issues: open, no assignees, no milestone, no epic
    expected_titles = [
        "Fix typo in 404 error page message",
        "Add tooltip to truncated sidebar labels",
    ]

    errors = []
    for title in expected_titles:
        issue = None
        for i in state.get("issues", []):
            if i.get("title") == title:
                issue = i
                break
        if issue is None:
            errors.append(f"Could not find issue '{title}'.")
            continue
        if issue.get("weight") != 5:
            errors.append(f"Issue '{title}' weight is {issue.get('weight')}, expected 5.")
        if med_id not in issue.get("labels", []):
            errors.append(f"Issue '{title}' missing priority::medium label.")

    if errors:
        return False, " ".join(errors)

    return True, "Weight set to 5 and priority::medium applied to both unassigned/unscheduled issues."
