import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    import_accounts = state.get("importAccounts", [])
    for imp in import_accounts:
        if imp.get("email") == "sarah@old-startup.com":
            return False, "The POP3 import account for sarah@old-startup.com still exists."

    return True, "The POP3 import account for sarah@old-startup.com has been successfully removed."
