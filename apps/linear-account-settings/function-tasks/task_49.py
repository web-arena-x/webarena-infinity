import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    passkeys = state.get("passkeys", [])

    for passkey in passkeys:
        if passkey.get("name") == "Windows Hello":
            return True, "Passkey 'Windows Hello' exists in passkeys."

    return False, "Passkey 'Windows Hello' not found in passkeys."
