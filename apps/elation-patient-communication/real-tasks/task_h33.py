import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Send no-reply letter to Christine Lee, acknowledge Catherine Morales
    reminder."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Check letter to Christine Lee with correct subject and no-reply
    letters = state.get("patientLetters", [])
    letter = next(
        (
            l for l in letters
            if l.get("patientId") == "pat_22"
            and l.get("direction") == "to_patient"
            and l.get("subject") == "Sleep Concerns Follow-up"
        ),
        None,
    )
    if letter is None:
        return False, (
            "No letter found to Christine Lee with subject "
            "'Sleep Concerns Follow-up'."
        )
    if letter.get("isDraft"):
        return False, "Letter to Christine Lee is still a draft."
    if not letter.get("doNotAllowResponse"):
        return False, (
            "Letter to Christine Lee does not have 'do not allow response' "
            "enabled."
        )

    # Check rem_6 acknowledged
    reminders = state.get("reminders", [])
    rem_6 = next((r for r in reminders if r.get("id") == "rem_6"), None)
    if rem_6 is None:
        return False, (
            "Reminder rem_6 (Catherine Morales thyroid update) not found."
        )
    if not rem_6.get("acknowledged"):
        return False, (
            "Reminder about Catherine Morales (rem_6) has not been "
            "acknowledged."
        )

    return True, (
        "No-reply letter sent to Christine Lee and Catherine Morales "
        "reminder acknowledged."
    )
