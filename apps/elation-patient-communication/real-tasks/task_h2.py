import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that a reply was sent to Christine Lee and conversation conv_21 was ended."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    letters = state.get("patientLetters", [])

    # Seed data only has ltr_29 in conv_21 (from_patient, unread)
    seed_letter_ids = {
        "ltr_1", "ltr_2", "ltr_3", "ltr_4", "ltr_5", "ltr_6", "ltr_7", "ltr_8",
        "ltr_9", "ltr_10", "ltr_11", "ltr_12", "ltr_13", "ltr_14", "ltr_15",
        "ltr_16", "ltr_17", "ltr_18", "ltr_19", "ltr_20", "ltr_21", "ltr_22",
        "ltr_23", "ltr_24", "ltr_25", "ltr_26", "ltr_27", "ltr_28", "ltr_29",
        "ltr_30", "ltr_31", "ltr_32", "ltr_33", "ltr_34", "ltr_35", "ltr_36",
        "ltr_37", "ltr_38", "ltr_39", "ltr_40", "ltr_41", "ltr_42", "ltr_43",
        "ltr_44", "ltr_45", "ltr_46", "ltr_47"
    }

    conv_21_letters = [ltr for ltr in letters if ltr.get("conversationId") == "conv_21"]

    if not conv_21_letters:
        return False, "No letters found for conversation conv_21 (Christine Lee)"

    # Check for a new reply (to_patient, not in seed data, not a draft)
    new_reply = None
    for ltr in conv_21_letters:
        if (ltr.get("id") not in seed_letter_ids
                and ltr.get("direction") == "to_patient"
                and not ltr.get("isDraft", False)):
            new_reply = ltr
            break

    if new_reply is None:
        return False, "No new reply (to_patient) found in conversation conv_21 for Christine Lee"

    # Check that all letters in conv_21 have conversationState "ended"
    not_ended = []
    for ltr in conv_21_letters:
        if ltr.get("conversationState") != "ended":
            not_ended.append(ltr.get("id"))

    if not_ended:
        return False, (
            f"Conversation conv_21 is not fully ended. Letters without 'ended' state: "
            f"{', '.join(not_ended)}"
        )

    return True, "Reply sent to Christine Lee about insomnia and conversation conv_21 ended"
