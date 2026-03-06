import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that an emergency contact has been added for Kevin Adebayo."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    patients = state.get("patients", [])
    patient = None
    for pat in patients:
        if pat.get("firstName") == "Kevin" and pat.get("lastName") == "Adebayo":
            patient = pat
            break

    if patient is None:
        return False, "Patient Kevin Adebayo not found"

    ec = patient.get("emergencyContact")
    if ec is None:
        return False, "Kevin Adebayo has no emergency contact set"

    ec_name = ec.get("name", "")
    if ec_name != "Grace Adebayo":
        return False, f"Emergency contact name is '{ec_name}', expected 'Grace Adebayo'"

    ec_phone = ec.get("phone", "")
    if ec_phone != "(650) 555-1122":
        return False, f"Emergency contact phone is '{ec_phone}', expected '(650) 555-1122'"

    ec_relationship = (ec.get("relationship") or "").lower()
    if ec_relationship != "wife":
        return False, (
            f"Emergency contact relationship is '{ec.get('relationship')}', expected 'Wife'"
        )

    return True, "Emergency contact Grace Adebayo added for Kevin Adebayo"
