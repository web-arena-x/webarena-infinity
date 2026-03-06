import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that James Rodriguez's Passport sharing level is set to the highest level (4)."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    patients = state.get("patients", [])
    patient = None
    for pat in patients:
        if pat.get("firstName") == "James" and pat.get("lastName") == "Rodriguez":
            patient = pat
            break

    if patient is None:
        return False, "Patient James Rodriguez not found"

    sharing_level = patient.get("passportSharingLevel")
    if sharing_level != 4:
        return False, (
            f"James Rodriguez passportSharingLevel is {sharing_level}, expected 4 "
            f"(Clinical Profile, Expanded Summary - highest level)"
        )

    return True, "James Rodriguez's Passport sharing level is set to 4 (highest level)"
