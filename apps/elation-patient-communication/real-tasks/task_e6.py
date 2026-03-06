import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the 'New Patient' tag has been removed from Emily Thompson."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    patients = state.get("patients", [])
    patient = None
    for pat in patients:
        if pat.get("firstName") == "Emily" and pat.get("lastName") == "Thompson":
            patient = pat
            break

    if patient is None:
        return False, "Patient Emily Thompson not found"

    tags = patient.get("tags", [])
    if "New Patient" in tags:
        return False, f"'New Patient' tag still present in Emily Thompson's tags: {tags}"

    return True, "'New Patient' tag has been removed from Emily Thompson's profile"
