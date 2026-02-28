import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Check that no label with title "blocked" exists
    for lbl in state.get("labels", []):
        if lbl.get("title") == "blocked":
            return False, "Label 'blocked' still exists and should have been deleted."

    # Find label "status::blocked"
    status_blocked_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "status::blocked":
            status_blocked_label = lbl
            break
    if status_blocked_label is None:
        return False, "Could not find label 'status::blocked'."

    # Check color
    if status_blocked_label.get("color") != "#b91c1c":
        return False, f"Label 'status::blocked' has color='{status_blocked_label.get('color')}', expected '#b91c1c'."

    # Check scoped (title contains "::" so it should be scoped)
    if status_blocked_label.get("scoped") is not True:
        return False, "Label 'status::blocked' does not have scoped=True."

    status_blocked_id = status_blocked_label["id"]

    # Find issue "Migrate user settings page to React"
    target_issue = None
    for issue in state.get("issues", []):
        if issue.get("title") == "Migrate user settings page to React":
            target_issue = issue
            break
    if target_issue is None:
        return False, "Could not find issue 'Migrate user settings page to React'."

    # Check the new label is applied to the issue
    if status_blocked_id not in target_issue.get("labels", []):
        return False, "Label 'status::blocked' is not applied to 'Migrate user settings page to React'."

    return True, "Label 'blocked' deleted, 'status::blocked' (#b91c1c, scoped) created, and applied to 'Migrate user settings page to React'."
