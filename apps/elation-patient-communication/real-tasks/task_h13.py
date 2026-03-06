import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that open conversations inactive since before Feb 25, 2026 have been ended."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    letters = state.get("patientLetters", [])

    # Open conversations with all letters having sentAt before 2026-02-25T00:00:00Z:
    # conv_8 (Kevin Adebayo billing - last letter ltr_12 sentAt 2026-02-24T16:00:00Z)
    # conv_9 (Maria Gonzalez labs - last letter ltr_14 sentAt 2026-02-23T14:00:00Z)
    conversations_to_end = ["conv_8", "conv_9"]

    not_ended = {}
    for ltr in letters:
        conv_id = ltr.get("conversationId")
        if conv_id in conversations_to_end:
            if ltr.get("conversationState") != "ended":
                if conv_id not in not_ended:
                    not_ended[conv_id] = []
                not_ended[conv_id].append(ltr.get("id"))

    if not_ended:
        details = []
        for conv_id, ltr_ids in not_ended.items():
            details.append(f"{conv_id}: letters {', '.join(ltr_ids)} not ended")
        return False, (
            f"The following inactive conversations are not fully ended: "
            f"{'; '.join(details)}"
        )

    # Spot-check that conversations active on/after Feb 25 are NOT ended
    # conv_1 (last activity 2026-02-25T16:20:00Z) should still be open
    # conv_20 (last activity 2026-02-25T10:00:00Z) should still be open
    spot_check_convs = ["conv_1", "conv_20"]
    wrongly_ended = []
    for ltr in letters:
        conv_id = ltr.get("conversationId")
        if conv_id in spot_check_convs:
            if ltr.get("conversationState") == "ended":
                wrongly_ended.append(f"{conv_id}/{ltr.get('id')}")

    if wrongly_ended:
        return False, (
            f"Some conversations that should still be open were incorrectly ended: "
            f"{', '.join(wrongly_ended)}"
        )

    return True, (
        "Open conversations inactive before Feb 25, 2026 (conv_8, conv_9) have been ended. "
        "Active conversations remain open."
    )
