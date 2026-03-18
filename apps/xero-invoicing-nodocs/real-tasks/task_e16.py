import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Set the next invoice number to 200 in settings."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})
    next_num = settings.get("invoiceNumberNextNumber")

    if next_num == 200:
        return True, "Invoice number next number is set to 200"
    else:
        return False, f"settings.invoiceNumberNextNumber is {next_num!r}, expected 200"
