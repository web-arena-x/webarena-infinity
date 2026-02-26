"""Disable the Forums category."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()

    forums_enabled = state.get("settings", {}).get("categoriesEnabled", {}).get("forums")
    if forums_enabled is False:
        return True, "Forums category is disabled."
    return False, f"Expected categoriesEnabled.forums to be False, got {forums_enabled!r}."
