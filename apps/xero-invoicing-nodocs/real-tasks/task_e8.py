import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Enable late payment penalties in settings."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})
    late_penalty_enabled = settings.get("latePenaltyEnabled")

    if late_penalty_enabled is True:
        return True, "Late payment penalties have been enabled"
    else:
        return False, f"latePenaltyEnabled is {late_penalty_enabled}, expected True"
