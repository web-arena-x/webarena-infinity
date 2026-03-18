import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    comments = state.get("comments", [])
    for c in comments:
        if c.get("presentationId") == "pres_003" and "Finance team confirmed" in c.get("content", ""):
            if c.get("resolved") is False:
                return True, "Comment 'Finance team confirmed...' on 'Series B Fundraising Pitch' is unresolved."
            else:
                return False, f"Comment 'Finance team confirmed...' found but resolved is {c.get('resolved')}, expected False."

    return False, "Comment containing 'Finance team confirmed' not found on pres_003."
