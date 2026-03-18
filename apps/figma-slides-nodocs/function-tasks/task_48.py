import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    comments = state.get("comments", [])
    for c in comments:
        if c.get("presentationId") == "pres_001" and "Canva" in c.get("content", ""):
            if c.get("resolved") is True:
                return True, "Comment about Canva on pres_001 is resolved."
            else:
                return False, f"Comment about Canva found on pres_001 but resolved is {c.get('resolved')}, expected True."

    return False, "Comment containing 'Canva' not found on pres_001."
