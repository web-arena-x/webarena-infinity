import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find milestones
    ms_v40 = None
    for ms in state.get("milestones", []):
        if "v4.0" in ms.get("title", "") and "Platform Redesign" in ms.get("title", ""):
            ms_v40 = ms
            break
    if ms_v40 is None:
        return False, "Could not find milestone 'v4.0 - Platform Redesign'."
    ms_id = ms_v40["id"]

    # Find labels
    lbl_in_progress = None
    lbl_done = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "workflow::in-progress":
            lbl_in_progress = lbl
        elif lbl.get("title") == "workflow::done":
            lbl_done = lbl
    if lbl_in_progress is None:
        return False, "Could not find label 'workflow::in-progress'."
    if lbl_done is None:
        return False, "Could not find label 'workflow::done'."

    ip_id = lbl_in_progress["id"]
    done_id = lbl_done["id"]

    # Expected issues: these were open in v4.0 with workflow::in-progress label
    expected_titles = [
        "Migrate user settings page to React",
        "Login page shows blank screen on Safari 17.2",
        "Add dark mode support for the entire application",
    ]

    for title in expected_titles:
        issue = next((i for i in state.get("issues", []) if i.get("title") == title), None)
        if issue is None:
            return False, f"Could not find issue '{title}'."

        if issue.get("status") != "closed":
            return False, f"Issue '{title}' status is '{issue.get('status')}', expected 'closed'."

        if issue.get("closedAt") is None:
            return False, f"Issue '{title}' has no closedAt date."

        if ip_id in issue.get("labels", []):
            return False, f"Issue '{title}' still has the 'workflow::in-progress' label."

        if done_id not in issue.get("labels", []):
            return False, f"Issue '{title}' is missing the 'workflow::done' label."

    return True, f"All v4.0 in-progress issues closed and relabeled as workflow::done."
