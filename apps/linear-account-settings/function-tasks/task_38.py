import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Email notification channel is disabled and all its settings are disabled."""
    try:
        resp = requests.get(f"{server_url}/api/state", timeout=5)
        resp.raise_for_status()
        state = resp.json()
    except Exception as e:
        return False, f"Failed to fetch state: {e}"

    channel = next((c for c in state["notificationChannels"] if c["id"] == "notif_email"), None)
    if not channel:
        return False, "Email notification channel not found."

    if channel["enabled"] is not False:
        return False, f"Email channel enabled is {channel['enabled']}, expected False."

    for setting in channel["settings"]:
        if setting["enabled"] is not False:
            return False, f"Email setting '{setting['id']}' enabled is {setting['enabled']}, expected False."

    if len(channel["settings"]) != 7:
        return False, f"Expected 7 Email settings, found {len(channel['settings'])}."

    return True, "Email channel is disabled and all 7 settings are disabled."
