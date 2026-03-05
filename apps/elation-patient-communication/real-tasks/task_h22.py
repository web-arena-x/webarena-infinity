import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Read Helen Matsumoto's son's message, add 'High Risk' tag, and reply."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Check ltr_10 is read
    letters = state.get("patientLetters", [])
    ltr_10 = next((l for l in letters if l.get("id") == "ltr_10"), None)
    if ltr_10 is None:
        return False, "Letter ltr_10 (Helen Matsumoto / son Ken) not found."
    if not ltr_10.get("isRead"):
        return False, "Helen Matsumoto's message (ltr_10) has not been marked as read."

    # Check High Risk tag on pat_10
    patients = state.get("patients", [])
    pat_10 = next((p for p in patients if p.get("id") == "pat_10"), None)
    if pat_10 is None:
        return False, "Patient pat_10 (Helen Matsumoto) not found."
    if "High Risk" not in pat_10.get("tags", []):
        return False, (
            f"Helen Matsumoto's tags are {pat_10.get('tags')}, "
            f"expected 'High Risk' to be present."
        )

    # Check reply in conv_7
    reply = next(
        (
            l for l in letters
            if l.get("conversationId") == "conv_7"
            and l.get("direction") == "to_patient"
            and l.get("patientId") == "pat_10"
        ),
        None,
    )
    if reply is None:
        return False, "No reply found in Helen Matsumoto's conversation (conv_7)."
    if reply.get("isDraft"):
        return False, "Reply to Helen Matsumoto is still a draft."

    return True, (
        "Helen Matsumoto's message read, 'High Risk' tag added, "
        "and reply sent."
    )
