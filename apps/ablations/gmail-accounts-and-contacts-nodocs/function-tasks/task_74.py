import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    aliases = state.get("aliases", [])

    matching = [a for a in aliases if a.get("email") == "sarah@chen-family.org"]
    if not matching:
        return False, "Alias 'sarah@chen-family.org' not found."

    alias = matching[0]
    if alias.get("name") != "Sarah (Family)":
        return False, f"Expected display name 'Sarah (Family)', got '{alias.get('name')}'."

    return True, "Alias 'sarah@chen-family.org' display name changed to 'Sarah (Family)'."
