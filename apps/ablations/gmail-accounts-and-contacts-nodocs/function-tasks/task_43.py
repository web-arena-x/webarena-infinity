import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    aliases = state.get("aliases", [])

    matching = [a for a in aliases if a.get("email") == "test@example.com"]
    if not matching:
        return False, "No alias found with email 'test@example.com'."

    alias = matching[0]
    if alias.get("useSSL") is not False:
        return False, f"Expected useSSL to be false, got '{alias.get('useSSL')}'."

    return True, "Alias 'test@example.com' successfully added with SSL disabled."
