import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Reply to Maria Gonzalez's conversation and acknowledge rem_1."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Check reply in conv_9 (Maria Gonzalez's diet/Metformin questions)
    letters = state.get("patientLetters", [])
    reply = next(
        (
            l for l in letters
            if l.get("conversationId") == "conv_9"
            and l.get("direction") == "to_patient"
            and l.get("patientId") == "pat_14"
            and l.get("id") not in ("ltr_13",)  # exclude original sent letter
        ),
        None,
    )
    if reply is None:
        return False, (
            "No reply found in Maria Gonzalez's conversation (conv_9)."
        )
    if reply.get("isDraft"):
        return False, "Reply to Maria Gonzalez is still a draft."

    # Check rem_1 acknowledged
    reminders = state.get("reminders", [])
    rem_1 = next((r for r in reminders if r.get("id") == "rem_1"), None)
    if rem_1 is None:
        return False, "Reminder rem_1 (Maria Gonzalez unread alert) not found."
    if not rem_1.get("acknowledged"):
        return False, (
            "Reminder about Maria Gonzalez's lab results (rem_1) "
            "has not been acknowledged."
        )

    return True, (
        "Reply sent to Maria Gonzalez and lab results reminder acknowledged."
    )
