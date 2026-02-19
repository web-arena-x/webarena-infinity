import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify Email channel is enabled and project_updates is enabled for email."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    channels = state.get("notificationChannels", {})
    groups = state.get("notificationGroups", [])

    # Check email channel is enabled
    email_channel = channels.get("email", {})
    if email_channel.get("enabled") is not True:
        return False, f"Expected email channel enabled=true, got {email_channel.get('enabled')}."

    # Check project_updates notification group has email=true
    project_group = next((g for g in groups if g.get("id") == "project_updates"), None)
    if not project_group:
        return False, "Notification group 'project_updates' not found."

    email_enabled = project_group.get("channels", {}).get("email")
    if email_enabled is not True:
        return False, f"Expected project_updates email=true, got {email_enabled}."

    return True, "Email channel enabled and project updates notification enabled for email."
