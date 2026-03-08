import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that every patient with 4+ active problems has 'Multi-Condition' tag and others do not."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    patients = state.get("patients", [])
    problems = state.get("problems", [])

    if not patients:
        return False, "No patients found in state"
    if not problems:
        return False, "No problems found in state"

    errors = []
    tag_name = "Multi-Condition"

    for patient in patients:
        patient_id = patient.get("id", "")
        patient_name = patient.get("lastName", patient.get("name", "unknown"))

        active_count = sum(
            1 for p in problems
            if p.get("patientId") == patient_id and p.get("status", "").lower() == "active"
        )

        tags = [t.lower() for t in patient.get("tags", [])]
        has_tag = tag_name.lower() in tags

        if active_count >= 4 and not has_tag:
            errors.append(
                f"Patient '{patient_name}' has {active_count} active problems but is missing '{tag_name}' tag"
            )
        elif active_count < 4 and has_tag:
            errors.append(
                f"Patient '{patient_name}' has only {active_count} active problems but has '{tag_name}' tag"
            )

    if errors:
        return False, "; ".join(errors)
    return True, "All patients with 4+ active problems have 'Multi-Condition' tag and others do not"
