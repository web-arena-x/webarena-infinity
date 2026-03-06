import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    settings = state.get("invoiceSettings", {})
    prefix = settings.get("creditNotePrefix", "")
    if prefix != "CR-":
        return False, f"Credit note prefix is '{prefix}', expected 'CR-'."

    return True, "Credit note prefix changed to 'CR-'."
