import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])

    target_email = None
    for email in emails:
        if email.get("isSent") is not True:
            continue
        subject = (email.get("subject") or "")
        subject_lower = subject.lower()
        has_fwd = "fwd:" in subject_lower or "fw:" in subject_lower
        has_quantum = "quantum error correction" in subject_lower
        if has_fwd and has_quantum:
            target_email = email
            break

    if not target_email:
        return False, "No sent email found with subject containing 'Fwd:' (or 'Fw:') and 'Quantum Error Correction'."

    to_list = target_email.get("to", [])
    to_emails = [
        (r.get("email", "") if isinstance(r, dict) else r).lower()
        for r in to_list
    ]

    if "sarah.chen@techcorp.io" not in to_emails:
        return False, f"Forwarded email 'to' field does not contain 'sarah.chen@techcorp.io'. Found: {to_list}"

    return True, "Task completed successfully."
