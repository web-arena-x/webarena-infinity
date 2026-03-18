import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    import_accounts = state.get("importAccounts", [])

    # Find import account with target email
    target_email = "sarah@side-project.io"
    account = None
    for ia in import_accounts:
        if ia.get("email") == target_email:
            account = ia
            break

    if not account:
        return False, f"Import account with email '{target_email}' not found."

    # Verify server
    if account.get("server") != "pop.side-project.io":
        return False, f"Expected server 'pop.side-project.io', got '{account.get('server')}'."

    # Verify port (check both string and int)
    port = account.get("port")
    if str(port) != "995":
        return False, f"Expected port '995', got '{port}'."

    # Verify username
    if account.get("username") != "sarah":
        return False, f"Expected username 'sarah', got '{account.get('username')}'."

    # Verify SSL
    if account.get("useSSL") is not True:
        return False, f"Expected useSSL to be True, got '{account.get('useSSL')}'."

    # Verify leave on server
    if account.get("leaveOnServer") is not True:
        return False, f"Expected leaveOnServer to be True, got '{account.get('leaveOnServer')}'."

    # Verify label incoming
    if account.get("labelIncoming") != "side-project":
        return False, f"Expected labelIncoming 'side-project', got '{account.get('labelIncoming')}'."

    return True, "POP3 import account for 'sarah@side-project.io' configured correctly with all settings."
