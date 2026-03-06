import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the draft letter to Martha Reeves-Whitfield (ltr_35) has been deleted."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    letters = state.get("patientLetters", [])
    for ltr in letters:
        if ltr.get("id") == "ltr_35":
            return False, "Letter ltr_35 (draft to Martha Reeves-Whitfield) still exists in patientLetters"

    return True, "Draft letter to Martha Reeves-Whitfield (ltr_35) has been deleted"
