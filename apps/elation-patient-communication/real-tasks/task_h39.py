import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Read unread messages from Christine Lee and Diane Foster-Hutchinson,
    reply to both, and sign off both conversations."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    letters = state.get("patientLetters", [])

    # Check ltr_29 (Christine Lee) is read
    ltr_29 = next((l for l in letters if l.get("id") == "ltr_29"), None)
    if ltr_29 is None:
        return False, "Letter ltr_29 (Christine Lee) not found."
    if not ltr_29.get("isRead"):
        return False, "Christine Lee's message (ltr_29) not marked read."

    # Check ltr_15 (Diane Foster-Hutchinson) is read
    ltr_15 = next((l for l in letters if l.get("id") == "ltr_15"), None)
    if ltr_15 is None:
        return False, "Letter ltr_15 (Diane Foster-Hutchinson) not found."
    if not ltr_15.get("isRead"):
        return False, (
            "Diane Foster-Hutchinson's message (ltr_15) not marked read."
        )

    # Check reply in conv_21 (Christine Lee)
    reply_cl = next(
        (
            l for l in letters
            if l.get("conversationId") == "conv_21"
            and l.get("direction") == "to_patient"
            and l.get("patientId") == "pat_22"
        ),
        None,
    )
    if reply_cl is None:
        return False, "No reply found in Christine Lee's conversation (conv_21)."
    if reply_cl.get("isDraft"):
        return False, "Reply to Christine Lee is still a draft."

    # Check reply in conv_10 (Diane Foster-Hutchinson)
    reply_dh = next(
        (
            l for l in letters
            if l.get("conversationId") == "conv_10"
            and l.get("direction") == "to_patient"
            and l.get("patientId") == "pat_16"
        ),
        None,
    )
    if reply_dh is None:
        return False, (
            "No reply found in Diane Foster-Hutchinson's "
            "conversation (conv_10)."
        )
    if reply_dh.get("isDraft"):
        return False, "Reply to Diane Foster-Hutchinson is still a draft."

    # Check both conversations are ended
    for conv_id, name in [("conv_21", "Christine Lee"), ("conv_10", "Diane Foster-Hutchinson")]:
        conv_letters = [l for l in letters if l.get("conversationId") == conv_id]
        for ltr in conv_letters:
            if ltr.get("conversationState") != "ended":
                return False, (
                    f"Letter {ltr.get('id')} in {conv_id} ({name}) has "
                    f"conversationState '{ltr.get('conversationState')}', "
                    f"expected 'ended'."
                )

    return True, (
        "Both messages read, replies sent, and conversations signed off "
        "for Christine Lee and Diane Foster-Hutchinson."
    )
