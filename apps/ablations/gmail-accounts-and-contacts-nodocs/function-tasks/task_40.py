import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    aliases = state.get("aliases", [])

    matching = [a for a in aliases if a.get("email") == "schen@alumni.stanford.edu"]
    if matching:
        return False, "Alias with email 'schen@alumni.stanford.edu' still exists. Expected it to be deleted."

    return True, "Alias 'schen@alumni.stanford.edu' successfully deleted."
