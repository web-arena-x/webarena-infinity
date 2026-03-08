import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Patients with Active+Controlled → 'Mixed-Status'. Active-only → 'All-Active'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Categorize patients by problem statuses
    patient_statuses = {}
    for prob in state.get("problems", []):
        pid = prob["patientId"]
        status = prob.get("status", "")
        if pid not in patient_statuses:
            patient_statuses[pid] = set()
        patient_statuses[pid].add(status)

    errors = []
    for patient in state.get("patients", []):
        pid = patient["id"]
        tags = patient.get("tags", [])
        statuses = patient_statuses.get(pid, set())
        has_active = "Active" in statuses
        has_controlled = "Controlled" in statuses

        if has_active and has_controlled:
            if "Mixed-Status" not in tags:
                errors.append(f"{patient['lastName']} should have 'Mixed-Status'.")
            if "All-Active" in tags:
                errors.append(f"{patient['lastName']} should NOT have 'All-Active'.")
        elif has_active and not has_controlled:
            if "All-Active" not in tags:
                errors.append(f"{patient['lastName']} should have 'All-Active'.")
            if "Mixed-Status" in tags:
                errors.append(f"{patient['lastName']} should NOT have 'Mixed-Status'.")
        else:
            if "Mixed-Status" in tags:
                errors.append(f"{patient['lastName']} should NOT have 'Mixed-Status'.")
            if "All-Active" in tags:
                errors.append(f"{patient['lastName']} should NOT have 'All-Active'.")

    if errors:
        return False, " ".join(errors)
    return True, "All patients correctly tagged with 'Mixed-Status' or 'All-Active'."
