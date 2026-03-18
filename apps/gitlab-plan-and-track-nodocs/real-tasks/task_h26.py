import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    bug_label = next((l for l in state["labels"] if l["name"] == "bug"), None)
    if bug_label is None:
        return False, "Label 'bug' not found."
    bug_id = bug_label["id"]

    milestone = next((m for m in state["milestones"] if "v2.0" in m.get("title", "")), None)
    if milestone is None:
        return False, "Milestone 'v2.0 — API Overhaul' not found."
    ms_id = milestone["id"]

    expected_closed = [28, 31, 78, 101, 104]
    for issue_id in expected_closed:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("status") != "closed":
            return False, f"Issue #{issue_id} status is '{issue.get('status')}', expected 'closed'."

    return True, f"All 5 low-weight bugs in v2.0 milestone are closed."
