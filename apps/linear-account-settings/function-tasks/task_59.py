import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    first_day = (
        state.get("preferences", {})
        .get("general", {})
        .get("firstDayOfWeek")
    )

    if first_day != "Saturday":
        return False, f"Expected firstDayOfWeek to be 'Saturday', but got '{first_day}'."

    return True, "preferences.general.firstDayOfWeek is 'Saturday'."
