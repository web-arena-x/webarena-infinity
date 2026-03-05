import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that team reply indicators have been disabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    try:
        team_reply_indicators = state["settings"]["readStatuses"]["teamReplyIndicators"]
    except (KeyError, TypeError) as e:
        return False, f"Could not find settings.readStatuses.teamReplyIndicators: {e}"

    if team_reply_indicators is False:
        return True, "Team reply indicators are disabled."
    return False, f"Expected settings.readStatuses.teamReplyIndicators to be False, got {team_reply_indicators!r}."
