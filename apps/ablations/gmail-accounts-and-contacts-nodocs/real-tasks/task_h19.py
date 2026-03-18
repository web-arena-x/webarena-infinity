import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    import_accounts = state.get("importAccounts", [])

    # Find the new import account
    new_import = None
    for imp in import_accounts:
        if imp.get("email") == "sarah@consulting-gig.com":
            new_import = imp
            break

    if new_import is None:
        return False, "Import account with email 'sarah@consulting-gig.com' not found."

    # Verify fields
    errors = []
    if new_import.get("server") != "pop.consulting-gig.com":
        errors.append(
            f"Expected server 'pop.consulting-gig.com', got '{new_import.get('server')}'."
        )
    if str(new_import.get("port")) != "110":
        errors.append(
            f"Expected port '110', got '{new_import.get('port')}'."
        )
    if new_import.get("username") != "sarah":
        errors.append(
            f"Expected username 'sarah', got '{new_import.get('username')}'."
        )
    if new_import.get("useSSL") is not False:
        errors.append(
            f"Expected useSSL to be False, got '{new_import.get('useSSL')}'."
        )
    if new_import.get("leaveOnServer") is not False:
        errors.append(
            f"Expected leaveOnServer to be False, got '{new_import.get('leaveOnServer')}'."
        )
    if new_import.get("labelIncoming") != "consulting":
        errors.append(
            f"Expected labelIncoming 'consulting', got '{new_import.get('labelIncoming')}'."
        )

    if errors:
        return False, " ".join(errors)

    # Verify the errored import account (sarah@old-startup.com) is removed
    for imp in import_accounts:
        if imp.get("email") == "sarah@old-startup.com":
            return False, (
                "Import account 'sarah@old-startup.com' (errored) still exists. "
                "It should have been removed."
            )

    return True, (
        "New POP3 import for sarah@consulting-gig.com created with correct settings. "
        "Errored import account sarah@old-startup.com has been removed."
    )
