import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    aliases = state.get("aliases", [])

    matching = [a for a in aliases if a.get("email") == "support@techcorp.io"]
    if not matching:
        return False, "Alias 'support@techcorp.io' not found."

    alias = matching[0]
    errors = []

    if str(alias.get("smtpPort")) != "465":
        errors.append(f"Expected smtpPort '465', got '{alias.get('smtpPort')}'")
    if alias.get("smtpUsername") != "support-admin@techcorp.io":
        errors.append(f"Expected smtpUsername 'support-admin@techcorp.io', got '{alias.get('smtpUsername')}'")

    if errors:
        return False, "; ".join(errors)

    return True, "Alias 'support@techcorp.io' SMTP port and username updated correctly."
