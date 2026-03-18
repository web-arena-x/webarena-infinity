import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    current_user = state.get("currentUser", {})
    last_name = current_user.get("lastName", "")
    first_name = current_user.get("firstName", "")

    errors = []

    if last_name != "Chen-Williams":
        errors.append(
            f"Account last name is '{last_name}', but expected 'Chen-Williams'."
        )

    if first_name != "Sarah":
        errors.append(
            f"Account first name was changed to '{first_name}', but it should "
            f"still be 'Sarah'."
        )

    if errors:
        return False, " ".join(errors)

    return True, (
        "Account last name has been successfully changed to 'Chen-Williams' "
        "and first name remains 'Sarah'."
    )
