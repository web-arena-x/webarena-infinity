import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    label = next((l for l in state["labels"] if l["name"] == "Urgent"), None)
    if not label:
        return False, "Label 'Urgent' not found."

    if label["type"] != "user":
        return False, f"Expected label type 'user', got '{label['type']}'."

    return True, "Label 'Urgent' created successfully."
