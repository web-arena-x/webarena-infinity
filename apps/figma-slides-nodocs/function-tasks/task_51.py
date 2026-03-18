import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    comments = state.get("comments", [])
    for c in comments:
        if c.get("presentationId") == "pres_002" and "logo clear space" in c.get("content", "").lower():
            if c.get("resolved") is True:
                return True, "Comment about logo clear space on 'Brand Identity Guidelines v2.0' is resolved."
            else:
                return False, f"Comment about logo clear space found but resolved is {c.get('resolved')}, expected True."

    return False, "Comment containing 'logo clear space' not found on pres_002."
