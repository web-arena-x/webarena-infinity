import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Two patients with E11.65: Active one gets 'DM-Review-Urgent', Controlled one gets 'DM-Review-Routine'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find all patients with E11.65 problems
    dm_patients = {}  # pid -> status
    for prob in state.get("problems", []):
        if prob.get("icd10") == "E11.65":
            pid = prob.get("patientId")
            status = prob.get("status", "").lower()
            dm_patients[pid] = status

    if len(dm_patients) < 2:
        return False, f"Expected 2 patients with E11.65, found {len(dm_patients)}."

    errors = []
    for patient in state.get("patients", []):
        pid = patient.get("id", "")
        if pid not in dm_patients:
            continue
        last_name = patient.get("lastName", "?")
        tags = patient.get("tags", [])
        status = dm_patients[pid]

        if status == "active":
            if "DM-Review-Urgent" not in tags:
                errors.append(f"{last_name} has Active diabetes but missing 'DM-Review-Urgent' tag.")
        elif status == "controlled":
            if "DM-Review-Routine" not in tags:
                errors.append(f"{last_name} has Controlled diabetes but missing 'DM-Review-Routine' tag.")

    if errors:
        return False, " ".join(errors)
    return True, "Both E11.65 patients correctly tagged: Active→DM-Review-Urgent, Controlled→DM-Review-Routine."
