import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify letters sent to both Spanish Speaking patients and sharing level upgraded for pat_46."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    seed_letter_ids = {f"ltr_{i}" for i in range(1, 48)}
    errors = []

    # Check letters sent to both patients
    spanish_patients = {
        "pat_14": "Maria Gonzalez",
        "pat_46": "Catherine Morales",
    }

    for pat_id, name in spanish_patients.items():
        letter_found = False
        for ltr in state.get("patientLetters", []):
            if (ltr.get("id") not in seed_letter_ids
                    and ltr.get("patientId") == pat_id
                    and ltr.get("direction") == "to_patient"
                    and not ltr.get("isDraft", False)):
                letter_found = True
                break
        if not letter_found:
            errors.append(f"No new letter sent to {name} ({pat_id})")

    # Check pat_46 sharing level upgraded to 3
    pat_46 = None
    for p in state.get("patients", []):
        if p.get("id") == "pat_46":
            pat_46 = p
            break

    if not pat_46:
        errors.append("Patient pat_46 (Catherine Morales) not found")
    else:
        level = pat_46.get("passportSharingLevel")
        if level < 3:
            errors.append(
                f"Catherine Morales (pat_46) sharing level is {level}, expected >= 3"
            )

    if errors:
        return False, "; ".join(errors)
    return True, "Letters sent to both Spanish Speaking patients, pat_46 sharing level upgraded to 3"
