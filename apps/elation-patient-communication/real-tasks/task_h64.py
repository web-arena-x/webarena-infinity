import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify differentiated treatment: Chronic Care patients below level 3 upgraded,
    those at 3+ get VIP tag."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # Patients who should be upgraded to level 3
    should_upgrade = {"pat_41": "Gregory Abrams", "pat_47": "Dennis Volkov"}
    # Patients who should have VIP added (already at 3+)
    should_vip = {
        "pat_1": "James Rodriguez",
        "pat_3": "Robert Washington",
        "pat_6": "Linda Garcia",
        "pat_14": "Maria Gonzalez",
        "pat_24": "Nancy Yamamoto",
        "pat_27": "Howard Blackwell",
        "pat_30": "Janet Okonkwo",
    }
    # Patient who already has VIP and level 4 — no change needed
    already_done = {"pat_8": "Patricia O'Brien"}

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

    for pat_id, name in should_vip.items():
        patient = patients_by_id.get(pat_id)
        if not patient:
            errors.append(f"{name} ({pat_id}) not found")
            continue
        if "VIP" not in patient.get("tags", []):
            errors.append(f"{name} ({pat_id}) missing 'VIP' tag. Tags: {patient.get('tags', [])}")

    for pat_id, name in already_done.items():
        patient = patients_by_id.get(pat_id)
        if not patient:
            errors.append(f"{name} ({pat_id}) not found")
            continue
        if "VIP" not in patient.get("tags", []):
            errors.append(f"{name} ({pat_id}) lost 'VIP' tag")

    if errors:
        return False, "; ".join(errors)
    return True, "Chronic Care patients: level upgraded for those below 3, VIP added for those at 3+"
