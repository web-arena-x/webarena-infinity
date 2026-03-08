import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Add 'Frequent-Visitor' to patients with 2+ signed visit notes."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Count signed notes per patient
    signed_counts = {}
    for n in state.get("visitNotes", []):
        if n.get("status") == "signed":
            pid = n.get("patientId")
            signed_counts[pid] = signed_counts.get(pid, 0) + 1

    errors = []
    tagged_names = []
    for patient in state.get("patients", []):
        pid = patient.get("id", "")
        last_name = patient.get("lastName", "?")
        tags = patient.get("tags", [])
        count = signed_counts.get(pid, 0)

        if count >= 2:
            if "Frequent-Visitor" not in tags:
                errors.append(
                    f"{last_name} has {count} signed notes but missing 'Frequent-Visitor' tag."
                )
            else:
                tagged_names.append(f"{last_name}({count})")

    if errors:
        return False, " ".join(errors)
    return True, (
        f"Patients with 2+ signed notes correctly tagged 'Frequent-Visitor': "
        f"{', '.join(tagged_names)}."
    )
