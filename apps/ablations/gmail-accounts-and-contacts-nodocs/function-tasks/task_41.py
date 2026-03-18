import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    aliases = state.get("aliases", [])

    support_alias = [a for a in aliases if a.get("email") == "support@techcorp.io"]
    if not support_alias:
        return False, "No alias found with email 'support@techcorp.io'."

    primary_alias = [a for a in aliases if a.get("email") == "sarah.chen@techcorp.io"]
    if not primary_alias:
        return False, "No alias found with email 'sarah.chen@techcorp.io'."

    errors = []
    if support_alias[0].get("isDefault") is not True:
        errors.append(f"Expected 'support@techcorp.io' isDefault to be true, got '{support_alias[0].get('isDefault')}'.")
    if primary_alias[0].get("isDefault") is not False:
        errors.append(f"Expected 'sarah.chen@techcorp.io' isDefault to be false, got '{primary_alias[0].get('isDefault')}'.")

    if errors:
        return False, " ".join(errors)

    return True, "Alias 'support@techcorp.io' successfully set as default."
