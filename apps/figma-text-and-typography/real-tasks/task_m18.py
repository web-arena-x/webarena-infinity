"""
Task: Set the default alignment to center and the default text direction to RTL.
Verify: preferences.defaultHorizontalAlign == 'center' AND preferences.defaultTextDirection == 'rtl'.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    preferences = state.get("preferences", {})

    errors = []

    default_align = preferences.get("defaultHorizontalAlign")
    if default_align != "center":
        errors.append(f"Expected preferences.defaultHorizontalAlign == 'center', got '{default_align}'.")

    default_direction = preferences.get("defaultTextDirection")
    if default_direction != "rtl":
        errors.append(f"Expected preferences.defaultTextDirection == 'rtl', got '{default_direction}'.")

    if errors:
        return False, " ".join(errors)

    return True, "Default alignment is 'center' and default text direction is 'rtl'."
