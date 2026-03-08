import requests
from datetime import datetime


def verify(server_url: str) -> tuple[bool, str]:
    """Add 'Flu-Overdue' to patients over 65 with no influenza vaccine record."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    today = datetime(2026, 3, 8)

    # Find patients with influenza vaccines
    patients_with_flu = set()
    for v in state.get("vaccinations", []):
        name = (v.get("vaccineName") or "").lower()
        if "influenza" in name or "flu" in name:
            patients_with_flu.add(v.get("patientId"))

    errors = []
    tagged_names = []
    for patient in state.get("patients", []):
        pid = patient.get("id", "")
        last_name = patient.get("lastName", "?")
        dob_str = patient.get("dateOfBirth", "")
        tags = patient.get("tags", [])

        if not dob_str:
            continue

        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d")
            age = (today - dob).days // 365
        except ValueError:
            continue

        if age > 65 and pid not in patients_with_flu:
            if "Flu-Overdue" not in tags:
                errors.append(f"{last_name} (age {age}) has no flu vaccine but missing 'Flu-Overdue' tag.")
            else:
                tagged_names.append(f"{last_name}({age})")

    if errors:
        return False, " ".join(errors)
    return True, (
        f"All patients over 65 without flu vaccines tagged 'Flu-Overdue': "
        f"{', '.join(tagged_names)}."
    )
