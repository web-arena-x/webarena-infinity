import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that a Passport invitation has been sent to Anthony Petrov."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    patients = state.get("patients", [])
    patient = None
    for pat in patients:
        if pat.get("firstName") == "Anthony" and pat.get("lastName") == "Petrov":
            patient = pat
            break

    if patient is None:
        return False, "Patient Anthony Petrov not found"

    passport_status = patient.get("passportStatus")
    if passport_status != "invited":
        return False, f"Anthony Petrov passportStatus is '{passport_status}', expected 'invited'"

    invited_at = patient.get("invitedAt")
    if invited_at is None:
        return False, "Anthony Petrov invitedAt is None, expected a timestamp"

    return True, "Passport invitation has been sent to Anthony Petrov"
