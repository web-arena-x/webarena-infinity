import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    sent_email = next(
        (e for e in emails
         if e.get("from", {}).get("email") == "alex.morgan@acmecorp.com"
         and e.get("subject") == "Team Sync"
         and any(r.get("email") == "sarah.chen@acmecorp.com" for r in e.get("to", []))),
        None,
    )
    if sent_email is None:
        return False, (
            "Could not find a sent email from alex.morgan@acmecorp.com "
            "with subject 'Team Sync' to sarah.chen@acmecorp.com."
        )

    if sent_email.get("isDraft") is True:
        return False, "Email 'Team Sync' is still a draft and has not been sent."

    return True, "Email 'Team Sync' sent to sarah.chen@acmecorp.com successfully."
