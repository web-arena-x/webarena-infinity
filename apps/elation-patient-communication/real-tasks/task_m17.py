import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that David Park has been opted out of SMS messaging."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    patients = state.get("patients", [])
    patient = None
    for pat in patients:
        if pat.get("firstName") == "David" and pat.get("lastName") == "Park":
            patient = pat
            break

    if patient is None:
        return False, "Patient David Park not found"

    sms_status = patient.get("smsOptInStatus")
    if sms_status != "opted_out":
        return False, f"David Park smsOptInStatus is '{sms_status}', expected 'opted_out'"

    return True, "David Park has been opted out of SMS messaging"
