import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Check 1: 2-Step Verification is disabled
    current_user = state.get("currentUser", {})
    two_step = current_user.get("twoStepVerification")
    if two_step is not False:
        errors.append(
            f"2-Step Verification is {two_step}, expected False (disabled)."
        )

    # Check 2: All app passwords are revoked (list should be empty)
    app_passwords = state.get("appPasswords", [])
    if len(app_passwords) != 0:
        pw_names = [p.get("name", "unknown") for p in app_passwords]
        errors.append(
            f"App passwords still exist ({len(app_passwords)}): {', '.join(pw_names)}. "
            f"Expected all to be revoked."
        )

    # Check 3: The family email alias (sarah@chen-family.org) is removed
    aliases = state.get("aliases", [])
    family_alias = None
    for a in aliases:
        if a.get("email") == "sarah@chen-family.org":
            family_alias = a
            break

    if family_alias is not None:
        errors.append(
            f"Family email alias sarah@chen-family.org still exists "
            f"(name: '{family_alias.get('name', '')}')."
        )

    if errors:
        return False, " ".join(errors)

    return True, (
        "Security audit complete: 2-Step Verification is disabled, "
        "all app passwords are revoked, and the family email alias is removed."
    )
