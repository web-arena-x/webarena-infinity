import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Diabetes-Management removed from all, Diabetes-Active added only to those with active diabetes."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    patients = state.get("patients", [])

    if not patients:
        return False, "No patients found in state"

    errors = []

    # Find Henderson and Bergstrom by name (case-insensitive)
    henderson = None
    bergstrom = None
    for p in patients:
        last = p.get("lastName", "").lower()
        if last == "henderson":
            henderson = p
        elif last == "bergstrom":
            bergstrom = p

    if henderson is None:
        errors.append("Patient Henderson not found")
    if bergstrom is None:
        errors.append("Patient Bergstrom not found")

    if errors:
        return False, "; ".join(errors)

    # Check Henderson
    henderson_tags = [t.lower() for t in henderson.get("tags", [])]
    if "diabetes-management" in henderson_tags:
        errors.append("Henderson still has 'Diabetes-Management' tag (should be removed)")
    if "diabetes-active" not in henderson_tags:
        errors.append("Henderson is missing 'Diabetes-Active' tag (has active diabetes)")

    # Check Bergstrom
    bergstrom_tags = [t.lower() for t in bergstrom.get("tags", [])]
    if "diabetes-management" in bergstrom_tags:
        errors.append("Bergstrom still has 'Diabetes-Management' tag (should be removed)")
    if "diabetes-active" in bergstrom_tags:
        errors.append("Bergstrom has 'Diabetes-Active' tag (diabetes is Controlled, should NOT have it)")

    if errors:
        return False, "; ".join(errors)
    return True, "Diabetes-Management removed from all; Diabetes-Active correctly applied only to Henderson"
