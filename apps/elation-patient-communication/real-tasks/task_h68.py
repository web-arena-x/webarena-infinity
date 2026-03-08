import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify New Patient tag removed from registered patients, kept for non-registered."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    errors = []

    # Registered patients who should have New Patient REMOVED
    should_remove = {"pat_2": "Emily Thompson"}
    # Non-registered patients who should KEEP New Patient
    should_keep = {
        "pat_5": "Marcus Johnson",
        "pat_9": "Anthony Petrov",
        "pat_31": "Craig Bennet",
        "pat_42": "Megan Burke",
    }

    patients_by_id = {p["id"]: p for p in state.get("patients", [])}

    for pat_id, name in should_remove.items():
        patient = patients_by_id.get(pat_id)
        if not patient:
            errors.append(f"{name} ({pat_id}) not found")
            continue
        if "New Patient" in patient.get("tags", []):
            errors.append(
                f"{name} ({pat_id}) still has 'New Patient' tag but is registered for Passport"
            )

    for pat_id, name in should_keep.items():
        patient = patients_by_id.get(pat_id)
        if not patient:
            errors.append(f"{name} ({pat_id}) not found")
            continue
        if "New Patient" not in patient.get("tags", []):
            errors.append(
                f"{name} ({pat_id}) lost 'New Patient' tag but hasn't registered for Passport"
            )

    if errors:
        return False, "; ".join(errors)
    return True, "New Patient tag removed from registered patients, kept for non-registered"
