import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Label 'needs-triage' must exist
    label = next((l for l in state["labels"] if l["name"] == "needs-triage"), None)
    if label is None:
        return False, "Label 'needs-triage' not found."
    if label.get("color", "").lower() != "#9b59b6":
        return False, f"Label 'needs-triage' color is '{label.get('color')}', expected '#9b59b6'."

    label_id = label["id"]

    # Board should have a list for needs-triage
    board = next((b for b in state["boards"] if b["name"] == "Development Board"), None)
    if board is None:
        return False, "Development Board not found."
    if not any(lst.get("labelId") == label_id for lst in board.get("lists", [])):
        return False, f"Development Board has no list for label 'needs-triage' (id {label_id})."

    # Issues #41 and #35 should have the label
    for issue_id in [41, 35]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if label_id not in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} does not have 'needs-triage' label (id {label_id}). Labels: {issue.get('labelIds')}."

    return True, "Label 'needs-triage' created, board list added, applied to #41 and #35."
