import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    v2_milestone = next((m for m in state["milestones"] if "v2.0" in m.get("title", "")), None)
    if v2_milestone is None:
        return False, "Milestone 'v2.0 — API Overhaul' not found."
    v2_id = v2_milestone["id"]

    high_label = next((l for l in state["labels"] if l["name"] == "priority::high"), None)
    if high_label is None:
        return False, "Label 'priority::high' not found."
    high_id = high_label["id"]

    for issue_id in [60, 61, 62]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if issue.get("milestoneId") != v2_id:
            return False, f"Issue #{issue_id} milestoneId is {issue.get('milestoneId')}, expected {v2_id}."
        if high_id not in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} does not have priority::high label."

    return True, "Issues #60, #61, #62 moved to v2.0 milestone with priority::high."
