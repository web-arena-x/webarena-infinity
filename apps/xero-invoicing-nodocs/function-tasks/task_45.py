import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state["settings"]
    expected = "Invoice {InvoiceNumber} - Kiwi Consulting Group"
    if settings.get("defaultEmailSubject") != expected:
        return False, f"Expected subject '{expected}', got '{settings.get('defaultEmailSubject')}'"
    return True, "Email template subject updated correctly."
