import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = next((i for i in state["invoices"] if i["invoiceNumber"] == "INV-0093"), None)
    if not inv:
        return False, "Invoice INV-0093 not found."
    if inv["brandingThemeId"] != "theme_4":
        return False, f"Expected brandingThemeId 'theme_4' (Bold Corporate), got '{inv['brandingThemeId']}'"
    return True, "Invoice INV-0093 branding theme changed to Bold Corporate."
