import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Epic 1 = User Authentication Overhaul
    epic = next((e for e in state["epics"] if "User Authentication Overhaul" in e.get("title", "")), None)
    if epic is None:
        return False, "Epic 'User Authentication Overhaul' not found."

    # status::in-progress = 16, status::review = 17
    in_progress_label = next((l for l in state["labels"] if l["name"] == "status::in-progress"), None)
    review_label = next((l for l in state["labels"] if l["name"] == "status::review"), None)
    if not in_progress_label or not review_label:
        return False, "Status labels not found."

    ip_id = in_progress_label["id"]
    rv_id = review_label["id"]

    # Issues #1 and #3 should have review, not in-progress
    for issue_id in [1, 3]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if ip_id in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} still has status::in-progress label."
        if rv_id not in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} does not have status::review label."

    return True, "Issues #1 and #3 changed from in-progress to review status."
