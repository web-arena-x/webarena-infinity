import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Reply to Priya Sharma's medical records request and sign off."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    letters = state.get("patientLetters", [])

    # Check reply in conv_13
    reply = next(
        (
            l for l in letters
            if l.get("conversationId") == "conv_13"
            and l.get("direction") == "to_patient"
            and l.get("patientId") == "pat_32"
        ),
        None,
    )
    if reply is None:
        return False, (
            "No reply found in Priya Sharma's medical records "
            "conversation (conv_13)."
        )
    if reply.get("isDraft"):
        return False, "Reply to Priya Sharma is still a draft."

    # Check conversation is ended
    conv_letters = [
        l for l in letters if l.get("conversationId") == "conv_13"
    ]
    for ltr in conv_letters:
        if ltr.get("conversationState") != "ended":
            return False, (
                f"Letter {ltr.get('id')} in conv_13 has conversationState "
                f"'{ltr.get('conversationState')}', expected 'ended'."
            )

    return True, (
        "Reply sent to Priya Sharma and conversation signed off."
    )
