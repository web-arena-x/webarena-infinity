import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    patients = state.get("patients", [])
    patient_map = {p["id"]: p for p in patients}

    targets = {
        "pat_23": "Victor Santos",
        "pat_31": "Craig Bennet",
    }

    for pid, name in targets.items():
        patient = patient_map.get(pid)
        if patient is None:
            return False, f"Patient {name} ({pid}) not found in state."

        # Check "Insurance Pending" tag
        tags = patient.get("tags", [])
        if "Insurance Pending" not in tags:
            return False, (
                f"{name} ({pid}) does not have 'Insurance Pending' tag. "
                f"Current tags: {tags}."
            )

        # Check passport status
        if patient.get("passportStatus") != "invited":
            return False, (
                f"{name} ({pid}) passportStatus is "
                f"'{patient.get('passportStatus')}', expected 'invited'."
            )

        # Check invitation code
        if patient.get("invitationCode") is None:
            return False, (
                f"{name} ({pid}) invitationCode is None, expected a valid code."
            )

    return True, "Victor Santos and Craig Bennet tagged and invited to Passport."
