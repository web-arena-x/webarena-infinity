import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify reply in conv_7, High Risk tag, and sharing level 4 for pat_10."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    seed_letter_ids = {f"ltr_{i}" for i in range(1, 48)}
    errors = []

    # Check for reply in conv_7
    has_reply = False
    for ltr in state.get("patientLetters", []):
        if (ltr.get("conversationId") == "conv_7"
                and ltr.get("direction") == "to_patient"
                and ltr.get("id") not in seed_letter_ids
                and not ltr.get("isDraft", False)):
            has_reply = True
            break

    if not has_reply:
        errors.append("No new reply in conv_7 (Helen Matsumoto's forgetfulness message)")

    # Check pat_10
    pat_10 = None
    for p in state.get("patients", []):
        if p.get("id") == "pat_10":
            pat_10 = p
            break

    if not pat_10:
        errors.append("Patient pat_10 (Helen Matsumoto) not found")
    else:
        tags = pat_10.get("tags", [])
        if "High Risk" not in tags:
            errors.append(f"Missing 'High Risk' tag. Tags: {tags}")
        if "Geriatric" not in tags:
            errors.append(f"Lost 'Geriatric' tag. Tags: {tags}")

        level = pat_10.get("passportSharingLevel")
        if level != 4:
            errors.append(f"Sharing level is {level}, expected 4")

    if errors:
        return False, "; ".join(errors)
    return True, "Reply sent in conv_7, High Risk tag added, sharing level set to 4 for pat_10"
