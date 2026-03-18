import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    current_user = state.get("currentUser", {})
    recovery_phone = current_user.get("recoveryPhone", "")

    if recovery_phone == "+1 (650) 555-0300":
        return True, (
            "Account recovery phone number has been successfully updated "
            "to +1 (650) 555-0300."
        )

    return False, (
        f"Account recovery phone number is '{recovery_phone}', "
        f"but expected '+1 (650) 555-0300'."
    )
