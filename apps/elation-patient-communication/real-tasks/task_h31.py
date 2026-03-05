import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Remove 'New Patient' tag from all patients who have it."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Patients with "New Patient" tag in seed data:
    # pat_2 (Emily Thompson), pat_5 (Marcus Johnson),
    # pat_9 (Anthony Petrov), pat_31 (Craig Bennet), pat_42 (Megan Burke)
    target_ids = {
        "pat_2": "Emily Thompson",
        "pat_5": "Marcus Johnson",
        "pat_9": "Anthony Petrov",
        "pat_31": "Craig Bennet",
        "pat_42": "Megan Burke",
    }

    patients = state.get("patients", [])
    patient_map = {p["id"]: p for p in patients}

    for pid, name in target_ids.items():
        patient = patient_map.get(pid)
        if patient is None:
            return False, f"Patient {name} ({pid}) not found."
        if "New Patient" in patient.get("tags", []):
            return False, (
                f"{name} ({pid}) still has the 'New Patient' tag."
            )

    return True, "'New Patient' tag removed from all 5 patients."
