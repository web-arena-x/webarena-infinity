import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Label 'stale' should exist with color #95a5a6
    label = next((l for l in state["labels"] if l["name"] == "stale"), None)
    if label is None:
        return False, "Label 'stale' not found."
    if label.get("color") != "#95a5a6":
        return False, f"Label 'stale' color is '{label.get('color')}', expected '#95a5a6'."

    label_id = label["id"]

    # Applied to Backlog (milestoneId 6) open issues with no assignee and no dueDate:
    # #34, #68, #70, #103, #105, #112, #116, #122
    target_ids = [34, 68, 70, 103, 105, 112, 116, 122]

    for issue_id in target_ids:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if label_id not in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} missing 'stale' label (id {label_id})."

    return True, "Label 'stale' created and applied to 8 unassigned Backlog issues without due dates."
