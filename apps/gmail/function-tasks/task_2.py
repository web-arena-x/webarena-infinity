import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    email = next(
        (e for e in state["emails"] if e["subject"] == "Monthly Financial Report - January 2026"),
        None,
    )
    if not email:
        return False, "Email 'Monthly Financial Report - January 2026' not found."

    if email["isRead"]:
        return False, "Email 'Monthly Financial Report - January 2026' is still marked as read."

    return True, "Email 'Monthly Financial Report - January 2026' is marked as unread."
