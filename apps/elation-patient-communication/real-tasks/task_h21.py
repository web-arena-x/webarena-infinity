import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Reply to Raymond Copeland about thirst/urination, then schedule virtual
    appointment with Dr. Kim on March 25 at 11 AM."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    letters = state.get("patientLetters", [])
    # Check for reply in conv_34 (Raymond Copeland's thirst/urination message)
    reply = next(
        (
            l for l in letters
            if l.get("conversationId") == "conv_34"
            and l.get("direction") == "to_patient"
            and l.get("patientId") == "pat_35"
        ),
        None,
    )
    if reply is None:
        return False, "No reply found in Raymond Copeland's conversation (conv_34)."
    if reply.get("isDraft"):
        return False, "Reply to Raymond Copeland is still a draft."

    # Check for virtual appointment with Dr. Kim on March 25
    appointments = state.get("appointments", [])
    appt = next(
        (
            a for a in appointments
            if a.get("patientId") == "pat_35"
            and a.get("providerId") == "prov_4"
            and a.get("place") == "virtual"
            and a.get("status") == "scheduled"
            and "2026-03-25" in (a.get("date") or "")
        ),
        None,
    )
    if appt is None:
        return False, (
            "No virtual appointment found for Raymond Copeland with Dr. Kim "
            "on March 25, 2026."
        )

    return True, (
        "Reply sent to Raymond Copeland and virtual appointment scheduled "
        "with Dr. Kim on March 25."
    )
