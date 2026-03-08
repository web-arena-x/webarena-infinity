# Task: Disable activity tracking.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    privacy = state.get("accountSettings", {}).get("privacySettings", {})
    tracking = privacy.get("activityTracking")

    if tracking is False:
        return True, "Activity tracking is now disabled."
    else:
        return False, f"activityTracking is {tracking}, expected false."
