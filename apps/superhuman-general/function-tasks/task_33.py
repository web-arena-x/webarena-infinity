import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state["settings"]

    team_sharing = settings.get("readReceipts", {}).get("teamSharing")
    if team_sharing is False:
        return True, "Team Read Statuses have been disabled."
    return False, f"Team Read Statuses (teamSharing) is {team_sharing}, expected False."
