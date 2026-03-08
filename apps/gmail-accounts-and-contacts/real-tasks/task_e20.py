# Task: Rename Emergency to Urgent.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    labels = state.get("contactLabels", [])
    for label in labels:
        if label.get("id") == "clabel_10":
            if label.get("name") == "Urgent":
                return True, "Emergency label has been renamed to Urgent."
            else:
                return False, f"Label clabel_10 name is '{label.get('name')}', expected 'Urgent'."

    return False, "Label with id 'clabel_10' not found in state."
