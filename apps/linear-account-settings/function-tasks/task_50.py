import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    passkeys = state.get("passkeys", [])

    has_old_name = any(p.get("name") == "MacBook Pro Touch ID" for p in passkeys)
    has_new_name = any(p.get("name") == "Work Laptop Touch ID" for p in passkeys)

    if has_old_name:
        return False, "Passkey 'MacBook Pro Touch ID' still exists (not renamed)."

    if not has_new_name:
        return False, "Passkey 'Work Laptop Touch ID' not found in passkeys."

    return True, "Passkey successfully renamed from 'MacBook Pro Touch ID' to 'Work Laptop Touch ID'."
