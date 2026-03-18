import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Change settings: prefix RC-, next number 500, 5-digit padding, branding Minimal Clean, tax Zero Rated."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})

    errors = []

    prefix = settings.get("invoiceNumberPrefix")
    if prefix != "RC-":
        errors.append(f"invoiceNumberPrefix is '{prefix}', expected 'RC-'")

    next_number = settings.get("invoiceNumberNextNumber")
    if next_number != 500:
        errors.append(f"invoiceNumberNextNumber is {next_number}, expected 500")

    padding = settings.get("invoiceNumberPadding")
    if padding != 5:
        errors.append(f"invoiceNumberPadding is {padding}, expected 5")

    branding = settings.get("defaultBrandingThemeId")
    if branding != "theme_3":
        errors.append(f"defaultBrandingThemeId is '{branding}', expected 'theme_3' (Minimal Clean)")

    tax = settings.get("defaultTaxRateId")
    if tax != "tax_5":
        errors.append(f"defaultTaxRateId is '{tax}', expected 'tax_5' (Zero Rated)")

    if errors:
        return False, "; ".join(errors)

    return True, "All settings updated correctly: prefix=RC-, nextNumber=500, padding=5, branding=Minimal Clean, tax=Zero Rated"
