import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the conversation with Aisha Patel about her prenatal visit is ended."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    letters = state.get("patientLetters", [])
    conv_letters = [ltr for ltr in letters if ltr.get("conversationId") == "conv_22"]

    if not conv_letters:
        return False, "No letters found with conversationId 'conv_22' (Aisha Patel prenatal conversation)"

    for ltr in conv_letters:
        conv_state = ltr.get("conversationState")
        if conv_state != "ended":
            return False, (
                f"Letter {ltr.get('id')} in conv_22 has conversationState '{conv_state}', expected 'ended'"
            )

    return True, "All letters in Aisha Patel's prenatal conversation (conv_22) have conversationState 'ended'"
