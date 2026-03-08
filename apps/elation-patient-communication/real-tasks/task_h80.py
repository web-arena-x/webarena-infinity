import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify letter sent to CABG patient, tag added, and EC phone updated."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    seed_letter_ids = {f"ltr_{i}" for i in range(1, 48)}
    errors = []

    # Check for new letter to pat_3
    letter_found = False
    for ltr in state.get("patientLetters", []):
        if (ltr.get("id") not in seed_letter_ids
                and ltr.get("patientId") == "pat_3"
                and ltr.get("direction") == "to_patient"
                and not ltr.get("isDraft", False)):
            letter_found = True
            break

    if not letter_found:
        errors.append("No new letter sent to pat_3 (Robert Washington, CABG patient)")

    # Check patient
    pat_3 = None
    for p in state.get("patients", []):
        if p.get("id") == "pat_3":
            pat_3 = p
            break

    if not pat_3:
        errors.append("Patient pat_3 (Robert Washington) not found")
    else:
        tags = pat_3.get("tags", [])
        if "Telehealth Preferred" not in tags:
            errors.append(f"Missing 'Telehealth Preferred' tag. Tags: {tags}")

        ec = pat_3.get("emergencyContact", {})
        if not ec:
            errors.append("No emergency contact found for pat_3")
        else:
            phone = ec.get("phone", "")
            if phone != "(510) 555-9999":
                errors.append(f"EC phone is '{phone}', expected '(510) 555-9999'")

    if errors:
        return False, "; ".join(errors)
    return True, "Letter sent to CABG patient, Telehealth Preferred added, EC phone updated"
