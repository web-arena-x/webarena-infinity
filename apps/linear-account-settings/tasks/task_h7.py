import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify issue_status notification disabled for slack, enabled on others."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    groups = state.get("notificationGroups", [])

    status_group = next((g for g in groups if g.get("id") == "issue_status"), None)
    if not status_group:
        return False, "Notification group 'issue_status' not found."

    channels = status_group.get("channels", {})
    slack_enabled = channels.get("slack")

    if slack_enabled is not False:
        return False, f"Expected issue_status slack=false, got {slack_enabled}."

    # Verify other channels remain as they were (desktop=true, email=true)
    desktop = channels.get("desktop")
    email = channels.get("email")
    if desktop is not True:
        return False, f"Expected issue_status desktop=true, got {desktop}."
    if email is not True:
        return False, f"Expected issue_status email=true, got {email}."

    return True, "Issue status changes notification disabled for Slack, other channels unchanged."
