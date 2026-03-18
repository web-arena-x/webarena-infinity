import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})

    sig_required = settings.get("signatureRequired")
    if sig_required is not False:
        return False, f"signatureRequired is {sig_required}, expected False."

    return True, "Require signature has been disabled (signatureRequired is False)."
