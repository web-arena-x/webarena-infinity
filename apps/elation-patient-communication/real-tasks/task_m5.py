import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    locations = state.get("practiceSettings", {}).get("practiceLocations", [])
    location = None
    for loc in locations:
        if loc.get("name") == "South Bay Clinic":
            location = loc
            break

    if location is None:
        return False, "South Bay Clinic not found in practice locations."

    address = str(location.get("address", "")).lower()
    if "850 stevens creek" not in address:
        return False, f"South Bay Clinic address is '{location.get('address')}', expected it to contain '850 Stevens Creek'."

    if location.get("posCode") != "11":
        return False, f"South Bay Clinic posCode is '{location.get('posCode')}', expected '11'."

    return True, "South Bay Clinic has been added as a practice location."
