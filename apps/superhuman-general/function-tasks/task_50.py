import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    auto_labels = state.get("autoLabels", [])

    for al in auto_labels:
        if al.get("name") == "Support Ticket":
            return False, "Auto Label 'Support Ticket' still exists; it should have been deleted."

    return True, "Custom Auto Label 'Support Ticket' has been deleted."
