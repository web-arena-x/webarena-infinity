import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    letters = state.get("patientLetters", [])

    # Seed data: conv_4 has only ltr_6 (from_patient), conv_28 has only ltr_39 (from_patient)
    seed_letter_ids = {"ltr_6", "ltr_39"}

    # Check conv_4 (Sophia Nguyen) - should have a new to_patient letter
    conv_4_replies = [
        l for l in letters
        if l.get("conversationId") == "conv_4"
        and l.get("direction") == "to_patient"
        and l.get("id") not in seed_letter_ids
    ]

    if not conv_4_replies:
        return False, (
            "No reply found in conv_4 (Sophia Nguyen). "
            "Expected a new to_patient letter."
        )

    for reply in conv_4_replies:
        if reply.get("isDraft") is True:
            return False, (
                f"Reply {reply.get('id')} in conv_4 is still a draft, expected sent."
            )

    # Check conv_28 (Susan Cho) - should have a new to_patient letter
    conv_28_replies = [
        l for l in letters
        if l.get("conversationId") == "conv_28"
        and l.get("direction") == "to_patient"
    ]

    if not conv_28_replies:
        return False, (
            "No reply found in conv_28 (Susan Cho). "
            "Expected a new to_patient letter."
        )

    for reply in conv_28_replies:
        if reply.get("isDraft") is True:
            return False, (
                f"Reply {reply.get('id')} in conv_28 is still a draft, expected sent."
            )

    return True, "Replies sent to both Sophia Nguyen and Susan Cho."
