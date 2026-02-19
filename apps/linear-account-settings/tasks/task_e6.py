import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the Mobile notification channel is disabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    channels = state.get("notificationChannels", {})
    mobile = channels.get("mobile", {})
    enabled = mobile.get("enabled")

    if enabled is not False:
        return False, f"Expected mobile channel enabled=false, got {enabled}."

    return True, "Mobile notification channel is disabled."
