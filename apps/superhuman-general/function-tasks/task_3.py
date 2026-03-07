import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    email = next(
        (e for e in emails if e["subject"] == "Partnership Opportunity - FinancePlus x Acme"
         and e["from"]["name"] == "David Kim"),
        None,
    )
    if email is None:
        return False, "Could not find email 'Partnership Opportunity - FinancePlus x Acme' from David Kim."

    if email.get("isStarred") is not True:
        return False, f"Email 'Partnership Opportunity - FinancePlus x Acme' is not starred. isStarred={email.get('isStarred')}"

    return True, "Email 'Partnership Opportunity - FinancePlus x Acme' from David Kim is starred."
