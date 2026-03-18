import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Set the late penalty rate to 2.5% in settings."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})
    rate = settings.get("latePenaltyRate")

    if rate == 2.5:
        return True, "Late penalty rate is set to 2.5"
    else:
        return False, f"settings.latePenaltyRate is {rate!r}, expected 2.5"
