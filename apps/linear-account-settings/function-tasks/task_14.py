import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    val = state["preferences"]["general"]["firstDayOfWeek"]
    if val != "Sunday":
        return False, f"Expected first day of week 'Sunday', got '{val}'."

    return True, "First day of week set to 'Sunday'."
