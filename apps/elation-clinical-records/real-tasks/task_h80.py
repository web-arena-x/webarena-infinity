import requests
from collections import defaultdict


def verify(server_url: str) -> tuple[bool, str]:
    """Patients with signed notes in >1 category → 'Multi-Visit-Type'.
    Patients with signed notes in exactly 1 category → 'Single-Visit-Type'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Collect categories per patient from signed notes
    patient_cats = defaultdict(set)
    for note in state.get("visitNotes", []):
        if note.get("status") == "signed":
            patient_cats[note["patientId"]].add(note.get("category", ""))

    errors = []
    for patient in state.get("patients", []):
        pid = patient["id"]
        tags = patient.get("tags", [])
        name = patient.get("lastName", pid)
        cats = patient_cats.get(pid, set())

        if len(cats) > 1:
            if "Multi-Visit-Type" not in tags:
                errors.append(f"{name} ({len(cats)} categories) missing 'Multi-Visit-Type'.")
            if "Single-Visit-Type" in tags:
                errors.append(f"{name} should NOT have 'Single-Visit-Type'.")
        elif len(cats) == 1:
            if "Single-Visit-Type" not in tags:
                errors.append(f"{name} (1 category) missing 'Single-Visit-Type'.")
            if "Multi-Visit-Type" in tags:
                errors.append(f"{name} should NOT have 'Multi-Visit-Type'.")
        else:
            if "Multi-Visit-Type" in tags:
                errors.append(f"{name} (no signed notes) should NOT have 'Multi-Visit-Type'.")
            if "Single-Visit-Type" in tags:
                errors.append(f"{name} (no signed notes) should NOT have 'Single-Visit-Type'.")

    if errors:
        return False, " ".join(errors)
    return True, "All patients correctly tagged based on signed note category diversity."
