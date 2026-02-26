"""Switch the inbox type to Important first."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()

    inbox_type = state.get("settings", {}).get("inboxType")
    if inbox_type == "important_first":
        return True, "Inbox type is set to 'important_first'."
    return False, f"Expected inboxType to be 'important_first', got {inbox_type!r}."
