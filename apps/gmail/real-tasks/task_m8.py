"""
Task M8: Disable the Social category tab in the inbox.
Check state["settings"]["categoriesEnabled"]["social"] == False.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()
    settings = state.get("settings", {})
    categories_enabled = settings.get("categoriesEnabled", {})
    social_enabled = categories_enabled.get("social")

    if social_enabled is None:
        return False, "settings.categoriesEnabled.social not found in state."

    if social_enabled is False:
        return True, "Social category tab is disabled (categoriesEnabled.social=false)."

    return False, f"Social category tab is still enabled (categoriesEnabled.social={social_enabled})."
