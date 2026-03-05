import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the 'Finance' auto-label has been enabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    auto_labels = state.get("autoLabels", [])
    for label in auto_labels:
        if label.get("name") == "Finance":
            if label.get("isEnabled") is True:
                return True, "Finance auto-label is enabled."
            return False, f"Expected Finance auto-label isEnabled to be True, got {label.get('isEnabled')!r}."

    return False, "Could not find auto-label named 'Finance'."
