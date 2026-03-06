import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the Main Office practice location has been renamed to 'SF Main Office'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    practice_settings = state.get("practiceSettings")
    if practice_settings is None:
        return False, "practiceSettings not found in state"

    locations = practice_settings.get("practiceLocations", [])
    location_names = [loc.get("name") for loc in locations]

    found_new = "SF Main Office" in location_names
    found_old = "Main Office" in location_names

    if not found_new:
        return False, (
            f"No practice location named 'SF Main Office' found. "
            f"Existing locations: {location_names}"
        )

    if found_old:
        return False, (
            f"Old location name 'Main Office' still exists. "
            f"Existing locations: {location_names}"
        )

    return True, "Practice location 'Main Office' has been renamed to 'SF Main Office'"
