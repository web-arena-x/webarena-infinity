import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Epic with most open children is API v3 Migration (6 open: 7,8,9,10,47,48)
    # Label 'epic-focus' should exist with color #2980b9
    label = next((l for l in state["labels"] if l["name"] == "epic-focus"), None)
    if label is None:
        return False, "Label 'epic-focus' not found."
    if label.get("color") != "#2980b9":
        return False, f"Label 'epic-focus' color is '{label.get('color')}', expected '#2980b9'."

    label_id = label["id"]

    # Applied to all open children of API v3 Migration: #7, #8, #9, #10, #47, #48
    for issue_id in [7, 8, 9, 10, 47, 48]:
        issue = next((i for i in state["issues"] if i["id"] == issue_id), None)
        if issue is None:
            return False, f"Issue #{issue_id} not found."
        if label_id not in issue.get("labelIds", []):
            return False, f"Issue #{issue_id} missing 'epic-focus' label (id {label_id})."

    # Board list for the label should exist
    board = next((b for b in state["boards"] if b["name"] == "Development Board"), None)
    if board is None:
        return False, "Development Board not found."
    has_list = any(l.get("labelId") == label_id for l in board.get("lists", []))
    if not has_list:
        return False, f"Development Board has no list for 'epic-focus' label (id {label_id})."

    return True, "Label 'epic-focus' created, applied to API v3 children, board list added."
