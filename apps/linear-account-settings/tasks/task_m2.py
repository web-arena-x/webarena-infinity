import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the first day of the week was changed to 'sunday'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})
    first_day = prefs.get("firstDayOfWeek")

    if first_day != "sunday":
        return False, f"Expected firstDayOfWeek='sunday', got '{first_day}'."

    return True, "First day of the week successfully changed to 'Sunday'."
