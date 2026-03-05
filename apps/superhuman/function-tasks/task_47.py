import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that follow-up auto-drafts have been disabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    try:
        follow_ups = state["settings"]["autoDrafts"]["followUps"]
    except (KeyError, TypeError) as e:
        return False, f"Could not find settings.autoDrafts.followUps: {e}"

    if follow_ups is False:
        return True, "Follow-up auto-drafts are disabled."
    return False, f"Expected settings.autoDrafts.followUps to be False, got {follow_ups!r}."
