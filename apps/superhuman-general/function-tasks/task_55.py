import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    for email in emails:
        if (email.get("subject") == "Re: Payment Terms Discussion" and
                "david.kim@financeplus.com" in str(email.get("from", ""))):
            remind_at = email.get("remindAt")
            if remind_at is None:
                return True, "Reminder cleared on 'Re: Payment Terms Discussion'."
            return False, f"Email 'Re: Payment Terms Discussion' still has remindAt={remind_at!r}; expected None."

    return False, "No email with subject 'Re: Payment Terms Discussion' from david.kim@financeplus.com found."
