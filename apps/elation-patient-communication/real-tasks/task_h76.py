import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify sharing level upgraded for appointment reminder patients below level 3."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # Patients with appointment reminders who need upgrade (were below 3)
    should_upgrade = {
        "pat_20": "Aisha Patel",
        "pat_4": "Sophia Nguyen",
    }
    # Patients with appointment reminders already at 3 (should stay)
    should_stay = {
        "pat_1": "James Rodriguez",
        "pat_36": "Martha Reeves-Whitfield",
    }

    errors = []
    patients_by_id = {p["id"]: p for p in state.get("patients", [])}

    for pat_id, name in should_upgrade.items():
        patient = patients_by_id.get(pat_id)
        if not patient:
            errors.append(f"{name} ({pat_id}) not found")
            continue
        level = patient.get("passportSharingLevel")
        if level < 3:
            errors.append(f"{name} ({pat_id}) sharing level is {level}, expected >= 3")

    for pat_id, name in should_stay.items():
        patient = patients_by_id.get(pat_id)
        if not patient:
            errors.append(f"{name} ({pat_id}) not found")
            continue
        level = patient.get("passportSharingLevel")
        if level < 3:
            errors.append(f"{name} ({pat_id}) sharing level dropped to {level}, expected >= 3")

    if errors:
        return False, "; ".join(errors)
    return True, "Sharing levels upgraded for appointment reminder patients below level 3"
