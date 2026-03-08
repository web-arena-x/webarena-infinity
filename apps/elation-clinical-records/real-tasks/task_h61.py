import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Add 'External-Review' to patients whose provider != current provider AND have active problems."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    current_provider_id = state["currentProvider"]["id"]

    # Find patients with active problems whose provider != current
    active_by_patient = {}
    for prob in state.get("problems", []):
        if prob.get("status") == "Active":
            pid = prob["patientId"]
            active_by_patient[pid] = active_by_patient.get(pid, 0) + 1

    errors = []
    for patient in state.get("patients", []):
        pid = patient["id"]
        tags = patient.get("tags", [])
        is_external = patient.get("primaryProvider") != current_provider_id
        has_active = active_by_patient.get(pid, 0) > 0

        if is_external and has_active:
            if "External-Review" not in tags:
                errors.append(f"{patient['lastName']} should have 'External-Review' tag.")
        else:
            if "External-Review" in tags:
                errors.append(f"{patient['lastName']} should NOT have 'External-Review' tag.")

    if errors:
        return False, " ".join(errors)
    return True, "All qualifying external-provider patients tagged 'External-Review'."
