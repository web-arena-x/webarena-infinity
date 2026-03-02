import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    practice_areas = state.get("practiceAreas", [])

    business_law = next(
        (pa for pa in practice_areas if pa.get("name") == "Business Law"),
        None
    )
    if business_law is None:
        return False, "No practice area named 'Business Law' found."

    corporate_business = next(
        (pa for pa in practice_areas if pa.get("name") == "Corporate/Business"),
        None
    )
    if corporate_business is not None:
        return False, "Practice area 'Corporate/Business' still exists; it should have been renamed."

    return True, "Practice area has been renamed from 'Corporate/Business' to 'Business Law'."
