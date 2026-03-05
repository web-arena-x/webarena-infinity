import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Invite all patients who have never been invited to Passport."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Patients with passportStatus="not_invited" in seed data:
    # pat_9 (Anthony Petrov), pat_15 (Brian Murphy),
    # pat_23 (Victor Santos), pat_31 (Craig Bennet),
    # pat_37 (Jason Liu), pat_42 (Megan Burke)
    target_patients = {
        "pat_9": "Anthony Petrov",
        "pat_15": "Brian Murphy",
        "pat_23": "Victor Santos",
        "pat_31": "Craig Bennet",
        "pat_37": "Jason Liu",
        "pat_42": "Megan Burke",
    }

    patients = state.get("patients", [])
    patient_map = {p["id"]: p for p in patients}

    for pid, name in target_patients.items():
        patient = patient_map.get(pid)
        if patient is None:
            return False, f"Patient {name} ({pid}) not found."

        if patient.get("passportStatus") != "invited":
            return False, (
                f"{name} ({pid}) passportStatus is "
                f"'{patient.get('passportStatus')}', expected 'invited'."
            )
        if patient.get("invitationCode") is None:
            return False, (
                f"{name} ({pid}) invitationCode is None, "
                f"expected a valid code."
            )

    return True, "All 6 uninvited patients have been invited to Passport."
