import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state["settings"]
    if settings.get("latePenaltyEnabled") is not True:
        return False, f"Expected latePenaltyEnabled true, got {settings.get('latePenaltyEnabled')}"
    if abs(settings.get("latePenaltyRate", 0) - 2.5) > 0.01:
        return False, f"Expected rate 2.5, got {settings.get('latePenaltyRate')}"
    if settings.get("latePenaltyFrequency") != "daily":
        return False, f"Expected frequency 'daily', got '{settings.get('latePenaltyFrequency')}'"
    return True, "Late payment penalty enabled with rate 2.5% daily."
