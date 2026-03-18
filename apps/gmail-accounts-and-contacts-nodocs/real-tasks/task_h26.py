import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify personal email change: recovery email, old import removed, new import added."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    current_user = state.get("currentUser", {})
    import_accounts = state.get("importAccounts", [])

    # Check recovery email updated
    recovery = current_user.get("recoveryEmail", "")
    if recovery != "sarah.chen.new@protonmail.com":
        return False, (
            f"Recovery email should be 'sarah.chen.new@protonmail.com', "
            f"got {recovery!r}."
        )

    # Check old Gmail import removed
    for imp in import_accounts:
        if imp.get("email") == "sarahchen.personal@gmail.com":
            return False, (
                "Old POP3 import for sarahchen.personal@gmail.com should "
                "have been removed."
            )

    # Check new Protonmail import exists
    new_import = None
    for imp in import_accounts:
        if imp.get("email") == "sarah.chen.new@protonmail.com":
            new_import = imp
            break

    if new_import is None:
        return False, (
            "New POP3 import for sarah.chen.new@protonmail.com not found."
        )

    # Verify import settings
    errors = []
    if new_import.get("server") != "pop.protonmail.com":
        errors.append(
            f"server should be 'pop.protonmail.com', "
            f"got {new_import.get('server')!r}"
        )
    if str(new_import.get("port", "")) != "993":
        errors.append(
            f"port should be '993', got {new_import.get('port')!r}"
        )
    if new_import.get("username") != "sarah.chen.new":
        errors.append(
            f"username should be 'sarah.chen.new', "
            f"got {new_import.get('username')!r}"
        )
    if not new_import.get("useSSL"):
        errors.append("SSL should be enabled")
    if not new_import.get("leaveOnServer"):
        errors.append("leaveOnServer should be true")
    if new_import.get("labelIncoming") != "personal":
        errors.append(
            f"label should be 'personal', "
            f"got {new_import.get('labelIncoming')!r}"
        )

    if errors:
        return False, "Import settings incorrect: " + "; ".join(errors) + "."

    return True, (
        "Personal email change complete: recovery email updated, "
        "old Gmail import removed, new Protonmail import added."
    )
