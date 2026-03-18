import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    user = state.get("currentUser", {})
    errors = []

    if user.get("recoveryEmail") != "sarah.chen.recovery@outlook.com":
        errors.append(f"Expected recoveryEmail 'sarah.chen.recovery@outlook.com', got '{user.get('recoveryEmail')}'")
    if user.get("recoveryPhone") != "+1 (510) 555-0100":
        errors.append(f"Expected recoveryPhone '+1 (510) 555-0100', got '{user.get('recoveryPhone')}'")

    if errors:
        return False, "; ".join(errors)

    return True, "Recovery email and phone updated correctly."
