import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    email = next(
        (e for e in emails if e["subject"] == "Budget Approval Needed - Marketing Campaign"),
        None,
    )
    if email is None:
        return False, "Could not find email 'Budget Approval Needed - Marketing Campaign'."

    if email.get("isDone") is not True:
        return False, f"Email 'Budget Approval Needed - Marketing Campaign' is not marked as done. isDone={email.get('isDone')}"

    return True, "Email 'Budget Approval Needed - Marketing Campaign' is marked as done."
