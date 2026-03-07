import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    email = next(
        (e for e in emails if e["subject"] == "Global Health Initiative - Sponsorship Request"
         and e["from"]["name"] == "Ana Gutierrez"),
        None,
    )
    if email is None:
        return False, "Could not find email 'Global Health Initiative - Sponsorship Request' from Ana Gutierrez."

    if email.get("isSpam") is not True:
        return False, f"Email 'Global Health Initiative - Sponsorship Request' is not marked as spam. isSpam={email.get('isSpam')}"

    return True, "Email 'Global Health Initiative - Sponsorship Request' from Ana Gutierrez is marked as spam."
