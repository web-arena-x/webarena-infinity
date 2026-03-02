import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    letters = state.get("patientLetters", [])
    conv_letters = [l for l in letters if l.get("conversationId") == "conv_1"]

    if not conv_letters:
        return False, "No letters found for conversation conv_1."

    to_patient_letters = [l for l in conv_letters if l.get("direction") == "to_patient"]

    if len(to_patient_letters) < 2:
        return False, f"Expected at least 2 to_patient letters in conv_1, found {len(to_patient_letters)}."

    new_replies = [l for l in to_patient_letters if l.get("id") != "ltr_2"]

    if not new_replies:
        return False, "No new reply letter found in conv_1 (only the original ltr_2 exists)."

    newest_reply = new_replies[-1]

    if newest_reply.get("isDraft") is True:
        return False, "The reply letter is still a draft and has not been sent."

    return True, "Reply sent to James Rodriguez about Lisinopril refill."
