import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Cancel Janet Okonkwo's virtual appt, schedule in-person with Dr. Chen
    on March 10 at 9 AM, and reply to her message."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Check appt_13 is cancelled
    appointments = state.get("appointments", [])
    appt_13 = next((a for a in appointments if a.get("id") == "appt_13"), None)
    if appt_13 is None:
        return False, "Appointment appt_13 (Janet Okonkwo virtual) not found."
    if appt_13.get("status") != "cancelled":
        return False, (
            f"Janet Okonkwo's virtual appointment status is "
            f"'{appt_13.get('status')}', expected 'cancelled'."
        )

    # Check new in-person appointment for pat_30 with prov_1 on March 10
    new_appt = next(
        (
            a for a in appointments
            if a.get("patientId") == "pat_30"
            and a.get("providerId") == "prov_1"
            and a.get("place") == "in_person"
            and a.get("status") == "scheduled"
            and "2026-03-10" in (a.get("date") or "")
        ),
        None,
    )
    if new_appt is None:
        return False, (
            "No in-person appointment found for Janet Okonkwo with "
            "Dr. Chen on March 10, 2026."
        )

    # Check reply in conv_14
    letters = state.get("patientLetters", [])
    reply = next(
        (
            l for l in letters
            if l.get("conversationId") == "conv_14"
            and l.get("direction") == "to_patient"
            and l.get("patientId") == "pat_30"
        ),
        None,
    )
    if reply is None:
        return False, "No reply found in Janet Okonkwo's conversation (conv_14)."
    if reply.get("isDraft"):
        return False, "Reply to Janet Okonkwo is still a draft."

    return True, (
        "Janet Okonkwo's virtual appointment cancelled, in-person "
        "appointment scheduled, and reply sent."
    )
