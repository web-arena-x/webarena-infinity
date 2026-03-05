import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Read both unread appointment requests, reply to urticaria patient
    (Susan Cho), and schedule virtual appt with Dr. Okafor on Mar 14."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    letters = state.get("patientLetters", [])

    # Check ltr_6 (Sophia Nguyen) is read
    ltr_6 = next((l for l in letters if l.get("id") == "ltr_6"), None)
    if ltr_6 is None:
        return False, "Letter ltr_6 (Sophia Nguyen appointment request) not found."
    if not ltr_6.get("isRead"):
        return False, "Sophia Nguyen's appointment request (ltr_6) not marked read."

    # Check ltr_39 (Susan Cho) is read
    ltr_39 = next((l for l in letters if l.get("id") == "ltr_39"), None)
    if ltr_39 is None:
        return False, "Letter ltr_39 (Susan Cho appointment request) not found."
    if not ltr_39.get("isRead"):
        return False, "Susan Cho's appointment request (ltr_39) not marked read."

    # Check reply in conv_28 (Susan Cho's urticaria conversation)
    reply = next(
        (
            l for l in letters
            if l.get("conversationId") == "conv_28"
            and l.get("direction") == "to_patient"
            and l.get("patientId") == "pat_40"
        ),
        None,
    )
    if reply is None:
        return False, "No reply found in Susan Cho's conversation (conv_28)."
    if reply.get("isDraft"):
        return False, "Reply to Susan Cho is still a draft."

    # Check virtual appointment for pat_40 with prov_3 on March 14
    appointments = state.get("appointments", [])
    appt = next(
        (
            a for a in appointments
            if a.get("patientId") == "pat_40"
            and a.get("providerId") == "prov_3"
            and a.get("place") == "virtual"
            and a.get("status") == "scheduled"
            and "2026-03-14" in (a.get("date") or "")
        ),
        None,
    )
    if appt is None:
        return False, (
            "No virtual appointment found for Susan Cho with Dr. Okafor "
            "on March 14, 2026."
        )

    return True, (
        "Both appointment requests read, reply sent to Susan Cho, and "
        "virtual appointment scheduled with Dr. Okafor."
    )
