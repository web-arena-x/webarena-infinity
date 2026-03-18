import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Change the default email body in settings."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})
    if not settings:
        return False, "No settings found in state"

    email_body = settings.get("defaultEmailBody", "")
    if not email_body:
        return False, "settings.defaultEmailBody is empty or missing"

    required_tokens = [
        "{ContactName}",
        "Kiwi Consulting Group",
        "{InvoiceNumber}",
        "{Total}",
        "{DueDate}",
    ]

    missing = []
    for token in required_tokens:
        if token not in email_body:
            missing.append(token)

    if missing:
        return False, f"defaultEmailBody is missing required content: {missing}. Current body: {email_body!r}"

    return True, "Default email body contains all required tokens: {ContactName}, Kiwi Consulting Group, {InvoiceNumber}, {Total}, {DueDate}"
