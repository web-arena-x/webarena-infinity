import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    user = state.get("currentUser", {})
    errors = []

    if user.get("firstName") != "S.":
        errors.append(f"Expected firstName 'S.', got '{user.get('firstName')}'")
    if user.get("lastName") != "Chen":
        errors.append(f"Expected lastName 'Chen', got '{user.get('lastName')}'")

    if errors:
        return False, "; ".join(errors)

    return True, "Account name changed to 'S. Chen' correctly."
