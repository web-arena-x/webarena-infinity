import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Change the late penalty frequency to weekly in the settings."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})
    frequency = settings.get("latePenaltyFrequency")

    if frequency == "weekly":
        return True, "Late penalty frequency is set to 'weekly'"
    else:
        return False, f"settings.latePenaltyFrequency is '{frequency}', expected 'weekly'"
