import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that Raymond Copeland's message was read and a reply was sent."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    letters = state.get("patientLetters", [])

    seed_letter_ids = {
        "ltr_1", "ltr_2", "ltr_3", "ltr_4", "ltr_5", "ltr_6", "ltr_7", "ltr_8",
        "ltr_9", "ltr_10", "ltr_11", "ltr_12", "ltr_13", "ltr_14", "ltr_15",
        "ltr_16", "ltr_17", "ltr_18", "ltr_19", "ltr_20", "ltr_21", "ltr_22",
        "ltr_23", "ltr_24", "ltr_25", "ltr_26", "ltr_27", "ltr_28", "ltr_29",
        "ltr_30", "ltr_31", "ltr_32", "ltr_33", "ltr_34", "ltr_35", "ltr_36",
        "ltr_37", "ltr_38", "ltr_39", "ltr_40", "ltr_41", "ltr_42", "ltr_43",
        "ltr_44", "ltr_45", "ltr_46", "ltr_47"
    }

    # Check ltr_46 is marked as read
    ltr_46 = None
    for ltr in letters:
        if ltr.get("id") == "ltr_46":
            ltr_46 = ltr
            break

    if ltr_46 is None:
        return False, "Letter ltr_46 (Raymond Copeland's message) not found"

    if not ltr_46.get("isRead"):
        return False, f"Letter ltr_46 isRead is {ltr_46.get('isRead')}, expected True"

    # Check for a reply in conv_34
    conv_34_letters = [ltr for ltr in letters if ltr.get("conversationId") == "conv_34"]
    new_reply = None
    for ltr in conv_34_letters:
        if (ltr.get("id") not in seed_letter_ids
                and ltr.get("direction") == "to_patient"
                and not ltr.get("isDraft", False)):
            new_reply = ltr
            break

    if new_reply is None:
        return False, "No reply (to_patient) found in conversation conv_34 for Raymond Copeland"

    return True, "Raymond Copeland's message was read and a reply was sent"
