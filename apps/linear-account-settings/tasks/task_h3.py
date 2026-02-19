import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify a passkey named 'YubiKey 5C' was registered with cross-platform type."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    passkeys = state.get("passkeys", [])

    yubikey = [p for p in passkeys if p.get("name") == "YubiKey 5C"]
    if not yubikey:
        return False, "Passkey 'YubiKey 5C' not found."

    pk = yubikey[0]
    if pk.get("deviceType") != "cross-platform":
        return False, f"Expected deviceType='cross-platform', got '{pk.get('deviceType')}'."

    return True, "Passkey 'YubiKey 5C' successfully registered with cross-platform type."
