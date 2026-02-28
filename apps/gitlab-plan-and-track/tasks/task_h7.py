import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find issue "Improve error boundary fallback UI"
    target_issue = None
    for issue in state.get("issues", []):
        if issue.get("title") == "Improve error boundary fallback UI":
            target_issue = issue
            break
    if target_issue is None:
        return False, "Could not find issue 'Improve error boundary fallback UI'."

    # Find label "type::bug"
    bug_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "type::bug":
            bug_label = lbl
            break
    if bug_label is None:
        return False, "Could not find label 'type::bug'."
    bug_label_id = bug_label["id"]

    # Find label "priority::medium"
    medium_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "priority::medium":
            medium_label = lbl
            break
    if medium_label is None:
        return False, "Could not find label 'priority::medium'."
    medium_label_id = medium_label["id"]

    issue_labels = target_issue.get("labels", [])

    # Check both new labels are present
    if bug_label_id not in issue_labels:
        return False, "Label 'type::bug' is not applied to 'Improve error boundary fallback UI'."
    if medium_label_id not in issue_labels:
        return False, "Label 'priority::medium' is not applied to 'Improve error boundary fallback UI'."

    # Check no other labels are present (exactly these two)
    if len(issue_labels) != 2:
        # Get names of unexpected labels
        expected_ids = {bug_label_id, medium_label_id}
        extra_ids = [lid for lid in issue_labels if lid not in expected_ids]
        extra_names = []
        for lbl in state.get("labels", []):
            if lbl["id"] in extra_ids:
                extra_names.append(lbl.get("title"))
        return False, f"Issue has unexpected labels beyond 'type::bug' and 'priority::medium': {extra_names}"

    return True, "Issue 'Improve error boundary fallback UI' now has exactly 'type::bug' and 'priority::medium' labels."
