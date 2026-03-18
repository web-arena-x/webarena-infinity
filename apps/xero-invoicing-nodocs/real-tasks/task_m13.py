import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Change the branding theme on draft invoice INV-0084 for Pinnacle Construction to Bold Corporate."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    invoices = state.get("invoices", [])
    target = None
    for inv in invoices:
        if inv.get("id") == "inv_84" or inv.get("invoiceNumber") == "INV-0084":
            target = inv
            break

    if target is None:
        return False, "Invoice INV-0084 not found in state"

    branding_theme_id = target.get("brandingThemeId")
    if branding_theme_id == "theme_4":
        return True, "Invoice INV-0084 branding theme has been changed to Bold Corporate (theme_4)"
    else:
        return False, f"Invoice INV-0084 brandingThemeId is '{branding_theme_id}', expected 'theme_4' (Bold Corporate)"
