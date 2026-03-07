import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    email = next(
        (e for e in emails
         if e["subject"] == "Complete Your Survey - Win a $500 Gift Card"),
        None,
    )
    if email is None:
        return False, "Could not find email 'Complete Your Survey - Win a $500 Gift Card'."

    if email.get("isTrashed") is not False:
        return False, (
            f"Email 'Complete Your Survey - Win a $500 Gift Card' is still in Trash. "
            f"isTrashed={email.get('isTrashed')}"
        )

    return True, "Email 'Complete Your Survey - Win a $500 Gift Card' moved back to Inbox from Trash."
