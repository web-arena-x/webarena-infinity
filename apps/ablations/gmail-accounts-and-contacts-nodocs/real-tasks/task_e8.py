import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    aliases = state.get("aliases", [])
    for a in aliases:
        if a.get("email") == "schen@alumni.stanford.edu":
            return False, "The Stanford alumni email alias (schen@alumni.stanford.edu) still exists."

    return True, "The Stanford alumni email alias has been successfully deleted."
