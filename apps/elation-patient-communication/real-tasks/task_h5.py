import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    letters = state.get("patientLetters", [])

    # Check ltr_20 (Janet Okonkwo, conv_14) is read
    ltr_20 = next((l for l in letters if l.get("id") == "ltr_20"), None)
    if ltr_20 is None:
        return False, "Letter ltr_20 (Janet Okonkwo) not found in state."
    if ltr_20.get("isRead") is not True:
        return False, "Letter ltr_20 (Janet Okonkwo) is still unread."

    # Check ltr_29 (Christine Lee, conv_21) is read
    ltr_29 = next((l for l in letters if l.get("id") == "ltr_29"), None)
    if ltr_29 is None:
        return False, "Letter ltr_29 (Christine Lee) not found in state."
    if ltr_29.get("isRead") is not True:
        return False, "Letter ltr_29 (Christine Lee) is still unread."

    # Check ALL letters in conv_14 have conversationState == "ended"
    conv_14_letters = [l for l in letters if l.get("conversationId") == "conv_14"]
    if not conv_14_letters:
        return False, "No letters found for conversation conv_14."
    for ltr in conv_14_letters:
        if ltr.get("conversationState") != "ended":
            return False, (
                f"Letter {ltr.get('id')} in conv_14 has conversationState "
                f"'{ltr.get('conversationState')}', expected 'ended'."
            )

    # Check ALL letters in conv_21 have conversationState == "ended"
    conv_21_letters = [l for l in letters if l.get("conversationId") == "conv_21"]
    if not conv_21_letters:
        return False, "No letters found for conversation conv_21."
    for ltr in conv_21_letters:
        if ltr.get("conversationState") != "ended":
            return False, (
                f"Letter {ltr.get('id')} in conv_21 has conversationState "
                f"'{ltr.get('conversationState')}', expected 'ended'."
            )

    return True, "Messages read and conversations ended for Janet Okonkwo and Christine Lee."
