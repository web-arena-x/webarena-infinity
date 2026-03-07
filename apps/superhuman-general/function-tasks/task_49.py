import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    auto_labels = state.get("autoLabels", [])

    for al in auto_labels:
        if al.get("name") == "Team Update":
            if al.get("enabled") is False:
                return True, "Auto Label 'Team Update' is disabled."
            return False, f"Auto Label 'Team Update' is still enabled (enabled={al.get('enabled')})."

    return False, "No Auto Label named 'Team Update' found."
