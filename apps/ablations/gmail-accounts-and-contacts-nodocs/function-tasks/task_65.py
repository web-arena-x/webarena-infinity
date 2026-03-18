import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    app_passwords = state.get("appPasswords", [])

    spark = [a for a in app_passwords if a.get("name") == "Spark Mac Client"]
    k9 = [a for a in app_passwords if a.get("name") == "K-9 Mail Android"]

    errors = []
    if not spark:
        errors.append("App password 'Spark Mac Client' not found")
    if not k9:
        errors.append("App password 'K-9 Mail Android' not found")

    if errors:
        return False, "; ".join(errors)

    return True, "Both app passwords 'Spark Mac Client' and 'K-9 Mail Android' created."
