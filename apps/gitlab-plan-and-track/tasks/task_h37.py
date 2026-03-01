import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find Frontend Modernization epic
    fm_epic = None
    for e in state.get("epics", []):
        if e.get("title") == "Frontend Modernization":
            fm_epic = e
            break
    if fm_epic is None:
        return False, "Could not find epic 'Frontend Modernization'."

    # Find accessibility label
    acc_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "accessibility":
            acc_label = lbl
            break
    if acc_label is None:
        return False, "Could not find label 'accessibility'."

    acc_id = acc_label["id"]

    # Check all open issues in the epic have the accessibility label
    open_issues = [i for i in state.get("issues", [])
                   if i.get("epicId") == fm_epic["id"] and i.get("status") == "open"]
    if len(open_issues) < 4:
        return False, f"Expected at least 4 open issues in Frontend Modernization, found {len(open_issues)}."

    errors = []
    for issue in open_issues:
        if acc_id not in issue.get("labels", []):
            errors.append(f"Issue '{issue.get('title')}' missing accessibility label.")

    if errors:
        return False, " ".join(errors)

    return True, f"Accessibility label added to all {len(open_issues)} open issues in Frontend Modernization epic."
