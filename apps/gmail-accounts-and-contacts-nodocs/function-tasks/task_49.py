import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    import_accounts = state.get("importAccounts", [])

    for acc in import_accounts:
        if acc.get("email") == "sarah@personal-blog.com":
            errors = []
            if acc.get("server") != "pop.personal-blog.com":
                errors.append(f"server is '{acc.get('server')}', expected 'pop.personal-blog.com'")
            if str(acc.get("port")) != "995":
                errors.append(f"port is '{acc.get('port')}', expected '995'")
            if acc.get("username") != "sarah":
                errors.append(f"username is '{acc.get('username')}', expected 'sarah'")
            if acc.get("labelIncoming") != "blog":
                errors.append(f"labelIncoming is '{acc.get('labelIncoming')}', expected 'blog'")
            if acc.get("useSSL") is not True:
                errors.append(f"useSSL is {acc.get('useSSL')}, expected True")
            if acc.get("leaveOnServer") is not True:
                errors.append(f"leaveOnServer is {acc.get('leaveOnServer')}, expected True")

            if errors:
                return False, "Import account 'sarah@personal-blog.com' found but has issues: " + "; ".join(errors)
            return True, "Import account 'sarah@personal-blog.com' exists with correct settings."

    return False, "No import account found with email 'sarah@personal-blog.com'."
