import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    email = next(
        (e for e in state["emails"] if e["subject"] == "Re: Platform Performance Issues"),
        None,
    )
    if not email:
        return False, "Email 'Re: Platform Performance Issues' not found."

    if not email["isStarred"]:
        return False, "Email 'Re: Platform Performance Issues' is not starred."

    return True, "Email 'Re: Platform Performance Issues' is starred."
