import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    import_accounts = state.get("importAccounts", [])

    for acc in import_accounts:
        if acc.get("email") == "sarah@old-startup.com":
            return False, "Import account with email 'sarah@old-startup.com' still exists. It should have been removed."

    return True, "Import account 'sarah@old-startup.com' has been successfully removed."
