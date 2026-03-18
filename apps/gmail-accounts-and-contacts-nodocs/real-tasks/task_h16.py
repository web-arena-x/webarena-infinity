import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    current_user = state.get("currentUser", {})
    aliases = state.get("aliases", [])

    # Verify account name changed to S. Chen
    errors = []
    if current_user.get("firstName") != "S.":
        errors.append(
            f"Expected currentUser.firstName 'S.', got '{current_user.get('firstName')}'."
        )
    if current_user.get("lastName") != "Chen":
        errors.append(
            f"Expected currentUser.lastName 'Chen', got '{current_user.get('lastName')}'."
        )

    # Verify recovery email changed
    if current_user.get("recoveryEmail") != "s.chen.recovery@gmail.com":
        errors.append(
            f"Expected recoveryEmail 's.chen.recovery@gmail.com', "
            f"got '{current_user.get('recoveryEmail')}'."
        )

    # Find the support alias and verify its name
    support_alias = None
    for a in aliases:
        if a.get("email") == "support@techcorp.io":
            support_alias = a
            break

    if support_alias is None:
        errors.append("Alias with email 'support@techcorp.io' not found.")
    elif support_alias.get("name") != "S. Chen (Support)":
        errors.append(
            f"Expected support alias name 'S. Chen (Support)', "
            f"got '{support_alias.get('name')}'."
        )

    if errors:
        return False, " ".join(errors)

    return True, (
        "Account name updated to 'S. Chen', recovery email changed to "
        "'s.chen.recovery@gmail.com', and support alias renamed to "
        "'S. Chen (Support)'."
    )
