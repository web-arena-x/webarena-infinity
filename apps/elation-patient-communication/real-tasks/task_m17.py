import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    letters = state.get("patientLetters", [])
    conv_letters = [l for l in letters if l.get("conversationId") == "conv_8"]

    if not conv_letters:
        return False, "No letters found for conversation conv_8."

    for l in conv_letters:
        if l.get("conversationState") != "ended":
            return False, f"Letter {l.get('id')} in conv_8 has conversationState '{l.get('conversationState')}', expected 'ended'."

    return True, "Billing conversation with Kevin Adebayo has been ended."
