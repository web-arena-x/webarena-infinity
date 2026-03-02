import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    patients = state.get("patients", [])
    patient_map = {p["id"]: p for p in patients}

    # Patients with passportStatus "invited" in seed data and their original codes
    invited_patients = {
        "pat_5": {"name": "Marcus Johnson", "original_code": "3847261"},
        "pat_13": {"name": "William Chang", "original_code": "1746290"},
        "pat_21": {"name": "George Kowalski", "original_code": "5027184"},
        "pat_28": {"name": "Stephanie Rivera", "original_code": "2648901"},
        "pat_39": {"name": "Tyler Robinson", "original_code": "7194028"},
        "pat_48": {"name": "Michelle O'Connor", "original_code": "4019283"},
    }

    for pid, info in invited_patients.items():
        patient = patient_map.get(pid)
        if patient is None:
            return False, f"Patient {info['name']} ({pid}) not found in state."

        # Check still invited
        if patient.get("passportStatus") != "invited":
            return False, (
                f"{info['name']} ({pid}) passportStatus is "
                f"'{patient.get('passportStatus')}', expected 'invited'."
            )

        # Check invitation code changed (resent)
        current_code = patient.get("invitationCode")
        if current_code is None:
            return False, (
                f"{info['name']} ({pid}) invitationCode is None."
            )

        if str(current_code) == info["original_code"]:
            return False, (
                f"{info['name']} ({pid}) invitationCode is still the original "
                f"'{info['original_code']}'. Expected a new code after resend."
            )

    return True, "Passport invitations resent to all 6 patients."
