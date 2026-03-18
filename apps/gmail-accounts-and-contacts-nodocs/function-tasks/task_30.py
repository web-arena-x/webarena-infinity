import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    current_user = state.get("currentUser", {})
    first_name = current_user.get("firstName")
    last_name = current_user.get("lastName")

    if first_name != "Sarah":
        return False, f"Expected firstName 'Sarah', got '{first_name}'."
    if last_name != "Chen-Williams":
        return False, f"Expected lastName 'Chen-Williams', got '{last_name}'."

    return True, "Account name successfully changed to Sarah Chen-Williams."
