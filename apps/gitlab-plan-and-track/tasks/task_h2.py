import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find label "type::bug" by title
    bug_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "type::bug":
            bug_label = lbl
            break
    if bug_label is None:
        return False, "Could not find label 'type::bug' in state."
    bug_label_id = bug_label["id"]

    # Find label "priority::low" by title
    low_label = None
    for lbl in state.get("labels", []):
        if lbl.get("title") == "priority::low":
            low_label = lbl
            break
    if low_label is None:
        return False, "Could not find label 'priority::low' in state."
    low_label_id = low_label["id"]

    # Find ALL issues that have BOTH labels
    matching_issues = []
    for issue in state.get("issues", []):
        issue_labels = issue.get("labels", [])
        if bug_label_id in issue_labels and low_label_id in issue_labels:
            matching_issues.append(issue)

    if len(matching_issues) < 1:
        return False, "No issues found with both 'type::bug' and 'priority::low' labels."

    # Check ALL such issues are closed
    not_closed = []
    for issue in matching_issues:
        if issue.get("status") != "closed":
            not_closed.append(issue.get("title", issue.get("id")))

    if not_closed:
        return False, f"The following open bugs with priority::low are not closed: {not_closed}"

    return True, f"All {len(matching_issues)} open bug(s) with priority::low have been closed."
