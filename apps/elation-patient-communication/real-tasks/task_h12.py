import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that all unread patient messages in the inbox have been replied to."""
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

    # Conversations that had unread from_patient letters in seed data:
    # conv_2 (ltr_4), conv_4 (ltr_6), conv_7 (ltr_10), conv_10 (ltr_15),
    # conv_13 (ltr_19), conv_14 (ltr_20), conv_16 (ltr_23), conv_17 (ltr_24),
    # conv_21 (ltr_29), conv_28 (ltr_39), conv_34 (ltr_46), conv_35 (ltr_47)
    unread_conversations = [
        "conv_2", "conv_4", "conv_7", "conv_10", "conv_13", "conv_14",
        "conv_16", "conv_17", "conv_21", "conv_28", "conv_34", "conv_35"
    ]

    # Group letters by conversation
    conv_letters = {}
    for ltr in letters:
        cid = ltr.get("conversationId")
        if cid not in conv_letters:
            conv_letters[cid] = []
        conv_letters[cid].append(ltr)

    no_reply = []
    for conv_id in unread_conversations:
        conv_ltrs = conv_letters.get(conv_id, [])
        has_new_reply = False
        for ltr in conv_ltrs:
            if (ltr.get("id") not in seed_letter_ids
                    and ltr.get("direction") == "to_patient"
                    and not ltr.get("isDraft", False)):
                has_new_reply = True
                break

        if not has_new_reply:
            no_reply.append(conv_id)

    if no_reply:
        return False, (
            f"The following conversations with unread messages have no reply: "
            f"{', '.join(no_reply)}"
        )

    return True, "All 12 unread patient messages in the inbox have been replied to"
