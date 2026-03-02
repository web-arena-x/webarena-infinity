import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    letters = state.get("patientLetters", [])
    conv_letters = [l for l in letters if l.get("conversationId") == "conv_24"]

    if not conv_letters:
        return False, "No letters found with conversationId 'conv_24' in patientLetters."

    for letter in conv_letters:
        if letter.get("conversationState") != "ended":
            return False, (
                f"Letter '{letter.get('id')}' in conversation conv_24 has "
                f"conversationState '{letter.get('conversationState')}', expected 'ended'."
            )

    return True, "Conversation with Howard Blackwell has been ended."
