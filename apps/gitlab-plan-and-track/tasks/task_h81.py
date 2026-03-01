import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Find the 'status::blocked' label
    sb_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "status::blocked":
            sb_label = lbl
            break
    if sb_label is None:
        return False, "Could not find label 'status::blocked'."

    if sb_label.get("color", "").lower() != "#b60205":
        errors.append(
            f"Label 'status::blocked' color is '{sb_label.get('color')}', expected '#b60205'."
        )
    if not sb_label.get("scoped"):
        errors.append("Label 'status::blocked' should be scoped.")

    # Find the new issue
    issue = None
    for i in state.get("issues", []):
        if i.get("title") == "Resolve CDN provider outage":
            issue = i
            break
    if issue is None:
        return False, "Could not find issue 'Resolve CDN provider outage'. " + " ".join(errors)

    # Check label on issue
    if sb_label["id"] not in issue.get("labels", []):
        errors.append("Issue missing 'status::blocked' label.")

    # Check assignee — Luca Rossi
    luca = None
    for u in state.get("users", []):
        if u.get("name") == "Luca Rossi":
            luca = u
            break
    if luca is None:
        errors.append("Could not find user 'Luca Rossi'.")
    elif luca["id"] not in issue.get("assignees", []):
        errors.append("Issue not assigned to Luca Rossi.")

    # Check milestone — v4.1 - Performance
    ms = None
    for m in state.get("milestones", []):
        if m.get("title") == "v4.1 - Performance":
            ms = m
            break
    if ms is None:
        errors.append("Could not find milestone 'v4.1 - Performance'.")
    elif issue.get("milestoneId") != ms["id"]:
        errors.append(
            f"Issue milestoneId is '{issue.get('milestoneId')}', expected '{ms['id']}'."
        )

    # Check weight
    if issue.get("weight") != 5:
        errors.append(f"Issue weight is {issue.get('weight')}, expected 5.")

    if errors:
        return False, " ".join(errors)

    return True, (
        "Label 'status::blocked' created with correct color; "
        "issue 'Resolve CDN provider outage' created with label, assignee, milestone, and weight."
    )
