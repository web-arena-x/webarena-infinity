import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    current_user = state.get("currentUser", {})
    recovery_email = current_user.get("recoveryEmail")

    if recovery_email != "sarah.backup@protonmail.com":
        return False, f"Expected recoveryEmail 'sarah.backup@protonmail.com', got '{recovery_email}'."

    return True, "Recovery email successfully changed to sarah.backup@protonmail.com."
