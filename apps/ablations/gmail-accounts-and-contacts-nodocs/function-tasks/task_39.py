import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    aliases = state.get("aliases", [])

    matching = [a for a in aliases if a.get("email") == "support@techcorp.io"]
    if not matching:
        return False, "No alias found with email 'support@techcorp.io'."

    alias = matching[0]
    if alias.get("name") != "TechCorp Support":
        return False, f"Expected alias name 'TechCorp Support', got '{alias.get('name')}'."

    return True, "Alias 'support@techcorp.io' name successfully changed to 'TechCorp Support'."
