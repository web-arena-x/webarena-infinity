import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})

    days_supply = settings.get("defaultDaysSupply")
    if days_supply != 90:
        return False, f"Default days supply is {days_supply}, expected 90."

    return True, "Default days supply changed to 90."
