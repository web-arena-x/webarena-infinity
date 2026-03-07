import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    email = next(
        (e for e in emails if e["subject"] == "Re: Infrastructure Migration Plan"
         and e["from"]["name"] == "Tom Bradley"),
        None,
    )
    if email is None:
        return False, "Could not find email 'Re: Infrastructure Migration Plan' from Tom Bradley."

    if email.get("isRead") is not False:
        return False, f"Email 'Re: Infrastructure Migration Plan' is not marked as unread. isRead={email.get('isRead')}"

    return True, "Email 'Re: Infrastructure Migration Plan' from Tom Bradley is marked as unread."
