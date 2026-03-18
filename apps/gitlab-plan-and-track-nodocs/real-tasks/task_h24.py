import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Issue #1 blocks issue #2 (the blocker of #2)
    issue1 = next((i for i in state["issues"] if i["id"] == 1), None)
    if issue1 is None:
        return False, "Issue #1 not found."

    # Check documentation label (id 3)
    doc_label = next((l for l in state["labels"] if l["name"] == "documentation"), None)
    if doc_label is None:
        return False, "Label 'documentation' not found."

    if doc_label["id"] not in issue1.get("labelIds", []):
        return False, f"Issue #1 does not have the documentation label. Labels: {issue1.get('labelIds')}."

    if issue1.get("dueDate") != "2026-04-30":
        return False, f"Issue #1 dueDate is '{issue1.get('dueDate')}', expected '2026-04-30'."

    return True, "Issue #1 (blocker of #2) has documentation label and due date 2026-04-30."
