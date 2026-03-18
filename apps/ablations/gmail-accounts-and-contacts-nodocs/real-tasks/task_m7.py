import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    app_passwords = state.get("appPasswords", [])

    # Find app password with name "Spark Email Client"
    target_name = "Spark Email Client"
    found = None
    for ap in app_passwords:
        if ap.get("name") == target_name:
            found = ap
            break

    if not found:
        return False, f"App password with name '{target_name}' not found in appPasswords."

    return True, f"App password '{target_name}' successfully generated."
