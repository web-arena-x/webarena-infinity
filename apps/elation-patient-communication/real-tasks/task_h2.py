import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find all letters where direction == "from_patient" and isDraft == False
    letters = state.get("patientLetters", [])
    patient_messages = [
        ltr for ltr in letters
        if ltr.get("direction") == "from_patient" and ltr.get("isDraft") is False
    ]

    if not patient_messages:
        return False, "No patient messages found in state."

    count = len(patient_messages)
    unread = []
    for ltr in patient_messages:
        if ltr.get("isRead") is not True:
            unread.append(ltr.get("id", "unknown"))

    if unread:
        return False, (
            f"{len(unread)} of {count} patient messages are still unread: "
            f"{', '.join(unread)}."
        )

    return True, f"All {count} patient messages are now marked as read."
