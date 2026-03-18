import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    aliases = state.get("aliases", [])

    matching = [a for a in aliases if a.get("email") == "sarah.personal@gmail.com"]
    if not matching:
        return False, "No alias found with email 'sarah.personal@gmail.com'."

    alias = matching[0]
    errors = []

    if alias.get("name") != "Sarah Chen (Personal)":
        errors.append(f"Expected name 'Sarah Chen (Personal)', got '{alias.get('name')}'.")
    if alias.get("smtpServer") != "smtp.gmail.com":
        errors.append(f"Expected smtpServer 'smtp.gmail.com', got '{alias.get('smtpServer')}'.")
    if str(alias.get("smtpPort")) != "587":
        errors.append(f"Expected smtpPort '587', got '{alias.get('smtpPort')}'.")
    if alias.get("smtpUsername") != "sarah.personal@gmail.com":
        errors.append(f"Expected smtpUsername 'sarah.personal@gmail.com', got '{alias.get('smtpUsername')}'.")
    if alias.get("useSSL") is not True:
        errors.append(f"Expected useSSL to be true, got '{alias.get('useSSL')}'.")

    if errors:
        return False, " ".join(errors)

    return True, "Alias 'sarah.personal@gmail.com' successfully added with all correct fields."
