import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    current_user = state.get("currentUser", {})
    two_step = current_user.get("twoStepVerification")

    if two_step is not False:
        return False, f"Expected twoStepVerification to be false, got '{two_step}'."

    return True, "2-Step Verification successfully disabled."
