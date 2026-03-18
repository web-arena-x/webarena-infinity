import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    aliases = state.get("aliases", [])

    # Find alias with target email
    target_email = "support@techcorp.io"
    alias = None
    for a in aliases:
        if a.get("email") == target_email:
            alias = a
            break

    if not alias:
        return False, f"Alias with email '{target_email}' not found."

    # Verify updated display name
    if alias.get("name") != "TechCorp Support Team":
        return False, f"Expected alias name 'TechCorp Support Team', got '{alias.get('name')}'."

    return True, "Alias 'support@techcorp.io' display name updated to 'TechCorp Support Team'."
