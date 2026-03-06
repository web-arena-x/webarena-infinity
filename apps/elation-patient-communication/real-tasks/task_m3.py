import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that a new practice location 'South Bay Clinic' has been added."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    practice_settings = state.get("practiceSettings")
    if practice_settings is None:
        return False, "practiceSettings not found in state"

    locations = practice_settings.get("practiceLocations", [])
    location = None
    for loc in locations:
        if loc.get("name") == "South Bay Clinic":
            location = loc
            break

    if location is None:
        return False, (
            f"No practice location named 'South Bay Clinic' found. "
            f"Existing locations: {[loc.get('name') for loc in locations]}"
        )

    address = location.get("address", "")
    if "789 Stevens Creek" not in address:
        return False, f"South Bay Clinic address is '{address}', expected it to contain '789 Stevens Creek'"

    pos_code = str(location.get("posCode", ""))
    if pos_code != "11":
        return False, f"South Bay Clinic posCode is '{pos_code}', expected '11'"

    return True, "Practice location 'South Bay Clinic' at 789 Stevens Creek with POS code 11 has been added"
