import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    auto_labels = state.get("autoLabels", [])

    for al in auto_labels:
        if al.get("name") == "Shipping Update":
            if al.get("enabled") is True:
                return True, "Auto Label 'Shipping Update' is enabled."
            return False, f"Auto Label 'Shipping Update' is not enabled (enabled={al.get('enabled')})."

    return False, "No Auto Label named 'Shipping Update' found."
