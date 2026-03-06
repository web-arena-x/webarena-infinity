import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that Helen Matsumoto's Passport sharing level is set to Objective Data Only (level 1)."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    patients = state.get("patients", [])
    patient = None
    for pat in patients:
        if pat.get("firstName") == "Helen" and pat.get("lastName") == "Matsumoto":
            patient = pat
            break

    if patient is None:
        return False, "Patient Helen Matsumoto not found"

    sharing_level = patient.get("passportSharingLevel")
    if sharing_level != 1:
        return False, (
            f"Helen Matsumoto passportSharingLevel is {sharing_level}, expected 1 "
            f"(Objective Data Only)"
        )

    return True, "Helen Matsumoto's Passport sharing level is set to Objective Data Only (level 1)"
