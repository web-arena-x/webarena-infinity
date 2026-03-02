import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    letters = state.get("patientLetters", [])
    matching = None
    for l in letters:
        if (
            l.get("patientId") == "pat_7"
            and l.get("direction") == "to_patient"
            and l.get("subject") == "Annual Flu Vaccine Reminder"
            and l.get("isDraft") is False
            and l.get("sentAt") is not None
        ):
            matching = l
            break

    if matching is None:
        return False, "No sent letter found to David Park (pat_7) with subject 'Annual Flu Vaccine Reminder'."

    return True, "Letter sent to David Park with subject 'Annual Flu Vaccine Reminder'."
