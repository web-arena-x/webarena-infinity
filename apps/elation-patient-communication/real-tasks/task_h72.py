import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify pat_17 (TIA patient) has sharing level 4 and both new tags."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    pat_17 = None
    for p in state.get("patients", []):
        if p.get("id") == "pat_17":
            pat_17 = p
            break

    if not pat_17:
        return False, "Patient pat_17 (Thomas Nakamura) not found"

    errors = []

    # Check sharing level
    level = pat_17.get("passportSharingLevel")
    if level != 4:
        errors.append(f"Sharing level is {level}, expected 4")

    # Check tags
    tags = pat_17.get("tags", [])
    if "Telehealth Preferred" not in tags:
        errors.append(f"Missing 'Telehealth Preferred' tag. Tags: {tags}")
    if "Chronic Care" not in tags:
        errors.append(f"Missing 'Chronic Care' tag. Tags: {tags}")
    if "High Risk" not in tags:
        errors.append(f"Lost 'High Risk' tag. Tags: {tags}")

    if errors:
        return False, "; ".join(errors)
    return True, "pat_17 updated: sharing level 4, Telehealth Preferred and Chronic Care tags added"
