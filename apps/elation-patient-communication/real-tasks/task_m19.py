import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that Maria Gonzalez's lab results conversation has been ended (signed off)."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    letters = state.get("patientLetters", [])
    conv_letters = [ltr for ltr in letters if ltr.get("conversationId") == "conv_9"]

    if not conv_letters:
        return False, "No letters found with conversationId 'conv_9' (Maria Gonzalez lab results)"

    for ltr in conv_letters:
        conv_state = ltr.get("conversationState")
        if conv_state != "ended":
            return False, (
                f"Letter {ltr.get('id')} in conv_9 has conversationState '{conv_state}', expected 'ended'"
            )

    return True, "All letters in Maria Gonzalez's lab results conversation (conv_9) have conversationState 'ended'"
