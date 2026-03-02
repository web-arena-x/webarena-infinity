import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    practice_settings = state.get("practiceSettings", {})
    locations = practice_settings.get("practiceLocations", [])

    for location in locations:
        if location.get("name") == "East Bay Clinic":
            return False, "East Bay Clinic still exists in practiceSettings.practiceLocations."

    return True, "East Bay Clinic has been removed from practice locations."
