import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    inv = None
    for i in state.get("invoices", []):
        if i.get("number") == "INV-0058":
            inv = i
            break

    if inv is None:
        return False, "Invoice INV-0058 not found."

    tax_mode = inv.get("taxMode", "")
    if tax_mode != "exclusive":
        return False, (
            f"INV-0058 taxMode is '{tax_mode}', expected 'exclusive' "
            f"(switched from tax-inclusive)."
        )

    theme_id = inv.get("brandingThemeId", "")
    if theme_id != "theme_professional":
        return False, (
            f"INV-0058 brandingThemeId is '{theme_id}', "
            f"expected 'theme_professional' (Professional Services)."
        )

    return True, (
        "INV-0058 (Murray River Winery) updated: tax mode changed to exclusive, "
        "branding theme changed to Professional Services."
    )
