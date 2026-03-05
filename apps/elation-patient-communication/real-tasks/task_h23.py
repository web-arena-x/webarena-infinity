import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Reply to the referral request about the retired allergist and tag
    the patient as VIP. Patient is Diane Foster-Hutchinson (pat_16)."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    letters = state.get("patientLetters", [])
    # Check reply in conv_10 (Diane Foster-Hutchinson's referral request)
    reply = next(
        (
            l for l in letters
            if l.get("conversationId") == "conv_10"
            and l.get("direction") == "to_patient"
            and l.get("patientId") == "pat_16"
        ),
        None,
    )
    if reply is None:
        return False, (
            "No reply found in Diane Foster-Hutchinson's referral "
            "conversation (conv_10)."
        )
    if reply.get("isDraft"):
        return False, "Reply to Diane Foster-Hutchinson is still a draft."

    # Check VIP tag on pat_16
    patients = state.get("patients", [])
    pat_16 = next((p for p in patients if p.get("id") == "pat_16"), None)
    if pat_16 is None:
        return False, "Patient pat_16 (Diane Foster-Hutchinson) not found."
    if "VIP" not in pat_16.get("tags", []):
        return False, (
            f"Diane Foster-Hutchinson's tags are {pat_16.get('tags')}, "
            f"expected 'VIP' to be present."
        )

    return True, (
        "Reply sent to Diane Foster-Hutchinson's referral request "
        "and 'VIP' tag added."
    )
