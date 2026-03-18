import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    presentations = state.get("presentations", [])
    match = [p for p in presentations if p.get("title") == "Annual Company All-Hands 2026"]
    if not match:
        return False, "No presentation found with title 'Annual Company All-Hands 2026'."

    pres = match[0]
    allow_comments = pres.get("shareSettings", {}).get("allowComments")
    if allow_comments is not False:
        return False, f"Expected shareSettings.allowComments to be false, got {allow_comments}."

    return True, "Commenting disabled on 'Annual Company All-Hands 2026'."
