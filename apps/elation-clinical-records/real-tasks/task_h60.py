import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Add 'Recent-Diagnosis' tag to patients with at least one problem diagnosed in 2024 or later."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find patients with problems diagnosed 2024+
    patients_with_recent_dx = set()
    for prob in state.get("problems", []):
        dx_date = prob.get("dxDate", "")
        if dx_date and dx_date >= "2024-01-01":
            patients_with_recent_dx.add(prob.get("patientId"))

    errors = []
    tagged_names = []
    for patient in state.get("patients", []):
        pid = patient.get("id", "")
        last_name = patient.get("lastName", "?")
        tags = patient.get("tags", [])

        if pid in patients_with_recent_dx:
            if "Recent-Diagnosis" not in tags:
                errors.append(
                    f"{last_name} has a problem diagnosed in 2024+ but missing 'Recent-Diagnosis' tag."
                )
            else:
                tagged_names.append(last_name)

    if errors:
        return False, " ".join(errors)
    return True, (
        f"All {len(patients_with_recent_dx)} patients with recent diagnoses tagged 'Recent-Diagnosis': "
        f"{', '.join(tagged_names)}."
    )
