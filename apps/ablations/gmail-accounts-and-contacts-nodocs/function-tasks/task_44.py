import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    aliases = state.get("aliases", [])

    matching = [a for a in aliases if a.get("email") == "sarah@chen-family.org"]
    if matching:
        return False, "Alias with email 'sarah@chen-family.org' still exists. Expected it to be deleted."

    return True, "Alias 'sarah@chen-family.org' successfully deleted."
