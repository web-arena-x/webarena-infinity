import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify reply in conv_20, conversation ended, and rem_2 acknowledged."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    seed_letter_ids = {f"ltr_{i}" for i in range(1, 48)}
    errors = []

    # Check for new reply in conv_20
    conv_20_letters = [
        ltr for ltr in state.get("patientLetters", [])
        if ltr.get("conversationId") == "conv_20"
    ]

    has_reply = False
    for ltr in conv_20_letters:
        if (ltr.get("id") not in seed_letter_ids
                and ltr.get("direction") == "to_patient"
                and not ltr.get("isDraft", False)):
            has_reply = True
            break

    if not has_reply:
        errors.append("No new reply found in conv_20 (Frank DeLuca's Tamsulosin question)")

    # Check conversation ended
    not_ended = []
    for ltr in conv_20_letters:
        if ltr.get("conversationState") != "ended":
            not_ended.append(ltr.get("id"))
    if not_ended:
        errors.append(f"conv_20 not fully ended. Letters without 'ended': {', '.join(not_ended)}")

    # Check rem_2 acknowledged
    rem_2 = None
    for rem in state.get("reminders", []):
        if rem.get("id") == "rem_2":
            rem_2 = rem
            break

    if rem_2 is None:
        errors.append("Reminder rem_2 not found")
    elif not rem_2.get("acknowledged"):
        errors.append("rem_2 (Frank DeLuca PSA unread alert) not acknowledged")

    if errors:
        return False, "; ".join(errors)
    return True, "Reply sent in conv_20, conversation ended, and rem_2 acknowledged"
