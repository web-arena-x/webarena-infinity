import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the 'VIP' tag has been added to David Park's profile."""
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

    tags = patient.get("tags", [])
    if "VIP" not in tags:
        return False, f"'VIP' tag not found in David Park's tags: {tags}"

    return True, "David Park's profile has the 'VIP' tag"
