import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the '1Password' passkey was removed."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    passkeys = state.get("passkeys", [])

    one_password = [p for p in passkeys if p.get("name") == "1Password"]
    if one_password:
        return False, "Passkey '1Password' still exists."

    # Ensure at least one passkey remains (MacBook Pro Touch ID)
    if len(passkeys) < 1:
        return False, "All passkeys were removed, expected at least one to remain."

    return True, "Passkey '1Password' successfully removed."
