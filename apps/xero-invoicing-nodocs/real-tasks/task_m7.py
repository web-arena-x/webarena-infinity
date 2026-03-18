import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Update the email template subject in settings to 'Invoice {InvoiceNumber} - Kiwi Consulting Group'."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})
    if not settings:
        return False, "Settings not found in state"

    subject = settings.get("defaultEmailSubject", "")
    if subject is None:
        subject = ""

    expected = "Invoice {InvoiceNumber} - Kiwi Consulting Group"

    if subject.strip() == expected:
        return True, f"Email template subject updated to '{expected}'"
    else:
        return False, f"defaultEmailSubject is '{subject}', expected '{expected}'"
