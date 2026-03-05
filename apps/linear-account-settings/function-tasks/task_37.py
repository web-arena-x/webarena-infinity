import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Slack 'Issue assigned to you' setting is enabled and Slack channel is enabled."""
    try:
        resp = requests.get(f"{server_url}/api/state", timeout=5)
        resp.raise_for_status()
        state = resp.json()
    except Exception as e:
        return False, f"Failed to fetch state: {e}"

    channel = next((c for c in state["notificationChannels"] if c["id"] == "notif_slack"), None)
    if not channel:
        return False, "Slack notification channel not found."

    if channel["enabled"] is not True:
        return False, f"Slack channel enabled is {channel['enabled']}, expected True (auto-enabled when a setting is enabled)."

    setting = next((s for s in channel["settings"] if s["id"] == "slack_issue_assigned"), None)
    if not setting:
        return False, "Slack 'Issue assigned to you' setting not found."

    if setting["enabled"] is not True:
        return False, f"slack_issue_assigned enabled is {setting['enabled']}, expected True."

    return True, "Slack 'Issue assigned to you' setting is enabled and Slack channel is enabled."
