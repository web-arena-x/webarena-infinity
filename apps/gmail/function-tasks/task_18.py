import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find a sent email with the expected subject
    sent_email = next(
        (e for e in state["emails"]
         if e["subject"] == "Meeting Follow-up"
         and e["isSent"]
         and not e["isTrashed"]),
        None,
    )
    if not sent_email:
        return False, "Sent email with subject 'Meeting Follow-up' not found."

    # Check recipient
    recipients = [r["email"] for r in sent_email.get("to", [])]
    if "sarah.chen@techcorp.io" not in recipients:
        return False, f"Expected recipient 'sarah.chen@techcorp.io', got {recipients}."

    return True, "Email 'Meeting Follow-up' sent to sarah.chen@techcorp.io."
