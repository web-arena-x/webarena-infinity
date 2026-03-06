import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that East Bay Clinic has been removed from practice locations."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    practice_settings = state.get("practiceSettings", {})
    locations = practice_settings.get("practiceLocations", [])

    for loc in locations:
        if loc.get("name") == "East Bay Clinic":
            return False, "East Bay Clinic still exists in practiceSettings.practiceLocations"

    return True, "East Bay Clinic has been removed from practice locations"
