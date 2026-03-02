import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Dr. Kim is prov_4. His uninvited patients in seed data:
    # pat_15 (Brian Murphy), pat_23 (Victor Santos), pat_31 (Craig Bennet)
    target_patient_ids = ["pat_15", "pat_23", "pat_31"]
    patient_names = {
        "pat_15": "Brian Murphy",
        "pat_23": "Victor Santos",
        "pat_31": "Craig Bennet",
    }

    patients = state.get("patients", [])
    patient_map = {p["id"]: p for p in patients}

    for pid in target_patient_ids:
        patient = patient_map.get(pid)
        if patient is None:
            return False, f"Patient {patient_names[pid]} ({pid}) not found in state."

        if patient.get("passportStatus") != "invited":
            return False, (
                f"{patient_names[pid]} ({pid}) passportStatus is "
                f"'{patient.get('passportStatus')}', expected 'invited'."
            )

        if patient.get("invitationCode") is None:
            return False, (
                f"{patient_names[pid]} ({pid}) invitationCode is None, "
                f"expected a valid code."
            )

    return True, "All uninvited patients of Dr. Kim have been invited to Passport."
