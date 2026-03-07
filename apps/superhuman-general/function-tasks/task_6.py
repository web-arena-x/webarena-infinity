import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    email = next(
        (e for e in emails if e["subject"] == "Re: Series B Term Sheet Discussion"
         and e["from"]["name"] == "Emily Rodriguez"),
        None,
    )
    if email is None:
        return False, "Could not find email 'Re: Series B Term Sheet Discussion' from Emily Rodriguez."

    if email.get("isTrashed") is not True:
        return False, f"Email 'Re: Series B Term Sheet Discussion' is not in Trash. isTrashed={email.get('isTrashed')}"

    return True, "Email 'Re: Series B Term Sheet Discussion' from Emily Rodriguez is moved to Trash."
