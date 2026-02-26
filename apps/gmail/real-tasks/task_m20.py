"""Change button labels to show text instead of icons."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()

    button_labels = state.get("settings", {}).get("buttonLabels")
    if button_labels == "text":
        return True, "Button labels are set to 'text'."
    return False, f"Expected buttonLabels to be 'text', got {button_labels!r}."
