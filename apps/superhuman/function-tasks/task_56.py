import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the 'Newsletters' auto-label has been disabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    auto_labels = state.get("autoLabels", [])
    for label in auto_labels:
        if label.get("name") == "Newsletters":
            if label.get("isEnabled") is False:
                return True, "Newsletters auto-label is disabled."
            return False, f"Expected Newsletters auto-label isEnabled to be False, got {label.get('isEnabled')!r}."

    return False, "Could not find auto-label named 'Newsletters'."
