import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    email = next((e for e in state["emails"] if e["subject"] == "Q1 Product Roadmap Review"), None)
    if not email:
        return False, "Email 'Q1 Product Roadmap Review' not found."

    if not email["isRead"]:
        return False, "Email 'Q1 Product Roadmap Review' is still unread."

    return True, "Email 'Q1 Product Roadmap Review' is marked as read."
