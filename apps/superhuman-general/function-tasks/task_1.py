import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    email = next(
        (e for e in emails if e["subject"] == "Q2 Product Roadmap - Final Review"
         and e["from"]["name"] == "Sarah Chen"),
        None,
    )
    if email is None:
        return False, "Could not find email 'Q2 Product Roadmap - Final Review' from Sarah Chen."

    if email.get("isRead") is not True:
        return False, f"Email 'Q2 Product Roadmap - Final Review' is not marked as read. isRead={email.get('isRead')}"

    return True, "Email 'Q2 Product Roadmap - Final Review' from Sarah Chen is marked as read."
