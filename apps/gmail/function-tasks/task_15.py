import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    label = next((l for l in state["labels"] if l["name"] == "Deadlines"), None)
    if not label:
        return False, "Label 'Deadlines' not found."

    if label["type"] != "user":
        return False, f"Expected label type 'user', got '{label['type']}'."

    # Find the Work label to check parentId
    work_label = next((l for l in state["labels"] if l["name"] == "Work"), None)
    if not work_label:
        return False, "Work label not found in state."

    if label.get("parentId") != work_label["id"]:
        return False, f"Expected parentId '{work_label['id']}', got '{label.get('parentId')}'."

    return True, "Label 'Deadlines' created as a child of 'Work'."
