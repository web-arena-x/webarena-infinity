import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    passkeys = state.get("passkeys", [])

    for passkey in passkeys:
        if passkey.get("name") == "YubiKey 5C NFC":
            return False, "Passkey 'YubiKey 5C NFC' still exists in passkeys."

    return True, "Passkey 'YubiKey 5C NFC' has been removed."
