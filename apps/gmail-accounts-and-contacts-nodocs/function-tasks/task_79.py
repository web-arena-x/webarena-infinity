import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    imports = state.get("importAccounts", [])

    matching = [i for i in imports if i.get("email") == "sarah@consulting.dev"]
    if not matching:
        return False, "Import account 'sarah@consulting.dev' not found."

    imp = matching[0]
    errors = []

    if imp.get("server") != "pop.consulting.dev":
        errors.append(f"Expected server 'pop.consulting.dev', got '{imp.get('server')}'")
    if str(imp.get("port")) != "110":
        errors.append(f"Expected port '110', got '{imp.get('port')}'")
    if imp.get("username") != "sarah.consulting":
        errors.append(f"Expected username 'sarah.consulting', got '{imp.get('username')}'")
    if imp.get("useSSL") is not False:
        errors.append(f"Expected useSSL false, got '{imp.get('useSSL')}'")
    if imp.get("leaveOnServer") is not False:
        errors.append(f"Expected leaveOnServer false, got '{imp.get('leaveOnServer')}'")
    if imp.get("labelIncoming") != "consulting-work":
        errors.append(f"Expected labelIncoming 'consulting-work', got '{imp.get('labelIncoming')}'")

    if errors:
        return False, "; ".join(errors)

    return True, "Import account 'sarah@consulting.dev' added with correct settings."
