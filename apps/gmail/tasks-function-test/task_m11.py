import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    emails = state.get("emails", [])
    for email in emails:
        if email.get("subject") == "Re: Conference Talk Proposal" and email.get("isDraft") is True:
            return False, (
                "Draft email with subject 'Re: Conference Talk Proposal' still exists. "
                "It should have been discarded."
            )

    return True, "Task completed successfully."
