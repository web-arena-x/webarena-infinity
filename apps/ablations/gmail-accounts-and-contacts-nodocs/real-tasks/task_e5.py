import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    current_user = state.get("currentUser")
    if current_user is None:
        return False, "currentUser not found in application state."

    two_step = current_user.get("twoStepVerification")
    if two_step is False:
        return True, "2-Step Verification has been turned off."
    else:
        return False, f"2-Step Verification is still enabled. twoStepVerification={two_step}"
