import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    email = next(
        (e for e in emails if e["subject"] == "FY2026 Budget Summary"
         and e["from"]["name"] == "Priya Sharma"),
        None,
    )
    if email is None:
        return False, "Could not find email 'FY2026 Budget Summary' from Priya Sharma."

    if email.get("isStarred") is not False:
        return False, f"Email 'FY2026 Budget Summary' is still starred. isStarred={email.get('isStarred')}"

    return True, "Star removed from email 'FY2026 Budget Summary' from Priya Sharma."
