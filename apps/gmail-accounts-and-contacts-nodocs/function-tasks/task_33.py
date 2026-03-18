import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    current_user = state.get("currentUser", {})
    recovery_phone = current_user.get("recoveryPhone")

    if recovery_phone != "+1 (650) 555-0000":
        return False, f"Expected recoveryPhone '+1 (650) 555-0000', got '{recovery_phone}'."

    return True, "Recovery phone successfully changed to +1 (650) 555-0000."
