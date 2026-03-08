import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify High Risk tag added to all Penicillin-allergic patients who lacked it."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # All patients with Penicillin allergy must have High Risk tag
    penicillin_patients = {
        "pat_1": "James Rodriguez",
        "pat_17": "Thomas Nakamura",
        "pat_27": "Howard Blackwell",
        "pat_36": "Martha Reeves-Whitfield",
        "pat_49": "Russell Keane",
    }

    errors = []
    for pat_id, name in penicillin_patients.items():
        patient = None
        for p in state.get("patients", []):
            if p.get("id") == pat_id:
                patient = p
                break
        if not patient:
            errors.append(f"Patient {pat_id} ({name}) not found")
            continue
        if "High Risk" not in patient.get("tags", []):
            errors.append(f"{name} ({pat_id}) missing 'High Risk' tag. Tags: {patient.get('tags', [])}")

    if errors:
        return False, "; ".join(errors)
    return True, "All Penicillin-allergic patients have 'High Risk' tag"
