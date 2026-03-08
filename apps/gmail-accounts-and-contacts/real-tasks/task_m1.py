# Task: Update profile name to 'Alexander Johnson' and recovery email to 'alex.secure@proton.me'.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    current_user = state.get("currentUser", {})
    name = current_user.get("name")
    if name != "Alexander Johnson":
        errors.append(f"Expected currentUser.name to be 'Alexander Johnson', got '{name}'")

    recovery_email = current_user.get("recoveryEmail")
    if recovery_email != "alex.secure@proton.me":
        errors.append(f"Expected currentUser.recoveryEmail to be 'alex.secure@proton.me', got '{recovery_email}'")

    if errors:
        return False, "; ".join(errors)
    return True, "Profile name updated to 'Alexander Johnson' and recovery email updated to 'alex.secure@proton.me'."
