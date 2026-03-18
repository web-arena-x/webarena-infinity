import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    aliases = state.get("aliases", [])

    # Find alias with the target email
    target_email = "sarah.personal@protonmail.com"
    alias = None
    for a in aliases:
        if a.get("email") == target_email:
            alias = a
            break

    if not alias:
        return False, f"Alias with email '{target_email}' not found."

    # Verify name
    if alias.get("name") != "Sarah Chen (Personal)":
        return False, f"Expected alias name 'Sarah Chen (Personal)', got '{alias.get('name')}'."

    # Verify SMTP server
    if alias.get("smtpServer") != "smtp.protonmail.com":
        return False, f"Expected smtpServer 'smtp.protonmail.com', got '{alias.get('smtpServer')}'."

    # Verify SMTP port (check both string and int)
    smtp_port = alias.get("smtpPort")
    if str(smtp_port) != "587":
        return False, f"Expected smtpPort '587', got '{smtp_port}'."

    # Verify SMTP username
    if alias.get("smtpUsername") != "sarah.personal@protonmail.com":
        return False, f"Expected smtpUsername 'sarah.personal@protonmail.com', got '{alias.get('smtpUsername')}'."

    # Verify SSL
    if alias.get("useSSL") is not True:
        return False, f"Expected useSSL to be True, got '{alias.get('useSSL')}'."

    return True, "Email alias 'Sarah Chen (Personal)' created correctly with all SMTP settings."
