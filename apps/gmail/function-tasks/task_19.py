import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find a draft email with the expected subject
    draft_email = next(
        (e for e in state["emails"]
         if e["subject"] == "Budget Discussion"
         and e["isDraft"]
         and not e["isTrashed"]),
        None,
    )
    if not draft_email:
        return False, "Draft email with subject 'Budget Discussion' not found."

    # Check recipient
    recipients = [r["email"] for r in draft_email.get("to", [])]
    if "david.kim@financeplus.com" not in recipients:
        return False, f"Expected recipient 'david.kim@financeplus.com', got {recipients}."

    return True, "Draft email 'Budget Discussion' saved for david.kim@financeplus.com."
