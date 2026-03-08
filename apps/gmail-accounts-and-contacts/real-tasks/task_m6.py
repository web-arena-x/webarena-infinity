# Task: Turn off all four notification types.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    notif = state.get("accountSettings", {}).get("notificationSettings", {})
    for key in ["delegateActivity", "contactChanges", "securityAlerts", "linkedServiceUpdates"]:
        val = notif.get(key)
        if val is not False:
            errors.append(f"Expected notificationSettings.{key} to be false, got {val}")

    if errors:
        return False, "; ".join(errors)
    return True, "All four notification types turned off."
