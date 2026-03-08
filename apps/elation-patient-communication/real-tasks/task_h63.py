import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify reply in conv_24 and EC phone updated for pat_27 (Howard Blackwell)."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    seed_letter_ids = {f"ltr_{i}" for i in range(1, 48)}
    errors = []

    # Check for new reply in conv_24
    has_reply = False
    for ltr in state.get("patientLetters", []):
        if (ltr.get("conversationId") == "conv_24"
                and ltr.get("direction") == "to_patient"
                and ltr.get("id") not in seed_letter_ids
                and not ltr.get("isDraft", False)):
            has_reply = True
            break

    if not has_reply:
        errors.append("No new reply found in conv_24 (Howard Blackwell's message about gardening)")

    # Check EC phone updated
    pat_27 = None
    for p in state.get("patients", []):
        if p.get("id") == "pat_27":
            pat_27 = p
            break

    if not pat_27:
        errors.append("Patient pat_27 (Howard Blackwell) not found")
    else:
        ec = pat_27.get("emergencyContact", {})
        if not ec:
            errors.append("No emergency contact found for pat_27")
        else:
            phone = ec.get("phone", "")
            if phone != "(650) 555-0001":
                errors.append(f"EC phone is '{phone}', expected '(650) 555-0001'")

    if errors:
        return False, "; ".join(errors)
    return True, "Reply sent in conv_24 and EC phone updated to (650) 555-0001 for Howard Blackwell"
