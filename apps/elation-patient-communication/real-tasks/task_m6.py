import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that Brian Murphy's email has been updated to brian.murphy@gmail.com."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    patients = state.get("patients", [])
    patient = None
    for pat in patients:
        if pat.get("firstName") == "Brian" and pat.get("lastName") == "Murphy":
            patient = pat
            break

    if patient is None:
        return False, "Patient Brian Murphy not found"

    email = patient.get("email")
    if email != "brian.murphy@gmail.com":
        return False, f"Brian Murphy's email is '{email}', expected 'brian.murphy@gmail.com'"

    return True, "Brian Murphy's email has been updated to brian.murphy@gmail.com"
