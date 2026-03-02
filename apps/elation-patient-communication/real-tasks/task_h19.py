import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    practice_settings = state.get("practiceSettings", {})
    locations = practice_settings.get("practiceLocations", [])

    # Check "Telehealth" location is removed
    telehealth_locations = [
        loc for loc in locations
        if loc.get("name") == "Telehealth"
    ]

    if telehealth_locations:
        return False, "Telehealth location still exists in practice locations."

    # Check "West SF Urgent Care" exists with correct address and posCode
    west_sf = next(
        (
            loc for loc in locations
            if loc.get("name") == "West SF Urgent Care"
        ),
        None,
    )

    if west_sf is None:
        return False, "West SF Urgent Care location not found in practice locations."

    address = west_sf.get("address", "") or ""
    if "2100 Geary" not in address:
        return False, (
            f"West SF Urgent Care address is '{address}', "
            f"expected it to contain '2100 Geary'."
        )

    pos_code = str(west_sf.get("posCode", ""))
    if pos_code != "20":
        return False, (
            f"West SF Urgent Care posCode is '{pos_code}', expected '20'."
        )

    return True, "Telehealth location removed and West SF Urgent Care added."
