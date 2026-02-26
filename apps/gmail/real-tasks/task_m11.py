"""Turn off the Send and Archive feature."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()

    send_and_archive = state.get("settings", {}).get("sendAndArchive")
    if send_and_archive is False:
        return True, "Send and Archive is disabled."
    return False, f"Expected sendAndArchive to be False, got {send_and_archive!r}."
