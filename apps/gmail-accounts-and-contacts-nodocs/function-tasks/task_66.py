import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    app_passwords = state.get("appPasswords", [])

    known = {"Thunderbird on MacBook", "Mail on iPhone", "Outlook Desktop"}
    remaining = [a for a in app_passwords if a.get("name") in known]

    if remaining:
        names = [a.get("name") for a in remaining]
        return False, f"Expected all app passwords revoked, but still found: {', '.join(names)}"

    return True, "All existing app passwords have been revoked."
