import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    current_user = state.get("currentUser", {})
    first_name = current_user.get("firstName")
    last_name = current_user.get("lastName")

    if first_name != "Sara":
        return False, f"Expected firstName 'Sara', got '{first_name}'."
    if last_name != "Chen":
        return False, f"Expected lastName 'Chen', got '{last_name}'."

    return True, "First name successfully changed to Sara, last name remains Chen."
