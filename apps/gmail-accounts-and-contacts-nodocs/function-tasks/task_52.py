import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    import_accounts = state.get("importAccounts", [])

    for acc in import_accounts:
        if acc.get("email") == "archive@company.com":
            errors = []
            if acc.get("server") != "pop.company.com":
                errors.append(f"server is '{acc.get('server')}', expected 'pop.company.com'")
            if str(acc.get("port")) != "110":
                errors.append(f"port is '{acc.get('port')}', expected '110'")
            if acc.get("useSSL") is not False:
                errors.append(f"useSSL is {acc.get('useSSL')}, expected False")
            if acc.get("leaveOnServer") is not False:
                errors.append(f"leaveOnServer is {acc.get('leaveOnServer')}, expected False")

            if errors:
                return False, "Import account 'archive@company.com' found but has issues: " + "; ".join(errors)
            return True, "Import account 'archive@company.com' exists with correct settings."

    return False, "No import account found with email 'archive@company.com'."
