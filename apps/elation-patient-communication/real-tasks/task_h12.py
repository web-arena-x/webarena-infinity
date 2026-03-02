import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    letters = state.get("patientLetters", [])

    # Dr. Torres (prov_2) open conversations in seed data:
    # conv_16 (pat_29, Andrew McIntyre) - open
    # conv_26 (pat_49, Russell Keane) - open

    # Check ALL letters in conv_16 have conversationState == "ended"
    conv_16_letters = [l for l in letters if l.get("conversationId") == "conv_16"]
    if not conv_16_letters:
        return False, "No letters found for conversation conv_16 (Andrew McIntyre)."

    for ltr in conv_16_letters:
        if ltr.get("conversationState") != "ended":
            return False, (
                f"Letter {ltr.get('id')} in conv_16 (Andrew McIntyre) has "
                f"conversationState '{ltr.get('conversationState')}', expected 'ended'."
            )

    # Check ALL letters in conv_26 have conversationState == "ended"
    conv_26_letters = [l for l in letters if l.get("conversationId") == "conv_26"]
    if not conv_26_letters:
        return False, "No letters found for conversation conv_26 (Russell Keane)."

    for ltr in conv_26_letters:
        if ltr.get("conversationState") != "ended":
            return False, (
                f"Letter {ltr.get('id')} in conv_26 (Russell Keane) has "
                f"conversationState '{ltr.get('conversationState')}', expected 'ended'."
            )

    return True, "All open conversations with Dr. Torres's patients have been ended."
