import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that team read statuses have been disabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    try:
        team_read_statuses = state["settings"]["readStatuses"]["teamReadStatuses"]
    except (KeyError, TypeError) as e:
        return False, f"Could not find settings.readStatuses.teamReadStatuses: {e}"

    if team_read_statuses is False:
        return True, "Team read statuses are disabled."
    return False, f"Expected settings.readStatuses.teamReadStatuses to be False, got {team_read_statuses!r}."
