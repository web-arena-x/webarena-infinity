import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify all sessions except current revoked, and Desktop channel disabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    sessions = state.get("sessions", [])
    channels = state.get("notificationChannels", {})

    # Check sessions
    non_current = [s for s in sessions if not s.get("isCurrent")]
    if non_current:
        return False, f"Expected 0 non-current sessions, found {len(non_current)}."

    current = [s for s in sessions if s.get("isCurrent")]
    if len(current) != 1:
        return False, f"Expected 1 current session, found {len(current)}."

    # Check desktop channel
    desktop = channels.get("desktop", {})
    if desktop.get("enabled") is not False:
        return False, f"Expected desktop channel enabled=false, got {desktop.get('enabled')}."

    return True, "All non-current sessions revoked and Desktop notifications disabled."
