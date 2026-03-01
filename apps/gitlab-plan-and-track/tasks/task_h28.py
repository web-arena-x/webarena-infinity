import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the UX label
    ux_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "UX":
            ux_label = lbl
            break
    if ux_label is None:
        return False, "Could not find label 'UX'."
    ux_id = ux_label["id"]

    # Check no issues have the UX label
    issues_with_ux = []
    for issue in state.get("issues", []):
        if ux_id in issue.get("labels", []):
            issues_with_ux.append(issue.get("title"))

    if issues_with_ux:
        return False, f"These issues still have the 'UX' label: {issues_with_ux}"

    # Check no epics have the UX label
    epics_with_ux = []
    for epic in state.get("epics", []):
        if ux_id in epic.get("labels", []):
            epics_with_ux.append(epic.get("title"))

    if epics_with_ux:
        return False, f"These epics still have the 'UX' label: {epics_with_ux}"

    return True, "The 'UX' label has been removed from all issues and epics."
