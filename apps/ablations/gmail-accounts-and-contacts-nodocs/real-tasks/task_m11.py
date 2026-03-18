import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    current_user = state.get("currentUser", {})

    recovery_email = current_user.get("recoveryEmail")
    recovery_phone = current_user.get("recoveryPhone")

    errors = []

    if recovery_email != "sarah.backup@protonmail.com":
        errors.append(
            f"Expected recoveryEmail='sarah.backup@protonmail.com', got '{recovery_email}'."
        )

    if recovery_phone != "+1 (510) 555-0199":
        errors.append(
            f"Expected recoveryPhone='+1 (510) 555-0199', got '{recovery_phone}'."
        )

    if errors:
        return False, " ".join(errors)

    return True, "Recovery email updated to sarah.backup@protonmail.com and recovery phone updated to +1 (510) 555-0199."
